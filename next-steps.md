# Next Steps — TFG H-NIDS con ML

> [!warning] CONGELADO EN CUANTO A CASILLAS — desde 2026-08-01
> Las tareas abiertas ya **no viven aquí**: están en [`features.md`](features.md), que es lo
> primero que lee el agente `leader` en cada mensaje y lo mantiene el `cronista`. Ningún agente
> marca ya casillas en este documento.
>
> Lo que **sigue vigente** de este fichero:
> - **§6 — Guía de ejecución detallada**: la especificación técnica de cada script. Es la
>   referencia que lee el `ml-implementador` antes de tocar código.
> - **§1-§5** — diagnóstico y bitácora: **historial**. Explican cómo se llegó aquí y por qué,
>   pero describen el estado a 2026-07-16, no el de hoy. Para el estado real, el disco manda.
>
> Las decisiones de diseño siguen en `resumen-de-decisiones.md`.

> Documento originalmente **vivo** para analizar y seguir los próximos pasos del proyecto.
> Combina un **diagnóstico** del estado actual (parte 1) con una **hoja de ruta**
> en dos tracks: **Informe** (parte 2) y **Código** (parte 3).

---

## ★ EMPIEZA AQUÍ — próxima sesión (estado a 2026-07-16)

> **Hito: el track de CÓDIGO de modelos está COMPLETO.** `program.py` · `validacion.py` ·
> `anomalias.py` · `firmas.py` · `baseline.py` · `hibrido.py` implementados, auditados y
> ejecutados (54 y 122). El experimento H1 cerró Q1/C → **54 features (opción A)**. **Ya no queda
> nada que programar en el núcleo del TFG.** Todos los números y figuras de los caps. 4 y 5 ya
> existen en disco.

**La próxima sesión es 100% TRACK INFORME (parte 2 de este doc).** No hace falta re-ejecutar código;
si quieres verificar el entorno, `Implementacion\readme` + §6.0. Los resultados están listos para
volcar.

**Orden sugerido (elige UNA tarea). El CUERPO del cap. 3 Diseño (3.1-3.6) quedó COMPLETO en borrador el 2026-07-16 (4ª tarea): 3.1 Requisitos · 3.2 Arquitectura (con diagrama Mermaid de la cascada) · 3.3 Metodología (splits, anti-leakage, 6 veredictos) · 3.4 Modelo de anomalías (diseño) · 3.5 Modelo de firmas (diseño) · 3.6 Conclusiones (ya cerrada; en la 3ª tarea del día se había pospuesto por falta de cuerpo). **6.1 Conclusiones quedó en borrador el 2026-07-16 (5ª tarea)**; **6.2 Líneas futuras la investiga Francisco (posible apartado propio del informe) — sale de la lista operativa de Claude.** **4.1 Tecnologías utilizadas quedó en borrador el 2026-07-16 (7ª tarea)** (entorno, lenguaje, tabla de 9 librerías con versión — fuente `readme.md`+`requirements.txt`). El **Apéndice A.2 (métricas) quedó en borrador el 2026-07-16 (8ª tarea)** como apéndice de fórmulas de referencia. Con esto, las tareas operativas de Claude que RESTAN son: la **bibliografía** (Zotero/IEEE → requiere Zotero, Francisco) y el **Resumen/Abstract** (al final). La teoría en prosa (2.x) y 6.2 siguen siendo de Francisco:**

1. ~~**Reestructurar el vault** (§2.1)~~ → `☑` **COMPLETADA 2026-07-15** (agente `redactor-tfg`,
   verificada en disco: 43 notas, MOC renumerado, 0 wikilinks rotos — detalle en la bitácora §5,
   entrada 2026-07-15).
2. ~~**Volcar resultados a caps. 4 y 5**~~ → `☑` **COMPLETADA 2026-07-16** (agentes `redactor-tfg`
   + dos auditorías adversariales `auditor-ml`, ambas APTO CON CAMBIOS, todos aplicados). Notas
   `4.3` (4.3.1-4.3.6), `4.4`, `4.5`, `5.1`, `5.2` y `5.3` redactadas en prosa y en estado
   `borrador`; caveats P-2/H-5/H-6/M2/M3 cumplidos. Incluye fe de erratas en
   `resumen-de-decisiones.md` (argumento 0-day de las 122) y reconciliación de
   `GUIA_RESULTADOS.md`. Detalle en la bitácora §5, entrada 2026-07-16.
3. **Teoría pendiente** (§2.2): ampliar `2.2 Ciberseguridad`, redactar el bloque `2.3 IA`, completar
   `2.1.6`. → `◐` **guiones de temas propuestos 2026-07-15** en las 9 notas del vault (verificado);
   la **redacción en prosa la hace Francisco** — Claude ya no tiene tarea operativa aquí. El **cuerpo del
   cap. 3 Diseño (3.1-3.6) quedó completo en borrador el 2026-07-16** (4ª tarea del día); **3.6 quedó
   cerrada** (en la 3ª tarea del día se había pospuesto a propósito por falta de cuerpo). Las conclusiones
   de capítulo **4.6 y 5.4 se completaron el 2026-07-16** (borrador). **6.1 Conclusiones se redactó el
   2026-07-16 (5ª tarea, borrador)**; **6.2 Líneas futuras la investiga Francisco** (posible apartado propio
   del informe) — ya no es tarea operativa de Claude. **4.1 Tecnologías se redactó en borrador el
   2026-07-16 (7ª tarea)** y el **Apéndice A.2 (métricas) en borrador el 2026-07-16 (8ª tarea).** Tareas
   operativas de Claude restantes: **bibliografía** (Zotero/IEEE → Francisco) y **Resumen/Abstract** (al final).
   La 2 (volcado) se completó el 2026-07-16 y la parte de Claude de la 4 (A.1 + 4.2.1) el 2026-07-16.
4. **4.2 dataset NSL-KDD** + Apéndice A.1 (columnas, reusar `_mappings_and_info.txt`); figuras EDA
   y de validación → 4.2.1. → `◐` **parte de Claude COMPLETADA 2026-07-16**: A.1 (41 features agrupadas
   + mapeos + 17 tipos 0-day marcados con ★) y 4.2.1 (EDA + validación en prosa con 5 figuras) redactadas
   y en estado `borrador`. **Queda solo la prosa teórica de 4.2** (origen del dataset, 41 features, por
   qué NSL-KDD) — es de **Francisco** (guion ya propuesto). Detalle en la bitácora §5, entrada 2026-07-16.
5. **Bibliografía** (Zotero/IEEE, §2.3) y **Resumen/Abstract** (al final, §2.2).

**Antes de escribir nada de resultados en la memoria, lee** `resumen-de-decisiones.md` (contrato de
decisiones y caveats) y `EL_FUTURO.md` (líneas futuras respaldadas con datos, para el cap. 6
Conclusiones). Las conclusiones del híbrido salen de ahí, no del código.

---

## 0. Cómo usar este documento

- **Leyenda de estado de tareas:**
  - `☐` pendiente · `◐` en curso · `☑` hecho · `⏸` bloqueado / a decidir
- **Severidad** (deuda técnica): 🔴 alta · 🟠 media · 🟡 baja
- Este doc se actualiza a mano según avanza el trabajo. Marca las casillas y añade notas debajo de cada tarea.
- Convención de fechas: absolutas (`AAAA-MM-DD`).
- **¿Vuelves al proyecto tras un tiempo sin tocarlo?** → salta directo a la **sección 6 (Guía de ejecución detallada)**: re-arranque en 5 minutos + especificación paso a paso de lo que toca hacer.

---

## 1. Diagnóstico (estado a 2026-07-01)

### 1.1 Implementación (Python)

**Lo que ya funciona:**
- `program.py` (`NSLKDDPreprocessor`): carga NSL-KDD → EDA (9 visualizaciones) → splits **D1/D2/D3** → One-Hot (`protocol_type`, `service`, `flag`) → escalado (MinMax/Standard) → LabelEncoder → guardado de CSVs + metadatos (`_mappings_and_info.txt`, `_usage_guide.txt`).
- `validacion.py` (`NSLKDDValidator`): integridad (dimensiones, alineación de columnas, nulos/inf, pureza D1/D3, rangos), distribución de clases, distribuciones de características (varianza baja, correlación > 0.95, discriminantes D1 vs D3), **drift KS** D1→D2, **outliers IQR**, y reporte en texto.
- `PIPELINE.md`: excelente documentación del flujo (diagramas Mermaid). **Activo reutilizable** para el capítulo de Desarrollo del informe.
- Decisión de diseño documentada: el scaler se ajusta en **D1+D3** (todo el train) y se aplica a D2.

**Lo que falta (núcleo del TFG):**
- ⛔ **Modelos sin implementar**: detección de anomalías (D1), detección de firmas (D3) y **sistema híbrido + evaluación** (D2). Es la pieza central pendiente.
- Protocolo de evaluación y métricas del sistema conjunto.

### 1.2 Informe (.md en `Obsidian_TFG_Vault/`)

| Sección | Estado | Nota |
|---|---|---|
| 01 Introducción (1.0–1.4) | borrador | Redacción real y coherente |
| 02 Marco Teórico → 2.1 Machine Learning | borrador | Bastante completo… |
| └ 2.1.6 Metodologías y buenas prácticas | pendiente | Vacío |
| 02 Marco Teórico → 2.2 Ciberseguridad | borrador (fino) | **Solo la intro**; falta mucho |
| 02 Marco Teórico → Inteligencia Artificial | **no existe** | Prometido en `1.4 Estructura` |
| 03 Desarrollo (3.1–3.6) | pendiente | Esqueleto vacío |
| 00 Preliminares (Resumen/Abstract) | pendiente | Placeholder descartado |
| Bibliografía | borrador | Lista cruda de URLs, sin formato |

### 1.3 Desajustes clave (informe ↔ estructura ↔ código)

1. **Estructura prometida vs actual.** `1.4 Estructura` describe **5 capítulos**:
   1) Introducción · 2) Marco Teórico (**Ciberseguridad + ML + IA**) · 3) Diseño (conceptos previos, requisitos, arquitectura, metodología, los dos modelos) · 4) Implementación · 5) Conclusiones y evaluación de resultados.
   La estructura `.md` actual **no** lo refleja: falta el bloque **IA**, `03 Desarrollo` mezcla Diseño + Implementación, y no hay capítulo de **Resultados/Conclusiones**.
2. **IA ausente** pese a que el proyecto es explícitamente de *ciberseguridad e IA*.
3. **Alineación código ↔ informe:** el trabajo de `program.py`/`validacion.py`/`PIPELINE.md` aún no está volcado al capítulo de Desarrollo.

---

## 2. Roadmap — TRACK INFORME

### 2.1 Reconciliación estructural — índice objetivo (fijado 2026-07-02)
> No se toca el vault todavía: esto queda planificado para decidir/ejecutar.

**Índice de referencia** aportado por el usuario (TFG tipo de Teleco). Bloque "Desarrollo del proyecto":

- **3 Diseño del sistema** — 3.1 Requisitos · 3.2 Arquitectura · 3.3 Metodología de funcionamiento del sistema · 3.4 Modelo de detección de anomalías · 3.5 Modelo de detección basado en firma · 3.6 Conclusiones del capítulo
- **4 Implementación del sistema** — 4.1 Tecnologías utilizadas (4.1.1 entorno y aplicaciones · 4.1.2 lenguaje · 4.1.3 librerías Python) · 4.2 Base de datos utilizada (4.2.1 análisis previo de la BD) · 4.3 Preprocesamiento de los datasets (4.3.1 adición/eliminación de etiquetas · 4.3.2 normalización de variables numéricas · 4.3.3 codificación de variables categóricas · **4.3.4 equilibrio y balanceo de muestras** · **4.3.5 selección de características** · 4.3.6 división del conjunto de datos) · 4.4 Entrenamiento del modelo de detección de anomalías · 4.5 Entrenamiento del modelo de detección basado en firmas · 4.6 Conclusiones del capítulo
- **5 Evaluación** — 5.1 Resultados modelo anomalías (5.1.1 matrices de confusión · 5.1.2 métricas de desempeño · 5.1.3 resultados finales) · 5.2 Resultados modelo firmas (5.2.1 matrices de confusión · 5.2.2 métricas de desempeño · **5.2.3 comparación de los resultados de cada algoritmo**) · 5.3 Conclusiones del capítulo
- **III Conclusiones** — Conclusiones y líneas futuras
- **IV Apéndices** — A Manual de uso: A.1 Columnas del dataset NSL-KDD · A.2 Métricas de desempeño (A.2.1 métricas del modelo de anomalías) · **Bibliografía**

