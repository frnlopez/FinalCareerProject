# -*- coding: utf-8 -*-
"""
anomalias.py — Etapa 1 del H-NIDS: detección de anomalías (spec next-steps.md §6.3).

Compara CUATRO algoritmos no supervisados entrenados SOLO con tráfico normal (D1)
y evaluados sobre el test completo (D2), bajo protocolo idéntico (mismo split,
misma semilla 42, mismo umbral percentil 95, mismas métricas):

  - IsolationForest
  - OneClassSVM (kernel RBF)
  - LocalOutlierFactor (novelty=True)
  - Autoencoder implementado como MLPRegressor (fit(X, X)); PROHIBIDO TF/Keras.

Todos exponen un anomaly score UNIFICADO donde MAYOR = MÁS ANÓMALO, para que la
comparación (AUC, umbral, matrices) sea homogénea.

Reglas de protocolo (invalidan el TFG si se rompen):
  * D2 es INTOCABLE para ajustar hiperparámetros o el umbral.
  * Selección de hiperparámetros: mejor AUC-ROC sobre un set etiquetado formado por
    D1_val (normal=0) + una muestra de D3 (ataques CONOCIDOS del train=1). Jamás D2.
  * Umbral: percentil 95 del anomaly score sobre D1_val (solo normal). Igual para los 4.

Decisión Q1/C: el set de features es parametrizable (--sin-seleccion → 122 features
en lugar de las 54 por defecto) para poder correr el experimento 54-vs-122 sin
reescribir el script. Nada de rutas hardcodeadas: todo sale de config.base_path().
"""
import argparse
import time

# Backend no interactivo fijado de forma explícita ANTES de cualquier import que
# arrastre matplotlib (evaluacion/program). Así no dependemos del orden de import
# para que nada bloquee ni intente abrir ventanas.
import matplotlib
matplotlib.use("Agg")

import numpy as np
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import IsolationForest
from sklearn.svm import OneClassSVM
from sklearn.neighbors import LocalOutlierFactor
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import roc_auc_score

import config
import evaluacion  # importado antes que program: fija el backend Agg de matplotlib
from program import load_specialized_splits


