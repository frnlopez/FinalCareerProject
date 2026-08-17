---
titulo: "Apéndice A.3 — Ficha del sistema (model card)"
numero: "A.3"
estado: borrador
---

# A.3 Ficha del sistema

Este apéndice documenta el sistema evaluado siguiendo la plantilla de **model card** propuesta por
[60]: detalles del modelo, uso previsto, particiones de datos, configuraciones
seleccionadas, alcance exacto de cada métrica, infraestructura de cómputo, análisis cuantitativo con
dispersión y limitaciones declaradas.

> [!note] Naturaleza de este apéndice
> Es un **volcado**, no una discusión. Todas las cifras se transcriben de los artefactos de
> `Resultados/` que se citan celda a celda; la interpretación corresponde al
> [[5.4 Conclusiones del capítulo|capítulo 5]] y a [[6.1 Conclusiones]]. Ninguna cifra de este
> apéndice se calcula aquí.

---

## A.3.1 Detalles del modelo

| Campo | Valor |
|---|---|
| Nombre | H-NIDS híbrido en cascada anomalías → firmas |
| Tipo | Sistema de dos etapas: detector *one-class* (etapa 1) + clasificador multiclase supervisado (etapa 2) |
| Etapa 1 publicada | **Autoencoder-MLP** (`sklearn.neural_network.MLPRegressor`), umbral por percentil 95 sobre `D1_val` |
| Etapa 2 publicada | **RandomForest** multiclase de 4 categorías de ataque, con umbral de confianza y clase de rechazo `unknown` |
| Variantes evaluadas | `54` (con selección de características) y `122_sin_seleccion` (sin selección) |
| Dataset | NSL-KDD (`KDDTrain+.txt` / `KDDTest+.txt`) |
| Semilla | `RANDOM_STATE = 42`, centralizada en `Implementacion/app/config.py` |
| Artefactos de origen (cuatro tablas principales) | `Resultados/metricas_anomalias.csv` · `metricas_firmas.csv` · `metricas_hibrido.csv` · `metricas_baseline.csv` |
| Artefacto de origen (medición aparte) | `Resultados/metricas_cascada_invertida.csv` |
| Sello de las **cuatro tablas principales** | `commit = 1163c90`, fecha `2026-08-09` (columnas `commit` y `fecha` de esos cuatro CSV) |
| Sello de la **cascada invertida** | `commit = 274923d-sucio`, fecha `2026-08-10` (columnas `commit` y `fecha` de `metricas_cascada_invertida.csv`) |

> [!warning] Son dos corridas distintas y no se presentan mezcladas
> Las cuatro tablas principales y la medición contrafactual de la cascada invertida (T3) **no salen
> de la misma corrida**: llevan commit y fecha distintos, como se comprueba en las columnas `commit`
> y `fecha` de los propios CSV. El criterio, fijado en `Implementacion/PIPELINE.md`, es que **ninguna
> cifra de una corrida se presente junto a las de la otra sin decirlo**. Por eso el sello va separado
> aquí y en A.3.9, y por eso la salvedad (iii) de A.3.6 reparte las celdas del titular por commit de
> origen.

**Uso previsto.** Trabajo académico de evaluación comparativa sobre un dataset público de referencia.
**No** es un sistema desplegable: opera sobre flujos ya extraídos y preprocesados, no sobre paquetes
en red, y no se ha evaluado frente a un adversario adaptativo (marco conceptual en
[[2.3.3 Límites y consideraciones éticas|2.3.3]] § *El modelo de amenaza como requisito metodológico
(P10)*, **especificación del adversario asumido en [[3.1 Requisitos del sistema]] § *3.1.5 Modelo de
amenaza***, lectura de sus consecuencias en el límite 3 de [[6.1 Conclusiones]], y sección A.3.7 de
esta ficha).

---

## A.3.2 Particiones de datos

Las tres particiones las genera `Implementacion/app/program.py` y son **idénticas en las dos
variantes**; su descripción funcional está en [[4.3 Preprocesamiento de los datasets]].

| Partición | Contenido | Tamaño | Función |
|---|---|---:|---|
| **D1** | Solo tráfico normal (de `KDDTrain+`) | 67.343 | Entrenamiento de la etapa 1 (*one-class*) |
| ├─ `D1_train` | 80 % de D1 | 53.874 * | Ajuste de los cuatro detectores |
| └─ `D1_val` | 20 % de D1 | 13.469 | Cálculo del umbral (percentil 95 del *score*) |
| **D2** | `KDDTest+` completo | 22.544 | Evaluación de extremo a extremo |
| ├─ normales | Clase `normal` de D2 | 9.711 | Denominador del FPR y de la cascada invertida (T3) |
| ├─ ataques de tipo conocido | Presentes también en train | 9.083 | Denominador de las métricas de la etapa 2 |
| └─ ataques 0-day | **17 tipos** ausentes del train | 3.750 | Denominador de `recall_0day_global` |
| **D3** | Solo ataques conocidos (de `KDDTrain+`) | 58.630 | Entrenamiento de la etapa 2 y calibración OOF del umbral de confianza |

**\* `D1_train` = 53.874 es una cifra derivada, no medida.** Ningún artefacto de `Resultados/` la
publica: sale de la **diferencia** entre el tamaño de D1 (67.343) y el de `D1_val` (13.469, este sí
publicado, en `Implementacion/PIPELINE.md`). Se incluye por completitud de la tabla y se marca como
derivada para que no se cite como salida de una corrida.

Muestreos internos con semilla, empleados durante el ajuste: **5.000 filas de D3** como conjunto
etiquetado de validación de la etapa 1 y **20.000 filas de `D1_train`** como submuestra de
OneClassSVM (`anomalias.py:163` para la muestra de D3; la submuestra de OneClassSVM se declara en
`anomalias.py:94-97` y se aplica en `anomalias.py:249-250`).

> [!warning] Qué es intocable en D2 — y qué sí lo miró
> La regla que enuncia el código (`anomalias.py:18-22`) es **acotada**: D2 es intocable **para
> ajustar hiperparámetros o el umbral**. No es —y este apéndice no lo afirma— que D2 quede fuera de
> *toda* decisión.
>
> **Lo que no mira D2 (ajuste de parámetros):**
>
> | Decisión | Dónde se ajusta | Referencia |
> |---|---|---|
> | Umbral de la etapa 1 | Percentil 95 del *score* sobre `D1_val` | `anomalias.py` |
> | Configuración **dentro** de cada algoritmo de la etapa 1 | AUC-ROC sobre `D1_val` + muestra etiquetada de 5.000 filas de D3 | `anomalias.py:281` |
> | Rejilla de hiperparámetros y eje de balanceo de la etapa 2 | `GridSearchCV` con `f1_macro` por validación cruzada **sobre D3** | `firmas.py` |
> | `UMBRAL_CONF` del híbrido | Calibración *out-of-fold* sobre D3; el método **no recibe D2 en su firma** (decisión P-4) | `hibrido.py::_calibrar_umbral_conf` |
>
> **Lo que sí miró D2: tres decisiones.** El **detector de la etapa 1** (H-2), el **clasificador de
> la etapa 2** (H-3) y **el set de características, 54 frente a 122** (Q1/C, experimento H1, decidido
> por recall 0-day por tipo y `f1_macro` medidos sobre D2). Las tres son selección de modelo sobre el
> conjunto de test, es decir *data snooping*, y por tanto las métricas publicadas son optimistas
> respecto a lo que daría un test verdaderamente ciego. La declaración de referencia de esta
> limitación es [[6.1 Conclusiones]]; el inventario tabulado de las tres decisiones, con criterio y
> registro de cada una, está en A.3.7 de esta misma ficha. No se presenta como protocolo limpio.

---

## A.3.3 Configuraciones seleccionadas (semilla 42)

### Etapa 1 — detectores de anomalías

Fuente: `Resultados/metricas_anomalias.csv`, columnas `config_ganadora` y `umbral`.

| Variante | Algoritmo | Configuración ganadora | Umbral (p95 sobre `D1_val`) |
|---|---|---|---:|
| 54 | IsolationForest | `{'n_estimators': 100, 'max_samples': 1.0}` | 0,440643 |
| 54 | OneClassSVM | `{'nu': 0.1, 'gamma': 'scale'}` | 19,186592 |
| 54 | LocalOutlierFactor | `{'n_neighbors': 20}` | 2,186273 |
| 54 | **Autoencoder** (publicado) | `{'hidden_layer_sizes': (64, 32, 64)}` | 0,000033 |
| 122_sin_seleccion | IsolationForest | `{'n_estimators': 100, 'max_samples': 0.5}` | 0,409761 |
| 122_sin_seleccion | OneClassSVM | `{'nu': 0.05, 'gamma': 'scale'}` | −0,506286 |
| 122_sin_seleccion | LocalOutlierFactor | `{'n_neighbors': 20}` | 2,315471 |
| 122_sin_seleccion | **Autoencoder** (publicado) | `{'hidden_layer_sizes': (64, 32, 64)}` | 0,000124 |

Los umbrales **no son comparables entre algoritmos**: cada uno se aplica sobre su propia escala de
*score*. El Autoencoder registra además el número de iteraciones del ajuste ganador: **117 de 162**
en la variante de 54 y **66 de 128** en la de 122 (`n_iter_ganador` / `n_iter_total_grid`).

### Etapa 2 — clasificador de firmas

Fuente: `Resultados/metricas_firmas.csv`, columnas `balanceo` y `config_ganadora`. El eje de balanceo
se decide **por algoritmo** (mini-experimento de 4.3.4, `firmas.py:100-108`).

| Variante | Algoritmo | Balanceo ganador | Configuración ganadora |
|---|---|---|---|
| 54 | DecisionTree | `class_weight` | `{'max_depth': 10, 'min_samples_leaf': 1}` |
| 54 | **RandomForest** (publicado) | `SMOTE` | `{'clf__max_depth': 10, 'clf__n_estimators': 300}` |
| 54 | KNN | `SMOTE` | `{'clf__n_neighbors': 5, 'clf__weights': 'uniform'}` |
| 54 | HistGradientBoosting | `SMOTE` | `{'clf__learning_rate': 0.1, 'clf__max_iter': 300}` |
| 122_sin_seleccion | DecisionTree | `class_weight` | `{'max_depth': 10, 'min_samples_leaf': 1}` |
| 122_sin_seleccion | **RandomForest** (publicado) | `SMOTE` | `{'clf__max_depth': None, 'clf__n_estimators': 100}` |
| 122_sin_seleccion | KNN | `SMOTE` | `{'clf__n_neighbors': 5, 'clf__weights': 'uniform'}` |
| 122_sin_seleccion | HistGradientBoosting | `SMOTE` | `{'clf__learning_rate': 0.05, 'clf__max_iter': 300}` |

### Sistema híbrido y baseline

| Elemento | 54 | 122_sin_seleccion | Fuente |
|---|---:|---:|---|
| Cascada publicada | Autoencoder → RandomForest | Autoencoder → RandomForest | `metricas_hibrido.csv` |
| `umbral_conf_elegido` (calibrado OOF sobre D3) | 0,5 | 0,5 | `metricas_hibrido.csv` |
| `tau` | 0,02 | 0,02 | `metricas_hibrido.csv` |
| Baseline monolítico | `{'max_depth': None, 'n_estimators': 300}` | `{'max_depth': None, 'n_estimators': 300}` | `metricas_baseline.csv` |

---

## A.3.4 Alcance de cada métrica

Cada tabla de `Resultados/` lleva una columna `alcance` que fija sobre qué población se calcula la
fila. **Las cifras de tablas distintas no son intercambiables** aunque compartan nombre de métrica.

| Artefacto | Alcance declarado | Denominador |
|---|---|---:|
| `metricas_anomalias.csv` | binario normal-vs-ataque (2 clases) sobre D2 completo | 22.544 |
| `metricas_firmas.csv` | multiclase 4 categorías de ataque sobre los ataques de D2 de tipo conocido | 9.083 |
| `metricas_baseline.csv` | multiclase 5 clases (normal + 4 ataques) sobre D2 completo | 22.544 |
| `metricas_hibrido.csv` | cascada extremo a extremo (5 clases + `unknown`) sobre D2 completo | 22.544 (0-day: 3.750) |
| `metricas_cascada_invertida.csv` | medida **contrafactual** de la cascada invertida (T3): `predict_proba` del clasificador de firmas sobre las filas normales de D2 | 9.711 |

