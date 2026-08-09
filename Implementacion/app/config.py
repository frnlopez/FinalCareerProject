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
#
# Segundo aviso que viaja en el dato: 'fpr_cascada' y 'bin_fpr' son literalmente
# el mismo número en la misma fila (hibrido.py los redondea del mismo b["fpr"]).
# No es un fallo: la etapa 2 solo reclasifica lo que la etapa 1 marcó y NUNCA
# devuelve un flujo a 'normal' así que la cascada no puede tener otro FPR que el
# de su etapa 1. Se conservan las DOS columnas —'bin_fpr' cierra el bloque binario
# que pide H-5 y 'fpr_cascada' es el FPR que P-2 exige junto al titular de 0-day—
# pero T1 no admite dos nombres para una magnitud sin declararlo. Se declara aquí.
ALCANCE_HIBRIDO = ("cascada extremo a extremo (5 clases + unknown) sobre D2 "
                   "completo; ojo: 'tiempo_entrenamiento_s' aquí es SOLO la "
                   "calibración de UMBRAL_CONF por OOF sobre D3 — el híbrido no "
                   "re-entrena las dos etapas. Y ojo también: 'fpr_cascada' y "
                   "'bin_fpr' son EL MISMO NÚMERO por construcción y no dos "
                   "medidas — la etapa 2 solo reclasifica los flujos que la etapa "
                   "1 marcó como sospechosos y nunca devuelve uno a 'normal' así "
                   "que el FPR de la cascada es por fuerza el de la etapa 1; se "
                   "publican las dos porque P-2 pide el FPR junto al titular de "
                   "0-day y H-5 pide el bloque binario completo")
ALCANCE_0DAY = ("recall de marcado como ataque sobre los ataques de D2 de tipo "
                "ausente del train")

# Alcance del bloque `conocida_` del HÍBRIDO. NO es ALCANCE_FIRMAS aunque se
# calcule sobre las mismas filas de D2: en el híbrido la medida es de extremo a
# extremo y los ataques que la etapa 1 no marcó entran como 'normal', así que
# baja respecto a firmas-solo. Cuánto baja depende de QUÉ métrica se mire, así que
# la cifra va con nombre y con corrida: RECALL MACRO, corrida 1163c90, variante de
# 54: 0,850 (RandomForest en metricas_firmas.csv) -> 0,671 ('conocida_recall_macro'
# en metricas_hibrido.csv), 17,9 pp. Antes aquí ponía "18 pp" a secas y era
# indistinguible de un error: con f1_macro la misma caída son 7,4 pp (0,822 ->
# 0,748). Reutilizar el texto de firmas hacía parecer la misma medida a dos cosas
# distintas.
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
# La columna 'tiempo_s': tres cálculos y cuatro declaraciones — en el dato
# ---------------------------------------------------------------------------
# 'tiempo_s' era el último superviviente del defecto que T1 vino a cerrar: mismo
# nombre en tres tablas y tres magnitudes distintas, sin que el dato lo dijese.
# Los CÁLCULOS son tres (bloque completo del algoritmo · solo entrenamiento ·
# tramo carga→cierre de fila) y los TEXTOS cuatro: anomalias.py y firmas.py
# comparten cálculo y NO comparten composición, así que un texto único no dejaba
# reconstruir ninguno de los dos. Cada fila de las cuatro tablas principales lleva
# una columna hermana 'alcance_tiempo_s' con uno de estos textos.
#
# NO se renombra la columna (la nota de trazabilidad de 4.4 la cita por su nombre)
# y NO se homogeneiza el cálculo (cada uno es el que describe su capítulo).
# Por eso 'tiempo_s' NO está en ALCANCE_COLUMNAS: ese diccionario da UN alcance
# por nombre de columna y aquí el alcance depende de la tabla. Va en el dato.
#
# ---------------------------------------------------------------------------
# REGLA DE T18 — QUÉ PUEDE ESCRIBIRSE EN ESTOS CUATRO TEXTOS
# ---------------------------------------------------------------------------
# Solo lo ESTABLE, es decir lo que se deduce del código y no de ninguna corrida:
#   - qué tramos entran en 'tiempo_s' y cuáles quedan fuera;
#   - qué columna mide cada tramo y cuál sale por resta;
#   - el aviso de P9 sobre qué mide (y qué NO) la latencia.
# PROHIBIDO en estos textos: porcentajes, bandas, factores de dispersión, cifras
# de ninguna corrida y cualquier atribución causal. Motivo (T18): publicar
# interpretación DENTRO del dato crea un bucle — el dato no se puede editar sin
# re-correr y cada corrida nueva falsa la cifra que dejó la anterior, que es
# exactamente lo que le pasó a las tres redacciones anteriores de este bloque
# (las cotas "27-49 %" y "varía hasta 4x" nacieron falsables y se falsaron). Y de
# paso la celda 'alcance_tiempo_s' llegó a ~3,2 kB por fila en un CSV de 9 líneas.
# TODOS los números interpretativos viven ahora en Implementacion/PIPELINE.md,
# sección "Las columnas de tiempo: qué miden y hasta dónde valen", anclados al
# commit de la corrida de la que salen: allí son editables sin re-correr nada.
# ---------------------------------------------------------------------------
#
# POR QUÉ perf_counter. Los cuatro scripts miden con time.perf_counter() y no con
# time.time(), que en Windows tiene una resolución de ~15,6 ms — suficiente para
# publicar un 'latencia_ms_por_flujo' = 0,0 en el predict del DecisionTree. La
# prueba, con sus cifras y su corrida, está en PIPELINE.md. perf_counter es
# monótono y NO tiene época: solo sirve para diferencias (la columna 'fecha' la
# sigue dando datetime.now()).
#
# LO QUE perf_counter NO ARREGLA: la varianza. Es wall-clock en una máquina no
# dedicada. Aquí NO se declara ninguna cota ni ningún factor; la dispersión medida
# entre las corridas que hay en git está tabulada en PIPELINE.md.
# Sin comas: estos textos viajan como valor dentro de un CSV.
_AVISO_TIEMPO_VARIANZA = (
    " · wall-clock de un pase único en máquina no dedicada: NO es reproducible ni "
    "comparable entre corridas y NO es una propiedad del algoritmo — vale como "
    "orden de magnitud y como comparación relativa DENTRO de esta misma corrida. "
    "La dispersión medida entre corridas y el umbral por debajo del cual una "
    "diferencia entre dos filas no significa nada están tabulados en "
    "Implementacion/PIPELINE.md sección 'Las columnas de tiempo: qué miden y "
    "hasta dónde valen' — anclados al commit de cada corrida y NO aquí a "
    "propósito: una cifra dentro del dato no se puede corregir sin re-correr"
)

