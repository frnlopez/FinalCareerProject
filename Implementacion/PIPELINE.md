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
`metricas_balanceo.csv`. Y `metricas_anomalias.csv` estrena **tres** columnas —las dos medidas
`tiempo_score_seleccion_s` y `tiempo_score_umbral_s`, más `n_iter_ganador` (épocas del ajuste;
**solo la rellena el autoencoder**, celda vacía en los otros tres detectores)—, así que el CSV
anterior tiene otro
esquema: al re-ejecutar, `limpiar_variante_csv()` lo apartará como
`metricas_anomalias.csv.esquema-anterior.bak` y hay que correr **las dos variantes** (54 y 122)
para regenerarlo completo.

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

Se miden con **`time.perf_counter()`**, no con `time.time()`. Motivo: en Windows `time.time()`
tiene una resolución de unos **15,6 ms**. La prueba de que eso rompía el dato es el `predict` del
**DecisionTree** en `metricas_firmas.csv`: daba `t_inf = 0,0 s` en las **dos** variantes, y de ahí
una fila que se contradecía sola —`latencia_ms_por_flujo = 0,0` (cero milisegundos por flujo, un
imposible) junto a un `flujos_por_segundo` vacío—. Con `perf_counter` ese mismo `predict` mide
`0,002 s` (54) y `0,004 s` (122): estaba un orden de magnitud **por debajo del tick**, así que
`time.time()` no podía verlo. `perf_counter` es monótono y de alta resolución, pero **no tiene
época**: solo sirve para diferencias. La columna `fecha` la sigue dando `datetime.now()`.

> [!caution] Lo que **no** era una prueba (corregido)
> Aquí se afirmaba que los **758.824 flujos/s** del autoencoder eran artefacto del reloj. **No lo
> eran.** Despejando, `t_inf = 22.544 / 758.824,7 = 0,029709 s`, que no es múltiplo de 15,6 ms; y
> la corrida nueva —ya con `perf_counter`— da `0,053 s` para ese mismo par. Era **varianza de
> máquina** (1,8×), no resolución. La afirmación se retira; la que se cita arriba (el `0,0 s` del
> DecisionTree) sí es demostrable.

`latencia_ms_por_flujo` y `flujos_por_segundo` se derivan del mismo par (tiempo de inferencia,
nº de flujos) y comparten **una sola guarda**: o se publican las dos, o ninguna (celda vacía).
Un tiempo no medible nunca se publica como `0.0`. Misma regla fuera de los tiempos: el `fpr`
de `evaluacion.evaluar_binario()` es `NaN` —celda vacía— si la partición no tiene ningún flujo
normal, porque sin negativos la tasa de falsas alarmas no está definida y un `0.0` publicaría
«cero falsas alarmas». Afecta a `fpr`, `bin_fpr`, `fpr_cascada` y `fpr_detector`; con D2 real
no se dispara.

> [!note] `fpr_cascada` **es** `bin_fpr` en `metricas_hibrido.csv`
> Mismo número y misma fila (0,101740 en la variante de 54 de la corrida `5516b60`), y es
> **correcto por construcción**: la etapa 2 solo reclasifica los flujos que la etapa 1 marcó como
> sospechosos y **nunca devuelve uno a `normal`**, así que la cascada no puede tener otro FPR que
> el de su etapa 1. Se conservan las dos columnas porque responden a dos requisitos distintos
> —`bin_fpr` cierra el bloque binario que pide **H-5** y `fpr_cascada` es el FPR que **P-2** exige
> junto al titular de 0-day—, pero T1 no admite dos nombres para una magnitud sin declararlo: la
> coincidencia va escrita en el dato, dentro de `config.ALCANCE_HIBRIDO`.