Precisiones que condicionan la lectura y que están documentadas en las propias columnas `alcance`:

- **`bin_fpr` del híbrido = `fpr` del Autoencoder**, por construcción y no por casualidad: en una
  cascada anomalías → firmas, la etapa 2 no puede crear ni corregir falsos positivos binarios. El
  desarrollo está en [[A.2 Métricas de desempeño]].
- **La fila `__global__` de la cascada invertida es una cota inferior**, no el FPR de un sistema de
  firmas-primero: en el sistema publicado `unknown` es alarma (decisión P-5), así que lo que cae bajo
  umbral no queda exonerado. Valores medidos: de las 9.711 filas normales de D2, el clasificador de
  firmas condenaría **6.558 (67,53 %)** en la variante de 54 y **3.329 (34,28 %)** en la de 122.
- **Las columnas de tiempo** (`tiempo_s`, `latencia_ms_por_flujo`, `flujos_por_segundo`) son
  *wall-clock* de un pase único en máquina no dedicada, miden solo el `predict`/`score` sobre
  características ya en memoria y **no** son capacidad operativa del sistema.

> [!note] Dónde vive el protocolo
> El protocolo de evaluación consolidado —particiones y función de cada una, prohibiciones y
> vocabulario de reproducibilidad— está en [[5.0 Protocolo de evaluación]], que **enuncia las
> reglas**. Este apéndice documenta **la instancia concreta** que las cumple: tamaños exactos,
> configuraciones ganadoras, alcance de cada artefacto y entorno de cómputo. Lo que aquí se repite
> del protocolo es solo lo imprescindible para leer las tablas sin salir del apéndice.

---

## A.3.5 Infraestructura de cómputo y entorno

| Elemento | Valor |
|---|---|
| CPU | Intel Core i7-12700H |
| Memoria | 34 GB RAM |
| Sistema operativo | Windows 11 Pro 10.0.26200 |
| Aceleración | Ninguna (no se emplea GPU) |
| Intérprete | Python 3.11 (entorno virtual `Implementacion/Imp`) |
| Dependencias | **21 paquetes con versión fijada** en `Implementacion/requirements.txt` |
| Versión de referencia | `scikit-learn==1.7.1` |

Otras versiones fijadas relevantes para la reproducción: `numpy==2.3.2`, `pandas==2.3.1`,
`scipy==1.16.0`, `imbalanced-learn==0.14.2`, `joblib==1.5.1`, `matplotlib==3.10.3`, `seaborn==0.13.2`.

> [!warning] El *wall-clock* no es reproducible
> Todas las corridas se hicieron en una máquina **no dedicada**. Las diferencias de tiempo entre
> corridas alcanzan factores de varias unidades sin que cambie la calidad: el bloque de «dispersión de
> máquina» de A.3.6 lo documenta y **no se cita como resultado**.

---

## A.3.6 Análisis cuantitativo: dispersión entre semillas

Volcado del artefacto `Resultados/dispersion_semillas.md`, generado por
`Implementacion/app/agregar_semillas.py` a partir de `Resultados/dispersion_semillas.csv`, que es la
fuente. La tabla **no se edita a mano**: se regenera corriendo el agregador.

Alcance exacto de este volcado, para que se sepa qué se transcribe y qué no:

| Bloque del artefacto | Cómo aparece aquí |
|---|---|
| Tablas de dispersión (198 filas: calidad + máquina) | **Íntegras**, fila a fila |
| Bloque «Avisos de la agregación» (19 líneas de aviso) | **Resumido** en una tabla de 6 filas, con los casos de mayor amplitud |

El resumen del bloque de avisos es una selección editorial de este apéndice, no del artefacto: para
el reparto completo semilla a semilla hay que ir al propio `dispersion_semillas.md` o a la columna
`decisiones_no_constantes` del CSV.

### Alcance y método del barrido

- **Semillas agregadas (10):** 1, 2, 3, 4, 5, 6, 7, 8, 9, 10.
- **Qué mide.** Dispersión **de los modelos sobre splits D1/D2/D3 y set de características FIJOS**.
  **No** es «dispersión del sistema»: `program.py` **no está parametrizado por semilla** —su
  `random_state=42` es literal y no importa `config.py`—, de modo que el barrido **no incluye
  variabilidad del preprocesado ni de la selección de características**.
- **Qué sí varía** entre corridas: el split 80/20 de D1 (y con él el umbral p95), la muestra de 5.000
  de D3, la submuestra de 20.000 de OneClassSVM, los *folds* de la validación cruzada y la
  inicialización de los modelos.
- **`sd` es la desviación típica muestral** (`ddof=1`).
- **Sin p-valor**, y la renuncia se declara con su razón: **10 puntos sobre un único dataset no
  sostienen un contraste**. Declarar la renuncia cumple el ítem *statistics* del checklist de
  [20]; callarla no.
- **La semilla 42 no entra en ninguna banda**, y es deliberado: es el **titular** de
  [[5.1 Resultados del modelo de detección de anomalías|5.1]]-[[5.3 Resultados del sistema híbrido|5.3]]
  y un punto **independiente**, no uno de los sumandos de su propia media. Aparece **al lado** de la
  banda para poder contar cuántas veces cae fuera sin hacerlo a mano.
- **Por qué se conservan `tabla_origen` y `alcance`.** Sin ellas la etiqueta es ambigua:
  «`54 · RandomForest`» nombra por igual al **clasificador de firmas** y a la **medición
  contrafactual de la cascada invertida**, que son dos medidas distintas. El texto de `alcance` va
  recortado a 70 caracteres para que la tabla quepa; el íntegro está en la columna homónima del CSV.
- **Columnas que solo trae el CSV** y que hay que mirar antes de citar una banda: `commits_origen`,
  `commit_agregador`, `decisiones_no_constantes`, `distancia_fuera_banda_42` y `commit_semilla_42`.

### El titular (semilla 42) frente a la banda

**13 de 98** celdas de calidad tienen el valor de la semilla 42 **fuera** del intervalo [mín, máx] de
las diez semillas del barrido. La cifra la calcula el agregador: no se cuenta a mano. Solo entra el
bloque de **calidad**; en el de máquina la banda mide carga de máquina y no el algoritmo.

El recuento se cita **con sus tres salvedades**, y las tres son parte de la cifra:

> [!warning] Salvedad (i) — el 13 depende del criterio de comparación
> El valor de la 42 se compara con los extremos **con la precisión con la que se persistió el CSV de
> origen** (6 decimales), no con el mín/máx a 4 decimales de las tablas de abajo, y un valor **igual**
> a un extremo cuenta como **dentro** (criterio simétrico en ambos extremos). Con los extremos
> redondeados a 4 decimales el recuento sería **14**, porque `f1_u2r` de RandomForest en
> `122_sin_seleccion` tiene la 42 en **0,318182**, exactamente en el mínimo.
>
> **Ese 14 no lo emite ninguna corrida.** No está en `dispersion_semillas.md` ni en
> `dispersion_semillas.csv`: es una **cuenta a mano declarada en el encabezado del agregador**
> (`Implementacion/app/agregar_semillas.py`, bloque de documentación del criterio dentro/fuera). El
> razonamiento es verificable —el mínimo redondeado de esa celda queda por encima del valor real de
> la 42—, pero la cifra es prosa, no salida de un script, y así se cita. El **13** sí lo calcula el
> agregador, que es la razón por la que se automatizó.

> [!warning] Salvedad (ii) — no todas esas celdas son métricas sobre D2
> De las 98 del denominador, **10 son umbrales** (8 de `umbral` · 2 de `umbral_conf_elegido`): no
> miden rendimiento sobre D2 sino una decisión del pipeline que se recalcula en cada semilla (el p95
> sobre el 20 % de D1 y el `UMBRAL_CONF` calibrado por OOF). **No se descuentan**, porque son justo lo
> que el barrido pone a prueba; si se descontasen, el denominador sería **88** y la cifra habría que
> recontarla. Y el descuento no sería inocuo: **3 celdas caen en el borde exacto** de su banda
> (`122_sin_seleccion` KNN `f1_u2r` (= máx) · `122_sin_seleccion` RandomForest `f1_u2r` (= mín) ·
> `122_sin_seleccion` Autoencoder→RandomForest `umbral_conf_elegido` (= máx)), cuentan como **dentro**
> por el criterio de la salvedad (i) y por eso deciden el recuento — y **una de las tres es un umbral**.

> [!warning] Salvedad (iii) — el titular y la banda no salen del mismo commit
> Los valores de la semilla 42 vienen de `1163c90` y `274923d-sucio` (columna `commit_semilla_42` del
> CSV, celda a celda) y los diez puntos de cada banda, de `df30cb2` (columna `commits_origen`). Parte
> de la distancia listada abajo **podría ser deriva de código** entre esas versiones y no dispersión
> por semilla. Reparto de las 98 celdas casadas por commit de origen del titular: `1163c90` aporta
> **94** (13 fuera de banda) · `274923d-sucio` aporta **4** (ninguna fuera de banda). Es una
> **salvedad de procedencia, no una invalidación**: cada cifra es el resultado real de su corrida.

#### Celdas fuera de banda, por distancia

| Tabla de origen | Variante | Algoritmo | Alcance | Métrica | Semilla 42 | Mín (10) | Máx (10) | Distancia |
|---|---|---|---|---|---:|---:|---:|---:|
| `metricas_firmas_semillas.csv` | 122_sin_seleccion | RandomForest | multiclase 4 categorías de ataque sobre los ataques de D2 de tipo cono… | `f1_macro` | 0.6956 | 0.7155 | 0.8435 | 0.019937 |
| `metricas_firmas_semillas.csv` | 54 | RandomForest | multiclase 4 categorías de ataque sobre los ataques de D2 de tipo cono… | `recall_macro` | 0.8496 | 0.7839 | 0.8370 | 0.012574 |
| `metricas_anomalias_semillas.csv` | 54 | Autoencoder | binario normal-vs-ataque (2 clases) sobre D2 completo | `pr_auc` | 0.9092 | 0.9208 | 0.9464 | 0.011533 |
| `metricas_hibrido_semillas.csv` | 122_sin_seleccion | Autoencoder->RandomForest | cascada extremo a extremo (5 clases + unknown) sobre D2 completo; ojo:… | `recall_0day_global` | 0.7853 | 0.6669 | 0.7800 | 0.005333 |
| `metricas_firmas_semillas.csv` | 54 | HistGradientBoosting | multiclase 4 categorías de ataque sobre los ataques de D2 de tipo cono… | `accuracy_D2` | 0.9577 | 0.9180 | 0.9538 | 0.003963 |
| `metricas_anomalias_semillas.csv` | 122_sin_seleccion | IsolationForest | binario normal-vs-ataque (2 clases) sobre D2 completo | `pr_auc` | 0.9511 | 0.9546 | 0.9609 | 0.003474 |
| `metricas_anomalias_semillas.csv` | 122_sin_seleccion | LocalOutlierFactor | binario normal-vs-ataque (2 clases) sobre D2 completo | `fpr` | 0.1659 | 0.1569 | 0.1635 | 0.002368 |
| `metricas_firmas_semillas.csv` | 122_sin_seleccion | RandomForest | multiclase 4 categorías de ataque sobre los ataques de D2 de tipo cono… | `recall_macro` | 0.7458 | 0.7480 | 0.8852 | 0.002158 |
| `metricas_firmas_semillas.csv` | 54 | RandomForest | multiclase 4 categorías de ataque sobre los ataques de D2 de tipo cono… | `f1_macro` | 0.8223 | 0.7779 | 0.8205 | 0.001792 |
| `metricas_anomalias_semillas.csv` | 54 | IsolationForest | binario normal-vs-ataque (2 clases) sobre D2 completo | `pr_auc` | 0.9181 | 0.9197 | 0.9421 | 0.001630 |
| `metricas_anomalias_semillas.csv` | 122_sin_seleccion | IsolationForest | binario normal-vs-ataque (2 clases) sobre D2 completo | `roc_auc` | 0.9459 | 0.9473 | 0.9539 | 0.001405 |
| `metricas_anomalias_semillas.csv` | 122_sin_seleccion | OneClassSVM | binario normal-vs-ataque (2 clases) sobre D2 completo | `fpr` | 0.0834 | 0.0819 | 0.0830 | 0.000412 |
| `metricas_anomalias_semillas.csv` | 54 | OneClassSVM | binario normal-vs-ataque (2 clases) sobre D2 completo | `roc_auc` | 0.8360 | 0.8200 | 0.8359 | 0.000097 |

