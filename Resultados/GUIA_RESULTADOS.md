# Guía de la carpeta `Resultados/`

> Guía de re-onboarding: qué es cada fichero de esta carpeta, cómo interpretarlo y en qué
> sección de la memoria del TFG se usa. Escrita para retomar el proyecto en frío.
> El mapa completo artefacto → sección vive en `next-steps.md` (sección 6.6).

---

## 1. Qué es esta carpeta

Aquí se vuelca **todo lo que generan los scripts** de `Implementacion/app/`:

| Script | Estado | Qué deposita aquí |
|---|---|---|
| `program.py` | funcionando | Splits D1/D2/D3 (CSVs originales y procesados), metadatos (`_mappings_and_info.txt`, `_usage_guide.txt`, `selected_features.txt`), transformadores (`.joblib`) y la figura del EDA |
| `validacion.py` | ejecutado (54 y 122) | **Por variante**: un `..._validation_report.txt`, un `..._vocabulario_onehot.csv` (§2.4) y **6** figuras de validación (las 4 de siempre + las 2 del KS contra los normales de D2, tarea T2). Con las dos variantes: **2** informes (`specialized_nsl_kdd_validation_report.txt` y `specialized_nsl_kdd_sin_seleccion_validation_report.txt`), **2** CSV de vocabulario y **12** figuras `validacion_*` |
| `anomalias.py` | ejecutado (54 y 122) | `metricas_anomalias.csv`, `modelos\anomalia_*.joblib`, figuras ROC/PR y matrices 2×2 |
| `firmas.py` | ejecutado (54 y 122) | `metricas_firmas.csv`, `metricas_balanceo.csv`, `firmas_reglas_*.txt`, `modelos\firma_*.joblib`, matrices 4×4 |
| `baseline.py` | ejecutado (54 y 122) | `metricas_baseline.csv`, `metricas_baseline_0day.csv`, `modelos\baseline_rf_*.joblib`, `figuras\baseline_cm_*.png` |
| `hibrido.py` | ejecutado (54 y 122) | `metricas_hibrido.csv`, `metricas_hibrido_calibracion.csv`, `metricas_hibrido_0day.csv`, `figuras\hibrido_cm_*.png`, `modelos\hibrido_*.joblib` (descriptor) |
| `cascada_invertida.py` | ejecutado (54 y 122) | `metricas_cascada_invertida.csv` y `figuras\cascada_invertida_<set>.png`. **No entrena nada**: carga `firma_*.joblib` y lee el umbral de `hibrido_*.joblib` |
| `evaluacion.py` | módulo común | No deposita por sí mismo: lo usan los cuatro scripts de modelos y `cascada_invertida.py` |
| `barrido_semillas.py` | **corrido** (T4, 2026-08-12 22:09 → 00:38, sello `df30cb2`) | Las **nueve** tablas `metricas_*_semillas.csv` (**2.320 filas** en total), a través de los cinco scripts hijos, más los artefactos sufijados `_semilla<N>` **no versionados**: **260** figuras `figuras\*_semilla*`, **20** `firmas_reglas_*_semilla*.txt` y **100** logs en `logs_barrido\`. Los `.joblib` por semilla los borra él mismo al cerrar cada semilla (en `modelos\` no queda ninguno). Además, `verificacion_semilla_joblib.txt`: la traza de que los 20 `.joblib` publicados declaran `semilla = 42` |
| `agregar_semillas.py` | **corrido tres veces** (T4, 2026-08-13: **7,2 s** la primera; **1,70 s** la segunda, tras el arreglo de `_tabla_md()`; y una tercera con el **titular automático**. **En disco están los de la tercera**, cabecera `2026-08-13T19:54:48`) | `dispersion_semillas.csv` y `dispersion_semillas.md` — **198 filas** (98 de *calidad* + 100 de *dispersión de máquina*) con n, media, sd muestral (`ddof=1`), mín y máx, más el valor de la semilla 42 al lado de cada banda y el recuento **«13 de 98»** fuera de banda; `commits_origen = df30cb2` único en todas las celdas y `commit_agregador = ddade37-sucio` — sello impreso, **pendiente de re-anclaje** (el de la segunda pasada, `df30cb2-sucio`, quedó re-anclado a `9ad971b`; §6.2) |

**Regla de oro:** nada de esta carpeta se edita a mano. Todo se **regenera** ejecutando los
scripts (con `random_state=42`); si un número va a la memoria, tiene que salir de aquí. Para
regenerar: activar el venv y ejecutar `python app\program.py` y luego `python app\validacion.py`
**más `python app\validacion.py --sin-seleccion`** — son dos informes, uno por variante
(detalles y trampas de ejecución en `next-steps.md`, sección 6.0).

**Corolario de la regla de oro:** como casi todo existe en dos variantes, **ninguna cifra se cita
sin nombrar el fichero del que sale**. Un «37 características con drift» a secas es ambiguo: son
37 en 54 características y 44 en 122.

Recordatorio de los splits (contexto en `next-steps.md` 6.0):

- **D1** — solo tráfico *normal* del train → entrena el modelo de **anomalías**.
- **D2** — test completo (normal + ataques, incluidos tipos nunca vistos) → **evaluación** final.
- **D3** — solo *ataques conocidos* del train → entrena el modelo de **firmas**.

---

## 2. Ficheros de datos (CSVs)

Todos comparten el prefijo `specialized_nsl_kdd_`.

### 2.1 Datos originales (sin procesar)

| Fichero | Contenido | Sección de la memoria |
|---|---|---|
| `..._original_D1_normal_for_anomaly.csv` | Filas crudas de D1 (41 columnas NSL-KDD + etiquetas) | 4.2.1 (análisis previo de la BD) / 4.3.6 (división) |
| `..._original_D2_complete_test.csv` | Filas crudas de D2 | ídem |
| `..._original_D3_known_attacks_for_signatures.csv` | Filas crudas de D3 | ídem |

Sirven de referencia/trazabilidad: permiten reconstruir cualquier fila procesada y auditar el
preprocesado. Los modelos **no** leen de aquí.

### 2.2 Datos procesados (los que consumen los modelos)

Por cada split hay tres ficheros:

| Sufijo | Contenido |
|---|---|
| `..._processed_X_<split>.csv` | Matriz de características **ya preprocesada**: one-hot + MinMax [0,1] + **selección a 54 features** (la variante con prefijo `..._sin_seleccion_` conserva las 122, para el experimento H1) |
| `..._processed_y_attack_<split>.csv` | Etiqueta de ataque específico (label-encoded, 40 clases; mapping en `_mappings_and_info.txt`) |
| `..._processed_y_category_<split>.csv` | Etiqueta de categoría (5 clases: NORMAL/DOS/PROBE/R2L/U2R) |

Dimensiones actuales (verificadas por `specialized_nsl_kdd_validation_report.txt`):

| Split | Filas × columnas de X | Uso |
|---|---|---|
| D1 | 67.343 × 54 | Entrenamiento anomalías |
| D2 | 22.544 × 54 | Evaluación |
| D3 | 58.630 × 54 | Entrenamiento firmas |

> Importante: los CSVs de X ya llevan aplicada la selección de características, así que
> `anomalias.py`/`firmas.py` no tienen que saber nada de la selección — cargan y entrenan.

**Destino en la memoria:** 4.3 (preprocesamiento) en general; la división D1/D2/D3 en **4.3.6**.

### 2.3 `specialized_nsl_kdd_transformers.joblib`

Transformadores ajustados y persistidos para inferencia reproducible: `scaler` (MinMax ajustado
en D1+D3), `label_encoder`, `category_encoder`, la lista `feature_columns` —la **final, tras la
selección** (54)— y `feature_columns_pre_seleccion`, que es la post one-hot (122).
Se carga con `joblib.load(...)`. **Destino:** 4.3.2 (normalización) y reproducibilidad (4.6 / apéndices).

### 2.4 Los dos `..._vocabulario_onehot.csv` (los genera `validacion.py`)

Artefacto que **respalda en disco el delta 77 → 122** del fix del one-hot del 2026-07-05, que
antes solo vivía en prosa. Una fila por columna categórica (`protocol_type`, `service`, `flag`)
más una fila `__total__` con los agregados:

| Columna | Qué es |
|---|---|
| `variante` | `con_seleccion` / `sin_seleccion` |
| `medido` | `True` si se pudo recontar; si es `False`, `motivo` dice por qué y el resto va **vacío** (nunca cifras inventadas) |
| `categorias_en_D1` | categorías de esa columna presentes **solo en D1** |
| `categorias_union_D1_D3` | categorías en la **unión D1+D3** (el vocabulario actual) |
| `recuperadas` | la diferencia: dummies que el alineamiento buggy perdía |
| `n_numericas`, `total_solo_d1`, `total_union`, `delta_total` | agregados; **solo en la fila `__total__`**, vacíos en las demás |
| `total_union_transformers` | contraste **independiente**: `len(feature_columns_pre_seleccion)` leído del `..._transformers.joblib` |
| `commit`, `fecha` | procedencia de la corrida, **al final de la fila**; mismo mecanismo y misma convención `-sucio` que la columna `commit` de los `metricas_*.csv` (`config.commit_actual()`). **Presentes en el CSV que hay en disco desde la corrida del 2026-08-11 20:53** (sello `fc1c6b4-sucio`): ver el aviso de abajo sobre qué vale y qué no vale ese sello |

> El sufijo **`-sucio`** de un sello dice que al correr había cambios sin commitear en
> `Implementacion/`, de modo que el hash es el del commit **anterior** al código que produjo el
> artefacto. Los tres valores posibles (`<hash>` · `-sucio` · `-suciedad_desconocida`) están
> tabulados en `Implementacion/PIPELINE.md`, sección «El sello `commit`: tres valores posibles»,
> que es la definición canónica: aquí no se duplica.

Cifras publicadas (idénticas en los dos ficheros, ver abajo): **38 numéricas + 39 dummies = 77**
frente a **38 + 84 = 122**, `delta_total` = **+45**, todas de `service` (**+44**) y `flag`
(**+1**); `protocol_type` no aporta ninguna. El contraste con el joblib da también **122**.

Tres avisos para citarlo:

- **El 77 es una RECONSTRUCCIÓN, no una observación.** Se recuenta hoy sobre el D1 de la corrida
  en curso simulando el alineamiento anterior al fix; coincide con lo que aquel producía **por
  construcción**, no por medición. No se puede escribir «observado en la corrida anterior al fix».
  **El `..._validation_report.txt` lo rotula así** (línea «La primera es una RECONSTRUCCIÓN…»,
  `validacion.py:1219-1229`), y también la consola. **El CSV NO lo rotula**: ahí la cifra vive en
  `total_solo_d1` = `77` sin marca alguna. Por eso, cuando se cite el número desde el CSV hay que
  arrastrar **siempre** este aviso a mano.
- **Los dos ficheros traen las mismas cifras**, y es correcto: la medición se hace sobre los CSV
  `_original_*`, y la selección de características actúa **después** del one-hot. Es la única
  salida de `validacion.py` que no depende de la variante.
- **El CSV que hay en disco YA lleva `commit` y `fecha`**, igual que los `metricas_*.csv`. El
  código las escribe desde el 2026-08-11 (`validacion.py` importa `config.py` y llama a
  `config.commit_actual()`) y las dos variantes **ya se re-corrieron**: los ficheros publicados
  salen de la corrida del **2026-08-11 a las 20:53**, con sello `fc1c6b4-sucio` y, en cada fila, la
  fecha de **su propia** invocación: `2026-08-11T20:53:27` en el CSV de la variante de 54 y
  `2026-08-11T20:53:46` en el de 122. La cabecera de los dos `..._validation_report.txt` trae **el
  mismo commit y esa misma marca por variante** (`:27` en la de 54, `:46` en la de 122): el commit
  sí es común a los cuatro artefactos, la fecha no, porque se captura una vez por invocación. Al
  citar, copiar los segundos del fichero que se está citando. **Esas columnas se pueden y se deben citar**: son
  la procedencia que viaja dentro del artefacto y sobrevive a un `clone`, al contrario que el
  mtime. Con una salvedad: un sello `-sucio` **no identifica la versión del código** —el hash es
  el del commit **anterior** al cambio y `-sucio` solo dice «difería, no se sabe en qué»—, así que
  aporta fecha fiable y aviso explícito de **no-reproducibilidad desde ese hash**, pero no permite
  reconstruir el código que lo produjo. Para eso manda el recuadro de anclaje de
  `Implementacion/PIPELINE.md`, que ya lo declara: el commit de cierre de ese ciclo es
  **`9af842c`**, que versiona a la vez `validacion.py` y los cuatro artefactos y es el último que
  toca ese script, así que el sello impreso `fc1c6b4-sucio` corresponde al estado de
  `validacion.py` **en `9af842c`**.

Son recuentos, así que se publican como **enteros** (`77`, no `77.0`).

**Destino en la memoria:** **4.3.3** (codificación de variables categóricas) como respaldo del
delta, y 4.6 / apéndices.

---

## 3. Ficheros de texto (metadatos y reportes)

### 3.1 `selected_features.txt`

Salida del paso **4.3.5 Selección de características** (calculado sobre D1+D3 tras el escalado,
ranking con `RandomForestClassifier(n_estimators=100, random_state=42, class_weight='balanced')`
sobre `y_category`). Contiene 4 bloques:

1. **Las 54 features conservadas**, ordenadas por importancia RF con importancia individual y
   acumulada (el top-54 acumula el **99,9 %** de la importancia total). Las 3 primeras:
   `src_bytes` (0,091), `dst_host_srv_count` (0,075), `dst_bytes` (0,066).
2. **1 eliminada por varianza ~0**: `num_outbound_cmds` (varianza exactamente 0).
3. **7 eliminadas por correlación > 0,95** (se conservó la de mayor varianza de cada par; p. ej.
   `serror_rate` y `srv_serror_rate` caen a favor de `flag_S0`).
4. **60 eliminadas por importancia** (fuera del top-99,9 %; casi todas dummies de `service_*` raras).

Cuenta: 122 de partida − 1 − 7 − 60 = **54 finales**. (El umbral es 99,9 %, no 99 %: el corte al
99 % daba 40 features y eliminaba indicadores clave para la detección 0-day — hallazgo H1 de la
auditoría de 2026-07-05; decisión final validada por el experimento H1 el 2026-07-15.)

**Destino en la memoria:** **4.3.5** (tabla de features conservadas + criterios; el bloque de
eliminadas puede ir a apéndice).

### 3.2 Los dos `..._validation_report.txt`

Resumen de `validacion.py`. **Son dos ficheros, uno por variante**, y no comparten ninguna de las
cifras que dependen del set de características (sí coinciden, obviamente, en las que no dependen
de él: tamaños de los splits, normales de D2 y las 4 características fuera de [0,1]):

| Fichero | Variante | Características | Drift (A) | Drift (B) | Media outliers D1 (entre características) | Baja varianza | Alta correlación |
|---|---|---|---|---|---|---|---|
| `specialized_nsl_kdd_validation_report.txt` | **54** (la del TFG) | 54 | **37** | **25** | **4,78 %** | 0 | 0 pares |
| `specialized_nsl_kdd_sin_seleccion_validation_report.txt` | 122 (experimento H1) | 122 | **44** | **31** | **2,44 %** | 1 | 14 pares |

Las dos últimas columnas son la comprobación de que la selección 4.3.5 hizo su trabajo: lo que en
122 son 1 feature de varianza ~0 y 14 pares correlacionados, en 54 es 0 y 0. **Salvo que se diga
lo contrario, las cifras de esta guía son las del informe de 54**, que es el set del TFG
(decisión Q1/C).

**Qué contiene, por orden:** *(desde la re-corrida del 2026-08-11 20:53: dos líneas de procedencia,
`Commit del código:` y `Fecha de la corrida:`, justo tras el título —**presentes en los dos ficheros
que hay en disco**; el detalle, en el aviso al final de este apartado y en §2.4)* · el titular de integridad y tamaños · las dos mediciones de drift y su
comparación · las recomendaciones (**solo si hay alguna**) · las características de D2 fuera de
[0,1] · **los tipos 0-day de D2 nominalmente** · **el vocabulario del one-hot (delta 77 → 122)**.
Los dos últimos son bloques **nuevos de la re-corrida del 2026-08-11** y se describen al final de
este apartado; el del vocabulario tiene además CSV propio (**§2.4**).

Cómo leerlo (los rótulos son idénticos en ambos ficheros, salvo el bloque de recomendaciones, que
el de 54 no imprime):

- `Integridad: APROBADA` → dimensiones, alineación de columnas, ausencia de nulos/inf, pureza de
  D1 (solo normal) y D3 (solo ataques) correctas. Si dice FALLA, no entrenar nada. **Aprobada en
  los dos informes.**
- Tamaños de los splits (67.343 / 22.544 / 58.630, iguales en ambas variantes) y el número de
  características, que es lo único que las distingue: **54** o **122**.
- `Drift (A) D1 vs D2 COMPLETO: 37 características`
  (`specialized_nsl_kdd_validation_report.txt`; **44** en el `_sin_seleccion_`) → 37 de 54
  features cambian de distribución
  entre train normal y test completo (test KS, p<0,01). Es **esperado y deseable**: D2 contiene
  ataques y tipos nuevos; ese drift es justo lo que el detector de anomalías debe captar. Incluye
  el top-15 por estadístico KS (`src_bytes` 0,346, `dst_bytes` 0,317…).
- `Drift (B) D1 vs D2 SOLO NORMALES: 25 características`
  (`specialized_nsl_kdd_validation_report.txt`; **31** en el `_sin_seleccion_`) → **la medición
  de la tarea T2**, añadida
  sin sustituir a la anterior. Compara D1 contra las **9.711 filas normales de D2**: tráfico
  legítimo contra tráfico legítimo, así que lo que mide **no** puede achacarse a que en el test
  haya ataques. Es la cifra que puede explicar por qué un umbral p95 ajustado en D1_val promete
  ≈5 % de FPR y sobre D2 rinde 8-10 %.
  - **Es desplazamiento ENTRE PARTICIONES, nunca «deriva temporal»**: NSL-KDD no tiene marca de
    tiempo.
  - El informe publica además un bloque `(A) vs (B)` con `delta = (A) − (B)`. Es una
    **comparación** de las dos mediciones sobre las mismas características, **no** un reparto de
    causas: el estadístico KS es un supremo de diferencia de CDF y **no es aditivo sobre una
    mezcla**, así que (A) no se descompone en (B) más un «aporte de los ataques». La salvedad va
    impresa en el propio `.txt`, bajo el rótulo del bloque: quien abra el artefacto suelto la
    tiene delante sin necesidad de esta guía.
- `Baja varianza: 0` y `Alta correlación: 0 pares` **en el informe de 54** → confirma que la
  selección 4.3.5 ya limpió ambos problemas (ese reporte se genera *después* de la selección). El
  `_sin_seleccion_` es el antes: **1** feature de varianza ~0 (`num_outbound_cmds`) y **14** pares
  por encima de 0,95, y por eso **es el único que trae bloque `Recomendaciones:`**, con dos.
  - En el informe de **54** las cuatro condiciones que generan recomendaciones son falsas, así que
    **el bloque no aparece en absoluto** — ni el encabezado. Es deliberado: antes se imprimía el
    rótulo con nada debajo y en un artefacto que se lee suelto eso se interpreta como que se perdió
    algo. **Su ausencia significa «ninguna», no «faltan datos».**
- `D2 fuera de [0,1]: 4 características (informativo)` → **las mismas cuatro en los dos
  informes**: `num_shells` (máx. 2,50), `num_file_creations` (2,33), `duration` (1,35) y `hot`
  (1,31). **No es un error**: el scaler se
  ajusta solo en train (D1+D3); re-ajustarlo con el test sería leakage. Vigilar su efecto en el
  autoencoder (FPR).

Los **dos bloques nuevos del final** (re-corrida del 2026-08-11), **idénticos en los dos
informes** porque ninguno depende del set de características:

- `Tipos de ataque 0-day en D2 (presentes en D2, ausentes de D3): 17` → la tabla **nominal** de los
  0-day, con su categoría y sus instancias, y el total: **3.750 instancias, el 16,63 % de D2**. Los
  cuatro mayores son `mscan` (996, probe), `apache2` (737, dos), `processtable` (685, dos) y
  `snmpguess` (331, r2l). Antes esta lista solo salía por consola y no quedaba en ningún artefacto.
  - La lista es **emergente**: se calcula como diferencia de conjuntos entre las etiquetas de D2 y
    las de D3, **nunca** desde una lista escrita a mano. Es el respaldo del recall 0-day por tipo
    de `metricas_baseline_0day.csv` y `metricas_hibrido_0day.csv`: **solo el detector de anomalías
    puede verlos**, porque el clasificador de firmas no ve ni una muestra suya en D3.
  - **Los 17 tipos no son las 36 filas** de `metricas_baseline_0day.csv` ni las 144 de
    `metricas_hibrido_0day.csv`: esas tablas multiplican por variante y por detector.
- `Vocabulario del One-Hot — delta del fix del 2026-07-05` → **77 → 122 características** (38
  numéricas + 39 dummies frente a 38 + 84), `Delta = +45`, con el desglose por columna categórica
  y el contraste independiente contra `feature_columns_pre_seleccion` del joblib. Es el **respaldo
  en disco** del delta que antes solo estaba en prosa, y tiene CSV propio: **§2.4**, donde están
  los tres avisos para citarlo (empezando por que **el 77 es una reconstrucción**, no una cifra
  observada en la corrida anterior al fix).

> **Los dos informes que hay en disco imprimen `commit` y `fecha` en su cabecera** (tras el
> título, antes de `Integridad:`), igual que los `metricas_*.csv` desde T1. Los publicados salen de
> la re-corrida del **2026-08-11 a las 20:53**: en
> `specialized_nsl_kdd_validation_report.txt`, los campos `Commit del código:` y
> `Fecha de la corrida:` dicen `fc1c6b4-sucio` y `2026-08-11T20:53:27` (se citan **por su nombre
> de campo**, no por su número de línea: el informe es regenerable y una re-corrida que cambie el
> alto de la cabecera desplazaría la referencia). **Residuo
> cerrado.** Queda el límite propio del sufijo: un sello `-sucio` **no identifica la versión del
> código** (el hash es el del commit *anterior* al cambio; `-sucio` solo dice «difería, no se sabe
> en qué»), así que da fecha fiable y aviso de **no-reproducibilidad desde ese hash**, y de qué
> versión salieron lo declara el recuadro de trazabilidad de `Implementacion/PIPELINE.md`: el
> commit de cierre es **`9af842c`**, que versiona a la vez el script y sus cuatro artefactos.

**Destino en la memoria:** **4.2.1** (análisis previo de la BD) y apoyo metodológico en 4.3.2.
Si a la memoria va una cifra de este apartado, va con el nombre de su fichero: la variante de 122
es material del experimento H1, no del sistema publicado.

### 3.3 `specialized_nsl_kdd_mappings_and_info.txt`

Diccionario de referencia de las etiquetas:

- Mapping **entero → ataque específico** del LabelEncoder (40 tipos: 0=apache2 … 39=xterm).
- Mapping **entero → categoría** (0=DOS, 1=NORMAL, 2=PROBE, 3=R2L, 4=U2R).
- Mapping **ataque específico → categoría** (qué ataques componen cada categoría).

Imprescindible para interpretar los CSVs de `y_attack`/`y_category` y las futuras matrices de
confusión. **Destino:** **Apéndice A.1** (columnas y etiquetas del NSL-KDD).

### 3.4 `specialized_nsl_kdd_usage_guide.txt`

Chuleta autogenerada por `program.py`: lista de ficheros generados, qué split usar para cada
modelo y snippets de `pd.read_csv(...)` con las rutas reales. Es documentación operativa, **no va
a la memoria** (como mucho, inspiración para el Apéndice de manual de uso).

---

## 4. Figuras (`figuras/`)

Todas en PNG, tituladas en español, listas para insertarse en la memoria.

> **Las seis figuras de `validacion.py` (4.2 a 4.5) existen por duplicado**: el nombre sin sufijo
> es la variante de **54** —la del TFG, la que se describe abajo— y el nombre acabado en
> `_sin_seleccion` es la de **122** (experimento H1). Son **12 ficheros**. La única de esta
> sección que **no** tiene gemela es `eda_distribuciones_divisiones.png` (4.1), de `program.py`.

### 4.1 `eda_distribuciones_divisiones.png` (generada por `program.py`)

Panel 3×3 del EDA de los splits:

| Panel | Qué muestra | Qué se concluye |
|---|---|---|
| D1: solo Normal | Una única barra (~67k) | D1 es puro: apto para one-class learning |
| D2: test completo | Barras normal/dos/r2l/probe/u2r | Test realista: ~43 % normal, ataques variados (r2l pesa más que en train) |
| D3: ataques | dos ≫ probe ≫ r2l ≫ u2r | El desbalance que obliga al paso 4.3.4 |
| Comparación de tamaños | D1 vs D2 vs D3 (escala log) | D2 es mucho menor que el train; sin solape |
| Top 8 ataques en D3 | `neptune` domina (~41k), luego satan, ipsweep… | Un solo tipo DoS concentra la mayoría del train de firmas |
| Distribución % D2 vs D3 | Barras por categoría | El test **no** replica el train: en D3 dos ≈ 78 %, en D2 ≈ 33 %; r2l casi ausente en train pero relevante en test |
| Promedios en D1 | duration, src_bytes, dst_bytes, count (log) | Escalas muy dispares → justifica el escalado |
| Correlación en D3 | Heatmap 5 features básicas | `count`/`srv_count` correlacionan; el resto casi independiente |
| Cobertura de tipos de ataque | Pastel: 52,5 % comunes · 42,5 % solo prueba · 5 % solo entrenamiento | **El dato estrella**: casi la mitad de los tipos de ataque del test no existen en el train → escenario "0-day" real |

**Destino:** **4.2.1** (análisis previo de la BD); el pastel de cobertura se retoma en 5.3 (0-day).

### 4.2 `validacion_distribucion_clases.png` (por `validacion.py`)

Tres barras, una por split (D1 solo normal · D2 con las 5 categorías · D3 con las 4 de ataque).
Versión limpia y compacta del reparto de clases; confirma visualmente la pureza de D1/D3 y el
desbalance de D3. **Destino:** **4.2.1** o **4.3.6** (elegir esta o los paneles equivalentes del EDA,
no duplicar).

### 4.3 `validacion_discriminantes_d1_vs_d3.png`

Rejilla 3×4 de histogramas superpuestos (verde = D1 normal, rojo = D3 ataques) de las 12 features
que mejor separan normal de ataque: `flag_SF`, `logged_in`, `same_srv_rate`, `dst_host_srv_count`,
`dst_host_same_srv_rate`, `flag_S0`, `service_http`, `service_private`, `dst_host_count`, `count`,
`srv_rerror_rate`, `dst_host_rerror_rate`.

Cómo leerla: cuanto menos se solapan verde y rojo, más discriminante es la feature. Ejemplos claros:

- `flag_S0` (conexión sin respuesta): casi exclusiva de ataques → firma natural de SYN flood (neptune).
- `flag_SF` y `logged_in`: concentradas en 1 para tráfico normal, en 0 para ataques.
- `same_srv_rate`: normal ≈ 1, ataques repartidos cerca de 0.

**Destino:** **4.2.1** como análisis, y **4.5** como justificación de las reglas/firmas explícitas
(estas features son las candidatas a umbrales interpretables).

### 4.4 `validacion_drift_ks.png`

Dos paneles del test de Kolmogorov-Smirnov D1 vs D2:

- **Izquierda:** top-20 features por estadístico KS (rojo = drift significativo). `src_bytes` y
  `dst_bytes` encabezan.
- **Derecha:** histograma de p-values con la línea p=0,01: **37** features caen a la izquierda
  (drift), unas pocas quedan cerca de 1 (sin drift).

Conclusión: el test se distribuye de forma distinta al tráfico normal de entrenamiento en el
**68,5 %** de las features (**37 de 54**) — coherente con que D2 mezcla ataques y tipos nuevos.
La cifra es la misma que publica `specialized_nsl_kdd_validation_report.txt` en
`Drift (A) D1 vs D2 COMPLETO: 37 características` y la que ya recoge la sección 3.2 de esta guía.
Su gemela `validacion_drift_ks_sin_seleccion.png` va con
`specialized_nsl_kdd_sin_seleccion_validation_report.txt` y dice
**44 de 122** (36,1 %): es la **misma medición sobre otra variante**, no una segunda medición de
drift (A) sobre el set del TFG — de esa solo hay una. **Destino:** **4.2.1**
(caracterización train/test) y argumento de contexto en 5.1.

### 4.4-bis Las dos figuras del KS contra los normales de D2 (T2)

- **`validacion_drift_ks_d2_normales.png`** — misma estructura que la anterior (top-20 por KS +
  histograma de p-values) pero con la medición **(B)**: D1 contra las 9.711 filas normales de D2.
  Rótulos propios para que las dos figuras **no se puedan confundir** al mirarlas en la memoria.
- **`validacion_drift_ks_comparativa.png`** — las dos KS **una al lado de la otra** para el top-20
  por KS contra D2 completo. Cómo se lee: cuál de las dos mediciones es mayor en cada
  característica y por cuánto. **Cómo NO se lee:** como una descomposición del drift en «lo que
  aportan los normales» y «lo que aportan los ataques» — esa resta no es una magnitud.

Las dos existen también con sufijo `_sin_seleccion` (variante de 122), como las otras cuatro. La
cifra de drift (B) que acompaña a las **sin sufijo** es **25 de 54**
(`specialized_nsl_kdd_validation_report.txt`); la de las `_sin_seleccion` es **31 de 122**
(`specialized_nsl_kdd_sin_seleccion_validation_report.txt`). **Destino:** **5.1** (el
desplazamiento D1→D2 como contexto del FPR) y **5.4**.

### 4.5 `validacion_outliers_iqr.png`

Barras agrupadas: % de outliers (criterio IQR) por feature (top-15 de D1), comparando D1/D2/D3.
Media de outliers en D1 **entre características** (el criterio IQR da un porcentaje por
característica y esta cifra es su media aritmética, no su mediana): **4,78 %**, dato de
`specialized_nsl_kdd_validation_report.txt` (variante de 54, la del TFG). La gemela
`validacion_outliers_iqr_sin_seleccion.png` va con
`specialized_nsl_kdd_sin_seleccion_validation_report.txt`, cuya media es **2,44 %**. Las dos
cifras **no son comparables y no se mezclan en la misma frase**: son la media sobre dos
poblaciones distintas de características (54 y 122), no la misma magnitud medida dos veces. Por
qué una es casi el doble que la otra **no está medido en ningún artefacto**; si hiciera falta
afirmarlo, hay que medirlo primero. Cómo leerla: features donde D3 dispara
los outliers frente a D1 (p. ej. `src_bytes`, `dst_host_diff_srv_*`, `dst_host_rerror_*`) señalan
comportamiento de ataque; niveles altos también en D1 recuerdan que el tráfico normal tampoco es
"limpio" (colas largas), relevante para fijar el umbral del detector de anomalías. **Destino:**
**4.2.1**.

---

## 5. Los datos clave que cuentan la historia

Resumen de la narrativa del preprocesado (con su artefacto de origen):

1. **One-hot con vocabulario D1+D3 → 122 features.** El fix del bug del one-hot (vocabulario =
   unión del train, no solo D1) subió de 77 a **122** features (38 numéricas + 84 dummies),
   recuperando **+45 dummies exclusivas de tráfico de ataque** — justo las señales que el modelo
   de firmas necesitaba. *(Delta documentado en `next-steps.md` 6.1 → sección 4.3.3 de la memoria.)*
2. **Selección 122 → 54 features.** Tres filtros encadenados: 1 por varianza ~0 + 7 por
   correlación > 0,95 + 60 por importancia; el top-54 acumula el **99,9 %** de la importancia RF.
   Validada por el experimento H1 (54 vs 122, 2026-07-15): 54 para ambas etapas.
   *(`selected_features.txt` → 4.3.5.)*
3. **Splits finales:** D1 67.343×54 · D2 22.544×54 · D3 58.630×54, integridad APROBADA.
   *(`specialized_nsl_kdd_validation_report.txt` → 4.3.6.)*
4. **Desbalance extremo en D3:** dos ~45,9k vs u2r ~52 → ratio ≈ **883:1**. Motiva el
   mini-experimento SMOTE vs `class_weight` (4.3.4) y el uso de `f1_macro`.
   *(Visible en el EDA y en `validacion_distribucion_clases.png`.)*
5. **17 tipos de ataque de D2 no existen en el train** (el 42,5 % de los tipos del test, panel
   "Cobertura" del EDA; `validacion.py` los lista **nominalmente en su informe** desde la
   re-corrida del 2026-08-11, además de por consola — ver §3.2). Son los "0-day" del experimento:
   indetectables por firmas, solo la etapa de anomalías puede cazarlos → argumento central del
   sistema híbrido (5.3).
6. **4 features de D2 quedan fuera de [0,1]** tras el escalado (`num_shells`,
   `num_file_creations`, `duration`, `hot`). Esperable: el scaler se ajusta solo en train para
   evitar leakage; el test puede desbordarlo. Se documenta como decisión metodológica, no como fallo.

---

## 6. Artefactos de los modelos (todos EXISTEN desde 2026-07-15)

Cada artefacto existe en dos variantes: set primario **54** y `_122_sin_seleccion` (experimento H1).
La decisión Q1/C (2026-07-15) fijó el **54** como set del TFG.

| Artefacto | Lo genera | Sección de la memoria |
|---|---|---|
| `modelos\anomalia_<algo>_<set>.joblib` (modelo + umbral p95 + config, ×4) | `anomalias.py` | 4.4 |
| `metricas_anomalias.csv` (fila por algoritmo y variante) | `anomalias.py` | **5.1** (5.1.2 tabla de métricas) |
| `figuras\anomalias_<set>_roc/pr.png` + `figuras\anomalias_cm_<algo>_<set>.png` | `anomalias.py` | 5.1 (5.1.1 matrices) |
| `metricas_balanceo.csv` (SMOTE vs `class_weight`/nada, f1_macro CV) | `firmas.py` | **4.3.4** |
| `modelos\firma_<algo>_<set>.joblib` (×4) | `firmas.py` | 4.5 |
| `firmas_reglas_54.txt` / `firmas_reglas_122_sin_seleccion.txt` (reglas del DecisionTree) | `firmas.py` | **4.5** (3-4 reglas comentadas) |
| `metricas_firmas.csv` + `figuras\firmas_cm_<algo>_<set>.png` | `firmas.py` | **5.2** (5.2.3 = comparativa) |
| `metricas_baseline.csv` + `metricas_baseline_0day.csv` + `figuras\baseline_cm_<set>.png` | `baseline.py` | **5.3** (comparación vs RF monolítico) |
| `metricas_hibrido.csv` (binaria H-5, conocidas, conservador) | `hibrido.py` | **5.3** |
| `metricas_hibrido_calibracion.csv` (sensibilidad de los 3 `UMBRAL_CONF`, OOF + D2) | `hibrido.py` | 5.3 (calibración τ=2pp) |
| `metricas_hibrido_0day.csv` (recall 0-day por tipo × 4 detectores + FPR; ojo filas `__global__`) | `hibrido.py` | **5.3** (análisis 0-day; cerró H1) |
| `figuras\hibrido_cm_<set>.png` (matriz 5×6 con `unknown`) | `hibrido.py` | 5.3 (H-6) |
| `modelos\hibrido_<set>.joblib` (descriptor: joblibs usados + umbral + τ) | `hibrido.py` | reproducibilidad (4.6/apéndices) |
| `metricas_cascada_invertida.csv` (5 filas por variante: 4 categorías + `__global__`) | `cascada_invertida.py` | **3.2.2** (por qué las anomalías van primero) |
| `figuras\cascada_invertida_<set>.png` (barras apiladas condenadas / bajo umbral) | `cascada_invertida.py` | **3.2.2** |

### 6.1 Cómo se cita `metricas_cascada_invertida.csv` (tarea T3)

Mide qué haría la **etapa 2** con el tráfico legítimo **si fuese la primera**: pasa las 9.711
filas normales de D2 por el clasificador de firmas ya entrenado y cuenta cuántas conservarían
etiqueta de ataque con confianza `>= UMBRAL_CONF`. Es **contrafactual** —en el sistema real esas
filas nunca llegan a la etapa 2— y **no es comparable** con ninguna columna de
`metricas_firmas.csv` ni de `metricas_hibrido.csv`.

- **Lo citable:** `n_condenadas` son los falsos positivos **irrecuperables** — **6.558 de 9.711**
  a 54 características y **3.329** a 122 (corrida `274923d-sucio`, `UMBRAL_CONF = 0,5`).
- **Lo que NO es:** la `tasa_condena` de `__global__` **no** es «el FPR de un sistema de
  firmas-primero», es una **cota inferior**. En este TFG `unknown` es **alarma**, no `normal`
  (decisión P-5), así que los 3.153 / 6.382 flujos que caen bajo el umbral **no quedan
  exonerados**: pasarían a la etapa siguiente.
- La lectura completa, el desglose por categoría y las salvedades para contrastarlo con el FPR del
  híbrido están en `Implementacion\PIPELINE.md`, sección **«La cascada invertida (T3)»**, anclados
  al commit de su corrida.

> Las tres viñetas de arriba son un **resumen derivado** de ese bloque de `PIPELINE.md`, que es la
> fuente. Hay otras dos copias (el docstring de `cascada_invertida.py` y la celda `alcance` del
> CSV) y `PIPELINE.md` las lista. Si el argumento de la cota inferior cambia —depende de la
> decisión **P-5**—, se reescribe allí y **se propaga aquí**, no al revés.

> Las notas del vault `04 Implementación del sistema\` y `05 Evaluación\` (volcado 2026-07-15/16)
> ya consumen estos artefactos; las figuras están copiadas en `Obsidian_TFG_Vault\assets\`.

### 6.2 Los artefactos del barrido de semillas (tarea T4) — **corrido y agregado el 2026-08-12/13**

Los cinco scripts de modelos aceptan **`--semilla N`**. Sin el flag la semilla es **42** y todo lo
descrito arriba se produce con su nombre de siempre; **todo lo publicado en esta carpeta es de la
semilla 42**. Con cualquier otra semilla la corrida se desvía en dos sitios y no toca nada de lo
anterior:

| Qué | Semilla 42 (lo publicado) | Semilla N ≠ 42 (el barrido) |
|---|---|---|
| `.joblib`, figuras, `firmas_reglas_*.txt` | nombre de siempre | sufijo `_semilla<N>` |
| Las nueve tablas de métricas | `metricas_<x>.csv` | `metricas_<x>_semillas.csv` (la publicada **no la abre ningún script de modelos**; el **agregador** sí, en lectura — ver más abajo) |

**El barrido ya corrió** (2026-08-12 22:09 → 00:38, sello `commit = df30cb2` limpio; sus nueve tablas
quedaron versionadas en `9ad971b`) y **ya se agregó**
(2026-08-13). El agregador se ha ejecutado **tres veces**, todas con cero `fit` —solo lee CSV—: la
primera en **7,2 s**; la segunda en **1,70 s**, con el arreglo de `_tabla_md()` que añade las
columnas `Tabla de origen` y `Alcance` (sello `commit_agregador = df30cb2-sucio`, cabecera
`2026-08-13T07:43:40`); y la tercera con el **titular automático** —las cuatro columnas `*_42` y el
recuento «13 de 98», que antes se calculaba a mano—. **Los dos ficheros de dispersión que hay en
disco son los de la tercera**: cabecera `2026-08-13T19:54:48` y
`commit_agregador = ddade37-sucio`, verificado en disco el 2026-08-13.

Esos sellos **no se retocan ni se regeneran** —por la razón estructural que explica
`Implementacion\PIPELINE.md`: un artefacto que estampa `config.commit_actual()` no puede llevar el
hash del commit que lo versiona, porque ese commit todavía no existe cuando el artefacto se
escribe—, así que el desajuste se resuelve **en prosa**, sello a sello y sin borrar el historial:

- **Segunda pasada, re-anclada:** `df30cb2-sucio` → **`9ad971b`**, el commit de cierre del cómputo de
  T4, que versiona a la vez `agregar_semillas.py`, las nueve tablas del barrido y los dos ficheros de
  dispersión. Ese re-anclaje **sigue siendo válido para lo que nombra** —aquella pasada—, aunque su
  sello ya no sea el que hay en disco. Fue el **tercer** re-anclaje del proyecto, tras
  `fc1c6b4-sucio` → `9af842c` y `00c3c3e-sucio` → `54d1349`.
- **Tercera pasada, PENDIENTE de re-anclaje:** `ddade37` es el commit **anterior** al cambio, así que
  el sello `ddade37-sucio` no identifica la versión que produjo la agregación; el commit de cierre
  que sí lo hará **todavía no existe** y aquí no se inventa ningún hash. Se completará cuando exista.

Y el `-sucio` no contamina las bandas, que las respalda `commits_origen = df30cb2` limpio. Lo que sí
hay que declarar al citar el titular es otra cosa: **titular y banda no salen del mismo commit**
(`commit_semilla_42` es `1163c90`, o `274923d-sucio` en la cascada invertida, frente a
`commits_origen = df30cb2`). Lo que hay en disco:

- **`verificacion_semilla_joblib.txt`** — la lista de los **20** `.joblib` publicados con la semilla
  que declara cada uno. Lo genera `python app\barrido_semillas.py --solo-verificar`, que **no entrena
  nada**: solo lee los descriptores. Veredicto, el mismo en sus dos pasadas: los 20 declaran
  `semilla = 42` (todos con `commit=1163c90`). El fichero en disco es el que **re-selló el preflight
  del barrido** (cabecera `Commit del código: df30cb2`, `2026-08-12T22:07:10`), no el de la pasada de
  las 15:57 — el runbook cuenta por qué en `Implementacion\PIPELINE.md`. Sostiene dos afirmaciones que
  el barrido necesita: que una corrida por defecto pasa la salvaguarda de mezcla de semillas, y que el
  borrado por sufijo del lanzador **no puede alcanzar** ninguno de esos 20 ficheros.

- **nueve `metricas_*_semillas.csv`** — mismas columnas que su tabla publicada, con `semilla` como
  parte de la identidad de la fila; **2.320 filas** entre las nueve. **Se versionan** (texto plano).
- **`dispersion_semillas.csv` y `dispersion_semillas.md`** — la agregación (`n`, media, **sd
  muestral `ddof=1`**, mín, máx a 4 decimales) por variante × algoritmo × alcance × métrica, con las
  columnas de tiempo en **bloque aparte** rotulado como dispersión de máquina: **198 filas**, 98 de
  calidad + 100 de dispersión de máquina. El `.md` es la tabla ya formateada para `A.3`. Las produce
  `python app\agregar_semillas.py` (sin flags, desde `Implementacion/`), que **aborta** si a alguna
  combinación le faltan semillas. Dos columnas que hay que mirar antes de citar una banda, porque el
  agregador las llena **avisando** sin abortar: `commits_origen` (los commits de las diez filas
  agregadas — **no** es `commit_agregador`, que es la del agregador y no produjo ninguno de los diez
  puntos) dice si una celda mezcla versiones del código —en esta corrida **no**: `df30cb2` único en
  las 198 filas—, y `decisiones_no_constantes` dice, con el reparto y en la misma fila que la media,
  si el `balanceo` o la `config_ganadora` no fueron los mismos en las diez semillas. Aquí **sí**:
  está poblada en **140 de las 198 filas** (15 celdas distintas). Eso no es un fallo: es material de
  `5.4`. Desde la **tercera** pasada el CSV trae además cuatro columnas del **titular**
  —`valor_semilla_42`, `dentro_banda_42`, `distancia_fuera_banda_42` y `commit_semilla_42`—, vacías a
  propósito en el bloque de máquina, y el `.md` la sección «El titular (semilla 42) frente a la
  banda» con el recuento **13 de 98**. La 42 **no entra** en ningún estadístico: es una comparación
  al lado de la banda, no un undécimo punto.
- **260 figuras `*_semilla*`**, **20 `firmas_reglas_*_semilla*.txt`** y **100 logs en
  `logs_barrido\`** — **no se versionan** (ver el `.gitignore` raíz). Del barrido no se cita ninguno
  de estos ficheros: las figuras y las reglas de la memoria son las de la semilla 42.
- **Ningún `.joblib` con sufijo `_semilla`** en `modelos\`: el lanzador los borra al cerrar cada
  semilla. Y las nueve tablas publicadas de la 42 quedaron **bit a bit idénticas**.

**Los tres titulares que hay que leer antes de citar la banda** (lectura completa, con las cifras y
sus salvedades, en `Implementacion\PIPELINE.md` → «El lanzador y el agregador del barrido» → *Lo que
dio la primera ejecución real*):

1. La **decisión de balanceo de 4.3.4 no es constante** entre semillas: `class_weight` gana en **17 de
   40** celdas de DecisionTree/RandomForest, y la `config_ganadora` del `GridSearchCV` tampoco es
   constante.
2. De los dos huecos que motivaron T4, uno **no** se cierra y el otro **sí**: firmas RF vs HGB
   (`f1_macro`, set 54) tiene **bandas solapadas** —el orden no queda establecido—, mientras que
   anomalías Autoencoder vs IsolationForest (`f1`) tiene **bandas disjuntas** y 10/10 semillas a favor
   del Autoencoder.
3. **La semilla 42 cae fuera de la banda [mín, máx] en 13 de las 98 celdas de calidad** (de esas 98,
   **10 son umbrales**: 8 de `umbral` y 2 de `umbral_conf_elegido`, que se agregan a propósito aunque
   no sean métricas sobre D2 — descontarlos daría 88 y rompería este titular, y además **uno de los
   tres empates del borde es un umbral**) —7 de
   anomalías, 5 de firmas y 1 del híbrido; baseline (8 celdas) y cascada invertida (4), todas
   dentro—, comparando contra los valores **con la precisión con la que se persistieron los CSV de
   origen** (6 decimales) y **no** contra los redondeados a 4 decimales que publica
   `dispersion_semillas.md`. **Los empates cuentan como dentro** (tres celdas en el borde
   exacto; contándolas como fuera saldrían 16). El caso a declarar: firmas 54-RF `f1_macro` 42 =
   **0,8223 > máx 0,8205**, o sea que el titular publicado del clasificador de firmas es el punto
   **más favorable** de las once corridas, no el centro (media **0,8035**); eso **no invalida el
   titular** —es el resultado real de su corrida—, pero obliga a **declarar la banda a su lado** en
   `5.2`. **Este recuento lo produce el agregador desde el 2026-08-13**: `_valor_semilla_42()` abre la
   tabla publicada homóloga **en lectura** —nunca en escritura—, casa la fila de la semilla 42 por
   clave estricta y `_recuento_titular()` emite «13 de 98» dentro de `dispersion_semillas.md`, con el
   valor de la 42 y su veredicto en cuatro columnas del CSV. *(Hasta esa fecha esta guía advertía lo
   contrario —«no lo produce ningún script… es cálculo manual», anclado a `agregar_semillas.py:29-32`,
   que hoy dice justo lo opuesto—; era cierto cuando se escribió y ha dejado de serlo.)* Si alguna de
   esas tablas se mueve, **no se recuenta a mano: se vuelve a correr el agregador**. Lista completa de
   las 13 celdas y los dos matices, en `Implementacion\PIPELINE.md`.

**Cómo se cita la dispersión:** la semilla 42 **no está** en el barrido (las diez son 1…10,
`config.SEMILLAS_BARRIDO`), así que el titular de 5.1-5.3 es un punto **independiente** de la banda
y va **al lado** de ella, nunca dentro. Y la banda mide la dispersión **de los modelos**: los splits
D1/D2/D3 y las 54 características son fijos, porque `program.py` no está parametrizado por semilla.
Detalle completo en `Implementacion\PIPELINE.md`, subsección «El andamiaje de la semilla».

---

## 7. Mantenimiento de esta guía

- **Última actualización: 2026-08-13, tercera pasada** (**cero corridas de modelos, cero `fit` y cero
  cifras alteradas**; solo texto y código de documentación). Pone al día lo que dejó desfasado la
  **automatización del titular «13 de 98»** en `agregar_semillas.py`:
  - §6.2 ya **no** dice que el recuento sea cálculo manual: lo emite el agregador, que **abre las
    nueve tablas publicadas en LECTURA** para recuperar el valor de la semilla 42 y **sigue sin
    escribir en ninguna** (la distinción lectura/escritura es la garantía, y se escribe con esas
    palabras aquí y en la tabla de §6.2).
  - Los sellos de §6.2 pasan de la **segunda** pasada del agregador (`df30cb2-sucio`,
    `2026-08-13T07:43:40`) a la **tercera**, que es la que hay en disco (`ddade37-sucio`,
    `2026-08-13T19:54:48`, verificado en el `.md` y en el CSV). El re-anclaje `df30cb2-sucio` →
    `9ad971b` **no se borra**: sigue nombrando la segunda pasada. El de la tercera queda **pendiente**
    hasta que exista su commit de cierre.
  - **Pendiente de esta misma fecha:** hay una **cuarta** regeneración prevista, la que llevará al
    `.md` la nota de que 10 de las 98 celdas son umbrales y la salvedad de que titular y banda vienen
    de commits distintos (las dos ya emitidas por el script, **ninguna de las dos en el fichero
    todavía**). Volverá a re-sellar los dos artefactos: al correrla, esta sección y §6.2 se releen
    **contra el fichero en disco**.
- **Añadido el 2026-08-13, segunda pasada** (**cero corridas, cero `fit`, cero artefactos
  regenerados y cero cifras alteradas**: solo texto). **Re-anclaje textual** del sello
  `commit_agregador = df30cb2-sucio` de `dispersion_semillas.csv`/`.md` a su commit de cierre,
  **`9ad971b`** (§1 y §6.2 de esta guía; la tabla de corridas y el recuadro del barrido en
  `Implementacion\PIPELINE.md`). Es el **tercer** re-anclaje del proyecto, tras `fc1c6b4-sucio` →
  `9af842c` y `00c3c3e-sucio` → `54d1349`, y se hace por la misma razón estructural: el sello
  impreso **dentro** de los dos artefactos **no se edita ni se regenera**, porque lo estampa
  `config.commit_actual()` y no puede llevar el hash del commit que lo versiona.
- **Añadido el 2026-08-13, primera pasada** (**cero cifras alteradas** y **cero `fit`**; pero **no** cero
  corridas: ese día se re-ejecutó `agregar_semillas.py` —solo lectura de CSV— y reescribió
  `dispersion_semillas.csv` y `.md`, que en disco son los de esa segunda pasada de 1,70 s).
  Pone al día lo que la corrida del barrido de **T4** dejó desfasado: la fila de
  `barrido_semillas.py` y la de `agregar_semillas.py` en §1 pasan de «sin correr» a **corrido**, con
  los recuentos verificados en disco (2.320 filas en las nueve `metricas_*_semillas.csv`; 198 en
  `dispersion_semillas.csv`/`.md`; 260 figuras, 100 logs y 20 ficheros de reglas por semilla; cero
  `.joblib` con sufijo `_semilla`), y §6.2 deja de estar escrita en futuro y añade los tres titulares
  del barrido —balanceo no constante, el hueco RF/HGB que **no** se cierra frente al AE/IF que **sí**,
  y las **13** celdas donde la 42 cae fuera de la banda (recuento manual, verificado celda a celda
  contra los valores crudos; una versión previa de esta guía decía 14)—. La lectura completa vive en
  `Implementacion\PIPELINE.md`; aquí solo el resumen y los recuentos de esta carpeta.
- **Añadido el 2026-08-12, tercera pasada** (cambios que exigió la auditoría del andamiaje de
  **T4**, todos aplicados **antes** de lanzar el barrido): §6.2 documenta ahora los dos avisos del
  agregador que hay que leer antes de citar una banda —mezcla de commits (`commits_origen`) y
  decisión de balanceo no constante— y añade los **20 `firmas_reglas_*_semilla*.txt`** a la lista de
  artefactos del barrido que **no** se versionan. **Cero corridas de modelos y cero cifras
  alteradas**; en aquel momento no existía todavía ninguna tabla del barrido (se lanzó esa misma
  noche).
- **Añadido el 2026-08-12, misma fecha y segunda pasada** (cierre del andamiaje de **T4**): **§6.2
  nueva** con los artefactos del barrido de semillas y las dos filas de `barrido_semillas.py` y
  `agregar_semillas.py` en la tabla de §1. **Cero corridas de modelos y cero cifras alteradas**: el
  único artefacto nuevo en disco es `verificacion_semilla_joblib.txt`, que se produce leyendo los
  descriptores de los 20 `.joblib` publicados (ni un `fit`). En esa pasada las nueve tablas
  `metricas_*_semillas.csv` y la dispersión aún **no existían**, y §6.2 se escribió en futuro a
  propósito; ya existen desde el barrido del 2026-08-12/13 y §6.2 está en presente.
- Actualización anterior: **2026-08-12** (solo texto: **cero cifras alteradas**, cero corridas, cero
  artefactos regenerados). Tres cosas, todas de trazabilidad: (1) **re-anclaje textual** del sello
  `fc1c6b4-sucio` de los cuatro artefactos de validación a su commit de cierre, **`9af842c`**
  (§2.4, §3.2 y la entrada de abajo); (2) las citas a la cabecera de los
  `..._validation_report.txt` pasan a nombrar el **campo** (`Commit del código:` /
  `Fecha de la corrida:`) en vez del número de línea, que es frágil ante cualquier re-corrida; y
  (3) **glosa de una línea del sufijo `-sucio`** en su primera aparición (§2.4), que remite a la
  tabla canónica de `Implementacion/PIPELINE.md` sin duplicarla.
- Actualización anterior: **2026-08-11** (residuos del cierre de `validacion.py`, solo rótulos,
  metadatos y documentación: **cero cifras alteradas**, cero re-entrenamientos). Lo que cambia en
  esta carpeta: **alta del artefacto `..._vocabulario_onehot.csv`** (uno por variante, §2.4 — no
  estaba inventariado en ninguna de las dos guías) y **dos bloques nuevos al final de los
  `..._validation_report.txt`**, los tipos 0-day nominales y el vocabulario del one-hot, descritos
  ya en §3.2. Además: el bloque `Recomendaciones:` **desaparece del informe de 54** cuando no hay
  ninguna (antes salía el encabezado vacío), el **77 se rotula como RECONSTRUCCIÓN** en el informe
  y en consola, y los recuentos del CSV de vocabulario se publican como **enteros** (`77`, no
  `77.0`). El anclaje de procedencia de estos artefactos está en el recuadro «Hueco de
  trazabilidad» de `Implementacion\PIPELINE.md`, reescrito en la misma pasada: los informes en
  disco son de la re-corrida del **2026-08-11 a las 20:53** (sello interno `fc1c6b4-sucio`), no de
  la de T2 del 2026-08-10. **Cerrado también** el residuo de `commit`+`fecha`: se estampan ya en la
  cabecera de los dos informes y como dos columnas del CSV de vocabulario, y están en los ficheros
  publicados. Quedaba pendiente el **re-anclaje** —el sello es `-sucio` porque al correr el ciclo
  aún no estaba commiteado—, **resuelto el 2026-08-12 por vía textual**: el commit de cierre es
  **`9af842c`** y así lo declaran hoy el recuadro de trazabilidad y la tabla de corridas de
  `Implementacion/PIPELINE.md`, además de §2.4 y §3.2 de esta guía. El sello impreso dentro de los
  artefactos **no se editó**: es una salida generada y sigue diciendo `fc1c6b4-sucio`.
- Actualización anterior: **2026-08-10** (cuarta pasada de **T2** y **T3**, solo documentación:
  cero código de modelos y cero re-entrenamientos). Sobre lo anotado en las pasadas anteriores de
  esa misma fecha, se registra el **alta de artefactos de `validacion.py`**: al correrse por
  primera vez la **variante de 122**, `Resultados/` pasa de 1 a **2** informes de validación y de
  6 a **12** figuras `validacion_*` (6 por variante), todos con marca de tiempo de esta sesión.
  Consecuencia documental: **toda cifra de validación se cita ahora con el nombre de su fichero**
  —las dos variantes no comparten ninguna cifra que dependa del set de características:
  drift (A) **37** (`specialized_nsl_kdd_validation_report.txt`) vs **44**
  (`specialized_nsl_kdd_sin_seleccion_validation_report.txt`), drift (B) **25** vs **31** y media
  de outliers entre características **4,78 %** vs **2,44 %** en esos mismos dos ficheros, por ese
  orden— y el recuadro
  «Hueco de trazabilidad» de `Implementacion\PIPELINE.md`
  queda corregido: seguía diciendo que `validacion.py` no se había re-corrido, lo que dejó de ser
  cierto. Sigue anclado al **05/07/2026** todo lo de `program.py`, `eda_distribuciones_divisiones.png`
  incluida.
- **En la misma pasada** (**T2**/**T3**): se añaden el KS contra
  los normales de D2 —drift (B) = **25** características en la variante de 54— con sus dos figuras, y la medición de la
  cascada invertida con su tabla y sus dos figuras. `Resultados/` pasa a **9** ficheros
  `metricas_*.csv` y **232** filas: 222 de la corrida `1163c90` del runbook + 10 de la corrida
  `274923d-sucio` de la cascada invertida. Las **222** filas previas quedan **intactas**.
- Actualización anterior: 2026-07-16 (pipeline completo — preprocesado, selección a 54,
  los 4 scripts de modelos ejecutados en 54 y 122, H1 cerrado; cifras reconciliadas con el
  reporte de validación vigente: 54 features, drift (A) 37, outliers media 4,78 %, 4 features de
  D2 fuera de [0,1]).
- Cuando se regeneren artefactos (nuevas ejecuciones de `program.py`/`validacion.py`) o aparezcan
  los ficheros de la sección 6, **actualizar esta guía en la misma sesión**: cifras, figuras
  nuevas y su destino en la memoria. Una guía desactualizada es peor que ninguna.
