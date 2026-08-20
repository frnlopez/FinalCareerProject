---
titulo: "Apéndice A.3 — Ficha del sistema (model card)"
numero: "A.3"
estado: redactada
---

# A.3 Ficha del sistema

Este apéndice tiene **dos partes de naturaleza distinta**, y conviene separarlas desde el principio:

1. **Ficha del sistema (A.3.1–A.3.9).** Documenta el sistema evaluado siguiendo la plantilla de
   **model card** propuesta por [60]: detalles del modelo, uso previsto, particiones de datos,
   configuraciones seleccionadas, alcance exacto de cada métrica, infraestructura de cómputo,
   análisis cuantitativo con dispersión y limitaciones declaradas.
2. **Anexo teórico desplazado del capítulo 2 (A.3.10 y A.3.11).** Recoge el material que
   [[2.1.4 Algoritmos de ML]] y [[2.1.6 Metodologías y buenas prácticas]] no conservan en el cuerpo,
   por aplicárseles el criterio «lo que el sistema usa»: los algoritmos que el H-NIDS no emplea
   (A.3.10) y el desarrollo metodológico general de las prácticas que sí emplea (A.3.11).

> [!note] Naturaleza de este apéndice
> **Las secciones de volcado (A.3.1–A.3.9) no son una discusión.** Todas sus cifras se transcriben de
> los artefactos de `Resultados/` que se citan celda a celda; la interpretación corresponde al
> [[5.4 Conclusiones del capítulo|capítulo 5]] y a [[6.1 Conclusiones]]. **Ninguna cifra de esas
> secciones se calcula aquí.**
>
> **A.3.10 y A.3.11 son marco teórico**, no volcado: no transcriben ningún artefacto, no introducen
> ninguna cifra nueva y no alteran nada de lo declarado en A.3.1–A.3.9. La disciplina del párrafo
> anterior sigue aplicándose íntegra a las secciones de volcado.

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
> **Lo que sí miró D2.** *Tres decisiones del sistema se tomaron mirando D2: el detector de la etapa 1, el clasificador de la etapa 2 y el set de características (54 frente a 122). Las tres son selección de modelo sobre el conjunto de test, es decir* data snooping, *y por tanto las métricas publicadas son optimistas respecto a lo que daría un test verdaderamente ciego.* Su alcance y sus cifras se fijan en [[4.3 Preprocesamiento de los datasets|4.3.5]] § *Decisión experimental*, y el inventario completo, como limitación del trabajo, en [[6.1 Conclusiones|6.1]] (§6.1.3); **el detalle de cada una no se reproduce aquí**. El inventario **tabulado** de las tres, con criterio y registro de cada una, está en A.3.7 de esta misma ficha. No se presenta como protocolo limpio.
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
> **Las 98 celdas NO se transcriben aquí.** Están íntegras y en su forma citable en
> `Resultados/dispersion_semillas.csv` y `Resultados/dispersion_semillas.md`, **ambos versionados**,
> con las mismas columnas que tendría esta tabla —tabla de origen, variante, algoritmo, alcance,
> métrica, `n`, media, `sd`, mín, máx, valor de la semilla 42 y si cae en banda—. Copiarlas dentro
> multiplicaría páginas **sin añadir una sola columna** al artefacto, y crearía una segunda copia que
> puede desincronizarse de él. **Las 13 celdas que caen fuera de su banda, que son las que sostienen
> afirmaciones en el capítulo 5, se enumeran en [[5.2 Resultados del modelo de detección basado en
> firmas|5.2]] (§5.2.4.3).**

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
- **El reparto interno del bloque sí resiste el cambio de corrida** —trasladado aquí desde
  [[4.4 Entrenamiento del modelo de detección de anomalías|4.4]], que es donde se redactó—. Medido
  sobre el **residual** (el tramo que no es ajuste ni inferencia) expresado como fracción del
  `tiempo_s`, ese peso se mueve **como mucho 4,5 puntos porcentuales** en las ocho filas
  (detectores × variantes); el máximo lo marca `IsolationForest` 122, que pasa del **31,0 %** al
  **26,5 %**. El orden se conserva casi entero: ordenadas de mayor a menor residual, la única que
  cambia de sitio es esa misma fila, que **baja del 4.º al 6.º puesto** adelantada por las dos de
  `LocalOutlierFactor`; las otras siete mantienen su posición relativa. La explicación es mecánica:
  la carga de máquina reescala el bloque entero y se cancela al dividir, mientras que el peso de
  cada tramo lo fija el diseño del script —cuántas filas puntúa y cuántas veces—, que la semilla 42
  hace determinista. **Es la magnitud menos frágil de las que aquí se publican, no una constante del
  algoritmo**, y arrastra dos salvedades sin las cuales no debe citarse: **(1)** son **dos corridas
  comparadas, no una serie** —los Δ salen de contrastar `ac496cb` con `1163c90`, y nada garantiza
  que una tercera se mantuviera en esa banda—; y **(2)** una de las dos, `ac496cb`, **no es
  reproducible desde git** (véase la salvedad de abajo, que le aplica igual). La comparación
  completa, celda a celda y anclada al *commit* de cada corrida, está en
  `Implementacion\PIPELINE.md`.