#### Bloque de calidad (98 celdas)

| Tabla de origen | Variante | Algoritmo | Alcance | Métrica | n | Media | sd | Mín | Máx | Semilla 42 | ¿En banda? |
|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---|
| `metricas_anomalias_semillas.csv` | 122_sin_seleccion | Autoencoder | binario normal-vs-ataque (2 clases) sobre D2 completo | `f1` | 10 | 0.8687 | 0.0232 | 0.8351 | 0.8965 | 0.8659 | dentro |
| `metricas_anomalias_semillas.csv` | 122_sin_seleccion | Autoencoder | binario normal-vs-ataque (2 clases) sobre D2 completo | `fpr` | 10 | 0.0861 | 0.0138 | 0.0488 | 0.0978 | 0.0849 | dentro |
| `metricas_anomalias_semillas.csv` | 122_sin_seleccion | Autoencoder | binario normal-vs-ataque (2 clases) sobre D2 completo | `pr_auc` | 10 | 0.9542 | 0.0067 | 0.9407 | 0.9602 | 0.9519 | dentro |
| `metricas_anomalias_semillas.csv` | 122_sin_seleccion | Autoencoder | binario normal-vs-ataque (2 clases) sobre D2 completo | `roc_auc` | 10 | 0.9480 | 0.0069 | 0.9341 | 0.9573 | 0.9472 | dentro |
| `metricas_anomalias_semillas.csv` | 122_sin_seleccion | Autoencoder | binario normal-vs-ataque (2 clases) sobre D2 completo | `umbral` | 10 | 0.0014 | 0.0016 | 0.0001 | 0.0043 | 0.0001 | dentro |
| `metricas_anomalias_semillas.csv` | 122_sin_seleccion | IsolationForest | binario normal-vs-ataque (2 clases) sobre D2 completo | `f1` | 10 | 0.8194 | 0.0087 | 0.8063 | 0.8322 | 0.8187 | dentro |
| `metricas_anomalias_semillas.csv` | 122_sin_seleccion | IsolationForest | binario normal-vs-ataque (2 clases) sobre D2 completo | `fpr` | 10 | 0.0898 | 0.0034 | 0.0823 | 0.0938 | 0.0928 | dentro |
| `metricas_anomalias_semillas.csv` | 122_sin_seleccion | IsolationForest | binario normal-vs-ataque (2 clases) sobre D2 completo | `pr_auc` | 10 | 0.9570 | 0.0019 | 0.9546 | 0.9609 | 0.9511 | **FUERA** |
| `metricas_anomalias_semillas.csv` | 122_sin_seleccion | IsolationForest | binario normal-vs-ataque (2 clases) sobre D2 completo | `roc_auc` | 10 | 0.9502 | 0.0022 | 0.9473 | 0.9539 | 0.9459 | **FUERA** |
| `metricas_anomalias_semillas.csv` | 122_sin_seleccion | IsolationForest | binario normal-vs-ataque (2 clases) sobre D2 completo | `umbral` | 10 | 0.4060 | 0.0042 | 0.4003 | 0.4126 | 0.4098 | dentro |
| `metricas_anomalias_semillas.csv` | 122_sin_seleccion | LocalOutlierFactor | binario normal-vs-ataque (2 clases) sobre D2 completo | `f1` | 10 | 0.7148 | 0.0253 | 0.6511 | 0.7342 | 0.7272 | dentro |
| `metricas_anomalias_semillas.csv` | 122_sin_seleccion | LocalOutlierFactor | binario normal-vs-ataque (2 clases) sobre D2 completo | `fpr` | 10 | 0.1607 | 0.0021 | 0.1569 | 0.1635 | 0.1659 | **FUERA** |
| `metricas_anomalias_semillas.csv` | 122_sin_seleccion | LocalOutlierFactor | binario normal-vs-ataque (2 clases) sobre D2 completo | `pr_auc` | 10 | 0.7559 | 0.0036 | 0.7484 | 0.7599 | 0.7546 | dentro |
| `metricas_anomalias_semillas.csv` | 122_sin_seleccion | LocalOutlierFactor | binario normal-vs-ataque (2 clases) sobre D2 completo | `roc_auc` | 10 | 0.8315 | 0.0042 | 0.8218 | 0.8364 | 0.8340 | dentro |
| `metricas_anomalias_semillas.csv` | 122_sin_seleccion | LocalOutlierFactor | binario normal-vs-ataque (2 clases) sobre D2 completo | `umbral` | 10 | 2.4144 | 0.0588 | 2.2966 | 2.5244 | 2.3155 | dentro |
| `metricas_anomalias_semillas.csv` | 122_sin_seleccion | OneClassSVM | binario normal-vs-ataque (2 clases) sobre D2 completo | `f1` | 10 | 0.8014 | 0.0010 | 0.7997 | 0.8033 | 0.8017 | dentro |
| `metricas_anomalias_semillas.csv` | 122_sin_seleccion | OneClassSVM | binario normal-vs-ataque (2 clases) sobre D2 completo | `fpr` | 10 | 0.0825 | 0.0004 | 0.0819 | 0.0830 | 0.0834 | **FUERA** |
| `metricas_anomalias_semillas.csv` | 122_sin_seleccion | OneClassSVM | binario normal-vs-ataque (2 clases) sobre D2 completo | `pr_auc` | 10 | 0.9254 | 0.0008 | 0.9238 | 0.9270 | 0.9258 | dentro |
| `metricas_anomalias_semillas.csv` | 122_sin_seleccion | OneClassSVM | binario normal-vs-ataque (2 clases) sobre D2 completo | `roc_auc` | 10 | 0.8883 | 0.0019 | 0.8855 | 0.8915 | 0.8898 | dentro |
| `metricas_anomalias_semillas.csv` | 122_sin_seleccion | OneClassSVM | binario normal-vs-ataque (2 clases) sobre D2 completo | `umbral` | 10 | 0.0837 | 0.3817 | -0.5839 | 0.5857 | -0.5063 | dentro |
| `metricas_anomalias_semillas.csv` | 54 | Autoencoder | binario normal-vs-ataque (2 clases) sobre D2 completo | `f1` | 10 | 0.8721 | 0.0161 | 0.8492 | 0.8934 | 0.8716 | dentro |
| `metricas_anomalias_semillas.csv` | 54 | Autoencoder | binario normal-vs-ataque (2 clases) sobre D2 completo | `fpr` | 10 | 0.0986 | 0.0050 | 0.0934 | 0.1070 | 0.1017 | dentro |
| `metricas_anomalias_semillas.csv` | 54 | Autoencoder | binario normal-vs-ataque (2 clases) sobre D2 completo | `pr_auc` | 10 | 0.9287 | 0.0077 | 0.9208 | 0.9464 | 0.9092 | **FUERA** |
| `metricas_anomalias_semillas.csv` | 54 | Autoencoder | binario normal-vs-ataque (2 clases) sobre D2 completo | `roc_auc` | 10 | 0.9343 | 0.0077 | 0.9242 | 0.9489 | 0.9288 | dentro |
| `metricas_anomalias_semillas.csv` | 54 | Autoencoder | binario normal-vs-ataque (2 clases) sobre D2 completo | `umbral` | 10 | 0.0001 | 0.0001 | 0.0000 | 0.0003 | 0.0000 | dentro |
| `metricas_anomalias_semillas.csv` | 54 | IsolationForest | binario normal-vs-ataque (2 clases) sobre D2 completo | `f1` | 10 | 0.8259 | 0.0120 | 0.8062 | 0.8428 | 0.8341 | dentro |
| `metricas_anomalias_semillas.csv` | 54 | IsolationForest | binario normal-vs-ataque (2 clases) sobre D2 completo | `fpr` | 10 | 0.0995 | 0.0019 | 0.0969 | 0.1024 | 0.1002 | dentro |
| `metricas_anomalias_semillas.csv` | 54 | IsolationForest | binario normal-vs-ataque (2 clases) sobre D2 completo | `pr_auc` | 10 | 0.9347 | 0.0079 | 0.9197 | 0.9421 | 0.9181 | **FUERA** |
| `metricas_anomalias_semillas.csv` | 54 | IsolationForest | binario normal-vs-ataque (2 clases) sobre D2 completo | `roc_auc` | 10 | 0.9294 | 0.0041 | 0.9225 | 0.9336 | 0.9229 | dentro |
| `metricas_anomalias_semillas.csv` | 54 | IsolationForest | binario normal-vs-ataque (2 clases) sobre D2 completo | `umbral` | 10 | 0.4366 | 0.0033 | 0.4320 | 0.4436 | 0.4406 | dentro |
| `metricas_anomalias_semillas.csv` | 54 | LocalOutlierFactor | binario normal-vs-ataque (2 clases) sobre D2 completo | `f1` | 10 | 0.5838 | 0.0404 | 0.5196 | 0.6480 | 0.5718 | dentro |
| `metricas_anomalias_semillas.csv` | 54 | LocalOutlierFactor | binario normal-vs-ataque (2 clases) sobre D2 completo | `fpr` | 10 | 0.1598 | 0.0025 | 0.1559 | 0.1650 | 0.1604 | dentro |
| `metricas_anomalias_semillas.csv` | 54 | LocalOutlierFactor | binario normal-vs-ataque (2 clases) sobre D2 completo | `pr_auc` | 10 | 0.7416 | 0.0057 | 0.7335 | 0.7502 | 0.7401 | dentro |
| `metricas_anomalias_semillas.csv` | 54 | LocalOutlierFactor | binario normal-vs-ataque (2 clases) sobre D2 completo | `roc_auc` | 10 | 0.8105 | 0.0075 | 0.8000 | 0.8223 | 0.8071 | dentro |
| `metricas_anomalias_semillas.csv` | 54 | LocalOutlierFactor | binario normal-vs-ataque (2 clases) sobre D2 completo | `umbral` | 10 | 2.2577 | 0.0588 | 2.1594 | 2.3362 | 2.1863 | dentro |
| `metricas_anomalias_semillas.csv` | 54 | OneClassSVM | binario normal-vs-ataque (2 clases) sobre D2 completo | `f1` | 10 | 0.7834 | 0.0016 | 0.7801 | 0.7847 | 0.7844 | dentro |
| `metricas_anomalias_semillas.csv` | 54 | OneClassSVM | binario normal-vs-ataque (2 clases) sobre D2 completo | `fpr` | 10 | 0.0837 | 0.0010 | 0.0821 | 0.0850 | 0.0849 | dentro |
| `metricas_anomalias_semillas.csv` | 54 | OneClassSVM | binario normal-vs-ataque (2 clases) sobre D2 completo | `pr_auc` | 10 | 0.8866 | 0.0028 | 0.8807 | 0.8896 | 0.8890 | dentro |
| `metricas_anomalias_semillas.csv` | 54 | OneClassSVM | binario normal-vs-ataque (2 clases) sobre D2 completo | `roc_auc` | 10 | 0.8301 | 0.0051 | 0.8200 | 0.8359 | 0.8360 | **FUERA** |
| `metricas_anomalias_semillas.csv` | 54 | OneClassSVM | binario normal-vs-ataque (2 clases) sobre D2 completo | `umbral` | 10 | 14.2180 | 9.7495 | 0.1280 | 22.2675 | 19.1866 | dentro |
| `metricas_baseline_semillas.csv` | 122_sin_seleccion | RandomForest_monolitico | multiclase 5 clases (normal + 4 ataques) sobre D2 completo | `bin_accuracy` | 10 | 0.7476 | 0.0009 | 0.7460 | 0.7489 | 0.7477 | dentro |
| `metricas_baseline_semillas.csv` | 122_sin_seleccion | RandomForest_monolitico | multiclase 5 clases (normal + 4 ataques) sobre D2 completo | `bin_fpr` | 10 | 0.0261 | 0.0002 | 0.0260 | 0.0265 | 0.0261 | dentro |
| `metricas_baseline_semillas.csv` | 122_sin_seleccion | RandomForest_monolitico | multiclase 5 clases (normal + 4 ataques) sobre D2 completo | `f1_macro` | 10 | 0.4694 | 0.0016 | 0.4672 | 0.4720 | 0.4698 | dentro |
| `metricas_baseline_semillas.csv` | 122_sin_seleccion | RandomForest_monolitico | multiclase 5 clases (normal + 4 ataques) sobre D2 completo | `recall_0day_global` | 10 | 0.1471 | 0.0046 | 0.1376 | 0.1539 | 0.1480 | dentro |
| `metricas_baseline_semillas.csv` | 54 | RandomForest_monolitico | multiclase 5 clases (normal + 4 ataques) sobre D2 completo | `bin_accuracy` | 10 | 0.7451 | 0.0017 | 0.7429 | 0.7484 | 0.7466 | dentro |
| `metricas_baseline_semillas.csv` | 54 | RandomForest_monolitico | multiclase 5 clases (normal + 4 ataques) sobre D2 completo | `bin_fpr` | 10 | 0.0269 | 0.0002 | 0.0266 | 0.0271 | 0.0268 | dentro |
| `metricas_baseline_semillas.csv` | 54 | RandomForest_monolitico | multiclase 5 clases (normal + 4 ataques) sobre D2 completo | `f1_macro` | 10 | 0.4703 | 0.0017 | 0.4678 | 0.4734 | 0.4721 | dentro |
| `metricas_baseline_semillas.csv` | 54 | RandomForest_monolitico | multiclase 5 clases (normal + 4 ataques) sobre D2 completo | `recall_0day_global` | 10 | 0.1402 | 0.0107 | 0.1269 | 0.1597 | 0.1496 | dentro |
| `metricas_cascada_invertida_semillas.csv` | 122_sin_seleccion | RandomForest | medida CONTRAFACTUAL de la cascada invertida (T3): predict_proba del c… | `n_condenadas` | 10 | 6011.1000 | 2398.7285 | 2157.0000 | 9051.0000 | 3329.0000 | dentro |
| `metricas_cascada_invertida_semillas.csv` | 122_sin_seleccion | RandomForest | medida CONTRAFACTUAL de la cascada invertida (T3): predict_proba del c… | `tasa_condena` | 10 | 0.6190 | 0.2470 | 0.2221 | 0.9320 | 0.3428 | dentro |
| `metricas_cascada_invertida_semillas.csv` | 54 | RandomForest | medida CONTRAFACTUAL de la cascada invertida (T3): predict_proba del c… | `n_condenadas` | 10 | 7436.9000 | 1524.5470 | 5585.0000 | 9586.0000 | 6558.0000 | dentro |
| `metricas_cascada_invertida_semillas.csv` | 54 | RandomForest | medida CONTRAFACTUAL de la cascada invertida (T3): predict_proba del c… | `tasa_condena` | 10 | 0.7658 | 0.1570 | 0.5751 | 0.9871 | 0.6753 | dentro |
| `metricas_firmas_semillas.csv` | 122_sin_seleccion | DecisionTree | multiclase 4 categorías de ataque sobre los ataques de D2 de tipo cono… | `accuracy_D2` | 10 | 0.8740 | 0.0402 | 0.7924 | 0.9080 | 0.9029 | dentro |
| `metricas_firmas_semillas.csv` | 122_sin_seleccion | DecisionTree | multiclase 4 categorías de ataque sobre los ataques de D2 de tipo cono… | `f1_macro` | 10 | 0.6716 | 0.0786 | 0.5356 | 0.7462 | 0.7309 | dentro |
| `metricas_firmas_semillas.csv` | 122_sin_seleccion | DecisionTree | multiclase 4 categorías de ataque sobre los ataques de D2 de tipo cono… | `f1_u2r` | 10 | 0.2306 | 0.1599 | 0.0296 | 0.3810 | 0.3492 | dentro |
| `metricas_firmas_semillas.csv` | 122_sin_seleccion | DecisionTree | multiclase 4 categorías de ataque sobre los ataques de D2 de tipo cono… | `recall_macro` | 10 | 0.7251 | 0.0489 | 0.6480 | 0.7705 | 0.7536 | dentro |
| `metricas_firmas_semillas.csv` | 122_sin_seleccion | HistGradientBoosting | multiclase 4 categorías de ataque sobre los ataques de D2 de tipo cono… | `accuracy_D2` | 10 | 0.9333 | 0.0146 | 0.9150 | 0.9519 | 0.9296 | dentro |
| `metricas_firmas_semillas.csv` | 122_sin_seleccion | HistGradientBoosting | multiclase 4 categorías de ataque sobre los ataques de D2 de tipo cono… | `f1_macro` | 10 | 0.7489 | 0.0329 | 0.6896 | 0.7866 | 0.7131 | dentro |
| `metricas_firmas_semillas.csv` | 122_sin_seleccion | HistGradientBoosting | multiclase 4 categorías de ataque sobre los ataques de D2 de tipo cono… | `f1_u2r` | 10 | 0.3250 | 0.1006 | 0.1082 | 0.4200 | 0.1699 | dentro |
| `metricas_firmas_semillas.csv` | 122_sin_seleccion | HistGradientBoosting | multiclase 4 categorías de ataque sobre los ataques de D2 de tipo cono… | `recall_macro` | 10 | 0.8301 | 0.0141 | 0.8117 | 0.8540 | 0.8312 | dentro |
| `metricas_firmas_semillas.csv` | 122_sin_seleccion | KNN | multiclase 4 categorías de ataque sobre los ataques de D2 de tipo cono… | `accuracy_D2` | 10 | 0.9529 | 0.0044 | 0.9459 | 0.9583 | 0.9499 | dentro |
| `metricas_firmas_semillas.csv` | 122_sin_seleccion | KNN | multiclase 4 categorías de ataque sobre los ataques de D2 de tipo cono… | `f1_macro` | 10 | 0.7584 | 0.0067 | 0.7479 | 0.7658 | 0.7530 | dentro |
| `metricas_firmas_semillas.csv` | 122_sin_seleccion | KNN | multiclase 4 categorías de ataque sobre los ataques de D2 de tipo cono… | `f1_u2r` | 10 | 0.1934 | 0.0044 | 0.1824 | 0.1972 | 0.1972 | dentro |
| `metricas_firmas_semillas.csv` | 122_sin_seleccion | KNN | multiclase 4 categorías de ataque sobre los ataques de D2 de tipo cono… | `recall_macro` | 10 | 0.8947 | 0.0043 | 0.8880 | 0.9004 | 0.8919 | dentro |
| `metricas_firmas_semillas.csv` | 122_sin_seleccion | RandomForest | multiclase 4 categorías de ataque sobre los ataques de D2 de tipo cono… | `accuracy_D2` | 10 | 0.9307 | 0.0388 | 0.8605 | 0.9747 | 0.8938 | dentro |
| `metricas_firmas_semillas.csv` | 122_sin_seleccion | RandomForest | multiclase 4 categorías de ataque sobre los ataques de D2 de tipo cono… | `f1_macro` | 10 | 0.7838 | 0.0390 | 0.7155 | 0.8435 | 0.6956 | **FUERA** |
| `metricas_firmas_semillas.csv` | 122_sin_seleccion | RandomForest | multiclase 4 categorías de ataque sobre los ataques de D2 de tipo cono… | `f1_u2r` | 10 | 0.4920 | 0.1026 | 0.3182 | 0.6429 | 0.3182 | dentro |
| `metricas_firmas_semillas.csv` | 122_sin_seleccion | RandomForest | multiclase 4 categorías de ataque sobre los ataques de D2 de tipo cono… | `recall_macro` | 10 | 0.8267 | 0.0504 | 0.7480 | 0.8852 | 0.7458 | **FUERA** |
| `metricas_firmas_semillas.csv` | 54 | DecisionTree | multiclase 4 categorías de ataque sobre los ataques de D2 de tipo cono… | `accuracy_D2` | 10 | 0.8850 | 0.0242 | 0.8440 | 0.9145 | 0.9135 | dentro |
| `metricas_firmas_semillas.csv` | 54 | DecisionTree | multiclase 4 categorías de ataque sobre los ataques de D2 de tipo cono… | `f1_macro` | 10 | 0.6876 | 0.0533 | 0.5976 | 0.7464 | 0.7456 | dentro |
| `metricas_firmas_semillas.csv` | 54 | DecisionTree | multiclase 4 categorías de ataque sobre los ataques de D2 de tipo cono… | `f1_u2r` | 10 | 0.2514 | 0.1533 | 0.0464 | 0.4138 | 0.3607 | dentro |
| `metricas_firmas_semillas.csv` | 54 | DecisionTree | multiclase 4 categorías de ataque sobre los ataques de D2 de tipo cono… | `recall_macro` | 10 | 0.7375 | 0.0282 | 0.6827 | 0.7672 | 0.7668 | dentro |
| `metricas_firmas_semillas.csv` | 54 | HistGradientBoosting | multiclase 4 categorías de ataque sobre los ataques de D2 de tipo cono… | `accuracy_D2` | 10 | 0.9406 | 0.0140 | 0.9180 | 0.9538 | 0.9577 | **FUERA** |
| `metricas_firmas_semillas.csv` | 54 | HistGradientBoosting | multiclase 4 categorías de ataque sobre los ataques de D2 de tipo cono… | `f1_macro` | 10 | 0.7929 | 0.0184 | 0.7680 | 0.8327 | 0.8041 | dentro |
| `metricas_firmas_semillas.csv` | 54 | HistGradientBoosting | multiclase 4 categorías de ataque sobre los ataques de D2 de tipo cono… | `f1_u2r` | 10 | 0.4823 | 0.0607 | 0.3797 | 0.5747 | 0.4318 | dentro |
| `metricas_firmas_semillas.csv` | 54 | HistGradientBoosting | multiclase 4 categorías de ataque sobre los ataques de D2 de tipo cono… | `recall_macro` | 10 | 0.8382 | 0.0213 | 0.8057 | 0.8756 | 0.8407 | dentro |
| `metricas_firmas_semillas.csv` | 54 | KNN | multiclase 4 categorías de ataque sobre los ataques de D2 de tipo cono… | `accuracy_D2` | 10 | 0.9559 | 0.0053 | 0.9489 | 0.9651 | 0.9564 | dentro |
| `metricas_firmas_semillas.csv` | 54 | KNN | multiclase 4 categorías de ataque sobre los ataques de D2 de tipo cono… | `f1_macro` | 10 | 0.7710 | 0.0079 | 0.7603 | 0.7841 | 0.7687 | dentro |
| `metricas_firmas_semillas.csv` | 54 | KNN | multiclase 4 categorías de ataque sobre los ataques de D2 de tipo cono… | `f1_u2r` | 10 | 0.2584 | 0.0129 | 0.2295 | 0.2705 | 0.2445 | dentro |
| `metricas_firmas_semillas.csv` | 54 | KNN | multiclase 4 categorías de ataque sobre los ataques de D2 de tipo cono… | `recall_macro` | 10 | 0.8961 | 0.0063 | 0.8854 | 0.9062 | 0.8974 | dentro |
| `metricas_firmas_semillas.csv` | 54 | RandomForest | multiclase 4 categorías de ataque sobre los ataques de D2 de tipo cono… | `accuracy_D2` | 10 | 0.9484 | 0.0134 | 0.9309 | 0.9705 | 0.9683 | dentro |
| `metricas_firmas_semillas.csv` | 54 | RandomForest | multiclase 4 categorías de ataque sobre los ataques de D2 de tipo cono… | `f1_macro` | 10 | 0.8035 | 0.0146 | 0.7779 | 0.8205 | 0.8223 | **FUERA** |
| `metricas_firmas_semillas.csv` | 54 | RandomForest | multiclase 4 categorías de ataque sobre los ataques de D2 de tipo cono… | `f1_u2r` | 10 | 0.4910 | 0.0657 | 0.4054 | 0.5902 | 0.4524 | dentro |
| `metricas_firmas_semillas.csv` | 54 | RandomForest | multiclase 4 categorías de ataque sobre los ataques de D2 de tipo cono… | `recall_macro` | 10 | 0.8126 | 0.0156 | 0.7839 | 0.8370 | 0.8496 | **FUERA** |
| `metricas_hibrido_semillas.csv` | 122_sin_seleccion | Autoencoder->RandomForest | cascada extremo a extremo (5 clases + unknown) sobre D2 completo; ojo:… | `bin_accuracy` | 10 | 0.8597 | 0.0215 | 0.8275 | 0.8860 | 0.8567 | dentro |
| `metricas_hibrido_semillas.csv` | 122_sin_seleccion | Autoencoder->RandomForest | cascada extremo a extremo (5 clases + unknown) sobre D2 completo; ojo:… | `bin_fpr` | 10 | 0.0861 | 0.0138 | 0.0488 | 0.0978 | 0.0849 | dentro |
| `metricas_hibrido_semillas.csv` | 122_sin_seleccion | Autoencoder->RandomForest | cascada extremo a extremo (5 clases + unknown) sobre D2 completo; ojo:… | `bin_recall` | 10 | 0.8187 | 0.0414 | 0.7644 | 0.8666 | 0.8125 | dentro |
| `metricas_hibrido_semillas.csv` | 122_sin_seleccion | Autoencoder->RandomForest | cascada extremo a extremo (5 clases + unknown) sobre D2 completo; ojo:… | `conocida_f1_macro` | 10 | 0.6757 | 0.0709 | 0.6077 | 0.7909 | 0.6554 | dentro |
| `metricas_hibrido_semillas.csv` | 122_sin_seleccion | Autoencoder->RandomForest | cascada extremo a extremo (5 clases + unknown) sobre D2 completo; ojo:… | `fpr_cascada` | 10 | 0.0861 | 0.0138 | 0.0488 | 0.0978 | 0.0849 | dentro |
| `metricas_hibrido_semillas.csv` | 122_sin_seleccion | Autoencoder->RandomForest | cascada extremo a extremo (5 clases + unknown) sobre D2 completo; ojo:… | `recall_0day_global` | 10 | 0.7363 | 0.0409 | 0.6669 | 0.7800 | 0.7853 | **FUERA** |
| `metricas_hibrido_semillas.csv` | 122_sin_seleccion | Autoencoder->RandomForest | cascada extremo a extremo (5 clases + unknown) sobre D2 completo; ojo:… | `umbral_conf_elegido` | 10 | 0.4700 | 0.0483 | 0.4000 | 0.5000 | 0.5000 | dentro |
| `metricas_hibrido_semillas.csv` | 54 | Autoencoder->RandomForest | cascada extremo a extremo (5 clases + unknown) sobre D2 completo; ojo:… | `bin_accuracy` | 10 | 0.8614 | 0.0156 | 0.8395 | 0.8824 | 0.8605 | dentro |
| `metricas_hibrido_semillas.csv` | 54 | Autoencoder->RandomForest | cascada extremo a extremo (5 clases + unknown) sobre D2 completo; ojo:… | `bin_fpr` | 10 | 0.0986 | 0.0050 | 0.0934 | 0.1070 | 0.1017 | dentro |
| `metricas_hibrido_semillas.csv` | 54 | Autoencoder->RandomForest | cascada extremo a extremo (5 clases + unknown) sobre D2 completo; ojo:… | `bin_recall` | 10 | 0.8312 | 0.0269 | 0.7939 | 0.8656 | 0.8318 | dentro |
| `metricas_hibrido_semillas.csv` | 54 | Autoencoder->RandomForest | cascada extremo a extremo (5 clases + unknown) sobre D2 completo; ojo:… | `conocida_f1_macro` | 10 | 0.7325 | 0.0290 | 0.6789 | 0.7706 | 0.7481 | dentro |
| `metricas_hibrido_semillas.csv` | 54 | Autoencoder->RandomForest | cascada extremo a extremo (5 clases + unknown) sobre D2 completo; ojo:… | `fpr_cascada` | 10 | 0.0986 | 0.0050 | 0.0934 | 0.1070 | 0.1017 | dentro |
| `metricas_hibrido_semillas.csv` | 54 | Autoencoder->RandomForest | cascada extremo a extremo (5 clases + unknown) sobre D2 completo; ojo:… | `recall_0day_global` | 10 | 0.7531 | 0.0173 | 0.7232 | 0.7771 | 0.7707 | dentro |
| `metricas_hibrido_semillas.csv` | 54 | Autoencoder->RandomForest | cascada extremo a extremo (5 clases + unknown) sobre D2 completo; ojo:… | `umbral_conf_elegido` | 10 | 0.4800 | 0.0632 | 0.4000 | 0.6000 | 0.5000 | dentro |

