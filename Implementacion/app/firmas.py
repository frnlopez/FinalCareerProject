# -*- coding: utf-8 -*-
"""
firmas.py — Etapa 2 del H-NIDS: detección basada en firmas (spec next-steps.md §6.4).

Clasificador MULTICLASE de ataques CONOCIDOS entrenado sobre D3 (solo ataques, 4
categorías: dos/probe/r2l/u2r; aquí NO existe 'normal') y evaluado sobre las filas
de ataque de D2 cuyo tipo específico SÍ estaba en el train. Compara CUATRO
algoritmos supervisados de scikit-learn bajo protocolo idéntico:

  - DecisionTree (base de la extracción de firmas legibles, export_text)
  - RandomForest
  - KNN (KNeighborsClassifier)
  - HistGradientBoosting

Protocolo (igual para los 4):
  * GridSearchCV con StratifiedKFold(5, shuffle=True, random_state=42) y
    scoring='f1_macro' (u2r tiene ~52 muestras: el accuracy miente, la macro no).
  * Mini-experimento de balanceo 4.3.4: SMOTE (dentro de cada fold, vía ImbPipeline)
    vs class_weight='balanced' (DT/RF) o vs nada (KNN/HistGB). El balanceo ganador
    por f1_macro CV se usa para el GridSearch final de ese algoritmo.

Reglas de protocolo (invalidan el TFG si se rompen):
  * D2 es INTOCABLE: nada de D2 se usa para elegir hiperparámetros ni balanceo
    (todo por CV sobre D3). D2 solo para la evaluación final (5.2).
  * SMOTE SOLO dentro de cada fold del CV (ImbPipeline), NUNCA antes del split (si
    no, los folds de validación contendrían sintéticos → CV optimista / leakage).
  * random_state=42 en TODO (StratifiedKFold, SMOTE, modelos, GridSearchCV).

Decisión Q1/C: el set de features es parametrizable (--sin-seleccion → 122 features
en lugar de las 54 por defecto). Nada de rutas hardcodeadas: todo sale de config.
"""
import argparse
import time

# Backend no interactivo fijado de forma explícita ANTES de cualquier import que
# arrastre matplotlib (evaluacion/program). Así nada bloquea ni abre ventanas.
import matplotlib
matplotlib.use("Agg")

import numpy as np
import pandas as pd
import joblib

from sklearn.model_selection import StratifiedKFold, GridSearchCV, cross_val_score
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.ensemble import RandomForestClassifier, HistGradientBoostingClassifier
from sklearn.neighbors import KNeighborsClassifier

from imblearn.pipeline import Pipeline as ImbPipeline
from imblearn.over_sampling import SMOTE

import config
import evaluacion  # importado antes que program: fija el backend Agg de matplotlib
from program import load_specialized_splits


