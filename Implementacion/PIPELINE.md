# Pipeline de Implementación — H-NIDS NSL-KDD

> Los diagramas Mermaid viven como ficheros sueltos en [`diagramas/`](diagramas/) (fuente `.mmd` + PNG/SVG renderizados).
> Ver [`diagramas/README.md`](diagramas/README.md) para cómo editarlos/exportarlos.

## Diagrama completo del pipeline

![Pipeline completo](diagramas/01_pipeline_completo.svg)

> Fuente editable: [`diagramas/01_pipeline_completo.mmd`](diagramas/01_pipeline_completo.mmd)

---

## Mapeo de ataques (39 tipos de ataque → 5 categorías)

![Mapeo de ataques a 5 categorías](diagramas/02_mapeo_ataques.svg)

> Fuente editable: [`diagramas/02_mapeo_ataques.mmd`](diagramas/02_mapeo_ataques.mmd)

---

## Estructura de archivos generados

```
Resultados/
└── specialized_nsl_kdd_
    ├── original_D1_normal_for_anomaly.csv
    ├── original_D2_complete_test.csv
    ├── original_D3_known_attacks_for_signatures.csv
    │
    ├── processed_X_D1_normal_for_anomaly.csv          ← features D1 (escaladas)
    ├── processed_y_attack_D1_normal_for_anomaly.csv
    ├── processed_y_category_D1_normal_for_anomaly.csv
    │
    ├── processed_X_D2_complete_test.csv               ← features D2 (escaladas)
    ├── processed_y_attack_D2_complete_test.csv
    ├── processed_y_category_D2_complete_test.csv
    │
    ├── processed_X_D3_known_attacks_for_signatures.csv ← features D3 (escaladas)
    ├── processed_y_attack_D3_known_attacks_for_signatures.csv
    ├── processed_y_category_D3_known_attacks_for_signatures.csv
    │
    ├── mappings_and_info.txt                           ← mapeos LabelEncoder + scaler
    ├── usage_guide.txt                                 ← guía de uso con ejemplos
    └── validation_report.txt                          ← generado por validacion.py
```

---

## Runbook de reconstrucción de las tablas de métricas (esquema T1)

El esquema de las tablas de métricas cambió con la tarea **T1** (columnas `alcance`,
`alcance_tiempo_s`, `semilla`, `commit`, `bin_accuracy`, tiempos separados de
entrenamiento/inferencia). Un CSV
con el esquema anterior **no se mezcla**: `evaluacion.limpiar_variante_csv()` lo aparta como
`<nombre>.esquema-anterior.bak` y lo regenera. Para volver a tener las tablas completas hacen
falta **estas ocho invocaciones**, desde `Implementacion/app/` y con el venv `Imp` activado.

`hibrido.py` va **al final de cada variante**: consume los `.joblib` que dejan `anomalias.py` y
`firmas.py`, y aborta si no encuentra los de su variante.

```powershell
# --- Variante de 54 características (selección 4.3.5 aplicada, por defecto) ---
python anomalias.py
python firmas.py
python baseline.py
python hibrido.py

# --- Variante de 122 características (sin selección) ---
python anomalias.py --sin-seleccion
python firmas.py    --sin-seleccion
python baseline.py  --sin-seleccion
python hibrido.py   --sin-seleccion
```

**Ninguna métrica de calidad cambia** respecto a lo publicado: la semilla es 42 en todo, los
modelos, los grids y la calibración OOF están intactos, y T1 solo añade columnas de
declaración. **Las columnas de tiempo sí cambian**, y era el objetivo: `tiempo_s`,
`tiempo_entrenamiento_s`, `tiempo_inferencia_s`, `latencia_ms_por_flujo` y
`flujos_por_segundo` se miden ahora con `perf_counter` (otra resolución) y arrastran además la
varianza de máquina descrita más abajo. Cambia también el valor de `alcance` en las 16 filas de
`metricas_balanceo.csv`. Y `metricas_anomalias.csv` estrena **cuatro** columnas —las dos medidas
`tiempo_score_seleccion_s` y `tiempo_score_umbral_s`, más `n_iter_ganador` y
`n_iter_total_grid` (épocas del ajuste; **solo las rellena el autoencoder**, celdas vacías en los
otros tres detectores)—, así que el CSV
anterior tiene otro
esquema: al re-ejecutar, `limpiar_variante_csv()` lo apartará como
`metricas_anomalias.csv.esquema-anterior.bak` y hay que correr **las dos variantes** (54 y 122)
para regenerarlo completo.