#### Bloque de máquina (NO es calidad y NO se cita como resultado)

Se publica aparte a propósito: es *wall-clock* en máquina no dedicada, de modo que su `sd` mide
**carga de máquina** y no el algoritmo. Dos observaciones distintas lo respaldan, y **no deben
leerse juntas** porque proceden de corridas distintas:

- **Dispersión del `tiempo_s`, sin causa atribuida.** El `tiempo_s` del Autoencoder de 54
  características va de **37,71 s** (`commit 38fdd4b`) a **181,91 s** (`commit 5516b60`), un factor
  **4,8×**, con **calidad idéntica al bit**. Ninguna de esas dos corridas registra el recuento de
  épocas, de modo que la banda se declara como **magnitud observada** y **no se atribuye** ni a
  épocas ni a carga de máquina.
- **Recuento de épocas.** La columna que lo registra, `n_iter_total_grid`, existe **solo** en
  `ac496cb` y `1163c90`; en esas dos corridas da **162** en la variante de 54 características y
  **128** en la de 122. Esa columna **no separa causas** y no decide si una diferencia de tiempo es
  de épocas o de carga de máquina.

> [!warning] Salvedad obligatoria: `ac496cb` no es reproducible desde git
> Los recuentos de épocas se apoyan en parte en la corrida `ac496cb`, cuyos CSV **nunca se
> commitearon** y fueron **sobrescritos por `1163c90`**: sobreviven solo citados en
> `Implementacion\PIPELINE.md`. **Un tercero no puede recalcular ese dato** desde el repositorio;
> vale como observación declarada, no como evidencia verificable.