> [!warning] Salvedad obligatoria: `ac496cb` no es reproducible desde git
> Los recuentos de épocas se apoyan en parte en la corrida `ac496cb`, cuyos CSV **nunca se
> commitearon** y fueron **sobrescritos por `1163c90`**: sobreviven solo citados en
> `Implementacion\PIPELINE.md`. **Un tercero no puede recalcular ese dato** desde el repositorio;
> vale como observación declarada, no como evidencia verificable.

En ningún caso son estos segundos una propiedad del algoritmo.

> **Las 100 filas NO se transcriben aquí**, por la misma razón y con más motivo: el propio título
> de este bloque declara que **no es calidad y no se cita como resultado**. Están en
> `Resultados/dispersion_semillas.csv` y `Resultados/dispersion_semillas.md`, versionados. Lo que
> sostiene afirmaciones vivas es la **prosa** de este apartado —la dispersión sin causa atribuida, el
> recuento de épocas, el reparto interno del bloque y la salvedad de `ac496cb`—, y **se conserva
> íntegra**.

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
| 3 — set de características | **54** (frente a 122) | Recall 0-day por tipo + `f1_macro`, medidos con la cascada AE→RF **sobre D2** (experimento H1) | Decisión Q1/C y sección fechada 2026-07-15 de `resumen-de-decisiones.md`; [[4.3 Preprocesamiento de los datasets|4.3.5]] § Decisión experimental |

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
>   comparación del experimento H1 (54 frente a 122, cascada AE→RF) se tabula en
>   [[4.3 Preprocesamiento de los datasets|4.3.5]]: el
>   lector puede ver el margen sobre el que se decidió.
> - **No se cuantifica cuánto sesgo introduce**: haría falta una partición de validación separada de
>   D2, que no existe en este diseño, y no se ha medido.
>
> Declararlo es más defendible que negarlo. Afirmar que «D2 no participa en ninguna decisión» sería
> **invertir** el defecto realmente cometido, y un lector que cotejase la ficha con
> `resumen-de-decisiones.md` lo detectaría de inmediato.