class NSLKDDSignatureTrainer:
    """
    Entrena y compara los cuatro clasificadores de firmas de la etapa 2 del H-NIDS.

    Sigue el estilo de NSLKDDPreprocessor / NSLKDDValidator / NSLKDDAnomalyTrainer:
    una sola clase que orquesta carga, mini-experimento de balanceo, GridSearchCV,
    evaluación sobre D2 y extracción de reglas legibles.
    """

    ALGORITMOS = ["DecisionTree", "RandomForest", "KNN", "HistGradientBoosting"]

    # --- Grids pequeños (spec §6.4.3). Se recorren con GridSearchCV + f1_macro. ---
    GRIDS = {
        "DecisionTree": {
            "max_depth": [5, 10, 20, None],
            "min_samples_leaf": [1, 5, 20],
        },
        "RandomForest": {
            "n_estimators": [100, 300],
            "max_depth": [10, None],
        },
        "KNN": {
            "n_neighbors": [3, 5, 11],
            "weights": ["uniform", "distance"],
        },
        "HistGradientBoosting": {
            "learning_rate": [0.05, 0.1],
            "max_iter": [100, 300],
        },
    }

    # --- Opciones de balanceo a comparar por algoritmo (mini-experimento 4.3.4). ---
    # DT y RF tienen class_weight='balanced' → SMOTE vs class_weight.
    # KNN y HistGB NO tienen class_weight → SMOTE vs nada (decisión Q6: no cruzar ejes).
    BALANCEO_OPCIONES = {
        "DecisionTree": ["SMOTE", "class_weight"],
        "RandomForest": ["SMOTE", "class_weight"],
        "KNN": ["SMOTE", "nada"],
        "HistGradientBoosting": ["SMOTE", "nada"],
    }

    # k_neighbors de SMOTE. u2r tiene ~52 muestras en D3 (~41 por fold de train), de
    # sobra para k=5. Si alguna clase pequeña lo hiciera fallar, bajar a 3 (spec §6.4.4).
    K_SMOTE = 5

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
        # Etiqueta legible del set de features para artefactos y tablas.
        self.set_features = "122_sin_seleccion" if sin_seleccion else "54"

        # Protocolo CV único (mismo split, misma semilla) para los 4 algoritmos.
        self.cv = StratifiedKFold(
            n_splits=5, shuffle=True, random_state=config.RANDOM_STATE
        )

        # Rellenados por cargar_datos()
        self.X_D3 = None
        self.y_D3 = None            # category_original (strings: dos/probe/r2l/u2r)
        self.X_D2_eval = None       # solo filas de ataque de D2 con tipo conocido
        self.y_D2_eval = None       # category_original de esas filas
        self.tipos_conocidos = None  # set de attack_original vistos en D3
        self.n_features = None

        # Rellenados por _experimento_balanceo() y _entrenar_final()
        self.balanceo_ganador = {}  # {algo: 'SMOTE'|'class_weight'|'nada'}
        self.filas_balanceo = []    # tabla 4.3.4
        self.resultados = {}        # {algo: dict con modelo, config, métricas...}

    # ------------------------------------------------------------------
    # 1. Carga de datos y construcción de conjuntos
    # ------------------------------------------------------------------
    def cargar_datos(self):
        """Carga D3 (train) y prepara la evaluación filtrada de D2 (0-day fuera)."""
        print("=" * 70)
        print("CARGA DE DATOS (set de features: {})".format(self.set_features))
        print("=" * 70)
        splits = load_specialized_splits(self.base_path)
        if splits is None:
            raise RuntimeError(
                "No se pudieron cargar las divisiones desde: " + self.base_path
            )

        # --- Train: D3 (solo ataques conocidos). Etiqueta = categoría (4 clases). ---
        self.X_D3 = splits["D3"]["X"]
        self.y_D3 = splits["D3"]["y_category"]["category_original"].astype(str).values
        self.n_features = self.X_D3.shape[1]

        # Tipos ESPECÍFICOS de ataque presentes en el train (para excluir 0-day en D2).
        tipos_D3 = splits["D3"]["y_attack"]["attack_original"].astype(str)
        self.tipos_conocidos = set(tipos_D3.unique())

        # --- Evaluación (5.2): SOLO filas de D2 que (a) sean ataque y (b) cuyo tipo
        # específico exista en el train. Los ~17 tipos nuevos (0-day) se EXCLUYEN
        # aquí: son trabajo de la etapa de anomalías y se miden en el híbrido. ---
        X_D2 = splits["D2"]["X"]
        cat_D2 = splits["D2"]["y_category"]["category_original"].astype(str)
        tipo_D2 = splits["D2"]["y_attack"]["attack_original"].astype(str)

        es_ataque = (cat_D2 != config.ETIQUETA_NORMAL).values
        tipo_conocido = tipo_D2.isin(self.tipos_conocidos).values
        mask_eval = es_ataque & tipo_conocido

        self.X_D2_eval = X_D2.loc[mask_eval].reset_index(drop=True)
        self.y_D2_eval = cat_D2.loc[mask_eval].reset_index(drop=True).values

        # Diagnóstico: cuántos 0-day se han apartado (son ataque pero tipo nuevo).
        n_0day = int((es_ataque & ~tipo_conocido).sum())
        tipos_0day = sorted(set(tipo_D2[es_ataque & ~tipo_conocido].unique()))

        print("   D3 (train firmas): {} filas · {} features · categorías {}".format(
            len(self.X_D3), self.n_features, sorted(set(self.y_D3))))
        vals, cnts = np.unique(self.y_D3, return_counts=True)
        print("   Distribución D3: {}".format(dict(zip(vals.tolist(), cnts.tolist()))))
        print("   Tipos de ataque conocidos (D3): {}".format(len(self.tipos_conocidos)))
        print("   D2 evaluación (ataques con tipo conocido): {} filas".format(
            len(self.X_D2_eval)))
        print("   D2 apartados como 0-day (tipo nuevo): {} filas · {} tipos: {}".format(
            n_0day, len(tipos_0day), tipos_0day))

    # ------------------------------------------------------------------
    # Construcción de estimadores (base y con balanceo)
    # ------------------------------------------------------------------
    def _estimador_base(self, algo, class_weight=None):
        """Instancia el clasificador del algoritmo (semilla 42, class_weight opcional)."""
        if algo == "DecisionTree":
            return DecisionTreeClassifier(
                random_state=config.RANDOM_STATE, class_weight=class_weight
            )
        if algo == "RandomForest":
            return RandomForestClassifier(
                random_state=config.RANDOM_STATE, n_jobs=-1, class_weight=class_weight
            )
        if algo == "KNN":
            # KNN no admite class_weight (se ignora class_weight si llega).
            return KNeighborsClassifier(n_jobs=-1)
        if algo == "HistGradientBoosting":
            # HistGB no admite class_weight.
            return HistGradientBoostingClassifier(random_state=config.RANDOM_STATE)
        raise ValueError("Algoritmo desconocido: " + algo)

    def _envolver_balanceo(self, algo, base, balanceo):
        """
        Devuelve el estimador listo para CV según el modo de balanceo:
          - 'SMOTE'  → ImbPipeline(SMOTE dentro del fold → clf). Sin leakage.
          - 'class_weight' / 'nada' → el propio estimador base.
        """
        if balanceo == "SMOTE":
            return ImbPipeline([
                ("smote", SMOTE(random_state=config.RANDOM_STATE, k_neighbors=self.K_SMOTE)),
                ("clf", base),
            ])
        return base

    def _estimador_para(self, algo, balanceo):
        """Estimador base + balanceo. class_weight='balanced' solo si el modo lo pide."""
        cw = "balanced" if balanceo == "class_weight" else None
        base = self._estimador_base(algo, class_weight=cw)
        return self._envolver_balanceo(algo, base, balanceo)

    # ------------------------------------------------------------------
    # 4. Mini-experimento de balanceo (sección 4.3.4)
    # ------------------------------------------------------------------
    def _experimento_balanceo(self):
        """
        Por algoritmo, compara sus dos opciones de balanceo con f1_macro en CV
        (mismo StratifiedKFold que el GridSearch), usando UN hiperparámetro por
        defecto razonable (decisión Q6: no cruzar balanceo × grid completo). El
        ganador por f1_macro se guarda para el GridSearch final. La tabla resultante
        (una fila por algoritmo × balanceo) ES la sección 4.3.4.
        """
        print("=" * 70)
        print("MINI-EXPERIMENTO DE BALANCEO (4.3.4) — f1_macro en CV sobre D3")
        print("=" * 70)

        for algo in self.ALGORITMOS:
            print("-" * 70)
            print("ALGORITMO: {}".format(algo))
            mejor = {"f1_macro": -np.inf, "balanceo": None}
            for balanceo in self.BALANCEO_OPCIONES[algo]:
                est = self._estimador_para(algo, balanceo)
                # SMOTE va DENTRO del pipeline → cross_val_score lo aplica por fold.
                scores = cross_val_score(
                    est, self.X_D3, self.y_D3,
                    cv=self.cv, scoring="f1_macro", n_jobs=-1,
                )
                f1m = float(scores.mean())
                print("      balanceo={:<12} → f1_macro(CV)={:.4f}".format(balanceo, f1m))
                self.filas_balanceo.append({
                    "algoritmo": algo,
                    "balanceo": balanceo,
                    "f1_macro_cv": round(f1m, 6),
                    "f1_macro_cv_std": round(float(scores.std()), 6),
                    "set_features": self.set_features,
                    "sin_seleccion": bool(self.sin_seleccion),
                    "n_features": self.n_features,
                })
                if f1m > mejor["f1_macro"]:
                    mejor = {"f1_macro": f1m, "balanceo": balanceo}
            self.balanceo_ganador[algo] = mejor["balanceo"]
            print("   Balanceo ganador: {} (f1_macro CV={:.4f})".format(
                mejor["balanceo"], mejor["f1_macro"]))

    # ------------------------------------------------------------------
    # 5. GridSearchCV final por algoritmo (con el balanceo ganador)
    # ------------------------------------------------------------------
    def _param_grid(self, algo, balanceo):
        """Grid del algoritmo; si el balanceo es SMOTE, prefija las claves con 'clf__'."""
        grid = dict(self.GRIDS[algo])
        if balanceo == "SMOTE":
            return {"clf__" + k: v for k, v in grid.items()}
        return grid

    def _entrenar_final(self, algo):
        """
        GridSearchCV sobre el grid del algoritmo usando el balanceo ganador del punto
        4 (dentro de ImbPipeline si el ganador es SMOTE), refit en TODO D3. Después
        evalúa sobre D2 filtrado (multiclase 4×4) y guarda la matriz de confusión.
        """
        print("-" * 70)
        print("GRIDSEARCH FINAL: {}".format(algo))
        print("-" * 70)
        t0 = time.time()

        balanceo = self.balanceo_ganador[algo]
        estimador = self._estimador_para(algo, balanceo)
        grid = self._param_grid(algo, balanceo)

        busqueda = GridSearchCV(
            estimator=estimador,
            param_grid=grid,
            scoring="f1_macro",
            cv=self.cv,
            n_jobs=-1,
            refit=True,
        )
        busqueda.fit(self.X_D3, self.y_D3)
        modelo = busqueda.best_estimator_  # refit en todo D3 (pipeline si SMOTE)
        print("   Balanceo: {} · mejor config: {} · f1_macro(CV)={:.4f}".format(
            balanceo, busqueda.best_params_, busqueda.best_score_))

        # 6. Evaluación sobre D2 filtrado (multiclase, para 5.2). labels FIJOS.
        y_pred = modelo.predict(self.X_D2_eval)
        metricas = evaluacion.evaluar_multiclase(
            self.y_D2_eval, y_pred, labels=config.CATEGORIAS_ATAQUE
        )
        print("   D2 (tipos conocidos) → f1_macro={:.4f} recall_macro={:.4f} acc={:.4f}".format(
            metricas["f1_macro"], metricas["recall_macro"], metricas["accuracy"]))

        # Matriz de confusión 4×4 (→ 5.2.1), sufijada por variante de features.
        evaluacion.plot_matriz_confusion(
            self.y_D2_eval, y_pred, labels=config.CATEGORIAS_ATAQUE,
            titulo="Matriz de confusión — {} (firmas, D2 tipos conocidos)".format(algo),
            filename="firmas_cm_{}_{}.png".format(algo, self.set_features),
        )

        self.resultados[algo] = {
            "modelo": modelo,
            "balanceo": balanceo,
            "config_ganadora": busqueda.best_params_,
            "f1_macro_cv": float(busqueda.best_score_),
            "metricas": metricas,
            "tiempo_s": time.time() - t0,
        }
        print("   Tiempo: {:.1f}s".format(self.resultados[algo]["tiempo_s"]))

    # ------------------------------------------------------------------
    # 7. Extracción de firmas legibles desde el mejor DecisionTree (parte IDS 4.5)
    # ------------------------------------------------------------------
    def _extraer_dt(self, modelo):
        """Devuelve el DecisionTreeClassifier subyacente (desenvuelve el ImbPipeline)."""
        if isinstance(modelo, ImbPipeline):
            return modelo.named_steps["clf"]
        return modelo

    def _extraer_firmas(self):
        """
        Con el MEJOR DecisionTree, export_text(max_depth=5) → reglas legibles tipo
        'si flag_S0 > 0.5 → dos'. Se guardan en firmas_reglas_<set_features>.txt para
        la sección 4.5 (IDS clásico). Sufijado para que las variantes coexistan.
        """
        if "DecisionTree" not in self.resultados:
            return
        dt = self._extraer_dt(self.resultados["DecisionTree"]["modelo"])
        reglas = export_text(
            dt, feature_names=list(self.X_D3.columns), max_depth=5
        )
        ruta = config.RESULTADOS_DIR + r"\firmas_reglas_{}.txt".format(self.set_features)
        cabecera = (
            "Reglas del mejor DecisionTree de firmas (export_text, max_depth=5)\n"
            "Set de features: {} · Balanceo: {} · Config: {}\n"
            "Categorías (orden de clases del árbol): {}\n"
            "{}\n"
        ).format(
            self.set_features,
            self.resultados["DecisionTree"]["balanceo"],
            self.resultados["DecisionTree"]["config_ganadora"],
            list(dt.classes_),
            "=" * 70,
        )
        with open(ruta, "w", encoding="utf-8") as f:
            f.write(cabecera)
            f.write(reglas)
        print("   Reglas de firmas: {}".format(ruta))

    # ------------------------------------------------------------------
    # Persistencia (modelos joblib, CSV de métricas, CSV de balanceo)
    # ------------------------------------------------------------------
    def _limpiar_variante_csv(self, csv_path):
        """
        Deja el CSV acumulado idempotente por variante: elimina las filas cuyo
        'set_features' coincida con el de esta corrida antes de reescribirlas. La
        otra variante (54 o 122) se conserva sin tocar. (Misma lógica que anomalias.py.)
        """
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

    def _persistir_balanceo(self):
        """Guarda la tabla 4.3.4 (SMOTE vs class_weight/nada) idempotente por variante."""
        csv_path = config.RESULTADOS_DIR + r"\metricas_balanceo.csv"
        self._limpiar_variante_csv(csv_path)
        for fila in self.filas_balanceo:
            evaluacion.guardar_metricas(fila, csv_path)
        print("   Tabla de balanceo (4.3.4): {}".format(csv_path))

    def _persistir(self):
        """Guarda modelos, la tabla de métricas de firmas y (fuera) la de balanceo."""
        csv_path = config.RESULTADOS_DIR + r"\metricas_firmas.csv"
        self._limpiar_variante_csv(csv_path)

        for algo, r in self.resultados.items():
            # Un joblib por algoritmo, sufijado por variante (H3) para que 54 y 122
            # coexistan. Guarda TODO lo necesario para el híbrido (el modelo soporta
            # predict_proba: DT/RF/KNN/HistGB lo tienen, y el ImbPipeline lo expone).
            ruta_modelo = config.MODELOS_DIR + r"\firma_{}_{}.joblib".format(
                algo, self.set_features)
            joblib.dump(
                {
                    "algoritmo": algo,
                    "modelo": r["modelo"],
                    "balanceo": r["balanceo"],
                    "config_ganadora": r["config_ganadora"],
                    "f1_macro_cv": r["f1_macro_cv"],
                    "base_path_usado": self.base_path,
                    "set_features": self.set_features,
                    "sin_seleccion": bool(self.sin_seleccion),
                    "n_features": self.n_features,
                    "feature_names": list(self.X_D3.columns),
                    "clases": config.CATEGORIAS_ATAQUE,
                    "tipos_conocidos": sorted(self.tipos_conocidos),
                },
                ruta_modelo,
            )

            # Una fila por algoritmo en la tabla acumulada (→ 5.2.2 / 5.2.3).
            m = r["metricas"]
            fila = {
                "algoritmo": algo,
                "set_features": self.set_features,
                "sin_seleccion": bool(self.sin_seleccion),
                "n_features": self.n_features,
                "balanceo": r["balanceo"],
                "config_ganadora": str(r["config_ganadora"]),
                "f1_macro_cv": round(r["f1_macro_cv"], 6),
                "accuracy_D2": round(m["accuracy"], 6),
                "precision_macro": round(m["precision_macro"], 6),
                "recall_macro": round(m["recall_macro"], 6),
                "f1_macro": round(m["f1_macro"], 6),
                "f1_weighted": round(m["f1_weighted"], 6),
                "n_test": int(len(self.y_D2_eval)),
                "tiempo_s": round(r["tiempo_s"], 2),
            }
            # Métricas por categoría (→ 5.2.2): precision/recall/f1 y soporte de cada clase.
            for clase in config.CATEGORIAS_ATAQUE:
                pc = m["por_clase"].get(clase, {})
                fila["precision_" + clase] = round(pc.get("precision", float("nan")), 6)
                fila["recall_" + clase] = round(pc.get("recall", float("nan")), 6)
                fila["f1_" + clase] = round(pc.get("f1", float("nan")), 6)
                fila["soporte_" + clase] = int(pc.get("soporte", 0))
            evaluacion.guardar_metricas(fila, csv_path)
            print("   Guardado modelo: {}".format(ruta_modelo))

        print("   Tabla de métricas de firmas (5.2): {}".format(csv_path))

    # ------------------------------------------------------------------
    # Orquestación
    # ------------------------------------------------------------------
    def entrenar_todos(self):
        """Ejecuta el pipeline completo de firmas para los cuatro algoritmos."""
        config.setup_utf8()
        config.ensure_dirs()
        self.cargar_datos()
        self._experimento_balanceo()
        self._persistir_balanceo()
        for algo in self.ALGORITMOS:
            self._entrenar_final(algo)
        self._extraer_firmas()
        self._persistir()
        print("=" * 70)
        print("FIRMAS COMPLETADO ({} features)".format(self.set_features))
        print("=" * 70)
        return self.resultados


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Etapa 2 del H-NIDS: detección basada en firmas (4 clasificadores "
                    "multiclase comparados bajo protocolo idéntico sobre NSL-KDD)."
    )
    parser.add_argument(
        "--sin-seleccion", action="store_true",
        help="Usa el set de 122 features (variante sin selección 4.3.5) en lugar "
             "de las 54 por defecto. Para el experimento 54-vs-122 (decisión Q1/C).",
    )
    args = parser.parse_args()

    trainer = NSLKDDSignatureTrainer(sin_seleccion=args.sin_seleccion)
    trainer.entrenar_todos()