En ningún caso son estos segundos una propiedad del algoritmo.

| Tabla de origen | Variante | Algoritmo | Alcance | Métrica | n | Media | sd | Mín | Máx |
|---|---|---|---|---|---:|---:|---:|---:|---:|
| `metricas_anomalias_semillas.csv` | 122_sin_seleccion | Autoencoder | binario normal-vs-ataque (2 clases) sobre D2 completo | `flujos_por_segundo` | 10 | 721485.9600 | 117671.0275 | 535460.2000 | 904920.0000 |
| `metricas_anomalias_semillas.csv` | 122_sin_seleccion | Autoencoder | binario normal-vs-ataque (2 clases) sobre D2 completo | `latencia_ms_por_flujo` | 10 | 0.0014 | 0.0003 | 0.0011 | 0.0019 |
| `metricas_anomalias_semillas.csv` | 122_sin_seleccion | Autoencoder | binario normal-vs-ataque (2 clases) sobre D2 completo | `tiempo_entrenamiento_s` | 10 | 35.7019 | 15.8000 | 19.3230 | 70.0510 |
| `metricas_anomalias_semillas.csv` | 122_sin_seleccion | Autoencoder | binario normal-vs-ataque (2 clases) sobre D2 completo | `tiempo_inferencia_s` | 10 | 0.0320 | 0.0055 | 0.0250 | 0.0420 |
| `metricas_anomalias_semillas.csv` | 122_sin_seleccion | Autoencoder | binario normal-vs-ataque (2 clases) sobre D2 completo | `tiempo_s` | 10 | 35.9550 | 15.8082 | 19.5900 | 70.3300 |
| `metricas_anomalias_semillas.csv` | 122_sin_seleccion | IsolationForest | binario normal-vs-ataque (2 clases) sobre D2 completo | `flujos_por_segundo` | 10 | 116008.7300 | 56548.0205 | 63219.4000 | 201214.4000 |
| `metricas_anomalias_semillas.csv` | 122_sin_seleccion | IsolationForest | binario normal-vs-ataque (2 clases) sobre D2 completo | `latencia_ms_por_flujo` | 10 | 0.0105 | 0.0044 | 0.0050 | 0.0158 |
| `metricas_anomalias_semillas.csv` | 122_sin_seleccion | IsolationForest | binario normal-vs-ataque (2 clases) sobre D2 completo | `tiempo_entrenamiento_s` | 10 | 2.9860 | 0.1194 | 2.8740 | 3.2150 |
| `metricas_anomalias_semillas.csv` | 122_sin_seleccion | IsolationForest | binario normal-vs-ataque (2 clases) sobre D2 completo | `tiempo_inferencia_s` | 10 | 0.2356 | 0.0981 | 0.1120 | 0.3570 |
| `metricas_anomalias_semillas.csv` | 122_sin_seleccion | IsolationForest | binario normal-vs-ataque (2 clases) sobre D2 completo | `tiempo_s` | 10 | 4.6690 | 0.1880 | 4.3900 | 4.9100 |
| `metricas_anomalias_semillas.csv` | 122_sin_seleccion | LocalOutlierFactor | binario normal-vs-ataque (2 clases) sobre D2 completo | `flujos_por_segundo` | 10 | 12360.0200 | 151.4281 | 12182.7000 | 12590.2000 |
| `metricas_anomalias_semillas.csv` | 122_sin_seleccion | LocalOutlierFactor | binario normal-vs-ataque (2 clases) sobre D2 completo | `latencia_ms_por_flujo` | 10 | 0.0809 | 0.0010 | 0.0794 | 0.0821 |
| `metricas_anomalias_semillas.csv` | 122_sin_seleccion | LocalOutlierFactor | binario normal-vs-ataque (2 clases) sobre D2 completo | `tiempo_entrenamiento_s` | 10 | 16.1018 | 0.4619 | 15.2940 | 17.0710 |
| `metricas_anomalias_semillas.csv` | 122_sin_seleccion | LocalOutlierFactor | binario normal-vs-ataque (2 clases) sobre D2 completo | `tiempo_inferencia_s` | 10 | 1.8242 | 0.0222 | 1.7910 | 1.8500 |
| `metricas_anomalias_semillas.csv` | 122_sin_seleccion | LocalOutlierFactor | binario normal-vs-ataque (2 clases) sobre D2 completo | `tiempo_s` | 10 | 25.0140 | 0.5478 | 24.0900 | 26.1500 |
| `metricas_anomalias_semillas.csv` | 122_sin_seleccion | OneClassSVM | binario normal-vs-ataque (2 clases) sobre D2 completo | `flujos_por_segundo` | 10 | 13891.9600 | 456.9030 | 13088.6000 | 14463.3000 |
| `metricas_anomalias_semillas.csv` | 122_sin_seleccion | OneClassSVM | binario normal-vs-ataque (2 clases) sobre D2 completo | `latencia_ms_por_flujo` | 10 | 0.0721 | 0.0024 | 0.0691 | 0.0764 |
| `metricas_anomalias_semillas.csv` | 122_sin_seleccion | OneClassSVM | binario normal-vs-ataque (2 clases) sobre D2 completo | `tiempo_entrenamiento_s` | 10 | 23.3979 | 0.4999 | 22.5930 | 24.4720 |
| `metricas_anomalias_semillas.csv` | 122_sin_seleccion | OneClassSVM | binario normal-vs-ataque (2 clases) sobre D2 completo | `tiempo_inferencia_s` | 10 | 1.6244 | 0.0542 | 1.5590 | 1.7220 |
| `metricas_anomalias_semillas.csv` | 122_sin_seleccion | OneClassSVM | binario normal-vs-ataque (2 clases) sobre D2 completo | `tiempo_s` | 10 | 39.3010 | 0.8445 | 38.1800 | 40.4900 |
| `metricas_anomalias_semillas.csv` | 54 | Autoencoder | binario normal-vs-ataque (2 clases) sobre D2 completo | `flujos_por_segundo` | 10 | 912386.9500 | 170907.2347 | 726391.6000 | 1189782.6000 |
| `metricas_anomalias_semillas.csv` | 54 | Autoencoder | binario normal-vs-ataque (2 clases) sobre D2 completo | `latencia_ms_por_flujo` | 10 | 0.0011 | 0.0002 | 0.0008 | 0.0014 |
| `metricas_anomalias_semillas.csv` | 54 | Autoencoder | binario normal-vs-ataque (2 clases) sobre D2 completo | `tiempo_entrenamiento_s` | 10 | 22.3951 | 7.0837 | 8.6730 | 31.9610 |
| `metricas_anomalias_semillas.csv` | 54 | Autoencoder | binario normal-vs-ataque (2 clases) sobre D2 completo | `tiempo_inferencia_s` | 10 | 0.0255 | 0.0043 | 0.0190 | 0.0310 |
| `metricas_anomalias_semillas.csv` | 54 | Autoencoder | binario normal-vs-ataque (2 clases) sobre D2 completo | `tiempo_s` | 10 | 22.6230 | 7.0907 | 8.8900 | 32.1800 |
| `metricas_anomalias_semillas.csv` | 54 | IsolationForest | binario normal-vs-ataque (2 clases) sobre D2 completo | `flujos_por_segundo` | 10 | 134959.0900 | 51455.4713 | 64631.2000 | 191575.1000 |
| `metricas_anomalias_semillas.csv` | 54 | IsolationForest | binario normal-vs-ataque (2 clases) sobre D2 completo | `latencia_ms_por_flujo` | 10 | 0.0086 | 0.0036 | 0.0052 | 0.0155 |
| `metricas_anomalias_semillas.csv` | 54 | IsolationForest | binario normal-vs-ataque (2 clases) sobre D2 completo | `tiempo_entrenamiento_s` | 10 | 2.8595 | 0.1742 | 2.6260 | 3.2500 |
| `metricas_anomalias_semillas.csv` | 54 | IsolationForest | binario normal-vs-ataque (2 clases) sobre D2 completo | `tiempo_inferencia_s` | 10 | 0.1939 | 0.0804 | 0.1180 | 0.3490 |
| `metricas_anomalias_semillas.csv` | 54 | IsolationForest | binario normal-vs-ataque (2 clases) sobre D2 completo | `tiempo_s` | 10 | 4.5660 | 0.2625 | 4.3200 | 5.1500 |
| `metricas_anomalias_semillas.csv` | 54 | LocalOutlierFactor | binario normal-vs-ataque (2 clases) sobre D2 completo | `flujos_por_segundo` | 10 | 22252.8000 | 1903.3129 | 17944.4000 | 25193.1000 |
| `metricas_anomalias_semillas.csv` | 54 | LocalOutlierFactor | binario normal-vs-ataque (2 clases) sobre D2 completo | `latencia_ms_por_flujo` | 10 | 0.0453 | 0.0043 | 0.0397 | 0.0557 |
| `metricas_anomalias_semillas.csv` | 54 | LocalOutlierFactor | binario normal-vs-ataque (2 clases) sobre D2 completo | `tiempo_entrenamiento_s` | 10 | 10.5086 | 0.5574 | 9.3800 | 11.6360 |
| `metricas_anomalias_semillas.csv` | 54 | LocalOutlierFactor | binario normal-vs-ataque (2 clases) sobre D2 completo | `tiempo_inferencia_s` | 10 | 1.0205 | 0.0968 | 0.8950 | 1.2560 |
| `metricas_anomalias_semillas.csv` | 54 | LocalOutlierFactor | binario normal-vs-ataque (2 clases) sobre D2 completo | `tiempo_s` | 10 | 15.9430 | 0.9189 | 14.2400 | 17.9600 |
| `metricas_anomalias_semillas.csv` | 54 | OneClassSVM | binario normal-vs-ataque (2 clases) sobre D2 completo | `flujos_por_segundo` | 10 | 10840.2000 | 3818.6411 | 8145.9000 | 16855.5000 |
| `metricas_anomalias_semillas.csv` | 54 | OneClassSVM | binario normal-vs-ataque (2 clases) sobre D2 completo | `latencia_ms_por_flujo` | 10 | 0.1010 | 0.0276 | 0.0593 | 0.1228 |
| `metricas_anomalias_semillas.csv` | 54 | OneClassSVM | binario normal-vs-ataque (2 clases) sobre D2 completo | `tiempo_entrenamiento_s` | 10 | 10.4263 | 0.2990 | 10.2130 | 11.2060 |
| `metricas_anomalias_semillas.csv` | 54 | OneClassSVM | binario normal-vs-ataque (2 clases) sobre D2 completo | `tiempo_inferencia_s` | 10 | 2.2766 | 0.6225 | 1.3370 | 2.7680 |
| `metricas_anomalias_semillas.csv` | 54 | OneClassSVM | binario normal-vs-ataque (2 clases) sobre D2 completo | `tiempo_s` | 10 | 24.9240 | 0.9084 | 23.1900 | 25.7300 |
| `metricas_baseline_semillas.csv` | 122_sin_seleccion | RandomForest_monolitico | multiclase 5 clases (normal + 4 ataques) sobre D2 completo | `flujos_por_segundo` | 10 | 262583.8000 | 106516.3367 | 143196.9000 | 374553.5000 |
| `metricas_baseline_semillas.csv` | 122_sin_seleccion | RandomForest_monolitico | multiclase 5 clases (normal + 4 ataques) sobre D2 completo | `latencia_ms_por_flujo` | 10 | 0.0045 | 0.0018 | 0.0027 | 0.0070 |
| `metricas_baseline_semillas.csv` | 122_sin_seleccion | RandomForest_monolitico | multiclase 5 clases (normal + 4 ataques) sobre D2 completo | `tiempo_entrenamiento_s` | 10 | 37.0471 | 1.0061 | 35.1510 | 38.4950 |
| `metricas_baseline_semillas.csv` | 122_sin_seleccion | RandomForest_monolitico | multiclase 5 clases (normal + 4 ataques) sobre D2 completo | `tiempo_inferencia_s` | 10 | 0.1008 | 0.0414 | 0.0600 | 0.1570 |
| `metricas_baseline_semillas.csv` | 122_sin_seleccion | RandomForest_monolitico | multiclase 5 clases (normal + 4 ataques) sobre D2 completo | `tiempo_s` | 10 | 37.0460 | 1.0053 | 35.1500 | 38.4900 |
| `metricas_baseline_semillas.csv` | 54 | RandomForest_monolitico | multiclase 5 clases (normal + 4 ataques) sobre D2 completo | `flujos_por_segundo` | 10 | 276574.0200 | 112872.4809 | 157752.7000 | 388837.8000 |
| `metricas_baseline_semillas.csv` | 54 | RandomForest_monolitico | multiclase 5 clases (normal + 4 ataques) sobre D2 completo | `latencia_ms_por_flujo` | 10 | 0.0043 | 0.0017 | 0.0026 | 0.0063 |
| `metricas_baseline_semillas.csv` | 54 | RandomForest_monolitico | multiclase 5 clases (normal + 4 ataques) sobre D2 completo | `tiempo_entrenamiento_s` | 10 | 31.9097 | 1.0484 | 30.5180 | 33.4390 |
| `metricas_baseline_semillas.csv` | 54 | RandomForest_monolitico | multiclase 5 clases (normal + 4 ataques) sobre D2 completo | `tiempo_inferencia_s` | 10 | 0.0958 | 0.0394 | 0.0580 | 0.1430 |
| `metricas_baseline_semillas.csv` | 54 | RandomForest_monolitico | multiclase 5 clases (normal + 4 ataques) sobre D2 completo | `tiempo_s` | 10 | 31.9080 | 1.0477 | 30.5200 | 33.4400 |
| `metricas_firmas_semillas.csv` | 122_sin_seleccion | DecisionTree | multiclase 4 categorías de ataque sobre los ataques de D2 de tipo cono… | `flujos_por_segundo` | 10 | 2747904.1400 | 426379.6864 | 1916972.7000 | 3063303.1000 |
| `metricas_firmas_semillas.csv` | 122_sin_seleccion | DecisionTree | multiclase 4 categorías de ataque sobre los ataques de D2 de tipo cono… | `latencia_ms_por_flujo` | 10 | 0.0004 | 0.0001 | 0.0003 | 0.0005 |
| `metricas_firmas_semillas.csv` | 122_sin_seleccion | DecisionTree | multiclase 4 categorías de ataque sobre los ataques de D2 de tipo cono… | `tiempo_entrenamiento_s` | 10 | 13.7895 | 11.9127 | 2.1560 | 26.9810 |
| `metricas_firmas_semillas.csv` | 122_sin_seleccion | DecisionTree | multiclase 4 categorías de ataque sobre los ataques de D2 de tipo cono… | `tiempo_inferencia_s` | 10 | 0.0034 | 0.0008 | 0.0030 | 0.0050 |
| `metricas_firmas_semillas.csv` | 122_sin_seleccion | DecisionTree | multiclase 4 categorías de ataque sobre los ataques de D2 de tipo cono… | `tiempo_s` | 10 | 14.0710 | 11.9082 | 2.4400 | 27.2500 |
| `metricas_firmas_semillas.csv` | 122_sin_seleccion | HistGradientBoosting | multiclase 4 categorías de ataque sobre los ataques de D2 de tipo cono… | `flujos_por_segundo` | 10 | 172115.9900 | 29299.7587 | 109205.2000 | 216798.7000 |
| `metricas_firmas_semillas.csv` | 122_sin_seleccion | HistGradientBoosting | multiclase 4 categorías de ataque sobre los ataques de D2 de tipo cono… | `latencia_ms_por_flujo` | 10 | 0.0060 | 0.0013 | 0.0046 | 0.0092 |
| `metricas_firmas_semillas.csv` | 122_sin_seleccion | HistGradientBoosting | multiclase 4 categorías de ataque sobre los ataques de D2 de tipo cono… | `tiempo_entrenamiento_s` | 10 | 136.5404 | 14.9129 | 112.3730 | 164.7980 |
| `metricas_firmas_semillas.csv` | 122_sin_seleccion | HistGradientBoosting | multiclase 4 categorías de ataque sobre los ataques de D2 de tipo cono… | `tiempo_inferencia_s` | 10 | 0.0544 | 0.0114 | 0.0420 | 0.0830 |
| `metricas_firmas_semillas.csv` | 122_sin_seleccion | HistGradientBoosting | multiclase 4 categorías de ataque sobre los ataques de D2 de tipo cono… | `tiempo_s` | 10 | 136.9500 | 14.9147 | 112.7800 | 165.2400 |
| `metricas_firmas_semillas.csv` | 122_sin_seleccion | KNN | multiclase 4 categorías de ataque sobre los ataques de D2 de tipo cono… | `flujos_por_segundo` | 10 | 3540.8600 | 160.0837 | 3340.6000 | 3804.4000 |
| `metricas_firmas_semillas.csv` | 122_sin_seleccion | KNN | multiclase 4 categorías de ataque sobre los ataques de D2 de tipo cono… | `latencia_ms_por_flujo` | 10 | 0.2829 | 0.0125 | 0.2629 | 0.2993 |
| `metricas_firmas_semillas.csv` | 122_sin_seleccion | KNN | multiclase 4 categorías de ataque sobre los ataques de D2 de tipo cono… | `tiempo_entrenamiento_s` | 10 | 79.4062 | 2.0220 | 77.4130 | 84.2620 |
| `metricas_firmas_semillas.csv` | 122_sin_seleccion | KNN | multiclase 4 categorías de ataque sobre los ataques de D2 de tipo cono… | `tiempo_inferencia_s` | 10 | 2.5698 | 0.1139 | 2.3870 | 2.7190 |
| `metricas_firmas_semillas.csv` | 122_sin_seleccion | KNN | multiclase 4 categorías de ataque sobre los ataques de D2 de tipo cono… | `tiempo_s` | 10 | 82.3250 | 1.9750 | 80.4700 | 87.1700 |
| `metricas_firmas_semillas.csv` | 122_sin_seleccion | RandomForest | multiclase 4 categorías de ataque sobre los ataques de D2 de tipo cono… | `flujos_por_segundo` | 10 | 174828.9200 | 62964.6506 | 115243.8000 | 278223.6000 |
| `metricas_firmas_semillas.csv` | 122_sin_seleccion | RandomForest | multiclase 4 categorías de ataque sobre los ataques de D2 de tipo cono… | `latencia_ms_por_flujo` | 10 | 0.0064 | 0.0021 | 0.0036 | 0.0087 |
| `metricas_firmas_semillas.csv` | 122_sin_seleccion | RandomForest | multiclase 4 categorías de ataque sobre los ataques de D2 de tipo cono… | `tiempo_entrenamiento_s` | 10 | 40.1839 | 24.8803 | 10.8740 | 62.0990 |
| `metricas_firmas_semillas.csv` | 122_sin_seleccion | RandomForest | multiclase 4 categorías de ataque sobre los ataques de D2 de tipo cono… | `tiempo_inferencia_s` | 10 | 0.0581 | 0.0186 | 0.0330 | 0.0790 |
| `metricas_firmas_semillas.csv` | 122_sin_seleccion | RandomForest | multiclase 4 categorías de ataque sobre los ataques de D2 de tipo cono… | `tiempo_s` | 10 | 40.5490 | 24.8946 | 11.2000 | 62.4800 |
| `metricas_firmas_semillas.csv` | 54 | DecisionTree | multiclase 4 categorías de ataque sobre los ataques de D2 de tipo cono… | `flujos_por_segundo` | 10 | 4166870.5600 | 325600.7992 | 3769349.0000 | 4656277.1000 |
| `metricas_firmas_semillas.csv` | 54 | DecisionTree | multiclase 4 categorías de ataque sobre los ataques de D2 de tipo cono… | `latencia_ms_por_flujo` | 10 | 0.0002 | 0.0000 | 0.0002 | 0.0003 |
| `metricas_firmas_semillas.csv` | 54 | DecisionTree | multiclase 4 categorías de ataque sobre los ataques de D2 de tipo cono… | `tiempo_entrenamiento_s` | 10 | 12.5740 | 7.4287 | 1.7500 | 17.4390 |
| `metricas_firmas_semillas.csv` | 54 | DecisionTree | multiclase 4 categorías de ataque sobre los ataques de D2 de tipo cono… | `tiempo_inferencia_s` | 10 | 0.0020 | 0.0000 | 0.0020 | 0.0020 |
| `metricas_firmas_semillas.csv` | 54 | DecisionTree | multiclase 4 categorías de ataque sobre los ataques de D2 de tipo cono… | `tiempo_s` | 10 | 12.8510 | 7.4260 | 2.0400 | 17.7300 |
| `metricas_firmas_semillas.csv` | 54 | HistGradientBoosting | multiclase 4 categorías de ataque sobre los ataques de D2 de tipo cono… | `flujos_por_segundo` | 10 | 158198.7400 | 74244.3300 | 71105.9000 | 299890.7000 |
| `metricas_firmas_semillas.csv` | 54 | HistGradientBoosting | multiclase 4 categorías de ataque sobre los ataques de D2 de tipo cono… | `latencia_ms_por_flujo` | 10 | 0.0076 | 0.0034 | 0.0033 | 0.0141 |
| `metricas_firmas_semillas.csv` | 54 | HistGradientBoosting | multiclase 4 categorías de ataque sobre los ataques de D2 de tipo cono… | `tiempo_entrenamiento_s` | 10 | 69.4763 | 3.9821 | 64.7330 | 79.0080 |
| `metricas_firmas_semillas.csv` | 54 | HistGradientBoosting | multiclase 4 categorías de ataque sobre los ataques de D2 de tipo cono… | `tiempo_inferencia_s` | 10 | 0.0693 | 0.0311 | 0.0300 | 0.1280 |
| `metricas_firmas_semillas.csv` | 54 | HistGradientBoosting | multiclase 4 categorías de ataque sobre los ataques de D2 de tipo cono… | `tiempo_s` | 10 | 69.9050 | 3.9838 | 65.1600 | 79.3700 |
| `metricas_firmas_semillas.csv` | 54 | KNN | multiclase 4 categorías de ataque sobre los ataques de D2 de tipo cono… | `flujos_por_segundo` | 10 | 5440.4800 | 243.4515 | 5076.1000 | 5976.4000 |
| `metricas_firmas_semillas.csv` | 54 | KNN | multiclase 4 categorías de ataque sobre los ataques de D2 de tipo cono… | `latencia_ms_por_flujo` | 10 | 0.1841 | 0.0080 | 0.1673 | 0.1970 |
| `metricas_firmas_semillas.csv` | 54 | KNN | multiclase 4 categorías de ataque sobre los ataques de D2 de tipo cono… | `tiempo_entrenamiento_s` | 10 | 49.6723 | 0.9327 | 48.7730 | 51.6080 |
| `metricas_firmas_semillas.csv` | 54 | KNN | multiclase 4 categorías de ataque sobre los ataques de D2 de tipo cono… | `tiempo_inferencia_s` | 10 | 1.6725 | 0.0728 | 1.5200 | 1.7890 |
| `metricas_firmas_semillas.csv` | 54 | KNN | multiclase 4 categorías de ataque sobre los ataques de D2 de tipo cono… | `tiempo_s` | 10 | 51.6900 | 0.9371 | 50.7800 | 53.7300 |
| `metricas_firmas_semillas.csv` | 54 | RandomForest | multiclase 4 categorías de ataque sobre los ataques de D2 de tipo cono… | `flujos_por_segundo` | 10 | 203763.2800 | 69797.7417 | 105459.7000 | 277675.0000 |
| `metricas_firmas_semillas.csv` | 54 | RandomForest | multiclase 4 categorías de ataque sobre los ataques de D2 de tipo cono… | `latencia_ms_por_flujo` | 10 | 0.0056 | 0.0023 | 0.0036 | 0.0095 |
| `metricas_firmas_semillas.csv` | 54 | RandomForest | multiclase 4 categorías de ataque sobre los ataques de D2 de tipo cono… | `tiempo_entrenamiento_s` | 10 | 31.6166 | 23.0660 | 9.4280 | 56.1030 |
| `metricas_firmas_semillas.csv` | 54 | RandomForest | multiclase 4 categorías de ataque sobre los ataques de D2 de tipo cono… | `tiempo_inferencia_s` | 10 | 0.0507 | 0.0205 | 0.0330 | 0.0860 |
| `metricas_firmas_semillas.csv` | 54 | RandomForest | multiclase 4 categorías de ataque sobre los ataques de D2 de tipo cono… | `tiempo_s` | 10 | 31.9970 | 23.0504 | 9.7600 | 56.4800 |
| `metricas_hibrido_semillas.csv` | 122_sin_seleccion | Autoencoder->RandomForest | cascada extremo a extremo (5 clases + unknown) sobre D2 completo; ojo:… | `flujos_por_segundo` | 10 | 241264.4400 | 52746.0031 | 179940.3000 | 327785.0000 |
| `metricas_hibrido_semillas.csv` | 122_sin_seleccion | Autoencoder->RandomForest | cascada extremo a extremo (5 clases + unknown) sobre D2 completo; ojo:… | `latencia_ms_por_flujo` | 10 | 0.0043 | 0.0009 | 0.0031 | 0.0056 |
| `metricas_hibrido_semillas.csv` | 122_sin_seleccion | Autoencoder->RandomForest | cascada extremo a extremo (5 clases + unknown) sobre D2 completo; ojo:… | `tiempo_entrenamiento_s` | 10 | 14.5081 | 8.7821 | 5.2790 | 25.3500 |
| `metricas_hibrido_semillas.csv` | 122_sin_seleccion | Autoencoder->RandomForest | cascada extremo a extremo (5 clases + unknown) sobre D2 completo; ojo:… | `tiempo_inferencia_s` | 10 | 0.0972 | 0.0199 | 0.0690 | 0.1250 |
| `metricas_hibrido_semillas.csv` | 122_sin_seleccion | Autoencoder->RandomForest | cascada extremo a extremo (5 clases + unknown) sobre D2 completo; ojo:… | `tiempo_s` | 10 | 16.7520 | 8.8076 | 7.4700 | 27.5900 |
| `metricas_hibrido_semillas.csv` | 54 | Autoencoder->RandomForest | cascada extremo a extremo (5 clases + unknown) sobre D2 completo; ojo:… | `flujos_por_segundo` | 10 | 359484.4500 | 76843.0165 | 240304.3000 | 432984.7000 |
| `metricas_hibrido_semillas.csv` | 54 | Autoencoder->RandomForest | cascada extremo a extremo (5 clases + unknown) sobre D2 completo; ojo:… | `latencia_ms_por_flujo` | 10 | 0.0029 | 0.0007 | 0.0023 | 0.0042 |
| `metricas_hibrido_semillas.csv` | 54 | Autoencoder->RandomForest | cascada extremo a extremo (5 clases + unknown) sobre D2 completo; ojo:… | `tiempo_entrenamiento_s` | 10 | 9.6319 | 5.2529 | 5.2470 | 22.3690 |
| `metricas_hibrido_semillas.csv` | 54 | Autoencoder->RandomForest | cascada extremo a extremo (5 clases + unknown) sobre D2 completo; ojo:… | `tiempo_inferencia_s` | 10 | 0.0658 | 0.0166 | 0.0520 | 0.0940 |
| `metricas_hibrido_semillas.csv` | 54 | Autoencoder->RandomForest | cascada extremo a extremo (5 clases + unknown) sobre D2 completo; ojo:… | `tiempo_s` | 10 | 12.1350 | 5.9565 | 6.9600 | 24.0800 |