> [!warning] Límite declarado de alcance: la corrección no se ejecuta en este trabajo
> **Qué corregiría el defecto.** Repetir las tres selecciones —algoritmo de cada etapa y set de
> características— contra una partición de validación tallada desde `KDDTrain+`, reservando D2
> exclusivamente para el reporte final.
>
> **Por qué no se hace, y no es un olvido.** Es una **decisión de alcance tomada
> explícitamente**, no una tarea pendiente del proyecto:
> - Exigiría **regenerar los splits** D1/D2/D3, y los splits **no se regeneran** en este trabajo
>   (misma razón que en el límite de rutas absolutas): toda cifra publicada en el capítulo 5 está
>   anclada a los splits actuales, de modo que retallarlos invalidaría el conjunto completo de
>   resultados ya medidos y sellados en A.3.9.
> - La consecuencia se **declara** en lugar de repararse: las métricas de la variante publicada son
>   optimistas en la parte atribuible a la selección, tal como se explica arriba, y el margen sobre
>   el que se decidió queda a la vista del lector en los CSV de todos los candidatos.
>
> **Dónde vive como continuación.** Se recoge como línea futura en [[6.2 Líneas futuras]]; su lectura
> como limitación del trabajo está en [[6.1 Conclusiones]], que es su sede canónica.

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

> [!todo] Qué son los seis ítems no rellenados: dato pendiente, sin efecto sobre lo afirmado
> La fuente del proyecto ([[benchmark-comparativo-nsl-kdd]]) respalda el **total de 17** y **enumera
> los 11 «FT»**, pero **no dice cuáles son los otros seis** ni de qué tratan. Cualquier
> caracterización de ese resto queda pendiente de comprobar contra el checklist original de
> [20], y **no se rellena por conjetura**.
>
> **Qué sí queda establecido sin ese dato**, de forma que el apéndice se sostiene igual:
> - Los 11 ítems «FT» están enumerados y resueltos uno a uno en la tabla siguiente, con su sede.
> - El criterio de elección del subconjunto es explícito: «FT» es el que aplica **a toda figura o
>   tabla con resultados empíricos**, que es exactamente lo que documenta esta ficha.
> - Las restricciones de los ítems 6, 9 y 10 se declaran en el callout posterior.
>
> Es decir, **lo único no resuelto es la identidad de los seis restantes**, y ninguna afirmación de
> este apéndice depende de ella.

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

## A.3.10 Algoritmos del marco teórico que el sistema no emplea

Material trasladado desde [[2.1.4 Algoritmos de ML]], cuyo criterio de inclusión en el cuerpo es
«lo que el sistema usa». Las dos familias siguientes **no intervienen en ninguna etapa del H-NIDS**
y se conservan aquí por completitud del panorama algorítmico; el cuerpo las menciona en una frase y
remite a este apartado.

### A.3.10.1 Regresión logística (excedente de [[2.1.4 Algoritmos de ML|2.1.4.1]])

La regresión logística toma un vector de características numéricas y estima la probabilidad de que un ejemplo pertenezca a una clase, modelando el logaritmo de la razón de probabilidades (*log-odds*): para un evento que ocurre con probabilidad $p$, la razón de probabilidades es $p/(1-p)$, y el modelo ajusta una combinación lineal de las características a $\log(p/(1-p))$ [5, cap. 4].

Es uno de los algoritmos supervisados más utilizados en la práctica por varias propiedades: se entrena de forma eficiente incluso a gran escala, se adapta bien a un número elevado de características, admite una descripción concisa —la clasificación se reduce a un producto escalar— y es **explicable**, ya que puede calcularse la contribución de cada característica a la puntuación final [5, cap. 4].

Su uso está condicionado por tres supuestos que conviene tener presentes:

- **Linealidad.** Asume que las características se relacionan linealmente con el logaritmo de la razón de probabilidades; si esta relación no se sostiene, el modelo pierde capacidad predictiva.
- **Baja multicolinealidad.** Las características de entrada deben ser razonablemente independientes entre sí; la redundancia entre variables distorsiona la estimación de los coeficientes.
- **Tamaño muestral.** La estimación por máxima verosimilitud que emplea la regresión logística es menos eficiente estadísticamente que los mínimos cuadrados de la regresión lineal, por lo que suele requerir más ejemplos de entrenamiento para alcanzar una potencia comparable [5, cap. 4].