> [!warning] Lo que `perf_counter` NO arregla: la varianza
> Arregla la resolución, no la dispersión. Es *wall-clock* en una máquina no dedicada, así que
> la misma corrida con la misma semilla da tiempos muy distintos.
>
> **Aquí no se escriben cotas** («varía hasta 4×»): no las hay, y cada corrida nueva desmiente la
> cifra que dejó la anterior —le pasó a la redacción previa de este aviso—. Lo que se escribe es
> **dispersión observada entre dos corridas nombradas**, que ninguna corrida futura puede
> desmentir:
>
> | Par de corridas | Dónde están | Dispersión observada |
> |---|---|---|
> | `38fdd4b` → `5516b60` | `metricas_anomalias.csv.esquema-anterior.bak` y el CSV vigente | Autoencoder 54: `tiempo_s` 37,71 s → 181,91 s = **4,83×**; `tiempo_entrenamiento_s` 37,492 s → 180,965 s = 4,83×; `tiempo_inferencia_s` 0,031 s → 0,147 s = **4,7×** (729.199 → 153.510 flujos/s) |
> | `8b07319` → `077119e` | CSV versionados en esos commits (código `c7cf319` en el segundo) | OneClassSVM 122: 163,26 s → 37,13 s y KNN 122 en firmas: 90,22 s → 207,81 s = **4,4×** en sentido contrario; en inferencia, autoencoder 54: 472.834 → 729.199 flujos/s (×1,54) y autoencoder 122: 758.825 → 421.427 (×0,56) |
>
> El primer par enseña además que **la dispersión no es cosa solo de los tiempos largos**: una
> medida de inferencia de decenas de milisegundos se mueve tanto como una de minutos.
> **Ninguno de esos factores es una cota superior** y **ninguna columna de tiempo es
> reproducible.** Sirven como comparación relativa de coste y de orden de magnitud; no para
> afirmar que un algoritmo es «un 20 % más rápido» que otro. El resto de la tabla sí es
> reproducible (semilla 42).

> [!danger] Qué mide la latencia — y qué no (declaración exigida por P9)
> `latencia_ms_por_flujo` y `flujos_por_segundo` miden **solo el `predict`/`score` sobre
> características ya calculadas y ya cargadas en memoria**. **No** incluyen la captura del
> tráfico, el ensamblado del flujo ni la extracción de las 41 características del registro
> NSL-KDD, que es donde vive el coste real de un despliegue. Por eso los **4,4 millones de
> flujos/s** del DecisionTree **no son capacidad operativa**: citarlos como tal sería exactamente
> la *Lab-Only Evaluation* que denuncia el pitfall **P9**. La frase viaja en cada fila dentro de
> `alcance_tiempo_s` (`config._AVISO_LATENCIA_SOLO_PREDICT`).

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

> [!note] El argumento que se alegaba antes, y su refutación —también fallida— corregidos
> Se decía que unificar «movería los 5,0/28,3/16,4/40,6 s de la tabla de `4.4`». **No era
> cierto.** Pero la refutación que se escribió aquí tampoco: aquellos «5,51/26,17/20,85/52,43 que
> publica **hoy** `metricas_anomalias.csv`» no son de ninguna corrida del árbol. Lo verificable,
> anclado a su artefacto:
>
> | Corrida | `tiempo_s` de IF / OCSVM / LOF / AE (54) | Dónde |
> |---|---|---|
> | `38fdd4b` | 4,01 / 23,28 / 13,28 / 37,71 | `metricas_anomalias.csv.esquema-anterior.bak` |
> | `5516b60` | 5,14 / 28,10 / 22,77 / 181,91 | `metricas_anomalias.csv` vigente |
>
> Ninguna de las dos coincide con la tabla de `4.4` **ni entre sí**, que es lo único que hacía
> falta: la cita del vault está desactualizada por su cuenta y hay que refrescarla al redactar,
> así que no protegía nada. Los valores van **anclados a su corrida** a propósito; la siguiente
> los vuelve a mover.

