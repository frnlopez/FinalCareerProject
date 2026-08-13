# Resumen de decisiones — TFG H-NIDS

> Registro **conciso** de las decisiones de diseño ya cerradas, para no re-litigarlas.
> Complementa a `features.md` (registro operativo vivo de tareas abiertas y cerradas) y a `next-steps.md`, congelado en cuanto a casillas: su §1-§5 es historial y bitácora, y su §6 sigue vigente como especificación técnica de cada script, salvo §6.5 (`hibrido.py`), superada por el grill H-1…H-7 de este mismo fichero.
> Regla: toda decisión de diseño del proyecto se registra aquí en el momento de tomarse.
> Regla: si este fichero y el código divergen, **el código/disco es la fuente de verdad**.

---

## Decisiones cerradas el 2026-07-02 (entrevista de grill)

Detalle completo en `next-steps.md §5`. Resumen:

1. Cap. 5 de la memoria gana sección **5.3 Resultados del sistema híbrido** (+5.4 conclusiones).
2. **Anomalías**: comparar 4 algoritmos — IsolationForest, OneClassSVM, LocalOutlierFactor, Autoencoder (vía `MLPRegressor`, sin TF/Keras).
3. **Firmas**: comparar 4 algoritmos — DecisionTree, RandomForest, KNN, HistGradientBoosting (todo sklearn).
4. **Balanceo (4.3.4)**: mini-experimento SMOTE vs `class_weight='balanced'`, SMOTE **dentro de cada fold** del CV (nunca antes del split), `imbalanced-learn`.
5. **Selección (4.3.5)**: filtro varianza/correlación sobre **D1+D3** + importancias RF (top-N ~importancia acumulada), evaluado con/sin.
6. **Umbral de anomalías**: percentil (p95) sobre el 20% de D1 reservado como validación, **igual para los 4** algoritmos. Nunca ajustar mirando D2.
7. **Híbrido**: cascada **anomalía → firmas**, con clase "desconocido/0-day" por baja confianza (`predict_proba` < umbral).
8. **Bug one-hot** (vocabulario = unión D1+D3): arreglar antes de entrenar (Paso 0). → hecho 2026-07-05.
9. **Código**: 3 scripts nuevos (`anomalias.py`, `firmas.py`, `hibrido.py`) + `evaluacion.py` común; grids pequeños + CV; `random_state=42` en todo. `evaluacion.py` se implementa **antes** que `anomalias.py`.
10. **Memoria**: Word + Zotero (IEEE); teoría NSL-KDD va a 4.2; orden de trabajo: **código primero, informe detrás**.

---

## Estado real reconciliado (verificado en código/disco 2026-07-06)

La prosa de `next-steps.md §3.1-E/§3.2/§5` iba por detrás del código. Estado real:

- **Selección de características: 122 → 54 features** (no 40). El default en `program.py`
  es `importancia_acumulada=0.999` (99.9%), no 99%. CSVs D1/D2/D3 regenerados a 54
  columnas (`selected_features.txt` con fecha 2026-07-05 19:53).
- **H1 (auditoría 4.3.5)**: la **Opción 1 ya está ejecutada** (umbral 99.9% → 54 features,
  recupera indicadores 0-day: `num_failed_logins`, `flag_REJ`, `flag_SH`, `num_shells`…).
  Falta solo la **validación con datos** (ver decisión del 2026-07-06 abajo).
- **H2**: resuelto — `program.py::_resolver_representante_conservado()` sigue la cadena
  greedy de correlación; el reporte ya no afirma en falso qué feature "se conservó".
- **H3**: resuelto — CLI `argparse` con `--sin-seleccion` + sufijo `_sin_seleccion` en
  todos los artefactos; las variantes con y sin selección coexisten sin pisarse.

> Bookkeeping cerrado (2026-07-14): la prosa de `next-steps.md` ya está reconciliada
> (H1-Opción1/H2/H3 marcados ☑ en §3.2, 40→54 propagado en todo el documento).

---

## Decisión del 2026-07-06

### Q1 — ¿mismo set de features para anomalías y firmas? → **Opción C**

**Contexto.** La selección de 54 features es **supervisada** (importancias de RF sobre
D1+D3 con `y_category`, 5 clases). Está alineada con **firmas** (clasificador multiclase
supervisado), pero el detector de **anomalías** se entrena **no supervisado y solo con D1
(normal)**. Un ranking supervisado D1+D3 favorece las features que separan normal-vs-ataque
y puede descartar features casi constantes en tráfico normal que serían la única señal de
un **0-day**. Forzar las mismas 54 al detector de anomalías puede degradar su recall 0-day
— precisamente el riesgo que señaló H1.

**Decisión: C — no fijar el set a ciegas; parametrizar y dejar que el experimento H1 lo resuelva con datos.**

- `anomalias.py`, `firmas.py` e `hibrido.py` **cargan el set de features vía parámetro/ruta**,
  no hardcodeado. Deben poder correr sobre la variante de 54 (`specialized_nsl_kdd_*`) y
  sobre la de 122 (`specialized_nsl_kdd_sin_seleccion_*`, ya generable con `--sin-seleccion`).
- El **experimento con/sin selección** (que ya se debe a la memoria para cerrar 4.3.5) **ES**
  la decisión. Métrica de decisión: **recall 0-day por tipo de ataque** (los ~17 tipos de D2
  ausentes del train) + **F1 macro**, no solo F1 global.
- Se ejecuta cuando existan los baselines mínimos (IsolationForest para anomalías, RandomForest
  para firmas). Comparar **54 vs 122** (40 queda descartado: ya no existe en disco).

**Resultados esperables y qué implican:**
- Si 54 no daña el recall 0-day → **A** de facto (mismo set 54 para ambos): simple y comparable.
- Si 54 daña el recall 0-day del detector de anomalías → **B**: firmas sobre 54, anomalías
  sobre 122 (o filtro no supervisado varianza/correlación sobre D1). Es el resultado probable.

**Consecuencia inmediata para la implementación:** los scripts deben aceptar el `base_path`
de los CSVs como argumento, de modo que cambiar 54↔122 sea un flag, no una reescritura.

### Q2 — rutas y configuración → **`config.py` compartido (acotado)**

- Se crea `Implementacion/app/config.py` con: `RANDOM_STATE=42`, `RESULTADOS_DIR`,
  `FIGURAS_DIR`, `MODELOS_DIR`, los dos `base_path` (54 = `specialized_nsl_kdd`,
  122 = `specialized_nsl_kdd_sin_seleccion`) y las convenciones de clase (ver Q3).
- Lo consumen los **scripts nuevos** (`evaluacion.py`, `anomalias.py`, `firmas.py`,
  `hibrido.py`). `program.py`/`validacion.py` **no se refactorizan ahora** (funcionan y
  están APROBADOS); solo migran sus rutas a `config.py` si en algún momento se tocan.
- Cierra la deuda 3.2 🟠 de rutas hardcodeadas para el código nuevo.

### Q3 — superficie de `evaluacion.py` → **§6.5b + `evaluar_0day_por_tipo` + convenciones**

- Funciones de §6.5b (`evaluar_binario`, `evaluar_multiclase`, `plot_matriz_confusion`,
  `plot_roc_pr`, `guardar_metricas`) **+ `evaluar_0day_por_tipo(y_tipo_real, es_sospechoso,
  tipos_0day) → {tipo: recall}`** (la usan el experimento H1 y `hibrido.py`; evita duplicar).
- Convenciones fijadas en `config.py`: **positivo = ataque = 1**, `normal = 0`; orden
  multiclase `['normal','dos','probe','r2l','u2r','unknown']` (unknown solo en híbrido).
- Fuera de alcance (evitar sobre-ingeniería): intervalos de confianza por bootstrap,
  calibración de probabilidades más allá del umbral del híbrido, logging estructurado.

### Q4 — calibración de `UMBRAL_CONF` del híbrido → **`cross_val_predict` OOF, sin leakage**

- El `UMBRAL_CONF` (marca "unknown/0-day" si `predict_proba` máx < umbral) se calibra sobre
  probabilidades **out-of-fold** del mismo `StratifiedKFold(5)` de `firmas.py`
  (`cross_val_predict`), NO sobre el D3 con el que se entrenó (sería in-sample → leakage) ni
  sobre un holdout (sacrificaría las ~52 muestras de u2r). El modelo final se re-entrena en
  todo D3 tras calibrar.
- Explorar `UMBRAL_CONF ∈ {0.4, 0.5, 0.6}`; elegir el que preserve el recall macro de las
  clases conocidas. Los 0-day no están en D3: su detección se **mide** en D2 (etapa 1
  anomalías), no se optimiza aquí.

### Q5 — `imbalanced-learn` y pinning → **instalar compatible con sklearn 1.7.1, con regla de parada**

- `requirements.txt` **ya está pinneado** (sklearn==1.7.1, numpy==2.3.2…): la parte de
  pinning de la deuda 3.3 está hecha.
- Instalar `imbalanced-learn` en una versión **compatible con sklearn 1.7.1 sin mover
  sklearn** y añadirlo a `requirements.txt`. **Regla de parada:** si el resolvedor de pip
  exige cambiar sklearn, NO instalar y consultar — cambiar sklearn invalidaría la
  reproducibilidad de las 54 features (importancias RF sensibles a versión).

### Q6 — ejes experimentales → **no cruzar**