### A.3.10.2 Agrupamiento: k-means y jerárquico (excedente de 2.1.4.4)

Los algoritmos de agrupamiento (*clustering*) buscan agrupar puntos de datos que resultan «cercanos» entre sí según alguna métrica, sin usar ninguna etiqueta durante el entrenamiento. Aunque este trabajo no emplea agrupamiento en su arquitectura final, se incluyen aquí por completitud del panorama de algoritmos de ML y porque delimitan, por contraste, el régimen semisupervisado (one-class) de 2.1.4.2: mientras que el agrupamiento no usa ninguna etiqueta, los detectores de anomalías de este sistema sí usan la etiqueta «normal» para decidir con qué datos entrenar.

**k-means.** Es habitualmente el primer algoritmo de agrupamiento que se considera. Se aplica a vectores de valores reales cuando se conoce de antemano el número de grupos deseado, denotado $k$. El algoritmo asigna cada punto a un grupo de forma que se minimice la suma de las distancias euclidianas de cada punto al centroide de su grupo, iterando entre la asignación de puntos a centroides y la recalculación de estos hasta la convergencia [12, cap. 14].

**Agrupamiento jerárquico.** A diferencia de k-means, no requiere fijar de antemano el número de grupos $k$ [12, cap. 14]:

- **Aglomerativo (ascendente).** Parte de tantos grupos como puntos de datos y, en cada paso, fusiona los dos grupos más similares —según una métrica de distancia, como la euclidiana o la de Mahalanobis— hasta que queda un único grupo. El resultado se representa como un dendrograma, cuyas capas pueden recorrerse para elegir el nivel de agrupamiento más adecuado.
- **Divisivo (descendente).** Recorre el proceso en sentido inverso: parte de un único grupo que contiene todos los puntos y lo va dividiendo sucesivamente según la métrica de distancia, hasta que cada punto queda en su propio grupo.

> [!note] Métrica asociada
> El coeficiente de silueta, métrica interna con la que se evalúa una partición en grupos, se
> desarrolla en [[A.2 Métricas de desempeño]] § A.2.2.2, por el mismo criterio: se define, pero no
> se reporta.

---

## A.3.11 Desarrollo metodológico ampliado

Material trasladado desde [[2.1.6 Metodologías y buenas prácticas]], que conserva en el cuerpo
**solo las prácticas que el sistema implementado emplea**. Lo que sigue es el desarrollo general de
cada una: no introduce ninguna cifra nueva y no altera nada de lo declarado en A.3.1–A.3.9.

### A.3.10.3 Redes neuronales artificiales (excedente de [[2.1.4 Algoritmos de ML|2.1.4.3]])

> Trasladado desde el cuerpo el 2026-08-20 al comprimir `2.1.4.3`. **Nada se ha reescrito:** es el
> texto que estaba en la memoria, movido íntegro por la restricción T7. El cuerpo conserva el
> resumen y la remisión a este apartado. Aquí se desarrolla porque el sistema **sí** contiene un
> componente neuronal —el autoencoder de la etapa 1— y un tribunal puede pedir su fundamento.


#### A.3.10.3.1 La neurona artificial y el perceptrón

La unidad básica de una red neuronal artificial es la **neurona artificial**, un modelo matemático simplificado de la neurona biológica: recibe un vector de entradas $x_1, \ldots, x_n$, calcula una combinación lineal ponderada de ellas más un término de sesgo (*bias*), y aplica a ese resultado una **función de activación** no lineal para producir su salida [6, cap. 6].

El **perceptrón**, propuesto por Rosenblatt, es la formulación más simple de esta idea: una sola neurona con una función de activación de umbral, capaz de separar linealmente dos clases. Su limitación clásica —no poder resolver problemas no separables linealmente, como la función XOR— es precisamente lo que motiva apilar varias neuronas en capas [6, cap. 6].

#### A.3.10.3.2 El perceptrón multicapa (MLP)

