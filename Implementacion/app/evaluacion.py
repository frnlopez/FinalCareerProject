# -*- coding: utf-8 -*-
"""
evaluacion.py — Módulo común de evaluación del TFG H-NIDS (decisión Q3).

Funciones reutilizadas por anomalias.py, firmas.py e hibrido.py para no
triplicar el cálculo de métricas ni el guardado de figuras/tablas. Todas las
convenciones de clase (positivo = ataque = 1, orden de categorías) viven en
config.py; aquí solo se consumen.

Contrato (Q3):
  - evaluar_binario(y_true, y_pred, y_score=None)      -> dict
  - evaluar_multiclase(y_true, y_pred, labels=None)    -> dict
  - evaluar_0day_por_tipo(y_tipo_real, es_sospechoso, tipos_0day) -> dict
  - plot_matriz_confusion(y_true, y_pred, labels, ...) -> ruta PNG
  - plot_roc_pr(scores_por_algo, y_true, ...)          -> dict de AUCs
  - guardar_metricas(fila, csv_path)                   -> None (append)
"""
import os
from datetime import datetime

import numpy as np
import pandas as pd

import matplotlib
matplotlib.use("Agg")  # backend no interactivo: nunca bloquea (nada de plt.show)
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import (
    precision_recall_fscore_support,
    confusion_matrix,
    classification_report,
    roc_auc_score,
    average_precision_score,
    roc_curve,
    precision_recall_curve,
    accuracy_score,
)

import config


# ---------------------------------------------------------------------------
# Métricas binarias (normal vs ataque) — usadas por anomalias.py e hibrido.py
# ---------------------------------------------------------------------------
def evaluar_binario(y_true, y_pred, y_score=None):
    """
    Métricas del problema binario normal(0) vs ataque(1).

    Parameters
    ----------
    y_true, y_pred : array-like de {0, 1}
        Etiquetas y predicciones (positivo = ataque = 1, ver config).
    y_score : array-like, opcional
        Puntuación continua donde MAYOR = más probable ataque (p. ej. el
        anomaly_score ya negado). Si se aporta, se calculan AUC-ROC y AUC-PR
        (independientes del umbral).

    Returns
    -------
    dict con precision/recall/f1 de la clase ataque, accuracy, FPR real,
    la matriz de confusión 2x2 (tn, fp, fn, tp) y, si hay y_score, roc_auc/pr_auc.
    """
    y_true = np.asarray(y_true).ravel()
    y_pred = np.asarray(y_pred).ravel()

    # pos_label=ataque para que precision/recall se refieran a detectar ataques
    p, r, f1, _ = precision_recall_fscore_support(
        y_true, y_pred, labels=[config.CLASE_ATAQUE],
        pos_label=config.CLASE_ATAQUE, average="binary", zero_division=0,
    )
    cm = confusion_matrix(y_true, y_pred, labels=[config.CLASE_NORMAL, config.CLASE_ATAQUE])
    tn, fp, fn, tp = cm.ravel()
    fpr = fp / (fp + tn) if (fp + tn) > 0 else 0.0

    resultado = {
        "precision": float(p),
        "recall": float(r),          # = TPR / tasa de detección de ataques
        "f1": float(f1),
        "accuracy": float(accuracy_score(y_true, y_pred)),
        "fpr": float(fpr),           # tasa de falsas alarmas sobre tráfico normal
        "tn": int(tn), "fp": int(fp), "fn": int(fn), "tp": int(tp),
    }
    if y_score is not None:
        y_score = np.asarray(y_score).ravel()
        # Requiere ambas clases presentes en y_true
        if len(np.unique(y_true)) == 2:
            resultado["roc_auc"] = float(roc_auc_score(y_true, y_score))
            resultado["pr_auc"] = float(average_precision_score(y_true, y_score))
        else:
            resultado["roc_auc"] = float("nan")
            resultado["pr_auc"] = float("nan")
    return resultado