- **Balanceo** (4 algoritmos × 2 esquemas; el eje comparado **depende del algoritmo**: SMOTE vs
  `class_weight` en DecisionTree y RandomForest, SMOTE vs **nada** en KNN e HistGradientBoosting,
  que no admiten `class_weight` en sklearn — `firmas.py:91-96`) **no se cruza con el grid de
  hiperparámetros**: se mide con un hiperparámetro por defecto y su ganador entra al GridSearch
  (`firmas.py:248-256`). **Corregido el 2026-08-13:** se corre **dentro de cada corrida de
  `firmas.py`, en las dos variantes** — no solo sobre el set **54**, como decía antes este bullet.
  Verificado contra disco: `firmas.py:559` llama a `_experimento_balanceo()` **sin condicional de
  variante**, `Resultados/metricas_balanceo.csv` trae **16 filas = 8 por variante** (`54` y
  `122_sin_seleccion`) y `config.ALCANCE_BALANCEO` (`config.py:463-468`) es **agnóstico a la
  variante**. `PIPELINE.md:1544` ya lo decía. **Esto corrige una descripción, no reabre Q6:** lo
  vigente de Q6 —que el balanceo no se cruza con el grid ni con el eje de selección— sigue intacto.
- **Selección** (54 vs 122, H1) se corre una vez con el baseline de cada modelo
  (IsolationForest / RandomForest) y el balanceo ya fijado, midiendo recall 0-day por tipo
  + F1 macro.
- Comparativa principal de los 4 algoritmos (5.1/5.2): sobre **54 + mejor balanceo por
  algoritmo**. Cada experimento aísla una variable (defendible en la memoria).

---

## Decisión del 2026-07-11

### 3.1-F — Baseline RF monolítico → **APROBADO. Ubicación: `baseline.py` aparte**

**Contexto.** El profesor de seguimiento observó que "todo el mundo acaba en un Random
Forest para este dataset". El patrón dominante en la literatura NSL-KDD (~99% en el split
de train) es un **único clasificador supervisado sobre TODO el train** (normal + 4 ataques),
evaluado sobre todo el test. Ese RF monolítico **no existía**: el RF del proyecto vive como
clasificador de firmas (entrenado solo con D3, 4 clases de ataque) y como motor de la
selección 4.3.5, nunca como clasificador global de las 5 clases.

**Decisión: SÍ añadirlo como baseline de control** (no como arquitectura del sistema). Es el
número que el tribunal espera y la única forma de responder "¿para qué el híbrido si un RF da
~99%?". La respuesta —y la tesis del TFG— es el **0-day**: un RF supervisado no puede detectar
los ~17 tipos de ataque ausentes del train; la etapa de anomalías sí. Ese contraste **es** la
justificación del híbrido.

**Ubicación: `baseline.py` aparte** (no un modo de `firmas.py`). Razón: es un experimento
distinto en las tres dimensiones —train = **D1+D3** (5 clases, incluye `normal`) vs D3 (4
clases de ataque) de firmas; evaluación = **D2 completo** vs D2 filtrado a tipos conocidos de
firmas—. Meterlo como flag en `firmas.py` mezclaría dos conjuntos de entrenamiento, dos sets
de etiquetas y dos sets de evaluación en un script cuya responsabilidad hoy es única. Un
script propio respeta la estructura D') "un-concern-por-script" y reutiliza `evaluacion.py` /
`config.py` sin tocar lo aprobado.

**Especificación de `baseline.py`:**
- Train: `X = concat(D1.X, D3.X)`, `y = category` (5 clases: `normal`+dos/probe/r2l/u2r).
- Modelo: `RandomForestClassifier(class_weight='balanced', random_state=42)` con
  `GridSearchCV(StratifiedKFold(5), f1_macro)` sobre el mismo grid RF pequeño de firmas
  (`n_estimators∈{100,300}` × `max_depth∈{10,None}`). No se cruza con el eje de balanceo
  (Q6): `class_weight='balanced'` fijo, como en la selección 4.3.5.
- Evaluación sobre **D2 completo**: multiclase 5 clases (`evaluar_multiclase`), binaria
  normal-vs-ataque (`evaluar_binario` con `y_score = 1 − P(normal)` para AUC), y **recall
  0-day por tipo** (`evaluar_0day_por_tipo`, `es_sospechoso = pred != 'normal'`).
- Parametrizable 54↔122 (Q1/C, flag `--sin-seleccion`).
- Artefactos: `Resultados\metricas_baseline.csv`, `Resultados\metricas_baseline_0day.csv`,
  `modelos\baseline_rf_<set>.joblib`, `figuras\baseline_cm_<set>.png`. Idempotencia por
  variante (misma lógica `_limpiar_variante_csv` que anomalias/firmas).

**Métrica de decisión frente al híbrido:** **recall 0-day por tipo** (misma tabla que el
experimento H1). La hipótesis a contrastar con datos: el recall 0-day del RF monolítico es
sensiblemente inferior al de la etapa de anomalías del híbrido.

---

## Decisiones del 2026-07-14 — hibrido.py (grill previo a implementar)

### H-1 — Origen de los modelos de las dos etapas → **A: cargar joblib + reconstruir solo para OOF**

**Contexto.** `hibrido.py` necesita el mejor detector de anomalías (etapa 1) y el mejor
clasificador de firmas (etapa 2). Ambos ya existen persistidos y auditados
(`anomalia_*_<set>.joblib`, `firma_*_<set>.joblib`, con modelo + umbral/config). Además,
calibrar `UMBRAL_CONF` exige probabilidades **out-of-fold** de firmas (Q4, sin leakage), que
NO se pueden obtener del modelo ya re-ajustado en todo D3.

**Decisión: A.**
- **Cascada final sobre D2:** cargar los `.joblib` persistidos (no re-entrenar). Una sola
  fuente de verdad; las métricas del híbrido cuadran con las de 5.1/5.2 ya reportadas.
- **Calibración de `UMBRAL_CONF`:** reconstruir el estimador de firmas desde su config
  guardada (`algoritmo` + `balanceo` + `config_ganadora`) y correr
  `cross_val_predict(method='predict_proba')` sobre D3 con el mismo `StratifiedKFold(5)`
  de `firmas.py`. El umbral se elige sobre esas probas OOF, **nunca sobre D2** (Q4).
- **Descartada C** (calibrar sobre probas in-sample del modelo refit): es leakage, viola Q4.
- **Descartada B** (re-entrenar todo en `hibrido.py`): duplica trabajo auditado y arriesga
  divergencia con los modelos que ya alimentan la memoria.

**Consecuencia de implementación:** para reconstruir el estimador de firmas idéntico,
`hibrido.py` reutiliza los builders de `firmas.NSLKDDSignatureTrainer` (`_estimador_para` +
`set_params`), no reimplementa la lógica de balanceo/pipeline.

### H-2 — Detector de la etapa 1 y reconciliación de Q6 (H1) → **Autoencoder por defecto + tabla 0-day de los 4**

**Contexto.** Tensión entre dos decisiones ya tomadas: 5.3 pide el **mejor** detector (por
AUC-ROC/F1 en 54 y 122 gana el **Autoencoder**, IsolationForest pegado detrás), mientras que
Q6 fijó el experimento **H1** (54 vs 122) sobre el **baseline IsolationForest**. Dato que
resuelve la tensión: el **recall 0-day por tipo depende SOLO del detector y su umbral**
(`es_sospechoso = score > umbral`), no de la etapa de firmas.

**Decisión:**
- **Cascada (5.3):** detector **seleccionable** por flag `--detector` (IF/OCSVM/LOF/Autoencoder),
  **por defecto Autoencoder** (el mejor; el que va a 5.3).
- **Detector FIJO entre 54 y 122** al comparar H1: no puede variar por variante o confunde el
  efecto del set de features.
- **Reconciliación de Q6:** `hibrido.py` calcula `evaluar_0day_por_tipo` **para los 4
  detectores** (carga cada `anomalia_*_<set>.joblib`, aplica su umbral guardado a las filas
  0-day de D2). Coste casi nulo y H1 deja de depender de elegir IF vs AE: se ve el recall
  0-day de los 4 en ambas variantes. **Q6 queda matizada**: H1 ya no es "solo IsolationForest"
  sino los 4 detectores, con el AE conduciendo la cascada.

### H-3 — Clasificador de la etapa 2 (firmas) → **RandomForest, seleccionable, fijo entre variantes**

**Contexto.** La etapa 2 asigna categoría y de su `predict_proba` sale la señal que dispara
`UMBRAL_CONF`. En 54 gana **RandomForest** (f1_macro D2 = 0.822, el sistema elegido); en 122
gana KNN (0.753, RF cae a 0.696).

**Decisión: RandomForest**, seleccionable por flag `--firma`, **fijo entre 54 y 122** (misma
razón que H-2: no confundir el efecto del set de features en H1). Doble justificación:
1. Es el mejor en el set primario (54), que es el sistema del TFG.
2. Su `predict_proba` es **suave** (media sobre 100-300 árboles) → una `UMBRAL_CONF` sobre él
   discrimina confianza de forma fina. KNN (k=3/5) y DecisionTree dan probabilidades
   **escalonadas** (pocos valores distintos), lo que haría que 0.4/0.5/0.6 se comporten de
   forma tosca. Para el mecanismo "unknown por baja confianza", RF es el técnicamente
   apropiado, no solo el más preciso.

**Nota sobre el comentario del profesor** ("todo el mundo cae en RF"): el RF monolítico que
usa la literatura ES `baseline.py`, y ya se demostró que colapsa (recall 0-day 0.15). El RF de
firmas es una pieza de la etapa 2; la aportación del TFG es la **cascada + detección 0-day**,
no el algoritmo. Las vías para diferenciarse más se acumulan en `EL_FUTURO.md` (creado hoy).

### H-4 — Criterio de calibración de `UMBRAL_CONF` → **presupuesto τ=2pp sobre OOF + tabla de sensibilidad en D2**

