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
import subprocess
import sys

# --- Reproducibilidad (decisión 2026-07-02: random_state=42 en TODO) ---
RANDOM_STATE = 42

# --- Rutas base del proyecto ---
RESULTADOS_DIR = r"C:\Users\francisco.lopez\KIKO_TFG\Working_Directory\Resultados"
FIGURAS_DIR = os.path.join(RESULTADOS_DIR, "figuras")
MODELOS_DIR = os.path.join(RESULTADOS_DIR, "modelos")

# Raíz del repositorio (Working_Directory/): este fichero vive en
# Working_Directory/Implementacion/app/config.py → tres niveles arriba.
REPO_DIR = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

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


# ---------------------------------------------------------------------------
# ALCANCE de cada fila de métricas (tarea T1)
# ---------------------------------------------------------------------------
# Problema que resuelve: había columnas HOMÓNIMAS con alcances distintos entre
# tablas. `accuracy_D2` vale 0,9683 en metricas_firmas.csv (4 clases, solo los
# ataques de D2 de tipo conocido) y 0,7395 en metricas_baseline.csv (5 clases,
# D2 entero). Mismo nombre, dos cosas. Desde T1 cada fila declara su alcance en
# una columna `alcance` con estos valores fijos (uno por tabla), de modo que
# ninguna cifra se pueda leer fuera de su contexto ni comparar con otra que no
# le corresponde.
#
# Sin comas: estos textos viajan como valor dentro de un CSV.
ALCANCE_ANOMALIAS = "binario normal-vs-ataque (2 clases) sobre D2 completo"
ALCANCE_FIRMAS = ("multiclase 4 categorías de ataque sobre los ataques de D2 "
                  "de tipo conocido")
ALCANCE_BASELINE = "multiclase 5 clases (normal + 4 ataques) sobre D2 completo"
# El añadido sobre 'tiempo_entrenamiento_s' NO es adorno: es el único sitio del
# DATO publicado donde se avisa de que esa columna homónima no mide lo mismo aquí
# que en las otras tres tablas (el híbrido no re-entrena la cascada; ver
# hibrido.SIGNIFICADO_TIEMPO_ENTRENAMIENTO). La columna NO se renombra: el
# conjunto mínimo homogéneo entre las cuatro tablas es requisito de T1. Así, quien
# lea la fila suelta sin abrir el código ya sabe qué tiene delante.
ALCANCE_HIBRIDO = ("cascada extremo a extremo (5 clases + unknown) sobre D2 "
                   "completo; ojo: 'tiempo_entrenamiento_s' aquí es SOLO la "
                   "calibración de UMBRAL_CONF por OOF sobre D3 — el híbrido no "
                   "re-entrena las dos etapas")
ALCANCE_0DAY = ("recall de marcado como ataque sobre los ataques de D2 de tipo "
                "ausente del train")

# Alcance del bloque `conocida_` del HÍBRIDO. NO es ALCANCE_FIRMAS aunque se
# calcule sobre las mismas filas de D2: en el híbrido la medida es de extremo a
# extremo y los ataques que la etapa 1 no marcó entran como 'normal', así que
# baja respecto a firmas-solo (18 pp en la corrida de 54). Reutilizar el texto
# de firmas hacía parecer la misma medida a dos cosas distintas.
ALCANCE_HIBRIDO_CONOCIDA = (
    "cascada extremo a extremo restringida a los ataques de D2 de tipo conocido "
    "(4 categorías); los ataques que la etapa 1 no marcó como sospechosos "
    "cuentan como 'normal' → NO comparable con la columna homónima de "
    "metricas_firmas.csv"
)

# Alcance de las columnas que salen de la SELECCIÓN DE HIPERPARÁMETROS / del
# ajuste del umbral. No son métricas sobre D2 y no deben leerse como tales:
#   auc_val        (anomalias) AUC-ROC sobre D1_val + muestra de D3
#   umbral         (anomalias) percentil 95 del score sobre D1_val
#   f1_macro_cv    (firmas, baseline, balanceo) f1_macro medio en CV sobre train
# Son sistemáticamente MÁS ALTAS que la métrica homóloga sobre D2 (IsolationForest
# 54: auc_val 0.9918 vs roc_auc 0.9229; baseline 54: f1_macro_cv 0.9094 vs
# f1_macro 0.4721), así que sin alcance propio invitan a citarlas como resultado.
ALCANCE_SELECCION = (
    "selección de hiperparámetros / ajuste del umbral: CV sobre el train "
    "(D3 o D1+D3); auc_val sobre D1_val + muestra de D3; umbral sobre D1_val "
    "solo — NUNCA D2"
)