Con **T18** cambia además el **contenido** de la columna `alcance_tiempo_s` de las cuatro tablas
principales: sale de ella toda la interpretación (porcentajes, factores, cifras de corridas
anteriores) y se queda solo lo estable. Los números viven ahora en la sección
[Las columnas de tiempo](#las-columnas-de-tiempo-qué-miden-y-hasta-dónde-valen) de este mismo
documento, anclados al commit de su corrida. **Ninguna métrica de calidad se ve afectada.**

> [!warning] Hueco de trazabilidad de la corrida publicada
> El runbook son **8 invocaciones**: `program.py` y `validacion.py` **NO se re-corrieron**, así que
> sus **5** figuras (`eda_distribuciones_divisiones.png` y las cuatro `validacion_*.png`) siguen
> ancladas a la corrida del **05/07/2026** y no a `ac496cb`. Los splits que consumen las 8
> invocaciones son los CSV procesados que dejó aquella corrida, idénticos (semilla 42); lo que no
> está anclado al commit publicado son esas cinco figuras.

> [!note] El texto de `alcance_tiempo_s` publicado es el de `ac496cb`, no el de `config.py` de hoy
> Los arreglos de redacción de `config.ALCANCE_TIEMPO_S_BLOQUE_ANOMALIAS` y
> `..._BLOQUE_FIRMAS` que exigió la auditoría de T18 (sacar de ellos las dos afirmaciones
> empíricas) son **posteriores** a la corrida publicada. La columna `commit` de cada fila declara
> con qué código se produjo —`ac496cb`—, así que el dato es autoconsistente; el texto corregido
> aparecerá en el CSV la próxima vez que se corra el runbook. **No se re-corre por esto**: cambia
> la redacción de una celda declarativa, ninguna medida.

### Recuento esperado (comprobado por código, no a ojo)

| Tabla | Filas por variante | Total con las dos variantes |
|---|---|---|
| `metricas_anomalias.csv` | 4 (un detector por fila) | **8** |
| `metricas_firmas.csv` | 4 (un clasificador por fila) | **8** |
| `metricas_baseline.csv` | 1 (RF monolítico) | **2** |
| `metricas_hibrido.csv` | 1 (la cascada) | **2** |

Lo verifica `evaluacion.comprobar_recuento()` al final de cada corrida (contra
`evaluacion.FILAS_ESPERADAS_POR_VARIANTE`): si la variante que se acaba de correr no tiene
exactamente esas filas, **aborta**. Junto a ella, `evaluacion.comprobar_unicidad()` verifica la
clave `set_features × algoritmo × alcance`. Las cuatro tablas auxiliares
(`metricas_balanceo.csv`, `metricas_baseline_0day.csv`, `metricas_hibrido_0day.csv`,
`metricas_hibrido_calibracion.csv`) tienen otra granularidad de fila y no llevan recuento fijo,
pero sí `alcance` y procedencia (`evaluacion.COLUMNAS_MINIMAS_AUXILIARES`).

> Al terminar las ocho, si quedan ficheros `*.esquema-anterior.bak` en `Resultados/`, es que
> había tablas del esquema viejo: comprobar que la nueva trae todas las filas y borrarlos a mano.
> Un `.bak` no se versiona ni se cita.

### Las columnas de tiempo: qué miden y hasta dónde valen

> [!important] Dónde vive cada cosa (regla de **T18**)
> El **dato publicado** —los cuatro textos `config.ALCANCE_TIEMPO_S_*` que viajan en la columna
> `alcance_tiempo_s`— lleva **solo lo estable**: qué tramos entran en `tiempo_s`, cuáles quedan
> fuera, qué columna mide cada uno y el aviso de **P9** sobre la latencia. **Ningún porcentaje,
> ninguna banda, ningún factor de dispersión, ninguna cifra de ninguna corrida y ninguna
> afirmación empírica**, ni siquiera cualitativa («no escala con el modelo», «las desviaciones
> caben dentro de X»): eso también es un dato de corrida y también se falsa.
>
> **Todos los números interpretativos están en esta sección**, y cada uno anclado al **commit**
> de la corrida de la que sale. Motivo: publicar interpretación dentro del dato crea un bucle —el
> dato no se puede editar sin re-correr y cada corrida nueva falsa la cifra que dejó la anterior—.
> Le pasó tres veces seguidas a la redacción de `config.ALCANCE_TIEMPO_S_*`: las cotas «27-49 %» y
> «varía hasta 4×» nacieron falsables y se falsaron, y la celda llegó a ≈3,2 kB **por fila** en un
> CSV de 9 líneas. Aquí, en cambio, se corrigen sin tocar una tabla.

#### Cómo se nombra una corrida (y por qué no se cita ningún `.bak`)

Una **corrida** se identifica por el **commit del código** que la produjo, que es lo que su
columna `commit` declara. El commit del árbol donde sus CSV quedaron **versionados** es otro, y
casi siempre posterior. Las corridas que existen en git:

| Corrida (columna `commit`) | CSV versionados en | Notas |
|---|---|---|
| *(sin columna `commit`)* | `8b07319` | Anterior a T1: solo tiene `tiempo_s`, sin tiempos separados ni latencia. |
| `c7cf319` | `077119e` (y `38fdd4b`, idénticos) | Primera con `tiempo_entrenamiento_s` / `tiempo_inferencia_s`. Aún con `time.time()`. |
| `38fdd4b` | `34bee30` (y `5516b60`, idénticos) | Primera con `perf_counter`. |
| `5516b60` | `5f98d88` | Añade `tiempo_score_seleccion_s` y `tiempo_score_umbral_s`. |
| `ac496cb` | *(aún en el árbol de trabajo, pendiente del commit de cierre de T18)* | **La publicada hoy.** Añade `n_iter_ganador` y `n_iter_total_grid`. 8 invocaciones, 222 filas, todas con `semilla = 42` y `commit = ac496cb` limpio. |

Cualquier cita a una corrida anterior apunta a **su commit**, nunca a un fichero
`*.esquema-anterior.bak`: los `.bak` son prescindibles —lo que contienen está en git— y no se
versionan.

#### Por qué `perf_counter` y no `time.time()`

En Windows `time.time()` tiene una resolución de unos **15,6 ms**. La prueba de que eso rompía el
dato es el `predict` del **DecisionTree** en `metricas_firmas.csv`: en la corrida `c7cf319` daba
`tiempo_inferencia_s = 0,0` en las **dos** variantes, y de ahí una fila que se contradecía sola
—`latencia_ms_por_flujo = 0,0` (cero milisegundos por flujo, un imposible) junto a un
`flujos_por_segundo` vacío—. Con `perf_counter`, en `38fdd4b`, ese mismo `predict` mide **0,002 s**
(54) y **0,004 s** (122): estaba un orden de magnitud **por debajo del tick**.

`perf_counter` es monótono y de alta resolución, pero **no tiene época**: solo sirve para
diferencias. La columna `fecha` la sigue dando `datetime.now()`.

> [!caution] Lo que **no** era una prueba (retirado)
> Se afirmó que los **758.824,7 flujos/s** del autoencoder de 122 (corrida `c7cf319`) eran
> artefacto del reloj. **No lo eran:** despejando, `t_inf = 22.544 / 758.824,7 = 0,029709 s`, que
> no es múltiplo de 15,6 ms. Y la corrida `38fdd4b`, ya con `perf_counter`, da `0,053 s` para ese
> mismo par. Era **varianza de máquina**, no resolución. La afirmación queda retirada; la del
> `0,0 s` del DecisionTree sí es demostrable.

`latencia_ms_por_flujo` y `flujos_por_segundo` se derivan del mismo par (tiempo de inferencia,
nº de flujos) y comparten **una sola guarda**: o se publican las dos, o ninguna (celda vacía).
Un tiempo no medible nunca se publica como `0.0`. Misma regla fuera de los tiempos: el `fpr`
de `evaluacion.evaluar_binario()` es `NaN` —celda vacía— si la partición no tiene ningún flujo
normal, porque sin negativos la tasa de falsas alarmas no está definida y un `0.0` publicaría
«cero falsas alarmas». Afecta a `fpr`, `bin_fpr`, `fpr_cascada` y `fpr_detector`; con D2 real
no se dispara.

> [!note] `fpr_cascada` **es** `bin_fpr` en `metricas_hibrido.csv`
> Mismo número y misma fila (0,101740 en la variante de 54 de la corrida `ac496cb`), y es
> **correcto por construcción**: la etapa 2 solo reclasifica los flujos que la etapa 1 marcó como
> sospechosos y **nunca devuelve uno a `normal`**, así que la cascada no puede tener otro FPR que
> el de su etapa 1. Se conservan las dos columnas porque responden a dos requisitos distintos
> —`bin_fpr` cierra el bloque binario que pide **H-5** y `fpr_cascada` es el FPR que **P-2** exige
> junto al titular de 0-day—, pero T1 no admite dos nombres para una magnitud sin declararlo: la
> coincidencia va escrita en el dato, dentro de `config.ALCANCE_HIBRIDO`.

#### Lo que `perf_counter` NO arregla: la dispersión entre corridas

Es *wall-clock* en una **máquina no dedicada**. Con la misma semilla, el mismo código y una
**calidad idéntica al bit**, los tiempos se mueven mucho. Lo que sigue **no es una cota** —la
corrida siguiente puede superarla—: es lo **medido** entre las cuatro corridas que llevan columna
`commit`, `c7cf319` · `38fdd4b` · `5516b60` · `ac496cb`, celda a celda.

| Tabla | Columna | Peor caso observado entre las cuatro corridas | Valores (`c7cf319` / `38fdd4b` / `5516b60` / `ac496cb`) |
|---|---|---|---|
| `metricas_anomalias.csv` | `tiempo_s` | **Autoencoder 54: 4,82×** | 52,43 / 37,71 / 181,91 / 38,20 s |
| `metricas_anomalias.csv` | `tiempo_inferencia_s` | **Autoencoder 54: 5,07×** | 0,048 / 0,031 / 0,147 / 0,029 s |
| `metricas_firmas.csv` | `tiempo_s` | **DecisionTree 54: 4,30×** | 2,35 / 2,01 / 7,35 / 1,71 s |
| `metricas_firmas.csv` | `tiempo_inferencia_s` | **DecisionTree 54: 3,5×** (entre las tres medidas con `perf_counter`) | *(0,0 = artefacto)* / 0,002 / 0,007 / 0,002 s |
| `metricas_baseline.csv` | `tiempo_s` | RF monolítico 54: 2,10× | 34,13 / 28,31 / 39,17 / 59,44 s |
| `metricas_hibrido.csv` | `tiempo_s` | La cascada 54: 1,90× | 24,80 / 22,17 / 27,71 / 42,02 s |

Dos lecturas que hay que arrastrar a cualquier frase de la memoria que compare tiempos:

1. **La dispersión no es cosa solo de los tiempos largos.** El autoencoder de 54 mueve su
   `tiempo_s` (decenas de segundos a minutos) y su `tiempo_inferencia_s` (decenas de
   milisegundos) prácticamente en el mismo factor, 4,8× y 5,1×.
2. **Ni la celda más estable baja de ≈1,2×.** El mínimo observado en las 8 filas de anomalías es
   `OneClassSVM` 54 con 1,23× (26,17 / 23,28 / 28,10 / 22,89 s). **Una diferencia menor que eso
   entre dos filas no significa nada**, y ninguna cifra de tiempo puede presentarse como propiedad
   del algoritmo sin declarar esta dispersión.
3. **Añadir una corrida solo ha empeorado la dispersión, nunca la ha estrechado.** De las seis
   celdas de la tabla, `ac496cb` empeora el factor en cuatro (`tiempo_inferencia_s` del
   autoencoder, `tiempo_s` del DecisionTree, del baseline y del híbrido) y no mejora ninguna. Es
   la razón de que la banda se declare **medida y no cota**.

**Ninguna columna de tiempo es reproducible.** Valen como comparación relativa de coste **dentro
de la misma corrida** y como orden de magnitud. El resto de la tabla sí es reproducible
(semilla 42).

> [!caution] Ni siquiera la **dirección** de una comparación de tiempos aguanta sola
> Comparar dos algoritmos por su tiempo **dentro de la misma corrida** parece más seguro que
> comparar dos corridas, pero tampoco basta. Contraejemplo medido: `HistGradientBoosting` es más
> caro de entrenar que `RandomForest` en **7 de los 8** pares disponibles, con una banda de
> **1,32× a 4,41×** y grids de igual cardinalidad — y el octavo **se invierte**: en `5516b60`,
> variante de 54, RF 108,152 s frente a HistGB 83,315 s (**0,77×**).
>
> | Corrida | 54 (`tiempo_entrenamiento_s` RF → HistGB) | 122 |
> |---|---|---|
> | `c7cf319` | 65,876 → 128,204 (**1,95×**) | 60,887 → 268,642 (**4,41×**) |
> | `38fdd4b` | 47,429 → 62,404 (**1,32×**) | 95,487 → 237,743 (**2,49×**) |
> | `5516b60` | 108,152 → 83,315 (**0,77×**) | 68,698 → 194,108 (**2,83×**) |
> | `ac496cb` | 48,943 → 64,997 (**1,33×**) | 52,609 → 181,346 (**3,45×**) |
>
> La corrida publicada **reconfirma la dirección en los dos pares** (1,33× y 3,45×), así que
> **T20 no se toca**; pero la inversión de `5516b60` sigue en la tabla y sigue mandando la regla:
> una dirección solo es citable si se repite en **todas** las corridas disponibles, y se cita con
> la banda de factores, nunca con el par de segundos. Aquí no se repite en todas: lo citable es
> «HistGB sale más caro que RF en 7 de 8 pares medidos», no «HistGB es más caro que RF».

> [!danger] Qué mide la latencia — y qué no (declaración exigida por P9)
> `latencia_ms_por_flujo` y `flujos_por_segundo` miden **solo el `predict`/`score` sobre
> características ya calculadas y ya cargadas en memoria**. **No** incluyen la captura del
> tráfico, el ensamblado del flujo ni la extracción de las 41 características del registro
> NSL-KDD, que es donde vive el coste real de un despliegue. Citar ese caudal como capacidad
> operativa sería exactamente la *Lab-Only Evaluation* que denuncia el pitfall **P9**. La
> frase viaja en cada fila dentro de `alcance_tiempo_s` (`config._AVISO_LATENCIA_SOLO_PREDICT`);
> el número, solo aquí.
>
> **Y el número, con dos cifras significativas y ni una más.** El caudal máximo de `ac496cb` es el
> del `predict` del DecisionTree: **del orden de 10⁶ flujos/s — ≈4,6·10⁶ a 54 características y
> ≈2,6·10⁶ a 122**, sobre una medida **única** de ~2 ms y ~4 ms respectivamente. La precisión con
> la que el CSV lo imprime (`4589459.9` y `2572359.1`) es ruido con formato de exactitud: el
> `tiempo_inferencia_s` publicado va redondeado a **milisegundos** (0,002 y 0,004 s), así que
> `9.083 / 0,002` da **4.541.500** —el divisor real, 1,9791 ms, solo se recupera despejando
> `latencia_ms_por_flujo`— y un margen de ±0,5 ms sobre esos ~2 ms mueve el caudal entre
> **3,6·10⁶ y 6,1·10⁶** flujos/s. Con dos cifras significativas ya se está siendo generoso.
>
> El propio par lo demuestra: es **el mismo DecisionTree**, cuyo coste por muestra en `predict` es
> el recorrido de un árbol de `max_depth=10` —idéntico en las dos variantes, porque la profundidad
> ganadora es la misma— y aun así la horquilla entre ellas es de **1,8×**. **Esa horquilla es
> *jitter*, no características.**

#### `tiempo_s`: tres significados, uno por tabla

`tiempo_s` era el último caso vivo del defecto que T1 cierra —mismo nombre de columna, tres
magnitudes—. Ni se homogeneiza el cálculo ni se renombra la columna: **cada fila declara qué
mide** en la columna hermana `alcance_tiempo_s`, obligatoria en las cuatro tablas principales
(`evaluacion.COLUMNAS_MINIMAS`).

Por qué declarar y no unificar: la nota de trazabilidad de `4.4` cita la columna por su nombre
(`tiempo_s`), así que renombrarla rompería la referencia; y el texto de `4.4` describe su
cálculo actual —«el proceso completo por algoritmo […] no solo el ajuste»—, de modo que
unificar los tres convertiría medidas ya descritas en una cuarta que no describe ningún
capítulo.

> [!note] La tabla de `4.4` del vault está desactualizada por su cuenta
> Se alegó que unificar «movería los 5,0/28,3/16,4/40,6 s que cita `4.4`». Esos cuatro valores son
> de la corrida **pre-T1 versionada en `8b07319`** y **ninguna corrida posterior los reproduce**:
>
> | Corrida | `tiempo_s` de IF / OCSVM / LOF / AE (54) |
> |---|---|
> | *(pre-T1, en `8b07319`)* | 5,04 / 28,34 / 16,42 / 40,56 |
> | `c7cf319` | 5,51 / 26,17 / 20,85 / 52,43 |
> | `38fdd4b` | 4,01 / 23,28 / 13,28 / 37,71 |
> | `5516b60` | 5,14 / 28,10 / 22,77 / 181,91 |
> | `ac496cb` **(publicada)** | 3,92 / 22,89 / 12,75 / 38,20 |
>
> Ninguna coincide con otra, que es lo único que hacía falta demostrar: la cita del vault hay que
> refrescarla al redactar (**T19**), así que no protegía nada.

| Tabla | Qué mide su `tiempo_s` | Constante |
|---|---|---|
| `metricas_anomalias.csv` | El **bloque completo del algoritmo**, en orden de ejecución (cinco tramos **principales**: dentro de la misma ventana caen además el submuestreo a 20.000 filas de `OneClassSVM`, la construcción del estimador en cada iteración y un `roc_auc_score` por configuración): (1) los `fit` del grid (= `tiempo_entrenamiento_s`) · (2) **puntuar el set de validación etiquetado —D1_val + 5.000 de D3 = 18.469 filas— una vez por cada configuración del grid** (6/9/4/2 configs) = `tiempo_score_seleccion_s` · (3) puntuar D1_val (13.469 filas) para el umbral p95 = `tiempo_score_umbral_s` · (4) la inferencia sobre D2 (22.544 filas) = `tiempo_inferencia_s` · (5) `evaluar_binario` + **una** figura, que es lo que queda al restar las cuatro columnas anteriores. | `config.ALCANCE_TIEMPO_S_BLOQUE_ANOMALIAS` |
| `metricas_firmas.csv` | El **bloque completo del algoritmo**, con otra composición: (1) `GridSearchCV` + refit sobre D3 (= `tiempo_entrenamiento_s`) · (2) el `predict` sobre los 9.083 flujos conocidos de D2 (= `tiempo_inferencia_s`) · (3) `evaluar_multiclase` + **una** figura: coste casi fijo, que sale por resta. **No** incluye el mini-experimento de balanceo de 4.3.4. | `config.ALCANCE_TIEMPO_S_BLOQUE_FIRMAS` |
| `metricas_baseline.csv` | **Solo el entrenamiento** (GridSearchCV + refit). Coincide con `tiempo_entrenamiento_s` de la misma fila: residual **cero** salvo redondeo. | `config.ALCANCE_TIEMPO_S_SOLO_ENTRENAMIENTO` |
| `metricas_hibrido.csv` | El tramo que va de la **carga de los splits** al **cierre de la fila**: D1/D2/D3 + carga de los `.joblib` + calibración OOF (= `tiempo_entrenamiento_s`) + cascada sobre D2 (= `tiempo_inferencia_s`) + tabla de sensibilidad de los 3 umbrales. **No** incluye la figura 5×6, la tabla 0-day de los cuatro detectores ni la escritura de los CSV. No es tiempo de ajuste: el híbrido no re-entrena. | `config.ALCANCE_TIEMPO_S_CARGA_A_CIERRE_FILA` |

Los tres `tiempo_s` **no son comparables entre sí** (tres cálculos, cuatro declaraciones: anomalías
y firmas comparten cálculo y no composición).

#### El residual: `tiempo_s` ≠ `tiempo_entrenamiento_s` + `tiempo_inferencia_s`

Ese residual es la razón de ser de `alcance_tiempo_s`. **Todos los porcentajes de abajo son de la
corrida `ac496cb`** (la publicada) y **de ninguna otra**: no predicen la fila que tengas delante
—el reparto que vale es el que sale de las columnas de tiempo de la propia fila— y se
recalculan aquí, sin tocar el CSV, cada vez que se corre el runbook.

> [!note] Por qué **un** decimal y no dos
> `tiempo_s` se publica redondeado a **dos decimales** mientras que las columnas que se le restan
> llevan tres, así que el residual arrastra hasta ±0,005 s de puro redondeo. Sobre denominadores
> de pocos segundos eso es **±0,13 pp** en `IsolationForest` 54 (0,005 / 3,92) y **±0,29 pp** en
> `DecisionTree` 54 (0,005 / 1,71): el segundo decimal del porcentaje es ruido y no se escribe.
> Las dos únicas cifras que van con dos decimales son las del híbrido, cuyo denominador es de
> decenas de segundos.

**Anomalías** (`ac496cb`). Ya no se estima nada: `anomalias.py` cronometra los dos tramos grandes
y los publica, así que la cola sale exacta por resta. Residual =
`tiempo_s` − `tiempo_entrenamiento_s` − `tiempo_inferencia_s`.

| Detector | Variante | Residual (= no ajuste ni inferencia) | del cual `tiempo_score_seleccion_s` | `tiempo_score_umbral_s` | cola (métricas + figura) |
|---|---|---|---|---|---|
| `IsolationForest` | 54 | **33,3 %** — (3,92 − 2,500 − 0,116) / 3,92 | 26,9 % | 1,8 % | 4,6 % |
| `OneClassSVM` | 54 | **49,5 %** — (22,89 − 9,083 − 2,479) / 22,89 | 42,3 % | 6,4 % | 0,7 % |
| `LocalOutlierFactor` | 54 | **27,6 %** — (12,75 − 8,435 − 0,801) / 12,75 | 20,9 % | 5,1 % | 1,5 % |
| `Autoencoder` | 54 | 0,5 % — (38,20 − 37,977 − 0,029) / 38,20 | 0,1 % | 0,0 % | 0,4 % |
| `IsolationForest` | 122 | **31,0 %** — (3,99 − 2,650 − 0,104) / 3,99 | 24,8 % | 1,6 % | 4,6 % |
| `OneClassSVM` | 122 | **38,5 %** — (34,39 − 19,632 − 1,518) / 34,39 | 35,4 % | 2,7 % | 0,5 % |
| `LocalOutlierFactor` | 122 | **27,7 %** — (20,32 − 13,307 − 1,380) / 20,32 | 21,4 % | 5,3 % | 0,9 % |
| `Autoencoder` | 122 | 0,7 % — (31,24 − 31,003 − 0,031) / 31,24 | 0,2 % | 0,1 % | 0,4 % |

Lo domina el **scoring de la selección**: el script pasa por el scorer bastantes más filas
eligiendo configuración (18.469 × 6/9/4/2) que evaluando (22.544 una vez). En `OneClassSVM` ese
tramo se acerca al propio ajuste. No entraba en `tiempo_entrenamiento_s` porque no es `fit`.

> [!caution] Repartos retirados por falsados
> Este documento publicó antes «el tramo (2) es el 75-86 % y el (3) el 5-15 %» y un scoring de
> selección de ≈9,5 s: procedían de un **modelo de coste no declarado** —con escalado plano por
> filas, ese tramo de `OneClassSVM` 54 salía en 17,8 s dentro de un residual **medido** de
> 11,497 s, un imposible—. Y publicó «**27-49 %**» sin anclar a corrida ni decir de qué filas: en
> `ac496cb` las dos filas del `Autoencoder` dan **0,5 %** y **0,7 %**, más de un orden de magnitud
> por debajo de esa banda, porque su ajuste se lo come todo. Los dos quedan retirados; la tabla de
> arriba los sustituye, con corrida declarada y con la resta escrita al lado.

**Firmas** (`ac496cb`). El `GridSearchCV` se lleva entre el **84,7 %** (mínimo: `DecisionTree` 54,
1,449 / 1,71) y el **99,6 %** (máximo: `HistGradientBoosting` 122, 181,346 / 182,04) del bloque, y
el residual es un único tramo —la cola de métricas + figura—. **No** lleva columna propia: al ser
un único componente sale exacto restando las otras dos columnas, y una columna más solo repetiría
una resta.

Ese residual, en segundos y por orden de tabla —`DecisionTree` · `RandomForest` · `KNN` ·
`HistGradientBoosting`—, es **0,259 · 0,273 · 0,321 · 0,340 s** a 54 características y
**0,280 · 0,298 · 0,349 · 0,513 s** a 122. Siete de las ocho filas caben en 0,26-0,35 s, pero la
octava (`HistGradientBoosting` 122) casi **dobla** el mínimo: la cola **no es un coste fijo**, es
un coste **poco variable dentro de un factor 2**, y así hay que citarla. Como es pequeño en
términos absolutos, solo pesa donde el bloque entero dura pocos segundos: **15,1 %** en
`DecisionTree` 54 y **10,5 %** en `DecisionTree` 122 —(2,67 − 2,386 − 0,004) / 2,67, con el
`tiempo_entrenamiento_s` a sus tres decimales: redondearlo a 2,39 daría 10,3 % y la fórmula
dejaría de reproducir su propio resultado—, frente al **0,3-0,7 %** de los otros seis.

**Híbrido** (`ac496cb`). Calibración OOF **92,61 %** (54) y **87,11 %** (122); el resto —**6,53 %**
y **12,50 %**— son la carga de los splits, la de los dos `.joblib` y las tres pasadas de métricas
de la tabla de sensibilidad, sin desglosar: ninguna columna los mide por separado. La cascada
sobre D2 completa el 100 %: **0,86 %** y **0,39 %**. Es decir: **más del 85 % de lo que cuesta el
híbrido es calibrar un umbral, no detectar**.

> [!note] El híbrido de 122 tarda **menos** que el de 54, y no es una paradoja
> `tiempo_s` da **42,02 s** (54) frente a **18,32 s** (122). Escribirlo como «más características,
> menos tiempo» sería falso: la causa es **mecánica y está en el dato**. El grueso del bloque es la
> calibración OOF, que reajusta el clasificador de firmas una vez por fold —y **la configuración
> ganadora de firmas no es la misma en las dos variantes**:
>
> | Variante | `config_ganadora` de `RandomForest` en `metricas_firmas.csv` |
> |---|---|
> | 54 | `{'clf__max_depth': 10, 'clf__n_estimators': 300}` |
> | 122 | `{'clf__max_depth': None, 'clf__n_estimators': 100}` |
>
> **300 árboles contra 100**: el híbrido de 54 hace del orden de 3× el trabajo en la calibración.
> Lo medido es `tiempo_entrenamiento_s` = **38,914 s** (54) frente a **15,959 s** (122), **2,44×**
> — del orden esperado, con la profundidad libre del modelo de 122 y la dispersión de máquina
> explicando el resto de la diferencia. La comparación de tiempos entre las dos variantes del
> híbrido **no compara dos anchos de entrada: compara dos bosques distintos.**
>
> Y tampoco es cierto que la calidad sea la misma en las dos: `conocida_f1_macro` vale
> **0,748051** (54) y **0,655441** (122). Son dos sistemas distintos, no el mismo con más
> columnas. Material para **T19** y **T21**.

> [!warning] Los tres tiempos de *scoring* de anomalías: cómo se citan
> `tiempo_score_seleccion_s`, `tiempo_score_umbral_s` y `tiempo_inferencia_s` miden **la misma
> operación** (puntuar filas con el modelo ya ajustado) sobre conjuntos de tamaño distinto, así
> que el cociente crudo entre dos de ellos **no es un cociente de coste por flujo**: hay que
> ponerlo siempre **contra la referencia de tamaños**. Para el par umbral/inferencia esa
> referencia es |D1_val| / |D2| = **13.469 / 22.544 = 0,597**.
>
> En `ac496cb`, `tiempo_score_umbral_s / tiempo_inferencia_s` va de **0,59**
> (`OneClassSVM` 54) a **0,81** (`LocalOutlierFactor` 54). Publicar ese rango a secas invita
> justo a la lectura que el dato prohíbe, así que se publica **normalizado por filas** (cociente
> dividido por 0,597 = coste por fila del tramo de umbral respecto al de inferencia):
>
> | Detector | 54 | 122 |
> |---|---|---|
> | `IsolationForest` | 1,01× | 1,01× |
> | `OneClassSVM` | 0,99× | 1,01× |
> | `LocalOutlierFactor` | **1,36×** | **1,32×** |
> | `Autoencoder` | 1,10× | 1,03× |
>
> Leído así: **seis de los ocho detectores puntúan D1_val a 0,99-1,10× el coste por fila de D2**
> —es decir, a coste por fila prácticamente igual, que es lo que la teoría predice— y las **dos
> filas de `LocalOutlierFactor`** se salen, a 1,36× (54) y 1,32× (122).
>
> **La desviación de LOF se describe y no se explica.** La corrida no controla nada de lo que
> decidiría esa diferencia —estado de caché, carga de la máquina, `n_jobs`—, así que no hay con
> qué atribuirla. Y no es estable: en `5516b60` el mismo cociente normalizado daba **1,18×** para
> `LocalOutlierFactor` 54 (0,703 / 0,597) y **1,49×** para el de 122. Es decir, entre las dos
> corridas el detector que más se sale cambia de variante y cambia de valor. **Descripción, no
> explicación.**
>
> *(Dos afirmaciones retiradas de este mismo recuadro. **Una:** que el desvío venía del
> `algorithm='brute'` que `sklearn` asigna a `LocalOutlierFactor` por encima de 15 features — era
> una atribución causal sobre una medida única. **Dos:** el argumento «LOF no es el único que lo
> enseña, el `Autoencoder` de 54 da 0,884», que servía para relativizar el primero. Esa premisa
> **ya no se sostiene**: en `ac496cb` **ningún** detector llega a 0,85 en el cociente crudo —los
> ocho valen 0,603 · 0,593 · 0,814 · 0,655 · 0,606 · 0,601 · 0,786 · 0,613—, LOF incluido, cuyo
> máximo es **0,814**. Los dos valores de `5516b60` que estaban por encima de 0,85 se han
> desplomado: `Autoencoder` 54 de **0,884 a 0,655** y `LocalOutlierFactor` 122 de **0,889 a
> 0,786**. **Una magnitud que se mueve así entre corridas no sostiene ninguna atribución causal**,
> ni a favor ni en contra.)*

> [!note] Las dos columnas de épocas del autoencoder: `n_iter_ganador` y `n_iter_total_grid`
> El autoencoder es un `MLPRegressor` con `early_stopping=True` y `max_iter=300`, así que su
> tiempo de ajuste depende de **dos** cosas que el CSV no separaba: cuántas épocas necesitó y cómo
> de cargada estaba la máquina. Sin ese dato no se puede decidir si los **180,965 s** (54) frente a
> **47,826 s** (122) de `5516b60` —relación **invertida** respecto a `38fdd4b`, que dio 37,492 s y
> 121,059 s— son épocas o carga. Es lo que pedía **T22**.
>
> Se publican **dos** columnas porque **no son intercambiables**, y confundirlas fue el defecto 2
> del dictamen de `0595a15`:
>
> | Columna | Qué cuenta | Para qué sirve |
> |---|---|---|
> | `n_iter_ganador` | Épocas del ajuste **de la configuración ganadora** | Saber si el modelo que se publica se cortó por `max_iter=300` o convergió |
> | `n_iter_total_grid` | **Suma** de las épocas de **todas** las configuraciones del grid | El denominador **coherente** de `tiempo_entrenamiento_s`, que cronometra exactamente esos mismos `fit` |
>
> **Coherente y no «único válido»:** el grid del autoencoder tiene **dos arquitecturas**,
> `(64, 32, 64)` y `(32, 16, 32)`, cuyo coste por época no es el mismo, así que el cociente
> `tiempo_entrenamiento_s / n_iter_total_grid` es una **media ponderada** entre dos costes por
> época distintos —ponderada por cuántas épocas consumió cada arquitectura, que es justo lo que la
> columna no desglosa—. Es el denominador que cubre el mismo conjunto de `fit` que el numerador, y
> por eso el cociente es interpretable; no es una constante física del modelo.
>
> **Respuesta medida a T22 (corrida `ac496cb`).** Con ese denominador:
>
> | Variante | `tiempo_entrenamiento_s` | `n_iter_total_grid` | s/época | `n_iter_ganador` |
> |---|---|---|---|---|
> | 54 | 37,977 s | 162 | **0,234** | 117 |
> | 122 | 31,003 s | 128 | **0,242** | 66 |
>
> El coste por época difiere un **3,3 %** entre las dos variantes, mientras que el tiempo total
> difiere un 22 % y el recuento de épocas un 27 % (162 vs 128). Conclusión: **la diferencia de
> tiempo del autoencoder entre las dos variantes es de épocas, no de carga de máquina** — el ajuste
> a 122 características no es más barato por época, es que necesitó menos épocas antes de que
> `early_stopping` lo cortara. Es exactamente la pregunta que T22 dejaba abierta y estas dos
> columnas son las que permiten responderla; sin ellas la comparación era indecidible.
>
> Dos avisos sobre esta respuesta: (a) vale para `ac496cb` y para ninguna otra corrida —el mismo
> par en `5516b60` no se puede recalcular porque aquel CSV **no tiene** las columnas de épocas—;
> y (b) ninguno de los dos ajustes ganadores tocó el tope (`max_iter=300`): 117 y 66, así que los
> dos cortaron por `early_stopping` y la comparación es entre dos ajustes convergidos.
>
> `tiempo_entrenamiento_s / n_iter_ganador` **no son** segundos por época: el numerador cubre las
> dos configuraciones del grid del autoencoder y el denominador solo una. `n_iter_total_grid` se
> acumula dentro del mismo bucle que suma los `fit` (`anomalias._seleccionar_config`), así que
> ambos cubren el mismo conjunto por construcción.
>
> Las dos van **vacías** en `IsolationForest`, `OneClassSVM` y `LocalOutlierFactor` —no ajustan
> por iteraciones comparables; nunca un `0`, que se leería como medida—. El `.joblib` guarda lo
> mismo más `best_validation_score` cuando el estimador lo expone. Alcance declarado en
> `config.ALCANCE_N_ITER` y `config.ALCANCE_N_ITER_TOTAL` (ambas en `config.ALCANCE_COLUMNAS`: no
> son métricas sobre D2).

> [!warning] El log del híbrido imprime otra cifra
> `hibrido.py` congela `tiempo_s` al construir la fila resumen, pero su línea final
> («HÍBRIDO COMPLETADO … de pared») se lee al terminar del todo, con las figuras, la tabla
> 0-day de los cuatro detectores (que vuelve a puntuar D2 con IF+OCSVM+LOF+AE) y los CSV ya
> escritos. Son **dos medidas distintas**, no una discrepancia: el propio log lo dice e imprime
> las dos.

### La columna `commit`: tres valores posibles

| Valor | Significado |
|---|---|
| `<hash>` | El código (`Implementacion/`) no tenía cambios sin commitear al correr. |
| `<hash>-sucio` | Había cambios sin commitear **en `Implementacion/`**. La fila no es reproducible desde ese hash tal cual. |
| `<hash>-suciedad_desconocida` | El hash es válido, pero el `git status` falló o agotó su timeout: no se pudo determinar si el código estaba limpio. |

El `-sucio` mira **solo `Implementacion/`**, no todo el árbol (`config._RUTA_SUCIEDAD`): los
propios scripts escriben figuras y CSV en `Resultados/`, que está versionado, así que un
`git status` completo daría `-sucio` siempre y la columna no discriminaría nada. Si git no está
disponible o el directorio no es un repositorio, el valor es `desconocido` (sin hash).

### Límite declarado: las cuatro tablas principales son de pase único (semilla 42)

Las cuatro tablas principales contienen **un solo pase, con la semilla 42**. La dispersión entre
semillas (tarea **T4**, 10 semillas) **no entra en ellas**: va a **tabla propia**, con clave de
unicidad que incluya `semilla`. Queda escrito aquí porque hoy T4 chocaría contra tres muros a la
vez y se descubriría en ejecución, no antes:

1. `evaluacion.limpiar_variante_csv()` borra por **variante**, no por clave: 10 semillas de la
   misma variante colapsarían a la última escrita.
2. `evaluacion.CLAVE_UNICIDAD` (`set_features × algoritmo × alcance`) **no incluye `semilla`**:
   dos semillas de la misma variante son un duplicado y `comprobar_unicidad()` **aborta**.
3. `evaluacion.FILAS_ESPERADAS_POR_VARIANTE` es fijo 4/4/1/1: 40 filas hacen **abortar** a
   `comprobar_recuento()`.

Los tres aborts **se conservan**: ninguna invocación legítima de la CLI actual los dispara y son
lo que hace comprobable el recuento del runbook. La dispersión de T4 entra como tabla nueva
en el anexo `A.3`.

---

## Decisión de diseño clave: ajuste del scaler

| Enfoque | Scaler ajustado en | Ventaja | Desventaja |
|---|---|---|---|
| ~~Anterior~~ | Solo D1 (normal) | Anomalías se "desbordan" del rango → más detectables | D3 mal escalado → firmas sesgadas |
| **Actual** | D1 + D3 (todo el train) | Escalado correcto para ambos modelos | Ninguna significativa |

El scaler se ajusta en `concat(D1, D3)` y se aplica igual a D2 (test), garantizando que ninguna división tenga ventaja artificial en el rango de valores.