**Contexto.** Q4 fijó los datos (probas OOF de D3 vía `cross_val_predict`, nunca D2) y el rango
(`UMBRAL_CONF ∈ {0.4, 0.5, 0.6}`), pero dejó abierto el criterio ("preservar el recall macro de
las clases conocidas"). Al implementarlo aparece una trampa: **en D3 no hay 0-day** (todos los
ataques son conocidos), así que subir el umbral solo puede **bajar** el recall macro OOF de forma
monótona (muestras conocidas de baja confianza pasan a `unknown`). "Maximizar recall macro OOF"
elegiría trivialmente 0.4. El umbral **no se puede optimizar en D3**; el beneficio real (cazar
0-day) solo se **mide** en D2.

**Decisión:**
1. **Regla de selección (criterio de presupuesto):** elegir el `UMBRAL_CONF` **más alto** de
   `{0.4, 0.5, 0.6}` cuyo recall macro OOF de las 4 clases conocidas **no caiga más de τ = 2 pp**
   respecto al baseline sin umbral. Coge el umbral más agresivo que apenas cuesta recall en
   conocidas; el pago en 0-day se mide luego en D2 (Q4). `τ` queda como **constante configurable**
   en el script (reproducible, ajustable sin reescribir). No hay τ "óptimo" objetivo: es un juicio
   de valor (cuánto recall conocido se sacrifica por sensibilidad 0-day); 2 pp = sacrificio pequeño.
2. **Reporte (análisis de sensibilidad):** persistir una tabla con los **tres** umbrales, cada uno
   con sus métricas **OOF** (recall_macro conocidas, tasa de falsos-unknown) **y** sus métricas
   **D2** (f1_macro multiclase, recall 0-day…). El elegido por τ=2pp va marcado. Coste casi nulo
   (3 evaluaciones) y muestra si el sistema es robusto o frágil al umbral. Con esta tabla el valor
   exacto de τ deja de ser crítico.
3. **Línea roja (invalida el TFG si se cruza):** el umbral se **selecciona** por la regla de
   presupuesto sobre OOF de D3; D2 se usa **solo para reportar**, jamás para elegir el umbral.
   Escoger el umbral por su resultado en D2 sería leakage y rompería Q4.
4. `predict_proba` = del estimador RF reconstruido (H-1); confianza = `max` sobre las 4 clases.

### H-5 — Evaluación binaria del híbrido → **idéntica a la etapa 1 por construcción; la tesis se juega vs baseline monolítico**