ALCANCE_HIBRIDO_CALIBRACION = (
    "sensibilidad de UMBRAL_CONF: las columnas 'oof_' son out-of-fold sobre D3 "
    "y de ellas SALE la decisión; las columnas 'd2_' son sobre D2 completo y "
    "solo se REPORTAN (nunca deciden)"
)

# Los dos bloques de esa fila mixta, por separado.
ALCANCE_OOF_D3 = ("out-of-fold sobre D3 (StratifiedKFold 5 · semilla 42): de aquí "
                  "SALE la decisión de UMBRAL_CONF — nunca D2")
ALCANCE_D2_REPORTE = ("sobre D2 completo y SOLO como reporte: ninguna decisión se "
                      "toma con estas columnas (P-4)")

# Convención de PREFIJOS y SUFIJOS de columna, complementaria a `alcance`. Una
# fila puede llevar más de un bloque de métricas; `alcance` describe el bloque
# PRINCIPAL (las columnas sin prefijo) y estos marcadores identifican los
# bloques secundarios, con el mismo significado en las cuatro tablas.
#
# ALCANCE (de este bloque): es DOCUMENTACIÓN, y está bien que lo sea. Ninguna de
# estas tres tablas (ALCANCE_PREFIJOS / ALCANCE_SUFIJOS / ALCANCE_COLUMNAS) la
# comprueba el código: validar_esquema_minimo() solo llega a alcance_de_columna()
# para columnas que casan con PREFIJOS_SIN_DECLARAR, y ninguna clave de aquí
# ('bin_', 'conocida_', 'recall_0day', '_cv', '_cv_std', '_val', 'umbral') puede
# casar con ese filtro. El único diccionario que el aviso resuelve de verdad es
# ALCANCE_PREFIJOS_AUXILIARES. Se declaran igual porque son el vocabulario que
# la memoria cita (A.3) y el que siguen los scripts al nombrar sus columnas.
ALCANCE_PREFIJOS = {
    "bin_": ALCANCE_ANOMALIAS,
    "conocida_": ALCANCE_HIBRIDO_CONOCIDA,
    "recall_0day": ALCANCE_0DAY,
}

# Prefijos que solo aparecen en las tablas AUXILIARES (hoy, la de calibración del
# híbrido, cuya fila cruza los dos alcances a propósito). "Solo" es literal: en
# una tabla PRINCIPAL no se resuelven (alcance_de_columna(..., incluir_auxiliares
# =False)) y validar_esquema_minimo() avisa, porque un 'oof_' —columna del train—
# dentro de metricas_firmas.csv, cuyo alcance dice "sobre los ataques de D2",
# sería exactamente la mezcla de alcances que T1 cierra.
ALCANCE_PREFIJOS_AUXILIARES = {
    "oof_": ALCANCE_OOF_D3,
    "d2_": ALCANCE_D2_REPORTE,
}

# Sufijos: todo lo que termina en _cv / _cv_std / _val viene del train (nunca D2).
ALCANCE_SUFIJOS = {
    "_cv": ALCANCE_SELECCION,
    "_cv_std": ALCANCE_SELECCION,
    "_val": ALCANCE_SELECCION,
}

# Columnas concretas con alcance propio que no encajan en prefijo ni sufijo.
ALCANCE_COLUMNAS = {
    "umbral": ALCANCE_SELECCION,
}

# Marcadores que PARECEN de alcance y se vigilan: si una columna empieza por uno
# de estos y el vocabulario declarado no sabe resolverla, es una columna de otro
# alcance colada sin declarar y validar_esquema_minimo() avisa.
PREFIJOS_SIN_DECLARAR = ("oof_", "d2_", "cv_", "val_", "train_", "d1_", "d3_")


