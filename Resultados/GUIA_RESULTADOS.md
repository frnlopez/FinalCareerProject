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
| `validacion.py` | funcionando | `specialized_nsl_kdd_validation_report.txt` y 4 figuras de validación |
| `anomalias.py` | ejecutado (54 y 122) | `metricas_anomalias.csv`, `modelos\anomalia_*.joblib`, figuras ROC/PR y matrices 2×2 |
| `firmas.py` | ejecutado (54 y 122) | `metricas_firmas.csv`, `metricas_balanceo.csv`, `firmas_reglas_*.txt`, `modelos\firma_*.joblib`, matrices 4×4 |
| `baseline.py` | ejecutado (54 y 122) | `metricas_baseline.csv`, `metricas_baseline_0day.csv`, `modelos\baseline_rf_*.joblib`, `figuras\baseline_cm_*.png` |
| `hibrido.py` | ejecutado (54 y 122) | `metricas_hibrido.csv`, `metricas_hibrido_calibracion.csv`, `metricas_hibrido_0day.csv`, `figuras\hibrido_cm_*.png`, `modelos\hibrido_*.joblib` (descriptor) |
| `evaluacion.py` | módulo común | No deposita por sí mismo: lo usan los cuatro scripts de modelos |

**Regla de oro:** nada de esta carpeta se edita a mano. Todo se **regenera** ejecutando los
scripts (con `random_state=42`); si un número va a la memoria, tiene que salir de aquí. Para
regenerar: activar el venv y ejecutar `python app\program.py` y luego `python app\validacion.py`
(detalles y trampas de ejecución en `next-steps.md`, sección 6.0).

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
en D1+D3), `label_encoder`, `category_encoder` y la lista `feature_columns` post one-hot.
Se carga con `joblib.load(...)`. **Destino:** 4.3.2 (normalización) y reproducibilidad (4.6 / apéndices).

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

### 3.2 `specialized_nsl_kdd_validation_report.txt`

Resumen de `validacion.py`. Cómo leerlo:

- `Integridad: APROBADA` → dimensiones, alineación de columnas, ausencia de nulos/inf, pureza de
  D1 (solo normal) y D3 (solo ataques) correctas. Si dice FALLA, no entrenar nada.
- Tamaños de los splits (67.343 / 22.544 / 58.630) y **54 características**.
- `Drift D1→D2: 37 características` → 37 de 54 features cambian de distribución entre train
  normal y test (test KS, p<0,01). Es **esperado y deseable**: D2 contiene ataques y tipos nuevos;
  ese drift es justo lo que el detector de anomalías debe captar. Incluye el top-15 por estadístico
  KS (`src_bytes` 0,346, `dst_bytes` 0,317…).
- `Baja varianza: 0` y `Alta correlación: 0 pares` → confirma que la selección 4.3.5 ya limpió
  ambos problemas (el reporte se genera *después* de la selección).
- `D2 fuera de [0,1]: 4 características (informativo)` → `num_shells` (máx. 2,50),
  `num_file_creations` (2,33), `duration` (1,35) y `hot` (1,31). **No es un error**: el scaler se
  ajusta solo en train (D1+D3); re-ajustarlo con el test sería leakage. Vigilar su efecto en el
  autoencoder (FPR).

**Destino en la memoria:** **4.2.1** (análisis previo de la BD) y apoyo metodológico en 4.3.2.

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
- **Derecha:** histograma de p-values con la línea p=0,01: 34 features caen a la izquierda (drift),
  unas pocas quedan cerca de 1 (sin drift).

Conclusión: el test se distribuye de forma distinta al tráfico normal de entrenamiento en el 85 %
de las features — coherente con que D2 mezcla ataques y tipos nuevos. **Destino:** **4.2.1**
(caracterización train/test) y argumento de contexto en 5.1.

### 4.5 `validacion_outliers_iqr.png`

Barras agrupadas: % de outliers (criterio IQR) por feature (top-15 de D1), comparando D1/D2/D3.
Mediana de outliers en D1: **4,78 %** (dato del reporte). Cómo leerla: features donde D3 dispara
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
   "Cobertura" del EDA; `validacion.py` los lista por consola). Son los "0-day" del experimento:
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

> Las notas del vault `04 Implementación del sistema\` y `05 Evaluación\` (volcado 2026-07-15/16)
> ya consumen estos artefactos; las figuras están copiadas en `Obsidian_TFG_Vault\assets\`.

---

## 7. Mantenimiento de esta guía

- **Última actualización: 2026-07-16** (estado: pipeline completo — preprocesado, selección a 54,
  los 4 scripts de modelos ejecutados en 54 y 122, H1 cerrado; cifras reconciliadas con el
  reporte de validación vigente: 54 features, drift 37, outliers mediana 4,78 %, 4 features de D2
  fuera de [0,1]).
- Cuando se regeneren artefactos (nuevas ejecuciones de `program.py`/`validacion.py`) o aparezcan
  los ficheros de la sección 6, **actualizar esta guía en la misma sesión**: cifras, figuras
  nuevas y su destino en la memoria. Una guía desactualizada es peor que ninguna.