Un **perceptrón multicapa** (*Multi-Layer Perceptron*, MLP) organiza las neuronas artificiales en **capas** sucesivas: una capa de entrada, una o varias capas ocultas y una capa de salida, en las que cada neurona de una capa recibe como entrada las salidas de todas las neuronas de la capa anterior (red densamente conectada o *fully connected*) [6, cap. 6]. Al introducir capas ocultas con funciones de activación no lineales, el MLP deja de estar limitado a fronteras de decisión lineales: puede aproximar funciones arbitrariamente complejas dado un número suficiente de neuronas, resultado conocido como teorema de aproximación universal [6, cap. 6].

Entre las funciones de activación más habituales en las capas ocultas se encuentran:

- **Sigmoide**, que comprime la salida al intervalo $(0,1)$ y fue históricamente la más usada, aunque hoy se emplea menos en capas intermedias por su tendencia a saturar y atenuar el gradiente.
- **Tangente hiperbólica (tanh)**, similar a la sigmoide pero centrada en cero, con salida en $(-1,1)$.
- **ReLU** (*Rectified Linear Unit*), que devuelve la entrada si es positiva y cero en caso contrario; es hoy la opción por defecto en la mayoría de arquitecturas por su sencillez de cálculo y porque mitiga —aunque no elimina— el problema de desvanecimiento del gradiente [6, cap. 6].

#### A.3.10.3.3 Entrenamiento: retropropagación y descenso de gradiente

Entrenar una red neuronal consiste en ajustar los pesos de todas sus conexiones para minimizar una función de pérdida que mide el error entre la salida de la red y el valor esperado. El procedimiento estándar combina dos mecanismos [6, cap. 6]:

1. **Descenso de gradiente.** Los pesos se actualizan iterativamente en la dirección opuesta al gradiente de la función de pérdida respecto a cada peso, con un tamaño de paso —la tasa de aprendizaje— que controla cuánto se desplaza el peso en cada iteración. En la práctica se emplean variantes estocásticas que estiman el gradiente sobre lotes (*mini-batches*) de ejemplos en lugar de sobre el conjunto de entrenamiento completo, lo que acelera el cálculo y añade una forma de regularización implícita.
2. **Retropropagación (*backpropagation*).** Es el algoritmo que calcula de forma eficiente el gradiente de la pérdida respecto a **todos** los pesos de la red, capa por capa, aplicando la regla de la cadena del cálculo diferencial desde la capa de salida hacia la capa de entrada. Sin retropropagación, calcular el gradiente de una red con varias capas ocultas tendría un coste computacional impracticable [6, cap. 6].

#### A.3.10.3.4 Qué distingue a las redes neuronales del ML clásico

Frente a los algoritmos descritos en 2.1.4.1 y 2.1.4.2 —que operan sobre las características tal como se les entregan, eventualmente tras una selección o transformación manual—, una red neuronal con capas ocultas suficientes puede **aprender su propia representación intermedia** de los datos como parte del mismo proceso de optimización que aprende la tarea final. Esta capacidad es también lo que separa, por grado, al aprendizaje profundo del resto del aprendizaje automático: cuantas más capas ocultas y más profunda la jerarquía de representaciones aprendidas, más nos acercamos a ese régimen. Dónde se traza esa frontera, y por qué el único componente neuronal de este sistema —un `MLPRegressor` de scikit-learn usado como autoencoder para el error de reconstrucción— queda deliberadamente **fuera** de ella, se discute con detalle en [[2.3.1 IA, ML y Deep Learning]], en el bloque «El único componente neuronal, y por qué no es "profundo"».

### A.3.11.1 CRISP-DM: fases, carácter iterativo y mapeo completo

Un proyecto de aprendizaje automático no es una sucesión lineal de tareas, sino un ciclo. El marco de referencia más extendido para ordenarlo es **CRISP-DM** (*Cross-Industry Standard Process for Data Mining*), que descompone un proyecto de minería de datos en seis fases [11]:

| Fase | Pregunta que responde |
|---|---|
| **Comprensión del problema** | ¿Qué se quiere conseguir y cómo se sabrá si se ha conseguido? |
| **Comprensión de los datos** | ¿Qué hay en los datos, de dónde vienen y qué defectos tienen? |
| **Preparación de los datos** | ¿Cómo se transforman en una matriz apta para el modelado? |
| **Modelado** | ¿Qué algoritmos se prueban y con qué configuración? |
| **Evaluación** | ¿El modelo resuelve el problema del que se partió, no solo la métrica? |
| **Despliegue** | ¿Cómo se pone en producción y cómo se mantiene? |

Su rasgo definitorio es el **carácter iterativo**: las flechas no van solo hacia adelante. Descubrir en la fase de modelado que una variable está mal codificada devuelve el proyecto a la preparación de datos, y una evaluación que no responde a la pregunta original devuelve a la comprensión del problema. CRISP-DM se adopta aquí como **marco de ordenación del trabajo y del relato, no como corsé**: sirve para explicar por qué las cosas se hicieron en un orden y no en otro, no para imponer una secuencia rígida que el desarrollo real nunca sigue.

El mapeo de las fases al trabajo realizado es directo:

| Fase CRISP-DM | Materialización en este TFG |
|---|---|
| Comprensión del problema | Objetivos y pregunta de investigación ([[1.3 Objetivo]], [[3.1 Requisitos del sistema]]) |
| Comprensión de los datos | EDA sobre NSL-KDD (`program.py`) y validación de los splits (`validacion.py`): integridad, distribuciones, deriva y valores atípicos |
| Preparación de los datos | Codificación, escalado, selección de características y generación de los splits D1/D2/D3 ([[4.3 Preprocesamiento de los datasets]]) |
| Modelado | Las dos etapas del sistema por separado: anomalías ([[4.4 Entrenamiento del modelo de detección de anomalías]]) y firmas ([[4.5 Entrenamiento del modelo de detección basado en firmas]]) |
| Evaluación | Evaluación única de extremo a extremo sobre D2 y contraste con el baseline monolítico (capítulo [[5.3 Resultados del sistema híbrido]]) |
| Despliegue | **Fuera del alcance del trabajo**, y así se declara en [[6.1 Conclusiones]]: el sistema es un prototipo de investigación, no un producto operativo |

> [!note] Una fase que no se ejecuta también se declara
> Dejar el despliegue fuera del alcance es una decisión legítima en un TFG, pero decirlo importa: buena parte de las críticas al aprendizaje automático aplicado a la seguridad se dirigen precisamente contra trabajos que presentan resultados de laboratorio como si fueran capacidades operativas. Este punto se retoma en 2.1.6.8 y en el inventario de límites de A.3.7.

### A.3.11.2 Fundamento de la partición y desarrollo de la línea roja del test

La partición de los datos es la práctica de la que dependen todas las demás. Su fundamento es sencillo: **medir el error sobre los mismos datos con los que se ajustó el modelo estima capacidad de memorización, no de generalización**. Un modelo suficientemente flexible puede reproducir su conjunto de entrenamiento casi a la perfección sin haber aprendido nada transferible a datos nuevos. La única estimación honesta del error de generalización se obtiene sobre datos que el modelo no ha visto [12, cap. 7].

En cuanto una decisión —por pequeña que sea— se toma mirando el resultado sobre el test, ese conjunto deja de ser una muestra no vista y su métrica pasa a estar sesgada de forma optimista, porque el experimentador ha actuado como un canal de información desde el test hacia el modelo. El sesgo no se elimina reconociéndolo después: solo se evita no cometiéndolo. Reconocerlo, en cambio, sí cambia lo que puede afirmarse de la cifra resultante, y por eso una desviación de esta regla se declara siempre.

