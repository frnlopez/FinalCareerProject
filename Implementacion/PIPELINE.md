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

> Este árbol cubre lo que dejan **`program.py` y `validacion.py`**, no todo `Resultados/`: las
> tablas `metricas_*.csv`, las reglas `firmas_reglas_*.txt` y las figuras de los scripts de
> modelos se inventarían en `Resultados/GUIA_RESULTADOS.md`.

```
Resultados/
├── selected_features.txt                              ← lo escribe program.py:531-535
│                                                        (select_features), SIN prefijo y
│                                                        SOLO en la variante de 54: en
│                                                        --sin-seleccion no hay selección
│                                                        que documentar y el fichero de la
│                                                        otra variante no se toca
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
    ├── transformers.joblib                             ← scaler, LabelEncoder,
    │                                                     category_encoder y las DOS listas
    │                                                     de columnas: 'feature_columns'
    │                                                     (final, tras selección) y
    │                                                     'feature_columns_pre_seleccion'
    │                                                     (post one-hot, sobre la que está
    │                                                     ajustado el scaler)
    ├── mappings_and_info.txt                           ← mapeos LabelEncoder + scaler
    ├── usage_guide.txt                                 ← guía de uso con ejemplos
    ├── validation_report.txt                           ← generado por validacion.py
    ├── vocabulario_onehot.csv                          ← generado por validacion.py:
    │                                                     delta 77 → 122 del one-hot,
    │                                                     una fila por columna
    │                                                     categórica + `__total__`
    └── composicion_d3.csv                              ← generado por validacion.py
                                                          (2026-08-16): reparto de D3
                                                          por categoría de ataque, una
                                                          fila por categoría (dos, probe,
                                                          r2l, u2r) + `__total__` con el
                                                          ratio de desbalance. Mismas
                                                          cifras en las dos variantes
```

> Todo lo que cuelga del nodo `specialized_nsl_kdd_` existe **dos veces**, una por variante:
> con el prefijo `specialized_nsl_kdd_` (54 características) y con
> `specialized_nsl_kdd_sin_seleccion_` (122) — el `_transformers.joblib` incluido, que también
> es uno por variante. **La única excepción es `selected_features.txt`**, que no lleva prefijo
> y existe **una sola vez**: solo lo escribe la variante de 54 (`program.py:1160-1168`; con
> `--sin-seleccion` el paso 4b se omite y ese fichero ni se genera ni se pisa). Fuera de este
> árbol queda `Resultados/figuras/`, donde escriben **los dos** scripts: `program.py` deposita su
> única figura, `eda_distribuciones_divisiones.png` (nombre fijo, sin sufijo de variante: la
> segunda invocación sobrescribe a la primera), y `validacion.py` deposita **12 ficheros** — sus
> 6 figuras `validacion_*.png` × 2 variantes, estas sí con sufijo, tabuladas más abajo en el
> recuadro de anclaje de la corrida (aquí no se duplican).
> **Tampoco cuelga de este árbol `Resultados/verificacion_semilla_joblib.txt`**, y se declara aquí
> para que el inventario no lo omita: lo escribe `barrido_semillas.py` —no `program.py` ni
> `validacion.py`— en modo `--solo-verificar` y cuando el preflight encuentra un problema, **existe
> una sola vez** (no lleva sufijo de variante, porque recorre las dos), está **versionado** y su
> subsección propia está más abajo, en la ficha de la traza de la semilla.
> Los informes de validación, por tanto, son **dos**:
> `specialized_nsl_kdd_validation_report.txt` y
> `specialized_nsl_kdd_sin_seleccion_validation_report.txt` (y **dos** también los
> `..._vocabulario_onehot.csv` y los `..._composicion_d3.csv`, aunque estos cuatro CSV sí traen
> **las mismas cifras** en las dos variantes y cada uno por su motivo: el del vocabulario se mide
> sobre los CSV `_original_*`, previos a la selección de características, y el de la composición de
> D3 cuenta **filas** por categoría, que la selección no toca porque solo actúa sobre las columnas
> — el propio artefacto lo dice en ambos casos), y **no comparten ninguna de las
> cifras que dependen del set de características** (54 vs 122 características, drift (A) 37 vs 44,
> drift (B) 25 vs 31, media de outliers entre características 4,78 % vs 2,44 % —el criterio IQR da
> un porcentaje por característica y la cifra publicada es su media, no su mediana). Lo que no
> depende del set sí es
> idéntico en los dos: los tamaños D1 67.343 / D2 22.544 / D3 58.630, los 9.711 normales de D2 y
> las 4 características fuera de [0,1]. Cualquier número tomado de un informe tiene que decir de
> cuál sale.

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

**Más dos invocaciones que no pertenecen al runbook de T1** y que se listan aquí porque también
depositan en `Resultados/`: la medición de la **cascada invertida** (**T3**), que escribe su
propia tabla y no toca ninguna de las ocho. Va **después** de `firmas.py` y de `hibrido.py` de su
variante: necesita `firma_<algo>_<set>.joblib` (el modelo) y `hibrido_<set>.joblib` (de donde lee
`umbral_conf_elegido`; si falta, **aborta** en lugar de inventarse un umbral). No entrena nada
—solo `predict_proba` sobre modelos persistidos—, tarda ≈10 s por variante y **D2 solo se
reporta** (P-4).

```powershell
python cascada_invertida.py                 # 54 características
python cascada_invertida.py --sin-seleccion # 122 características
```

Salidas: `Resultados/metricas_cascada_invertida.csv` (**5 filas por variante**, 10 en total) y
`Resultados/figuras/cascada_invertida_54.png` / `..._122_sin_seleccion.png`.