# ---------------------------------------------------------------------------
# Métricas multiclase — usadas por firmas.py (4 clases) e hibrido.py (5-6)
# ---------------------------------------------------------------------------
def evaluar_multiclase(y_true, y_pred, labels=None):
    """
    Métricas multiclase con orden de etiquetas FIJO (config).

    Parameters
    ----------
    y_true, y_pred : array-like de etiquetas string (p. ej. 'dos', 'probe'...).
    labels : list, opcional
        Orden explícito de clases. Si None, se usa el orden observado ordenado.

    Returns
    -------
    dict con precision/recall/f1 por clase, macro y weighted, la matriz de
    confusión (con sus labels) y el classification_report como texto.
    """
    y_true = np.asarray(y_true).ravel()
    y_pred = np.asarray(y_pred).ravel()
    if labels is None:
        labels = sorted(set(np.unique(y_true)) | set(np.unique(y_pred)))

    p, r, f1, soporte = precision_recall_fscore_support(
        y_true, y_pred, labels=labels, zero_division=0,
    )
    p_macro, r_macro, f1_macro, _ = precision_recall_fscore_support(
        y_true, y_pred, labels=labels, average="macro", zero_division=0,
    )
    p_w, r_w, f1_w, _ = precision_recall_fscore_support(
        y_true, y_pred, labels=labels, average="weighted", zero_division=0,
    )
    cm = confusion_matrix(y_true, y_pred, labels=labels)

    por_clase = {
        clase: {
            "precision": float(p[i]),
            "recall": float(r[i]),
            "f1": float(f1[i]),
            "soporte": int(soporte[i]),
        }
        for i, clase in enumerate(labels)
    }
    return {
        "labels": list(labels),
        "por_clase": por_clase,
        "precision_macro": float(p_macro),
        "recall_macro": float(r_macro),
        "f1_macro": float(f1_macro),
        "precision_weighted": float(p_w),
        "recall_weighted": float(r_w),
        "f1_weighted": float(f1_w),
        "accuracy": float(accuracy_score(y_true, y_pred)),
        "matriz_confusion": cm,
        "classification_report": classification_report(
            y_true, y_pred, labels=labels, zero_division=0,
        ),
    }


# ---------------------------------------------------------------------------
# Recall 0-day por tipo (decisión Q3/C) — métrica que resuelve H1 y alimenta 5.3
# ---------------------------------------------------------------------------
def evaluar_0day_por_tipo(y_tipo_real, es_sospechoso, tipos_0day):
    """
    Fracción de cada tipo de ataque 0-day que la etapa 1 (anomalías) marca como
    sospechoso. Es la métrica de decisión del experimento 54-vs-122 (decisión C)
    y el análisis central del híbrido (§6.5).

    Parameters
    ----------
    y_tipo_real : array-like
        Tipo de ataque específico por muestra (columna 'attack_original' de D2).
    es_sospechoso : array-like de bool
        Salida binaria de la etapa 1 (True = marcado como anomalía/ataque).
    tipos_0day : iterable
        Tipos de ataque presentes en D2 y AUSENTES del train (los "0-day").
        Se calculan en runtime: set(tipos D2) - {'normal'} - set(tipos D3).

    Returns
    -------
    dict {tipo: {'n': soporte, 'detectados': int, 'recall': float}} + clave
    '__global__' con el recall agregado sobre todos los 0-day.
    """
    y_tipo_real = np.asarray(y_tipo_real).ravel()
    es_sospechoso = np.asarray(es_sospechoso).ravel().astype(bool)

    resultado = {}
    total_n = total_det = 0
    for tipo in sorted(tipos_0day):
        mask = (y_tipo_real == tipo)
        n = int(mask.sum())
        detectados = int(es_sospechoso[mask].sum())
        resultado[tipo] = {
            "n": n,
            "detectados": detectados,
            "recall": float(detectados / n) if n > 0 else float("nan"),
        }
        total_n += n
        total_det += detectados
    resultado["__global__"] = {
        "n": total_n,
        "detectados": total_det,
        "recall": float(total_det / total_n) if total_n > 0 else float("nan"),
    }
    return resultado


# ---------------------------------------------------------------------------
# Figuras — todas a FIGURAS_DIR, 300 dpi, títulos en español (van a la memoria)
# ---------------------------------------------------------------------------
def plot_matriz_confusion(y_true, y_pred, labels, titulo, filename, normalizar=False):
    """
    Guarda la matriz de confusión como heatmap. `filename` es solo el nombre
    (se resuelve contra FIGURAS_DIR). Devuelve la ruta absoluta del PNG.
    """
    config.ensure_dirs()
    cm = confusion_matrix(y_true, y_pred, labels=labels)
    if normalizar:
        with np.errstate(all="ignore"):
            cm_norm = cm.astype(float) / cm.sum(axis=1, keepdims=True)
            cm_norm = np.nan_to_num(cm_norm)
        datos, fmt = cm_norm, ".2f"
    else:
        datos, fmt = cm, "d"

    fig, ax = plt.subplots(figsize=(1.6 * len(labels) + 2, 1.4 * len(labels) + 2))
    sns.heatmap(datos, annot=True, fmt=fmt, cmap="Blues", cbar=True,
                xticklabels=labels, yticklabels=labels, ax=ax)
    ax.set_xlabel("Predicción")
    ax.set_ylabel("Real")
    ax.set_title(titulo)
    fig.tight_layout()
    ruta = os.path.join(config.FIGURAS_DIR, filename)
    fig.savefig(ruta, dpi=300, bbox_inches="tight")
    plt.close(fig)
    return ruta


