# -*- coding: utf-8 -*-
"""
config.py — Configuración central de los modelos del TFG H-NIDS (decisión Q2).

Consumido por evaluacion.py, anomalias.py, firmas.py e hibrido.py. Centraliza
rutas, semilla y convenciones de clase para que sean IDÉNTICAS en los tres
modelos y no queden hardcodeadas (cierra la deuda 3.2 🟠 para el código nuevo).

program.py / validacion.py NO dependen de este módulo: funcionan y están
APROBADOS; solo migrarán sus rutas aquí si en algún momento se tocan.
"""
import os
import sys

# --- Reproducibilidad (decisión 2026-07-02: random_state=42 en TODO) ---
RANDOM_STATE = 42

# --- Rutas base del proyecto ---
RESULTADOS_DIR = r"C:\Users\francisco.lopez\KIKO_TFG\Working_Directory\Resultados"
FIGURAS_DIR = os.path.join(RESULTADOS_DIR, "figuras")
MODELOS_DIR = os.path.join(RESULTADOS_DIR, "modelos")

# --- Prefijos de los CSV procesados (decisión Q1/C: features parametrizables) ---
# 54 features = selección 4.3.5 aplicada (por defecto).
# 122 features = variante sin selección (generada con `program.py --sin-seleccion`).
# Los scripts de modelos eligen el set vía flag, no reescribiendo código.
BASE_PATH_54 = os.path.join(RESULTADOS_DIR, "specialized_nsl_kdd")
BASE_PATH_122 = os.path.join(RESULTADOS_DIR, "specialized_nsl_kdd_sin_seleccion")


def base_path(sin_seleccion=False):
    """Prefijo de los CSV procesados según la variante de features (Q1/C)."""
    return BASE_PATH_122 if sin_seleccion else BASE_PATH_54


# --- Convenciones de clase (decisión Q3) — únicas para los tres modelos ---
# Binario: positivo = ataque = 1, normal = 0.
CLASE_NORMAL = 0
CLASE_ATAQUE = 1
ETIQUETA_NORMAL = "normal"
ETIQUETA_UNKNOWN = "unknown"  # solo la produce el híbrido (baja confianza / 0-day)

# Orden FIJO de categorías para matrices de confusión y reportes.
CATEGORIAS_ATAQUE = ["dos", "probe", "r2l", "u2r"]                  # 4 clases de firmas (D3)
CATEGORIAS_MULTICLASE = [ETIQUETA_NORMAL] + CATEGORIAS_ATAQUE       # 5 clases
CATEGORIAS_HIBRIDO = CATEGORIAS_MULTICLASE + [ETIQUETA_UNKNOWN]     # 6 (con 0-day)


def ensure_dirs():
    """Crea los directorios de salida si no existen."""
    for d in (RESULTADOS_DIR, FIGURAS_DIR, MODELOS_DIR):
        os.makedirs(d, exist_ok=True)


def setup_utf8():
    """Fuerza salida UTF-8 en consolas Windows (mismo patrón que program.py):
    sin esto los prints con emojis cascan con cp1252."""
    if sys.stdout.encoding and sys.stdout.encoding.lower().replace("-", "") != "utf8":
        try:
            sys.stdout.reconfigure(encoding="utf-8")
            sys.stderr.reconfigure(encoding="utf-8")
        except (AttributeError, ValueError):
            # stdout no reconfigurable (p. ej. redirigido): se continúa sin forzar
            pass