| Tabla | Qué mide su `tiempo_s` | Constante |
|---|---|---|
| `metricas_anomalias.csv` | El **bloque completo del algoritmo**, en orden de ejecución (cinco tramos **principales**: dentro de la misma ventana caen además el submuestreo a 20.000 filas de `OneClassSVM`, la construcción del estimador en cada iteración y un `roc_auc_score` por configuración): (1) los `fit` del grid (= `tiempo_entrenamiento_s`) · (2) **puntuar el set de validación etiquetado —D1_val + 5.000 de D3 = 18.469 filas— una vez por cada configuración del grid** (6/9/4/2 configs) = `tiempo_score_seleccion_s` · (3) puntuar D1_val para el umbral p95 = `tiempo_score_umbral_s` · (4) la inferencia sobre D2 (= `tiempo_inferencia_s`) · (5) `evaluar_binario` + **una** figura, que es lo que queda al restar las cuatro columnas anteriores. | `config.ALCANCE_TIEMPO_S_BLOQUE_ANOMALIAS` |
| `metricas_firmas.csv` | El **bloque completo del algoritmo**, con otra composición: (1) `GridSearchCV` + refit sobre D3 (= `tiempo_entrenamiento_s`, el 95,7-99,7 % del total **en la corrida `38fdd4b`**) · (2) el `predict` sobre los 9.083 flujos conocidos de D2 (= `tiempo_inferencia_s`) · (3) `evaluar_multiclase` + **una** figura: coste casi fijo, sin banda publicada (ver el aviso del residual). **No** incluye el mini-experimento de balanceo de 4.3.4. | `config.ALCANCE_TIEMPO_S_BLOQUE_FIRMAS` |
| `metricas_baseline.csv` | **Solo el entrenamiento** (GridSearchCV + refit). Coincide con `tiempo_entrenamiento_s` de la misma fila: residual **cero** salvo redondeo. | `config.ALCANCE_TIEMPO_S_SOLO_ENTRENAMIENTO` |
| `metricas_hibrido.csv` | El tramo que va de la **carga de los splits** al **cierre de la fila**: D1/D2/D3 + carga de los `.joblib` + calibración OOF (= `tiempo_entrenamiento_s`, 86-91 %) + cascada sobre D2 (= `tiempo_inferencia_s`, ~0,5 %) + tabla de sensibilidad de los 3 umbrales. **No** incluye la figura 5×6, la tabla 0-day de los cuatro detectores ni la escritura de los CSV. No es tiempo de ajuste: el híbrido no re-entrena. | `config.ALCANCE_TIEMPO_S_CARGA_A_CIERRE_FILA` |

Los tres `tiempo_s` **no son comparables entre sí** (tres cálculos, cuatro declaraciones: anomalías
y firmas comparten cálculo y no composición).

> [!warning] `tiempo_s` **no** es `tiempo_entrenamiento_s + tiempo_inferencia_s`
> El residual entre las tres columnas es la razón de ser de `alcance_tiempo_s`, y en anomalías es
> enorme: **27-49 % de `tiempo_s` en la corrida de referencia `38fdd4b`** (allí el máximo fue
> `OneClassSVM` 54 con 11,50 s de 23,28 s; luego OCSVM 122 39,6 %, IF 54 35,1 %, IF 122 28,9 %,
> LOF 27,3 % y 27,2 %), y solo el 0,3-0,5 % en el autoencoder. **Esos seis porcentajes son de esa
> corrida y de ninguna otra**: no predicen la fila que tengas delante —el reparto que vale es el
> que sale de las cinco columnas de tiempo de la propia fila—, igual que declara el
> `alcance_tiempo_s` que viaja en el CSV. Ese residual **ya no se reparte por estimación**: `anomalias.py` cronometra sus
> dos tramos grandes y los publica como `tiempo_score_seleccion_s` (el scoring del set etiquetado
> repetido por configuración del grid) y `tiempo_score_umbral_s` (el scoring de D1_val), de modo
> que la cola de métricas + figura sale por resta desde el propio CSV. El reparto que este
> documento daba antes —«75-86 % / 5-15 %», y un scoring de selección de ≈9,5 s que igualaba al
> ajuste en `OneClassSVM` 54— procedía de un modelo de coste no declarado y **se retira**: con
> escalado plano por filas ese mismo tramo salía en 17,8 s dentro de un residual medido de
> 11,497 s, un imposible. En firmas el mismo residual es la cola de métricas + figura —un tramo de
> coste casi fijo que no escala con el modelo—, y ahí **no** hace falta columna nueva: al ser un único
> tramo se obtiene exacto restando las otras dos columnas de tiempo. Tampoco se le pone banda:
> las dos corridas de referencia no se solapan (`38fdd4b`, 0,258-0,314 s y 10,7-12,8 % en
> `DecisionTree`; `5516b60`, 1,052 s y 14,3 % en `DecisionTree` 54), así que **el número que vale
> es el de la resta**.