> [!note] La tabla de la teoría; el sistema se desvió de ella en tres decisiones
> En la tabla de 2.1.6.2, la fila **Validación** incluye el «algoritmo ganador» entre lo que corresponde decidir en validación —y lo mismo vale para la elección del espacio de características—. Esa es la práctica correcta y se mantiene enunciada así porque es la que el marco teórico debe fijar. Lo que este trabajo añade es la constatación de que **su implementación no la respetó en las tres decisiones declaradas**: la comparación entre algoritmos de cada etapa y la comparación entre los sets de 54 y 122 características se resolvieron sobre el conjunto de test. El inventario tabulado de esas tres decisiones **no se repite aquí**: está en A.3.7 § *Límite de protocolo*. La corrección —repetir las tres comparaciones sobre un conjunto de decisión independiente de D2 y volver a medir— queda recogida como línea futura en [[6.2 Líneas futuras]].

Sobre la duplicidad del inventario de las tres decisiones: el mismo inventario reaparece en [[6.1 Conclusiones]], y la duplicidad es deliberada porque cada sede responde a una pregunta distinta. **En 2.1.6.2 el inventario funciona como encuadre metodológico**: sirve de ejemplo concreto de qué es el *data snooping*, en qué momento del ciclo de trabajo se cuela y por qué el perímetro de protocolo no basta para impedirlo. **En [[6.1 Conclusiones]] el mismo inventario se trata como limitación del trabajo**: allí se valora cuánto compromete la validez de las cifras publicadas en el capítulo 5 y qué haría falta para levantarlo.

| Objeto | Sede canónica | Qué se decide allí |
|---|---|---|
| **Inventario de las tres decisiones** tomadas con métricas de D2, tratado como limitación del trabajo | [[6.1 Conclusiones]] | El recuento de decisiones y la redacción con la que se enuncian como limitación |
| **Desviación relativa al set de características (54 frente a 122)**, la tercera de las tres | [[4.3 Preprocesamiento de los datasets\|4.3.5]] § «Decisión experimental: 54 frente a 122 (experimento H1, medido sobre D2)» | El alcance y las cifras de esa desviación concreta, por proximidad al experimento H1 que las genera |
| **Volcado tabulado decisión a decisión**, con criterio y registro de cada una | A.3.7 § *Límite de protocolo* | La consulta de ficha |

Se declara en el cuerpo, y no en una nota al pie, por una razón de fondo: **negar un fallo de protocolo es peor que cometerlo**. Una versión anterior de esa sección afirmaba que «ninguna decisión del sistema se toma mirando D2», lo que convertía un defecto acotado y auditable en una afirmación falsa sobre el propio método; una segunda versión lo redujo a una única intervención, lo que tampoco era cierto. La magnitud del sesgo no se puede cuantificar con los datos disponibles —haría falta un conjunto de decisión independiente de D2—, de modo que no se estima.

### A.3.11.3 Motivación general de la validación cruzada

Un único corte train/validación tiene dos inconvenientes: la estimación depende de qué muestras cayeron a cada lado —con conjuntos pequeños, la varianza es considerable— y desperdicia datos, porque la parte reservada a validar no entrena. La **validación cruzada de K particiones** (*K-fold*) resuelve ambos: los datos se dividen en K bloques, se entrena K veces dejando cada vez un bloque fuera para validar, y la estimación final es el promedio de las K medidas. Toda muestra actúa una vez como validación y K−1 veces como entrenamiento [13].

Sobre la **estratificación** —exigir que cada partición conserve la proporción de clases del conjunto completo— este apéndice **no repite la justificación**: con clases equilibradas es una mejora marginal y con clases muy minoritarias es imprescindible, por un razonamiento combinatorio que se desarrolla en su sede única, [[2.1.6 Metodologías y buenas prácticas]] § 2.1.6.3, donde además se conecta con el caso medido de `u2r` en D3.

### A.3.11.4 Coste de `GridSearchCV` y alternativas