class NSLKDDAnomalyTrainer:
    """
    Entrena y compara los cuatro detectores de anomalías de la etapa 1 del H-NIDS.

    Sigue el estilo de NSLKDDPreprocessor / NSLKDDValidator: una sola clase que
    orquesta carga, selección de hiperparámetros, umbral y evaluación.
    """

    # --- Grids pequeños (spec §6.3.4). Se recorren enteros, no hay GridSearchCV
    # porque el problema es no supervisado: la selección se hace por AUC-ROC sobre
    # el set etiquetado D1_val + muestra de D3. ---
    GRIDS = {
        "IsolationForest": [
            {"n_estimators": n, "max_samples": m}
            for n in (100, 200, 300)
            for m in (0.5, 1.0)
        ],
        "OneClassSVM": [
            {"nu": nu, "gamma": g}
            for nu in (0.01, 0.05, 0.1)
            for g in ("scale", 0.01, 0.1)
        ],
        "LocalOutlierFactor": [
            {"n_neighbors": k} for k in (10, 20, 35, 50)
        ],
        "Autoencoder": [
            {"hidden_layer_sizes": h} for h in ((64, 32, 64), (32, 16, 32))
        ],
    }

    ALGORITMOS = ["IsolationForest", "OneClassSVM", "LocalOutlierFactor", "Autoencoder"]

    # OneClassSVM es O(n^2): entrenarlo con las ~67k filas de D1 es inviable.
    # Se entrena con una submuestra reproducible (spec §6.3, "trampas conocidas").
    N_SUBMUESTRA_OCSVM = 20000
    # Tamaño de la muestra de ataques CONOCIDOS (D3) para la selección de config.
    N_MUESTRA_D3 = 5000
    PERCENTIL_UMBRAL = 95  # decisión fijada: ~5% de FPR aceptado sobre lo normal.

    def __init__(self, sin_seleccion=False):
        """
        Parameters
        ----------
        sin_seleccion : bool
            False (por defecto) → set de 54 features (selección 4.3.5 aplicada).
            True → set de 122 features (variante sin selección). Decisión Q1/C.
        """
        self.sin_seleccion = sin_seleccion
        self.base_path = config.base_path(sin_seleccion=sin_seleccion)
        # Etiqueta legible del set de features para la tabla de métricas.
        self.set_features = "122_sin_seleccion" if sin_seleccion else "54"

        # Rellenados por cargar_datos()
        self.X_D1_train = None
        self.X_D1_val = None
        self.X_D2 = None
        self.y_bin = None          # etiqueta binaria de D2 (1=ataque, 0=normal)
        self.X_val_lab = None      # D1_val + muestra D3 (para selección de config)
        self.y_val_lab = None
        self.n_features = None

        # Rellenados por entrenar_todos()
        self.resultados = {}       # {algo: dict con modelo, umbral, config, métricas}

    # ------------------------------------------------------------------
    # 1-2. Carga de datos y construcción de conjuntos
    # ------------------------------------------------------------------
    def cargar_datos(self):
        """Carga D1/D2/D3, define la etiqueta binaria de D2 y prepara los splits."""
        print("=" * 70)
        print("CARGA DE DATOS (set de features: {})".format(self.set_features))
        print("=" * 70)
        splits = load_specialized_splits(self.base_path)
        if splits is None:
            raise RuntimeError(
                "No se pudieron cargar las divisiones desde: " + self.base_path
            )

        X_D1 = splits["D1"]["X"]
        self.X_D2 = splits["D2"]["X"]
        self.n_features = X_D1.shape[1]

        # Etiqueta binaria de D2: positivo = ataque = 1 (config.CLASE_ATAQUE).
        cat_D2 = splits["D2"]["y_category"]["category_original"].values
        self.y_bin = (cat_D2 != config.ETIQUETA_NORMAL).astype(int)

        # Split de D1 (solo normal): 80% entrenamiento, 20% validación (semilla 42).
        self.X_D1_train, self.X_D1_val = train_test_split(
            X_D1, test_size=0.2, random_state=config.RANDOM_STATE
        )

        # Set de validación ETIQUETADO para elegir hiperparámetros (spec §6.3.4):
        # D1_val (normal=0) + muestra de D3 (ataques conocidos del train=1).
        # NUNCA se usa D2 para esto.
        X_D3 = splits["D3"]["X"]
        n_d3 = min(self.N_MUESTRA_D3, len(X_D3))
        X_D3_muestra = X_D3.sample(n=n_d3, random_state=config.RANDOM_STATE)

        self.X_val_lab = pd.concat([self.X_D1_val, X_D3_muestra], axis=0, ignore_index=True)
        self.y_val_lab = np.concatenate([
            np.full(len(self.X_D1_val), config.CLASE_NORMAL),
            np.full(len(X_D3_muestra), config.CLASE_ATAQUE),
        ])

        print("   D1: {} filas ({} train / {} val) · {} features".format(
            len(X_D1), len(self.X_D1_train), len(self.X_D1_val), self.n_features))
        print("   D2: {} filas ({} ataques / {} normales)".format(
            len(self.X_D2), int(self.y_bin.sum()), int((self.y_bin == 0).sum())))
        print("   Set validación etiquetado: {} normales (D1_val) + {} ataques (D3)".format(
            len(self.X_D1_val), n_d3))

    # ------------------------------------------------------------------
    # Construcción de modelos, datos de entrenamiento y anomaly score unificado
    # ------------------------------------------------------------------
    def _construir(self, algo, cfg):
        """Instancia el modelo del algoritmo con la configuración dada (semilla 42)."""
        if algo == "IsolationForest":
            return IsolationForest(random_state=config.RANDOM_STATE, n_jobs=-1, **cfg)
        if algo == "OneClassSVM":
            # OneClassSVM no admite random_state (algoritmo determinista).
            return OneClassSVM(kernel="rbf", **cfg)
        if algo == "LocalOutlierFactor":
            # novelty=True OBLIGATORIO para poder puntuar datos nuevos (D2).
            return LocalOutlierFactor(novelty=True, n_jobs=-1, **cfg)
        if algo == "Autoencoder":
            # Autoencoder = MLPRegressor reconstruyendo su entrada (fit(X, X)).
            # early_stopping reserva internamente un 10% para parar sin tocar D2.
            return MLPRegressor(
                random_state=config.RANDOM_STATE,
                early_stopping=True,
                max_iter=300,
                **cfg,
            )
        raise ValueError("Algoritmo desconocido: " + algo)

    def _datos_entrenamiento(self, algo, X_train):
        """
        Datos con los que se entrena cada algoritmo. OneClassSVM usa una submuestra
        de 20.000 (O(n^2)); el resto usa todo D1_train. Submuestra reproducible.
        """
        if algo == "OneClassSVM" and len(X_train) > self.N_SUBMUESTRA_OCSVM:
            return X_train.sample(n=self.N_SUBMUESTRA_OCSVM, random_state=config.RANDOM_STATE)
        return X_train

    def _ajustar(self, algo, model, X_fit):
        """Entrena el modelo. El autoencoder reconstruye su entrada: fit(X, X)."""
        if algo == "Autoencoder":
            model.fit(X_fit, X_fit)
        else:
            model.fit(X_fit)
        return model

    def _score(self, algo, model, X):
        """
        Anomaly score UNIFICADO: MAYOR = MÁS ANÓMALO (más probable ataque).

        En sklearn, score_samples/decision_function dan "mayor = más normal";
        por eso se niegan. El autoencoder usa el MSE de reconstrucción (ya positivo
        y creciente con la anomalía).
        """
        if algo in ("IsolationForest", "LocalOutlierFactor"):
            return -model.score_samples(X)
        if algo == "OneClassSVM":
            return -np.asarray(model.decision_function(X)).ravel()
        if algo == "Autoencoder":
            recon = model.predict(X)
            return ((recon - X.values) ** 2).mean(axis=1)
        raise ValueError("Algoritmo desconocido: " + algo)

    # ------------------------------------------------------------------
    # 4. Selección de hiperparámetros por AUC-ROC (no supervisada de facto)
    # ------------------------------------------------------------------
    def _seleccionar_config(self, algo):
        """
        Entrena cada configuración del grid sobre D1_train y elige la de mejor
        AUC-ROC sobre el set etiquetado (D1_val + muestra D3). Devuelve el modelo
        ganador (ya entrenado sobre D1_train), su config, su AUC de validación y
        el tiempo de ENTRENAMIENTO acumulado (solo los fit del grid, sin contar
        el scoring: T1 separa entrenamiento e inferencia).
        """
        X_fit = self._datos_entrenamiento(algo, self.X_D1_train)
        mejor = {"auc": -np.inf, "cfg": None, "model": None}
        t_fit_total = 0.0

        for cfg in self.GRIDS[algo]:
            model = self._construir(algo, cfg)
            t_fit = time.perf_counter()
            self._ajustar(algo, model, X_fit)
            t_fit_total += time.perf_counter() - t_fit
            scores = self._score(algo, model, self.X_val_lab)
            auc = roc_auc_score(self.y_val_lab, scores)
            print("      cfg={} → AUC-ROC(val)={:.4f}".format(cfg, auc))
            if auc > mejor["auc"]:
                mejor = {"auc": auc, "cfg": cfg, "model": model}

        return mejor["model"], mejor["cfg"], mejor["auc"], t_fit_total

    # ------------------------------------------------------------------
    # 3-6. Entrenamiento, umbral y evaluación de un algoritmo
    # ------------------------------------------------------------------
    def _procesar_algoritmo(self, algo):
        """Selecciona config, fija el umbral en D1_val y evalúa sobre D2."""
        print("-" * 70)
        print("ALGORITMO: {}".format(algo))
        print("-" * 70)
        # perf_counter (no time.time) en TODAS las medidas de duración: en Windows
        # time.time() tiene ~15,6 ms de resolución y cuantizaba los tiempos cortos.
        # Es monótono y sin época: solo vale para diferencias (la columna 'fecha'
        # la sigue dando datetime.now() dentro de guardar_metricas).
        t0 = time.perf_counter()

        model, cfg, auc_val, t_entrenamiento = self._seleccionar_config(algo)
        print("   Config ganadora: {} (AUC-ROC val={:.4f})".format(cfg, auc_val))

        # 5. Umbral = percentil 95 del score sobre D1_val (solo normal). Igual para
        # los 4 algoritmos. Nunca se mira D2 para esto.
        scores_val = self._score(algo, model, self.X_D1_val)
        umbral = float(np.percentile(scores_val, self.PERCENTIL_UMBRAL))
        print("   Umbral (p{} sobre D1_val) = {:.6f}".format(self.PERCENTIL_UMBRAL, umbral))

        # 6. Evaluación sobre D2 (binaria). y_pred = score > umbral.
        # El scoring de D2 es la INFERENCIA del detector: se cronometra aparte
        # del entrenamiento (T1) para poder reportar latencia por flujo.
        t_inf = time.perf_counter()
        score_D2 = self._score(algo, model, self.X_D2)
        t_inferencia = time.perf_counter() - t_inf
        y_pred = (score_D2 > umbral).astype(int)
        metricas = evaluacion.evaluar_binario(self.y_bin, y_pred, score_D2)

        print("   D2 → AUC-ROC={:.4f} AUC-PR={:.4f} F1={:.4f} recall={:.4f} FPR={:.4f}".format(
            metricas.get("roc_auc", float("nan")), metricas.get("pr_auc", float("nan")),
            metricas["f1"], metricas["recall"], metricas["fpr"]))

        # Matriz de confusión 2x2 con etiquetas legibles (normal/ataque).
        etiquetas = ["normal", "ataque"]
        y_true_str = np.where(self.y_bin == config.CLASE_ATAQUE, "ataque", "normal")
        y_pred_str = np.where(y_pred == config.CLASE_ATAQUE, "ataque", "normal")
        evaluacion.plot_matriz_confusion(
            y_true_str, y_pred_str, labels=etiquetas,
            titulo="Matriz de confusión — {} (anomalías, D2)".format(algo),
            filename="anomalias_cm_{}_{}.png".format(algo, self.set_features),
        )

        self.resultados[algo] = {
            "modelo": model,
            "config_ganadora": cfg,
            "auc_val": auc_val,
            "umbral": umbral,
            "score_D2": score_D2,
            "metricas": metricas,
            # OJO: 'tiempo_s' es el bloque COMPLETO del algoritmo (grid + umbral +
            # inferencia + figura), no el ajuste. Va declarado en el dato con
            # config.ALCANCE_TIEMPO_S_BLOQUE_ALGORITMO.
            "tiempo_s": time.perf_counter() - t0,
            "tiempo_entrenamiento_s": t_entrenamiento,
            "tiempo_inferencia_s": t_inferencia,
        }
        print("   Tiempo: {:.1f}s total (entrenamiento {:.1f}s · inferencia D2 "
              "{:.2f}s)".format(self.resultados[algo]["tiempo_s"],
                                t_entrenamiento, t_inferencia))

    # ------------------------------------------------------------------
    # 7. Persistencia (modelos joblib, CSV de métricas, figuras ROC/PR)
    # ------------------------------------------------------------------
    def _fila_metricas(self, algo, r):
        """
        Fila de la tabla de métricas para un algoritmo. Empieza por el conjunto
        mínimo obligatorio (T1): 'algoritmo' + 'alcance' (aquí, binario
        normal-vs-ataque sobre D2 completo) + variante + nº de features. La
        procedencia (semilla, commit, fecha) la inyecta guardar_metricas.

        OJO con las dos columnas que NO son de D2 (T1, config.ALCANCE_SELECCION):
          - 'auc_val': AUC-ROC sobre D1_val + muestra de D3, la cifra con la que
            se ELIGIÓ la configuración. Es sistemáticamente más alta que el
            'roc_auc' de D2 (IsolationForest 54: 0,9918 frente a 0,9229), así que
            citarla como "AUC del detector" sería citar un número del train.
          - 'umbral': percentil 95 del score sobre D1_val, también del train.
        El sufijo '_val' y la columna 'umbral' están declarados en
        config.ALCANCE_SUFIJOS / ALCANCE_COLUMNAS con ese alcance propio.

        Y con 'tiempo_s': aquí mide el BLOQUE COMPLETO del algoritmo (grid +
        umbral + inferencia sobre D2 + figura), que es lo que cita la tabla de 4.4
        del vault; en metricas_baseline.csv la columna homónima es solo el
        GridSearchCV y en metricas_hibrido.csv es el tramo de la carga de los
        splits al cierre de la fila. Por eso cada fila lleva 'alcance_tiempo_s':
        el dato dice qué mide.
        """
        m = r["metricas"]
        fila = {
            "algoritmo": algo,
            "alcance": config.ALCANCE_ANOMALIAS,
            "set_features": self.set_features,
            "sin_seleccion": bool(self.sin_seleccion),
            "n_features": self.n_features,
            "config_ganadora": str(r["config_ganadora"]),
            "auc_val": round(r["auc_val"], 6),
            "umbral": round(r["umbral"], 6),
            "roc_auc": round(m.get("roc_auc", float("nan")), 6),
            "pr_auc": round(m.get("pr_auc", float("nan")), 6),
            "precision": round(m["precision"], 6),
            "recall": round(m["recall"], 6),
            "f1": round(m["f1"], 6),
            "accuracy": round(m["accuracy"], 6),
            "fpr": round(m["fpr"], 6),
            "tn": m["tn"], "fp": m["fp"], "fn": m["fn"], "tp": m["tp"],
            "tiempo_s": round(r["tiempo_s"], 2),
            "alcance_tiempo_s": config.ALCANCE_TIEMPO_S_BLOQUE_ALGORITMO,
        }
        # Tiempos separados (T1): entrenamiento = fits del grid; inferencia =
        # scoring de D2 completo, que es lo que mide latencia y caudal.
        fila.update(evaluacion.metricas_tiempo(
            r["tiempo_entrenamiento_s"], r["tiempo_inferencia_s"], len(self.X_D2)
        ))
        return fila

    def _persistir(self):
        """Guarda modelos, la tabla de métricas y las curvas ROC/PR superpuestas."""
        csv_path = config.RESULTADOS_DIR + r"\metricas_anomalias.csv"

        filas = {algo: self._fila_metricas(algo, r)
                 for algo, r in self.resultados.items()}

        # Idempotencia por variante (H3), ahora con la función única de
        # evaluacion.py: el CSV es único y acumulado, pero al re-ejecutar una
        # variante (54 o 122) se borran primero sus filas previas para no
        # acumular duplicados. La otra variante se conserva intacta.
        evaluacion.limpiar_variante_csv(
            csv_path, self.set_features,
            evaluacion.cabecera_esperada(next(iter(filas.values())))
            if filas else None,
        )

        for algo, r in self.resultados.items():
            # Un joblib por algoritmo, sufijado por variante de features (H3) para
            # que 54 y 122 coexistan sin pisarse. Todo lo necesario para desplegar.
            ruta_modelo = config.MODELOS_DIR + r"\anomalia_{}_{}.joblib".format(
                algo, self.set_features)
            joblib.dump(
                {
                    "algoritmo": algo,
                    "modelo": r["modelo"],
                    "umbral": r["umbral"],
                    "config_ganadora": r["config_ganadora"],
                    "base_path_usado": self.base_path,
                    "set_features": self.set_features,
                    "n_features": self.n_features,
                    "percentil_umbral": self.PERCENTIL_UMBRAL,
                    "semilla": config.RANDOM_STATE,
                    "commit": config.commit_actual(),
                },
                ruta_modelo,
            )

            # Una fila por algoritmo en la tabla acumulada (→ tabla 5.1.2).
            evaluacion.guardar_metricas(filas[algo], csv_path)
            print("   Guardado modelo: {}".format(ruta_modelo))

        # La clave de unicidad (variante × algoritmo × alcance) y el recuento de
        # filas de la variante (4 detectores → 8 con las dos variantes) se
        # verifican, no se suponen.
        evaluacion.comprobar_unicidad(csv_path)
        evaluacion.comprobar_recuento(csv_path, self.set_features)

        # Figura estrella de 5.1: ROC/PR de los 4 algoritmos superpuestas.
        scores_por_algo = {algo: r["score_D2"] for algo, r in self.resultados.items()}
        nombre_fig = "anomalias_{}".format(self.set_features)
        evaluacion.plot_roc_pr(
            scores_por_algo, self.y_bin,
            nombre_fig=nombre_fig,
            titulo="Detección de anomalías (D2, {} features)".format(self.set_features),
        )
        print("   Tabla de métricas: {}".format(csv_path))
        print("   Figuras ROC/PR: {0}_roc.png / {0}_pr.png".format(nombre_fig))

    # ------------------------------------------------------------------
    # Orquestación
    # ------------------------------------------------------------------
    def entrenar_todos(self):
        """Ejecuta el pipeline completo para los cuatro algoritmos."""
        config.setup_utf8()
        config.ensure_dirs()
        self.cargar_datos()
        for algo in self.ALGORITMOS:
            self._procesar_algoritmo(algo)
        self._persistir()
        print("=" * 70)
        print("ANOMALÍAS COMPLETADO ({} features)".format(self.set_features))
        print("=" * 70)
        return self.resultados


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Etapa 1 del H-NIDS: detección de anomalías (4 algoritmos "
                    "comparados bajo protocolo idéntico sobre NSL-KDD)."
    )
    parser.add_argument(
        "--sin-seleccion", action="store_true",
        help="Usa el set de 122 features (variante sin selección 4.3.5) en lugar "
             "de las 54 por defecto. Para el experimento 54-vs-122 (decisión Q1/C).",
    )
    args = parser.parse_args()

    trainer = NSLKDDAnomalyTrainer(sin_seleccion=args.sin_seleccion)
    trainer.entrenar_todos()