# Lo que NO entra en la inferencia medida. Va pegado a los cuatro alcances de
# tiempo porque acompaña al par (latencia, caudal) que publica cada fila: sin esta
# frase, citar el caudal del DecisionTree como capacidad operativa sería
# exactamente la Lab-Only Evaluation que denuncia el pitfall P9.
_AVISO_LATENCIA_SOLO_PREDICT = (
    " · 'latencia_ms_por_flujo' y 'flujos_por_segundo' miden SOLO el predict/score "
    "sobre características ya calculadas y ya en memoria: NO incluyen captura de "
    "tráfico · ensamblado del flujo · extracción de las 41 características "
    "—donde vive el coste real de un despliegue— así que no son capacidad "
    "operativa del sistema"
)

# anomalias.py: bloque completo del algoritmo. El tramo que no es ajuste ni
# inferencia sobre D2 es grande y estaba sin declarar; desde T1 sus dos
# componentes principales se MIDEN y se publican como columnas propias
# ('tiempo_score_seleccion_s' y 'tiempo_score_umbral_s'), de modo que el reparto
# se lee de la propia fila y no hace falta estimarlo ni publicarlo aquí.
ALCANCE_TIEMPO_S_BLOQUE_ANOMALIAS = (
    "'tiempo_s' = el bloque completo del algoritmo. Sus cinco tramos principales "
    "en orden de ejecución: (1) los fit del grid — y solo ellos son "
    "'tiempo_entrenamiento_s' — (2) puntuar el set de validación etiquetado "
    "(D1_val + la muestra de D3) UNA VEZ POR CONFIGURACIÓN del grid = "
    "'tiempo_score_seleccion_s' (3) puntuar D1_val para fijar el umbral p95 = "
    "'tiempo_score_umbral_s' (4) la inferencia sobre D2 = 'tiempo_inferencia_s' y "
    "(5) la cola de evaluar_binario + UNA figura —la matriz de confusión; la de "
    "curvas ROC/PR se dibuja al final del script y queda fuera—. 'Principales' es "
    "literal: dentro de la misma ventana caen también el submuestreo de "
    "OneClassSVM · la construcción del estimador en cada iteración del grid y un "
    "roc_auc_score por configuración — despreciables pero no nulos — así que el "
    "tramo (5) no tiene columna propia: es lo que queda al restar de 'tiempo_s' "
    "las cuatro columnas de tiempo anteriores. El reparto entre tramos se LEE de "
    "las columnas de esta misma fila y no se estima. AVISO al reconstruirlo: los "
    "tramos (2) (3) y (4) miden la MISMA operación sobre conjuntos de tamaño "
    "distinto así que un cociente CRUDO entre dos de ellos NO es un cociente de "
    "coste por flujo: hay que dividirlo por la razón de tamaños de sus conjuntos "
    "antes de leerlo — y aun normalizado sigue siendo wall-clock de un pase único "
    "en una corrida que no controla ni el estado de caché ni la carga de la "
    "máquina ni n_jobs. La comparación normalizada está en PIPELINE.md anclada a "
    "su corrida"
    + _AVISO_TIEMPO_VARIANZA + _AVISO_LATENCIA_SOLO_PREDICT
)