def alcance_de_columna(columna, incluir_auxiliares=True):
    """
    Alcance de UNA columna según el vocabulario de prefijos/sufijos declarado.

    Devuelve None si la columna no lleva marcador: entonces su alcance es el
    PRINCIPAL de la fila (el de la columna `alcance`).

    incluir_auxiliares : bool
        Si False, ALCANCE_PREFIJOS_AUXILIARES NO se consulta, así que 'oof_' y
        'd2_' quedan sin resolver. Lo usa validar_esquema_minimo() con las tablas
        PRINCIPALES: ahí esos prefijos no tienen sitio (son de la tabla de
        calibración del híbrido) y deben disparar el aviso, no resolverse.
    """
    for prefijo, alcance in ALCANCE_PREFIJOS.items():
        if columna.startswith(prefijo):
            return alcance
    if incluir_auxiliares:
        for prefijo, alcance in ALCANCE_PREFIJOS_AUXILIARES.items():
            if columna.startswith(prefijo):
                return alcance
    for sufijo, alcance in ALCANCE_SUFIJOS.items():
        if columna.endswith(sufijo):
            return alcance
    return ALCANCE_COLUMNAS.get(columna)


# ---------------------------------------------------------------------------
# Procedencia por fila (tarea T1): semilla y commit viajan CON el dato
# ---------------------------------------------------------------------------
_COMMIT_CACHE = None


# Alcance del `git status` que decide el sufijo '-sucio': SOLO el código
# (`Implementacion/`). Motivo: los propios scripts escriben en `Resultados/`
# (figuras, CSV de métricas) durante la corrida y esas rutas están versionadas,
# así que un `git status` de todo el árbol daría '-sucio' SIEMPRE —incluso
# partiendo de un checkout limpio— en cuanto se hubiese guardado la primera
# figura, y la columna `commit` perdería su capacidad de discriminar. Limitarlo
# al código es además lo que la columna quiere decir: con qué versión del código
# se produjo la fila. Así da igual el orden en que se llame a commit_actual().
_RUTA_SUCIEDAD = "Implementacion"


def commit_actual():
    """
    Hash corto del commit de `Working_Directory/` en el momento de la corrida,
    con sufijo '-sucio' si hay cambios sin commitear EN EL CÓDIGO
    (`Implementacion/`; ver _RUTA_SUCIEDAD para el motivo del acotado).

    Tres valores posibles en la columna `commit` de las tablas (documentados
    también en PIPELINE.md, junto al runbook):
      '<hash>'                        código sin cambios sin commitear
      '<hash>-sucio'                  había cambios en `Implementacion/`
      '<hash>-suciedad_desconocida'   el hash es válido pero el `git status` falló
                                      o agotó el timeout: suciedad indeterminada

    Se cachea (una sola invocación de git por proceso). Si git no está
    disponible o el directorio no es un repositorio, devuelve 'desconocido':
    la procedencia se degrada, nunca rompe la corrida. Solo lectura.
    """
    global _COMMIT_CACHE
    if _COMMIT_CACHE is not None:
        return _COMMIT_CACHE

    def _git(*args):
        return subprocess.run(
            ("git",) + args, cwd=REPO_DIR, capture_output=True, text=True,
            timeout=15, check=True,
        ).stdout.strip()

    # Dos try SEPARADOS a propósito: un `status` que agote el timeout o falle no
    # debe tirar el hash que ya se había obtenido (el árbol arrastra ~1,1 GB de
    # ficheros ignorados y `status` es mucho más caro que `rev-parse`). En ese
    # caso se conserva el hash y se marca la suciedad como indeterminada.
    try:
        commit = _git("rev-parse", "--short", "HEAD")
    except (OSError, UnicodeDecodeError, subprocess.SubprocessError):
        _COMMIT_CACHE = "desconocido"
        return _COMMIT_CACHE

    try:
        if _git("status", "--porcelain", "--", _RUTA_SUCIEDAD):
            commit += "-sucio"
    except (OSError, UnicodeDecodeError, subprocess.SubprocessError):
        commit += "-suciedad_desconocida"

    _COMMIT_CACHE = commit
    return commit


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