### Decisiones no constantes entre semillas

En **15 celdas distintas** de la agregación, la columna de **decisión** (`config_ganadora` o
`balanceo`) **no fue la misma en las diez semillas**: la media de esas celdas promedia modelos con
decisiones distintas, y hay que declararlo al citarla. La cifra afecta a **140 de las 198 filas**
agregadas.

> [!note] 19 líneas de aviso, 15 celdas
> El bloque «Avisos de la agregación» del artefacto tiene **19 líneas**, no 15: cuatro celdas de
> firmas (`54 · DecisionTree`, `54 · RandomForest`, `122_sin_seleccion · DecisionTree`,
> `122_sin_seleccion · RandomForest`) generan **dos avisos cada una**, uno por `balanceo` y otro por
> `config_ganadora`. 19 − 4 = **15 celdas distintas**, que es la cifra que se cita aquí y la que
> usan `Implementacion/PIPELINE.md` y `Resultados/GUIA_RESULTADOS.md`.

El reparto exacto, semilla a semilla, está en la columna `decisiones_no_constantes` del CSV y en el
bloque «Avisos de la agregación» de `Resultados/dispersion_semillas.md`. Los casos de mayor amplitud:

| Tabla | Variante · Algoritmo | Columna | Reparto |
|---|---|---|---|
| `metricas_firmas.csv` | 54 · RandomForest | `balanceo` | SMOTE en 5 · `class_weight` en 5 |
| `metricas_firmas.csv` | 122_sin_seleccion · RandomForest | `balanceo` | SMOTE en 6 · `class_weight` en 4 |
| `metricas_firmas.csv` | 122_sin_seleccion · DecisionTree | `balanceo` | SMOTE en 5 · `class_weight` en 5 |
| `metricas_firmas.csv` | 54 · DecisionTree | `balanceo` | SMOTE en 7 · `class_weight` en 3 |
| `metricas_baseline.csv` | 54 y 122 · RandomForest_monolitico | `config_ganadora` | `n_estimators: 300` en 5 · `n_estimators: 100` en 5 |
| `metricas_anomalias.csv` | 122_sin_seleccion · Autoencoder | `config_ganadora` | `(64, 32, 64)` en 6 · `(32, 16, 32)` en 4 |