# firmas.py: mismo cálculo que el de anomalías y otra composición. Aquí el
# residual es UN SOLO tramo con coste apreciable —la cola de métricas + figura—
# así que sale EXACTO por resta de las tres columnas publicadas y no necesita
# columna propia. La selección de balanceo (4.3.4) NO está dentro.
ALCANCE_TIEMPO_S_BLOQUE_FIRMAS = (
    "'tiempo_s' = el bloque completo del algoritmo. Sus tres tramos en orden de "
    "ejecución: (1) el GridSearchCV con el balanceo ganador + el refit sobre todo "
    "D3 = 'tiempo_entrenamiento_s' (2) el predict sobre los flujos de D2 de tipo "
    "conocido = 'tiempo_inferencia_s' y (3) la cola de evaluar_multiclase + UNA "
    "figura —la matriz de confusión 4x4—. El (3) no lleva columna propia porque "
    "sale EXACTO "
    "restando de 'tiempo_s' las otras dos columnas de tiempo —salvo dos "
    "menudencias que caen en la misma ventana: leer busqueda.best_estimator_ y "
    "dos print—. NO incluye el mini-experimento de balanceo de 4.3.4 que corre "
    "antes y se publica en metricas_balanceo.csv"
    + _AVISO_TIEMPO_VARIANZA + _AVISO_LATENCIA_SOLO_PREDICT
)

# baseline.py: SOLO el GridSearchCV. Es el que rompe la comparación entre tablas.
# Dentro de la ventana del cronómetro solo hay la construcción del estimador y el
# GridSearchCV.fit, así que el residual 'tiempo_s' − 'tiempo_entrenamiento_s' es
# cero por construcción (salvo redondeo).
ALCANCE_TIEMPO_S_SOLO_ENTRENAMIENTO = (
    "'tiempo_s' = SOLO el entrenamiento (GridSearchCV + refit sobre D1+D3): "
    "coincide con 'tiempo_entrenamiento_s' de esta misma fila —el residual entre "
    "las dos columnas es cero salvo redondeo— y NO incluye inferencia ni figuras "
    "— no comparable con el 'tiempo_s' de metricas_anomalias.csv ni de "
    "metricas_firmas.csv" + _AVISO_TIEMPO_VARIANZA + _AVISO_LATENCIA_SOLO_PREDICT
)

