# -*- coding: utf-8 -*-
"""
hibrido.py — Sistema híbrido H-NIDS: cascada anomalías → firmas (sección 5.3).

Combina las dos etapas ya entrenadas y persistidas por `anomalias.py` y `firmas.py`
y las evalúa de extremo a extremo sobre D2. NO re-entrena: carga los `.joblib`
auditados (una sola fuente de verdad; las métricas cuadran con 5.1/5.2). Lo único
que reconstruye es el estimador de firmas —desde su config guardada— para obtener
probabilidades OUT-OF-FOLD sobre D3 y calibrar con ellas `UMBRAL_CONF` sin leakage.

Cascada (H-2/H-3):
  etapa 1  score = anomaly_score(detector, X_D2);  es_sospechoso = score > umbral
  etapa 2  sobre los sospechosos: proba = firma.predict_proba(X);  categoría = argmax
           si max(proba) < UMBRAL_CONF → 'unknown' (ataque desconocido / 0-day)
  no sospechoso → 'normal'
  Detector por defecto = Autoencoder (mejor en 5.1); firma por defecto = RandomForest
  (mejor en 54 y con predict_proba suave: base fina para un umbral de confianza).

Reglas de protocolo (invalidan el TFG si se rompen):
  * LÍNEA ROJA (H-4/P-4): `UMBRAL_CONF` se SELECCIONA sobre probabilidades OOF de D3
    (nunca sobre D2). La función de calibración ni siquiera recibe D2 en su firma.
    D2 se usa SOLO para reportar (tabla de sensibilidad). Elegir el umbral por su
    resultado en D2 sería leakage.
  * D1 no se carga (P-3): el detector y su umbral llegan ya entrenados del joblib.
  * random_state=42 en todo; mismo StratifiedKFold(5) que firmas.py para el OOF (Q4).

Decisiones: resumen-de-decisiones.md § 2026-07-14 (H-1…H-7 + P-1…P-5).
"""
import argparse
import time

# Backend no interactivo fijado ANTES de cualquier import que arrastre matplotlib
# (evaluacion/anomalias/firmas/program). Así nada bloquea ni abre ventanas.
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

import numpy as np
import pandas as pd
import joblib

from sklearn.model_selection import StratifiedKFold, cross_val_predict

import config
import evaluacion  # importado pronto: reafirma el backend Agg de matplotlib
from anomalias import NSLKDDAnomalyTrainer
from firmas import NSLKDDSignatureTrainer
from program import load_specialized_splits