`GridSearchCV` recorre de forma exhaustiva una rejilla de combinaciones de hiperparámetros y evalúa cada una por validación cruzada [14]. Su coste crece como el producto de los tamaños de cada eje multiplicado por el número de particiones, lo que en la práctica obliga a decidir cuánto presupuesto se le dedica. Existen alternativas más eficientes cuando ese presupuesto es el factor limitante, como la búsqueda aleatoria [15].

### A.3.11.5 Checklist de reproducibilidad: fundamento de los cuatro ítems de dispersión

Un experimento que no puede repetirse no es una evidencia: es una anécdota. En aprendizaje automático la reproducibilidad no se da por supuesta, porque casi todo el proceso incorpora aleatoriedad —el reparto en particiones, la inicialización de los modelos, el muestreo interno, la generación de puntos sintéticos— y porque el resultado depende además de las versiones exactas de las bibliotecas empleadas. La comunidad ha respondido con listas de comprobación que enumeran qué debe declararse para que un resultado sea verificable [20].

Declarar una única corrida como si fuera el resultado, sin ninguna medida de dispersión, es precisamente lo que esas listas piden evitar, y su vocabulario nombra los cuatro elementos que hay que declarar. **La tabla de cumplimiento no se repite aquí**: los once ítems «FT», con su estado y su sede, están en A.3.8. Lo que sigue es el fundamento de los cuatro que atañen a la dispersión, que el cuerpo de 2.1.6.7 resume en un párrafo:

| Ítem | Qué exige | Cómo se cumple en este trabajo |
|---|---|---|
| ***Number of runs*** | Cuántas ejecuciones sostienen la cifra | **10 corridas**, con semillas 1 a 10 |
| ***Central tendency*** | Qué resumen se publica | **Media** de las diez corridas |
| ***Error bars*** | Qué dispersión acompaña al resumen | **Desviación típica muestral** (`ddof=1`) y banda **[mínimo, máximo]** |
| ***Statistics*** | Qué contraste estadístico se aplica, o por qué no se aplica | **Ninguno, y la renuncia se declara con su razón**: diez puntos sobre un único conjunto de datos no sostienen un contraste de hipótesis |

> [!note] Declarar la renuncia forma parte del cumplimiento
> El ítem de estadística de la lista de comprobación no obliga a aplicar un contraste; obliga a **decir qué se hizo**. Renunciar razonadamente a un p-valor que no sostendrían los datos lo cumple; guardar silencio sobre el punto, no.

Las **tres palancas** con las que este trabajo instrumenta la reproducibilidad —semilla fija, entorno congelado y artefactos persistidos, con su materialización concreta en el proyecto— **no se repiten aquí**: están tabuladas en [[2.1.6 Metodologías y buenas prácticas]] § 2.1.6.7.

### A.3.11.6 Desarrollo de la deriva y las clases nunca vistas

Sobre la deriva: aunque el conjunto de test contuviera solo tipos de ataque conocidos, sus características no se distribuyen igual que las del entrenamiento. Sobre las clases nunca vistas: ninguna partición de validación construida sobre el entrenamiento puede contener un solo ejemplo de ellos, luego ninguna validación cruzada puede anticipar cómo se comportará el modelo ante ellos. El fenómeno tiene una formulación clásica en el ámbito de la detección de intrusiones, donde se argumenta que la enorme variabilidad del tráfico real y el coste asimétrico de los errores explican la distancia sistemática entre los resultados de laboratorio y el rendimiento operativo [21].

---

## Notas relacionadas

[[A.1 Columnas del dataset NSL-KDD]] · [[A.2 Métricas de desempeño]] ·
[[2.1.4 Algoritmos de ML]] · [[2.1.6 Metodologías y buenas prácticas]] ·
[[4.3 Preprocesamiento de los datasets]] · [[5.4 Conclusiones del capítulo]] ·
[[6.1 Conclusiones]]