**Implicaciones detectadas del índice (⏸ a decidir en la entrevista):**
- `☑` **DECIDIDO 2026-07-02**: el cap. 5 se adapta → 5.1 anomalías · 5.2 firmas · **5.3 Resultados del sistema híbrido** · 5.4 Conclusiones del capítulo. El híbrido es la tesis del TFG y tiene sección propia de evaluación.
- ⏸ **4.3.4 Balanceo** y **4.3.5 Selección de características** son pasos de pipeline que **hoy no existen** en `program.py` → nueva tarea de código (ver 3.1-E).
- ⏸ El dataset se presenta en **4.2 (Implementación)**, lo que resuelve la duda de 2.2 sobre dónde va la teoría de NSL-KDD.

**Tareas de reestructuración:**
- `☑` Añadir bloque **Inteligencia Artificial** en `02 Marco Teórico/` (p. ej. `2.3 Inteligencia Artificial/`): IA vs ML vs DL, IA en ciberseguridad, límites y consideraciones éticas. → *cruza con Q abierta en 2.2* → **hecho 2026-07-15** (2.3.1-2.3.3 como esqueletos; la redacción de la teoría la hace Francisco).
- `☑` Separar el actual `03 Desarrollo/` en **`03 Diseño del sistema`** y **`04 Implementación del sistema`** siguiendo el índice objetivo. → **hecho 2026-07-15** (3.1-3.6 y 4.1-4.6 con H2 4.3.1-4.3.6; los 6 ficheros viejos estaban vacíos, mapeo en bitácora).
- `☑` Crear **`05 Evaluación/`** (matrices de confusión, métricas, comparativa por algoritmo) y **`06 Conclusiones/`** (conclusiones y líneas futuras) como capítulos separados. → **hecho 2026-07-15** (5.1-5.4 con 5.3 = híbrido según decisión 2026-07-02; 6.1-6.2).
- `☑` Crear **`Apéndices/`**: A.1 columnas NSL-KDD (reusar `_mappings_and_info.txt`) · A.2 métricas de desempeño. → **hecho 2026-07-15** (A.1-A.2 como esqueletos con referencia a sus fuentes).
- `☑` Renumerar/actualizar el MOC (`00 Índice TFG.md`) tras la reestructuración. → **hecho 2026-07-15** (reescrito con leyenda de estados; 0 wikilinks rotos verificados).

### 2.2 Huecos de contenido a redactar
- `☐` **2.2 Ciberseguridad** (ampliar): historia y evolución de los IDS/IPS, taxonomía IDS (NIDS/HIDS), **detección por firmas vs por anomalías**, tipos de ataque **DoS / Probe / R2L / U2R**, panorama de amenazas. → guion de temas propuesto 2026-07-15 (en la propia nota del vault); redacción: Francisco.
- `◐` **Teoría del dataset NSL-KDD**: origen (KDD'99 → NSL-KDD), 41 características, problema de duplicados/desbalance, por qué se elige. → **DECIDIDO 2026-07-02**: va en **4.2 Base de datos utilizada** (+4.2.1 análisis previo), según el índice objetivo. El detalle de columnas, al **Apéndice A.1**. → guion de temas propuesto 2026-07-15 (en la propia nota del vault). → **borrador Claude 2026-07-21** (reparto de teoría de 4.2 cedido a Claude, decisión 2026-07-21): «Origen» y «Las 41 características y sus 3 grupos» redactados como borrador factual con marcadores `[CITA:...]` pendientes de Zotero; el bloque «Por qué se eligió NSL-KDD» queda a revisión de Francisco (refleja el criterio del autor). No `☑` hasta resolver citas y esa revisión.
- `☐` **2.1.6 Metodologías y buenas prácticas** (ML): completar. → guion de temas propuesto 2026-07-15 (en la propia nota del vault); redacción: Francisco.
- `☐` **Bloque IA** (contenido, ver 2.1). → guion de temas propuesto 2026-07-15 (en la propia nota del vault); redacción: Francisco.
- `☐` **Resumen** y **Abstract** (redactar al final, cuando el resto esté cerrado).

### 2.3 Bibliografía
> **DECIDIDO 2026-07-02**: la memoria se entrega en **Word** (`TFG - Fran.docx`; era `TFG - KIKO.docx`, corregido 2026-07-16); las notas de Obsidian son la fuente y se vuelcan a Word. Citas con **Zotero + plugin de Word** (estilo IEEE automático).

- `☐` Instalar Zotero + conector de Word; importar las URLs crudas de `Bibliografía.md` como entradas.
- `☐` Convertir la lista cruda de `Bibliografía.md` a **formato IEEE** vía Zotero.
- `☐` Verificar que cada cita `[n]` del texto tenga su entrada y viceversa.

### 2.4 Integrar implementación en el informe
- `☐` Volcar `PIPELINE.md` (diagramas + explicación) al capítulo de **Diseño/Implementación**.
- `☑` Documentar el diseño de splits **D1/D2/D3** y la justificación del scaler en D1+D3. → **hecho 2026-07-16** (notas 4.3.2 y 4.3.6 de la memoria, en prosa y auditadas).
- `☑` Incluir figuras del EDA y de la validación (drift, outliers, distribuciones) como resultados intermedios. → **hecho 2026-07-16**: 5 figuras incrustadas en **4.2.1** (`eda_distribuciones_divisiones.png`, `validacion_distribucion_clases.png`, `validacion_discriminantes_d1_vs_d3.png`, `validacion_drift_ks.png`, `validacion_outliers_iqr.png`), en prosa y estado `borrador`.

---

## 3. Roadmap — TRACK CÓDIGO

### 3.1 Matriz de experimentos de ML
> Objetivo del TFG: **investigar y experimentar**. Requisito de alcance (2026-07-02): **no basta un algoritmo por modelo** — hay que entrenar **varios algoritmos por modelo, con el mismo protocolo, y compararlos** (alimenta 5.1/5.2.3 del informe).

**A) Modelo de detección de ANOMALÍAS — entrenar con D1 (solo normal). DECIDIDO 2026-07-02: comparar los 4**

| Algoritmo | Idea | Hiperparámetros clave a explorar | Notas |
|---|---|---|---|
| `IsolationForest` | Aísla anomalías por particiones | `contamination`, `n_estimators`, `max_samples` | Baseline |
| `OneClassSVM` | Frontera del comportamiento normal | `nu`, `gamma`, `kernel` | **Submuestrear D1** (O(n²) con ~67k) y documentarlo |
| `LocalOutlierFactor` | Densidad local vs vecinos | `n_neighbors` | `novelty=True` obligatorio para predecir sobre D2 |
| Autoencoder (sklearn) | Error de reconstrucción como score | capas ocultas, épocas, umbral | Vía `MLPRegressor` — **sin dependencia TF/Keras** |

- `☑` Implementar baseline con `IsolationForest`. → **hecho 2026-07-06** (los 4 algoritmos en `anomalias.py`).
- `☑` **Umbral de decisión — DECIDIDO 2026-07-02**: reservar ~20% de D1 como validación, fijar el umbral en un **percentil del score** (p. ej. p95 ≈ 5% FPR aceptado) sobre ese tramo. **Mismo criterio para los 4 algoritmos** (comparación homogénea). Nunca ajustar el umbral mirando D2. Complementar con ROC/PR sobre D2 (independientes del umbral). → **hecho 2026-07-06** (p95 sobre D1_val; FPR real en D2 ~8-10% por drift, no ~5% — a explicar en la memoria).
- `☑` Entrenar y evaluar **todos** los algoritmos con el mismo protocolo (mismo split, mismas métricas, misma semilla). → **hecho 2026-07-06** (ejecutado en 54 y 122 features).
- `☑` Tabla comparativa + matrices de confusión por algoritmo → alimenta **5.1**. → **hecho 2026-07-06** (`metricas_anomalias.csv` + figuras; mejor detector: Autoencoder ≈ IsolationForest; LOF el más débil).

**B) Modelo de detección de FIRMAS — entrenar con D3 (ataques conocidos). DECIDIDO 2026-07-02: comparar los 4**

| Algoritmo | Idea | Notas |
|---|---|---|
| `DecisionTree` | Reglas interpretables | Base para extraer "firmas" legibles (`export_text`) |
| `RandomForest` | Ensemble bagging multiclase | `class_weight='balanced'` (D3 muy desbalanceado) |
| `KNN` | Clasificación por vecindad | Sensible al escalado (ya resuelto en pipeline) |
| `HistGradientBoostingClassifier` | Boosting (sklearn, rendimiento tipo XGBoost) | Sin dependencia nueva |
| Reglas explícitas (complemento) | Umbrales por característica discriminante | Usa el análisis D1 vs D3 de `validacion.py` |

- `☑` Clasificador multiclase (dos/probe/r2l/u2r) sobre D3 con **todos** los algoritmos elegidos. → **hecho 2026-07-06 (impl.) · ejecutado 2026-07-11 (54 y 122)** en `firmas.py`.
- `☑` Extraer reglas interpretables (firmas) del árbol / características discriminantes. → **hecho 2026-07-11**: `firmas_reglas_54.txt` / `firmas_reglas_122_sin_seleccion.txt`.
- `☑` Manejar el **desbalance** (ratio alto detectado en la validación) → cruza con 3.1-E balanceo. → **hecho 2026-07-11**: SMOTE dentro del fold; tabla ganadores en `metricas_balanceo.csv`.
- `☑` Comparación de resultados de cada algoritmo → alimenta **5.2.3**. → **hecho 2026-07-11**: `metricas_firmas.csv` + 8 figuras `firmas_cm_*.png`. Mejor firma para el híbrido: **RandomForest sobre 54 (SMOTE)**, f1_macro D2 = 0.822. Hallazgo: 122 generaliza PEOR a D2 (RF cae 0.822→0.696, sobreajuste a D3 por los dummies extra). Detalle en `sesion-2026-07-11.md`.

**E) Nuevos pasos de preprocesamiento exigidos por el índice (no existen aún en `program.py`)**

- `☑` **4.3.4 Equilibrio y balanceo de muestras** — **DECIDIDO 2026-07-02**: mini-experimento **SMOTE vs `class_weight='balanced'`** sobre D3 y elegir con datos. Añadir `imbalanced-learn` a requirements. SMOTE **solo al train**, nunca a D2. Cuidado con u2r (~50 muestras): reducir `k_neighbors`.
  → **Hecho 2026-07-11** (tabla producida por `firmas.py`, `metricas_balanceo.csv`, f1_macro CV sobre D3). Ganadores: DecisionTree → **class_weight** (54: 0.953 / 122: 0.957); RandomForest → **SMOTE** (0.974 / 0.980); KNN → **SMOTE** (0.945 / 0.952); HistGradientBoosting → **SMOTE** (0.969 / 0.972; sin balanceo colapsa a 0.83/0.80). Esta tabla ES el contenido de 4.3.4.
- `☑` **4.3.5 Selección de características** — **DECIDIDO 2026-07-02**: dos pasos: (1) filtro barato — eliminar varianza ~0 y una de cada par con correlación >0.95 (ya calculados por `validacion.py`); (2) ranking de **importancias de RandomForest**, conservar top-N que acumulen ~99% de importancia. Evaluar **con vs sin selección** para justificarlo. Documentar features eliminadas.
  → **CERRADA 2026-07-15**: el experimento H1 (54 vs 122) resuelve Q1/C hacia **54 features (opción A)** para ambas etapas. Las 122 no recuperan ningún tipo 0-day relevante que las 54 pongan a cero y degradan la firma ~9 pp (`conocida f1_macro` 0.655 vs 0.748, sobreajuste a D3). Detalle y datos en `resumen-de-decisiones.md` (§ Decisión del 2026-07-15). Matiz honesto para la memoria: las 122 dan un detector marginalmente mejor (Pareto) → opción B queda como línea futura (`EL_FUTURO.md §3`).
  → **Implementada y ejecutada 2026-07-05, umbral de importancia acumulada 99,9% (H1-Opción1)** (`select_features()` en `program.py`, tras el escalado; flag CLI `--sin-seleccion` para generar la variante de 122): **122 → 54 features** (1 varianza · 7 correlación · 60 fuera del top-99,9% de importancia RF; el top-54 acumula el 99,9% — desglose exacto en `Resultados\selected_features.txt`). Salidas: `selected_features.txt`, CSVs de X ya filtrados (54 columnas), `transformers.joblib`. Trampa de la varianza D1-only: evitada (verificado por auditoría). **Para cerrarla ☑ falta:** el experimento H1 (54 vs 122 con recall 0-day por tipo de la etapa de anomalías; el lado *baseline* de esa tabla ya está medido — ver 3.1-F). Estado real reconciliado en `resumen-de-decisiones.md`.

**C) Sistema HÍBRIDO — combinar y evaluar sobre D2**