class NSLKDDHybridEvaluator:
    """
    Evalúa el sistema híbrido en cascada sobre D2 y calibra `UMBRAL_CONF` con OOF de D3.

    Mismo estilo clase-por-script que el resto del pipeline. No re-entrena modelos:
    orquesta carga de joblibs, calibración sin leakage, cascada y reporte por alcance.
    """

    DETECTORES = ["IsolationForest", "OneClassSVM", "LocalOutlierFactor", "Autoencoder"]
    FIRMAS = ["DecisionTree", "RandomForest", "KNN", "HistGradientBoosting"]

    # Rango a explorar (Q4) y presupuesto de caída de recall macro OOF (H-4).
    UMBRALES_CONF = [0.4, 0.5, 0.6]
    TAU = 0.02  # 2 pp: caída máxima tolerada del recall macro OOF de clases conocidas.

    def __init__(self, sin_seleccion=False, detector="Autoencoder", firma="RandomForest"):
        if detector not in self.DETECTORES:
            raise ValueError("Detector desconocido: " + str(detector))
        if firma not in self.FIRMAS:
            raise ValueError("Firma desconocida: " + str(firma))

        self.sin_seleccion = sin_seleccion
        self.detector = detector
        self.firma = firma
        self.base_path = config.base_path(sin_seleccion=sin_seleccion)
        self.set_features = "122_sin_seleccion" if sin_seleccion else "54"

        # Reutilizamos los builders auditados (H-1): scoring de anomalías y
        # reconstrucción del estimador de firmas. No se reimplementa nada.
        self._anom = NSLKDDAnomalyTrainer(sin_seleccion=sin_seleccion)
        self._sig = NSLKDDSignatureTrainer(sin_seleccion=sin_seleccion)

        # Mismo CV que firmas.py (Q4): StratifiedKFold(5, shuffle, semilla 42).
        self.cv = StratifiedKFold(
            n_splits=5, shuffle=True, random_state=config.RANDOM_STATE
        )

        # Rellenados por cargar_datos()
        self.X_D2 = None
        self.cat_D2 = None          # category_original de D2 (5 clases reales)
        self.tipo_D2 = None         # attack_original de D2 (tipo específico)
        self.y_bin = None           # binaria D2: 1=ataque, 0=normal
        self.X_D3 = None
        self.y_D3 = None            # category_original de D3 (4 clases de ataque)
        self.tipos_conocidos = None
        self.tipos_0day = None
        self.mask_ataque = None
        self.mask_tipo_conocido = None
        self.n_features = None

        # Rellenados por la cascada y la calibración
        self.score_cascada = None   # anomaly score del detector de la cascada sobre D2
        self.es_sospechoso = None   # etapa 1 (bool) — ES la binaria del híbrido (H-5)
        self.proba_susp = None      # predict_proba de firma sobre los sospechosos
        self.clases_firma = None    # orden de clases de la firma de la cascada
        self.umbral_conf = None     # elegido por la regla de presupuesto (H-4)
        self.tabla_calibracion = []  # filas OOF+D2 de los 3 umbrales
        self.tabla_0day = []        # recall 0-day por tipo de los 4 detectores
        self.metricas_run = None    # fila resumen de la corrida

    # ------------------------------------------------------------------
    # 1. Carga (P-3: solo D2 y D3; D1 no hace falta)
    # ------------------------------------------------------------------
    def cargar_datos(self):
        print("=" * 70)
        print("HÍBRIDO — carga (set: {} · detector: {} · firma: {})".format(
            self.set_features, self.detector, self.firma))
        print("=" * 70)
        splits = load_specialized_splits(self.base_path)
        if splits is None:
            raise RuntimeError("No se pudieron cargar las divisiones: " + self.base_path)

        self.X_D2 = splits["D2"]["X"]
        self.cat_D2 = splits["D2"]["y_category"]["category_original"].astype(str).values
        self.tipo_D2 = splits["D2"]["y_attack"]["attack_original"].astype(str).values
        self.y_bin = (self.cat_D2 != config.ETIQUETA_NORMAL).astype(int)
        self.n_features = self.X_D2.shape[1]

        self.X_D3 = splits["D3"]["X"]
        self.y_D3 = splits["D3"]["y_category"]["category_original"].astype(str).values
        tipos_D3 = splits["D3"]["y_attack"]["attack_original"].astype(str)
        self.tipos_conocidos = set(tipos_D3.unique())

        # Máscaras de D2 y tipos 0-day = ataques de D2 cuyo tipo NO está en el train.
        self.mask_ataque = (self.cat_D2 != config.ETIQUETA_NORMAL)
        self.mask_tipo_conocido = np.isin(self.tipo_D2, list(self.tipos_conocidos))
        self.tipos_0day = sorted(
            set(self.tipo_D2[self.mask_ataque & ~self.mask_tipo_conocido])
        )

        print("   D2: {} filas ({} ataques / {} normales) · {} features".format(
            len(self.X_D2), int(self.y_bin.sum()), int((self.y_bin == 0).sum()),
            self.n_features))
        print("   D3: {} filas · categorías {}".format(
            len(self.X_D3), sorted(set(self.y_D3))))
        print("   Tipos 0-day en D2 (ausentes del train): {} → {}".format(
            len(self.tipos_0day), self.tipos_0day))

    # ------------------------------------------------------------------
    # Carga de joblibs persistidos (H-1) con verificación de variante
    # ------------------------------------------------------------------
    def _cargar_joblib(self, prefijo, algo):
        ruta = config.MODELOS_DIR + r"\{}_{}_{}.joblib".format(prefijo, algo, self.set_features)
        datos = joblib.load(ruta)
        # Salvaguarda: el joblib debe ser de la misma variante de features (54/122)
        # que estamos evaluando, o las columnas no cuadrarían con X_D2.
        if str(datos.get("set_features")) != str(self.set_features):
            raise RuntimeError(
                "El joblib {} es de la variante '{}' pero se esperaba '{}'".format(
                    ruta, datos.get("set_features"), self.set_features))
        return datos, ruta

    # ------------------------------------------------------------------
    # 2. Calibración de UMBRAL_CONF sobre OOF de D3 (H-4/P-4).
    #    LÍNEA ROJA: esta función NO recibe D2. Solo D3.
    # ------------------------------------------------------------------
    def _calibrar_umbral_conf(self, joblib_firma):
        """
        Reconstruye el estimador de firmas desde su config, obtiene probabilidades
        OOF sobre D3 (cross_val_predict, mismo CV que firmas.py) y selecciona
        `UMBRAL_CONF` por la regla de presupuesto τ=2pp. Devuelve
        (umbral_elegido, prob_oof_por_umbral) — todo derivado SOLO de D3.
        """
        print("-" * 70)
        print("CALIBRACIÓN de UMBRAL_CONF sobre OOF de D3 (sin tocar D2)")
        print("-" * 70)

        algo = joblib_firma["algoritmo"]
        balanceo = joblib_firma["balanceo"]
        cfg = joblib_firma["config_ganadora"]
        # Reconstrucción fiel (H-1): mismo builder + set_params (claves ya con 'clf__'
        # si SMOTE, como las persiste firmas.py::_entrenar_final).
        est = self._sig._estimador_para(algo, balanceo)
        est.set_params(**cfg)

        # Probabilidades out-of-fold: cada muestra de D3 puntuada por un modelo que
        # NO la vio en su fold de entrenamiento (SMOTE se aplica dentro del fold vía
        # ImbPipeline → sin leakage). Columnas en orden alfabético de clases.
        proba_oof = cross_val_predict(
            est, self.X_D3, self.y_D3, cv=self.cv, method="predict_proba", n_jobs=-1
        )
        clases_oof = np.unique(self.y_D3)  # orden que usa cross_val_predict
        pred_oof = clases_oof[proba_oof.argmax(axis=1)]
        conf_oof = proba_oof.max(axis=1)

        # Baseline sin umbral (nada pasa a 'unknown'): recall macro de las 4 conocidas.
        recall_baseline = evaluacion.evaluar_multiclase(
            self.y_D3, pred_oof, labels=config.CATEGORIAS_ATAQUE
        )["recall_macro"]
        print("   Recall macro OOF (sin umbral, baseline) = {:.4f}".format(recall_baseline))

        oof_por_umbral = {}
        candidatos = []
        for u in self.UMBRALES_CONF:
            pred_u = pred_oof.copy().astype(object)
            baja_conf = conf_oof < u
            pred_u[baja_conf] = config.ETIQUETA_UNKNOWN
            recall_u = evaluacion.evaluar_multiclase(
                self.y_D3, pred_u, labels=config.CATEGORIAS_ATAQUE
            )["recall_macro"]
            tasa_falsos_unknown = float(baja_conf.mean())  # D3 son todos conocidos
            caida = recall_baseline - recall_u
            oof_por_umbral[u] = {
                "recall_macro_oof": recall_u,
                "tasa_falsos_unknown_oof": tasa_falsos_unknown,
                "caida_vs_baseline": caida,
            }
            dentro = caida <= self.TAU
            if dentro:
                candidatos.append(u)
            print("   umbral={:.1f} → recall_macro_oof={:.4f} (caída {:.4f}) "
                  "· falsos_unknown={:.4f} {}".format(
                      u, recall_u, caida, tasa_falsos_unknown,
                      "[dentro de τ]" if dentro else "[fuera de τ]"))

        # Regla de presupuesto (H-4): el umbral MÁS ALTO cuya caída ≤ τ. Si ninguno
        # cabe, el más conservador (el más bajo).
        elegido = max(candidatos) if candidatos else min(self.UMBRALES_CONF)
        print("   → UMBRAL_CONF elegido (τ={:.2f}) = {:.1f}".format(self.TAU, elegido))

        for u in self.UMBRALES_CONF:
            oof_por_umbral[u]["recall_macro_baseline_oof"] = recall_baseline
        return elegido, oof_por_umbral

    # ------------------------------------------------------------------
    # 3. Cascada sobre D2 (H-2/H-3). Score de etapa 1 una sola vez.
    # ------------------------------------------------------------------
    def _preparar_cascada(self, joblib_det, joblib_firma):
        """Calcula el score de la etapa 1 y la proba de firma sobre los sospechosos.
        Ambos son independientes de UMBRAL_CONF, así que se computan una única vez."""
        # Etapa 1: anomaly score y sospechosos (reutiliza _score de anomalias.py, H-1).
        model_det = joblib_det["modelo"]
        umbral_det = joblib_det["umbral"]
        self.score_cascada = self._anom._score(self.detector, model_det, self.X_D2)
        self.es_sospechoso = self.score_cascada > umbral_det  # binaria del híbrido (H-5)

        # Etapa 2: predict_proba de la firma SOLO sobre los sospechosos.
        model_firma = joblib_firma["modelo"]
        self.clases_firma = np.asarray(model_firma.classes_)
        Xs = self.X_D2.loc[self.es_sospechoso]
        if len(Xs) > 0:
            self.proba_susp = model_firma.predict_proba(Xs)
        else:
            self.proba_susp = np.empty((0, len(self.clases_firma)))
        print("   Etapa 1: {} sospechosos / {} ({} normales dejados pasar)".format(
            int(self.es_sospechoso.sum()), len(self.X_D2),
            int((~self.es_sospechoso).sum())))

    def _ensamblar_prediccion(self, umbral_conf):
        """Construye la predicción final sobre TODO D2 para un UMBRAL_CONF dado.
        No sospechoso → 'normal'; sospechoso → categoría argmax, o 'unknown' si la
        confianza máxima < umbral_conf. Barato: solo re-umbraliza la proba cacheada."""
        pred = np.full(len(self.X_D2), config.ETIQUETA_NORMAL, dtype=object)
        if self.proba_susp.shape[0] > 0:
            conf = self.proba_susp.max(axis=1)
            cat_susp = self.clases_firma[self.proba_susp.argmax(axis=1)].astype(object)
            cat_susp[conf < umbral_conf] = config.ETIQUETA_UNKNOWN
            pred[self.es_sospechoso] = cat_susp
        return pred

    # ------------------------------------------------------------------
    # 4. Evaluación sobre D2 por alcance (H-5/H-6) para un UMBRAL_CONF dado
    # ------------------------------------------------------------------
    def _metricas_d2(self, pred_final):
        """Métricas del híbrido sobre D2, cada una con su alcance (H-6). Sin número
        único engañoso. Devuelve un dict con: binaria (=etapa 1, H-5), por-categoría-
        conocida (coste del filtro de anomalías), f1_macro 5 clases conservador
        (unknown = error) y el desglose 0-day (routing a unknown)."""
        # (a) Binaria = etapa 1 por construcción (H-5): reutiliza es_sospechoso.
        binaria = evaluacion.evaluar_binario(
            self.y_bin, self.es_sospechoso.astype(int), self.score_cascada
        )

        # (b) Por categoría conocida: end-to-end sobre ataques de tipo conocido de D2.
        # Mide el coste de anteponer el filtro de anomalías frente a firmas-solo (5.2).
        mask_conocida = self.mask_ataque & self.mask_tipo_conocido
        conocida = evaluacion.evaluar_multiclase(
            self.cat_D2[mask_conocida], pred_final[mask_conocida],
            labels=config.CATEGORIAS_ATAQUE,
        )

        # (c) f1_macro a 5 clases CONSERVADOR (H-6): los 'unknown' cuentan como error
        # (no están en labels). Infravalora al híbrido a propósito; aun así la tesis
        # se sostiene por el 0-day. Es el número comparable con baseline.py.
        conservador = evaluacion.evaluar_multiclase(
            self.cat_D2, pred_final, labels=config.CATEGORIAS_MULTICLASE,
        )

        # (d) 0-day: recall de "marcado sospechoso" por tipo (etapa 1, indep. del
        # umbral) + de los detectados, % enrutados a 'unknown' vs mal-etiquetados.
        r0 = evaluacion.evaluar_0day_por_tipo(
            self.tipo_D2, self.es_sospechoso, self.tipos_0day
        )
        mask_0day = self.mask_ataque & ~self.mask_tipo_conocido
        det_0day = mask_0day & self.es_sospechoso
        n_det_0day = int(det_0day.sum())
        pred_0day_det = pred_final[det_0day]
        pct_unknown = (float((pred_0day_det == config.ETIQUETA_UNKNOWN).mean())
                       if n_det_0day > 0 else float("nan"))

        return {
            "binaria": binaria,
            "conocida": conocida,
            "conservador": conservador,
            "recall_0day": r0,
            "pct_unknown_entre_0day_detectados": pct_unknown,
            "n_conocida": int(mask_conocida.sum()),
        }

    # ------------------------------------------------------------------
    # 5. Tabla 0-day de los 4 detectores (H-2) — cierra H1, con FPR (P-2)
    # ------------------------------------------------------------------
    def _tabla_0day_cuatro_detectores(self):
        """Para CADA uno de los 4 detectores: carga su joblib, puntúa D2 con su
        umbral guardado y calcula el recall 0-day por tipo + su FPR binario. El
        recall 0-day depende SOLO del detector y su umbral (no de la firma), así que
        H1 (54 vs 122) deja de depender de elegir IF vs AE."""
        print("-" * 70)
        print("RECALL 0-DAY DE LOS 4 DETECTORES (H-2, cierra H1) — con FPR (P-2)")
        print("-" * 70)
        for det in self.DETECTORES:
            try:
                jd, _ = self._cargar_joblib("anomalia", det)
            except (FileNotFoundError, RuntimeError) as e:
                # M1: un joblib ausente o de otra variante (54/122) no debe abortar
                # toda la tabla; se omite ese detector con aviso y se sigue con el resto.
                print("   [aviso] detector {} no disponible ({}); se omite.".format(det, e))
                continue
            score = self._anom._score(det, jd["modelo"], self.X_D2)
            es_sosp = score > jd["umbral"]
            fpr = evaluacion.evaluar_binario(self.y_bin, es_sosp.astype(int))["fpr"]
            r0 = evaluacion.evaluar_0day_por_tipo(self.tipo_D2, es_sosp, self.tipos_0day)
            es_cascada = (det == self.detector)
            print("   {:<20} recall_0day_global={:.4f} · FPR={:.4f}{}".format(
                det, r0["__global__"]["recall"], fpr,
                "  ← detector de la cascada" if es_cascada else ""))
            for tipo, d in r0.items():
                self.tabla_0day.append({
                    "set_features": self.set_features,
                    "detector": det,
                    "es_cascada": bool(es_cascada),
                    "fpr_detector": round(fpr, 6),
                    "tipo": tipo,
                    "n": d["n"],
                    "detectados": d["detectados"],
                    "recall": round(d["recall"], 6) if d["recall"] == d["recall"] else d["recall"],
                })

    # ------------------------------------------------------------------
    # 6. Figura: matriz de confusión 5×6 (H-6)
    # ------------------------------------------------------------------
    def _plot_matriz_5x6(self, pred_final):
        """Matriz filas=5 clases reales × columnas=6 (con 'unknown'). No usa el
        helper cuadrado de evaluacion: aquí filas≠columnas por construcción."""
        from sklearn.metrics import confusion_matrix
        cm6 = confusion_matrix(self.cat_D2, pred_final, labels=config.CATEGORIAS_HIBRIDO)
        # La fila 'unknown' (índice 5) es todo ceros (no hay 'unknown' real) → se quita.
        idx_unknown = config.CATEGORIAS_HIBRIDO.index(config.ETIQUETA_UNKNOWN)
        cm = np.delete(cm6, idx_unknown, axis=0)
        filas = config.CATEGORIAS_MULTICLASE      # 5 reales
        cols = config.CATEGORIAS_HIBRIDO          # 6 predichas

        fig, ax = plt.subplots(figsize=(1.5 * len(cols) + 2, 1.4 * len(filas) + 2))
        sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", cbar=True,
                    xticklabels=cols, yticklabels=filas, ax=ax)
        ax.set_xlabel("Predicción (híbrido)")
        ax.set_ylabel("Real")
        ax.set_title("Matriz de confusión — híbrido {}→{} (D2, {} features)".format(
            self.detector, self.firma, self.set_features))
        fig.tight_layout()
        ruta = config.FIGURAS_DIR + r"\hibrido_cm_{}.png".format(self.set_features)
        fig.savefig(ruta, dpi=300, bbox_inches="tight")
        plt.close(fig)
        print("   Matriz 5×6: {}".format(ruta))

    # ------------------------------------------------------------------
    # 7. Persistencia (H-7): 3 CSV idempotentes + figura + descriptor joblib
    # ------------------------------------------------------------------
    def _limpiar_variante_csv(self, csv_path):
        """Idempotencia por variante (misma lógica auditada que anomalias/firmas)."""
        import os
        if not os.path.exists(csv_path):
            return
        try:
            df = pd.read_csv(csv_path)
        except Exception:
            return
        if "set_features" not in df.columns:
            return
        df = df[df["set_features"].astype(str) != str(self.set_features)]
        if len(df) == 0:
            os.remove(csv_path)
        else:
            df.to_csv(csv_path, index=False)

    def _persistir(self, ruta_det, ruta_firma):
        # (1) Tabla de calibración: sensibilidad de los 3 umbrales (OOF + D2, H-4).
        csv_cal = config.RESULTADOS_DIR + r"\metricas_hibrido_calibracion.csv"
        self._limpiar_variante_csv(csv_cal)
        for fila in self.tabla_calibracion:
            evaluacion.guardar_metricas(fila, csv_cal)
        print("   Tabla de calibración: {}".format(csv_cal))

        # (2) Tabla 0-day por tipo de los 4 detectores (cierra H1, con FPR).
        csv_0day = config.RESULTADOS_DIR + r"\metricas_hibrido_0day.csv"
        self._limpiar_variante_csv(csv_0day)
        for fila in self.tabla_0day:
            evaluacion.guardar_metricas(fila, csv_0day)
        print("   Tabla 0-day (4 detectores): {}".format(csv_0day))

        # (3) Fila resumen de la corrida (métricas por alcance con el umbral elegido).
        csv_res = config.RESULTADOS_DIR + r"\metricas_hibrido.csv"
        self._limpiar_variante_csv(csv_res)
        evaluacion.guardar_metricas(self.metricas_run, csv_res)
        print("   Tabla resumen: {}".format(csv_res))

        # (4) Descriptor reproducible (H-7): referencias + umbral + τ. NO re-serializa
        # los modelos (ya existen en sus joblibs); guarda qué usa y la decisión.
        ruta_desc = config.MODELOS_DIR + r"\hibrido_{}.joblib".format(self.set_features)
        joblib.dump({
            "tipo": "descriptor_hibrido",
            "set_features": self.set_features,
            "sin_seleccion": bool(self.sin_seleccion),
            "n_features": self.n_features,
            "detector": self.detector,
            "firma": self.firma,
            "joblib_detector": ruta_det,
            "joblib_firma": ruta_firma,
            "umbral_conf_elegido": self.umbral_conf,
            "umbrales_explorados": self.UMBRALES_CONF,
            "tau": self.TAU,
            "tipos_0day": self.tipos_0day,
            "base_path_usado": self.base_path,
        }, ruta_desc)
        print("   Descriptor del híbrido: {}".format(ruta_desc))

    # ------------------------------------------------------------------
    # Orquestación
    # ------------------------------------------------------------------
    def evaluar_todo(self):
        config.setup_utf8()
        config.ensure_dirs()
        t0 = time.time()
        self.cargar_datos()

        # Cargar los joblibs de la cascada (H-1).
        joblib_det, ruta_det = self._cargar_joblib("anomalia", self.detector)
        joblib_firma, ruta_firma = self._cargar_joblib("firma", self.firma)

        # Calibración SOLO con D3 (P-4: la función no recibe D2).
        self.umbral_conf, oof_por_umbral = self._calibrar_umbral_conf(joblib_firma)

        # Preparar cascada sobre D2 (score etapa 1 + proba etapa 2), una sola vez.
        print("-" * 70)
        print("CASCADA SOBRE D2")
        print("-" * 70)
        self._preparar_cascada(joblib_det, joblib_firma)

        # Tabla de sensibilidad: los 3 umbrales, cada uno con OOF (ya calculado) + D2.
        for u in self.UMBRALES_CONF:
            pred_u = self._ensamblar_prediccion(u)
            m = self._metricas_d2(pred_u)
            oof = oof_por_umbral[u]
            self.tabla_calibracion.append({
                "set_features": self.set_features,
                "detector": self.detector,
                "firma": self.firma,
                "umbral_conf": u,
                "elegido": bool(u == self.umbral_conf),
                "oof_recall_macro_conocidas": round(oof["recall_macro_oof"], 6),
                "oof_recall_macro_baseline": round(oof["recall_macro_baseline_oof"], 6),
                "oof_tasa_falsos_unknown": round(oof["tasa_falsos_unknown_oof"], 6),
                "d2_f1_macro_5_conservador": round(m["conservador"]["f1_macro"], 6),
                "d2_recall_0day_global": round(m["recall_0day"]["__global__"]["recall"], 6),
                "d2_pct_unknown_entre_0day_det": (
                    round(m["pct_unknown_entre_0day_detectados"], 6)
                    if m["pct_unknown_entre_0day_detectados"] ==
                    m["pct_unknown_entre_0day_detectados"] else float("nan")),
            })

        # Predicción final con el umbral ELEGIDO → métricas resumen + figura 5×6.
        pred_final = self._ensamblar_prediccion(self.umbral_conf)
        m = self._metricas_d2(pred_final)
        b = m["binaria"]
        c = m["conocida"]
        cons = m["conservador"]
        r0g = m["recall_0day"]["__global__"]
        print("-" * 70)
        print("RESUMEN (umbral_conf={:.1f})".format(self.umbral_conf))
        print("   Binaria (=etapa 1): recall={:.4f} FPR={:.4f} f1={:.4f} AUC-ROC={:.4f}".format(
            b["recall"], b["fpr"], b["f1"], b.get("roc_auc", float("nan"))))
        print("   Por categoría conocida: recall_macro={:.4f} f1_macro={:.4f} (n={})".format(
            c["recall_macro"], c["f1_macro"], m["n_conocida"]))
        print("   f1_macro 5 clases (conservador, unknown=error): {:.4f}".format(cons["f1_macro"]))
        print("   Recall 0-day global (etapa 1): {:.4f} (n={})".format(
            r0g["recall"], r0g["n"]))

        self.metricas_run = {
            "set_features": self.set_features,
            "sin_seleccion": bool(self.sin_seleccion),
            "n_features": self.n_features,
            "detector": self.detector,
            "firma": self.firma,
            "umbral_conf_elegido": self.umbral_conf,
            "tau": self.TAU,
            # binaria (= etapa 1, H-5)
            "bin_recall": round(b["recall"], 6),
            "bin_precision": round(b["precision"], 6),
            "bin_f1": round(b["f1"], 6),
            "bin_fpr": round(b["fpr"], 6),
            "bin_accuracy": round(b["accuracy"], 6),
            "bin_roc_auc": round(b.get("roc_auc", float("nan")), 6),
            "bin_pr_auc": round(b.get("pr_auc", float("nan")), 6),
            "bin_tn": b["tn"], "bin_fp": b["fp"], "bin_fn": b["fn"], "bin_tp": b["tp"],
            # por categoría conocida (coste del filtro de anomalías)
            "conocida_precision_macro": round(c["precision_macro"], 6),
            "conocida_recall_macro": round(c["recall_macro"], 6),
            "conocida_f1_macro": round(c["f1_macro"], 6),
            "n_conocida": m["n_conocida"],
            # f1_macro 5 clases conservador (comparable con baseline.py)
            "f1_macro_5_conservador": round(cons["f1_macro"], 6),
            "accuracy_5": round(cons["accuracy"], 6),
            # 0-day (titular) + FPR de la cascada (P-2)
            "recall_0day_global": round(r0g["recall"], 6),
            "n_0day": r0g["n"],
            "fpr_cascada": round(b["fpr"], 6),
            "tiempo_s": round(time.time() - t0, 2),
        }

        # Figura 5×6 y tabla 0-day de los 4 detectores.
        self._plot_matriz_5x6(pred_final)
        self._tabla_0day_cuatro_detectores()

        # Persistir todo.
        self._persistir(ruta_det, ruta_firma)
        print("=" * 70)
        print("HÍBRIDO COMPLETADO ({} features) en {:.1f}s".format(
            self.set_features, time.time() - t0))
        print("=" * 70)
        return self.metricas_run


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Sistema híbrido H-NIDS: cascada anomalías→firmas evaluada sobre D2 "
                    "(sección 5.3). Carga los modelos persistidos; no re-entrena."
    )
    parser.add_argument(
        "--sin-seleccion", action="store_true",
        help="Usa el set de 122 features (variante sin selección 4.3.5) en lugar de "
             "las 54 por defecto. Para el experimento 54-vs-122 (decisión Q1/C, P-1).",
    )
    parser.add_argument(
        "--detector", choices=NSLKDDHybridEvaluator.DETECTORES, default="Autoencoder",
        help="Detector de la etapa 1 (por defecto Autoencoder, el mejor en 5.1; H-2).",
    )
    parser.add_argument(
        "--firma", choices=NSLKDDHybridEvaluator.FIRMAS, default="RandomForest",
        help="Clasificador de la etapa 2 (por defecto RandomForest; H-3).",
    )
    args = parser.parse_args()

    evaluador = NSLKDDHybridEvaluator(
        sin_seleccion=args.sin_seleccion, detector=args.detector, firma=args.firma
    )
    evaluador.evaluar_todo()