**Contexto.** `§6.5` pide comparar la binaria (normal vs ataque) del sistema completo contra el
detector de anomalías solo ("¿aporta la cascada?"). En una cascada **pura** anomalía→firmas la
respuesta es trivial y hay que asumirla: la binaria del híbrido **coincide exactamente** con la
de la etapa 1. Razón: la etapa 1 decide sospechoso vs normal; la etapa 2 solo **sub-clasifica**
los sospechosos en dos/probe/r2l/u2r/**unknown** (todas "ataque"), se entrena solo con D3 y **no
tiene clase 'normal'**, así que nunca devuelve un sospechoso a normal. El `unknown` sigue siendo
positivo. ⇒ La decisión binaria la toma entera la etapa 1; la cascada no aporta nada binario.

**Decisión (presentación de 5.3 e implementación):**
1. Reportar la binaria del híbrido **declarando explícitamente** que coincide con la etapa 1 por
   construcción (con la justificación de arriba). No duplicar una "tabla binaria del híbrido" con
   números iguales sin explicarlo: parecería datos duplicados ante el tribunal.
2. La aportación real de la cascada se sitúa donde está: **(a)** convertir "sospechoso" en una
   **categoría accionable**, y **(b)** separar ataques de categoría conocida de los **unknown/0-day**.
3. **La comparación central de 5.3 NO es "cascada vs anomalía-sola binaria"** (empate por
   construcción), sino **híbrido vs RF monolítico (`baseline.py`)**: ahí el híbrido gana en 0-day
   y en no ahogar r2l/u2r. Esa es la tesis.
4. **Implementación:** la "binaria del híbrido" reutiliza directamente el `es_sospechoso` de la
   etapa 1 (no se recalcula por otra vía).

### H-6 — Scoring de la evaluación multiclase del híbrido → **matriz 5×6 + métricas por alcance, sin número único**

**Contexto.** El híbrido evalúa **todo D2** (22.544). Etiquetas reales = 5 (normal, dos, probe,
r2l, u2r); predicciones posibles = **6** (las 5 + `unknown`). Un 0-day (p. ej. `apache2`) tiene
categoría real = dos, pero lo **deseable** es que el sistema lo marque `unknown`, no que le aplique
la firma de dos. Cualquier "accuracy/f1 a 5 clases" único miente: si `unknown` cuenta como fallo,
castiga el enrutado correcto de un 0-day; si se mapea `unknown` a su categoría real, premia
mal-etiquetar un ataque nuevo como firma conocida.

**Decisión:**
1. **Artefacto primario:** matriz de confusión filas = {normal, dos, probe, r2l, u2r} × columnas =
   {normal, dos, probe, r2l, u2r, **unknown**}, sobre todo D2. Descriptiva, sin ambigüedad.
2. **Métricas resumen, cada una con su alcance declarado** (no un número global engañoso):
   - **Binaria** (etapa 1, ver H-5).
   - **Por categoría conocida:** recall/precision de la cascada end-to-end sobre ataques de tipo
     conocido (mide el coste de añadir el filtro de anomalías frente a firmas-solo de 5.2).
   - **0-day (titular):** (i) recall de "marcado sospechoso" por tipo (`evaluar_0day_por_tipo`);
     (ii) de los detectados, % enrutados a `unknown` vs mal-etiquetados como categoría conocida.
3. **Comparación vs `baseline.py` (la tesis):** sobre la métrica comparable y para la que se diseñó
   el híbrido: **recall 0-day por tipo** (baseline: `pred≠normal`; híbrido: sospechoso en etapa 1).
   Además, f1_macro a 5 clases de ambos **con la advertencia** de que en el híbrido los `unknown`
   cuentan como error (conservador: infravalora al híbrido y aun así la tesis se sostiene por el 0-day).
4. **Evitar explícitamente** un "f1_macro global a 5 clases" como titular del híbrido, justificando
   en la memoria por qué (castigaría el enrutado correcto a `unknown` o premiaría el mal-etiquetado).

### H-7 — Artefactos, CLI e idempotencia de `hibrido.py` → **mismo patrón auditado que anomalias/firmas/baseline**

**Decisión: replicar el patrón "un concern por script" ya auditado.**
- **CLI:** `--sin-seleccion` (54↔122, Q1/C) · `--detector {IsolationForest,OneClassSVM,
  LocalOutlierFactor,Autoencoder}` (default Autoencoder, H-2) · `--firma {DecisionTree,
  RandomForest,KNN,HistGradientBoosting}` (default RandomForest, H-3). `τ` = constante del
  módulo (H-4).
- **Idempotencia por variante:** mismo `_limpiar_variante_csv` (borra las filas de `set_features`
  de esta corrida, conserva la otra).
- **Artefactos en `Resultados\`:**
  - `metricas_hibrido.csv` — una fila por corrida (set, detector, firma, `umbral_conf` elegido,
    binaria, por-categoría-conocida, f1_macro-5clases-conservador).
  - `metricas_hibrido_0day.csv` — recall 0-day **por tipo** del detector de la cascada **+ de los
    4 detectores** (H-2), para cerrar H1.
  - `metricas_hibrido_calibracion.csv` — tabla de sensibilidad de los 3 umbrales (OOF + D2, H-4).
  - `figuras\hibrido_cm_<set>.png` — matriz 5×6 (H-6).
  - `modelos\hibrido_<set>.joblib` — **descriptor** reproducible: qué joblibs de detector/firma
    usa + `umbral_conf` elegido + τ + rutas. NO re-serializa los modelos (ya existen); guarda las
    referencias y la decisión.

---

## Pendientes de diseño de `hibrido.py` — RATIFICADOS 2026-07-14 (antes de escribir código)

Los cinco puntos que quedaron abiertos al cerrar el grill (los 3 menores + las 2 preguntas
de implementación) se ratifican así antes de teclear. Todos son consistentes con decisiones
previas; ninguno cambia H-1…H-7, solo los concreta.

- **P-1 · Alcance de H1 (54 vs 122) → una variante por invocación.** `hibrido.py` corre **una
  variante por invocación** (`--sin-seleccion` o no), como anomalias/firmas/baseline. El
  experimento H1 = correrlo dos veces; la comparación 54-vs-122 se **lee** de
  `metricas_hibrido_0day.csv` (acumula ambas variantes por idempotencia `_limpiar_variante_csv`),
  sin script aparte. Mantiene "un concern por script".
- **P-2 · Caveat de FPR en la comparación 0-day → reportar FPR junto al recall 0-day.** El recall
  0-day del híbrido y el del baseline se miden a **FPR distinto** (etapa 1 ≈ 8-10% FPR por el
  umbral p95 + drift; baseline RF ≈ 2.7%). Parte de la ventaja 0-day del híbrido es que alarma
  más. **Cada fila de `metricas_hibrido_0day.csv` lleva el FPR binario del detector** junto al
  recall por tipo; no se vende el recall 0-day aislado.
- **P-3 · Datos que carga → solo D2 y D3.** D2 (evaluación) y D3 (OOF de calibración). **D1 NO se
  carga**: el modelo de anomalías y su umbral llegan ya entrenados desde el joblib (confirmado
  contra `anomalias.py::_persistir` — el joblib guarda modelo + umbral + config).
- **P-4 · Línea roja anti-leakage de H-4 → separación estructural, no disciplina.** La función de
  calibración de `UMBRAL_CONF` recibe **solo D3** (X, y) y el estimador reconstruido; **NO recibe
  D2 en su firma**. La evaluación sobre D2 es una fase posterior e independiente, invocada
  después de fijar el umbral. Así el leakage del criterio de selección (elegir umbral mirando D2)
  es estructuralmente imposible, no depende de recordar la regla.
- **P-5 · Binaria del híbrido (H-5) → reutilizar `es_sospechoso`, sin veto de la etapa 2.** La
  binaria del híbrido **es** `es_sospechoso` de la etapa 1, reutilizado tal cual (no se recalcula
  por otra vía). La etapa 2 solo sub-clasifica sospechosos; al no tener clase `normal` no puede
  devolver un sospechoso a normal ⇒ no veta a la etapa 1. Se reporta declarando la igualdad por
  construcción (H-5).

**Consecuencia de implementación (reconstrucción fiel):** `hibrido.py` NO reimplementa scoring ni
builders. Reutiliza `NSLKDDAnomalyTrainer._score(algo, model, X)` para el anomaly score de la
etapa 1 y `NSLKDDSignatureTrainer._estimador_para(algo, balanceo) + set_params(**config_ganadora)`
para reconstruir el estimador de firmas del OOF. Verificado contra el código: `config_ganadora`
persistido por `firmas.py` ya lleva el prefijo `clf__` cuando el balanceo ganador es SMOTE, de modo
que `set_params` sobre el `ImbPipeline` funciona sin traducción.

---

## Decisión del 2026-07-15 — Q1/C resuelta por el experimento H1 → **54 features (opción A)**

**Contexto.** Q1/C dejó el set de features (54 vs 122) parametrizable y delegó la decisión al
experimento H1, con métrica **recall 0-day por tipo + f1_macro**. `hibrido.py` ejecutado en ambas
variantes (2026-07-15) produce por fin los dos lados de la tabla.

**Datos (cascada Autoencoder→RandomForest, `UMBRAL_CONF=0.5`):**

| Métrica | 54 | 122 |
|---|---|---|
| Recall 0-day global (detector) | 0.771 | 0.785 |
| FPR binaria | 0.102 | 0.085 |
| Detector AUC-ROC | 0.929 | 0.947 |
| **`conocida f1_macro` (end-to-end, n=9083)** | **0.748** | 0.655 |
| f1_macro 5 clases (conservador) | 0.641 | 0.583 |

**Decisión: A — 54 features para AMBAS etapas.** Confirmada por el desglose por tipo (no solo el
global). **[FE DE ERRATAS 2026-07-16, detectada por auditoría del volcado a la memoria]** La
redacción original de este párrafo afirmaba que "las 122 no recuperan ningún tipo que las 54
pongan a cero" y que "`mailbomb` lo fallan ambos"; `metricas_hibrido_0day.csv` la desmiente.
Lectura correcta del CSV (Autoencoder, cascada): el delta global es **+55 detecciones**
(2.890 → 2.945 de 3.750), del que **36 provienen de `mailbomb`** — las 122 SÍ lo sacan de cero
(recall 0.00 → 0.123), aunque sigue esencialmente fallado (36/293) — y **20 de `mscan`**
(0.98 → 1.00, ya casi saturado); el resto neto ≈ 0 (retrocesos en `sendmail` y `snmpguess`).
**La decisión NO cambia**: se sostiene en la etapa 2, no en el 0-day. La diferencia decisiva es
que las 122 degradan la firma ~9 pp (`conocida f1_macro` 0.655 vs 0.748) por sobreajuste de RF a
los dummies extra de D3, y la tesis ya está ganada ~5× sobre el baseline a 54 (0.771 vs 0.150).
El matiz de `mailbomb` refuerza además la opción B (sets por etapa) como línea futura y la
complementariedad de detectores (LOF lo caza a 0.82 sobre 54). **Cierra la casilla 4.3.5.**

**A reportar en la memoria (honestidad, no esconder):** las 122 dan un detector marginalmente
mejor en la tarea pura de anomalías (Pareto en recall/FPR, +AUC), confirmando el riesgo que motivó
Q1/C —la selección supervisada ciega un poco al detector no supervisado—, pero el efecto es pequeño
y 54 gana el sistema. La **opción B** (122 anomalías / 54 firmas) queda como línea futura en
`EL_FUTURO.md §3`.

**Hallazgos colaterales del experimento (más relevantes que 54-vs-122; a 5.3 + `EL_FUTURO.md`):**
1. **Complementariedad de detectores:** ningún detector domina por tipo. Sobre 54, el AE (elegido)
   es ciego a `mailbomb` (0.00, que LOF caza a 0.82) y a `snmpguess` (0.02, que IF caza a 0.74).
   → ensemble de detectores = línea futura nº1.
2. **`snmpgetattack` (n=178):** punto ciego de los 4 detectores en ambos sets → límite de las
   features por-flujo de NSL-KDD, no de los modelos.
3. **`UMBRAL_CONF`:** solo el 13.4% de los 0-day cazados se enrutan a `unknown` (RF sobre-confiado
   OOD) → open-set recognition, línea futura.

**Aclaración (nivel de firmas):** en 54 la firma NO "funciona mal" — RF solo da f1_macro **0.822**
(5.2). El punto débil real es **u2r** (37 muestras en D2, f1 0.17–0.45) y algo r2l; `dos`/`probe`
van muy bien. La caída 0.822→0.748 al entrar en la cascada es el **coste del filtro de anomalías**
(ataques conocidos marcados normal o enrutados a unknown), no un fallo del clasificador.

---

## Decisiones del 2026-07-21 (grill de redacción del vault)

Decisiones tomadas durante la sesión de redacción del 2026-07-21. Ninguna afecta al código
ni a las cifras; fijan convenciones de redacción y un ajuste del reparto de teoría.

### Reparto de 4.2 (opción 1) → la teoría del dataset la redacta Claude como borrador factual

La teoría del apartado **4.2** (origen del dataset, las 41 features, por qué NSL-KDD), antes
reservada a Francisco en el reparto de redacción (acuerdo 2026-07-15), se **cede a Claude** para
su redacción como **borrador factual** con marcadores `[CITA:...]` pendientes. Reparto resultante:
- «Origen» y «Las 41 características y sus 3 grupos» → borrador de Claude (hechos verificables).
- «Por qué se eligió NSL-KDD» → borrador provisional que **Francisco revisa** (refleja el criterio
  del autor).
- Las citas `[CITA:...]` las **resuelve Francisco en Zotero**.

La casilla §2.2 «Teoría del dataset NSL-KDD» de `next-steps.md` pasa de `☐` (Francisco) a `◐`
(borrador Claude 2026-07-21): no se cierra hasta resolver citas y la revisión del bloque «por qué».
(Registro del 2026-07-21, anterior al congelado de `next-steps.md` del 2026-08-01; el estado vivo
está en `features.md`.)

### Convención de código incrustado en la memoria

Se incrustan **fragmentos de código inline**, en la sección que ilustran, **verbatim recortado**:
código real con elisiones `# ...`, **no pseudocódigo**. Regla asociada: los **comentarios del
código fuente que contradigan la prosa** (p. ej. "no supervisado" en `anomalias.py`) se **recortan**
del fragmento mostrado, para no reintroducir por la puerta de atrás terminología que la memoria ha
unificado. Aplicada en 4.3.1-4.3.5, 4.4 y 4.5 (7 fragmentos).

### Terminología del detector de anomalías → "semisupervisado (one-class)" como término canónico

- Término **canónico** del detector de anomalías = **"semisupervisado (one-class)"**.
- "No supervisado" se admite como **sinónimo declarado una sola vez** (en 3.4.1), reconociendo que
  la literatura y `scikit-learn` lo usan indistintamente.
- **Consecuencia pendiente (no resuelta, territorio de Francisco):** `2.2.4` del Marco Teórico aún
  dice "detectores no supervisados" → queda como divergencia a corregir por Francisco al redactar
  la teoría en prosa.

---

## Decisiones del 2026-08-06 (grill de los cuatro informes del `researcher`)

Cerradas en el `grill-me` de 13 preguntas del **2026-08-06**, que convirtió los cuatro informes de
`Obsidian_TFG_Vault/99 Investigación/` en las 18 fichas T0-T17 de `features.md`. Registradas aquí el
**2026-08-09** (volcado parcial de T17: falta el bloque «Decisiones tomadas a partir de este informe»
en los cuatro informes y la deriva de documentación de `evaluacion.py`).

### Criterio rector del lote → **refinar el proyecto o enseñar el límite; nunca sucedáneos**

Nada que no refine el proyecto o no ayude al lector a ver que **con NSL-KDD se hizo todo lo
posible**. Las imposibilidades se **declaran con su razón técnica**: no se omiten ni se sustituyen
por sucedáneos sintéticos. Y el dataset tiene **argumento positivo propio** (Goldschmidt y Chudá:
solo el 23 % de los datasets NIDS trae partición train/test predefinida, 16 % desde 2020, y su
ausencia es «*prone to biased evaluations and selective reporting*»; NSL-KDD sí la trae y este TFG la
respeta). Ese argumento va **antes** de cualquier límite.

### Decisión marco (a) — **se REABRE el track de código**, de forma declarada y acotada

**Contexto.** El track de código se dio por cerrado el **2026-07-16**. Los cuatro informes dejaron
dos motivos que no se pueden despachar con redacción: (1) la auditoría C1-C7 del protocolo de
evaluación **no se cumplía en C3 ni en C6** —`accuracy_D2` era una columna homónima con dos alcances
distintos: 0,9683 en firmas y 0,7395 en baseline—; y (2) **dos decisiones ya cerradas descansaban en
huecos de 1-2 pp medidos con n=1** (RandomForest 0,822 vs HistGradientBoosting 0,804 en firmas;
Autoencoder 0,8605 vs IsolationForest 0,8257 en anomalías).

**Decisión: reabrir, con el alcance exacto de la spec y nada más.**
- **Nivel 1 — esquema de métricas** (T1): **no mueve ningún número publicado** de calidad.
- **Nivel 2 acotado — 10 semillas** (T4): **los titulares de 5.1-5.3 siguen siendo los de la semilla
  42**; la dispersión entra como tabla nueva en `A.3` más un párrafo en `5.4`. **No se reescribe el
  capítulo.**
- **Dos mediciones baratas**: KS de D1 contra las 9.711 filas normales de D2 (T2) y medición de la
  cascada invertida sobre modelos ya persistidos (T3).
- **Todo pasa por `auditor-ml`.** Nada más entra en la reapertura.

### Decisión marco (b) — **se retira la regla «lo escribe Francisco», en dos velocidades**

- **`2.x` — retirada completa:** `redactor-tfg` redacta la prosa desde los guiones ya existentes.
- **`6.2 Líneas futuras` — borrador de agente con revisión final de Francisco.** Es el sitio natural
  del material de Nested Learning, y bloqueada dejaba a medias un entregable del encargo.
- **La bibliografía final en Zotero/IEEE sigue siendo de Francisco** (trabajo mecánico en su máquina).

> **Ejecución pendiente en T0**, con un choque abierto: `2.1.4` no figura en las ubicaciones de T0 ni
> en la sección «Fuera de la lista operativa» de `features.md`, pero la «Restricción dura» de T25 sí
> se la reserva a Francisco. **T0 y T25 son la misma pregunta; la decide Francisco al cerrar T0.**

### Renuncia declarada al p-valor sobre las 10 semillas

**Sin p-valor**, con la renuncia **declarada y su razón: 10 puntos sobre un único dataset no
sostienen un contraste.** Declarar la renuncia **cumple** el ítem *statistics* del checklist de
Pineau et al.; callarla no. Si los intervalos de RandomForest/HistGradientBoosting o de
Autoencoder/IsolationForest se solapan, **se dice y no se establece el orden** — eso es un hallazgo
para `5.4`, no un desastre.

---

## Decisiones del 2026-08-09

### T18 — **el CSV publica solo lo estable; los números viven en `PIPELINE.md` anclados a commits**

Conclusión de diseño del rediseño de `alcance_tiempo_s`. `metricas_*.csv` publica únicamente lo
**estable** —qué tramos de tiempo entran, cuáles no y el aviso de P9—, y **todos los números** de
reparto viven en `PIPELINE.md`, **anclados a commits de git** y editables sin re-correr. Las dos
frases empíricas que el CSV llegó a publicar en 8/8 y 8/8 filas —«las desviaciones observadas caben
dentro de la dispersión entre corridas» y «un tramo de coste casi FIJO que no escala con el
modelo»— salen a **0/8 y 0/8**. Corrida final `1163c90`, 222 filas, `semilla = 42`, deriva de calidad
cero contra nueve anclas externas. Dictamen de `auditor-ml`: APTO.

### T22 — **`n_iter_total_grid` es determinista: la dispersión de wall-clock es carga de máquina**

Cerrada **con la conclusión invertida** respecto a lo que la ficha planteaba. `n_iter_total_grid`
queda registrado por fila y resulta **determinista**: **162** a 54 características y **128** a 122,
idénticos entre corridas. Con las épocas congeladas, el wall-clock del Autoencoder se mueve **1,29× y
3,63×** entre corridas ⇒ esa variación es **carga de máquina, no épocas**. El cociente s/época **no
separa nada** al tener denominador fijo.

**Consecuencia de diseño:** el eje **54-vs-122 es indecidible con este diseño sin medidas
repetidas**. Eso es un **resultado**, no una tarea pendiente. Y **T4 no debe diseñar las 10 semillas
para resolver la duda del número de épocas**: ya está resuelta.

### `[6]` (Goodfellow) — **no se retira; se ancla en `2.1.4 Algoritmos de ML`**

**Contexto.** Tras repuntar `2.1.2:30,64` de `[6]` a `[5]` en la auditoría de bibliografía (T15),
`[6]` se quedó **sin cita en el texto**, lo que choca con la regla dura de T16 («ninguna entrada sin
cita en el texto»).

**Decisión de Francisco: `[6]` NO se retira — se ancla en `2.1.4 Algoritmos de ML`**, abriendo allí
el bloque de redes neuronales que hoy falta (enlaza con T24). El anclaje legítimo es el **error de
reconstrucción**, que el proyecto usa en `3.4.2` y `4.4`: Goodfellow se cita como referencia canónica
**del concepto**, **sin afirmar que el modelo del TFG sea profundo**.

**Tres descartes:**
1. **`2.1.5`/`2.1.6`**: son métricas y metodología, **no arquitecturas**.
2. **Presentar el autoencoder como red profunda** para colgarle la cita: la memoria afirma lo
   contrario en `3.1:28`, `3.4:28` y `2.3.1:24` ⇒ crearía una **contradicción entre capítulos**.
3. **Retirar `[6]`** de la bibliografía: descartado por la propia decisión de anclarla.

> **Salvedad RESUELTA el 2026-08-09, al cerrar T0.** Era la contradicción entre la ficha T25 —que
> declaraba `2.1.4` como prosa de Francisco— y la decisión marco (b), que retira esa regla de `2.x`
> por completo. **Francisco decide no exceptuar `2.1.4`**: exceptuar una sola nota reintroduciría a
> mano la regla recién retirada del capítulo entero. La prosa de `2.1.4` la redacta el
> `redactor-tfg`, y con ello **T25 y T24 quedan desbloqueadas**.

---

## Decisiones del 2026-08-11

### T11 se estrecha — **`4.2.1` es la fuente numérica del KS; `5.1` la usa por referencia**

**Contexto.** El cierre de **T2** (2026-08-10) dejó el drift KS medido en **dos mediciones separadas y
no intercambiables**: **(A)** D1 vs D2 completo (**37/54** y **44/122** características con drift) y
**(B)** D1 vs las **9.711 normales de D2** (**25/54** y **31/122**; `src_bytes` 0,346 → 0,091,
`dst_bytes` 0,317 → 0,107). Con T10 escribiendo `4.2.1` y T11 escribiendo `5.1`, las mismas cifras
podían acabar **publicadas dos veces**, con el riesgo de que divergieran.

**Decisión de Francisco: `4.2.1` es la FUENTE NUMÉRICA y `5.1` la usa por referencia, sin repetir
cifras.** Consecuencia directa: **T11 pasa a interpretar, no a publicar** — el capítulo 5 explica el
desplazamiento D1→D2 y por qué el umbral p95 promete ≈5 % de FPR y el real es 8-10 %, pero **los
números y la tabla viven en `4.2.1`**.

**Se mantiene intacta la salvedad de T2:** el `delta = (A) − (B)` se publica como **comparación, nunca
como descomposición aditiva** —el KS es un supremo de diferencia de CDF y **no es aditivo sobre una
mezcla**—, y debe ir impresa **donde estén las cifras**, es decir en `4.2.1`.

**Precisión de vocabulario que no se relaja:** es **desplazamiento entre particiones, no deriva
temporal**. NSL-KDD no tiene marca de tiempo.

**Anotado también en la ficha T11 de `features.md`**, en su viñeta `5.1`/`5.4`.

### Procedencia dentro de los artefactos de `validacion.py` → **`import config`; Q2 EXTENDIDA de las rutas a la procedencia**

**Contexto.** Los artefactos de `validacion.py` —los dos `*_validation_report.txt` y los dos
`*_vocabulario_onehot.csv`— no permitían leer **de qué corrida** salían: el mtime no lo dice (git no
lo versiona; tras un `clone` es la fecha de la copia) y el fichero no imprimía `commit` ni `fecha`, a
diferencia de los `metricas_*.csv`, que traen las dos columnas desde **T1**. El anclaje vivía solo en
un recuadro de `PIPELINE.md`, que hay que reescribir a mano en cada re-corrida. El mecanismo para
resolverlo **ya existía y solo existía en un sitio**: `config.commit_actual()`, con su convención de
sufijo `-sucio` acotada a `Implementacion/`. Duplicarlo por copia estaba descartado de antemano
—eliminar duplicación por copia es lo que se venía haciendo en los ciclos anteriores—, así que la
única vía era **importar `config.py` desde `validacion.py`**, y eso choca con una frontera que tres
sitios del proyecto declaraban inexistente.

**Decisión de Francisco (opción A): se crea la dependencia.** `validacion.py` hace `import config`
y usa `config.commit_actual()` más `datetime.now()` para estampar `commit` y `fecha` en la cabecera
de los dos informes (tras el título, antes de `Integridad:`) y como **dos columnas al final** del CSV
del vocabulario. La fecha se captura **una vez por invocación**, en el constructor, para que todos
los artefactos de la misma corrida lleven el mismo sello.

**PRECISIÓN SOBRE EL PERMISO — leer con cuidado, porque es fácil de tergiversar.** **Q2** (arriba,
§ Decisiones del 2026-07-06) dice que `program.py`/`validacion.py` «no se refactorizan ahora… solo
migran **sus rutas** a `config.py` si en algún momento se tocan». Es decir: **Q2 autoriza cruzar la
frontera para las RUTAS, y `config.commit_actual()` NO es una ruta.** Por tanto **este permiso no es
literal: es por ANALOGÍA**, y se apoya en que, una vez escrito el `import config`, la frontera queda
cruzada igual —el coste arquitectónico que Q2 evaluaba es el mismo—. Lo que ha ocurrido aquí es que
**Francisco ha consumido Q2 y ha EXTENDIDO su alcance: de las rutas a la procedencia.**
**No registrar esto como «Q2 ya lo autorizaba tal cual»:** quien lo lea dentro de tres meses creería
que Q2 dice algo que no dice. Q2 sigue intacta en su literalidad; lo que se amplía es su alcance, y
la ampliación es de esta fecha y de esta entrada.

**Acotado:** solo `validacion.py`. **`program.py` NO pasa a depender de `config.py`**, y **las rutas
de ninguno de los dos se han migrado**: esa parte de Q2 continúa sin ejecutarse.

**Dos condiciones verificadas antes de escribir el import** (si alguna hubiese fallado, el cambio no
se hacía): (1) `config.py` **no tiene efectos al importarse** —solo define constantes y funciones;
`ensure_dirs()` y `setup_utf8()` existen pero no se llaman a nivel de módulo, así que no crea
directorios ni toca matplotlib/stdout—, y (2) **no hay ciclo de imports**: `config.py` solo importa
la librería estándar. La condición (1) queda anotada como nota para quien edite `config.py`, porque
`validacion.py` ahora depende de ella: a diferencia de `import program`, la posición de
`import config` respecto al bloque `plt.style.use` **no** es load-bearing.

**Documentación actualizada para que deje de mentir** (la frontera se declaraba inexistente en tres
sitios, más un cuarto que apareció al revisar): `CLAUDE.md` (bloque de orden de ejecución), la
cabecera de `Implementacion/app/config.py`, el recuadro de trazabilidad de
`Implementacion/PIPELINE.md` y `Resultados/GUIA_RESULTADOS.md` (§2.4 y §3.2). **La tabla canónica de
los tres valores de `commit` (`<hash>`, `-sucio`, `-suciedad_desconocida`) sigue viviendo solo en
`PIPELINE.md` y no se ha duplicado.**

**Ninguna cifra cambia:** es procedencia y formato. **Y el cambio está en el árbol y las dos
variantes YA se re-corrieron**: los artefactos publicados salen de la corrida del **2026-08-11 a las
20:53** y llevan las dos líneas de cabecera y las dos columnas
(`Resultados/specialized_nsl_kdd_validation_report.txt:4-5` dice `Commit del código: fc1c6b4-sucio`
y `Fecha de la corrida: 2026-08-11T20:53:27`). **El commit es idéntico en los cuatro artefactos; la
fecha es la de cada invocación**: `2026-08-11T20:53:27` en la variante de 54 y
`2026-08-11T20:53:46` en la de 122, y cada CSV de vocabulario repite en sus filas el par de su
propia invocación. No citar `:27` como sello del informe de 122.

**Aun así el anclaje canónico sigue siendo el recuadro de `PIPELINE.md`, y su aviso de re-anclaje se
mantiene**, porque el sello estampado es `-sucio`: un sello así **no identifica una versión del
código** —el hash apunta al commit *anterior* al cambio y `-sucio` solo dice «difería, no se sabe en
qué»—. Lo que sí aporta es una fecha fiable **dentro** del fichero, que sobrevive a un `clone`, y el
aviso explícito de **no-reproducibilidad desde ese hash**. Cuando exista el commit de cierre de este
ciclo, hay que sustituir por él el hash del recuadro y el sello que se cita; **no se anota aquí
ningún hash futuro**.

> **NOTA FECHADA — 2026-08-12: el commit de cierre ya existe y es `9af842c`.** Los dos párrafos de
> arriba se conservan **tal cual** como historial de la decisión; lo que sigue es su actualización,
> no una reescritura. El commit de cierre de este ciclo es **`9af842c`** («codigo: cerrar los siete
> residuos de validacion.py y estampar la procedencia en sus artefactos»), que versiona **a la vez**
> `validacion.py`, `config.py` y los **cuatro artefactos** de la corrida del 2026-08-11 20:53, y es
> el **último** commit que toca `validacion.py` (verificado con `git log -- Implementacion/app/validacion.py`).
> Por eso el sello impreso `fc1c6b4-sucio` —cuyo hash es el del commit **anterior** al cambio—
> corresponde al estado de `validacion.py` **en `9af842c`**, y ahí es donde hay que hacer
> `git checkout` para reproducir los cuatro artefactos.
>
> - **El re-anclaje se hizo por vía TEXTUAL, no re-corriendo.** Se actualizaron el recuadro de
>   trazabilidad y la tabla de corridas de `Implementacion/PIPELINE.md` y las §2.4, §3.2 y §7 de
>   `Resultados/GUIA_RESULTADOS.md`. **Cero cifras alteradas y cero artefactos regenerados.**
> - **El sello DENTRO de los artefactos NO se editó y sigue diciendo `fc1c6b4-sucio`**: es una
>   salida generada, y solo cambiaría re-corriendo `validacion.py` con el árbol limpio. Lo que el
>   fichero no puede decir por sí solo —de qué versión salió— lo dicen el recuadro de `PIPELINE.md`
>   y esta nota.
> - **Anclaje frágil corregido de paso:** la cita `..._validation_report.txt:4-5` del párrafo de
>   arriba apunta a un artefacto regenerable y cualquier re-corrida que cambie el número de líneas
>   de cabecera la desplaza en silencio. Hoy sigue siendo correcta (verificado en disco el
>   2026-08-12: la línea 4 dice `Commit del código: fc1c6b4-sucio` y la 5
>   `Fecha de la corrida: 2026-08-11T20:53:27`), pero la forma canónica de citarla es **por el
>   nombre del campo** (`Commit del código:` / `Fecha de la corrida:`), no por su número de línea.
> - **Lo que NO cambia:** el anclaje canónico de procedencia sigue siendo el recuadro de
>   `PIPELINE.md`; la tabla de los tres valores de `commit` sigue viviendo solo ahí; y la
>   advertencia de que un sello `-sucio` no identifica por sí mismo una versión del código sigue
>   siendo cierta —lo que la resuelve aquí es el par «commit de cierre + este documento», no el
>   sello.
> - **Queda fuera de esta nota** el sello citado en
>   `Obsidian_TFG_Vault\04 Implementación del sistema\4.2 Base de datos utilizada.md`, que es del
>   vault y lo lleva el `redactor-tfg`: está fichado como residuo en `features.md`.

**Efecto colateral sobre una ficha abierta — NO está cerrada.** La ficha «Rutas absolutas
hardcodeadas en `program.py` y `validacion.py`» (🟠, `features.md`; origen `next-steps.md:267`)
queda **parcialmente destrabada**: el `import config` que necesitaría ya existe en `validacion.py`,
así que ese obstáculo desaparece. **Sigue ABIERTA**, y su parte bloqueante era otra: toca
`program.py`, y eso obliga a **decidir antes si se regeneran los splits** — decisión pendiente de
Francisco.

---

## Bitácora de este fichero

- `2026-07-06` — Creado. Reconciliado el estado real (54 features, H1-Opción1/H2/H3 hechos
  en código pese a la prosa de `next-steps.md`). Decidida Q1 → Opción C (set de features
  parametrizable por modelo; el experimento H1 con recall 0-day por tipo lo resuelve).
- `2026-07-06` — **Grill previo a la implementación completado.** Cerradas Q2 (config.py
  compartido acotado), Q3 (superficie de evaluacion.py + evaluar_0day_por_tipo + convenciones
  de clase), Q4 (UMBRAL_CONF vía cross_val_predict OOF, sin leakage), Q5 (imbalanced-learn
  compatible con sklearn 1.7.1 + regla de parada; requirements ya pinneado), Q6 (no cruzar
  balanceo × selección). Listo para empezar por `config.py` + `evaluacion.py`.
- `2026-07-06` — **`config.py` + `evaluacion.py` implementados y verificados** (smoke test en
  el venv: métricas binarias/multiclase/0-day correctas, figuras y CSV acumulado). No se tocó
  `program.py`/`validacion.py`.
- `2026-07-06` — **Q5 ejecutada, regla de parada NO disparada.** `imbalanced-learn==0.14.2`
  (acepta sklearn>=1.4.2,<2) instalado sin mover sklearn 1.7.1 / numpy 2.3.2 / scipy 1.16.0;
  añade `sklearn-compat==0.1.6`. Ambos pinneados en `requirements.txt`. Entorno congelado y
  coherente para todos los modelos.
- `2026-07-11` — **3.1-F resuelta: baseline RF monolítico APROBADO, ubicación `baseline.py`
  aparte** (elegida por el autor frente a "modo en firmas.py"). Registrada la especificación
  completa arriba. Métrica de decisión vs híbrido: recall 0-day por tipo. En la misma sesión
  se lanzó la ejecución pendiente de `firmas.py` (54 → 122).
- `2026-07-14` — **Arranque del grill de `hibrido.py`.** Cerradas H-1 (origen de modelos →
  cargar joblib persistidos + reconstruir el estimador de firmas solo para el OOF de
  `UMBRAL_CONF`) y H-2 (detector etapa 1 = Autoencoder por defecto seleccionable; tabla 0-day
  por tipo de los 4 detectores; Q6 matizada) y H-3 (etapa 2 = RandomForest seleccionable, fijo
  entre variantes). Creado `EL_FUTURO.md` (vías de diferenciación, a raíz del comentario del
  profesor sobre el RF). Cerrada H-4 (calibración de `UMBRAL_CONF`: presupuesto τ=2pp sobre OOF
  + tabla de sensibilidad de los 3 umbrales en D2; D2 solo para reportar) y H-5 (binaria del
  híbrido idéntica a la etapa 1 por construcción; la tesis se juega vs baseline monolítico) y H-6
  (scoring multiclase: matriz 5×6 + métricas por alcance, sin número único; comparación vs baseline
  por recall 0-day) y H-7 (artefactos/CLI/idempotencia = patrón auditado; descriptor joblib).
  **Grill de `hibrido.py` cerrado (H-1…H-7).** Registrados los pendientes de diseño menores
  (alcance H1, caveat FPR, datos cargados). `hibrido.py` aún NO implementado: es el siguiente paso.
- `2026-07-14` — **Pendientes de diseño RATIFICADOS (P-1…P-5) y arranque de la implementación de
  `hibrido.py`.** Verificadas en disco las interfaces reales (`config.py`, `evaluacion.py`,
  `anomalias.py`, `firmas.py`, `program.load_specialized_splits`) antes de tocar código (regla §6).
  Cerrados los 5 puntos abiertos: P-1 una variante por invocación · P-2 FPR junto al recall 0-day ·
  P-3 solo D2+D3 · P-4 calibración con separación estructural anti-leakage (no ve D2) · P-5 binaria
  = `es_sospechoso` sin veto de etapa 2. Bookkeeping de `next-steps.md` (40→54, H1/H2/H3) cerrado.
  Implementado `hibrido.py` siguiendo H-1…H-7 + P-1…P-5. **Auditado por `auditor-ml`: veredicto
  APTO** (sin bloqueantes ni importantes; verificados uno a uno los 7 riesgos críticos: anti-leakage
  estructural de la calibración, orden de clases OOF↔cascada, reensamblado booleano, reconstrucción
  fiel de la firma con prefijo `clf__` de SMOTE, regla τ=2pp, reutilización de `_score`/umbral,
  máscaras 0-day y matriz 5×6). 3 hallazgos MENOR: **M1 aplicado** (el bucle de 4 detectores ahora
  captura también `RuntimeError` de variante mal etiquetada → degrada con aviso en vez de abortar);
  **M2/M3 = notas para la memoria 5.3** (no código): `metricas_hibrido_0day.csv` incluye filas
  `tipo='__global__'` a filtrar al agregar; `d2_recall_0day_global` es idéntico en los 3 umbrales por
  construcción (recall 0-day = etapa 1, independiente de `UMBRAL_CONF`) — explicarlo para que no se
  lea como error. **Ejecutado (54 y 122)** sin errores.
- `2026-07-15` — **`hibrido.py` ejecutado (54 y 122) → Q1/C resuelta: 54 features (opción A).**
  `UMBRAL_CONF=0.5` en ambas (regla τ=2pp). Cascada AE→RF: binaria recall 0.832 / FPR 0.102 (54);
  recall 0-day global 0.771 (54) vs 0.150 del baseline monolítico → tesis del híbrido confirmada
  ~5×. Decisión Q1/C y hallazgos colaterales (complementariedad de detectores, `snmpgetattack`
  ciego, 13.4% de routing a unknown) registrados arriba (§ Decisión del 2026-07-15) y en
  `EL_FUTURO.md`. **Casilla 4.3.5 cerrada.** Siguiente: volcado a la memoria caps. 4-5.
- `2026-07-16` — **Volcado a la memoria de caps. 4.3-4.5 y 5.1-5.3 completado y AUDITADO** (dos
  auditorías adversariales de cifras: cap. 5 APTO CON CAMBIOS —3 menores, aplicados—; cap. 4 APTO
  CON CAMBIOS —4 aplicados + 1 opcional aplicado—). **Fe de erratas registrada arriba** en la
  decisión del 2026-07-15: el argumento de descarte de la ventaja 0-day de las 122 contradecía a
  `metricas_hibrido_0day.csv` (`mailbomb` 0.00→0.123 con 122, 65% del delta); la decisión A (54)
  no cambia — se sostiene en la degradación ~9 pp de la etapa de firmas. Corregido también en la
  memoria (4.3.5). `GUIA_RESULTADOS.md` reconciliada con el estado real (54 features, drift 37,
  4 features de D2 fuera de [0,1], inventario de artefactos de modelos).
- `2026-07-21` — *(registrado 2026-07-22)* — **Grill de redacción del vault.** Registradas 3
  decisiones (§ Decisiones del 2026-07-21): reparto de 4.2 opción 1 (teoría del dataset cedida a
  Claude como borrador factual con `[CITA:]` pendientes; «por qué» a revisión de Francisco);
  convención de código incrustado inline verbatim recortado (comentarios que contradigan la prosa
  se recortan); terminología canónica del detector = "semisupervisado (one-class)", "no supervisado"
  como sinónimo declarado una vez. Todo verificado en disco; sin cambios de código ni cifras.
- `2026-08-01` — **Reparto documental entre los tres ficheros de seguimiento.** `features.md` es el
  registro operativo vivo (tareas abiertas y cerradas); `next-steps.md` queda **congelado en cuanto
  a casillas** (su §1-§5 es historial y bitácora, y su §6 sigue vigente como especificación técnica
  de cada script); `resumen-de-decisiones.md` es el registro de decisiones de diseño. **Salvedad:**
  §6.5 (`hibrido.py`) está superada por el grill H-1…H-7 de este mismo fichero, como ya declara
  `next-steps.md:592-597`. Propagado a `CLAUDE.md:117`, `resumen-de-decisiones.md:4`,
  `README.md:26-28` y `Guia_ML\README.md:7-9`. **Deuda conocida, no resuelta:**
  `Implementacion\diagramas\README.md:10` conserva la redacción antigua; tiene ficha abierta en
  `features.md`.
- `2026-08-06` — *(registrado 2026-08-09)* — **Grill de los cuatro informes del `researcher`
  (13 preguntas).** Registradas arriba (§ Decisiones del 2026-08-06) el **criterio rector** del lote,
  la **decisión marco (a)** —reapertura declarada del track de código, cerrado el 2026-07-16, con
  alcance exacto: Nivel 1 + Nivel 2 acotado a 10 semillas + dos mediciones baratas, todo por
  `auditor-ml`—, la **decisión marco (b)** —retirada de la regla «lo escribe Francisco» en dos
  velocidades: `2.x` completa, `6.2` a borrador con revisión final, bibliografía Zotero/IEEE sigue
  siendo de Francisco— y la **renuncia declarada al p-valor** sobre las 10 semillas. El lote se dio de
  alta como las fichas T0-T17 de `features.md`; los descartes cerrados están en su tabla «Descartado
  — no reabrir». Sin cambios de cifras.
- `2026-08-09` — **Cierre de T18, T22, T15 y la ficha «Auditar la bibliografía».** Registradas arriba
  (§ Decisiones del 2026-08-09) las conclusiones de diseño de **T18** (el CSV publica solo lo estable;
  los números viven en `PIPELINE.md` anclados a commits) y de **T22** (`n_iter_total_grid`
  determinista, 162 a 54 y 128 a 122 ⇒ la dispersión de wall-clock es carga de máquina, no épocas; el
  eje 54-vs-122 es indecidible con este diseño sin medidas repetidas), y la decisión de Francisco de
  **no retirar `[6]` (Goodfellow) y anclarla en `2.1.4`** con sus tres descartes. **Volcado parcial de
  T17**, que sigue abierta: falta el bloque «Decisiones tomadas a partir de este informe» en los
  cuatro informes de `99 Investigación/` y la deriva de documentación de `evaluacion.py`.
- `2026-08-11` — **Estrechamiento de T11 y migración de la deuda técnica de `next-steps.md` §3.2.**
  Registrada arriba (§ Decisiones del 2026-08-11) la decisión de Francisco de que **`4.2.1` sea la
  fuente numérica del KS y `5.1` la use por referencia** ⇒ **T11 interpreta, no publica**. En el mismo
  cierre, las casillas de deuda de `next-steps.md` §3.2 pasan a **cinco fichas de `features.md`** (§3.2
  y §3.3 quedan como historial con cabecera propia, **sin reescribir ninguna casilla**; el aviso de
  §3.3 declara que sus tres `☐` ya están hechas y no deben reabrirse), y quedan dadas de alta **dos
  specs nuevas**: las tres correcciones del `4.2` y la glosa del sufijo `-sucio` en `PIPELINE.md` y
  `GUIA_RESULTADOS.md`. **Sin cambios de cifras.** **Desajuste vivo anotado en `features.md`:**
  `Implementacion/app/validacion.py` está **modificado, sin commitear y sin re-correr** (`+231 −21`) —
  los 2 informes de validación y las 12 figuras de `Resultados/` son de la corrida `274923d`-sucio y
  **no corresponden al código actual**; C3 está aplicada en el árbol, y C1 y C2 **a medias** (el dict
  `onehot` es un *dead parameter* y `_save_report()` no escribe ni los 0-day ni el delta).
  **SUPERADO ese mismo día por la entrada de abajo:** en la re-corrida del **2026-08-11 20:53**
  (sello `fc1c6b4-sucio`) los cuatro artefactos de `validacion.py` se regeneraron con el código
  del árbol, así que **ya no son de `274923d`-sucio ni están desalineados**. El desajuste descrito
  en esta viñeta es el estado **anterior** a esa corrida y no debe citarse como estado actual.
- `2026-08-11` — **Procedencia dentro de los artefactos de `validacion.py` (residuo 5, opción A).**
  Registrada arriba la decisión de Francisco de **crear la dependencia `validacion.py` → `config.py`**
  para reutilizar `config.commit_actual()` y estampar `commit`+`fecha` en los dos informes y en el CSV
  del vocabulario, en vez de duplicar el mecanismo por copia. **El permiso NO es literal de Q2:**
  Q2 solo autorizaba cruzar la frontera para las **rutas**, y Francisco **extiende su alcance a la
  procedencia** (`program.py` no queda afectado; las rutas siguen hardcodeadas). Verificado antes:
  `config.py` no tiene efectos al importarse y no hay ciclo. Actualizadas las declaraciones de
  `CLAUDE.md`, la cabecera de `config.py`, `PIPELINE.md` y `GUIA_RESULTADOS.md`. **Sin cambios de
  cifras**, y **CON re-corrida**: las dos variantes se re-corrieron el **2026-08-11 a las 20:53**
  (sello `fc1c6b4-sucio`; fecha `2026-08-11T20:53:27` en la variante de 54 y
  `2026-08-11T20:53:46` en la de 122), así que los artefactos en disco **ya llevan** el sello en
  la cabecera de los dos informes y en las dos columnas del CSV del vocabulario. **El aviso de
  re-anclaje de `PIPELINE.md` se mantiene igualmente**, porque un sello `-sucio` no identifica una
  versión del código. Destraba parcialmente la ficha de rutas hardcodeadas, que
  **sigue abierta** (su bloqueo real es la decisión sobre regenerar los splits).
- `2026-08-12` — **Re-anclaje del sello `fc1c6b4-sucio` a su commit de cierre, `9af842c`.** Añadida
  arriba, dentro de la entrada de procedencia, una **nota fechada** que actualiza el aviso «cuando
  exista el commit de cierre…» sin borrar el texto original: ese commit **ya existe** y es
  **`9af842c`**, último que toca `validacion.py` y que versiona a la vez el script y los cuatro
  artefactos. Re-anclaje **textual**: **cero cifras alteradas, cero corridas, cero artefactos
  regenerados**, y **el sello impreso dentro de los artefactos no se editó** (sigue diciendo
  `fc1c6b4-sucio`, porque es una salida generada). Misma pasada que el re-anclaje de
  `Implementacion/PIPELINE.md` y `Resultados/GUIA_RESULTADOS.md`. Corregido de paso el anclaje
  frágil `..._validation_report.txt:4-5`, que pasa a citarse **por el nombre del campo**. Queda
  fuera —y fichado como residuo— el sello citado en el vault (`4.2 Base de datos utilizada.md`),
  que lleva el `redactor-tfg`.
- `2026-08-12` — **Las siete decisiones D1-D7 del barrido de semillas de T4.** Tomadas por Francisco
  en la sesión del andamiaje, antes de lanzar cómputo alguno. Se registran aquí porque **D1 y D5 son
  las que `A.3` y `5.4` van a citar**, y hasta ahora vivían solo en docstrings, en
  `Implementacion/PIPELINE.md` y en la ficha T4.
  - **D1 · Las 10 semillas son `[1,2,3,4,5,6,7,8,9,10]`**, constante `SEMILLAS_BARRIDO` en
    `config.py`, con aserción de que son 10 distintas y de que **42 no está dentro**. *Por qué esa
    lista:* es trivialmente reproducible, se escribe en `A.3` en una línea y **no admite la sospecha
    de *cherry-picking*** que sí admitiría cualquier lista de valores «bonitos» (7, 13, 99, 777). Las
    semillas no tienen semántica: basta con que sean fijas, públicas y elegidas **antes** de ver
    resultados. *Por qué 42 queda fuera a propósito:* la alternativa —9 semillas nuevas más reutilizar
    la fila ya publicada de la 42— obligaría al agregador a **leer las tablas publicadas**, que es
    precisamente lo que el andamiaje existe para no abrir. **Consecuencia que `A.3` y `5.4` deben
    decir explícitamente: la banda son 10 puntos con las semillas 1-10, y el titular de `5.1`-`5.3`
    es la 42, un punto INDEPENDIENTE que se declara y se sitúa dentro o fuera de la banda** — más
    honesto que meter el titular dentro de su propia banda.
  - **D2 · `cascada_invertida.py` entra en el barrido, con las 10 semillas.** Es el **quinto** script
    (la ficha T4 decía «4» y estaba mal; corregido en la ficha). No hace `fit` y cuesta segundos, y su
    cifra (67,53 % / 34,28 %) la va a citar **T9**: publicarla con `n=1` cuando las otras cuatro van
    con `n=10` sería incoherente.
  - **D3 · Los `.joblib` del barrido se borran al terminar cada semilla**, después de `hibrido.py` y
    `cascada_invertida.py` —que consumen los de su propia semilla—, dejando **intactos los 20
    publicados de la 42**. Lo hace el lanzador, no una pasada manual. *Por qué, habiendo 80,26 GB
    libres:* no son versionables ni reproducen nada que el código más la semilla no reproduzcan, y
    4,8 GB de `*_semilla<N>.joblib` convertirían `Resultados/modelos/` en un sitio donde ya no se
    distingue de un vistazo lo publicado de lo desechable.
  - **D4 · Las ~260 figuras del barrido no aportan**: se excluyen con `Resultados/figuras/*_semilla*`
    en el `.gitignore` raíz y se deja que se generen. Añadir un flag `--sin-figuras` habría obligado a
    tocar cinco scripts para ahorrar ≈44 MB locales. **`A.3` publica una tabla de dispersión, no 260
    gráficas.**
  - **D5 · Lista CERRADA de métricas que agrega el agregador** — de aquí sale literalmente la tabla de
    `A.3`. Anomalías: `roc_auc`, `pr_auc`, `f1`, `fpr`, `umbral`. Firmas: `f1_macro`, `accuracy_D2`,
    `recall_macro`, `f1_u2r` (la clase frágil). Baseline: `bin_accuracy`, `bin_fpr`, `f1_macro`,
    `recall_0day_global`. Híbrido: `bin_recall`, `bin_fpr`, `bin_accuracy`, `conocida_f1_macro`,
    `recall_0day_global`, `fpr_cascada`, `umbral_conf_elegido`. Cascada invertida: la tasa de la fila
    `__global__`. **`umbral` y `umbral_conf_elegido` entran a propósito**: son parámetros calibrados
    por semilla, y su dispersión es lo que **explica** la del FPR. **Las 6 columnas de tiempo NO
    entran, y la razón es medida, no estética:** el wall-clock dispersa **4,8×** entre corridas de
    calidad idéntica al bit (Autoencoder-54: 37,71 → 181,91 s, dato de T1), así que una `sd` de
    tiempos sobre 10 semillas mediría **la carga de la máquina, no el algoritmo**. Si algún día se
    publican, van en bloque aparte **rotulado como dispersión de máquina**, nunca junto a las métricas
    de calidad.
    - **Ampliación fechada del 2026-08-12 (no reescribe lo de arriba):** de la cascada invertida se
      agregan **dos** columnas de la fila `__global__`, `n_condenadas` **y** `tasa_condena`, no solo
      la tasa. Así está en el agregador (`agregar_semillas.py:139`) y así lo documenta
      `PIPELINE.md`. *Por qué:* aunque una sea la otra reescalada por un denominador constante (las
      9.711 normales de D2), **lo citable es `n_condenadas`** —lo declaran la ficha del barrido en
      `PIPELINE.md` y `config.ALCANCE_CASCADA_INVERTIDA`—, y con solo la tasa a 4 decimales T7/T11
      tendrían que multiplicar por 9.711 **a mano** para recuperarla: cálculo manual, que este
      proyecto no admite, y con pérdida de ~1 flujo de resolución. Es un entero: agregarlo es
      gratis y sin pérdida. El resto de la lista de D5 sigue **cerrada** tal cual.
  - **D6 · El agregador es un script nuevo, `Implementacion/app/agregar_semillas.py`**: cero `fit` y
    cero acceso a los CSV publicados. Lee las `metricas_*_semillas.csv`, agrupa por
    `(set_features, algoritmo, alcance)` y emite `n`, media, **`sd` muestral (`ddof=1`)**, mín y máx a
    4 decimales, con procedencia en cabecera. Dos salidas: `Resultados/dispersion_semillas.csv` **y**
    `Resultados/dispersion_semillas.md` con la tabla ya formateada, para que **T7** la pegue en `A.3`
    sin recalcular nada a mano —la regla del proyecto prohíbe el cálculo manual, que era el hallazgo
    🟠 nº 3 del andamiaje—. **Aborta si alguna combinación no tiene las 10 semillas:** una media de 7
    puntos presentada como de 10 es peor que no tener tabla. **El agregador NO decide el
    solapamiento:** emite mín/máx y `sd`, y la lectura —«los intervalos de RF y HGB se solapan, luego
    el orden no queda establecido»— la escribe **T11 en prosa, sin p-valor y con la renuncia
    declarada**.
  - **D7 · Se acepta la ventana de 4-5 h de máquina desatendida** con Francisco trabajando en
    paralelo. La estimación de ≈160 min de la ficha era de 4 scripts sin `cascada_invertida.py`, y el
    ensayo midió **1,6× más lento** con la máquina en uso (≈145 s frente a los ≈90 s publicados para
    anomalías-54). Por eso **el lanzador debe poder reanudar por semilla** —saltar las celdas
    `(semilla, set)` que ya tengan sus filas—: es **requisito**, no un extra.
  - **Límite del diseño que acompaña a las siete y hay que declarar en la memoria:** `program.py`
    **no** está parametrizado por semilla (su `random_state=42` es literal y no importa `config.py`).
    Las 10 semillas miden dispersión **de los modelos sobre splits D1/D2/D3 y set de características
    FIJOS**, sin variabilidad de preprocesado ni de selección de features. **Consecuencia para `5.4`:
    si RF y HGB se solapan, NO se podrá concluir «son equivalentes», solo «con estos splits el orden
    no queda establecido».**