- `☑` **Arquitectura de fusión — DECIDIDO 2026-07-02: cascada anomalía → firmas. IMPLEMENTADA en `hibrido.py`, auditada APTO y EJECUTADA (54 y 122) 2026-07-15.**
  - Etapa 1: el mejor detector de anomalías clasifica cada flujo de D2 como *normal* vs *sospechoso*.
  - Etapa 2: los sospechosos pasan al mejor modelo de firmas, que asigna categoría (dos/probe/r2l/u2r); si la confianza (`predict_proba` máx.) queda por debajo de un umbral → **"ataque desconocido / 0-day"**.
  - Justificación: el modelo de firmas se entrena solo con ataques (D3) y no conoce la clase *normal*; la cascada evita que condene tráfico legítimo.
  - Salidas para 5.3: evaluación **binaria** (=etapa 1 por construcción, H-5) y **multiclase** (matriz 5×6 con `unknown`, H-6); calibración de `UMBRAL_CONF` por OOF de D3 (H-4).
- `☑` Analizar cobertura: qué ataques de D2 **no** están en D3 (solo detectables por anomalías) — ya lo reporta `validacion.py`. Medir específicamente la detección de estos "0-day" por la etapa 1. → **hecho 2026-07-15**: `metricas_hibrido_0day.csv` (recall 0-day por tipo de los 4 detectores + FPR). Hallazgo: detectores complementarios por tipo (LOF caza `mailbomb`, IF caza `snmpguess`, el AE los falla); `snmpgetattack` ciego para los 4 (límite de features). → `EL_FUTURO.md §2/§4`.

**F) Baseline de comparación — RF monolítico (☑ RESUELTO 2026-07-11 · planteada 2026-07-09)**

> Origen: comentario del profesor de seguimiento ("todo el mundo acaba en un Random
> Forest para este dataset"). Analizado: RF **ya está** como clasificador de firmas
> (3.1-B) y como motor de la selección 4.3.5; lo que NO existe es un **RF monolítico**
> = un único clasificador supervisado sobre TODO el train (normal + 4 ataques),
> evaluado sobre todo D2. Ese es el patrón dominante en la literatura NSL-KDD (~99%).

- `☑` **RF monolítico añadido como baseline de control (no como arquitectura).**
  → **RESUELTO 2026-07-11**: APROBADO por el autor; ubicación en **`baseline.py` aparte**
    (no modo de `firmas.py`). Decisión y spec completas en `resumen-de-decisiones.md`
    (§ Decisión del 2026-07-11, 3.1-F). **Implementado, auditado (APTO, sin leakage) y
    ejecutado (54 y 122)** — ver `sesion-2026-07-11.md`.
  - **Resultado que confirma la tesis del híbrido:** f1_macro CV = 0.909 pero **f1_macro D2
    = 0.472 (54) / 0.470 (122)** — desplome CV→test; **recall 0-day global = 0.150** (el
    ~85% de los 0-day pasan como "normal"); recall_r2l = 0.004, recall_u2r = 0.01 (el
    normal ahoga las clases raras pese a `class_weight='balanced'`). Es el lado "baseline"
    de la tabla del experimento H1; falta el lado "híbrido".
  - Desarrollo del razonamiento: `Guia_ML/04_los_tres_modelos.md §5`.

**D') Estructura del código — DECIDIDO 2026-07-02**

```
app/
├── program.py      (existente — preprocesado; se le añaden 4.3.4 balanceo y 4.3.5 selección)
├── validacion.py   (existente — validación de datos)
├── anomalias.py    (nuevo — entrena/evalúa los 4 algoritmos de anomalías, umbral por percentil)
├── firmas.py       (nuevo — entrena/evalúa los 4 clasificadores multiclase sobre D3)
├── hibrido.py      (nuevo — cascada anomalía→firmas, evaluación final sobre D2)
└── evaluacion.py   (nuevo — módulo común: métricas, matrices de confusión, ROC/PR, tablas comparativas, guardado en Resultados/)
```
- Cada script entrena **todos** sus algoritmos con el mismo protocolo y persiste modelos con `joblib`.
- Mismo estilo clase-por-script que `program.py`/`validacion.py`; comentarios en español.

**D) Protocolo de evaluación y métricas**

- `☐` **Hiperparámetros — DECIDIDO 2026-07-02**: `GridSearchCV` con **rejillas pequeñas y documentadas** (3-4 valores por hiperparámetro clave). Firmas: `StratifiedKFold(5)` sobre D3. Anomalías: selección sobre el split de validación de D1. `random_state=42` en todo. Las tablas de grids van a la memoria (4.4/4.5).
- `☐` Métricas: **Precision / Recall / F1 por categoría**, macro/weighted, **matriz de confusión**, curvas **ROC/PR** (para el detector de anomalías).
- `☐` Evaluación binaria (normal vs ataque) y multiclase (5 categorías).
- `☐` Comparativa de todos los experimentos en una tabla única (para el capítulo de Resultados).
- `☐` Guardar resultados/figuras de forma reproducible en `Resultados/`.

### 3.2 Deuda técnica priorizada
> Documentado, **sin arreglar aún**. Revisar antes de dar los resultados por definitivos.

- `☑` 🔴 **Posible pérdida de datos en el One-Hot.** Se alinean columnas usando **D1 (solo normal)** como referencia; las categorías de `service`/`flag` presentes solo en D3 (ataques) o D2 (test) se **descartan** al reindexar. Debería alinearse contra la **unión** de categorías (o fijar el vocabulario con todo el train). *Impacto: sesgo en firmas y en evaluación.*
  → **DECIDIDO 2026-07-02: arreglar ANTES de entrenar ningún modelo.** Corregir alineación (vocabulario = D1+D3), regenerar CSVs y re-validar con `validacion.py`. Es el **paso 0** del track de código.
  → **Hecho 2026-07-05**: vocabulario = unión D1+D3 ordenada; 77→122 features (+45 dummies de ataque recuperados; 122 = 38 numéricas + 84 dummies). CSVs regenerados y `validacion.py` APROBADA.