Esto **no es un error**: es material de análisis para [[5.4 Conclusiones del capítulo]].

---

## A.3.7 Limitaciones declaradas

### Límite de reproducibilidad: rutas absolutas *hardcodeadas*

`Implementacion/app/program.py` y `Implementacion/app/validacion.py` contienen **rutas absolutas** al
árbol de trabajo de la máquina de desarrollo (`C:\Users\francisco.lopez\...`) para localizar el
dataset crudo y escribir los resultados. En consecuencia:

- **Reproducir el pipeline en otra máquina exige editar esas rutas** antes de ejecutar nada. No basta
  con clonar el repositorio, crear el entorno virtual e instalar `requirements.txt`.
- Los scripts de modelos (`anomalias.py`, `firmas.py`, `baseline.py`, `hibrido.py`,
  `cascada_invertida.py`) sí resuelven sus rutas a través de `config.py`; el problema está acotado a
  los dos ficheros citados.

> [!warning] Es deuda técnica declarada, no una decisión de diseño
> No hay ninguna razón metodológica que justifique las rutas absolutas: son una comodidad de
> desarrollo que quedó fijada. La corrección se descartó porque su ejecución obligaba a **regenerar
> los splits**, y los splits **no se regeneran** —toda la cadena de resultados publicados quedaría
> desanclada—. Se documenta aquí para que quien intente reproducir el trabajo sepa exactamente qué
> tiene que tocar, en lugar de descubrirlo con una excepción.