def plot_roc_pr(scores_por_algo, y_true, nombre_fig, titulo=""):
    """
    Superpone las curvas ROC y PR de varios algoritmos para la clase ataque.

    Parameters
    ----------
    scores_por_algo : dict {nombre_algo: y_score}
        y_score con MAYOR = más probable ataque.
    y_true : array-like {0, 1}
    nombre_fig : str
        Base del nombre; genera <base>_roc.png y <base>_pr.png en FIGURAS_DIR.

    Returns
    -------
    dict {algo: {'roc_auc': ..., 'pr_auc': ...}}
    """
    config.ensure_dirs()
    y_true = np.asarray(y_true).ravel()
    aucs = {}

    # ROC
    fig_roc, ax_roc = plt.subplots(figsize=(7, 6))
    for algo, score in scores_por_algo.items():
        score = np.asarray(score).ravel()
        fpr, tpr, _ = roc_curve(y_true, score, pos_label=config.CLASE_ATAQUE)
        auc = roc_auc_score(y_true, score)
        aucs.setdefault(algo, {})["roc_auc"] = float(auc)
        ax_roc.plot(fpr, tpr, label=f"{algo} (AUC={auc:.3f})")
    ax_roc.plot([0, 1], [0, 1], "k--", alpha=0.4, label="Aleatorio")
    ax_roc.set_xlabel("Tasa de falsos positivos (FPR)")
    ax_roc.set_ylabel("Tasa de verdaderos positivos (TPR)")
    ax_roc.set_title(f"Curvas ROC{' — ' + titulo if titulo else ''}")
    ax_roc.legend(loc="lower right")
    fig_roc.tight_layout()
    ruta_roc = os.path.join(config.FIGURAS_DIR, f"{nombre_fig}_roc.png")
    fig_roc.savefig(ruta_roc, dpi=300, bbox_inches="tight")
    plt.close(fig_roc)

    # Precision-Recall
    fig_pr, ax_pr = plt.subplots(figsize=(7, 6))
    for algo, score in scores_por_algo.items():
        score = np.asarray(score).ravel()
        prec, rec, _ = precision_recall_curve(y_true, score, pos_label=config.CLASE_ATAQUE)
        ap = average_precision_score(y_true, score)
        aucs.setdefault(algo, {})["pr_auc"] = float(ap)
        ax_pr.plot(rec, prec, label=f"{algo} (AP={ap:.3f})")
    ax_pr.set_xlabel("Recall")
    ax_pr.set_ylabel("Precision")
    ax_pr.set_title(f"Curvas Precision-Recall{' — ' + titulo if titulo else ''}")
    ax_pr.legend(loc="lower left")
    fig_pr.tight_layout()
    ruta_pr = os.path.join(config.FIGURAS_DIR, f"{nombre_fig}_pr.png")
    fig_pr.savefig(ruta_pr, dpi=300, bbox_inches="tight")
    plt.close(fig_pr)

    return aucs


# ---------------------------------------------------------------------------
# Tabla única acumulada de experimentos (roadmap 3.1-D)
# ---------------------------------------------------------------------------
def guardar_metricas(fila, csv_path):
    """
    Añade una fila (dict) a un CSV acumulado, una fila por experimento. Se
    inserta una columna 'fecha' automáticamente. Ese CSV es la "tabla única"
    de la que salen las comparativas del capítulo de Resultados.

    Nota: para columnas consistentes, pasar siempre el mismo conjunto de claves
    por CSV (algoritmo, params, métricas). Si el fichero no existe, se crea con
    cabecera; si existe, se hace append sin cabecera.
    """
    fila = dict(fila)
    fila.setdefault("fecha", datetime.now().isoformat(timespec="seconds"))
    os.makedirs(os.path.dirname(csv_path) or ".", exist_ok=True)
    df_fila = pd.DataFrame([fila])
    if os.path.exists(csv_path):
        df_fila.to_csv(csv_path, mode="a", header=False, index=False)
    else:
        df_fila.to_csv(csv_path, index=False)
