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

# Alcance de la tabla auxiliar de BALANCEO (4.3.4). ALCANCE_SELECCION no le vale:
# su texto habla de 'auc_val' y de 'umbral', dos columnas que metricas_balanceo.csv
# NO tiene (su fila es algoritmo × balanceo y solo trae f1_macro_cv/_cv_std), así
# que describía media tabla ajena y ninguna de las suyas. Este sí dice lo que hay:
# de dónde sale el f1_macro_cv y por qué el SMOTE de esas filas no es leakage.
ALCANCE_BALANCEO = (
    "selección del esquema de balanceo (4.3.4): f1_macro medio en CV sobre D3 "
    "(StratifiedKFold 5 · semilla 42) con SMOTE aplicado SOLO dentro de cada fold "
    "vía imblearn.Pipeline — nunca D2 y nunca citable como resultado"
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

# ---------------------------------------------------------------------------
# La columna 'tiempo_s': tres significados, uno por tabla — declarados en el dato
# ---------------------------------------------------------------------------
# 'tiempo_s' era el último superviviente del defecto que T1 vino a cerrar: mismo
# nombre en tres tablas y tres magnitudes distintas, sin que el dato lo dijese.
# NO se homogeneiza el cálculo y NO se renombra la columna. Las razones (las de
# verdad; la que se alegaba antes —"movería los 5,0/28,3/16,4/40,6 s que cita la
# tabla de 4.4"— era falsa: metricas_anomalias.csv ya publica 5.51/26.17/20.85/
# 52.43 para esas cuatro filas, así que la cita del vault está rota de todos
# modos y no había nada que proteger):
#   - No se RENOMBRA porque el nombre 'tiempo_s' está citado literalmente en la
#     nota de trazabilidad de 4.4 (la lista de columnas de metricas_anomalias.
#     csv), y renombrarlo rompería esa referencia sin ganar nada que el alcance
#     declarado no dé ya.
#   - No se HOMOGENEIZA porque cada cálculo es el que su capítulo describe: el
#     "proceso completo por algoritmo (búsqueda en rejilla, fijación del umbral,
#     evaluación y generación de figuras), no solo el ajuste" es literalmente lo
#     que 4.4 dice que mide su columna Tiempo. Unificar los tres convertiría
#     medidas descritas en el texto en una cuarta que no describe nadie.
# Se hace, pues, lo que T1 hace con todo lo demás: que el dato publicado declare
# su alcance. Cada fila de las cuatro tablas principales lleva una columna
# hermana 'alcance_tiempo_s' con uno de estos textos.
#
# Por eso 'tiempo_s' NO está en ALCANCE_COLUMNAS: ese diccionario da UN alcance
# por nombre de columna y aquí el alcance depende de la tabla. Va en el dato.
#
# LO QUE ESTA DECLARACIÓN NO ARREGLA (léase antes de comparar dos tiempos):
# desde la corrección de T1 la medida se toma con time.perf_counter(), así que la
# RESOLUCIÓN deja de ser el reloj de ~15,6 ms de Windows. La VARIANZA sigue ahí:
# es wall-clock en una máquina no dedicada y entre dos corridas del mismo día se
# observaron factores de hasta 4,4× (OneClassSVM 122: 163,26 s → 37,13 s; KNN 122
# en firmas: 90,22 s → 207,81 s). Las cifras DE PARTIDA de esos dos pares (163,26
# y 90,22) son del esquema de tablas anterior, que ya no está en el árbol de
# trabajo: se recuperan de los CSV versionados en el commit 8b07319 (y
# anteriores). Las de llegada (37,13 y 207,81) están versionadas en 077119e;
# producidas con el código c7cf319, que es lo que declara la columna 'commit' de
# sus filas (metricas_anomalias.csv:7 y metricas_firmas.csv:8) y la referencia
# inequívoca para reproducirlas. Ninguna columna de tiempo es reproducible: son
# comparación relativa de coste y de orden de magnitud, nada más.
# Sin comas (como el resto de ALCANCE_*): estos textos viajan como valor de CSV.
_AVISO_TIEMPO_VARIANZA = (" · wall-clock de pase único en máquina no dedicada: "
                          "varía hasta 4x entre corridas — es orden de magnitud "
                          "y no cifra reproducible")

# anomalias.py y firmas.py: bloque completo del algoritmo.
ALCANCE_TIEMPO_S_BLOQUE_ALGORITMO = (
    "'tiempo_s' = el proceso completo por algoritmo (selección de "
    "hiperparámetros + ajuste + inferencia sobre D2 + figuras) y no solo el "
    "ajuste; para el ajuste solo está 'tiempo_entrenamiento_s' de esta misma "
    "fila" + _AVISO_TIEMPO_VARIANZA
)

# baseline.py: SOLO el GridSearchCV. Es el que rompe la comparación entre tablas.
ALCANCE_TIEMPO_S_SOLO_ENTRENAMIENTO = (
    "'tiempo_s' = SOLO el entrenamiento (GridSearchCV + refit sobre D1+D3): "
    "coincide con 'tiempo_entrenamiento_s' de esta misma fila y NO incluye "
    "inferencia ni figuras — no comparable con el 'tiempo_s' de "
    "metricas_anomalias.csv ni de metricas_firmas.csv" + _AVISO_TIEMPO_VARIANZA
)

# hibrido.py: el tramo de la corrida que va de la carga de datos al cierre de la
# fila resumen. NO es "el script entero": el cronómetro se lee al construir el
# dict metricas_run (hibrido.py:612) y después aún quedan la figura 5x6 la tabla
# 0-day de los cuatro detectores —que vuelve a puntuar D2 con IF + OCSVM + LOF +
# AE y cuesta unos 4-5 s de los ~27 s de la variante de 54— y la escritura de los
# CSV. Por eso el log final del script (hibrido.py:641) imprime una cifra MAYOR
# que esta columna: son dos medidas distintas y el texto lo dice para que nadie
# lea la discrepancia como un error. El cronómetro NO se mueve: reordenar la
# persistencia para que la fila se escriba con su propio tiempo dentro es un
# cambio de código que no aporta nada al dato.
ALCANCE_TIEMPO_S_CARGA_A_CIERRE_FILA = (
    "'tiempo_s' = el tramo de la corrida que va desde la carga de los splits "
    "hasta el cierre de esta fila (carga de D1/D2/D3 + carga de los .joblib de "
    "las dos etapas + calibración OOF sobre D3 + cascada sobre D2 + tabla de "
    "sensibilidad de los 3 umbrales); NO incluye lo que se hace DESPUÉS de "
    "tomar la medida: la figura 5x6 · la tabla 0-day de los cuatro detectores · "
    "la escritura de los CSV — de ahí que el log del script imprima una cifra "
    "mayor que esta; no es tiempo de ajuste —el híbrido no re-entrena— ni "
    "comparable con el 'tiempo_s' de las otras tres tablas"
    + _AVISO_TIEMPO_VARIANZA
)

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
# 'tiempo_s' NO entra aquí a propósito: su alcance depende de la TABLA (tres
# significados; ver el bloque ALCANCE_TIEMPO_S_*) y este diccionario solo sabe dar
# uno por nombre de columna. Se declara en el dato, con 'alcance_tiempo_s'.
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