> [!warning] Los tres tiempos de *scoring* de anomalías no son comparables por flujo
> `tiempo_score_seleccion_s`, `tiempo_score_umbral_s` y `tiempo_inferencia_s` miden **la misma
> operación** (puntuar filas con el modelo ya ajustado) sobre tres conjuntos de tamaño distinto,
> y aun así **no se pueden normalizar por número de filas y comparar entre sí**: cada uno cae en
> un **estado de caché** diferente. En el grid, cada modelo se puntúa justo después de su propio
> `fit` (caliente); el pase del umbral reutiliza el ganador, ajustado 2-3 iteraciones antes
> (frío); y la inferencia sobre D2 reutiliza el que el pase del umbral acaba de calentar.
>
> El único que lo enseña es **`LocalOutlierFactor`**: en la corrida `5516b60`,
> `tiempo_score_umbral_s / tiempo_inferencia_s` da **0,703** (54) y **0,889** (122), cuando la
> razón de filas puntuadas impone 13.469/22.544 = **0,597**. **No es error de medida.** LOF es el
> único porque `sklearn` le asigna `algorithm='brute'` por encima de 15 features y su *scoring*
> recorre las 53.874 filas de `D1_train`, mientras IF, OCSVM y el autoencoder puntúan contra un
> modelo compacto. De ahí que **no** se pueda concluir «el *scoring* del umbral de LOF cuesta más
> por flujo que la inferencia sobre D2»: es la misma operación con el mismo modelo. El aviso
> viaja también en el dato (`config.ALCANCE_TIEMPO_S_BLOQUE_ANOMALIAS`).

> [!note] `n_iter_ganador`: sin ella, el `tiempo_entrenamiento_s` del autoencoder no se puede leer
> El autoencoder es un `MLPRegressor` con `early_stopping=True` y `max_iter=300`, así que su
> tiempo de ajuste depende de **dos** cosas que el CSV no separaba: cuántas épocas necesitó y
> cómo de cargada estaba la máquina. Con `38fdd4b` dando 37,492 s (54) y 121,059 s (122), y
> `5516b60` dando 180,965 s (54) y 47,826 s (122) —**relación invertida**—, no había forma de
> decidir. Desde ahora `metricas_anomalias.csv` publica `n_iter_ganador`: épocas del ajuste del
> modelo ganador, **solo para el autoencoder** (celda vacía en IF, OCSVM y LOF, que no ajustan
> por iteraciones comparables; nunca un `0`, que se leería como medida). Un valor igual a **300**
> avisa además de que el ajuste se cortó por el tope y no por convergencia. El `.joblib` guarda
> lo mismo más `best_validation_score` cuando el estimador lo expone. Alcance declarado en
> `config.ALCANCE_N_ITER` (entra en `config.ALCANCE_COLUMNAS`: no es una métrica sobre D2).

> [!warning] El log del híbrido imprime otra cifra
> `hibrido.py` congela `tiempo_s` al construir la fila resumen, pero su línea final
> («HÍBRIDO COMPLETADO … de pared») se lee al terminar del todo, con las figuras, la tabla
> 0-day de los cuatro detectores (que vuelve a puntuar D2 con IF+OCSVM+LOF+AE: unos 4-5 s de
> los ≈27 s de la variante de 54) y los CSV ya escritos. Son **dos medidas distintas**, no una
> discrepancia: el propio log lo dice e imprime las dos.

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