# hibrido.py: el tramo de la corrida que va de la carga de datos al cierre de la
# fila resumen. NO es "el script entero": el cronómetro se lee al construir el
# dict metricas_run y después aún quedan la figura 5x6 la tabla 0-day de los
# cuatro detectores y la escritura de los CSV. Por eso el log final del script
# imprime una cifra MAYOR que esta columna: son dos medidas distintas y el texto
# lo dice para que nadie lea la discrepancia como un error. El cronómetro NO se
# mueve: reordenar la persistencia para que la fila se escriba con su propio
# tiempo dentro es un cambio de código que no aporta nada al dato.
ALCANCE_TIEMPO_S_CARGA_A_CIERRE_FILA = (
    "'tiempo_s' = el tramo de la corrida que va desde la carga de los splits "
    "hasta el cierre de esta fila (carga de D1/D2/D3 + carga de los .joblib de "
    "las dos etapas + calibración OOF sobre D3 = 'tiempo_entrenamiento_s' + "
    "cascada sobre D2 = 'tiempo_inferencia_s' + tabla de sensibilidad de los 3 "
    "umbrales); lo que queda al restar esas dos columnas son la carga de los "
    "splits los dos .joblib y las pasadas de métricas de la tabla de sensibilidad "
    "— ninguna columna los mide por separado. NO incluye lo que se hace DESPUÉS "
    "de tomar la medida: la figura 5x6 · la tabla 0-day de los cuatro detectores "
    "· la escritura de los CSV — de ahí que el log del script imprima una cifra "
    "mayor que esta; no es tiempo de ajuste —el híbrido no re-entrena— ni "
    "comparable con el 'tiempo_s' de las otras tres tablas"
    + _AVISO_TIEMPO_VARIANZA + _AVISO_LATENCIA_SOLO_PREDICT
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
#
# 'n_iter_ganador' y 'n_iter_total_grid' (metricas_anomalias.csv) tampoco son
# métricas sobre D2 y sin alcance propio se leerían como tales: son ÉPOCAS.
#
# POR QUÉ SON DOS COLUMNAS Y NO UNA (corrección de la versión anterior, que era la
# cuarta objeción del dictamen NO APTO de 0595a15): 'n_iter_ganador' son las
# épocas de UNA configuración —la ganadora— mientras que 'tiempo_entrenamiento_s'
# suma los fit de TODAS las del grid. Dividir la una por la otra no da segundos
# por época: da un número sin significado. El texto anterior invitaba justo a esa
# división. Se publica por eso 'n_iter_total_grid' —la suma de las épocas de todas
# las configuraciones del grid, exactamente el mismo conjunto de fit que
# 'tiempo_entrenamiento_s' cronometra—, que es el denominador COHERENTE con el que
# esa división tiene sentido (media ponderada entre las dos arquitecturas del
# grid, no una constante del modelo: ver ALCANCE_N_ITER_TOTAL).
# 'n_iter_ganador' se conserva porque responde a otra
# pregunta: si el ajuste del modelo que se publica se cortó por max_iter o por
# convergencia.
ALCANCE_N_ITER = (
    "épocas consumidas por el ajuste del modelo GANADOR sobre D1_train "
    "(Autoencoder = MLPRegressor con early_stopping=True y max_iter=300) — NO es "
    "una métrica sobre D2 y NO es el denominador de 'tiempo_entrenamiento_s': "
    "esta columna cuenta UNA configuración y ese tiempo suma los fit de TODAS las "
    "del grid (para eso está 'n_iter_total_grid'). Sirve para saber si el ajuste "
    "que se publica se cortó por el tope —un valor igual a max_iter=300— o por "
    "convergencia. Celda VACÍA en IsolationForest OneClassSVM y "
    "LocalOutlierFactor: no ajustan por iteraciones comparables y un 0 se leería "
    "como medida"
)

ALCANCE_N_ITER_TOTAL = (
    "suma de las épocas de TODAS las configuraciones del grid sobre D1_train "
    "(Autoencoder = MLPRegressor con early_stopping=True y max_iter=300) — NO es "
    "una métrica sobre D2. Cubre exactamente el mismo conjunto de fit que "
    "cronometra 'tiempo_entrenamiento_s' así que es el denominador COHERENTE "
    "para leer ese tiempo en segundos por época DENTRO de una corrida. NO decide "
    "si una diferencia de tiempo entre dos filas es de épocas o de carga de "
    "máquina: el recuento de épocas es DETERMINISTA con la semilla 42 —los mismos "
    "162 (54) y 128 (122) en las dos corridas que registran la columna— así que "
    "con el denominador constante el cociente es el numerador reescalado y "
    "absorbe la carga de máquina entera sin separar las dos causas. Coherente y "
    "no 'el único válido': el grid del autoencoder tiene DOS arquitecturas "
    "(64 32 64) y (32 16 32) cuyo coste por época no es el mismo así que ese "
    "cociente es una MEDIA PONDERADA entre dos costes por época distintos — "
    "interpretable pero no una constante del modelo. Celda VACÍA en "
    "IsolationForest OneClassSVM y LocalOutlierFactor por el mismo motivo que "
    "'n_iter_ganador'"
)

ALCANCE_COLUMNAS = {
    "umbral": ALCANCE_SELECCION,
    "n_iter_ganador": ALCANCE_N_ITER,
    "n_iter_total_grid": ALCANCE_N_ITER_TOTAL,
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