### Límite de protocolo: tres decisiones del sistema se tomaron con métricas medidas sobre D2

Los hiperparámetros, la estrategia de balanceo y los umbrales del sistema se ajustaron sin mirar D2
(tabla del callout de A.3.2). **Tres decisiones, en cambio, sí se apoyaron en métricas calculadas
sobre D2**, y se declaran aquí en lugar de omitirlas.

> [!note] Relación con el cuerpo de la memoria
> La **sede canónica** de esta limitación es [[6.1 Conclusiones]], donde se declara como limitación
> del trabajo. Lo que sigue es su **volcado tabulado** para consulta de ficha: la misma limitación,
> desglosada decisión a decisión con su criterio de selección y el registro donde consta. Si ambas
> versiones difirieran, manda la redacción de [[6.1 Conclusiones]].


| Decisión | Opción publicada | Criterio de selección | Registro de la decisión |
|---|---|---|---|
| 1 — detección de anomalías | Autoencoder-MLP | AUC-ROC / F1, métricas cuyo alcance declarado es «binario normal-vs-ataque sobre D2 completo» (A.3.4) | Decisión H-2 en `resumen-de-decisiones.md`; `hibrido.py:16` y `:755` documentan «Detector por defecto = Autoencoder (mejor en 5.1)» |
| 2 — clasificador de firmas | RandomForest | `f1_macro` **sobre D2** = 0,822 | Decisión H-3 en `resumen-de-decisiones.md` |
| 3 — set de características | **54** (frente a 122) | Recall 0-day por tipo + `f1_macro`, medidos con la cascada AE→RF **sobre D2** (experimento H1) | Decisión Q1/C y sección fechada 2026-07-15 de `resumen-de-decisiones.md`; [[4.3 Preprocesamiento de los datasets]] § Decisión experimental |

Las tres son selección de modelo sobre el conjunto de test, es decir *data snooping*, y por tanto las
métricas publicadas son optimistas respecto a lo que daría un test verdaderamente ciego. La tercera
es la más estructural, porque no elige un modelo dentro de un espacio de características dado, sino
que **define ese espacio** para todo el sistema publicado.

**Por qué se declara y no se disimula.** El razonamiento no depende de ninguna fuente externa y se
sostiene solo: si la métrica que decide qué modelo se publica se calcula sobre la misma población que
después se reporta como resultado, esa población ha dejado de ser un conjunto de test ciego y ha
actuado como conjunto de selección. El efecto práctico es que las cifras de la variante publicada
están **optimistamente sesgadas** en la parte que corresponde a haber escogido —entre ocho candidatos
de algoritmo (cuatro por etapa) y entre los dos sets de características— lo que mejor puntuaba en la
propia población de evaluación. En la literatura de
seguridad este patrón se cataloga como contaminación por selección sobre el test
[18].

> [!warning] Verificación pendiente — sin acceso al texto completo
> La referencia [18] se usa aquí **solo como
> etiqueta de la literatura**: el argumento del párrafo anterior no se apoya en ella y se mantiene
> íntegro si se retira. Queda pendiente comprobar contra el texto completo la denominación exacta del
> defecto y su numeración en la taxonomía; el proyecto no tiene acceso institucional a esa fuente y
> el criterio con el que se cerró fue precisamente que no sostuviera ninguna afirmación del trabajo.

> [!warning] Alcance exacto de este sesgo, para no exagerarlo ni minimizarlo
> - Afecta a **tres** decisiones: qué familia de algoritmo se publica en cada etapa y qué set de
>   características usa el sistema completo. No afecta a los hiperparámetros, a la estrategia de
>   balanceo, al umbral p95 ni a `UMBRAL_CONF`, que se ajustaron sobre `D1_val` y D3.
> - Las métricas de **todos** los candidatos, no solo las del ganador, están publicadas en
>   `Resultados/metricas_anomalias.csv` y `metricas_firmas.csv` y volcadas en el capítulo 5, y la
>   comparación 54 frente a 122 se tabula íntegra en [[4.3 Preprocesamiento de los datasets]]: el
>   lector puede ver el margen sobre el que se decidió.
> - **No se cuantifica cuánto sesgo introduce**: haría falta una partición de validación separada de
>   D2, que no existe en este diseño, y no se ha medido.
>
> Declararlo es más defendible que negarlo. Afirmar que «D2 no participa en ninguna decisión» sería
> **invertir** el defecto realmente cometido, y un lector que cotejase la ficha con
> `resumen-de-decisiones.md` lo detectaría de inmediato.

> [!todo] Qué faltaría para cerrarlo
> Repetir las tres selecciones —algoritmo de cada etapa y set de características— contra una
> partición de validación tallada desde `KDDTrain+` y
> reservar D2 exclusivamente para el reporte final. No se ha hecho: exigiría regenerar los splits, y
> los splits **no se regeneran** (misma razón que en el límite de rutas absolutas). Queda como línea
> futura.

### Otros límites del alcance evaluado

- **Un solo dataset.** Todas las cifras proceden de NSL-KDD. No hay evidencia de *replicabilidad*
  sobre otro conjunto (vocabulario de [20]).
- **El barrido de semillas no cubre el preprocesado** (véase A.3.6): la dispersión medida es de los
  modelos, no del sistema completo.
- **Sin evaluación adversaria.** No se ha medido el comportamiento frente a un atacante que conozca el
  modelo e intente evadirlo. El modelo de amenaza asumido tiene su marco conceptual en
  [[2.3.3 Límites y consideraciones éticas|2.3.3]] § *El modelo de amenaza como requisito
  metodológico (P10)*, su **especificación dimensión a dimensión** —y la razón, apoyada en las
  propiedades del NSL-KDD, de que no se realice un experimento adversario— en
  [[3.1 Requisitos del sistema]] § *3.1.5 Modelo de amenaza*, y la lectura de sus consecuencias
  sobre los resultados en el límite 3 de [[6.1 Conclusiones]].
- **Sin despliegue real.** Las columnas de rendimiento miden `predict`/`score` sobre características
  ya extraídas y en memoria: no incluyen captura de tráfico, ensamblado del flujo ni extracción de las
  41 características, que es donde vive el coste real de un despliegue.

---

## A.3.8 Checklist de reproducibilidad

Se rellenan los **11 ítems «FT»** del *Machine Learning Reproducibility Checklist* de
[20] — el subconjunto que aplica **a toda figura o tabla con resultados empíricos**,
de los **17** que componen el checklist completo. Los **seis restantes no se rellenan**. El detalle de
la fuente está en [[benchmark-comparativo-nsl-kdd]].

> [!todo] Qué son los seis ítems no rellenados: sin verificar
> La fuente del proyecto ([[benchmark-comparativo-nsl-kdd]]) respalda el **total de 17** y **enumera
> los 11 «FT»**, pero **no dice cuáles son los otros seis** ni de qué tratan. Cualquier
> caracterización de ese resto queda pendiente de comprobar contra el checklist original de
> [20]; hasta entonces este apéndice solo afirma que no se rellenan y por qué se
> eligió el subconjunto «FT»: es el que aplica **a toda figura o tabla con resultados empíricos**,
> que es exactamente lo que documenta esta ficha.

| # | Ítem FT | Estado | Dónde se cumple |
|---|---|---|---|
| 1 | *Data collection* | Cumplido | NSL-KDD, `KDDTrain+` / `KDDTest+`; origen y procedencia en [[4.2 Base de datos utilizada]] |
| 2 | *Link to data* | Cumplido | Repositorio público citado en `CLAUDE.md` y en [[4.2 Base de datos utilizada]] |
| 3 | *Pre-processing* | Cumplido | One-hot, escalado y selección descritos en [[4.3 Preprocesamiento de los datasets]]; diagrama en `Implementacion/PIPELINE.md` |
| 4 | *Sample allocation* | Cumplido | Particiones D1/D2/D3 con tamaños exactos en A.3.2 |
| 5 | *Hyper-parameters* | Cumplido | `config_ganadora` persistida en cada CSV y volcada en A.3.3 |
| 6 | *Number of runs* | Cumplido (T4) | 10 semillas (1-10) agregadas, más la 42 como titular independiente |
| 7 | *Description* | Cumplido **con la salvedad de protocolo de A.3.7** | Alcance por artefacto en A.3.4; protocolo en el capítulo 5. Tres decisiones —el detector de la etapa 1, el clasificador de la etapa 2 y el set de características (54 frente a 122)— se tomaron con métricas medidas sobre D2, y así se declara en A.3.7 |
| 8 | *Statistics* | Cumplido **por renuncia declarada** | Sin p-valor, con la razón explícita: 10 puntos sobre un único dataset no sostienen un contraste (A.3.6) |
| 9 | *Error bars* | Cumplido (T4) | Mín/máx y `sd` muestral (`ddof=1`) por celda en A.3.6 |
| 10 | *Central tendency* | Cumplido (T4) | Media de las 10 semillas por celda en A.3.6 |
| 11 | *Computing infrastructure* | Cumplido | A.3.5 |

> [!note] Alcance de los ítems 6, 9 y 10
> Los cierra el barrido de T4, y los cierra **con la restricción de A.3.6**: la dispersión es de los
> modelos sobre splits y set de características fijos. Un lector que espere barras de error del
> sistema completo —preprocesado incluido— no las encontrará aquí, y por eso se dice.

---

## A.3.9 Procedencia de los datos de este apéndice

| Bloque | Artefacto | Sello |
|---|---|---|
| Configuraciones y métricas de la semilla 42 | `Resultados/metricas_anomalias.csv` · `metricas_firmas.csv` · `metricas_hibrido.csv` · `metricas_baseline.csv` | `commit = 1163c90`, `2026-08-09` |
| Cascada invertida (T3) | `Resultados/metricas_cascada_invertida.csv` | `274923d-sucio`, `2026-08-10` (columnas `commit` y `fecha` del propio CSV; coincide con `commit_semilla_42` del agregado) |
| Tabla de dispersión (T4) | `Resultados/dispersion_semillas.md` / `.csv` y `comparaciones_pareadas.csv` | `commit_agregador = 0276039-sucio` (quinta pasada del agregador, 2026-08-17); filas agregadas de `df30cb2`. **Re-anclado en prosa a `98a0289`** |

> [!info] El sello del agregado es pre-commit: **re-anclaje HECHO** (2026-08-17)
> `commit_agregador = 0276039-sucio` es el valor **impreso en los artefactos en disco**, estampado por
> `config.commit_actual()` **antes** del commit que versiona los propios artefactos: por construcción, un
> fichero no puede llevar el hash del commit que lo incluye. La versión del código que produjo esa
> agregación es **`98a0289`** —«codigo: emitir el "8 de 10" pareado desde agregar_semillas.py y
> corregir el residuo de T22», del 2026-08-17, que arrastra a la vez `agregar_semillas.py` y los tres
> artefactos del agregador—, verificado con git y **no** estimado. `0276039` es el commit **anterior**
> al cambio y es de track *informe*, así que **no contiene el código** que produjo las cifras. El sello
> impreso **no se edita**: el re-anclaje va **en prosa**, aquí y en `Implementacion/PIPELINE.md` (tabla
> de corridas, tabla de las cinco pasadas y recuadro de re-anclajes), que es como el proyecto ha hecho
> los cinco anteriores — el de la cuarta pasada (`6bb224c-sucio` → **`1cb5c26`**, 2026-08-14) sigue
> siendo válido para lo que nombra, aunque su artefacto ya no sea el que hay en disco.

---

## Notas relacionadas

[[A.1 Columnas del dataset NSL-KDD]] · [[A.2 Métricas de desempeño]] ·
[[4.3 Preprocesamiento de los datasets]] · [[5.4 Conclusiones del capítulo]] ·
[[6.1 Conclusiones]]