- `☐` 🟠 **Rutas absolutas hardcodeadas** en `program.py` y `validacion.py` (poco portable/reproducible).
- `☑` 🟠 **Incoherencia de ruta** — **RESUELTA 2026-07-16**: `CLAUDE.md` decía dataset en `...\KIKO\Archivos dataset\`; verificado en disco y en `program.py:91` que la ruta real es `...\KIKO_TFG\Working_Directory\Archivos dataset\` (y salida en `...\Working_Directory\Resultados\`, no `...\KIKO\...\Resultados\`). Corregidas ambas rutas en `CLAUDE.md`. La ruta vieja `KIKO\` no existe.
- `☑` 🟡 `train_test_split` importado y no usado.
  → **Hecho 2026-07-05**: import eliminado de `program.py` en la misma pasada del paso 0.
- `☐` 🟡 `warnings.filterwarnings('ignore')` global — oculta avisos útiles durante la experimentación.
- `☑` 🟡 Conteo de tipos de ataque — **RESUELTO 2026-07-16**: la cifra real es **40 etiquetas del `LabelEncoder` = `normal` + 39 tipos de ataque** → 5 categorías (fuente: `specialized_nsl_kdd_mappings_and_info.txt`, "Total de ataques específicos: 40" incluye `normal`; coherente con la nota 4.3.1 del vault). Corregido el "51 tipos" erróneo en `CLAUDE.md` (→ "39 tipos de ataque") y en `PIPELINE.md`.

**Hallazgos de la auditoría de 4.3.5 (2026-07-05) — veredicto APTO CON CAMBIOS. Estado RECONCILIADO 2026-07-11 (detalle en `resumen-de-decisiones.md`, § Estado real reconciliado):**

- `☑` 🟠 **H1 — Opción 1 ejecutada (umbral de importancia 99,9% → 54 features).** El corte previo al 99% (40 features) eliminaba indicadores clave para la detección 0-day (`num_failed_logins`, `flag_REJ`, `flag_SH`, `num_shells`, `su_attempted`, `urgent`, `flag_S1`, `service_finger/login/imap4`, `flag_RSTOS0`…); subir a 99,9% los recupera (+14). **Falta solo la justificación con datos** (por eso 4.3.5 sigue `◐`, no ☑): el experimento **54 vs 122 con recall 0-day por tipo** de la etapa de anomalías (paso 6 de §4). El lado *baseline* de esa tabla (RF monolítico) ya está medido — ver 3.1-F. El set de 40 queda descartado (no existe en disco).
- `☑` 🟡 **H2 — resuelto**: `program.py::_resolver_representante_conservado()` sigue la cadena greedy de correlación; `selected_features.txt` ya no afirma en falso qué feature se conservó.
- `☑` 🟡 **H3 — resuelto**: CLI `argparse` con `--sin-seleccion` + sufijo `_sin_seleccion` en todos los artefactos; las variantes con y sin selección coexisten sin pisarse.

**Pendientes menores (2026-07-05):**

- `☐` 🟡 La lista nominal de los 17 tipos 0-day solo sale por consola; persistirla en el reporte de `validacion.py`.
- `☐` 🟡 El delta **77→122** del fix one-hot no está en ningún artefacto regenerable (solo en este documento); dejarlo en un artefacto de `Resultados/`.
- `☐` 🟡 `validacion.py` compara columnas D2/D3 por conjunto, no por orden (`validacion.py:156-159`) — fix de una línea.

### 3.3 Reproducibilidad
- `☑` Persistir transformadores ajustados (`scaler`, `label_encoder`, `category_encoder`) con `joblib` para inferencia consistente.
  → **Hecho 2026-07-05** para el preprocesado: `Resultados\specialized_nsl_kdd_transformers.joblib`. Los modelos (anomalías/firmas) se persistirán en sus propios scripts.
- `☐` Fijar **semilla global** (`random_state`) en todos los experimentos.
- `☐` Centralizar rutas/parámetros en un **config** (archivo o argumentos CLI).
- `☐` Fijar versiones en `requirements.txt` (pinning) para reproducibilidad.

---

## 4. Dependencias Informe ↔ Código

Qué resultado del código alimenta qué parte del informe (para ordenar el trabajo):

| Resultado de código | Alimenta capítulo del informe |
|---|---|
| EDA + splits D1/D2/D3 + validación | Diseño (dataset, metodología de datos) |
| `PIPELINE.md` | Diseño / Implementación |
| Modelo de anomalías (experimentos) | Implementación + Resultados |
| Modelo de firmas (experimentos) | Implementación + Resultados |
| Evaluación del híbrido en D2 (métricas, matrices) | Resultados y Conclusiones |
| Comparativa de experimentos | Resultados y Conclusiones |

**Orden de trabajo — DECIDIDO 2026-07-02: código primero, informe detrás.**

> **Estado a 2026-07-14 — orden pendiente (siguiente sesión).** Detalle y resultados en `sesion-2026-07-14.md` (diseño), `sesion-2026-07-11.md` y `sesion-2026-07-06.md`; decisiones en `resumen-de-decisiones.md`.
> 1. ☑ Paso 0 (fix one-hot) · ☑ 4.3.5 selección (**54 features**) · ☑ `config.py` + `evaluacion.py` · ☑ `imbalanced-learn` instalado.
> 2. ☑ `anomalias.py` implementado, auditado y **ejecutado (54 y 122)**.
> 3. ☑ **`firmas.py`** implementado, auditado APTO y **ejecutado (54 y 122)** — produjo 4.3.4 balanceo, reglas (4.5) y métricas 5.2/5.2.3.
> 4. ☑ **`baseline.py`** (RF monolítico, 3.1-F) creado, auditado **APTO** y **ejecutado (54 y 122)** — lado "baseline" de la tabla H1.
> 5. ◐ **`hibrido.py`** — **IMPLEMENTADO 2026-07-14** siguiendo H-1…H-7 + P-1…P-5 (cascada Autoencoder→RandomForest, calibración OOF con presupuesto τ=2pp sin ver D2, matriz 5×6, tabla 0-day de los 4 detectores con FPR). Compila e importa OK. **Auditado APTO** (M1 aplicado) y **EJECUTADO (54 y 122) 2026-07-15** sin errores. `UMBRAL_CONF=0.5`; recall 0-day 0.771 (54) vs 0.150 del baseline → tesis confirmada ~5×. Spec/decisiones en `resumen-de-decisiones.md` (§ 2026-07-14/07-15).
> 6. ☑ **Experimento H1** (54 vs 122) con **recall 0-day por tipo** — **CERRADO 2026-07-15**: leído de `metricas_hibrido_0day.csv`; Q1/C → **54 (opción A)**; 4.3.5 cerrada; tabla frente al baseline completa (híbrido 0.771 vs baseline 0.150).
> 7. ◐ **Volcado a la memoria (caps. 4 y 5) + teoría (Ciberseguridad + IA), en paralelo.** ← **RETOMAR AQUÍ: ya no queda código de modelos pendiente; el trabajo restante es la memoria.**

1. **Paso 0**: arreglar bug 🔴 one-hot → regenerar CSVs → re-validar con `validacion.py`.
2. Añadir a `program.py`: **4.3.4 balanceo** (SMOTE vs class_weight) y **4.3.5 selección de características** (filtro corr. + importancias RF).
3. `anomalias.py`: 4 algoritmos (IF, OCSVM, LOF, Autoencoder-MLP), umbral p95 sobre validación de D1, grids pequeños + CV.
4. `firmas.py`: 4 clasificadores (DT, RF, KNN, HistGB) multiclase sobre D3 + extracción de reglas.
5. `hibrido.py`: cascada anomalía → firmas, evaluación binaria y multiclase sobre D2, análisis 0-day.
6. Volcar resultados a caps. 4 y 5 del informe; teoría (Marco Teórico: Ciberseguridad + IA) se redacta en los huecos.

---

## 5. Bitácora de decisiones (añadir aquí según avancemos)

- `2026-07-01` — Creado el documento. Estructura acordada: análisis + roadmap en dos tracks; reconciliación estructural del informe planificada (no ejecutada); deuda técnica documentada sin arreglar.
- `2026-07-02` — Incorporado el **índice objetivo** del informe (caps. 3 Diseño · 4 Implementación · 5 Evaluación · Conclusiones · Apéndices). Requisito de alcance: **comparar varios algoritmos por modelo**, no uno solo. Detectados dos pasos de pipeline nuevos (balanceo 4.3.4 y selección de características 4.3.5) y la ausencia del híbrido en el cap. 5 → decisiones abiertas en entrevista.
- `2026-07-02` — **Entrevista de decisiones (grill) completada.** Resueltas 10 decisiones:
  1. Cap. 5 gana sección **5.3 Resultados del sistema híbrido** (y 5.4 Conclusiones).
  2. Anomalías: **IF + OCSVM + LOF + Autoencoder** (vía `MLPRegressor`, sin TF).
  3. Firmas: **DT + RF + KNN + HistGradientBoosting** (todo sklearn).
  4. Balanceo 4.3.4: mini-experimento **SMOTE vs class_weight** (añade `imbalanced-learn`).
  5. Selección 4.3.5: **filtro correlación/varianza + importancias RF** (top-N ~99%), evaluado con/sin.
  6. Umbral anomalías: **percentil (p95) sobre 20% de D1 reservado como validación**, igual para los 4.
  7. Híbrido: **cascada anomalía → firmas** con clase "desconocido/0-day" por baja confianza.
  8. Bug 🔴 one-hot: **arreglar antes de entrenar** (paso 0).
  9. Código: **3 scripts nuevos + evaluacion.py común**; hiperparámetros con **grids pequeños + CV**, `random_state=42`.
  10. Memoria en **Word + Zotero** (IEEE); teoría NSL-KDD va a 4.2; orden de trabajo: **código primero**.
- `2026-07-02` — Añadida la **sección 6: Guía de ejecución detallada** (re-arranque + spec de cada paso con referencias a líneas de código reales). El doc es ahora autocontenido para retomar el proyecto en frío.
- `2026-07-05` — **PASO 0 COMPLETADO.** Fix 🔴 one-hot en `program.py` (vocabulario = unión D1+D3 ordenada): **77 → 122 features** (+45 dummies de ataque recuperados; 122 = 38 numéricas + 84 dummies, verificado por auditoría). En la misma pasada: eliminado import sin uso de `train_test_split`, transformadores persistidos con joblib (`Resultados\specialized_nsl_kdd_transformers.joblib`) y `plt.show()` → `savefig` en `program.py` (figura en `Resultados\figuras\eda_distribuciones_divisiones.png`). CSVs regenerados (D1 67.343×122 · D2 22.544×122 · D3 58.630×122), `validacion.py` **APROBADA**, auditoría adversarial: veredicto **APTO, sin leakage**. Avisos operativos descubiertos:
  - Los scripts necesitan `PYTHONIOENCODING=utf-8` en esta máquina (los emojis de los prints cascan con cp1252).
  - `validacion.py` aún bloquea con 4 `plt.show()` (líneas 250, 318, 381, 428) — NO se tocó; ejecutar con `MPLBACKEND=Agg` o aplicar el savefig pendiente.
  - ⚠️ **TRAMPA para el paso 6.2 (selección de características)**, detectada por auditoría: `validacion.py` calcula la varianza ~0 **solo sobre D1**, así que gran parte de las "48 features de varianza ~0" son precisamente los dummies exclusivos de D3 recién recuperados. El filtro de varianza **DEBE** calcularse sobre D1+D3 o deshace el fix silenciosamente.
  - D2 escalado queda en rango [0, 2.5] (esperable: scaler ajustado en train); vigilar el FPR del autoencoder.
- `2026-07-05` — **(2ª tanda) 4.3.5 implementada + avisos operativos resueltos + validación APROBADA.**
  - **Los 4 avisos de la entrada anterior, arreglados:** (a) utf-8 vía `sys.stdout.reconfigure` en ambos scripts — ya no hace falta `PYTHONIOENCODING`; (b) `validacion.py` sin `plt.show()` → 4 figuras `validacion_*.png` en `Resultados\figuras\`; (c) varianza/correlación de `validacion.py` ahora sobre **D1+D3** (trampa del paso 6.2 desactivada); (d) nuevo chequeo informativo de D2 fuera de [0,1] (3 features, máx 2,33 en `num_file_creations`) *[corregido 2026-07-16: el reporte vigente, con el set de 54, registra **4** features, máx. 2,50 en `num_shells` — ver bitácora 2026-07-16]* + chequeo de columnas contra `transformers.joblib`.
  - **4.3.5 Selección de características implementada** en `program.py` (`select_features()`, tras el escalado, flag `aplicar_seleccion=True` en `main`): **122 → 40 features** (1 varianza: `num_outbound_cmds` · 7 correlación · 74 fuera del top-99% de importancia RF; top-40 = 99,16% de la importancia). Salidas: `Resultados\selected_features.txt`, CSVs de X ya filtrados (D1 67.343×40 · D2 22.544×40 · D3 58.630×40), `transformers.joblib` con `feature_columns` (40) y `feature_columns_pre_seleccion` (122). Trampa de la varianza D1-only: evitada (verificado por auditoría).
  - `validacion.py` → **APROBADA**. Ejecución sin variables de entorno ni bloqueos.
  - Creada `Resultados\GUIA_RESULTADOS.md`: inventario explicado de los 22 artefactos con su sección destino en la memoria.
  - **Auditoría: APTO CON CAMBIOS** — 3 hallazgos registrados como deuda en 3.2 (🟠 H1: el corte al 99% elimina features clave para 0-day, ⏸ decisión pendiente 99% vs 99,9% vs medir recall 0-day · 🟡 H2: texto falso en `selected_features.txt` sobre qué se conservó en cadenas de correlación · 🟡 H3: `aplicar_seleccion=False` deja estado inconsistente y el flag no tiene CLI). **Deben resolverse antes de que resultados con 40 features vayan a la memoria.**
  - Pendientes menores anotados en 3.2 (lista 0-day no persistida · delta 77→122 no regenerable · comparación de columnas por set en `validacion.py:156-159`) y corregida la nota obsoleta de la sección 6.0 sobre `plt.show()`/`PYTHONIOENCODING`.
  - **Quedó a medias:** el experimento con/sin selección y la decisión H1 — son lo que falta para cerrar la casilla 4.3.5 (marcada ◐ en 3.1-E).
- `2026-07-06` — **Arranque del track de modelos** (resumen completo en `sesion-2026-07-06.md`).
  - **Grill previo a implementar**: 6 decisiones cerradas (Q1-Q6) en `resumen-de-decisiones.md`. La de fondo (Q1/C): el set de features (54 vs 122) queda **parametrizable** y lo decide el experimento H1 con datos.
  - **Reconciliación del estado real**: la selección da **54 features** (no 40), y H1-Opción1/H2/H3 ya estaban resueltos en código pese a la prosa de este doc. Deuda de pinning (3.3): ya estaba hecha (`requirements.txt` pinneado).
  - **Base de código creada**: `config.py` (rutas/semilla/convenciones) y `evaluacion.py` (métricas comunes + `evaluar_0day_por_tipo`), ambos verificados. `imbalanced-learn==0.14.2` instalado sin mover sklearn 1.7.1 (Q5).
  - **`anomalias.py` COMPLETO**: implementado (IF/OCSVM/LOF/Autoencoder-MLP, umbral p95 sobre D1_val), auditado (APTO CON CAMBIOS → arreglado: artefactos sufijados por variante, CSV idempotente, backend Agg) y **ejecutado en 54 y 122**. Mejor detector: **Autoencoder ≈ IsolationForest**; LOF el más débil; FPR real ~8-10% (drift, no bug).
  - **`firmas.py` implementado y auditado APTO** (SMOTE dentro del fold, filtrado 0-day por tipo, export_text) — **pendiente de ejecutar**. Nota memoria 4.3.4: SMOTE interpola sobre dummies one-hot (limitación a citar).
  - **Quedó pendiente (orden en §4)**: ejecutar `firmas.py` → `hibrido.py` → experimento H1 (recall 0-day por tipo).
- `2026-07-09` — **Guía de aprendizaje creada** en `Working_Directory/Guia_ML/` (5 ficheros,
  material interno de estudio, no la memoria): README con diagrama del flujo + glosario;
  01 fundamentos y datos; 02 preparación (one-hot, escalado, SMOTE, selección); 03
  validación y métricas (CV, GridSearch, matriz de confusión, ROC/PR); 04 los tres
  modelos + argumento 0-day + discusión RF. Ancla la teoría 2.1.x al código real.
  - **Decisión pendiente registrada (⏸)**: baseline **RF monolítico** como experimento
    de control — ver **3.1-F**. Recomendación: sí; a la espera de aprobación del autor.
  - **Ejecución de `firmas.py` (siguiente step, §4.3) EN PAUSA** hasta resolver 3.1-F:
    si se añade el baseline, cambia lo que se ejecuta en esta tanda.
- `2026-07-11` — **Firmas ejecutadas, baseline creado/ejecutado y 3.1-F resuelta** (resumen completo en `sesion-2026-07-11.md`; decisión 3.1-F completa en `resumen-de-decisiones.md`, entrada 2026-07-11 — no se duplica aquí).
  - **3.1-F resuelta**: baseline RF monolítico **APROBADO** por el autor, ubicación **`baseline.py` aparte** (no modo de `firmas.py`). Casilla 3.1-F pasa a ☑.
  - **`firmas.py` EJECUTADO (54 y 122)** — antes estaba `◐` (implementado sin ejecutar). Cerradas las 4 casillas de 3.1-B y la de 4.3.4 balanceo. Ganadores de balanceo: DT→class_weight, RF/KNN/HistGB→SMOTE. Métricas D2 multiclase (solo tipos conocidos, n=9083, f1_macro): en **54** gana **RandomForest 0.822** (HistGB 0.804 · KNN 0.769 · DT 0.746); en **122** gana KNN 0.753 (RF cae a 0.696). **Hallazgo clave**: 122 generaliza PEOR a D2 pese a igual/mejor CV — sobreajuste a D3 por los dummies extra (RF-122 eligió `max_depth=None` vs `max_depth=10` en RF-54). **Mejor firma para el híbrido: RandomForest sobre 54 (SMOTE)**. u2r es el punto débil universal (37 muestras en D2, f1 0.17–0.45). **La casilla 4.3.5 sigue `◐`** (pendiente el experimento H1).
  - **`baseline.py` CREADO, AUDITADO (APTO, sin leakage) y EJECUTADO (54 y 122)**: RF monolítico, train = D1+D3 (5 clases, 125.973 filas), `GridSearchCV(StratifiedKFold5, f1_macro)` + `class_weight='balanced'`, evaluado sobre **D2 completo** (22.544 filas); parametrizable 54/122 (`--sin-seleccion`). Resultado: f1_macro **CV = 0.909** con `{max_depth: None, n_estimators: 300}` pero **f1_macro D2 = 0.472 (54) / 0.470 (122)** — desplome CV→test; accuracy D2 0.740/0.738; binaria recall 0.575, precision 0.966, FPR 0.027, AUC-ROC 0.957; **recall 0-day global = 0.150** (561/3750; ~85% de 0-day pasan como "normal"); recall_r2l = 0.004, recall_u2r = 0.01; recall 0.0 en apache2/mailbomb/processtable/snmpguess/snmpgetattack, ~1.0 en saint/udpstorm. **Interpretación (cap. 5)**: confirma con datos la tesis del híbrido — un RF supervisado monolítico da un CV alto engañoso, colapsa en test, no detecta 0-day y ahoga r2l/u2r. Es el lado "baseline" de la tabla del experimento H1.
  - **Quedó pendiente (orden en §4)**: `hibrido.py` (cascada anomalía→firmas, 5.3) → experimento H1 (recall 0-day por tipo de la etapa de anomalías) que completa la tabla frente al baseline y decide el set de features definitivo (Q1/C). En paralelo: volcado a memoria caps. 4-5.
- `2026-07-14` — **Grill de diseño de `hibrido.py` completado (SIN código)** (resumen en `sesion-2026-07-14.md`; decisiones completas en `resumen-de-decisiones.md`, § 2026-07-14 — no se duplican aquí).
  - Verificado el estado real en disco (regla §6): leídos `config.py`/`evaluacion.py`/`anomalias.py`/`firmas.py` para fijar las interfaces reales de las que depende el híbrido.
  - **7 decisiones cerradas (H-1…H-7)**: origen de modelos (cargar joblib + reconstruir solo para OOF); detector = Autoencoder por defecto seleccionable + tabla 0-day de los 4 (matiza Q6); firma = RandomForest seleccionable; calibración `UMBRAL_CONF` por presupuesto τ=2pp sobre OOF + tabla de sensibilidad, D2 solo para reportar; binaria del híbrido ≡ etapa 1 por construcción; scoring multiclase = matriz 5×6 + métricas por alcance sin número único; artefactos/CLI = patrón auditado. Pendientes menores anotados (alcance H1, caveat FPR).
  - **Creado `EL_FUTURO.md`**: vías de diferenciación (comentario del profesor sobre el RF). No es de esta sesión rellenarlo.
  - `hibrido.py` pasa a ◐ (diseño cerrado, sin implementar). **Siguiente paso: escribir el código** siguiendo H-1…H-7.
- `2026-07-14` — **`hibrido.py` IMPLEMENTADO** (ratificados antes P-1…P-5 en `resumen-de-decisiones.md`; verificadas las interfaces reales en disco). Clase `NSLKDDHybridEvaluator`: carga los joblibs de detector+firma (no re-entrena, H-1), calibra `UMBRAL_CONF` con `cross_val_predict` OOF sobre D3 —función que **no recibe D2**, línea roja P-4— por presupuesto τ=2pp (H-4), corre la cascada sobre D2 (Autoencoder→RandomForest por defecto, seleccionables, H-2/H-3), reutiliza `_score`/`_estimador_para` de anomalias/firmas (sin reimplementar), y produce: `metricas_hibrido.csv` (binaria=etapa 1 H-5, por-categoría-conocida, f1_macro-5 conservador, FPR), `metricas_hibrido_calibracion.csv` (sensibilidad OOF+D2 de los 3 umbrales), `metricas_hibrido_0day.csv` (recall 0-day por tipo de los 4 detectores + FPR, cierra H1 con P-2), `figuras\hibrido_cm_<set>.png` (matriz 5×6 H-6) y `modelos\hibrido_<set>.joblib` (descriptor, no re-serializa modelos H-7). `py_compile` e `import` OK. **Pendiente: auditoría (`auditor-ml`) → ejecución (54 y 122).**
- `2026-07-15` — **`hibrido.py` auditado (APTO) y ejecutado (54 y 122); experimento H1 cerrado; Q1/C → 54 (opción A); casilla 4.3.5 cerrada.** Auditoría `auditor-ml`: sin bloqueantes; M1 aplicado (endurecimiento del bucle de 4 detectores), M2/M3 notas para 5.3. Ejecución sin errores (`UMBRAL_CONF=0.5`, τ=2pp): binaria recall 0.832 / FPR 0.102 (54); **recall 0-day global 0.771 (54) vs 0.150 del baseline monolítico → tesis del híbrido confirmada ~5×**. Decisión Q1/C (54 vs 122) resuelta hacia **54** con el desglose por tipo: las 122 no rescatan ningún tipo relevante y degradan la firma ~9 pp (sobreajuste a D3); dan un detector marginalmente mejor (Pareto) → opción B a `EL_FUTURO.md §3`. **Hallazgos colaterales (a 5.3 + `EL_FUTURO.md`, más relevantes que 54-vs-122)**: (1) detectores complementarios por tipo (LOF↔`mailbomb`, IF↔`snmpguess`, AE ciego a ambos) → ensemble = línea futura nº1; (2) `snmpgetattack` ciego para los 4 (límite de features NSL-KDD); (3) solo 13.4% de 0-day cazados enrutados a `unknown` (RF sobre-confiado OOD) → open-set. Aclaración: la firma sobre 54 SÍ funciona bien (RF f1_macro 0.822 solo); el débil real es u2r/r2l. Detalle en `resumen-de-decisiones.md` (§ Decisión del 2026-07-15). **Ya no queda código de modelos pendiente; el trabajo restante es el volcado a la memoria (caps. 4-5) + teoría.**
- `2026-07-15` — **Reestructuración del vault COMPLETADA** (agente `redactor-tfg`, verificada en disco). Creadas: `02 Marco Teórico\2.3 Inteligencia Artificial\` (2.3.1-2.3.3, esqueletos para Francisco), `03 Diseño del sistema\` (3.1-3.6), `04 Implementación del sistema\` (4.1-4.6, con H2 4.3.1-4.3.6), `05 Evaluación\` (5.1-5.4; 5.3 = híbrido según decisión 2026-07-02), `06 Conclusiones\` (6.1-6.2) y `Apéndices\` (A.1-A.2). Total **43 notas**; MOC `00 Índice TFG.md` reescrito con leyenda de estados y wikilinks verificados (**0 rotos**). Los esqueletos de resultados referencian sus artefactos fuente y los caveats H-5/H-6/P-2. Las 5 casillas de §2.1 pasan a ☑.
  - **Migración:** los 6 ficheros viejos de `03 Desarrollo\` estaban vacíos (solo "Pendiente de redactar"); mapeo: 3.1→3.1/3.2 Diseño · 3.2→4.2 · 3.3→4.1 · 3.4→3.4 Diseño · 3.5→3.5 Diseño · 3.6→3.3 Diseño. Carpeta vieja borrada (queda el directorio vacío retenido por un handle de Obsidian; desaparece al reiniciar la app).
  - **Reparto de redacción acordado con el autor (2026-07-15):** Claude escribe estructura + volcado de resultados/decisiones; la teoría (2.1.6, 2.2, 2.3 IA) la redacta Francisco (Claude solo propone guiones/temas).
  - **Divergencia menor detectada:** la memoria en disco se llama `TFG - Fran.docx`, no `TFG - KIKO.docx` como dicen `CLAUDE.md` y este doc — pendiente corregir `CLAUDE.md`.
  - **Siguiente paso:** tarea 2 del bloque ★ — volcado de resultados a caps. 4 y 5 (mapa en §6.6 y `Resultados\GUIA_RESULTADOS.md`; leer antes `resumen-de-decisiones.md`).
- `2026-07-15` — **Guiones de teoría escritos en el vault** (agente `redactor-tfg`, aprobado por el autor y verificado en disco). Esquemas orientativos —no prosa— con formato (a) qué contar · (b) conexión con el proyecto · (c) fuente sugerida, en **9 notas**: `2.1.6` (metodologías: CRISP-DM, línea roja D2/P-4, los 3 casos reales de leakage evitado, f1_macro vs accuracy, reproducibilidad, sobreestimación CV→test con el caso baseline 0.909→0.472) · **4 notas NUEVAS en `2.2 Ciberseguridad`**: `2.2.2 Sistemas de detección de intrusiones` (historia Anderson 1980→Denning 1987→Snort/Zeek→SIEM/XDR), `2.2.3 Taxonomía de los IDS`, `2.2.4 Detección por firmas frente a detección por anomalías` (sección-motivación de la tesis; Axelsson 1999 falacia de la tasa base; justificación de la cascada), `2.2.5 Taxonomía de ataques y panorama de amenazas` (DoS/Probe/R2L/U2R con ejemplos del dataset) · las **3 de `2.3 IA` ampliadas** (por qué ML clásico sin DL; adversarial ML/open-set enlazado a `EL_FUTURO.md`; ética: XAI, privacidad, obsolescencia de NSL-KDD, AI Act/NIS2) · `4.2` (guion parte teórica del dataset: DARPA'98→KDD'99→NSL-KDD, 3 grupos de las 41 features).
  - La **redacción en prosa** de los 9 guiones corresponde a **Francisco** (reparto acordado 2026-07-15). Las fuentes sugeridas (Anderson 1980, Denning 1987, Axelsson 1999, Sommer & Paxson 2010, Tavallaee 2009, McHugh 2000, NIST SP 800-94, AI Act/NIS2) **NO están aún en `Bibliografía.md`**: entrarán vía Zotero cuando Francisco las confirme.
  - El MOC lleva ahora un callout `> [!info] Punto actual` bajo el título que refleja la fase en curso (petición del autor: dejar reflejado en cada momento el punto en el que estamos); las notas con guion marcadas `✍ teoría (Francisco) — guion propuesto 2026-07-15`.
  - **Siguiente paso:** tarea 2 del bloque ★ — volcado de resultados a caps. 4 y 5 (pendiente de aprobación del autor).
- `2026-07-16` — **Tarea 2 del bloque ★ (volcado de resultados a caps. 4 y 5) COMPLETADA y AUDITADA.**
  - **Volcado a la memoria**: redactadas en prosa (agentes `redactor-tfg`) las notas `4.3 Preprocesamiento` (subsecciones 4.3.1-4.3.6 completas, incl. tabla de balanceo, selección 122→54 y veredicto H1), `4.4` y `4.5` (protocolos, grids exactos del código, configs ganadoras, 4 reglas comentadas de `firmas_reglas_54.txt`), `5.1`, `5.2` y `5.3` (tablas desde los CSVs, figuras `_54` incrustadas desde `assets\`, caveats H-5/H-6/P-2/M2/M3 cumplidos). Todas pasan a estado `borrador`; el MOC lo refleja.
  - **Dos auditorías adversariales de cifras** (`auditor-ml`): cap. 5 → **APTO CON CAMBIOS** (3 menores: rango recall r2l 0.84-0.89; precisión de la submuestra OCSVM ~53.900→20.000; cadena causal RF-122 marcada como interpretación); cap. 4 → **APTO CON CAMBIOS** (4 obligatorios + 1 opcional). Todos aplicados.
  - **Hallazgo 🟠 relevante con FE DE ERRATAS en `resumen-de-decisiones.md`**: el argumento de descarte de la ventaja 0-day de las 122 features ("mailbomb lo fallan ambos") contradecía a `metricas_hibrido_0day.csv` — la verdad: delta **+55 detecciones**, 36 de `mailbomb` (0.00→0.123 con 122; sigue esencialmente fallado con 36/293) y 20 de `mscan`. **La decisión Q1/C (54) NO cambia** (se sostiene en la degradación ~9 pp de la firma). Corregido en `resumen-de-decisiones.md` (fe de erratas fechada) y en la memoria (4.3.5).
  - **`GUIA_RESULTADOS.md` reconciliada** con el estado real: 54 features (no 40), umbral 99,9%, drift 37, outliers mediana 4,78%, **4** features de D2 fuera de [0,1] (máx. 2,50 en `num_shells` — corrige el "3 features, máx 2,33 en `num_file_creations`" que este documento afirma en la entrada del 2026-07-05), inventario real de artefactos de modelos.
  - Figuras copiadas a `Obsidian_TFG_Vault\assets\` (**29 PNG**) para su incrustación en la memoria.
  - **Siguiente paso sugerido**: tarea 4 del bloque ★ (4.2 dataset + 4.2.1 con figuras EDA/validación + Apéndice A.1) o las conclusiones de capítulo (3.6/4.6/5.4); la teoría en prosa sigue en manos de Francisco.
- `2026-07-16` — **(2ª tarea del día) Parte de Claude de la tarea 4 del bloque ★ COMPLETADA: Apéndice A.1 + subsección 4.2.1.** La parte teórica de 4.2 (origen del dataset, 41 features en prosa, por qué NSL-KDD) NO se tocó — sigue siendo de Francisco (guion ya propuesto 2026-07-15).
  - **A.1** (`Apéndices\A.1 Columnas del dataset NSL-KDD.md`, estado→`borrador`): tabla de las 41 características agrupadas (básicas 1-9, contenido 10-22, tráfico-tiempo 23-31, tráfico-host 32-41) con tipo y descripción; mapeos de etiquetas (40 tipos, 5 categorías, tipo→categoría) desde `_mappings_and_info.txt`; y los **17 tipos 0-day** (en D2 y no en D3) marcados con ★.
  - **4.2.1** (dentro de `04 Implementación del sistema\4.2 Base de datos utilizada.md`, estado nota→`borrador`): EDA + validación en prosa con 5 figuras incrustadas. Cifras volcadas: tamaños D1 67.343 / D2 22.544 / D3 58.630 × 54; desbalance D3 (ratio ≈883:1); los 17 0-day; características discriminantes (flag_S0, flag_SF, logged_in, same_srv_rate); drift KS 37/54 features (top src_bytes 0,346, dst_bytes 0,317, dst_host_rerror_rate 0,298); outliers IQR mediana D1 4,78 %; 4 features de D2 fuera de [0,1].
  - **Verificación factual contra disco (sin pasada de `auditor-ml`)**: los 17 tipos 0-day recalculados con pandas como `set(D2.attack)-set(D3.attack)` coinciden EXACTAMENTE con los ★ (DOS: apache2, mailbomb, processtable, udpstorm · PROBE: mscan, saint · R2L: named, sendmail, snmpgetattack, snmpguess, worm, xlock, xsnoop · U2R: httptunnel, ps, sqlattack, xterm). Los 41 nombres de feature se contrastaron con las columnas reales del CSV original (coinciden en nombre, orden y grupo; la 42ª columna `level` = dificultad, no es feature). Las cifras del EDA/validación se comprobaron directamente, por eso no hizo falta auditoría adversarial.
  - MOC (`00 Índice TFG.md`) ya actualizado por Claude: callout "Punto actual", entradas de 4.2 y A.1 y sus estados.
  - Casillas cerradas por esto: §2.4 "figuras del EDA y de la validación (4.2.1)" → ☑. La casilla de §2.2 "Teoría del dataset NSL-KDD" (que remite el detalle de columnas a A.1) se deja en `☐` porque su cuerpo es la prosa teórica de 4.2, que es de Francisco; A.1 (parte de Claude) ya está hecho. El pendiente menor de §3.2 sobre persistir los 17 0-day en el reporte de `validacion.py` NO queda cubierto (esto es en A.1, no en el reporte del script) — sigue `☐`.
  - **Siguiente paso sugerido**: conclusiones de capítulo (3.6/4.6/5.4) o Apéndice A.2 (métricas) / bibliografía; la teoría en prosa (incl. la de 4.2) sigue en manos de Francisco.
- `2026-07-16` — **(3ª tarea del día) Conclusiones de capítulo 4.6 y 5.4 redactadas (borrador); 3.6 pospuesta a propósito.** Ambas conclusiones sintetizan material ya redactado y auditado (notas 4.x/5.x); **no se generaron cifras nuevas**.
  - **5.4 Conclusiones del capítulo (Evaluación)** (`05 Evaluación\5.4 Conclusiones del capítulo.md`, estado→`borrador`): síntesis de 5.1/5.2/5.3 — mejor detector (Autoencoder), mejor firma (RandomForest+SMOTE), tesis del híbrido (recall 0-day 0.771 vs 0.150 baseline ≈5×), los 3 caveats (P-2 FPR desigual, coste de la cascada 0.822→0.748, binaria≡etapa 1 H-5) y los 3 hallazgos que trascienden 54-vs-122 (ensemble, open-set, `snmpgetattack` punto ciego), enlazados a 6.1/6.2/`EL_FUTURO.md`.
  - **4.6 Conclusiones del capítulo (Implementación)** (`04 Implementación del sistema\4.6 Conclusiones del capítulo.md`, estado→`borrador`): pipeline reproducible (semilla 42, pinning, joblib), decisiones de preprocesado justificadas con datos (one-hot 77→122, scaler D1+D3 anti-leakage, balanceo 4.3.4, selección 4.3.5), anti-leakage transversal (D2 intocable), comparación multi-algoritmo bajo protocolo común, modelos seleccionados y persistidos.
  - MOC (`00 Índice TFG.md`) actualizado por Claude: 4.6 y 5.4 → `borrador`, callout "Punto actual" al día.
  - **Hallazgo estructural (razón por la que 3.6 NO se escribió)**: el cuerpo del **cap. 3 Diseño (notas 3.1 Requisitos, 3.2 Arquitectura, 3.3 Metodología, 3.4 Modelo anomalías, 3.5 Modelo firmas) sigue en esqueleto** (bloques `> [!todo]`, estado `pendiente`). Escribir la conclusión de un capítulo aún no redactado sería hueca e inconsistente → **3.6 queda pendiente hasta que exista el cuerpo del cap. 3**. Además **4.1 Tecnologías utilizadas** (4.1.1/4.1.2/4.1.3) sigue en esqueleto (sección descriptiva menor; fuente `Implementacion\readme.md` y `requirements.txt`).
  - **Consecuencia para la planificación**: el cuerpo del **cap. 3 Diseño (3.1-3.5)** es ahora el mayor hueco estructural de la memoria. NO es teoría (ML/Ciber/IA) sino diseño del sistema (arquitectura/cascada/splits/protocolo) → corresponde a **Claude** según el reparto, con material fuente disponible (`PIPELINE.md`, `resumen-de-decisiones.md`, notas 4.x/5.x ya escritas). Es la **próxima tarea operativa recomendada**; tras ella, cerrar 3.6.
  - **Siguiente paso sugerido**: redactar el cuerpo del cap. 3 Diseño (3.1-3.5) → cerrar 3.6; tareas menores restantes: 4.1 Tecnologías, Apéndice A.2 (métricas) y bibliografía; la teoría en prosa sigue en manos de Francisco.
- `2026-07-16` — **(4ª tarea del día) Cuerpo del cap. 3 Diseño (3.1-3.6) redactado en prosa (borrador); 3.6 cerrada.** Se completó el mayor hueco estructural que quedaba en la memoria. Nivel de redacción **conceptual** (el qué y el porqué), SIN cifras de resultados (cap. 5) ni detalle de entrenamiento (cap. 4), con referencias cruzadas a 4.x/5.x. Fuentes: esqueletos previos, `PIPELINE.md`, `resumen-de-decisiones.md` y las notas 4.x/5.x ya escritas. **No se generaron cifras nuevas.** Las 6 notas pasan a `borrador`:
  - **3.1 Requisitos del sistema**: funcionales (detectar anómalo/0-day, clasificar 4 categorías, señalar desconocido), de datos (NSL-KDD, D1/D3 train especializado, D2 test realista), no funcionales (reproducibilidad `random_state=42`, interpretabilidad de firmas, sin Deep Learning pesado — solo scikit-learn) y de alcance (comparar varios algoritmos por etapa).
  - **3.2 Arquitectura del sistema**: cascada 2 etapas anomalías→firmas con **diagrama Mermaid**; por qué ese orden (firmas no conoce la clase 'normal'); de dónde sale la detección 0-day.
  - **3.3 Metodología de funcionamiento**: diseño de splits D1/D2/D3, ajuste del escalador sobre D1+D3 (anti-leakage), recorrido de un flujo por la cascada (6 veredictos posibles), protocolo de evaluación común (D2 intocable).
  - **3.4 Modelo de detección de anomalías** (diseño, no implementación): planteamiento one-class; 4 algoritmos candidatos (IF/OCSVM/LOF/Autoencoder) de familias distintas; diseño del umbral p95 sobre validación de D1; papel de filtro binario en la cascada.
  - **3.5 Modelo de detección basado en firmas** (diseño): clasificación supervisada multiclase sobre D3 (sin clase normal); 4 algoritmos (DT/RF/KNN/HistGB); firmas interpretables (`export_text`, analogía IDS clásico); desbalance como decisión de diseño (SMOTE vs class_weight); salida "desconocido/0-day".
  - **3.6 Conclusiones del capítulo (Diseño)**: síntesis de las decisiones de diseño y puente al cap. 4. **Queda cerrada** (en la 3ª tarea de hoy se había pospuesto a propósito por falta de cuerpo del capítulo).
  - MOC (`00 Índice TFG.md`) actualizado por Claude: 3.1-3.6 → `borrador`, callout "Punto actual" indica "cap. 3 Diseño completo".
  - **Siguiente paso sugerido**: conclusiones globales 6.1/6.2 (fuente `EL_FUTURO.md`+`resumen-de-decisiones.md`, NO el código), 4.1 Tecnologías (esqueleto; fuente `readme.md`+`requirements.txt`), Apéndice A.2 (métricas) o bibliografía; la teoría en prosa sigue en manos de Francisco.
- `2026-07-16` — **(5ª tarea del día) 6.1 Conclusiones redactada (borrador); 6.2 delegada a Francisco; divergencia del `.docx` resuelta.** Síntesis de material ya volcado; **sin cifras nuevas** (todo del cap. 5 y de `resumen-de-decisiones.md`).
  - **6.1 Conclusiones** (`06 Conclusiones\6.1 Conclusiones.md`, estado→`borrador`): grado de cumplimiento de los objetivos de [[1.3 Objetivo]] (general + 4 específicos, todos cumplidos; matiz: la comparación multi-algoritmo amplió el mínimo exigido); validación de la tesis del híbrido (recall 0-day 0.771 vs 0.150 baseline ≈5×; f1_macro baseline 0.909 CV → 0.472 test; firmas y anomalías complementarias); y limitaciones honestas (FPR ~10% por drift, u2r/r2l débiles, enrutado a "unknown" limitado, `snmpgetattack` ciego por límite del dataset). Enlaza a 6.2 sin redactarla.
  - **6.2 Líneas futuras**: NO se redacta. **Decisión del autor (2026-07-16)**: Francisco la está investigando y podría derivar en un apartado propio del informe → queda como **tarea de Francisco**, fuera de la lista operativa de Claude. En el MOC se marcó como "✍ en investigación por Francisco".
  - **Divergencia del `.docx` RESUELTA** (arrastrada desde la bitácora 2026-07-15): el documento final del repo es **`TFG - Fran.docx`** (confirmado por el autor), no `TFG - KIKO.docx`. Corregidas las 2 referencias en `CLAUDE.md` (árbol de estructura + sección propia) y las 2 de este doc (§2.3 y §6.0). No existía casilla en §2.x para esta divergencia; queda cerrada aquí.
  - MOC (`00 Índice TFG.md`) actualizado por Claude: 6.1→borrador, 6.2→en investigación (Francisco), callout "Punto actual" al día.
  - **Siguiente paso sugerido**: tareas operativas de Claude restantes = **4.1 Tecnologías utilizadas** (esqueleto; fuente `readme.md`+`requirements.txt`), **Apéndice A.2** (métricas), **bibliografía** (Zotero/IEEE) y **Resumen/Abstract** (al final). La teoría en prosa (2.x) y **6.2** siguen en manos de Francisco.
- `2026-07-16` — **(6ª y última tanda del día) Cerradas las 2 deudas de incoherencia de `CLAUDE.md` que quedaban; las 3 incoherencias históricas quedan resueltas. Cierre de sesión.** Solo verificación en disco/código y corrección de documentación; **sin cambios de código ni cifras nuevas**.
  - **Deuda 🟠 "Incoherencia de ruta" RESUELTA** (§3.2, casilla ☑): verificado en disco y en `program.py` (líneas 91 y 388/1087/1137) que la ruta real del dataset es `...\KIKO_TFG\Working_Directory\Archivos dataset\` y la de salida `...\Working_Directory\Resultados\`; la vieja `...\KIKO\...` no existe. Corregidas ambas rutas en `CLAUDE.md`.
  - **Deuda 🟡 "Conteo de tipos de ataque" RESUELTA** (§3.2, casilla ☑): la cifra real es **40 etiquetas del `LabelEncoder` = `normal` + 39 tipos de ataque** → 5 categorías (fuente `specialized_nsl_kdd_mappings_and_info.txt`; coherente con la nota 4.3.1 del vault). Corregido el "51 tipos" erróneo en `CLAUDE.md` (→ "39 tipos de ataque") y en `PIPELINE.md`.
  - Con esto quedan cerradas las **3 incoherencias históricas de `CLAUDE.md`**: nombre del `.docx` (`TFG - Fran.docx`, resuelta en la 5ª tarea), ruta del dataset y conteo de tipos.
  - **Resumen de la sesión 2026-07-16 (6 tandas)**: se completaron A.1 + 4.2.1, el cuerpo del cap. 3 Diseño (3.1-3.6), las conclusiones de capítulo 4.6/5.4 y las conclusiones globales 6.1, más las correcciones de documentación en `CLAUDE.md` y `PIPELINE.md`. **Tareas operativas de Claude que restan para próximas sesiones**: 4.1 Tecnologías utilizadas, Apéndice A.2 (métricas), bibliografía (Zotero/IEEE) y Resumen/Abstract (al final). **6.2 Líneas futuras** la investiga Francisco (posible apartado propio); la **teoría en prosa (2.x)** sigue en manos de Francisco.
- `2026-07-16` — **(7ª tarea del día) 4.1 Tecnologías utilizadas redactada en prosa (borrador).** Sección descriptiva menor del cap. 4; fuentes `Implementacion\readme.md` y `Implementacion\requirements.txt` (verificadas en disco). **No se generaron cifras nuevas ni se tocó código.** La nota (`04 Implementación del sistema\4.1 Tecnologías utilizadas.md`, estado→`borrador`) cubre sus tres subsecciones:
  - **4.1.1 Entorno y aplicaciones**: Windows 11, entorno virtual (venv `Imp`, Python 3.11), VS Code, Git, Obsidian, Word + Zotero.
  - **4.1.2 Lenguaje**: Python 3.11 (justificación: ecosistema científico, estabilidad de versión, reproducibilidad sensible a la versión de scikit-learn).
  - **4.1.3 Librerías**: tabla de las 9 librerías directas con versión exacta (de `requirements.txt`) y su papel en el pipeline (numpy, pandas, scikit-learn, imbalanced-learn, scipy, matplotlib, seaborn, joblib, pillow) + nota sobre dependencias transitivas pinneadas + nota de que NO hay dependencia de Deep Learning (autoencoder vía `MLPRegressor`).
  - MOC (`00 Índice TFG.md`) ya actualizado por Claude: 4.1→borrador y callout "Punto actual" al día.
  - **Siguiente paso sugerido**: **Apéndice A.2 Métricas de desempeño** (autocontenida, cerrable por Claude). Quedan después la **bibliografía** (requiere Zotero → Francisco) y el **Resumen/Abstract** (al final). La teoría en prosa (2.x) y **6.2** siguen en manos de Francisco.
- `2026-07-16` — **(8ª tarea del día) Apéndice A.2 Métricas de desempeño redactado (borrador) e incoherencia del checklist de `CLAUDE.md` cerrada.** Solo redacción de apéndice y corrección de documentación; **sin cifras nuevas ni cambios de código**.
  - **A.2 Métricas de desempeño** (`Apéndices\A.2 Métricas de desempeño.md`, estado→`borrador`) redactada como **apéndice de fórmulas de referencia**, NO teoría conceptual (esa sigue en 2.1.5, de Francisco). Contenido: matriz de confusión binaria y multiclase (5×6 en el híbrido); fórmulas de Precision, Recall/TPR, F1, FPR, promedios macro/weighted, AUC-ROC y AUC-PR; y **A.2.1** (caso one-class: score de anomalía, umbral p95 sobre D1_val = FPR nominal 5%, FPR nominal vs real ~8-10% por drift, salvaguarda anti-leakage sobre D2). Convención **positivo=ataque=1**. MOC ya actualizado por Claude (A.2→borrador + callout).
  - **Incoherencia del checklist "Estado actual del código" de `CLAUDE.md` RESUELTA**: marcaba aún como pendientes `[ ]` el entrenamiento de anomalías, la extracción de firmas y la evaluación conjunta (completados hace días). Ahora marca ☑ todo el track de código (balanceo/selección en `program.py`, `anomalias.py`, `firmas.py`, `baseline.py`, `hibrido.py`) con nota de estado 2026-07-16 remitiendo a `next-steps.md`/`resumen-de-decisiones.md`. También se alineó la línea de "Dependencias principales" de `CLAUDE.md` para incluir `imbalanced-learn` y `joblib`. Cierra la última incoherencia conocida de `CLAUDE.md` frente al disco.
  - **Siguiente paso sugerido**: tareas operativas de Claude restantes = **bibliografía** (Zotero/IEEE → requiere Zotero, Francisco) y **Resumen/Abstract** (al final). La teoría en prosa (2.x) y **6.2** siguen en manos de Francisco.
- `2026-07-21` — *(registrado 2026-07-22)* — **Sesión de redacción del vault: terminología unificada, 4.2 teórica cedida a Claude y convención de código incrustado.** Todo verificado en disco; **sin cambios de código ni cifras nuevas**. Notas afectadas quedan en `borrador`. Decisiones nuevas en `resumen-de-decisiones.md` (§ Decisiones del 2026-07-21).
  - **Terminología "semisupervisado" unificada.** Término canónico del detector de anomalías = **"semisupervisado (one-class)"**; "no supervisado" se admite como sinónimo declarado una sola vez. Editado el párrafo de `3.4 Modelo de detección de anomalías.md` §3.4.1 (reconciliación semisupervisado↔no supervisado, con nota de que scikit-learn y la literatura lo usan indistintamente) y las 2 ocurrencias de "no supervisado/a" de `4.4 Entrenamiento del modelo de detección de anomalías.md` → "semisupervisado/a" (+ enlace a 3.4). Verificado en disco (3.4.1 líneas 13-15; 4.4 líneas 9 y 13).
  - **`3.5 Modelo de detección basado en firmas.md`**: §3.5.3 añade la definición de "interpretabilidad" al inicio del apartado; §3.5.5 añade un párrafo con el criterio de diseño de `UMBRAL_CONF` (anti-leakage, probabilidades OOF sobre D3, regla de presupuesto), remitiendo a 5.3 para la calibración concreta.
  - **`4.1 Tecnologías utilizadas.md` §4.1.3**: frase nueva en la prosa del cuerpo sobre las dependencias transitivas pinneadas (el callout ya existía). Verificado exacto contra `requirements.txt`: **21 entradas = 9 directas + 12 transitivas** (coincide).
  - **`4.2 Base de datos utilizada.md` — prosa TEÓRICA redactada como borrador de Claude** (antes ✍ Francisco): «Origen» (DARPA 1998→KDD'99→NSL-KDD), «Las 41 características y sus 3 grupos», «Por qué se eligió NSL-KDD». Con marcadores `[CITA:...]` pendientes de Zotero y el bloque «Por qué NSL-KDD» a revisión de Francisco. Casilla §2.2 «Teoría del dataset NSL-KDD» pasa de `☐` (Francisco) a `◐` (borrador Claude 2026-07-21); **NO se cierra** hasta resolver citas y esa revisión.
  - **Convención NUEVA: código incrustado en la memoria.** Fragmentos de código Python **verbatim recortados** (elisiones `# ...`, código real, no pseudocódigo), inline en la sección que ilustran. Incrustados en 4.3.1 (LabelEncoder sobre el vocabulario del mapeo), 4.3.2 (`scaler.fit` sobre D1+D3 + transform), 4.3.3 (unión one-hot D1∪D3), 4.3.4 (`ImbPipeline` SMOTE + `cross_val_score`), 4.3.5 (los 2 pasos de `select_features`), 4.4 (`_score`, score de anomalía unificado) y 4.5 (`export_text`). Verificado en disco: **7 bloques `python`** (5 en 4.3, 1 en 4.4, 1 en 4.5).
  - **Divergencia detectada (coherencia, NO resuelta — territorio de Francisco)**: `2.2.4 Detección por firmas frente a detección por anomalías.md` sigue diciendo "detectores no supervisados", que contradice el término canónico recién fijado ("semisupervisado"). Es teoría en prosa de Francisco → se reporta, no se toca.
  - **Siguiente paso sugerido**: sin cambios respecto al plan previo — **bibliografía** (Zotero → Francisco) y **Resumen/Abstract** (al final); teoría en prosa (2.x) y **6.2** siguen en manos de Francisco.