> [!note] Lo que `validacion.py` estrenó con **T2** y lo que ha añadido después
> **T2** (2026-08-10): el KS de D1 contra **solo las filas normales de D2** —medición (B)— añadió
> `validacion_drift_ks_d2_normales.png` y `validacion_drift_ks_comparativa.png` (más sus gemelas
> `_sin_seleccion`) y **dos líneas de titular** al `..._validation_report.txt`, la (B) y su
> bloque `(A) vs (B)`. No sustituye a la medición (A).
>
> **La re-corrida del 2026-08-11 fue más allá de esas dos líneas**: el informe tiene hoy **tres
> bloques** que antes no estaban —(1) el `(A) vs (B)` con el `delta` y su salvedad de no
> aditividad, (2) los **tipos 0-day de D2 nominalmente**, con instancias y total, y (3) el
> **vocabulario del one-hot** con el delta 77 → 122 y su desglose por columna categórica— y
> estrena un artefacto propio, `..._vocabulario_onehot.csv`. Contenido detallado en
> `Resultados/GUIA_RESULTADOS.md` §3.2 y §2.4.
>
> **La re-corrida del 2026-08-16** añade un **cuarto bloque** al informe, «Composición de D3 por
> categoría de ataque», y su artefacto propio `..._composicion_d3.csv` (uno por variante). No
> cambia ninguna medición previa: drift, outliers, tamaños y vocabulario salen idénticos.
>
> Nada de esto entra en el runbook: `validacion.py` sigue siendo la puerta de calidad de
> `program.py` y **no** forma parte del runbook de las tablas de métricas.

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
> El runbook son **8 invocaciones**: **`program.py` NO se re-corrió**. Todo lo que deposita
> —los CSV originales y procesados de las dos variantes, `_mappings_and_info.txt`,
> `_usage_guide.txt`, `selected_features.txt`, `_transformers.joblib` y su única figura,
> `eda_distribuciones_divisiones.png`— sigue anclado a la corrida del **05/07/2026** y no a
> `1163c90`. Los splits que consumen las 8 invocaciones son esos CSV, idénticos (semilla 42);
> lo que no está anclado al commit publicado es esa figura del EDA.
>
> **`validacion.py` sí se re-corrió, y varias veces.** Lo que hay en disco **no** es la corrida
> de **T2** (`274923d-sucio`, 2026-08-10), ni la del ciclo de `84e3c8f` (2026-08-11, primera pasada),
> ni la de `fc1c6b4-sucio` (2026-08-11 20:53, cerrada en `9af842c`): las tres quedaron
> **sobrescritas**.
> *(El sufijo `-sucio` de un sello dice que al correr había cambios sin commitear en
> `Implementacion/`, de modo que el hash es el del commit **anterior** al código que produjo el
> artefacto. Los tres valores posibles del sello están tabulados en
> [El sello `commit`: tres valores posibles](#el-sello-commit-tres-valores-posibles-columna-de-los-csv-y-cabecera-de-los-informes),
> y esa tabla es la única definición: aquí no se duplica.)*
> Los artefactos publicados salen de la
> **re-corrida con el árbol limpio del 2026-08-17**, cuyo sello interno es **`ac36b88`**, sin
> sufijo `-sucio` (el ciclo que añade el reparto de D3 por categoría de ataque a los informes y a
> dos CSV nuevos; la primera pasada de ese ciclo, del 2026-08-16, sí salió `a8c20e9-sucio` y quedó
> **sobrescrita**). `ac36b88` es el commit **anterior** al que versiona estos artefactos, pero al
> estar el árbol limpio **identifica exactamente el código** que los produjo, y desde él la corrida
> es **reproducible** — que es justo lo que un sello `-sucio` no podía dar.
> Sus salidas, **seis artefactos versionados** más las figuras:
>
> | Artefacto | Cuántos | Qué cambia respecto a la corrida anterior |
> |---|---|---|
> | `..._validation_report.txt` | 2 (54 y `_sin_seleccion`) | Bloque nuevo «Composición de D3 por categoría de ataque»; el resto de cifras, idéntico |
> | `..._composicion_d3.csv` | 2 | **Artefacto nuevo** |
> | `..._vocabulario_onehot.csv` | 2 | **Solo cambia el sello**: mismas mediciones (77 → 122, delta 45) |
> | `figuras/validacion_*.png` | 12 (6 por variante) | Regeneradas, mismo contenido |
>
> La corrida terminó con **exit 0** e **integridad APROBADA** en las dos variantes. Ninguna cifra de
> calidad cambia por ello: `validacion.py` no entrena nada y solo lee los CSV de `program.py`. Las
> mediciones de drift se mantienen: **(A) 37 / (B) 25** sobre 54 características y
> **(A) 44 / (B) 31** sobre 122.
>
> Las cifras del bloque nuevo, **idénticas en las dos variantes** (la selección de características
> cambia columnas, no filas):
>
> | Categoría | Instancias | % de D3 |
> |---|---|---|
> | `dos` | 45.927 | 78,3336 % |
> | `probe` | 11.656 | 19,8806 % |
> | `r2l` | 995 | 1,6971 % |
> | `u2r` | 52 | 0,0887 % |
> | **`__total__`** | **58.630** | 100 % |
>
> Ratio de desbalance mayoritaria\minoritaria (`dos` frente a `u2r`): el informe lo imprime
> redondeado a un decimal, **883,2:1** (`validacion.py` formatea esa línea con `{:.1f}`). La cifra
> con dos decimales, **883,21**, es la de la columna `ratio_desbalance_max_min` del CSV
> `..._composicion_d3.csv` —que el informe reproduce en su volcado de la tabla, fila `__total__`—,
> y así la atribuye también `Resultados/GUIA_RESULTADOS.md`.
>
> **Por qué este sello NO necesita re-anclaje en prosa.** Los ciclos anteriores de `validacion.py`
> se publicaron con sello `-sucio` y hubo que anclarlos a mano a su commit de cierre
> (`fc1c6b4-sucio` → `9af842c`). Aquí el problema **desaparece en origen**: la re-corrida del
> 2026-08-17 se hizo con el árbol de `Implementacion/` **limpio**, así que el sello impreso es
> `ac36b88` a secas. Ese hash es el del commit **anterior** al que versionará estos ficheros, pero
> como no había diferencias sin commitear, **es exactamente el código que los generó**: basta hacer
> `checkout` de `ac36b88` y volver a lanzar `validacion.py` para obtenerlos. No es más que eso —no
> dice qué commit los versiona, y eso se sigue leyendo del historial de git—, pero sí es lo único
> que faltaba: reproducibilidad. El sello dentro del artefacto **no se edita a mano**: es una salida
> generada.
>
> **Los ciclos anteriores, para el historial.** La corrida del **2026-08-11 a las 20:53**
> (`fc1c6b4-sucio`) cerró los siete residuos de `validacion.py` —rótulo del 77 como reconstrucción,
> enteros en el CSV del vocabulario, `Recomendaciones:` vacío suprimido y el estampado de
> `commit`+`fecha` dentro de los propios artefactos— y quedó commiteada en **`9af842c`**. Sus
> ficheros están **sobrescritos** por la corrida de hoy; lo que sobrevive de aquel ciclo es el
> código, que sigue vigente salvo por el bloque de composición de D3 añadido después.
>
> **Y la procedencia no hay que creérsela: se lee en el contenido.** Los informes de hoy traen
> cuatro bloques que la corrida de T2 **no producía** —los **17 tipos 0-day** de D2 nominalmente y
> con sus instancias, el bloque del **vocabulario del one-hot** (delta 77 → 122), el rótulo
> «Outliers D1 (media entre características)», que sustituyó a la abreviatura ambigua «med.», y la
> **composición de D3 por categoría**—, más los CSV de vocabulario y de composición, que entonces
> **no existían**. Un tercero los **regenera** con las dos invocaciones sobre los CSV de
> `program.py` y compara.
>
> **Leer la procedencia DENTRO del fichero: resuelto en el código y ya presente en el disco.** El
> mtime es del sistema de ficheros y git no lo versiona: tras un `clone` los artefactos llevan la
> fecha de la copia, no la de la corrida. Los **seis** artefactos de la corrida del 2026-08-17
> —cabecera de los dos `..._validation_report.txt` y las dos últimas columnas de los
> `..._vocabulario_onehot.csv` y de los `..._composicion_d3.csv`— **imprimen `commit` y `fecha`**,
> igual que los `metricas_*.csv`, que traen las dos columnas desde **T1**. Verificado en disco: en
> `Resultados/specialized_nsl_kdd_validation_report.txt`, los campos de cabecera
> `Commit del código:` y `Fecha de la corrida:` (van tras el título y antes de `Integridad:`)
> están presentes y poblados: el commit declarado es `ac36b88`, y la marca temporal exacta,
> la que traiga el campo `Fecha de la corrida:` de ese fichero. **Se citan por su nombre de campo y
> no por su número de línea**: la cabecera es un artefacto regenerable y cualquier re-corrida que le
> añada o quite líneas desplazaría la referencia en silencio. **El commit es el mismo en los seis
> artefactos; la fecha NO**: cada invocación captura la suya en el constructor, así que la variante
> de 54 y la de 122 (`specialized_nsl_kdd_sin_seleccion_validation_report.txt`) llevan marcas
> distintas, separadas por los segundos que tardó en lanzarse la segunda.
> Cada CSV repite en
> todas sus filas el par de **su propia** invocación. **La prosa de este proyecto NO copia la marca
> temporal: remite al campo** (decisión de Francisco, 2026-08-16). Copiar los segundos hacía que
> cada re-corrida convirtiera en falso lo escrito —pasó con las fechas de la corrida anterior, que
> siguieron citadas cuando ya no existían en ningún artefacto—. El **commit sí se cita**: identifica
> el estado del código y no cambia al re-correr. Si hace falta la fecha, se lee del fichero.
>
> La decisión de arquitectura que lo bloqueaba está **tomada** (2026-08-11, Francisco; registrada en
> `resumen-de-decisiones.md`): `validacion.py` **importa `config.py`** y reutiliza
> `config.commit_actual()` —con su convención `-sucio` de la tabla del final de este documento—
> en vez de duplicar el mecanismo por copia. Se estampan `commit` y `fecha` en la cabecera de los
> dos informes (tras el título, antes de `Integridad:`) y como dos columnas de **cada uno de los dos
> CSV** que emite: el del vocabulario del one-hot y el de la composición de D3 —**seis artefactos
> sellados en total**, los mismos que enumera el recuadro de arriba. Eso **cruza una frontera que
> este documento declaraba inexistente**: `validacion.py`
> ya no es independiente de `config.py`. **`program.py` sí sigue siéndolo**, y sus rutas —y las de
> `validacion.py`— siguen hardcodeadas: esa parte de Q2 no se ha ejecutado.
>
> **Los artefactos se re-corrieron** (2026-08-17, sello limpio `ac36b88`), así que la procedencia se
> lee dentro de cada fichero. Este recuadro sigue siendo el anclaje **canónico** de la corrida, pero
> ya **no arrastra un re-anclaje pendiente**: al ser el sello limpio, identifica por sí solo el
> código que produjo los seis artefactos. Se re-escribe en cada re-corrida futura de `validacion.py`.
>
> **Qué vale y qué no vale un sello `-sucio`.** *(Doctrina general del proyecto, que sigue vigente
> para las corridas que sí salieron sucias; la de `validacion.py` que hay hoy en disco **no** es una
> de ellas.)* Un sello como `fc1c6b4-sucio` **NO identifica una
> versión del código**: el hash apunta al commit **anterior** al cambio, y `-sucio` solo dice
> «el árbol de `Implementacion/` difería de ese commit, no se sabe en qué». Lo que **sí** aporta:
> (a) una **fecha fiable dentro del fichero**, que sobrevive a un `clone` —al contrario que el
> mtime—, y (b) el **aviso explícito de no-reproducibilidad** desde ese hash, que es precisamente
> lo que evita citar el artefacto como si fuese reproducible. Lo que **no** aporta: saber qué
> versión lo produjo. Eso lo da el commit de cierre, y quien lo declara es este recuadro, no el
> fichero (para el ciclo de `fc1c6b4-sucio` fue `9af842c`). **Para los seis artefactos que hay hoy
> en disco esto ya no aplica**: su sello es limpio y sí identifica el código. La convención de los
> tres valores está en
> [El sello `commit`: tres valores posibles](#el-sello-commit-tres-valores-posibles-columna-de-los-csv-y-cabecera-de-los-informes)
> y no se duplica aquí.
>
> Nada que ver con la limitación de `ac496cb` de más abajo: allí los CSV no están en git ni se
> pueden regenerar; aquí son artefactos de texto plano **versionados y reproducibles**, y del propio
> fichero se lee **de qué versión exacta del código** salió.
>
> | Figura (× 2 variantes: sin sufijo = 54, `_sin_seleccion` = 122) | Origen |
> |---|---|
> | `validacion_distribucion_clases.png` | de siempre |
> | `validacion_discriminantes_d1_vs_d3.png` | de siempre |
> | `validacion_drift_ks.png` | de siempre |
> | `validacion_outliers_iqr.png` | de siempre |
> | `validacion_drift_ks_d2_normales.png` | **T2** |
> | `validacion_drift_ks_comparativa.png` | **T2** |
>
> Lo que la re-corrida **no** arregla: al no tocar `program.py`, el hueco de
> `eda_distribuciones_divisiones.png` sigue abierto. Y las cifras de la variante de 122 siguen sin
> coincidir con las de 54 en todo lo que depende del set de características (ver el recuadro del
> árbol de `Resultados/`, más arriba).

> [!note] El texto de `alcance_tiempo_s` publicado **sí** es el de `config.py` de hoy
> En la corrida `ac496cb` no lo era: los arreglos de redacción de
> `config.ALCANCE_TIEMPO_S_BLOQUE_ANOMALIAS` y `..._BLOQUE_FIRMAS` que exigió la auditoría de T18
> eran posteriores a aquella corrida. La re-corrida `1163c90` los incorpora: las cuatro celdas
> `alcance_tiempo_s` publicadas coinciden **carácter a carácter** con las cuatro constantes
> `config.ALCANCE_TIEMPO_S_*` del código de hoy (2.367 · 1.536 · 1.196 · 1.676 caracteres).
>
> Quedan **dos** divergencias vivas entre `config.py` y lo publicado, y ninguna de las dos obliga
> a re-correr:
>
> 1. **`config.ALCANCE_N_ITER_TOTAL`**, reformulado **después** de `1163c90` (recuadro de las dos
>    columnas de épocas del autoencoder, más abajo). **No toca el dato**: ese texto **no viaja a
>    ninguna columna** de ningún CSV —`ALCANCE_COLUMNAS` solo lo consulta
>    `config.alcance_de_columna()`, y a esa función solo llega `validar_esquema_minimo()` para
>    columnas que casan con `PREFIJOS_SIN_DECLARAR`, filtro con el que `n_iter_total_grid` no
>    casa—. Es documentación en el código, no celda.
> 2. **`config.ALCANCE_BALANCEO`**, al que el 2026-08-12 se le quitó el número de semilla (decía
>    «StratifiedKFold 5 · semilla 42» y ahora dice «StratifiedKFold 5 · shuffle · la semilla de la
>    corrida está en la columna `semilla`»). Esta **sí** es una celda publicada: `firmas.py:280`
>    escribe esa constante en la columna `alcance`, y las 16 filas de
>    `Resultados/metricas_balanceo.csv` conservan el texto antiguo. **No hay dato corrupto y no hay
>    que re-correr `firmas.py`**: esas 16 filas son todas `semilla = 42` (verificado en el CSV), así
>    que el texto viejo es verdadero de ellas — se quitó el literal precisamente para que dejara de
>    serlo automáticamente en un barrido, no para corregir una falsedad ya escrita. La divergencia se
>    cierra sola la próxima vez que se re-corra `firmas.py` con el defecto.
>    **Aviso operativo:** si algún día se re-corre `firmas.py`, hay que re-correr **las dos variantes
>    o ninguna**. `evaluacion.limpiar_variante_csv()` compara **conjuntos de columnas**, no valores,
>    así que re-correr solo `54` no invalidaría las filas de `122_sin_seleccion`: la tabla quedaría
>    con 8 filas declarando el alcance nuevo y 8 el viejo, mezcla que ninguna comprobación detecta.

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
clave `set_features × algoritmo × alcance`.

Las **cinco** tablas auxiliares (`evaluacion.TABLAS_AUXILIARES`) tienen otra granularidad de fila
—algoritmo × balanceo, tipo de ataque, umbral candidato, categoría asignada— y por eso no llevan
`algoritmo` ni la clave de unicidad, pero sí `alcance` y procedencia
(`evaluacion.COLUMNAS_MINIMAS_AUXILIARES`), y las cinco publicadas ya la traen:

| Tabla auxiliar | Filas | Granularidad de fila | Recuento comprobado por |
|---|---|---|---|
| `metricas_balanceo.csv` | 16 | algoritmo × esquema de balanceo × variante | — |
| `metricas_baseline_0day.csv` | 36 | tipo de ataque 0-day × variante | — |
| `metricas_hibrido_0day.csv` | 144 | tipo × detector × variante | — |
| `metricas_hibrido_calibracion.csv` | 6 | `UMBRAL_CONF` candidato × variante | — |
| `metricas_cascada_invertida.csv` | 10 | categoría asignada × variante (**5 por variante**) | `cascada_invertida.NSLKDDInvertedCascadeMeasurer._comprobar_tabla()` |

La última es la única con recuento fijo, y lo comprueba **el propio script**, no
`comprobar_recuento()`: esa función solo conoce las cuatro tablas principales y meter una
auxiliar en `FILAS_ESPERADAS_POR_VARIANTE` tocaría un contrato que no se toca. La comprobación
propia verifica **cuatro** cosas al releer el CSV escrito —las 5 filas de la variante; que las
categorías estén una y solo una vez; que los `n_argmax` de las cuatro sumen `n_normales_d2`, que
es lo que hace de los buckets del argmax una **partición** de las normales de D2; y que los
`n_condenadas` de las cuatro sumen el de `__global__`— y **aborta** si alguna falla. Las dos
últimas son distintas y las dos hacen falta: una partición rota que afectase solo a filas por
debajo del umbral dejaría los `n_condenadas` cuadrando. Se comprueba sobre enteros y no sobre
`tasa_condena`, que solo cuadra hasta el redondeo (ver más abajo).

> Al terminar las ocho, si quedan ficheros `*.esquema-anterior.bak` en `Resultados/`, es que
> había tablas del esquema viejo: comprobar que la nueva trae todas las filas y borrarlos a mano.
> Un `.bak` no se versiona ni se cita. Las dos invocaciones de `cascada_invertida.py` van aparte y
> tienen su propio `.bak` si alguna vez cambia su esquema.

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
| `ac496cb` | *(nunca versionados: los sustituyó la re-corrida `1163c90` antes del commit de cierre de T18)* | Primera con `n_iter_ganador` y `n_iter_total_grid`. **Corrida histórica**: sus cifras solo sobreviven citadas en este documento, no hay CSV suyo en git. |
| `1163c90` | `8fdc421` (commit de cierre de **T18**) | **La publicada hoy.** Mismo esquema que `ac496cb`. 8 invocaciones, **222 filas** —subtotal de las ocho tablas del runbook, **no** el total de `Resultados/`—, todas con `semilla = 42` y `commit = 1163c90` limpio. |
| `274923d-sucio` | `b1f1df2` (commit de cierre de **T3**, que versiona a la vez `cascada_invertida.py` y su CSV) | **Solo la cascada invertida (T3)**: 2 invocaciones, **10 filas** en `metricas_cascada_invertida.csv`, `semilla = 42`. No toca ninguna de las ocho tablas del runbook. El `-sucio` es correcto y previsto: la corrida es anterior al commit que versiona su propio código (`config._RUTA_SUCIEDAD` mira `Implementacion/`). |
| `fc1c6b4-sucio` | `9af842c` (commit de cierre del ciclo de los siete residuos, que versiona a la vez `validacion.py` y sus cuatro artefactos) | **Solo `validacion.py`**, corrida del **2026-08-11 20:53** (2 invocaciones). Entra en esta tabla porque la columna `commit` rige también en los dos `*_vocabulario_onehot.csv`, que **sí están versionados**; el mismo sello va en la cabecera de los dos `*_validation_report.txt`. **No escribe en ningún `metricas_*.csv`**, así que no altera el recuento de filas de abajo. El commit es común a los cuatro artefactos; la **fecha** es la de cada invocación (`2026-08-11T20:53:27` a 54, `2026-08-11T20:53:46` a 122). El `-sucio` es previsto y **no identifica una versión del código** —el hash es el del commit **anterior** al cambio—, así que la versión que lo produjo es la de la columna de al lado, `9af842c`: el re-anclaje está hecho aquí y en el recuadro de trazabilidad de arriba. **Estos artefactos ya no son los que hay en disco**: los sobrescribió la re-corrida de `a8c20e9-sucio` (fila siguiente). Sigue nombrando su corrida, que es lo que una tabla de corridas registra. |
| `a8c20e9-sucio` | *(ninguno: **nunca se versionó** y ya no hace falta anclarla)* | **Solo `validacion.py`**, re-corrida del **2026-08-16** (2 invocaciones, exit 0, integridad **APROBADA**). Añadía el bloque «Composición de D3 por categoría de ataque» a los dos informes y estrenaba los dos `*_composicion_d3.csv`. **No escribe en ningún `metricas_*.csv`**, así que no altera el recuento de filas de abajo. El `-sucio` era previsto —el árbol tenía sin commitear el propio cambio de `validacion.py`—, y por eso **no identificaba una versión del código**. **Estos artefactos ya no son los que hay en disco**: los sobrescribió la re-corrida limpia de `ac36b88` (fila siguiente), que trae **exactamente las mismas cifras** y resuelve el sello en origen, de modo que el re-anclaje en prosa que esta fila arrastraba **queda sin objeto**. Sigue nombrando su corrida, que es lo que una tabla de corridas registra. |
| `ac36b88` | *(no necesita re-anclaje: el sello es **limpio** y ya identifica el código; el commit que versiona los artefactos es posterior y se lee del historial de git)* | **Solo `validacion.py`**, re-corrida con el **árbol limpio** del **2026-08-17** (2 invocaciones, exit 0, integridad **APROBADA**). **Es la que hay en disco.** Reescribe los **seis** artefactos versionados —los dos `*_validation_report.txt`, los dos `*_vocabulario_onehot.csv` y los dos `*_composicion_d3.csv`— y las 12 figuras `validacion_*.png`, con **todas las cifras idénticas** a las publicadas (D3: `dos` 45.927 · `probe` 11.656 · `r2l` 995 · `u2r` 52 · total 58.630, ratio 883,21; drift 122 **(A) 44 / (B) 31**, 54 **(A) 37 / (B) 25**): **lo único que cambió fue el sello**. **No escribe en ningún `metricas_*.csv`**, así que no altera el recuento de filas de abajo. El commit es común a los seis artefactos; la **fecha** es la de cada invocación y se lee en el campo `Fecha de la corrida:` de cada uno (esta prosa no la copia: caducaría en la siguiente re-corrida). `ac36b88` es el commit **anterior** al que versionará estos ficheros, pero al no haber cambios sin commitear **identifica exactamente el código** que los produjo y los hace **reproducibles** desde él. |
| `00c3c3e-sucio` | `54d1349` (commit que versiona a la vez `barrido_semillas.py` y la traza que ese script produce) | **No es una corrida de modelos**: es la verificación `--solo-verificar` del **2026-08-12 15:57**, con **cero `fit`**, que solo lee los descriptores de los 20 `.joblib` publicados y escribe `Resultados/verificacion_semilla_joblib.txt`. Entra en esta tabla porque ese fichero lleva el mismo campo de cabecera `Commit del código:` y la misma convención. **No escribe en ningún `metricas_*.csv`**, así que no altera el recuento de filas de abajo. El `-sucio` es previsto: HEAD era `00c3c3e` y el código del lanzador estaba sin commitear, de modo que la versión que produjo la traza es la de la columna de al lado, `54d1349`. El sello impreso dentro del fichero **no se edita** —es salida de `config.commit_actual()`—: el re-anclaje se hace aquí y en la subsección de la traza de la semilla. **El mismo sello lo lleva otra cosa, y no es esta:** el **ensayo de humo a semilla 1** de ese mismo día (`anomalias.py --semilla 1`) corrió con el árbol igual de sucio, así que **sí hizo `fit`** (cuatro) y **sí escribió** una `metricas_*.csv` — `metricas_anomalias_semillas.csv`, que **nunca fue una de las nueve publicadas**. Ese fichero **sí existe hoy** en `Resultados/` —es una de las nueve `metricas_*_semillas.csv` del barrido, con 80 filas—, pero **el contenido que escribió el ensayo ya no está**: lo sobrescribió el barrido de `df30cb2` (el residuo del ensayo desapareció, no el fichero). Bajo la clave «una corrida se identifica por el commit del código que la produjo», este sello nombra **dos** corridas: al citarlo hay que decir cuál. |
| `df30cb2` | `9ad971b` (commit de cierre del **cómputo de T4**, que versiona a la vez las nueve tablas del barrido y los dos artefactos de la agregación) | **El barrido de las diez semillas (T4)**, del **2026-08-12 22:09 al 2026-08-13 00:38**: 100 invocaciones (5 scripts × 2 variantes × 10 semillas) que escriben **2.320 filas** repartidas en las nueve `metricas_*_semillas.csv`, con `semilla` de 1 a 10 y `commit = df30cb2` **limpio** en todas (lo verificó el agregador: `commits_origen = df30cb2` único en sus 198 celdas). **No toca ninguna de las nueve tablas publicadas de la semilla 42**, que quedaron bit a bit idénticas. El mismo sello, con fecha `2026-08-12T22:07:10`, lo lleva `verificacion_semilla_joblib.txt`, re-sellado por el preflight del barrido. |
| `df30cb2-sucio` | `9ad971b` (el mismo commit de cierre: versiona a la vez `agregar_semillas.py` y sus dos artefactos) | **No es una corrida de modelos**: es el **agregador** de T4 (`agregar_semillas.py`) del **2026-08-13**, con **cero `fit`** —solo lee CSV—, que escribe `dispersion_semillas.csv` y `.md` (**198 filas**) con `commit_agregador = df30cb2-sucio` y fecha `2026-08-13T07:43:40`. Entra en esta tabla porque esos dos artefactos **están versionados** y llevan la misma convención de sello. **No escribe en ningún `metricas_*.csv`**, así que no altera el recuento de filas de abajo. El `-sucio` es previsto: HEAD era `df30cb2` y el arreglo de `_tabla_md()` estaba sin commitear, de modo que la versión que produjo la agregación es la de la columna de al lado, `9ad971b`. El sello impreso dentro de los dos artefactos **no se edita** —es salida de `config.commit_actual()`—: el re-anclaje se hace aquí y en el recuadro del «tercer re-anclaje de sello del proyecto», al final de «Lo que dio la primera ejecución real». Y **el `-sucio` no contamina la cita**: lo que respalda cada banda es `commits_origen = df30cb2` limpio, no este sello. **Este sello ya no es el que hay en disco**: lo sobrescribió la tercera pasada del agregador (fila siguiente). Sigue nombrando su corrida —la segunda pasada, de las `07:43:40`—, que es lo que una tabla de corridas registra. |
| `ddade37-sucio` | `9d4c26d` (commit de cierre de la automatización del titular «13 de 98», que versiona a la vez `agregar_semillas.py` y los dos artefactos de dispersión) | **No es una corrida de modelos**: es la **tercera pasada del agregador** de T4, del **2026-08-13 `19:54:48`**, con **cero `fit`** —solo lee CSV—, que reescribe `dispersion_semillas.csv` y `.md` (**198 filas**, las mismas cifras) añadiendo el **titular automático**: las cuatro columnas `*_42` y el recuento «13 de 98». Para eso **abre las nueve publicadas en LECTURA**, y **sigue sin escribir en ninguna `metricas_*.csv`**, así que no altera el recuento de filas de abajo. El `-sucio` es previsto: HEAD era `ddade37` y el titular automático estaba sin commitear, de modo que la versión que produjo la agregación es la de la columna de al lado, `9d4c26d`. El sello impreso dentro de los dos artefactos **no se edita** —es salida de `config.commit_actual()`—: el re-anclaje se hace aquí y en el recuadro de re-anclajes del final de «Lo que dio la primera ejecución real». **Este sello nombra DOS invocaciones, y hay que decir cuál** (mismo caso que `00c3c3e-sucio`): la de las `19:54:48`, que es la que registra esta tabla, y una **regeneración posterior a las `20:13:37`** tras aplicar los cinco hallazgos altos del `auditor-ml` — esa segunda es la que `9d4c26d` dejó versionada (verificado el 2026-08-14 con `git show 9d4c26d:Resultados/dispersion_semillas.md`, cuya cabecera dice `2026-08-13T20:13:37`). Así que el re-anclaje identifica **exactamente** el código de la corrida de las `20:13:37`, y para la de las `19:54:48` identifica ese mismo código **antes** de los arreglos del auditor, que nunca se versionó por separado. Las cifras (198 filas, «13 de 98») son las mismas en las dos. **Este sello ya no es el que hay en disco**: lo sobrescribió la cuarta pasada (fila siguiente). Ojo también a la procedencia cruzada que expone esta pasada: `commit_semilla_42` es `1163c90` / `274923d-sucio` mientras `commits_origen` es `df30cb2` — titular y banda no salen del mismo código. |
| `6bb224c-sucio` | `1cb5c26` (commit de cierre de la **Tanda 2** de la Fase 2, del 2026-08-14, que arrastra a la vez `agregar_semillas.py` y los dos artefactos de dispersión que venían sin commitear) | **No es una corrida de modelos**: es la **cuarta pasada del agregador** de T4, del **2026-08-14 `15:15:13`**, con **cero `fit`** —solo lee CSV—, que reescribe `dispersion_semillas.csv` y `.md` (**198 filas**, las mismas cifras) añadiendo a la salvedad de procedencia del `.md` el **reparto de las 98 celdas casadas por commit de origen del titular** (`_reparto_commits_titular_md()`, contado desde `commit_semilla_42`: `1163c90` **94** con 13 fuera de banda · `274923d-sucio` **4** con ninguna fuera). **Este sello ya no es el que hay en disco**: lo sobrescribió la quinta pasada (fila siguiente). Sigue nombrando su corrida —la cuarta, de las `15:15:13`—, que es lo que una tabla de corridas registra. **Sigue sin escribir en ninguna `metricas_*.csv`**, así que no altera el recuento de filas de abajo. El `-sucio` es previsto: HEAD era `6bb224c` y el reparto por commit estaba sin commitear, de modo que la versión que produjo la agregación es la de la columna de al lado, `1cb5c26`. El sello impreso dentro de los dos artefactos **no se edita** —es salida de `config.commit_actual()`—: el re-anclaje se hace aquí y en el recuadro de re-anclajes del final de «Lo que dio la primera ejecución real». |
| `0276039-sucio` | `98a0289` («codigo: emitir el "8 de 10" pareado desde `agregar_semillas.py` y corregir el residuo de T22», del 2026-08-17, que versiona a la vez `agregar_semillas.py` y los **tres** artefactos del agregador que venían sin commitear) | **No es una corrida de modelos**: es la **quinta pasada del agregador** de T4, del **2026-08-17**, con **cero `fit`** —solo lee CSV—, que reescribe `dispersion_semillas.csv` y `.md` (**198 filas, las mismas cifras**; en el `.md`, la sección nueva «Comparaciones pareadas por semilla») y **estrena `comparaciones_pareadas.csv`** (**13 filas de datos**). **Es la que hay en disco** (verificado en la cabecera del `.md` y en la columna `commit_agregador` del CSV). **Sigue sin escribir en ninguna `metricas_*.csv`**, así que no altera el recuento de filas de abajo. El `-sucio` es previsto: HEAD era `0276039` y el código que emite el recuento pareado estaba sin commitear, de modo que la versión que produjo la agregación es la de la columna de al lado, `98a0289`. El sello impreso dentro de los tres artefactos **no se edita** —es salida de `config.commit_actual()`—: el re-anclaje se hace aquí y en el recuadro de re-anclajes del final de «Lo que dio la primera ejecución real». |

De las **nueve corridas versionadas de esta tabla desde `1163c90` en adelante** (las filas anteriores
—`c7cf319`, `38fdd4b` y `5516b60`— también están versionadas, pero son de esquemas previos y quedan
fuera de este recuento) —`1163c90` en `8fdc421`, `274923d-sucio` en
`b1f1df2`, `fc1c6b4-sucio` en `9af842c`, `00c3c3e-sucio` en `54d1349`, las dos de `df30cb2` (limpio
y `-sucio`) en `9ad971b`, `ddade37-sucio` en `9d4c26d`, `6bb224c-sucio` en `1cb5c26` y
`0276039-sucio` en `98a0289`—, solo dos escriben en alguna de las
nueve `metricas_*.csv` **publicadas**
(no lo hacen ni `fc1c6b4-sucio` ni la verificación de `00c3c3e-sucio`; la `metricas_anomalias_semillas.csv`
que escribió el ensayo de humo bajo ese mismo sello no era una de las nueve, y su contenido lo
sobrescribió después el barrido. **Tampoco las dos de `df30cb2`**: el barrido escribe **solo** en las nueve
`metricas_*_semillas.csv`, que son tablas aparte, y el agregador no escribe en ninguna
`metricas_*.csv`). **La novena de esa lista es la última, `0276039-sucio` —la quinta pasada del
agregador—, cuyos tres artefactos son los que hay hoy en disco**, y tampoco escribe en ninguna
publicada. **La corrida más reciente de la tabla que aún NO está versionada es `ac36b88`
(2026-08-17, la re-corrida limpia de `validacion.py`)**, y por eso no entra en este recuento de
nueve; la de `a8c20e9-sucio` que ocupaba este hueco quedó sobrescrita sin llegar a versionarse. No confundir este recuento con «las
cuatro corridas versionadas» de la subsección «Lo que `perf_counter` NO arregla», que designa otro
cuarteto y se cita por su nombre y no por número de línea. Sumando esas dos, las **nueve tablas publicadas de la semilla 42** tienen hoy
**232 filas repartidas en 9 ficheros** `metricas_*.csv`
(222 + 10): las **ocho** tablas de la corrida `1163c90` —las cuatro principales más las cuatro
auxiliares, como detalla la fila de `1163c90`— con `commit = 1163c90`, y la novena, la de la
cascada invertida, con `274923d-sucio`. Son **dos corridas distintas**, no una, y ninguna cifra de una debe presentarse
junto a las de la otra sin decirlo. **Las nueve `metricas_*_semillas.csv` del barrido no entran en
ese recuento**: son otras 2.320 filas en otros nueve ficheros, con `commit = df30cb2`, y su cita
va siempre por la banda de `dispersion_semillas.csv`, nunca mezclada con las cifras de la 42.

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
> Mismo número y misma fila (0,101740 en la variante de 54 de la corrida `1163c90`), y es
> **correcto por construcción**: la etapa 2 solo reclasifica los flujos que la etapa 1 marcó como
> sospechosos y **nunca devuelve uno a `normal`**, así que la cascada no puede tener otro FPR que
> el de su etapa 1. Se conservan las dos columnas porque responden a dos requisitos distintos
> —`bin_fpr` cierra el bloque binario que pide **H-5** y `fpr_cascada` es el FPR que **P-2** exige
> junto al titular de 0-day—, pero T1 no admite dos nombres para una magnitud sin declararlo: la
> coincidencia va escrita en el dato, dentro de `config.ALCANCE_HIBRIDO`.

#### Lo que `perf_counter` NO arregla: la dispersión entre corridas

Es *wall-clock* en una **máquina no dedicada**. Con la misma semilla, el mismo código y una
**calidad idéntica al bit**, los tiempos se mueven mucho. Lo que sigue **no es una cota** —la
corrida siguiente puede superarla—: es lo **medido** entre las cinco corridas que llevan columna
`commit`, `c7cf319` · `38fdd4b` · `5516b60` · `ac496cb` · `1163c90`, celda a celda.

> [!warning] `ac496cb` **no es reproducible desde git**
> Todas las cifras de la columna `ac496cb` que aparecen en este documento —aquí y en el resto de
> secciones— proceden de una corrida cuyos **CSV nunca se commitearon** y que además **fueron
> sobrescritos por la re-corrida `1163c90`**. No se pueden recuperar ni por hash ni por fichero:
> sobreviven **solo citadas aquí**. Cualquier frase de la memoria que se apoye en ellas tiene que
> arrastrar esta salvedad; no valen como evidencia verificable por un tercero. Las cifras de las
> otras cuatro corridas (`c7cf319`, `38fdd4b`, `5516b60`, `1163c90`) sí están en git.

| Tabla | Columna | Peor caso observado entre las cinco corridas | Valores (`c7cf319` / `38fdd4b` / `5516b60` / **`ac496cb` ⚠ no verificable** / `1163c90`) |
|---|---|---|---|
| `metricas_anomalias.csv` | `tiempo_s` | **Autoencoder 54: 4,82×** | 52,43 / 37,71 / 181,91 / 38,20 / 49,20 s |
| `metricas_anomalias.csv` | `tiempo_inferencia_s` | **Autoencoder 54: 5,07×** | 0,048 / 0,031 / 0,147 / 0,029 / 0,041 s |
| `metricas_firmas.csv` | `tiempo_s` | **DecisionTree 54: 4,30×** | 2,35 / 2,01 / 7,35 / 1,71 / 2,07 s |
| `metricas_firmas.csv` | `tiempo_inferencia_s` | **DecisionTree 54: 3,5×** (entre las cuatro medidas con `perf_counter`) | *(0,0 = artefacto)* / 0,002 / 0,007 / 0,002 / 0,002 s |
| `metricas_baseline.csv` | `tiempo_s` | RF monolítico 54: **2,43×** | 34,13 / 28,31 / 39,17 / 59,44 / 24,48 s |
| `metricas_hibrido.csv` | `tiempo_s` | La cascada 54: 1,90× | 24,80 / 22,17 / 27,71 / 42,02 / 25,40 s |

Dos lecturas que hay que arrastrar a cualquier frase de la memoria que compare tiempos:

1. **La dispersión no es cosa solo de los tiempos largos.** El autoencoder de 54 mueve su
   `tiempo_s` (decenas de segundos a minutos) y su `tiempo_inferencia_s` (decenas de
   milisegundos) prácticamente en el mismo factor, 4,8× y 5,1×.
2. **Ni la celda más estable baja de ≈1,2×.** El mínimo observado en las 8 filas de anomalías
   sigue siendo `OneClassSVM` 54, con 1,23× (26,17 / 23,28 / 28,10 / **22,89 ⚠ no verificable** /
   25,58 s). **Una diferencia menor que eso entre dos filas no significa nada**, y ninguna cifra de
   tiempo puede presentarse como propiedad del algoritmo sin declarar esta dispersión. El suelo
   depende de `ac496cb`, que aporta el mínimo de la serie y no es reproducible desde git; **sin esa
   columna el suelo sería 28,10/23,28 = 1,21×**, prácticamente el mismo, así que el argumento se
   sostiene solo con las cuatro corridas versionadas.
3. **Añadir una corrida solo ha empeorado la dispersión, nunca la ha estrechado.** De las seis
   celdas de la tabla, `ac496cb` empeoró el factor en cuatro (`tiempo_inferencia_s` del
   autoencoder, `tiempo_s` del DecisionTree, del baseline y del híbrido) y `1163c90` lo empeora en
   una más —el baseline de 54 pasa de 2,10× a **2,43×**, porque esta corrida da el mínimo de la
   serie, 24,48 s—. **Ninguna de las dos ha mejorado ninguna celda**, que es exactamente lo que
   cabe esperar de un máximo sobre un mínimo al añadir muestras: la banda solo puede ensancharse.
   Es la razón de que se declare **medida y no cota**. **Salvedad:** la aportación de `ac496cb` a
   esas cuatro celdas **no es verificable desde git** (sus CSV nunca se commitearon y los
   sobrescribió `1163c90`); el argumento de que la banda solo se ensancha se sostiene igual con
   las cuatro corridas que sí están versionadas, pero los factores concretos que cita esta tabla
   dependen de una columna no recuperable.

**Ninguna columna de tiempo es reproducible.** Valen como comparación relativa de coste **dentro
de la misma corrida** y como orden de magnitud. El resto de la tabla sí es reproducible
(semilla 42).

> [!caution] Ni siquiera la **dirección** de una comparación de tiempos aguanta sola
> Comparar dos algoritmos por su tiempo **dentro de la misma corrida** parece más seguro que
> comparar dos corridas, pero tampoco basta. Es lo que mide **T20** sobre el par
> `RandomForest` / `HistGradientBoosting` de `metricas_firmas.csv`, con grids de igual
> cardinalidad:
>
> | Corrida | 54 (`tiempo_entrenamiento_s` RF → HistGB) | 122 |
> |---|---|---|
> | `c7cf319` | 65,876 → 128,204 (**1,95×**) | 60,887 → 268,642 (**4,41×**) |
> | `38fdd4b` | 47,429 → 62,404 (**1,32×**) | 95,487 → 237,743 (**2,49×**) |
> | `5516b60` | 108,152 → 83,315 (**0,77×**) | 68,698 → 194,108 (**2,83×**) |
> | `ac496cb` ⚠ **no verificable** | 48,943 → 64,997 (**1,33×**) | 52,609 → 181,346 (**3,45×**) |
> | `1163c90` **(publicada)** | 61,444 → 60,745 (**0,99×**) | 51,097 → 122,820 (**2,40×**) |
>
> ⚠ La fila `ac496cb` **no es reproducible desde git**: sus CSV nunca se commitearon y los
> sobrescribió `1163c90`. Los pares que aporta al recuento no son verificables por un tercero; el
> resto de filas de esta tabla sí lo son.
>
> [!warning] Homónimo peligroso: este «8 de 10» NO es el del capítulo 5
> El «8 de 10» de esta sección es un recuento de **pares de TIEMPO DE ENTRENAMIENTO**
> `RandomForest` vs `HistGradientBoosting`, tomado sobre **cinco corridas** (dos variantes por
> corrida = 10 pares). **No tiene nada que ver** con el «8 de 10» que usan las notas `5.2`, `5.4`
> y `3.5` de la memoria, que es el **recuento pareado entre las 10 semillas** de qué algoritmo
> gana en `f1_macro`. Misma cadena, dos mediciones distintas: no se citan la una por la otra.
>
> **Lo citable, y ni una palabra más:** *`HistGradientBoosting` es más caro de entrenar que
> `RandomForest` en **8 de los 10** pares intra-corrida de **tiempo de entrenamiento**
> registrados —recuento tomado sobre cinco corridas, **una de ellas, `ac496cb`, no reproducible
> desde git**; no es el recuento entre semillas del capítulo 5—, con grids de igual
> cardinalidad; el par de 54 **se invierte en 2 de las 5 corridas**, así que la afirmación solo es
> sólida en la variante de 122 —5 de 5, todas por encima de 2,4×—, y en ningún caso HistGB gana en
> calidad: `f1_macro` **0,804 vs 0,822** en la variante de 54 de `1163c90`.*
>
> **La horquilla «1,31×-4,40×» queda retirada**: se quedó sin suelo en cuanto la corrida publicada
> añadió un segundo contraejemplo. Una banda cuyo extremo inferior cae por debajo de 1,0 en dos de
> diez pares no es una banda, es un rango con la dirección dentro.
>
> Y la inversión **no es solo del entrenamiento**: en inferencia el par de 54 va en sentido
> contrario y con holgura, `latencia_ms_por_flujo` **0,0032 ms/flujo** en HistGB frente a
> **0,0072** en RF. Entrenar y predecir son dos costes distintos y no se citan juntos.
>
> Regla que queda: una dirección solo es citable si se repite en **todas** las corridas
> disponibles; si no, se cita con el recuento de pares de tiempo de entrenamiento (**8 de 10**,
> cinco corridas — no el recuento entre semillas del capítulo 5) y con la variante en la que
> sí aguanta, nunca con un par de segundos ni con una horquilla.

> [!danger] Qué mide la latencia — y qué no (declaración exigida por P9)
> `latencia_ms_por_flujo` y `flujos_por_segundo` miden **solo el `predict`/`score` sobre
> características ya calculadas y ya cargadas en memoria**. **No** incluyen la captura del
> tráfico, el ensamblado del flujo ni la extracción de las 41 características del registro
> NSL-KDD, que es donde vive el coste real de un despliegue. Citar ese caudal como capacidad
> operativa sería exactamente la *Lab-Only Evaluation* que denuncia el pitfall **P9**. La
> frase viaja en cada fila dentro de `alcance_tiempo_s` (`config._AVISO_LATENCIA_SOLO_PREDICT`);
> el número, solo aquí.
>
> **Y el número, como orden de magnitud y nunca con siete dígitos.** El caudal máximo de
> `1163c90` es el del `predict` del `DecisionTree`, y así es como se cita:
>
> > **≈4·10⁶ flujos/s a 54 características y ≈2,6·10⁶ a 122** (n = 9.083), medidos sobre **2,2 ms**
> > y **3,6 ms** de *wall-clock* en un **pase único**: un orden de magnitud, no una cifra. Y solo
> > del `predict` sobre características ya en memoria (salvedad **P9** / **T21** de arriba).
>
> Los 2,2 y 3,6 ms salen de `latencia_ms_por_flujo × 9.083` (0,000238 y 0,000391 ms/flujo), que es
> el único sitio donde el tiempo de inferencia del DecisionTree conserva cifras.
>
> **La fila es además incoherente consigo misma, y hay que declararlo:** `flujos_por_segundo` se
> calcula del tiempo **sin redondear**, pero `tiempo_inferencia_s` se publica a **3 decimales**.
> Quien intente reconstruir el caudal desde las columnas visibles hace `9.083 / 0,002` y obtiene
> **4.541.500** frente a los `4196350.2` publicados, y `9.083 / 0,004` = **2.270.750** frente a
> `2556719.0`: un desvío del **8,2 %** (54) y del **12,6 %** (122), tomando en cada caso el menor
> de los dos valores como base. **La fila invita a una reconstrucción que no cierra**, y por eso el
> caudal se cita con una cifra significativa y con el aviso al lado.
>
> La regla de la base —**el menor de los dos valores**— es uniforme, está declarada y reproduce
> las dos cifras, pero conviene decir que **el menor no es el mismo tipo de valor en las dos
> variantes**: en 54 el menor es el caudal **publicado** y en 122 el **reconstruido**. Es la
> elección que **maximiza** el desvío en ambos casos, o sea **conservadora y a favor del aviso**:
> con la otra base los porcentajes saldrían menores, nunca mayores.
>
> El propio par lo remata: es **el mismo DecisionTree**, cuyo coste por muestra en `predict` es
> el recorrido de un árbol de `max_depth=10` —idéntico en las dos variantes, porque la profundidad
> ganadora es la misma— y aun así la horquilla entre ellas es de **1,6×** (2,2 → 3,6 ms). **Esa
> horquilla es *jitter*, no características.**

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
> | `ac496cb` ⚠ **no verificable** | 3,92 / 22,89 / 12,75 / 38,20 |
> | `1163c90` **(publicada)** | 5,27 / 25,58 / 20,16 / 49,20 |
>
> ⚠ La fila `ac496cb` **no es reproducible desde git**: sus CSV nunca se commitearon y los
> sobrescribió `1163c90`. El argumento —que ninguna corrida reproduce los valores del vault— se
> sostiene igual con las filas verificables.
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
corrida `1163c90`** (la publicada) y **de ninguna otra**: no predicen la fila que tengas delante
—el reparto que vale es el que sale de las columnas de tiempo de la propia fila— y se
recalculan aquí, sin tocar el CSV, cada vez que se corre el runbook.

> [!note] Por qué **un** decimal y no dos
> `tiempo_s` se publica redondeado a **dos decimales** mientras que las columnas que se le restan
> llevan tres, así que el residual arrastra hasta ±0,005 s de puro redondeo. Sobre denominadores
> de pocos segundos eso es **±0,09 pp** en `IsolationForest` 54 (0,005 / 5,27) y **±0,24 pp** en
> `DecisionTree` 54 (0,005 / 2,07): el segundo decimal del porcentaje es ruido y no se escribe.
> Las dos únicas cifras que van con dos decimales son las del híbrido, cuyo denominador es de
> decenas de segundos.

**Anomalías** (`1163c90`). Ya no se estima nada: `anomalias.py` cronometra los dos tramos grandes
y los publica, así que la cola sale exacta por resta. Residual =
`tiempo_s` − `tiempo_entrenamiento_s` − `tiempo_inferencia_s`. **Van las ocho filas**: publicar
solo cuatro sería escoger.

| Detector | Variante | Residual (= no ajuste ni inferencia) | del cual `tiempo_score_seleccion_s` | `tiempo_score_umbral_s` | cola (métricas + figura) |
|---|---|---|---|---|---|
| `IsolationForest` | 54 | **30,6 %** — (5,27 − 3,509 − 0,151) / 5,27 | 21,1 % | 2,6 % | 6,9 % |
| `OneClassSVM` | 54 | **48,4 %** — (25,58 − 10,688 − 2,501) / 25,58 | 41,4 % | 6,1 % | 0,9 % |
| `LocalOutlierFactor` | 54 | **27,7 %** — (20,16 − 13,288 − 1,288) / 20,16 | 21,4 % | 5,3 % | 1,1 % |
| `Autoencoder` | 54 | 0,5 % — (49,20 − 48,933 − 0,041) / 49,20 | 0,1 % | 0,1 % | 0,3 % |
| `IsolationForest` | 122 | **26,5 %** — (5,24 − 3,699 − 0,151) / 5,24 | 21,2 % | 1,4 % | 3,9 % |
| `OneClassSVM` | 122 | **41,0 %** — (94,01 − 50,652 − 4,764) / 94,01 | 37,5 % | 3,1 % | 0,5 % |
| `LocalOutlierFactor` | 122 | **28,5 %** — (45,33 − 29,341 − 3,048) / 45,33 | 23,0 % | 4,5 % | 1,1 % |
| `Autoencoder` | 122 | 0,5 % — (113,18 − 112,535 − 0,083) / 113,18 | 0,1 % | 0,0 % | 0,3 % |

Lo domina el **scoring de la selección**: el script pasa por el scorer bastantes más filas
eligiendo configuración (18.469 × 6/9/4/2) que evaluando (22.544 una vez). En `OneClassSVM` ese
tramo se acerca al propio ajuste. No entraba en `tiempo_entrenamiento_s` porque no es `fit`.

> [!tip] **Lo reproducible de este bloque no son los segundos: es el reparto**
> Es el hallazgo más sólido que ha dado la serie de corridas y **es la afirmación sobre la que
> debe apoyarse el capítulo**, en lugar de sobre segundos que no se repiten.
>
> Entre `ac496cb` y `1163c90` los tiempos absolutos se mueven sin control —el `tiempo_s` del
> `OneClassSVM` de 122 va de 34,39 s a 94,01 s, **2,73×**—. Y sin embargo el residual **como
> fracción del bloque** se mueve, en las ocho filas, **como mucho 4,5 pp**:
>
> | Detector · variante | Residual en `ac496cb` ⚠ **no verificable** | en `1163c90` | Δ |
> |---|---|---|---|
> | `OneClassSVM` 54 | 49,5 % | 48,4 % | −1,1 pp |
> | `OneClassSVM` 122 | 38,5 % | 41,0 % | +2,5 pp |
> | `IsolationForest` 54 | 33,3 % | 30,6 % | −2,7 pp |
> | `IsolationForest` 122 | 31,0 % | 26,5 % | **−4,5 pp** |
> | `LocalOutlierFactor` 122 | 27,7 % | 28,5 % | +0,8 pp |
> | `LocalOutlierFactor` 54 | 27,6 % | 27,7 % | +0,1 pp |
> | `Autoencoder` 122 | 0,7 % | 0,5 % | −0,2 pp |
> | `Autoencoder` 54 | 0,5 % | 0,5 % | 0,0 pp |
>
> ⚠ **Las dos columnas no son simétricas en verificabilidad.** La de `1163c90` sale de CSV que
> están versionados (en `8fdc421`); la de `ac496cb` **no es reproducible desde git** —sus CSV nunca se
> commitearon y los sobrescribió `1163c90`—, así que sobrevive **solo citada aquí**. Los Δ de esta
> tabla, y con ellos el hallazgo entero, dependen de una columna que un tercero no puede
> recalcular.
>
> **Y el orden de las ocho filas se conserva casi entero.** Ordenadas de mayor a menor residual,
> la única que cambia de sitio es `IsolationForest` 122, que baja del 4.º al 6.º puesto
> adelantada por las dos de `LocalOutlierFactor`; las otras siete conservan su posición relativa,
> y los dos escalones grandes —OCSVM por encima del 38 %, autoencoder por debajo del 1 %— se
> repiten idénticos.
>
> Formulación citable: *los segundos absolutos de estas tablas no son reproducibles, pero **el
> reparto interno del bloque sí lo es a unos pocos puntos porcentuales**.* Es coherente con la
> causa: la carga de máquina reescala el bloque **entero** y por eso se cancela al dividir, mientras
> que el peso de cada tramo lo fija el diseño del script (cuántas filas puntúa y cuántas veces),
> que la semilla 42 hace determinista. **Ojo con el alcance: son dos corridas, una de ellas no
> reproducible desde git, y no una serie.** Que el reparto sea estable no lo convierte en
> constante del algoritmo, solo en la magnitud **menos frágil** de las que aquí se publican. Y la
> estabilidad se afirma **contra `ac496cb`**, cuyos CSV nunca se commitearon y fueron sobrescritos
> por `1163c90`: la comparación no la puede rehacer nadie a partir del repositorio.

> [!caution] Repartos retirados por falsados
> Este documento publicó antes «el tramo (2) es el 75-86 % y el (3) el 5-15 %» y un scoring de
> selección de ≈9,5 s: procedían de un **modelo de coste no declarado** —con escalado plano por
> filas, ese tramo de `OneClassSVM` 54 salía por encima del residual **medido** de la propia fila,
> un imposible. En `1163c90` esa fila mide 10,688 s de ajuste y **12,391 s** de residual, del que
> el tramo (2) son 10,597 s: sale del dato, no de un modelo—. Y publicó «**27-49 %**» sin anclar a
> corrida ni decir de qué filas: en
> `1163c90` las dos filas del `Autoencoder` dan **0,5 %** y **0,5 %**, más de un orden de magnitud
> por debajo de esa banda, porque su ajuste se lo come todo. Los dos quedan retirados; la tabla de
> arriba los sustituye, con corrida declarada y con la resta escrita al lado.

**Firmas** (`1163c90`). El `GridSearchCV` se lleva del **87,68 %** (mínimo: `DecisionTree` 54,
1,815 / 2,07) al **99,66 %** (máximo: `HistGradientBoosting` 122, 122,820 / 123,24) del bloque, y
el residual es un único tramo —la cola de métricas + figura—. **No** lleva columna propia: al ser
un único componente sale exacto restando las otras dos columnas, y una columna más solo repetiría
una resta.

| Clasificador | 54 | 122 |
|---|---|---|
| `DecisionTree` | **87,68 %** | **89,19 %** |
| `RandomForest` | 99,42 % | 99,43 % |
| `KNN` | 95,73 % | 95,98 % |
| `HistGradientBoosting` | 99,48 % | **99,66 %** |

Ese residual, en segundos y por orden de tabla —`DecisionTree` · `RandomForest` · `KNN` ·
`HistGradientBoosting`—, es **0,253 · 0,290 · 0,337 · 0,286 s** a 54 características y
**0,275 · 0,262 · 0,345 · 0,322 s** a 122. Las ocho filas caben ahora en **0,25-0,35 s**, un
factor **1,36×** entre extremos: la cola **no es un coste fijo**, pero tampoco se desmadra. (La
corrida anterior, `ac496cb`, daba un factor **2**, con `HistGradientBoosting` 122 en 0,513 s; que
el factor se mueva así entre dos corridas es más motivo para citarla como «poco variable» que
para ponerle una cota. Ese factor **2** **no es verificable desde git**: los CSV de `ac496cb`
nunca se commitearon y los sobrescribió `1163c90`.)

Como es pequeño en términos absolutos, solo pesa donde el bloque entero dura pocos segundos:
**≈12 %** en `DecisionTree` 54 —(2,07 − 1,815 − 0,002) / 2,07 = 12,2 %— y **≈11 %** en
`DecisionTree` 122 —(2,58 − 2,301 − 0,004) / 2,58 = 10,7 %—, frente al **0,3-0,8 %** de los otros
seis. Los dos se escriben redondeados a la unidad **a propósito**: el redondeo de `tiempo_s` a dos
decimales propaga **±0,24 pp** y **±0,19 pp** respectivamente, así que el decimal no es suyo.
Ojo también con el otro redondeo: el `tiempo_entrenamiento_s` va a sus tres decimales, y truncarlo
a 1,82 o 2,30 haría que la fórmula dejase de reproducir su propio resultado.

**Híbrido** (`1163c90`). Calibración OOF **92,18 %** (54) y **86,20 %** (122). El resto —**7,82 %**
y **13,80 %**— **incluye la inferencia**: la cascada sobre D2 son **0,74 %** y **0,63 %**, y lo
demás (7,08 % y 13,17 %) es la carga de los splits, la de los dos `.joblib` y las tres pasadas de
métricas de la tabla de sensibilidad, sin desglosar, porque ninguna columna los mide por separado.
La precisión importa: escribir «el resto» dejando la inferencia fuera daría tres sumandos que no
llegan al 100 %. Es decir: **más del 85 % de lo que cuesta el híbrido es calibrar un umbral, no
detectar** —y la detección propiamente dicha no llega al 1 %—.

> [!note] El híbrido de 122 tarda **menos** que el de 54, y no es una paradoja
> `tiempo_s` da **25,40 s** (54) frente a **15,83 s** (122). Escribirlo como «más características,
> menos tiempo» sería falso: la causa es **mecánica y está en el dato**. El grueso del bloque es la
> calibración OOF, que reajusta el clasificador de firmas una vez por fold —y **la configuración
> ganadora de firmas no es la misma en las dos variantes**:
>
> | Variante | `config_ganadora` de `RandomForest` en `metricas_firmas.csv` |
> |---|---|
> | 54 | `{'clf__max_depth': 10, 'clf__n_estimators': 300}` |
> | 122 | `{'clf__max_depth': None, 'clf__n_estimators': 100}` |
>
> **300 árboles contra 100**: el híbrido de 54 hace más trabajo en la calibración aunque tenga
> menos columnas. Lo medido en `1163c90` es `tiempo_entrenamiento_s` = **23,414 s** (54) frente a
> **13,646 s** (122), **1,72×**. Que no llegue al 3× que sugiere el recuento de árboles tiene
> explicación a mano —el modelo de 122 crece con `max_depth=None`, así que cada uno de sus 100
> árboles es más caro— pero **no se cuantifica aquí**: el factor cae dentro de la dispersión de
> máquina de la sección anterior y no hay medida que lo separe. Lo citable es solo la conclusión
> cualitativa: la comparación de tiempos entre las dos variantes del híbrido **no compara dos
> anchos de entrada: compara dos bosques distintos.**
>
> Y tampoco es cierto que la calidad sea la misma en las dos: `conocida_f1_macro` vale
> **0,748051** (54) y **0,655441** (122). Son dos sistemas distintos, no el mismo con más
> columnas. Material para **T19** y **T21**.

> [!warning] Los tres tiempos de *scoring* de anomalías: cómo se citan
> `tiempo_score_seleccion_s`, `tiempo_score_umbral_s` y `tiempo_inferencia_s` miden **la misma
> operación** (puntuar filas con el modelo ya ajustado) sobre conjuntos de tamaño distinto, así
> que el cociente crudo entre dos de ellos **no es un cociente de coste por flujo**: hay que
> ponerlo siempre **contra la referencia de tamaños**. Para el par umbral/inferencia esa
> referencia es |D1_val| / |D2| = **13.469 / 22.544 = 0,5975**.
>
> En `1163c90`, `tiempo_score_umbral_s / tiempo_inferencia_s` va de **0,483**
> (`IsolationForest` 122) a **0,894** (`IsolationForest` 54). Publicar ese rango a secas invita
> justo a la lectura que el dato prohíbe, así que se publica **normalizado por filas** (cociente
> dividido por 0,5975 = coste por fila del tramo de umbral respecto al de inferencia):
>
> | Detector | 54 (crudo → normalizado) | 122 (crudo → normalizado) |
> |---|---|---|
> | `IsolationForest` | 0,894 → **1,50×** | 0,483 → **0,81×** |
> | `OneClassSVM` | 0,628 → 1,05× | 0,605 → 1,01× |
> | `LocalOutlierFactor` | 0,824 → **1,38×** | 0,670 → 1,12× |
> | `Autoencoder` | 0,634 → 1,06× | 0,590 → 0,99× |
>
> Leído así: **cuatro de los ocho detectores puntúan D1_val a 0,99-1,10× el coste por fila de D2**
> —a coste por fila prácticamente igual, que es lo que la teoría predice— y los otros cuatro se
> salen: `IsolationForest` 54 (1,50×) y `LocalOutlierFactor` 54 (1,38×) por arriba,
> `IsolationForest` 122 (0,81×) por abajo, y `LocalOutlierFactor` 122 rozando el borde (1,12×).
>
> **La banda «0,99-1,10×» es *post hoc*:** no viene de ningún criterio fijado de antemano, se
> traza sobre los valores ya medidos de modo que caben justo esos cuatro. Vale como descripción
> —el recuento y los que se salen van nombrados uno a uno—, no como umbral de tolerancia.
>
> **Ninguna de esas desviaciones se explica, y ahora hay dos razones para no intentarlo.**
>
> **Una: el atípico cambia de algoritmo en cada corrida.** El máximo del cociente crudo fue
> `Autoencoder` 54 en `5516b60` (0,884), `LocalOutlierFactor` 54 en `ac496cb` (0,814) e
> `IsolationForest` 54 en `1163c90` (0,894). Tres corridas, tres detectores distintos, y siempre
> rondando 0,81-0,89 en crudo. **Que se mueva la identidad del atípico y no su magnitud es la
> firma de un sorteo aleatorio**, no de una propiedad del algoritmo: si la causa fuese estructural,
> el que se sale sería siempre el mismo. **Salvedad de verificabilidad:** uno de los tres puntos
> —el de `ac496cb`— **no es reproducible desde git**, porque sus CSV nunca se commitearon y los
> sobrescribió `1163c90`; los de `5516b60` y `1163c90` sí lo son.
>
> **Dos, y es el argumento fuerte: a esta escala la magnitud no es medible con este banco.** Los
> ocho cocientes se construyen con medidas **sub-segundo** de un **pase único** en una máquina no
> dedicada —el par del `Autoencoder` 54 son **26 ms sobre 41 ms**—. El redondeo a milisegundos por
> sí solo mueve esos cocientes varios puntos, y la carga de máquina, más. No hay nada que atribuir
> porque no hay señal por encima del ruido.
>
> *(Tres afirmaciones retiradas de este mismo recuadro. **Una:** que el desvío venía del
> `algorithm='brute'` que `sklearn` asigna a `LocalOutlierFactor` por encima de 15 features — era
> una atribución causal sobre una medida única. **Dos:** el argumento «LOF no es el único que lo
> enseña, el `Autoencoder` de 54 da 0,884», que servía para relativizar el primero. **Tres:** el
> «seis de los ocho a 0,99-1,10×, LOF el que se sale» de la corrida anterior, que `1163c90` deja
> en cuatro de ocho y con LOF ya sin la exclusiva. **Una magnitud que se mueve así entre corridas
> no sostiene ninguna atribución causal**, ni a favor ni en contra.)*

> [!note] Las dos columnas de épocas del autoencoder: `n_iter_ganador` y `n_iter_total_grid`
> El autoencoder es un `MLPRegressor` con `early_stopping=True` y `max_iter=300`, así que su
> tiempo de ajuste depende de **dos** cosas que el CSV no separaba: cuántas épocas necesitó y cómo
> de cargada estaba la máquina. Sin ese dato no se podía decidir si los **180,965 s** (54) frente a
> **47,826 s** (122) de `5516b60` —relación **invertida** respecto a `38fdd4b`, que dio 37,492 s y
> 121,059 s— eran épocas o carga. Es lo que pedía **T22**.
>
> **Ese dato ya existe y sí decide**, pero en un eje distinto del que se pedía: decide **entre
> corridas** y deja **indecidible** la comparación 54 vs 122. La respuesta va más abajo y es la
> contraria de la que este documento publicó con `ac496cb`.
>
> Se publican **dos** columnas porque **no son intercambiables**, y confundirlas fue el defecto 2
> del dictamen de `0595a15`:
>
> | Columna | Qué cuenta | Para qué sirve |
> |---|---|---|
> | `n_iter_ganador` | Épocas del ajuste **de la configuración ganadora** | Saber si el modelo que se publica se cortó por `max_iter=300` o convergió |
> | `n_iter_total_grid` | **Suma** de las épocas de **todas** las configuraciones del grid | Leer `tiempo_entrenamiento_s` en **segundos por época** con un denominador coherente: cubre exactamente los mismos `fit` que ese tiempo cronometra |
>
> **Coherente, y nada más que coherente.** Dos límites, los dos importantes:
>
> 1. **No es el «único válido».** El grid del autoencoder tiene **dos arquitecturas**,
>    `(64, 32, 64)` y `(32, 16, 32)`, cuyo coste por época no es el mismo, así que el cociente
>    `tiempo_entrenamiento_s / n_iter_total_grid` es una **media ponderada** entre dos costes por
>    época distintos —ponderada por cuántas épocas consumió cada arquitectura, que es justo lo que
>    la columna no desglosa—. No es una constante física del modelo.
> 2. **No separa causas: no decide si una diferencia de tiempo es de épocas o de carga de
>    máquina.** Este documento y `config.ALCANCE_N_ITER_TOTAL` lo afirmaron y era falso. **Como el
>    recuento de épocas sale igual en lo medido** —mismos 162 y 128 en las dos corridas que lo
>    registran, una de ellas (`ac496cb`) no reproducible desde git, ver más abajo—, el denominador es constante y el cociente **es el numerador
>    reescalado**: absorbe íntegramente la carga de máquina y no la distingue de nada. Sirve para
>    leer el tiempo en s/época **dentro de una corrida**, no para atribuirle causa a una diferencia
>    entre dos.
>
> **Respuesta medida a T22.** El dato que lo zanja es que las dos corridas que registran épocas
> dan **exactamente los mismos recuentos**:
>
> | Variante | `n_iter_total_grid` | `n_iter_ganador` | `tiempo_entrenamiento_s` en `ac496cb` ⚠ **no verificable** | s/época | en `1163c90` | s/época |
> |---|---|---|---|---|---|---|
> | 54 | **162** | **117** | 37,977 s | 0,234 | 48,933 s | **0,3021** |
> | 122 | **128** | **66** | 31,003 s | 0,242 | 112,535 s | **0,8792** |
>
> ⚠ Las dos columnas de `ac496cb` —tiempo y s/época— **no son reproducibles desde git**: sus CSV
> nunca se commitearon y los sobrescribió `1163c90`. Tampoco lo son los recuentos de épocas
> atribuidos a esa corrida, de modo que la afirmación «idénticos en las dos corridas que los
> registran» —y los factores **1,29×** y **3,63×** que salen de ella— descansa sobre una corrida
> verificable (`1163c90`) y otra que no lo es.
>
> **El recuento de épocas del autoencoder sale igual en lo medido**: 162 (54) y 128 (122)
> para el grid completo, 117 y 66 para el ajuste ganador, **idénticos en las dos corridas que los
> registran, una de ellas (`ac496cb`) no reproducible desde git**;
> ninguno tocó `max_iter=300`, así que todos cortaron por `early_stopping`. Es lo esperable con
> semilla 42 y datos idénticos, pero hasta ahora no estaba medido. Con ese recuento congelado,
> `tiempo_entrenamiento_s` varía entre corridas **1,29×** (54) y **3,63×** (122).
>
> > **La variación de tiempo del autoencoder entre corridas es carga de máquina y no épocas: está
> > medido con el número de épocas fijo en las dos corridas que lo registran, una de ellas
> > (`ac496cb`) no reproducible desde git.**
>
> **Y la comparación 54 vs 122 no es decidible con este diseño.** Cada variante es una invocación
> distinta del script —dos sesiones, no dos medidas de la misma—; la dirección del par **se
> invierte dos veces** en las cuatro corridas registradas (122 más lento en `38fdd4b`, 54 más lento
> en `5516b60` y en `ac496cb`, 122 otra vez en `1163c90`); y el cociente s/época —**0,234 / 0,242**
> en `ac496cb` frente a **0,3021 / 0,8792** en `1163c90`, sobre **denominadores idénticos**— hereda
> esa carga por completo, porque con el denominador constante el cociente es el numerador
> reescalado y nada más. Decidirlo exigiría un **diseño de medidas repetidas** —N repeticiones por
> variante dentro de la misma sesión, y publicar mediana y dispersión en vez de un valor—, **que no
> se ha hecho**.
>
> **Queda retirada** la conclusión que este documento publicó con `ac496cb` —«la diferencia de
> tiempo del autoencoder entre las dos variantes es de épocas, no de carga de máquina», apoyada en
> un 3,3 % de diferencia de coste por época—: `1163c90` la falsa con los mismos denominadores y
> tiempos que se mueven 1,29× y 3,63×. Aquel 3,3 % era una coincidencia de dos sesiones con carga
> parecida, no una medida del modelo.
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

### La cascada invertida (T3): qué mide, qué NO mide y cómo se cita

Aquí viven **la lectura y los números** de `metricas_cascada_invertida.csv`, por la misma regla de
**T18** que rige los `alcance_tiempo_s`: la celda `alcance` del CSV se repite en las 10 filas y no
se puede corregir sin re-correr, así que lleva **solo lo estable** —el contrafactual, la
población, el denominador, la procedencia del umbral y la marca P-4— y todo lo interpretativo se
escribe en esta sección, anclado al commit de su corrida.

**Qué mide.** `cascada_invertida.py` carga el clasificador de firmas ya entrenado
(`firma_RandomForest_<set>.joblib`) y le pasa **solo las 9.711 filas normales de D2** —las que en
el sistema real nunca llegan a la etapa 2, porque la etapa 1 no las marca—. Cuenta cuántas
saldrían con etiqueta de ataque y confianza `>= UMBRAL_CONF`. Es la afirmación de **3.2.2** («si
las firmas fueran primero, condenarían tráfico legítimo en masa») convertida en número. La etapa 2
se entrena solo con D3, que son solo ataques: **no tiene clase `normal`**, así que su argmax es
siempre una de las cuatro categorías de ataque y lo único que puede frenar una condena es el
umbral de confianza.

> [!important] La fila `__global__` es una **cota inferior** del FPR, no el FPR
> Es el error que traía la primera versión de esta medición, enunciado como igualdad tanto en
> `config.ALCANCE_CASCADA_INVERTIDA` como en el comentario de `cascada_invertida.py`, y que por
> tanto **viajaba dentro de las 10 filas del CSV**.
>
> En el sistema publicado `unknown` **no es** `normal`: es **alarma** (decisión **P-5**; en
> `hibrido.py::_ensamblar_prediccion` el flujo degradado a `unknown` sigue dentro de
> `es_sospechoso`, y la binaria del híbrido **es** `es_sospechoso`). Así que los flujos normales
> que aquí caen por debajo del umbral —**3.153** a 54 características y **6.382** a 122— **no
> quedan exonerados**: en una cascada con las firmas delante pasarían a la etapa siguiente y
> podrían acabar en alarma igualmente. Presentar `tasa_condena` como «el FPR de un sistema de
> firmas-primero» o contradice la convención `unknown` = alarma, o postula en silencio otro
> sistema — y ese otro sistema es justo el que el descarte **«Cascada invertida completa»**
> declara inexistente y cerrado («no se puede invertir esta cascada, solo construir otro
> sistema»).
>
> **Lo que la tabla mide sin ambigüedad** son los falsos positivos **irrecuperables**
> (`n_condenadas`): los que salen ya con etiqueta de ataque y confianza suficiente, y que ninguna
> etapa posterior puede deshacer. Ese es el número citable.
>
> **Este bloque es el único sitio donde vive el DESARROLLO del argumento**, no el único sitio
> donde se menciona. Hay otras tres apariciones, y las tres son **resúmenes derivados** de este
> bloque, sin razonamiento propio:
>
> | Dónde | Qué contiene | Estatus |
> |---|---|---|
> | `Implementacion\PIPELINE.md` (este bloque) | El argumento completo: P-5, `unknown` = alarma, por qué la igualdad era falsa | **fuente** |
> | `Implementacion\app\cascada_invertida.py:22-43` (docstring) | El mismo aviso en prosa, para quien lea el código sin la guía | derivado |
> | `Resultados\GUIA_RESULTADOS.md` §6.1 | Tres viñetas de cómo citar la tabla | derivado |
> | `config.ALCANCE_CASCADA_INVERTIDA` (celda `alcance` del CSV) | Una frase: «cota inferior; lo citable es `n_condenadas`» + puntero aquí | derivado |
>
> Que la celda sea solo una frase es deliberado: el porqué depende de la decisión **P-5**, no del
> código, y una celda se repite en las 10 filas de un CSV que no se corrige sin re-correr.
>
> **Si P-5 se revisara algún día**, se reescribe aquí **y se propagan los tres derivados** —el
> docstring y la guía a mano; la celda `alcance` exige además **re-correr las dos variantes** de
> `cascada_invertida.py` (≈10 s, no entrena), porque el texto viaja dentro del dato. Corregir solo
> este bloque deja copias contradictorias en disco.

**Las cifras** (corrida `274923d-sucio`, `semilla = 42`, `UMBRAL_CONF = 0,5` leído de
`hibrido_<set>.joblib::umbral_conf_elegido` en las dos variantes):

| Variante | Condenadas / 9.711 normales | `tasa_condena` `__global__` | Bajo umbral (→ `unknown`) | Mediana de confianza |
|---|---|---|---|---|
| **54** | **6.558** | 0,675317 | 3.153 | 0,5355 |
| **122** | **3.329** | 0,342807 | 6.382 | 0,46 |

Desglose por categoría asignada por el argmax (`n_argmax` → `n_condenadas`):

| Categoría | 54 | 122 |
|---|---|---|
| `dos` | 6.394 → **4.706** | 5.573 → 881 |
| `probe` | 1.592 → 1.002 | 2.216 → **1.792** |
| `r2l` | 1.698 → 833 | 1.903 → 643 |
| `u2r` | 27 → 17 | 19 → 13 |
| `__global__` | 9.711 → **6.558** | 9.711 → **3.329** |

`n_argmax` de `__global__` es el total de normales **por construcción**, no por casualidad: sin
clase `normal`, toda fila recibe una categoría de ataque. Los `n_argmax` de las cuatro categorías
particionan ese total y los `n_condenadas` suman el de `__global__` — lo comprueba el script y
**aborta** si no cuadra.

> [!note] Las `tasa_condena` de las cuatro categorías **no** suman exactamente el `__global__`
> Los **recuentos** sí. Las tasas publicadas, no: se redondean a 6 decimales, y en la variante de
> 122 suman **0,342808** frente al **0,342807** de la fila `__global__`. Es 1 unidad en el sexto
> decimal, pero la afirmación «suman exactamente» era falsa tal y como estaba escrita —y estaba
> escrita dentro del dato—. Cualquier comprobación de coherencia se hace sobre `n_condenadas`.

**Las dos variantes no son comparables como «más o menos características».** El gap —67,5 % contra
34,3 %— se mide sobre **dos bosques distintos**: la configuración ganadora de `RandomForest` en
`metricas_firmas.csv` es `{max_depth: 10, n_estimators: 300}` a 54 y `{max_depth: None,
n_estimators: 100}` a 122 (misma tabla que ya obliga a la salvedad del `tiempo_s` del híbrido más
arriba). Con `max_depth=None` las hojas son puras, así que cada árbol vota one-hot y el
`predict_proba` de un bosque de 100 solo puede dar múltiplos de 0,01: es exactamente lo que
enseñan las medianas publicadas de la variante de 122 —**0,44 · 0,55 · 0,46 · 0,73**, frente a
valores como 0,545132 o 0,533087 en la de 54—, y la mediana global, **0,46**, cae **por debajo**
del `UMBRAL_CONF = 0,5`. **No se cuantifica aquí** cuánto de la diferencia entre las dos variantes
aporta cada causa: no hay medida que las separe y sería justo la atribución que este documento
evita en todas partes.

> [!caution] Si la memoria contrasta este número con el FPR del híbrido, tiene que declararlo
> El denominador **es el mismo** (las 9.711 normales de D2), así que la resta es aritméticamente
> posible: `fpr_cascada` = **0,101740** en la variante de 54 (corrida `1163c90`) frente al
> 0,675317 de aquí. Pero **no son dos medidas del mismo tipo**: una es el FPR **medido** del
> sistema publicado y la otra una **cota inferior** de un sistema hipotético, salidas además de
> **dos corridas distintas** (`1163c90` y `274923d-sucio`). El contraste sostiene el argumento de
> 3.2.2 —el orden de las etapas no es indiferente— siempre que las dos salvedades vayan escritas
> al lado. Sin ellas es una comparación de peras con manzanas presentada como titular.

### El sello `commit`: tres valores posibles (columna de los CSV y cabecera de los informes)

Esta convención es **una sola** y rige en **dos sitios**: la columna `commit` de los
`metricas_*.csv` y de los `..._vocabulario_onehot.csv`, y el **campo de cabecera**
`Commit del código:` de los dos `..._validation_report.txt` (desde la corrida del 2026-08-11).
Todos salen de la misma llamada, `config.commit_actual()`.

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
unicidad que incluye `semilla`. El motivo son tres muros que, en las cuatro tablas principales,
siguen intactos y **se conservan** — ninguna invocación legítima de la CLI los dispara y son lo
que hace comprobable el recuento del runbook:

1. `evaluacion.limpiar_variante_csv()` borra por **variante**, no por clave: 10 semillas de la
   misma variante colapsarían a la última escrita.
2. `evaluacion.CLAVE_UNICIDAD` (`set_features × algoritmo × alcance`) **no incluye `semilla`**:
   dos semillas de la misma variante son un duplicado y `comprobar_unicidad()` **aborta**.
3. `evaluacion.FILAS_ESPERADAS_POR_VARIANTE` es fijo 4/4/1/1: 40 filas hacen **abortar** a
   `comprobar_recuento()`.

La dispersión de T4 entra como tabla nueva en el anexo `A.3`.

#### El andamiaje de la semilla (implementado el 2026-08-12; barrido corrido y agregado)

Esta subsección describe el **mecanismo**; las cifras que produjo están en la ficha del agregador,
más abajo. El barrido **se corrió** el **2026-08-12 (22:09 → 00:38)** con sello `commit = df30cb2`,
y se agregó a continuación: en disco están las nueve `metricas_*_semillas.csv` (**2.320 filas**) y
`dispersion_semillas.csv` / `.md` (**198 filas**). La lectura de si los intervalos de
RandomForest/HistGradientBoosting y de Autoencoder/IsolationForest se solapan está en la ficha
«El lanzador y el agregador del barrido» → *Lo que dio la primera ejecución real*.

**Vía de inyección: un flag `--semilla N`** en los cinco scripts ejecutables (`anomalias.py`,
`firmas.py`, `baseline.py`, `hibrido.py`, `cascada_invertida.py`), que llama a
`config.fijar_semilla(N)` **antes** de instanciar la clase del script. El razonamiento de por qué
un flag y no una variable de entorno ni un argumento de función está en el encabezado de
`config.py`, sección «CÓMO SE INYECTA LA SEMILLA». `validacion.py` **no** lleva el flag: no
consume `RANDOM_STATE` (valida los splits que deja `program.py`).

**El defecto sigue siendo 42.** Sin `--semilla`, cada script produce exactamente lo de antes:
mismos nombres de artefacto, mismas nueve tablas, mismas figuras.

Con una semilla distinta de 42 se activan dos desvíos, y son los que impiden pisar lo publicado:

| Qué | Con semilla 42 | Con semilla N ≠ 42 |
|---|---|---|
| `.joblib`, figuras, `firmas_reglas_*.txt` | nombre publicado (`…_54.joblib`) | sufijo `_semilla<N>` (`…_54_semilla<N>.joblib`), vía `config.sufijo_artefactos()` |
| Las nueve tablas de métricas | la tabla publicada | `metricas_<x>_semillas.csv`, vía `config.ruta_tabla()` — la publicada **no se abre** |

En las tablas `*_semillas.csv` la unidad de fila es el par **(variante, semilla)**, y las tres
comprobaciones se adaptan a esa unidad sin tocar el contrato de las principales: el borrado es por
(variante, semilla), la clave es `CLAVE_UNICIDAD_SEMILLAS` (la de siempre **más** `semilla`) y el
recuento exige los mismos **4/4/1/1/5** —cinco recuentos, con las 5 filas de la cascada invertida
incluidas— **por cada** (variante, semilla). Lo deciden por el **nombre del
fichero** (`config.es_tabla_de_semillas()`), no por un parámetro en cada llamada, para que la regla
viva en un solo sitio.

**Salvaguarda de mezcla:** `hibrido.py` y `cascada_invertida.py` cargan `.joblib` de otros scripts,
así que comprueban que la clave `semilla` del artefacto coincide con la de la corrida y **abortan**
si no. **Con una excepción declarada:** la tabla de los cuatro detectores de `hibrido.py`
(`_tabla_0day_cuatro_detectores`) no aborta — su guarda M1 captura el fallo de carga, **incluido el
de semilla distinta**, omite ese detector con un aviso y sigue, dejando la celda de
`metricas_hibrido_0day*` corta (54 filas en vez de 72). La fila de la **cascada principal** sí
aborta, igual que `cascada_invertida.py`, así que ninguna cifra citable sale de un artefacto de otra
semilla sin que la corrida se caiga o la tabla quede visiblemente corta.
Desde el 2026-08-12 la comprobación es **simétrica en los dos artefactos que lee
`cascada_invertida.py`**: antes el descriptor del híbrido —de donde sale `UMBRAL_CONF`— entraba solo
por el nombre del fichero, sin verificar variante ni semilla. Importa porque ese umbral **es** el
criterio de condena: con uno de otra semilla, `n_condenadas` —la cifra citable— dejaría de
corresponder a la fila que la publica (`cascada_invertida._leer_umbral_conf`).

**Traza de la semilla de los `.joblib` publicados.** La afirmación «los 20 `.joblib` publicados
declaran `semilla = 42`» ya no descansa en la palabra de quien la escribió: la produce
`python app\barrido_semillas.py --solo-verificar`, que lee los descriptores (**cero `fit`**) y deja
la lista completa en `Resultados/verificacion_semilla_joblib.txt`. El veredicto es el mismo en las dos
pasadas que ha tenido: **20 de 20** con `semilla = 42`, todos con `commit=1163c90`.

**Lo que sí cambió es el sello de la cabecera, y era lo previsto.** El fichero que hay en disco a
2026-08-13 es el que **re-selló el paso 3 del runbook** justo antes de lanzar el barrido:
`Commit del código: df30cb2`, `Fecha de la verificación: 2026-08-12T22:07:10`. Ya **no** es el que
versiona `54d1349` (durante la corrida apareció como línea `M` del `git status`, exactamente como el
paso de cierre del runbook manda esperar); **la traza que hay en disco la versiona `9ad971b`**, el
commit de cierre del cómputo de T4, y así lo declara su fila en la tabla de corridas (detalle en el
recuadro de más abajo). La versión anterior, con sello `00c3c3e-sucio` y
fecha `15:57`, sigue siendo recuperable desde `54d1349`.

**Por qué el sello no se retoca nunca a mano, ni el de antes ni el de ahora.** Ese campo es **salida
generada** por `config.commit_actual()`: el de la pasada de las 15:57 decía `00c3c3e-sucio` (árbol
sucio en HEAD=`00c3c3e`, el código del lanzador aún sin commitear) y el de la pasada de las 22:07 dice
`df30cb2`. No es texto editable: retocarlo rompería la correspondencia entre el artefacto y lo que
imprimió el código. El re-anclaje se hace **en la prosa y en la tabla de corridas** —`00c3c3e-sucio` →
`54d1349`—, igual que en `97e679b` se re-ancló `fc1c6b4-sucio` a `9af842c` sin tocar el sello impreso.

La traza sostiene dos cosas: que una corrida por defecto pasa la salvaguarda de mezcla, y que el borrado por
sufijo del lanzador **no puede alcanzar** ninguno de esos 20 ficheros (ninguno lleva la marca
`_semilla`, `config.MARCA_SEMILLA`).

> **Cuándo se re-sella esa traza** (y por qué la frase de arriba no se vuelve falsa al lanzar el
> barrido). La misma verificación corre como **preflight de todo lanzamiento** —`--dry-run`
> incluido: `--dry-run` no ejecuta scripts ni borra `.joblib`, pero **no es una pasada de solo
> lectura**—. En ese papel es una comprobación, no un artefacto: si sale limpia **no reescribe** el
> fichero (`verificar_joblibs_publicados(escribir_si_ok=False)`), así que un `--dry-run` no mueve el
> sello. Se reescribe en dos casos: con
> `--solo-verificar`, que es el modo cuyo propósito *es* producirlo, y cuando el preflight
> **encuentra un problema**, porque entonces el fichero es el diagnóstico del abort. Sin esta
> asimetría, el primer lanzamiento real habría re-sellado la cabecera con otro commit y otra fecha
> y habría dejado esta cita falsa sin que nadie tocase una cifra.
>
> **Pero el propio runbook SÍ re-sella la traza, en su paso 3.** Ese paso es
> `python app\barrido_semillas.py --solo-verificar`, y ese modo reescribe el fichero **siempre**
> (`escribir_si_ok=True` por defecto, `barrido_semillas.py:149-150`) — de hecho el paso de cierre
> **espera** ver la traza como línea `M` en el `git status`. **Y eso es exactamente lo que pasó el
> 2026-08-12 a las 22:07**, al seguir el runbook para lanzar el barrido: el sello pasó de
> `00c3c3e-sucio` / `15:57` a `df30cb2` / `22:07:10`, y la traza dejó de ser la que versiona
> `54d1349`. No es un fallo: es lo que se quiere, porque el sello nuevo identifica la corrida nueva.
> **Re-anclado ya:** la traza que hay en disco —cabecera `Commit del código: df30cb2`,
> `2026-08-12T22:07:10`, verificado en el fichero— es la que versiona **`9ad971b`**, el commit de
> cierre del cómputo de T4, y así lo declara su fila en la tabla de corridas. Aquí el sello es
> **limpio**, así que sí identifica una versión del código; lo que el re-anclaje añade es en qué
> commit quedó versionada esa traza, igual que se hizo con `00c3c3e-sucio` → `54d1349` y antes con
> `fc1c6b4-sucio` → `9af842c`.

**Las diez semillas son `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`** (`config.SEMILLAS_BARRIDO`, con
aserciones al importar: diez valores, sin repetidos y **sin la 42**). La 42 queda fuera por dos
razones y ninguna es de comodidad: (1) `--semilla 42` es **indistinguible de una corrida por
defecto** —el sufijo es cadena vacía y no hay desvío de tablas—, así que ese pase sobrescribiría las
cuatro tablas publicadas, los 20 `.joblib` y las 39 figuras; y (2) la 42 es el **titular** de
5.1-5.3, un punto **independiente** de la banda, no uno de sus diez sumandos. Consecuencia para
`A.3`: por variante hay **once** corridas —diez del barrido más la publicada—, y el titular se cita
**al lado** de la banda, nunca dentro.

**Lo que SÍ varía dentro de cada semilla** (verificado línea a línea contra el código, no deducido
del nombre del flag). Es lo que hay que declarar al citar la banda: sin esta lista, la dispersión se
leería como «solo aleatoriedad de la inicialización del modelo», y es bastante más que eso.

| Qué cambia | Dónde | Qué arrastra |
|---|---|---|
| El **split 80/20 de D1** en `D1_train`/`D1_val` | `anomalias.py:152` (`train_test_split(..., random_state=config.RANDOM_STATE)`) | Los cuatro detectores se ajustan sobre otras filas **y el umbral cambia**: es el percentil 95 del score sobre `D1_val` (`anomalias.py:352`). El umbral es la frontera de decisión de la etapa 1, así que mueve recall y FPR de anomalías **y del híbrido** (su binaria *es* la etapa 1) |
| La **muestra de 5.000 de D3** del set de validación etiquetado | `anomalias.py:161` (`X_D3.sample(random_state=...)`) | Cambia el `auc_val` con el que se **elige la configuración** de cada detector: el ganador del grid puede ser otro |
| La **submuestra de 20.000 de OneClassSVM** | `anomalias.py:244` (`X_train.sample(random_state=...)`) | OneClassSVM no admite `random_state` —es determinista dado el dato—, así que **toda** su variación entre semillas viene de aquí y del split de D1 |
| Los **folds del `StratifiedKFold(5, shuffle=True)`** | `firmas.py:131`, `baseline.py:91`, `hibrido.py:117` | El `f1_macro` de CV con el que se elige el **balanceo ganador de 4.3.4**, el `best_params_` del `GridSearchCV` y las probabilidades **out-of-fold** con las que se calibra `UMBRAL_CONF`: las tres decisiones pueden salir distintas |
| La **inicialización de los modelos** | `IsolationForest`, `MLPRegressor` (pesos + el 10 % interno del `early_stopping`), `DecisionTree`, `RandomForest`, `SMOTE` | La dispersión «clásica» de la semilla. `OneClassSVM`, `LocalOutlierFactor` y `KNN` no la tienen: no aceptan `random_state` |

**Lo que el barrido NO varía, y hay que declararlo igual.** Son **dos** límites, y el segundo se
pasa por alto con facilidad porque no vive en `program.py`:

1. **El preprocesado:** los splits D1/D2/D3, el vocabulario del one-hot, el escalador y la selección
   de las 54 características. `program.py` no está parametrizado por semilla (su `random_state=42` es
   literal y no importa `config.py`), así que las 10 semillas miden la dispersión **de los modelos
   sobre unos splits y un set de características fijos** — no la del preprocesado. Una banda leída
   como si incluyese la variabilidad de la selección de características sería una banda sobrevendida.
2. **El par de la cascada.** `hibrido.py` evalúa el par `(detector=Autoencoder, firma=RandomForest)`,
   **fijado por defecto** en la firma de su constructor (`hibrido.py:94`,
   `def __init__(self, sin_seleccion=False, detector="Autoencoder", firma="RandomForest")`) a partir
   de lo que ganó en el pase de la semilla 42. El barrido **no lo re-elige**: las diez corridas de
   híbrido son diez ajustes de *ese* par, no diez elecciones del mejor par. El matiz, en los dos
   sentidos: en las **diez** semillas de híbrido-54 el Autoencoder gana en `recall_0day` a los otros
   tres detectores —comprobable en `Resultados/metricas_hibrido_0day_semillas.csv`, filas
   `__global__` de la variante `54`: el Autoencoder es la fila de la cascada (`es_cascada = True`) y
   los otros tres las del detector suelto; ese fichero **sí está versionado** (los logs de `Resultados/logs_barrido/`
   no lo están, `.gitignore:56`, así que no sirven de respaldo para un tercero)—, con lo que la
   elección resulta **robusta a la semilla**; el caso más ajustado es la **semilla 9**, donde el AE
   saca **0,756533** frente al **0,755733** del IsolationForest. Pero la **banda de dispersión no
   incluye la variabilidad de esa elección**, y no puede citarse como si la incluyese.

#### El lanzador y el agregador del barrido (escritos el 2026-08-12; corridos el 2026-08-12/13)

Dos scripts nuevos, los dos **fuera** del pipeline del sistema: no entrenan nada del H-NIDS y
ninguno de los cinco scripts de modelos los importa.

- **`app/barrido_semillas.py`** — lanzador desatendido. Recorre las 10 semillas × 2 variantes × 5
  scripts en el orden de dependencias (`anomalias` → `firmas` → `hibrido` → `cascada_invertida`, y
  `baseline` al final: depende del preprocesado pero no del híbrido). Tres propiedades que no son
  extras:
  - **Reanudable.** Antes de cada corrida comprueba si la tabla `*_semillas.csv` de ese paso ya trae
    el recuento **exacto** de filas de esa `(variante, semilla)` —4/4/1/1 de
    `evaluacion.FILAS_ESPERADAS_POR_VARIANTE` y 5 en la cascada invertida— y la salta si sí. El
    barrido corre mientras la máquina se usa para otras cosas, así que tiene que poder cortarse y
    continuar. Se exige el recuento exacto y no «al menos una fila»: una corrida cortada a medias
    puede haber dejado 2 de las 4 filas de anomalías, y darla por hecha dejaría la celda incompleta.
    Para que la reanudación no se atasque, cada paso escribe su `.joblib` **antes** de la fila que
    `ya_hecho()` consulta; `hibrido.py` lo hacía al revés y se corrigió el 2026-08-12 (ver el
    recuadro «La ventana de bloqueo» más abajo).
  - **Borra los `.joblib` de cada semilla al terminarla**, y solo entonces —después de `hibrido.py` y
    `cascada_invertida.py`, que consumen los de su propia semilla, y en las dos variantes a la vez
    porque comparten el sufijo de semilla—. Sin borrado serían **200 ficheros ≈ 4,8 GB**: los
    **20 `.joblib` de un pase ya cubren las dos variantes** (10 de `54` y 10 de `122_sin_seleccion`)
    y ocupan **481,33 MB** medidos el 2026-08-12, así que la cuenta es 481,33 MB × 10 semillas. La
    derivación anterior decía «20 modelos × 10 semillas × 2 sets ≈ 5 GB» y **multiplicaba las
    variantes dos veces**; el «≈5 GB» salía parecido por casualidad. El filtro exige que el nombre
    **termine** en `_semilla<N>.joblib`, con el sufijo compuesto por `config.sufijo_de_semilla()` y no
    por un glob a mano, así que `_semilla1` no puede llevarse `_semilla10` y los 20 publicados quedan
    fuera por construcción.
  - **Falla rápido.** Si un hijo devuelve código ≠ 0, el barrido se detiene y **no** borra los
    `.joblib` de esa semilla: quedan para diagnosticar y la reanudación los reutiliza. Un fallo casi
    nunca es de una semilla concreta —el código es el mismo en las diez— y seguir produciría diez
    veces el mismo error con horas de cómputo en medio.
  - Un **log por corrida** en `Resultados/logs_barrido/` (no versionado). `--dry-run` imprime el plan
    sin ejecutar ningún script ni borrar ningún `.joblib`, pero **sí** hace el preflight de
    verificación y **sí** crea los directorios de salida: no es una pasada de solo lectura (ver el
    recuadro sobre cuándo se re-sella la traza).
- **`app/agregar_semillas.py`** — agregador. Las **bandas** (`n`/media/sd/mín/máx) salen **solo** de
  las `metricas_*_semillas.csv`: construye esas rutas con `config.nombre_tabla_semillas()` y no con
  `config.ruta_tabla()`, que dependería de la semilla global. Emite dos ficheros:
  `Resultados/dispersion_semillas.csv` y `Resultados/dispersion_semillas.md`, este último con la
  tabla ya formateada para pegarla en `A.3` sin recalcular nada a mano.
  - **Lectura sí, escritura no** (cambió el **2026-08-13**; antes esta ficha decía «nunca abre las
    nueve publicadas», y eso ya no describe el código). Desde que el agregador emite él mismo el
    titular «N de M celdas fuera de banda», `_leer_publicada()` **abre las nueve tablas publicadas en
    modo LECTURA** —`pd.read_csv`, cacheada por fichero— para recuperar el valor de la semilla 42 de
    cada celda. La distinción es la garantía que importa y por eso se escribe con estas palabras:
    **ninguna tabla publicada se escribe jamás**, y el script lo comprueba antes de empezar en
    `_comprobar_salidas_no_publicadas()`, que contrasta sus dos rutas de salida **por nombre y por
    ruta absoluta** contra las de todas las publicadas y las del barrido. Las **bandas** siguen sin
    tocar las publicadas: de ahí sale únicamente el punto de comparación.
  - Agrupa por `(set_features, algoritmo, alcance)` —la `CLAVE_UNICIDAD` de las tablas **sin**
    `semilla`, que es el eje sobre el que se agrega— y da `n`, media, **sd muestral (`ddof=1`)**, mín
    y máx a **4 decimales**. `ddof=1` porque las diez semillas son una muestra, no la población.
  - **El `.md` tiene que llevar `alcance` y `tabla_origen`, igual que el CSV.** Sin ellos la etiqueta
    del `.md` es ambigua justo en el artefacto que T7 pega en `A.3`: «54 · RandomForest» nombra por
    igual el **clasificador de firmas** y la **medición contrafactual** de la cascada invertida, dos
    medidas incompatibles. Es el defecto que cerró T1 y el CSV ya lo evitaba (comentario de `alcance`
    en `_agregar_metrica`). Corregido en el código el **2026-08-13** —`_tabla_md()` emite las dos
    columnas y recorta el `alcance` a 70 caracteres, con el texto íntegro en la columna del CSV— y el
    agregador se **re-ejecutó** a continuación, así que el `dispersion_semillas.md` que hay en disco
    **ya las lleva**: sus **198 filas** traen `Tabla de origen` y `Alcance`. Ese `.md` en disco es
    el de la **quinta** pasada del agregador, la que estrena `comparaciones_pareadas.csv`: su
    cabecera dice `commit_agregador = 0276039-sucio` (verificado en disco el
    2026-08-17, no deducido del código; la marca temporal la declara el propio artefacto y esta prosa
    no la copia, que caducaría en la siguiente re-corrida). El histórico de las cinco pasadas, con qué sello dejó cada una y los
    **re-anclajes** de los sellos de la segunda a la quinta —`df30cb2-sucio` →
    **`9ad971b`**, `ddade37-sucio` → **`9d4c26d`**, `6bb224c-sucio` → **`1cb5c26`** y
    `0276039-sucio` → **`98a0289`**—, están más abajo, en «Lo
    que dio la primera ejecución real», y en la tabla de corridas.
  - **Aborta** si a alguna combinación le falta alguna semilla, le sobra una ajena o le aparece
    repetida. Una media de 7 puntos rotulada como de 10 es peor que no tener tabla, y nadie la
    detecta releyendo la tabla.
  - Métricas agregadas, lista cerrada: anomalías `roc_auc`/`pr_auc`/`f1`/`fpr`/`umbral`; firmas
    `f1_macro`/`accuracy_D2`/`recall_macro`/`f1_u2r`; baseline
    `bin_accuracy`/`bin_fpr`/`f1_macro`/`recall_0day_global`; híbrido
    `bin_recall`/`bin_fpr`/`bin_accuracy`/`conocida_f1_macro`/`recall_0day_global`/`fpr_cascada`/
    `umbral_conf_elegido`; cascada invertida `n_condenadas` **y** `tasa_condena` de la fila
    `__global__`. Las dos de la cascada y no solo la tasa aunque una sea la otra reescalada por un
    denominador constante (las 9.711 normales de D2): **lo citable es `n_condenadas`** —así lo
    declaran esta ficha y `config.ALCANCE_CASCADA_INVERTIDA`—, y con solo la tasa a 4 decimales
    habría que multiplicar por 9.711 **a mano** para recuperarla, cálculo manual que este proyecto no
    admite y que además perdería ~1 flujo de resolución.
  - **Procedencia por celda, con dos sellos que no son el mismo.** `commits_origen` trae el conjunto
    distinto de commits de las diez filas agregadas —el que vale para citar la banda— y
    `commit_agregador` es el del **agregador** (con qué versión de `agregar_semillas.py` se
    calcularon media y sd). Se llama `commit_agregador` y **no** `commit`: en las nueve
    `metricas_*.csv` esa columna significa «el código que produjo la fila» y aquí significaría «el
    del agregador, que no produjo ninguno de los diez puntos» — el homónimo con dos significados
    que prohíbe la regla de `config.py:326-332`, y esta tabla no pasa por
    `guardar_metricas()`/`validar_esquema_minimo()`, así que el nombre distinto es la única red. El
    script **avisa** si una celda mezcla commits, y el `.md` lista los dos sellos por separado en su
    cabecera. Importa porque el barrido es reanudable y puede correrse a lo largo de días: basta que
    cambie el sufijo `-sucio` para que una celda deje de venir de una sola versión del código, y
    sellarla con el commit del agregador publicaría diez puntos rotulados con un commit que no
    produjo ninguno de ellos.
  - **Avisa si una DECISIÓN no es constante dentro de la celda** (`balanceo`, `config_ganadora`), con
    el reparto —«SMOTE en 7 semilla(s) · class_weight en 3»— y **sin abortar**. El reparto es
    **columna del CSV** (`decisiones_no_constantes`, vacía si la decisión fue la misma en las diez) y
    no solo aviso del `.md`: si `A.3` se armase desde la tabla, un aviso que vive en otro fichero
    dejaría invisible la mezcla justo en la fila cuya media la promedia. Los folds del
    `StratifiedKFold` mueven el balanceo ganador de 4.3.4 y el `best_params_` del `GridSearchCV`, y el
    balanceo por algoritmo es una decisión **cerrada con n=1**: sin este aviso, `A.3` publicaría la
    media de `f1_macro` de RandomForest sobre diez modelos entrenados con dos esquemas de balanceo
    distintos sin decirlo. No aborta a propósito: que la decisión voltee en 3 de 10 semillas es un
    **hallazgo para 5.4**, no un error del barrido.
  - Las **columnas de tiempo van en bloque aparte**, rotulado como *dispersión de máquina* y con la
    razón escrita en el propio fichero: el wall-clock dispersa hasta **4,8×** entre corridas en
    máquina no dedicada con calidad idéntica al bit (Autoencoder-54: 37,71 → 181,91 s, dato de T1) y
    con el recuento de épocas igual en lo medido (mismos valores en las dos corridas que lo
    registran, una de ellas —`ac496cb`— no reproducible desde git), así que su sd mide carga de
    máquina, no algoritmo.
    `alcance_tiempo_s` **no** se agrega —es prosa, no un número—; en su lugar se comprueba que sea
    constante dentro de cada celda.
  - **No decide nada:** no dice si dos intervalos se solapan ni calcula p-valores. Eso lo escribe T11
    en prosa, y la renuncia al contraste (10 puntos sobre un único dataset) va declarada.

##### Lo que dio la primera ejecución real (2026-08-12/13)

El barrido corrió del **2026-08-12 22:09 al 2026-08-13 00:38** y el agregador a continuación
(`python app\agregar_semillas.py` sin flags, desde `Implementacion/`). **El agregador se ha ejecutado
cinco veces**, y conviene declararlo porque cada pasada re-sella sus artefactos y solo la última
es la que hay en disco:

| Pasada | Cuándo | Qué la motivó | Sello que dejó | Estado del sello |
|---|---|---|---|---|
| 1.ª (7,2 s) | 2026-08-13 madrugada | la agregación inicial | *(sobrescrito)* | — |
| 2.ª (1,70 s) | 2026-08-13 `07:43:40` | el arreglo de `_tabla_md()` (columnas `Tabla de origen` y `Alcance`) | `commit_agregador = df30cb2-sucio` | **re-anclado en prosa a `9ad971b`** (recuadro del final de esta subsección y tabla de corridas) |
| 3.ª | 2026-08-13 `19:54:48` | el **titular automático**: el agregador pasa a comparar la semilla 42 contra cada banda y a emitir «N de M» | `commit_agregador = ddade37-sucio` | **re-anclado en prosa a `9d4c26d`** (recuadro del final de esta subsección y tabla de corridas), el commit que cerró la automatización del titular. Ojo: bajo ese mismo sello hubo **dos** invocaciones —esta, de las `19:54:48`, y una regeneración a las `20:13:37` tras los arreglos del `auditor-ml`—, y la que `9d4c26d` versiona es la de las `20:13:37`. *(sobrescrito en disco por la 4.ª, pero el sello sigue nombrando esta pasada)* |
| 4.ª | 2026-08-14 `15:15:13` | el **reparto por commit de origen del titular**: la salvedad de procedencia del `.md` pasa a decir cuántas de las 98 celdas casadas aporta cada `commit_semilla_42` y cuántos «fuera» salen de cada uno (`_reparto_commits_titular_md()`) | `commit_agregador = 6bb224c-sucio` | **re-anclado en prosa a `1cb5c26`** (recuadro del final de esta subsección y tabla de corridas). *(sobrescrito en disco por la 5.ª, pero el sello sigue nombrando esta pasada)* |
| 5.ª | 2026-08-17 *(hora en la cabecera del artefacto)* | el **recuento pareado por semilla**: el agregador estrena `comparaciones_pareadas.csv` (13 filas de datos) y añade al `.md` la sección «Comparaciones pareadas por semilla» | `commit_agregador = 0276039-sucio` | **re-anclado en prosa a `98a0289`** (recuadro del final de esta subsección y tabla de corridas), el commit que versiona a la vez el código del recuento pareado y los tres artefactos |

**Los ficheros que hay en disco son los de la quinta —ya son TRES, no dos** (`commit_agregador =
0276039-sucio`, verificado en disco el 2026-08-17; la marca temporal, en la cabecera de cada uno). Cero `fit` en las cinco: el agregador solo lee CSV. Salida:
`dispersion_semillas.csv` y `.md`, **198 filas** = 98 de *calidad* + 100 de *dispersión de máquina*,
con `commits_origen = df30cb2` **único** en todas las celdas (ninguna mezcla versiones del código).
Las nueve tablas publicadas de la
semilla 42 quedaron **bit a bit
idénticas** y `Resultados/modelos/` no contiene ningún `.joblib` con sufijo `_semilla`: el borrado por
semilla funcionó. Cuatro hallazgos, y los cuatro son material citable — de **`A.3`** (T7) y de
**`5.4`** / **`5.2`** (T11):

1. **La decisión de balanceo de 4.3.4 NO es constante entre semillas.** En DecisionTree y
   RandomForest —los dos algoritmos donde el eje es SMOTE vs `class_weight`—, `class_weight` gana en
   **17 de las 40** celdas (variante × algoritmo × semilla): **54-DT 3, 54-RF 5, 122-DT 5, 122-RF 4**;
   SMOTE gana en las 23 restantes. Eso importa porque el balanceo por algoritmo es una decisión
   **cerrada con n=1** (el pase de la 42). Queda capturado donde tiene que estar, en la columna
   `decisiones_no_constantes`, **poblada en 140 de las 198 filas** (**15** celdas distintas). La
   `config_ganadora` del `GridSearchCV` tampoco es constante: **IsolationForest-122 da 5
   configuraciones distintas en 10 semillas**, y el baseline RF alterna `n_estimators` **100 y 300 a
   5/5**.
2. **Los dos huecos que motivaron T4 se resuelven en sentidos opuestos.**
   - Firmas **RandomForest vs HistGradientBoosting** (`f1_macro`, set 54): **el orden NO queda
     establecido.** Las bandas [mín, máx] solapan de par en par —RF **[0,7779–0,8205]** ∩ HGB
     **[0,7680–0,8327]**—, solapan también a ±1 sd, y el **máximo de HGB supera la media de RF**. Lo
     único que se sostiene es la observación **pareada**: RF > HGB en **8 de 10** semillas, en las dos
     variantes.
   - Anomalías **Autoencoder vs IsolationForest** (`f1`): **el orden SÍ queda establecido.** Bandas
     **disjuntas** en 54 —AE [0,8492–0,8934] vs IF [0,8062–0,8428]— y AE > IF en **10 de 10**
     semillas.
3. **Aviso de esquema, para quien cite el contraste de anomalías.** `accuracy` **no** está en la lista
   cerrada de `ESPECIFICACION` para anomalías (solo `roc_auc`, `pr_auc`, `f1`, `fpr`, `umbral`), así
   que el contraste publicado **0,8605 vs 0,8257** de la semilla 42 **no aparece** en
   `dispersion_semillas.csv`. Calculado directo de `metricas_anomalias_semillas.csv` también sale
   disjunto y 10/10, pero **quien lo cite debe decir de dónde sale** — de la tabla de semillas, no de
   la de dispersión.
4. **La semilla 42 cae fuera de la banda [mín, máx] en 13 de las 98 celdas de calidad.** Aviso previo
   al recuento, porque sin él se recuenta y salen 88: de esas **98 celdas de calidad, 10 son
   umbrales** —8 de `umbral` (4 detectores × 2 variantes) y 2 de `umbral_conf_elegido` (híbrido × 2
   variantes)—, que **no** son métricas sobre D2 y se agregan a propósito porque son justo lo que el
   barrido pone a prueba (`agregar_semillas.py:86-90`; lista cerrada de métricas más arriba). Importa
   aquí y no en otro sitio porque **uno de los tres empates del borde es un umbral**, así que
   descontarlos rompería el titular «13 de 98». *(Ese aviso **no** llegó al `.md` en la regeneración
   del 2026-08-13 19:54, aunque la ficha lo daba por prometido. El texto lo emite el script, así que
   se ha añadido a `agregar_semillas.py` —`_nota_no_metricas_md()`, en la sección «El titular (semilla
   42) frente a la banda»—, y **calculado, no escrito a mano**: el desglose 8 + 2, el denominador 88
   que saldría al descontarlos y el hecho de que uno de los tres empates de borde sea un umbral los
   cuenta el propio agregador. **El `.md` en disco ya lo lleva**, verificado en el fichero el
   2026-08-14: la sección del titular trae el desglose 8 + 2, el denominador 88 y los tres empates de
   borde con la marca de que uno es un umbral.)*
   El recuento
   compara la 42 contra los valores de las diez semillas **con la precisión con la que se persistieron
   los CSV de origen** (6 decimales), **no** contra los redondeados a 4 decimales que publica
   `dispersion_semillas.md`: a 4 decimales hay márgenes que desaparecen y el recuento saldría otro.
   Lista completa, por tabla:
   - **Anomalías (7):** 54-IF `pr_auc` 0,918074 < mín 0,919704 · 54-AE `pr_auc` 0,909239 < mín
     0,920772 · 54-OCSVM `roc_auc` 0,835981 > máx 0,835884 · 122-IF `roc_auc` 0,945888 < mín 0,947293 ·
     122-IF `pr_auc` 0,951087 < mín 0,954561 · 122-OCSVM `fpr` 0,083411 > máx 0,082999 · 122-LOF `fpr`
     0,165894 > máx 0,163526.
   - **Firmas (5):** 54-RF `f1_macro` 0,822286 > máx 0,820494 · 54-RF `recall_macro` 0,849576 > máx
     0,837002 · 54-HGB `accuracy_D2` 0,957723 > máx 0,953760 · 122-RF `f1_macro` 0,695587 < mín
     0,715524 · 122-RF `recall_macro` 0,745847 < mín 0,748005.
   - **Híbrido (1):** 122 `recall_0day_global` 0,785333 > máx 0,780000.
   - **Baseline (8 celdas) y cascada invertida (4): todas DENTRO.**

   El caso de **54-OCSVM `roc_auc` tiene un margen de 1e-4** —dentro del ruido de redondeo—, así que no
   se presenta al mismo nivel que el de firmas 54-RF. Y **los empates cuentan como DENTRO**, criterio
   que hay que declarar porque decide el recuento: **tres** celdas caen en el **borde exacto** (firmas
   122-RF `f1_u2r` 0,318182 = mín, firmas 122-KNN `f1_u2r` 0,197183 = máx, híbrido-122
   `umbral_conf_elegido` 0,5000 = máx) y contándolas como fuera saldrían **16** en vez de 13.

   **El caso relevante es firmas 54-RF:** el `f1_macro` publicado (**0,8223**) está por encima del
   máximo de las diez semillas (**0,8205**) y su media es **0,8035**; o sea, el titular publicado del
   clasificador de firmas es el punto **más favorable** de las once corridas, no el centro. En 122 el
   mismo modelo cae al **otro** lado (`f1_macro` 0,6956 < mín 0,7155). Eso **no invalida ningún
   titular** —cada cifra publicada es el resultado real de su corrida—, pero obliga a **declarar la
   banda junto al titular** en `5.2`.

   **Procedencia del recuento: lo produce el script, desde el 2026-08-13.** Hasta esa fecha esta
   ficha advertía lo contrario —«este recuento no lo produce ningún script… las 13 celdas salen de
   cálculo manual»—, y era cierto cuando se escribió; **ya no lo es**, y el ancla que citaba
   (`agregar_semillas.py:29-32`) dice hoy justo lo opuesto. Lo que hace el código actual:
   `_valor_semilla_42()` **abre en lectura** la tabla publicada homóloga —única lectura de una tabla
   publicada en todo el script, y nunca una escritura— y casa la fila de la semilla 42 por tabla,
   `CLAVE_AGRUPACION` completa (incluido el TEXTO de `alcance`), filtro de la `ESPECIFICACION` y
   `semilla = 42`, exigiendo **exactamente una** fila; `_comparar_con_titular()` la compara contra
   `min_crudo`/`max_crudo` (los extremos con la precisión del CSV de origen, 6 decimales) y
   `_recuento_titular()` emite «N de M». El «NO DECIDE NADA» del encabezado sigue vigente pero acotado
   a lo que siempre significó: **no** dice si dos intervalos se solapan ni calcula p-valores. Una
   celda que no case queda **fuera de las dos cifras** —ni numerador ni denominador— y se avisa.
   Consecuencia práctica: **si alguna de esas tablas se mueve, el recuento no se recuenta a mano, se
   vuelve a correr el agregador**.

> **Sexto re-anclaje de sello del proyecto, ya HECHO, y ninguno PENDIENTE (2026-08-17).** *(Este
> encabezado dijo lo contrario entre el 2026-08-16 y el 2026-08-17, con razón: la re-corrida de
> `validacion.py` del 2026-08-16 salió con sello `a8c20e9-sucio` y arrastraba un séptimo re-anclaje.
> **Ese pendiente se cerró SIN re-anclaje**, que es la vía preferible: `validacion.py` se volvió a
> correr el **2026-08-17 con el árbol limpio**, los seis artefactos llevan hoy el sello limpio
> **`ac36b88`** con las mismas cifras, y un sello limpio no necesita anclarse a nada porque ya
> identifica el código. El quinto re-anclaje, `6bb224c-sucio` → `1cb5c26`, sigue siendo válido.)*
> Los cinco anteriores,
> todos citados arriba, son `fc1c6b4-sucio` → `9af842c`, `00c3c3e-sucio` → `54d1349`, `df30cb2-sucio` →
> `9ad971b`, `ddade37-sucio` → `9d4c26d` y `6bb224c-sucio` → `1cb5c26`.
>
> **El tercero, hecho, es el de la SEGUNDA pasada del agregador:** `dispersion_semillas.csv`/`.md`
> llevaron impreso `commit_agregador = df30cb2-sucio`, y ese sello **queda intacto**: el re-anclaje se
> hace **en prosa**, y su commit de cierre es **`9ad971b`** —el que versiona a la vez
> `agregar_semillas.py` y los dos artefactos de dispersión—, igual que se hizo `00c3c3e-sucio` →
> `54d1349` y `fc1c6b4-sucio` → `9af842c`. Está anclado en dos sitios: aquí y en la **tabla de
> corridas** de más arriba, que le dedica su propia fila. **La versión del código que produjo aquella
> agregación es `9ad971b`, no `df30cb2`.**
>
> **El cuarto, hecho el 2026-08-14, es el de la TERCERA pasada** (2026-08-13 `19:54:48`,
> `commit_agregador = ddade37-sucio`, la del titular automático): su commit de cierre es **`9d4c26d`**
> —«codigo: automatizar el titular "13 de 98" en el agregador de semillas», que versiona a la vez
> `agregar_semillas.py` y los dos artefactos de dispersión—, y `ddade37` es el commit **anterior** al
> cambio, verificado con `git show --stat 9d4c26d` y `git log --follow` sobre el script el
> 2026-08-14. El sello impreso **no se toca**; el re-anclaje va en prosa, aquí y en la tabla de
> corridas. **Con una salvedad que hay que declarar al citarlo:** ese sello nombra **dos**
> invocaciones —la de las `19:54:48`, que es la que tabulan esta subsección y la tabla de corridas, y
> una **regeneración a las `20:13:37`** tras aplicar los cinco hallazgos altos del `auditor-ml`—, y la
> que quedó versionada en `9d4c26d` es la **segunda** (`git show 9d4c26d:Resultados/dispersion_semillas.md`
> da cabecera `2026-08-13T20:13:37`). Para la corrida de las `19:54:48` el re-anclaje apunta a ese
> mismo código **antes** de los arreglos del auditor, un estado que no se versionó por separado. Las
> cifras —198 filas y «13 de 98»— son idénticas en las dos. Es el mismo patrón de «un sello, dos
> corridas» que ya documenta `00c3c3e-sucio` en la tabla de corridas.
>
> **El quinto, hecho el 2026-08-14, es el de la CUARTA pasada** (2026-08-14 `15:15:13`, la del
> reparto por commit de origen del titular), que **fue** la que había en disco hasta la quinta pasada
> del 2026-08-17: sus dos artefactos
> llevan impreso `commit_agregador = 6bb224c-sucio`, y ese sello **queda intacto**. `6bb224c` es el
> commit **anterior** al cambio y por tanto **no identifica la versión que produjo la agregación**; su
> commit de cierre es **`1cb5c26`** —«codigo+informe: cerrar la Fase 2 - Tanda 2, ficha del sistema y
> reconciliacion de sellos», del 2026-08-14, que arrastra a la vez `agregar_semillas.py` y los dos
> artefactos de dispersión, que venían sin commitear de la sesión anterior—, verificado con
> `git log --oneline 1cb5c26` el 2026-08-14, no deducido de la prosa. El sello impreso **no se toca**;
> el re-anclaje va en prosa, aquí y en la tabla de corridas. **Con esto no quedaba ningún re-anclaje
> pendiente *a fecha de 2026-08-14*** — afirmación acotada a esa fecha, que quedó en suspenso con la
> re-corrida de `validacion.py` del **2026-08-16** (`a8c20e9-sucio`) y **volvió a ser cierta el
> 2026-08-17**, cuando esa corrida se rehízo con el árbol limpio y su sello pasó a `ac36b88`, que no
> necesita anclaje. Los re-anclajes anteriores **siguen siendo válidos para lo que nombran**: cada
> uno, su pasada. Ninguno es un ancla huérfana ni se borra; simplemente ya no describen el fichero que
> hay en disco, y por eso las cinco pasadas están tabuladas más arriba con el sello de cada una.
>
> **El sexto, hecho el 2026-08-17, es el de la QUINTA pasada** (2026-08-17, la del recuento
> pareado por semilla), que es la que hay hoy en disco: sus **tres** artefactos —`dispersion_semillas.csv`,
> `dispersion_semillas.md` y el nuevo `comparaciones_pareadas.csv`— llevan impreso
> `commit_agregador = 0276039-sucio`, y ese sello **queda intacto**. `0276039` es el commit
> **anterior** al cambio —«informe: separar en 3.5 los dos "8 de 10" homonimos»— y por tanto **no
> contiene el código que produjo los artefactos**; el commit que sí lo contiene es **`98a0289`**
> («codigo: emitir el "8 de 10" pareado desde agregar_semillas.py y corregir el residuo de T22»), que
> versiona a la vez el cambio de `agregar_semillas.py` y los tres artefactos, verificado
> con `git show --stat 98a0289` el 2026-08-17 y no deducido de la prosa. El sello impreso **no se
> toca**; el re-anclaje va en prosa, aquí, en la tabla de pasadas y en la tabla de corridas. **El
> pendiente que arrastraba `validacion.py`** (`a8c20e9-sucio`) **no se cerró con este re-anclaje sino
> re-corriendo el script con el árbol limpio** el 2026-08-17: su sello es hoy `ac36b88`, limpio.
>

> **Aviso de estado, 2026-08-14:** esa cuarta regeneración **ya se ha corrido** (2026-08-14
> `15:15:13`) y el `.md` en disco **ya lleva** el reparto por commit de origen del titular: la
> salvedad de procedencia dice hoy que de las 98 celdas casadas `1163c90` aporta **94** (13 fuera de
> banda) y `274923d-sucio` **4** (ninguna fuera), contado celda a celda desde `commit_semilla_42` por
> `_reparto_commits_titular_md()` y nunca escrito a mano. **Eso es lo único que añadió esta pasada**:
> la nota de las 10 celdas que son umbrales y la salvedad de procedencia del titular **ya estaban en
> el `.md`** desde antes —el aviso previo las atribuía por error a esta regeneración—. Y, como estaba
> previsto, la pasada **volvió a re-sellar los dos artefactos con otra fecha y otro
> `commit_agregador`**; esta subsección y la tabla de las pasadas se han releído **contra el fichero
> en disco** el 2026-08-14 antes de darlas por buenas.
>
> **La razón es estructural, y con escribirla una vez basta para los seis casos: un artefacto
> versionado que estampa `config.commit_actual()` no puede llevar nunca el hash del commit que lo
> versiona, porque tiene que existir antes de ese commit.** De ahí se sigue lo demás: regenerarlo
> después del cierre no arregla nada —volvería a salir como línea `M` del `git status` y exigiría un
> segundo commit, que a su vez tampoco estaría en el sello—, así que no se regenera y el desajuste se
> resuelve en el texto, no en el fichero.
>
> **Y el `-sucio` no contamina la cita**, en ninguna de las cinco pasadas. Lo que respalda la
> banda es `commits_origen = df30cb2` **limpio** —los diez puntos de cada celda—; `commit_agregador`
> solo dice con qué versión del agregador se calcularon media y sd. Además el sufijo está **acotado a
> `Implementacion/`** (`config.py:783-822`, `_RUTA_SUCIEDAD`): no señala nada del dataset ni de los
> resultados, sino exactamente el cambio de `agregar_semillas.py` todavía sin commitear cuando corrió
> cada pasada — el arreglo de `_tabla_md()` en la segunda, el titular automático en la tercera, el
> reparto por commit de origen del titular en la cuarta y el recuento pareado por semilla en la quinta.
>
> **Lo que el `-sucio` sí obliga a mirar en la tercera pasada, y es otra cosa:** el titular y la banda
> **no salen del mismo commit**. `commits_origen` es `df30cb2` en las 198 celdas, pero
> `commit_semilla_42` es **`1163c90`** en 94 de las celdas de calidad y **`274923d-sucio`** en las 4
> de la cascada invertida (verificado en `dispersion_semillas.csv` el 2026-08-14). Es la cronología
> normal del proyecto —el titular se publicó antes de que existiera el barrido— y **no invalida
> nada**: cada cifra es el resultado real de su corrida. Pero es una **salvedad de procedencia** que
> hay que declarar al citar «13 de 98», porque parte de la distancia de una celda podría ser **deriva
> de código** entre esas versiones y no dispersión por semilla. El agregador la emite desde el
> 2026-08-13 en la sección del titular del `.md` (`_nota_procedencia_titular_md()`), comparando los
> dos conjuntos de commits; **el `.md` en disco sí la lleva** —y desde la cuarta pasada
> (2026-08-14 `15:15:13`) lleva además el **reparto**: `1163c90` aporta 94 celdas casadas con las 13
> fuera de banda y `274923d-sucio` las otras 4 con ninguna fuera, contado por
> `_reparto_commits_titular_md()`— y la columna `commit_semilla_42` del CSV la da celda a celda desde
> la tercera pasada.

**La ventana de bloqueo de la reanudación (corregida el 2026-08-12, antes de correr el barrido).**
`hibrido.py` escribía su fila resumen **antes** de volcar el descriptor `hibrido_<sufijo>.joblib`. Con
ese orden, un corte del proceso entre las dos escrituras dejaba el barrido **atascado**, no solo
incompleto: al relanzar, `barrido_semillas.ya_hecho()` daba el paso por hecho —la fila estaba— pero
`cascada_invertida.py` abortaba porque el descriptor de donde lee `UMBRAL_CONF` no existía, y cada
relanzamiento volvía a fallar en el mismo punto hasta que alguien borrase la fila a mano. Ahora
`hibrido._persistir()` vuelca **primero** el descriptor y **después** la fila, con lo que la ventana
se invierte y se vuelve inocua: un corte ahí deja un descriptor huérfano, `ya_hecho()` devuelve
`False` y la reanudación reejecuta el paso y lo sobrescribe. Es el orden que ya seguían `anomalias.py`,
`firmas.py` y `baseline.py` (`.joblib` antes que CSV), así que la corrección lo **unifica**: en los
cinco scripts, la fila de métricas es lo último que se escribe. Ni una cifra cambia — es solo el
orden de dos escrituras.

**Qué del barrido se versiona y qué no.** Se versionan las nueve `metricas_*_semillas.csv` y
`dispersion_semillas.csv`/`.md` (texto plano, y son lo citable). Quedan **fuera** del repositorio,
por el mismo criterio —del barrido no se cita ninguno—: los `.joblib` (`Resultados/modelos/` entero),
las ~260 figuras `*_semilla*`, los ~100 logs de `logs_barrido/` y los **20
`firmas_reglas_*_semilla*.txt`** que deja `firmas.py`. Los cuatro patrones están en el `.gitignore`
raíz; los artefactos homólogos de la semilla 42 no llevan la marca `_semilla` y siguen versionados.

**Estado, verificado en disco el 2026-08-13:** el barrido **está corrido y agregado** (2026-08-12
22:09 → 00:38, sello `commit = df30cb2`). Existen las nueve `metricas_*_semillas.csv` (**2.320
filas**), `dispersion_semillas.csv` y `dispersion_semillas.md` (**198 filas**), **260** figuras
`*_semilla*` en `Resultados/figuras/`, **100** logs en `Resultados/logs_barrido/` y **20**
`firmas_reglas_*_semilla*.txt`, más la traza `verificacion_semilla_joblib.txt`. Todo lo descrito
arriba —`commits_origen`, `commit_agregador`, `decisiones_no_constantes`, `n_condenadas` agregada, el
nuevo orden de escritura de `hibrido.py`— ya tiene salida en disco, no es solo código. `Resultados/`
sigue **sin ningún `.joblib` con sufijo `_semilla`**: el borrado por semilla del lanzador funcionó, y
las nueve tablas publicadas de la 42 quedaron **bit a bit idénticas**.

Las dos vías de solo-comprobación del lanzador siguen disponibles y siguen sin producir ni una cifra
nueva: `--solo-verificar` recorre los `.joblib` de `Resultados/modelos/` sin la marca `_semilla`, lee
su descriptor y comprueba que los 20 declaran `semilla = 42` (cero `fit`), y `--dry-run` imprime el
plan completo —los comandos de las 100 corridas y qué `.joblib` borraría— ejecutando igual ese
preflight y `config.ensure_dirs()`, pero sin lanzar ningún script hijo ni borrar nada.

#### Runbook del barrido de semillas (escrito el 2026-08-12, antes de lanzarlo)

Esta ficha es **operativa**: qué se teclea, en qué directorio, qué hay que comprobar antes, cuántas
filas debe haber al acabar y cómo se verifica que la semilla 42 no se movió. **No repite** lo que
explica la ficha anterior (*El lanzador y el agregador del barrido*): la reanudabilidad, el borrado de
los `.joblib` por semilla, la ventana de bloqueo de `hibrido.py` y qué se versiona y qué no están
allí, y allí se leen.

**Desde qué directorio, y por qué aquí dice otra cosa que el runbook de T1.** Los dos son correctos y
no se contradicen en el resultado, solo en la forma de escribir el comando:

| Runbook | Directorio de trabajo | Forma de la invocación |
|---|---|---|
| Reconstrucción de las tablas (T1, más arriba en este documento) | `Implementacion/app/` | `python anomalias.py` |
| Barrido de semillas (este) | `Implementacion/` | `python app\barrido_semillas.py` |

El cwd **no cambia ningún artefacto**: todas las rutas de datos y de salida son absolutas y salen de
`config.py` (`config.RESULTADOS_DIR` es una ruta literal absoluta, y `FIGURAS_DIR`/`MODELOS_DIR`
cuelgan de ella). Lo único que cambia es la ruta con la que se nombra el script. Para el barrido el
cwd correcto es `Implementacion/` porque es el que el propio lanzador **fija a sus procesos hijo**
(`barrido_semillas.py:128-134`, `subprocess.run(..., cwd=self.dir_impl)` en la línea 366): tecleando
desde ahí, lo que se ve por consola es lo mismo que el barrido hace por dentro. El `import config`
funciona igual en los dos casos porque Python pone el directorio **del script** (`app/`) a la cabeza
de `sys.path`, no el cwd.

**El bloque completo, copiable de una vez** (PowerShell, desde la raíz del repositorio
`Working_Directory/`):

```powershell
# 0. ÁRBOL LIMPIO ANTES DE LANZAR: debe salir VACÍO. Si sale algo, NO se lanza el
#    barrido: primero se cierra el commit (lo hace el skill `cierre`, en hilo
#    principal y preguntando) y luego se vuelve a comprobar aquí.
git status --porcelain -- Implementacion

# 1. Entorno
cd Implementacion
.\Imp\Scripts\Activate.ps1

# 2. PREFLIGHT MANUAL: no puede quedar residuo de una corrida previa a medias.
#    Debe salir VACÍO (ver más abajo por qué esto no es limpieza cosmética).
#    OJO: se excluye verificacion_semilla_joblib.txt a propósito. Esa traza casa con
#    *_semilla*, está versionada en 54d1349 y es PERMANENTE: no es residuo. Sin la
#    exclusión el comando nunca saldría vacío y la comprobación se volvería ruido.
Get-ChildItem -Recurse ..\Resultados -Filter *_semilla* |
  Where-Object { $_.Name -ne 'verificacion_semilla_joblib.txt' } |
  Select-Object FullName

# 3. Verificar los .joblib publicados (cero fit; reescribe la traza)
python app\barrido_semillas.py --solo-verificar

# 4. Plan sin ejecutar nada (sí hace el preflight de la 42 y crea directorios)
python app\barrido_semillas.py --dry-run

# 5. El barrido: 10 semillas x 2 sets x 5 scripts = 100 corridas, reanudable
python app\barrido_semillas.py

# 6. La tabla de dispersión para A.3
python app\agregar_semillas.py
```

**Los tres prerrequisitos de los pasos 0, 2 y 4, con su razón.**

0. **El árbol tiene que estar limpio ANTES de lanzar** — es una **comprobación** que teclea el
   operador (paso 0), no un `git commit` que se lance desde el runbook: el commit lo hace el skill
   `cierre`, en hilo principal y preguntando. La razón es la procedencia:
   `config.commit_actual()` (`config.py:783-822`) sella el hash con sufijo **`-sucio`** si hay
   cambios sin commitear en `Implementacion/`, y ese sello se estampa en la columna `commit` de cada
   fila que escriba la corrida. Lanzar con el árbol sucio haría nacer las 2.320 filas de las nueve
   `metricas_*_semillas.csv` con un sello **no recuperable desde git** —`<hash>-sucio` no identifica
   ningún estado del código— y **no hay re-anclaje posible a posteriori**: la única forma de arreglarlo
   sería volver a correr el barrido entero, 4-5 h.

1. **Cero residuo con marca `_semilla` y ninguna `metricas_*_semillas.csv` de una corrida previa a
   medias.** Hay que **comprobarlo** con el comando del paso 2 (y borrar a mano lo que aparezca)
   **antes** de lanzar. El motivo no es el orden: `barrido_semillas.ya_hecho()` decide si una
   `(variante, semilla)` está hecha **leyendo las filas de esas tablas**, así que una tabla dejada por
   una corrida anterior —sobre todo si la produjo código sin commitear— hace que la reanudación tome
   la celda por hecha y **se salte un paso del barrido real**, publicando una banda con un punto que
   no salió de este pase. El filtro `*_semilla*` alcanza a la vez los `.joblib` de
   `Resultados/modelos/`, las figuras `Resultados/figuras/*_semilla*`, los
   `firmas_reglas_*_semilla*.txt`, los logs de `logs_barrido/` y las propias
   `metricas_*_semillas.csv` (la cadena `_semillas` contiene `_semilla`). Y **no** alcanza nada de la
   semilla 42: los nombres de artefacto de la corrida los gobierna `config.sufijo_semilla()`
   (`config.py:203-213`), que con la 42 devuelve cadena vacía.
2. **`--dry-run` primero.** Imprime las 100 invocaciones y qué `.joblib` borraría, sin ejecutar
   ningún hijo. No es una pasada de solo lectura: hace el preflight de la 42 y
   `config.ensure_dirs()` (ver el recuadro sobre cuándo se re-sella la traza).

**Recuento total esperado al acabar el barrido completo.** La reanudación comprueba filas por
`(variante, semilla)`; esta tabla es el total del fichero, y **se deriva**, no se escribe a mano:

> total = (filas por variante y semilla) × **2** variantes (`54`, `122_sin_seleccion`) × **10**
> semillas (`len(config.SEMILLAS_BARRIDO)`, que son `[1..10]` sin la 42)

| Tabla | Filas por (variante, semilla) | De dónde sale ese número | Total (× 2 × 10) |
|---|---|---|---|
| `metricas_anomalias_semillas.csv` | 4 | `evaluacion.FILAS_ESPERADAS_POR_VARIANTE` (4 detectores) | **80** |
| `metricas_firmas_semillas.csv` | 4 | `evaluacion.FILAS_ESPERADAS_POR_VARIANTE` (4 clasificadores) | **80** |
| `metricas_baseline_semillas.csv` | 1 | `evaluacion.FILAS_ESPERADAS_POR_VARIANTE` (un RF monolítico) | **20** |
| `metricas_hibrido_semillas.csv` | 1 | `evaluacion.FILAS_ESPERADAS_POR_VARIANTE` (una cascada) | **20** |
| `metricas_balanceo_semillas.csv` | 8 | 4 algoritmos × 2 esquemas de balanceo (`firmas.py`: SMOTE vs `class_weight` en DT y RF; SMOTE vs nada en KNN y HGB) | **160** |
| `metricas_baseline_0day_semillas.csv` | 18 | 17 tipos 0-day de D2 + la fila `__global__` | **360** |
| `metricas_hibrido_0day_semillas.csv` | 72 | 4 detectores × esas 18 filas (`hibrido._tabla_0day_cuatro_detectores`) | **1.440** |
| `metricas_hibrido_calibracion_semillas.csv` | 3 | los 3 umbrales de `hibrido.UMBRALES_CONF = [0.4, 0.5, 0.6]` | **60** |
| `metricas_cascada_invertida_semillas.csv` | 5 | `len(config.CATEGORIAS_ATAQUE) + 1` (4 categorías + `__global__`) | **100** |

**Cinco** de esas nueve cifras las exige el lanzador de forma **exacta** para dar un paso por hecho
(`barrido_semillas.PASOS` + `_filas_esperadas()`, comparado con `==` en `ya_hecho()`,
`barrido_semillas.py:280-320`): las cuatro principales, que salen de
`evaluacion.FILAS_ESPERADAS_POR_VARIANTE`, **y las 5 de la cascada invertida**, que el paso declara
en el propio `PASOS` (`barrido_semillas.py:107-109`, `len(config.CATEGORIAS_ATAQUE) + 1`) porque
`FILAS_ESPERADAS_POR_VARIANTE` solo cubre las principales. Ese 5 lo verifica además el propio script
al reescribir su tabla (`cascada_invertida._comprobar_tabla()`, `cascada_invertida.py:124` y
`:477-483`),
que es la comprobación equivalente a `comprobar_recuento()` para una tabla que no puede pasar por
ella (`evaluacion.py:148-152`). Es el mismo reparto que declara la ficha anterior: «4/4/1/1 … y 5 en
la cascada invertida». Las que **no** tiene comprobación automática son las **cuatro** auxiliares
restantes —balanceo 8, `baseline_0day` 18, `hibrido_0day` 72 y calibración 3—, y por eso van
tabuladas aquí: son la comprobación a mano del final. Las tres derivadas de datos (8, 18, 72) son **invariantes a la
semilla** porque dependen de los splits y del vocabulario, que `program.py` **no** parametriza por
semilla; el 18 y el 72 se verificaron contra las tablas publicadas de la semilla 42 (18 y 72 filas
por variante). Salvedad declarada del 72: si a un detector le faltase su `.joblib`, `hibrido.py` lo
**omite con aviso** en lugar de abortar la tabla (guarda M1), y esa celda saldría con 54 en vez de 72
— un 72 corto es señal de detector caído, no de tabla mal contada.

**Comprobación de cierre: que la semilla 42 no se movió.** El `--solo-verificar` del paso 3 es
*preflight*, o sea **antes**. Al terminar el barrido hay que comprobarlo **después**, y son dos
comandos:

```powershell
git status --porcelain -- Resultados
python app\barrido_semillas.py --solo-verificar
```

Qué debe salir, exactamente. **Estos dos comandos se teclean después del paso 6**, no del 5: así los
`??` esperados incluyen `dispersion_semillas.csv` / `.md`, que las produce el agregador. Si se
comprueba tras el paso 5, la lista de `??` es la misma **menos esas dos**; el resto del criterio no
cambia.

- **`git status`**: como **añadidos** (`??`) las nueve `metricas_*_semillas.csv` y
  —tras el paso 6— `dispersion_semillas.csv` / `dispersion_semillas.md`. **Nada más**, con una
  única línea `M` esperada: la de `verificacion_semilla_joblib.txt`, que **la produce el propio
  paso 3** del bloque (`--solo-verificar` la reescribe siempre: `escribir_si_ok=True` es su defecto,
  `barrido_semillas.py:149-150`). Esa `M` se espera; **cualquier otra `M` es el problema**: ni sobre
  las nueve `metricas_*.csv` publicadas, ni sobre las **39** figuras de `Resultados/figuras/`, ni
  sobre `firmas_reglas_54.txt` / `firmas_reglas_122_sin_seleccion.txt`. (El barrido en sí **no**
  reescribe la traza: como preflight se invoca con `escribir_si_ok=False` y solo la toca si encuentra
  problemas, que sería un abort.) Son 61 ficheros versionados en `Resultados/` y el barrido no debe
  tocar ninguno.
- **Lo que `git status` NO puede ver, y por eso hace falta el segundo comando**: los `.joblib`
  (`Resultados/modelos/` entero está en `.gitignore`), las ~260 figuras `*_semilla*`, los 20
  `firmas_reglas_*_semilla*.txt` y los logs de `logs_barrido/` están **ignorados**, así que un
  `.joblib` publicado pisado por el barrido **no saldría** en el `git status`. Eso lo cierra
  `--solo-verificar`: recorre los `.joblib` de `Resultados/modelos/` sin la marca `_semilla`, lee su
  descriptor y debe informar de **20 de 20** con `semilla = 42` y **0 con problema**, dejando la lista
  en `Resultados/verificacion_semilla_joblib.txt`. Si el borrado por semilla funcionó, además, en
  `Resultados/modelos/` no debe quedar **ningún** fichero con `_semilla` en el nombre (mismo comando
  del paso 2, con su misma exclusión de la traza).

**Si se corta o si un hijo falla.** El *mecanismo* (reanudación por recuento exacto y fallo rápido
sin borrar los `.joblib`) está en la ficha anterior; aquí solo lo operativo:

- **Qué se teclea, en los dos casos:** exactamente **el mismo comando, sin flags** —
  `python app\barrido_semillas.py` —. **No hay que pasar `--semillas`**: el `--semillas` del
  *lanzador* selecciona **qué semillas se ejecutan** (`barrido_semillas.py:498-503`), no sirve para
  reanudar, y el homónimo que existe «solo para auditar un barrido parcial» es el del **agregador**
  (`agregar_semillas.py:725-732`, dentro de su bloque `argparse` de `718-733`).
- **Dónde está el diagnóstico de un fallo:** el mensaje de error trae la ruta del log, que es
  `Resultados/logs_barrido/<script>_<set>_semilla<N>.log`, con el comando completo y la salida del
  hijo (stdout y stderr juntos).
- **Si el arreglo toca código:** las celdas ya corridas quedan selladas con el commit anterior, así
  que `agregar_semillas.py` avisará de que esa celda **mezcla commits** (`commits_origen` con más de
  un valor) — el aviso es correcto y hay que decidir si se acepta o se reejecuta la semilla entera.

#### `comparaciones_pareadas.csv` — recuentos pareados por semilla (alta del 2026-08-17)

**Quién lo emite.** `agregar_semillas.py`, en la misma pasada que produce `dispersion_semillas.csv` y
`dispersion_semillas.md`. No hay que teclear nada aparte: sale del **paso 6** del runbook de arriba.
No es una de las cuatro tablas de métricas principales (su clave lleva `semilla`, que la
`CLAVE_UNICIDAD` de aquellas no admite), así que **no las toca ni las reescribe**.

**Qué contiene.** **13 filas de datos** más la cabecera, repartidas en **tres** comparaciones
pareadas, cada una con una fila por bloque y una fila `__global__`:

| Comparación | Tabla de origen | Bloques | Filas |
|---|---|---|---|
| `firmas_RandomForest_vs_HistGradientBoosting_f1_macro` | `metricas_firmas_semillas.csv` | 2 sets | 2 + `__global__` |
| `balanceo_SMOTE_vs_class_weight_f1_macro_cv` | `metricas_balanceo_semillas.csv` | 2 sets × DecisionTree/RandomForest | 4 + `__global__` |
| `balanceo_SMOTE_vs_nada_f1_macro_cv` | `metricas_balanceo_semillas.csv` | 2 sets × KNN/HistGradientBoosting | 4 + `__global__` |

Cada fila declara el sentido (`mayor_es_mejor`), `n_pares`, `gana_a`/`gana_b`/`empates` —los empates
**no se reparten**—, las semillas concretas de cada lado, la media y los extremos de la diferencia, el
`alcance` de la métrica, y `commits_origen` / `commit_agregador` / `fecha` como procedencia. La
columna `decisiones_no_constantes` avisa de que el balanceo o la configuración ganadora **cambian
entre semillas** dentro del bloque.

**Qué se puede citar de él.** Las filas de la comparación de **firmas**: son `f1_macro` multiclase
sobre los ataques de tipo conocido de D2, y son las que respaldan el «**8 de 10**» de `5.2`, `5.4` y
`3.5` y el «**16 de 20**» global. La fila `__global__` se cita **rotulada como agregado de sus
bloques**, no como una medida independiente.

**Qué NO se puede citar.** Las dos comparaciones de **balanceo** (`40 de 40` y `23-17`): son
`f1_macro` medio en **CV sobre D3** dentro del mini-experimento 4.3.4, criterio de **selección** y no
resultado —así lo dice su propia columna `alcance`—. Y el «8 de 10» de esta tabla **no es** el «8 de
10» de tiempos de entrenamiento de `:596-611`: allí está explicado por qué son cifras distintas y por
qué no se citan la una por la otra; aquí no se repite.

**Estado en disco, verificado el 2026-08-17:** escrito por la **quinta pasada del agregador** con
`commit_agregador = 0276039-sucio` (la marca temporal exacta la declara la cabecera del artefacto; esta
prosa no la copia, que caducaría en la siguiente re-corrida). El sello va **sucio** porque el código
que emite este bloque aún no estaba commiteado al correr el agregador, así que **`0276039` no contiene
ese código**: está **re-anclado en prosa a `98a0289`** —el commit que versiona a la vez
`agregar_semillas.py` y los tres artefactos—, en la tabla de corridas, en la tabla de las cinco
pasadas y en el recuadro del «sexto re-anclaje de sello del proyecto». El sello impreso dentro del
fichero **no se edita**: es salida de `config.commit_actual()`.

---

## Decisión de diseño clave: ajuste del scaler

| Enfoque | Scaler ajustado en | Ventaja | Desventaja |
|---|---|---|---|
| ~~Anterior~~ | Solo D1 (normal) | Anomalías se "desbordan" del rango → más detectables | D3 mal escalado → firmas sesgadas |
| **Actual** | D1 + D3 (todo el train) | Escalado correcto para ambos modelos | Ninguna significativa |

El scaler se ajusta en `concat(D1, D3)` y se aplica igual a D2 (test), garantizando que ninguna división tenga ventaja artificial en el rango de valores.