---

## 6. Guía de ejecución detallada (re-onboarding)

> Escrita para retomar el proyecto **en frío**. Cada subsección es autocontenida: qué tocar, dónde, cómo, qué debe salir y qué trampas evitar.

### 6.0 Re-arranque en 5 minutos

**Qué es esto:** TFG de un NIDS híbrido sobre NSL-KDD. Dos modelos ML (anomalías entrenado solo con tráfico normal; firmas entrenado solo con ataques) que se combinan en cascada y se evalúan sobre el test. El preprocesado **ya funciona**; los modelos son lo que falta.

**Arrancar el entorno:**
```powershell
cd C:\Users\francisco.lopez\KIKO_TFG\Working_Directory\Implementacion
.\Imp\Scripts\Activate.ps1          # venv Python 3.11
python app\program.py               # regenera splits D1/D2/D3 (figuras EDA → Resultados\figuras\, no bloquea)
python app\validacion.py            # valida los CSVs; imprime APROBADA/FALLA y guarda *_validation_report.txt + figuras validacion_*.png
```
> Desde 2026-07-05 ambos scripts se ejecutan **sin variables de entorno ni bloqueos**: utf-8 vía `sys.stdout.reconfigure` (ya no hace falta `PYTHONIOENCODING`) y todas las figuras van a `Resultados\figuras\` con `savefig` (nada de `plt.show()`).

**Dónde está cada cosa:**
| Qué | Ruta |
|---|---|
| Dataset crudo | `Working_Directory\Archivos dataset\KDDTrain+.txt` / `KDDTest+.txt` |
| CSVs generados | `Working_Directory\Resultados\specialized_nsl_kdd_*` |
| Ficheros clave | `*_processed_X_D1_normal_for_anomaly.csv` · `*_processed_X_D2_complete_test.csv` · `*_processed_X_D3_known_attacks_for_signatures.csv` + sus `y_attack`/`y_category` |
| Informe (fuente) | `Obsidian_TFG_Vault/` (se vuelca a `TFG - Fran.docx` al final) |
| Helper de carga | `program.py` → función suelta `load_specialized_splits(base_path)` (devuelve dict `{'D1','D2','D3'}`) |

**Números de referencia (NSL-KDD, aproximados — verifica con la salida de `program.py`):**
- D1 (train normal): ~67.300 · D3 (train ataques): ~58.600 · D2 (test completo): ~22.500 (≈43% normal / 57% ataque).
- Desbalance D3: dos ~45,9k · probe ~11,7k · r2l ~1,0k · **u2r ~52**.
- D2 contiene **~17 tipos de ataque que NO existen en el train** (los "0-day" del experimento; `validacion.py` los lista).

**Estado del preprocesado actual:** One-Hot de `protocol_type/service/flag` + `MinMaxScaler` ajustado en D1+D3 (en `main()` se llama con `scaler_type='minmax'` — mantenerlo: OCSVM, KNN y el autoencoder agradecen [0,1]).

---

### 6.1 PASO 0 — Arreglar el bug 🔴 del one-hot

**Dónde:** `Implementacion/app/program.py`, método `preprocess_specialized_splits`, bloque **"Paso 2: Alineando columnas (referencia D1)"** (~líneas 272-280).

**El problema exacto:** esta línea toma como vocabulario SOLO las columnas de D1 (tráfico normal):
```python
self.feature_columns_after_encoding = list(encoded[D1_KEY]['X_enc'].columns)
```
Los dummies de `service`/`flag` que solo aparecen en tráfico de ataque (D3) se descartan al reindexar → el modelo de firmas pierde justo las señales más discriminantes.

**El fix (vocabulario = unión del train D1+D3, orden determinista):**
```python
train_cols = sorted(set(encoded[D1_KEY]['X_enc'].columns) | set(encoded[D3_KEY]['X_enc'].columns))
self.feature_columns_after_encoding = train_cols
```
Las categorías que solo existen en D2 (test) se quedan fuera **a propósito**: en producción tampoco las conocerías; queda como cero en todas las dummies. No es leakage, es realismo — explícalo así en la memoria (4.3.3).

**Después del fix, en la misma pasada (deuda 3.3 barata):**
1. Quitar el import sin uso de `train_test_split` (línea 6).
2. Persistir transformadores al final de `preprocess_specialized_splits` o en `save_specialized_splits`:
   ```python
   import joblib
   joblib.dump({'scaler': self.scaler, 'label_encoder': self.label_encoder,
                'category_encoder': self.category_encoder,
                'feature_columns': self.feature_columns_after_encoding},
               f'{base_path}_transformers.joblib')
   ```
3. (Opcional, calidad de vida) cambiar `plt.show()` del EDA por `plt.savefig(...)` en `Resultados/figuras/` — deja de bloquear la ejecución y las figuras quedan listas para la memoria.

**Verificación:** ejecutar `program.py` → **anota el nº de características que imprime el Paso 2 antes y después** (debe subir; ese delta va a la memoria como justificación del fix). Luego `validacion.py` → debe seguir `APROBADA`. Marcar la casilla 🔴 en 3.2.

> `☑` **COMPLETADO 2026-07-05.** Delta: 77 → 122 features (+45 dummies exclusivos de D3 recuperados). CSVs regenerados (D1 67.343×122 · D2 22.544×122 · D3 58.630×122), `validacion.py` APROBADA, auditoría adversarial APTO (sin leakage). También hechos los 3 extras: import de `train_test_split` eliminado, transformadores persistidos (`..._transformers.joblib`) y `plt.show()` → `savefig` en `program.py` (`Resultados\figuras\eda_distribuciones_divisiones.png`). Ojo: `validacion.py` conserva 4 `plt.show()` (líneas 250, 318, 381, 428).

---

### 6.2 Añadir 4.3.4 (balanceo) y 4.3.5 (selección) al pipeline

**Selección de características → SÍ se materializa en `program.py`** (nuevo paso tras el escalado):
1. **Filtro barato:** eliminar features con varianza ≈ 0 (sobre D1+D3) y, de cada par con |corr| > 0.95, conservar la de mayor varianza. `validacion.py` ya calcula ambas cosas — copia la lógica, no la rehagas.
   ⚠️ **Trampa (auditoría 2026-07-05):** la lista de varianza ~0 de `validacion.py` está calculada **solo sobre D1** — muchas de esas "48 features" son los dummies exclusivos de D3 recuperados por el fix del paso 0. **NO reutilizar esa lista D1-only**: recalcular la varianza sobre D1+D3 (ver bitácora 2026-07-05) o el filtro deshace el fix silenciosamente.
2. **Importancias:** entrenar un `RandomForestClassifier(n_estimators=100, random_state=42, class_weight='balanced')` sobre **D1+D3** con `y_category` (5 clases: normal + 4 ataques), ordenar `feature_importances_` descendente y conservar el top-N que acumule **~99%** de la importancia.
3. Guardar: lista en `Resultados/selected_features.txt` (con la importancia de cada una) y **regenerar los CSVs de X ya filtrados** (así `anomalias.py`/`firmas.py` no tienen que saber nada de la selección).
4. Para la memoria: correr los modelos con/sin selección una vez que existan (basta el baseline IF y RF) y meter la tabla comparativa en 4.3.5.

**Balanceo → NO se materializa en CSVs; vive dentro de `firmas.py`:**
- SMOTE debe aplicarse **dentro de cada fold del CV**, nunca antes (si sobremuestras antes del split, los folds de validación contienen sintéticos derivados del train → CV optimista). La herramienta correcta:
  ```python
  from imblearn.pipeline import Pipeline as ImbPipeline
  from imblearn.over_sampling import SMOTE
  pipe = ImbPipeline([('smote', SMOTE(random_state=42, k_neighbors=5)), ('clf', modelo)])
  # u2r tiene ~52 muestras → en folds de 5, ~41 por fold: k_neighbors=5 aún cabe, pero si peta usa k_neighbors=3
  ```
- Instalar antes: `pip install imbalanced-learn` y **añadirlo a `requirements.txt`**.
- El mini-experimento decidido: por algoritmo, comparar `SMOTE` vs `class_weight='balanced'` (DT/RF lo tienen; **KNN y HistGB no** → en esos dos, SMOTE vs nada) con `f1_macro` en CV. La tabla resultante ES el contenido de la sección 4.3.4 de la memoria.

---

### 6.3 `anomalias.py` — especificación

**Clase sugerida `NSLKDDAnomalyTrainer`** (mismo estilo que las existentes). Flujo:

1. **Carga:** `load_specialized_splits(...)` → X de D1 y D2, y binaria de D2: `y_bin = (y_category_original != 'normal')`.
2. **Split de D1:** `train_test_split(X_D1, test_size=0.2, random_state=42)` → `D1_train` / `D1_val`.
3. **Score unificado** (clave para comparar en igualdad; en sklearn "mayor score = más normal", nosotros queremos "mayor = más anómalo"):

| Algoritmo | Anomaly score | Nota |
|---|---|---|
| `IsolationForest(random_state=42)` | `-model.score_samples(X)` | rápido, sin problema con 67k |
| `OneClassSVM(kernel='rbf')` | `-model.decision_function(X)` | **entrenar con submuestra de D1_train de 20.000** (`.sample(n=20000, random_state=42)`) — O(n²); documentar en memoria |
| `LocalOutlierFactor(novelty=True)` | `-model.score_samples(X)` | `novelty=True` obligatorio para poder puntuar D2 |
| Autoencoder: `MLPRegressor(random_state=42, early_stopping=True)` entrenado con `fit(X, X)` | MSE de reconstrucción por muestra: `((model.predict(X) - X)**2).mean(axis=1)` | sin TF/Keras; arquitectura tipo `(64, 32, 64)` |

4. **Selección de hiperparámetros (no hay `GridSearchCV` sin etiquetas):** construir un set de validación etiquetado con **D1_val (normal) + una muestra de D3** (p. ej. 5.000 ataques, `random_state=42`) y elegir la configuración con mejor **AUC-ROC** sobre él. Es defendible: usa solo ataques *conocidos* (train), jamás D2. Grids pequeños:
   - IF: `n_estimators [100,200,300]` × `max_samples [0.5, 1.0]`
   - OCSVM: `nu [0.01, 0.05, 0.1]` × `gamma ['scale', 0.01, 0.1]`
   - LOF: `n_neighbors [10, 20, 35, 50]`
   - AE: `hidden_layer_sizes [(64,32,64), (32,16,32)]`
5. **Umbral (decisión fijada):** con la config ganadora, `umbral = np.percentile(anomaly_score(D1_val), 95)` — solo sobre lo normal, ≈5% de FPR aceptado. **Mismo percentil para los 4.** Nunca tocar D2 para esto.
6. **Evaluación sobre D2 (binaria):** `y_pred = score > umbral`. Reportar por algoritmo: AUC-ROC, AUC-PR, precision/recall/F1 (clase ataque), FPR real, matriz de confusión 2×2.
7. **Persistir:** `Resultados/modelos/anomalia_<algo>.joblib` (modelo + umbral + config), `Resultados/metricas_anomalias.csv` (fila por algoritmo → tabla de 5.1.2), figuras ROC/PR superpuestas de los 4 (→ figura estrella de 5.1) y matrices de confusión (→ 5.1.1).

**Trampas conocidas:** LOF sin `novelty=True` no tiene `predict` para datos nuevos · el AE con MinMax [0,1] converge mejor · si OCSVM tarda >10 min, baja la submuestra y documenta.

---

### 6.4 `firmas.py` — especificación

**Clase sugerida `NSLKDDSignatureTrainer`.** Flujo:

1. **Carga:** X de D3 + `y_category` de D3 (4 clases de ataque; aquí NO hay 'normal').
2. **Protocolo:** `GridSearchCV(cv=StratifiedKFold(5, shuffle=True, random_state=42), scoring='f1_macro')` — `f1_macro` porque con u2r al 0,1% el accuracy miente.
3. **Grids pequeños:**
   - DT: `max_depth [5, 10, 20, None]` × `min_samples_leaf [1, 5, 20]`
   - RF: `n_estimators [100, 300]` × `max_depth [10, None]`
   - KNN: `n_neighbors [3, 5, 11]` × `weights ['uniform', 'distance']`
   - HistGB: `learning_rate [0.05, 0.1]` × `max_iter [100, 300]`
4. **Mini-experimento de balanceo** (ver 6.2): cada algoritmo × {SMOTE, class_weight/nada} → tabla `f1_macro` CV → sección 4.3.4.
5. **Evaluación sobre D2 (multiclase, para 5.2):** SOLO sobre las filas de ataque de D2 cuyo tipo exista en el train (las ~17 clases nuevas se excluyen aquí: son el trabajo de la etapa de anomalías y se miden en el híbrido). Matriz de confusión 4×4 por algoritmo (→ 5.2.1), precision/recall/F1 por categoría + macro (→ 5.2.2), tabla comparativa de los 4 (→ 5.2.3).
6. **Extracción de firmas (la parte "IDS clásico" de la memoria):** con el mejor DecisionTree, `sklearn.tree.export_text(dt, feature_names=..., max_depth=5)` → reglas legibles tipo `si srv_serror_rate > 0.5 y flag_S0 = 1 → dos (neptune)`. Guardar en `Resultados/firmas_reglas.txt` y comentar 3-4 reglas en la sección 4.5 conectándolas con el ataque real que describen.
7. **Persistir:** `Resultados/modelos/firma_<algo>.joblib`, `Resultados/metricas_firmas.csv`, figuras.

---

### 6.5 `hibrido.py` — especificación

> ⚠️ **OBSOLETA EN PARTE (boceto pre-grill).** La especificación **vigente** de `hibrido.py`
> es el grill del **2026-07-14** en `resumen-de-decisiones.md` (decisiones **H-1…H-7** +
> *Pendientes de diseño*). Donde esta §6.5 y el grill discrepen, **manda el grill**. En concreto:
> `UMBRAL_CONF` NO se calibra "con un split de validación de D3" (lo que dice abajo) sino por
> **OOF (`cross_val_predict`) con presupuesto τ=2pp** (H-4); el detector es **Autoencoder** por
> defecto (H-2) y la firma **RandomForest** (H-3); la binaria ≡ etapa 1 (H-5); scoring = matriz
> 5×6 sin número único (H-6). Esta §6.5 se mantiene solo como contexto de la lógica de cascada.

**Lógica de la cascada (decidida):**
```python
score = anomaly_score(mejor_modelo_anomalias, X_D2)
es_sospechoso = score > umbral                       # etapa 1
proba = mejor_modelo_firmas.predict_proba(X_D2[es_sospechoso])
categoria = proba.argmax(axis=1)                     # etapa 2
categoria[proba.max(axis=1) < UMBRAL_CONF] = 'unknown'   # 0-day
# no sospechoso → 'normal'
```
- `UMBRAL_CONF`: explorar `[0.4, 0.5, 0.6]` **calibrando con un split de validación de D3** (no con D2); justificar el elegido.
- **Evaluaciones para 5.3:**
  1. **Binaria** del sistema completo (normal vs cualquier-ataque) — comparar contra el mejor detector de anomalías solo: ¿aporta la cascada?
  2. **Multiclase** 5 categorías (+unknown): las predicciones 'unknown' cuentan como acierto binario pero se reportan aparte.
  3. **Análisis 0-day**: de los ~17 tipos de D2 ausentes del train, ¿qué % marca la etapa 1 como sospechoso? Tabla tipo→%detección. Este es el argumento central de las conclusiones del TFG.
- **Persistir:** `Resultados/metricas_hibrido.csv` + matriz de confusión final + tabla 0-day.

### 6.5b `evaluacion.py` — módulo común (hazlo ANTES que 6.3)

Funciones que usan los tres scripts (evita triplicar código):
- `evaluar_binario(y_true, y_pred, y_score=None)` → dict con precision/recall/F1/FPR/AUCs.
- `evaluar_multiclase(y_true, y_pred, labels)` → dict + `classification_report`.
- `plot_matriz_confusion(...)`, `plot_roc_pr(dict_de_scores)` → guardan PNG en `Resultados/figuras/` (300 dpi, títulos en español — van directas a la memoria).
- `guardar_metricas(dict, csv_path)` → append de una fila por experimento (algoritmo, params, métricas, fecha) — ese CSV acumulado es la "tabla única" del roadmap 3.1-D.

---

### 6.6 Volcado al informe — mapa resultado → sección

| Artefacto generado | Sección de la memoria |
|---|---|
| Delta de features del fix one-hot (6.1) | 4.3.3 Codificación |
| Tabla SMOTE vs class_weight (6.4) | 4.3.4 Balanceo |
| `selected_features.txt` + tabla con/sin (6.2) | 4.3.5 Selección |
| Grids + configs ganadoras (6.3/6.4) | 4.4 / 4.5 Entrenamiento |
| `firmas_reglas.txt` (reglas comentadas) | 4.5 |
| `metricas_anomalias.csv` + ROC/PR + matrices | 5.1 completo |
| `metricas_firmas.csv` + matrices + comparativa | 5.2 completo (5.2.3 = tabla de los 4) |
| `metricas_hibrido.csv` + análisis 0-day | 5.3 (nueva sección decidida) |
| Figuras EDA + `*_validation_report.txt` | 4.2.1 Análisis previo de la BD |

Recordatorio: la reestructuración del vault (sección 2.1: separar Diseño/Implementación, crear 05 Evaluación, bloque IA, apéndices) → `☑` **hecha 2026-07-15** (ver bitácora §5). El volcado ya tiene sus secciones destino creadas como esqueletos en el vault.

### 6.7 Checklist de cada sesión de trabajo

- **Al abrir:** leer la bitácora (sección 5) y los ⏸/◐ de este doc → elegir UNA tarea.
- **Al cerrar:** marcar casillas, apuntar en la bitácora qué se hizo y qué quedó a medias (con fecha absoluta).
- **Regla de oro:** si un resultado va a la memoria, tiene que salir de un script reproducible con `random_state=42`, no de una ejecución manual perdida.
