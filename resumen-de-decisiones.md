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
  la decisión. Métrica de decisión: **recall 0-day por tipo de ataque** (los 17 tipos de D2
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

**Nota del 2026-08-18 — la enumeración entre paréntesis de esta Q3 está DESFASADA; la decisión, no.**
La superficie real de `Implementacion/app/evaluacion.py` en disco hoy son **trece funciones públicas**
*(recuento corregido por la nota siguiente de esta misma fecha: **trece funciones en total, doce
públicas** — `_respaldar_csv` es privada; verificado contra el fichero en disco)*,
no las seis que enumera la viñeta: además de `evaluar_binario`, `evaluar_multiclase`,
`plot_matriz_confusion`, `plot_roc_pr`, `guardar_metricas` y `evaluar_0day_por_tipo`, expone
`metricas_tiempo` y **toda la maquinaria de esquema que trajo T1** —`validar_esquema_minimo`,
`cabecera_esperada`, `limpiar_variante_csv` (con su auxiliar `_respaldar_csv`), `comprobar_unicidad` y
`comprobar_recuento`—. **Lo que NO está superado:** la Q3 fija la superficie **por referencia a la
§6.5b de `next-steps.md`**, y esa referencia sigue siendo el contrato válido —ya actualizada—; lo
desfasado es solo su paréntesis, que ahora se lee como **la foto de 2026-08-06**, no como límite
vigente. Las **convenciones de clase** de la viñeta siguiente y el **fuera de alcance** siguen intactos
y verificados: `evaluacion.py` **no** contiene intervalos de confianza por bootstrap, ni calibración
más allá del umbral del híbrido, ni logging estructurado. **No se re-litiga ninguna decisión: solo se
deja constancia de que la lista dejó de ser exhaustiva.**

> [!todo] Sin establecer: **de qué decisión cuelga `metricas_tiempo`.** Las seis funciones de esquema
> se atribuyen a **T1** (esquema de métricas, lote de reapertura del 2026-08-06) con respaldo en la
> ficha y en la descripción de `CLAUDE.md`. Para `metricas_tiempo` **no se ha encontrado en el repo
> ninguna decisión registrada que amplíe la Q3 para admitirla**: entró sin quedar anotada. No se
> inventa aquí una justificación; lo decide Francisco si quiere cerrarlo.

**Nota del 2026-08-18 (segunda) — autoría de la corrección y recuento exacto.** Francisco AUTORIZÓ
hoy corregir las dos sedes que aún describían la superficie de `evaluacion.py` desfasada
(`CLAUDE.md:64`, que corrige él, y esta Q3). La viñeta original se deja **intacta** a propósito, como
traza de lo que se decidió el 2026-08-06: la reparación es esta nota, no una reescritura. Precisión
sobre el recuento de la nota anterior, verificada contra `Implementacion/app/evaluacion.py` en disco
hoy: el módulo define **trece funciones**, de las cuales **doce son públicas** y una es auxiliar
privada (`_respaldar_csv`). Las doce públicas, en orden de aparición: `metricas_tiempo`,
`validar_esquema_minimo`, `evaluar_binario`, `evaluar_multiclase`, `evaluar_0day_por_tipo`,
`plot_matriz_confusion`, `plot_roc_pr`, `cabecera_esperada`, `limpiar_variante_csv`,
`comprobar_unicidad`, `comprobar_recuento` y `guardar_metricas`. La ampliación respecto al paréntesis
original viene de **T1** (esquema de métricas) salvo `metricas_tiempo`, cuyo origen sigue sin
establecerse (ver el pendiente de arriba, que no se cierra aquí).

### Q4 — calibración de `UMBRAL_CONF` del híbrido → **`cross_val_predict` OOF, sin leakage**

- El `UMBRAL_CONF` (marca "unknown/0-day" si `predict_proba` máx < umbral) se calibra sobre
  probabilidades **out-of-fold** del mismo `StratifiedKFold(5)` de `firmas.py`
  (`cross_val_predict`), NO sobre el D3 con el que se entrenó (sería in-sample → leakage) ni
  sobre un holdout (sacrificaría las 52 muestras de u2r; recuento exacto en `Resultados\specialized_nsl_kdd_composicion_d3.csv`). El modelo final se re-entrena en
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
los 17 tipos de ataque ausentes del train; la etapa de anomalías sí. Ese contraste **es** la
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

> **NOTA FECHADA — 2026-08-14: la elección del algoritmo ganador de cada etapa SÍ miró D2.**
> El texto de H-2 y H-3 se conserva **tal cual** como historial; esto es un añadido que declara
> una desviación del protocolo ideal detectada al auditar la formulación de la regla, no una
> corrección del texto anterior.
>
> **1. Qué se decidió mirando D2.**
> - **H-2 (arriba, «Contexto»):** el Autoencoder se da por ganador «por AUC-ROC/F1 en 54 y 122».
>   Esas son métricas **de D2**, las reportadas en 5.1. El código lo documenta igual:
>   `hibrido.py:16` («Detector por defecto = Autoencoder (mejor en 5.1)») y la ayuda del flag
>   `--detector` en `hibrido.py:755` («por defecto Autoencoder, el mejor en 5.1; H-2»).
> - **H-3 (arriba, «Contexto»):** RandomForest se elige porque en 54 gana con **f1_macro D2 =
>   0.822** (frente a KNN 0.753 y RF 0.696 en 122). El criterio está enunciado sobre D2 de forma
>   literal en la propia decisión.
>
> **2. Cuál es la regla realmente vigente**, y es más estrecha que la que se venía enunciando.
> La que declara el código en `anomalias.py:18-22` es: *«D2 es INTOCABLE **para ajustar
> hiperparámetros o el umbral**»* (y, en la línea siguiente, «Selección de hiperparámetros: […]
> Jamás D2»). Es decir: la prohibición cubre **hiperparámetros y umbral**, no la comparación
> final entre algoritmos. La formulación general que circulaba por las notas —«ninguna decisión
> se toma mirando D2»— es **más amplia y falsa**, porque la elección de detector y de
> clasificador se apoyó justamente en D2. Esa formulación se ha corregido hoy en las notas del
> vault; a partir de aquí la que vale es la del código, con esta desviación declarada.
>
> **3. Qué SÍ quedó limpio** (para que esto no se lea como enmienda a la totalidad):
> - **Selección de configuración DENTRO de cada algoritmo de la etapa 1:** por AUC-ROC sobre
>   `D1_val` + una muestra de D3, nunca D2 (`anomalias.py:281`, `_seleccionar_config`).
> - **Hiperparámetros de firmas:** `GridSearchCV` con `StratifiedKFold(5)` y `f1_macro` **sobre
>   D3** (`firmas.py:16-18`, `:133`).
> - **Umbral de anomalías:** percentil 95 sobre `D1_val`, igual para los cuatro detectores
>   (`anomalias.py:22`).
> - **`UMBRAL_CONF`:** calibrado con probabilidades *out-of-fold* sobre D3 vía
>   `cross_val_predict` (`_calibrar_umbral_conf`, `hibrido.py:247`), y con **blindaje
>   estructural**: la función **no recibe D2 en su firma** (P-4; `hibrido.py:20-23`).
>
> **4. Encuadre y qué se hace con ello.** Es un caso de **data snooping en la selección de
> modelo** (P5/P3 de Arp et al.). Se **declara, no se corrige a posteriori**: rehacer la elección
> de detector y clasificador sin mirar D2 obligaría a rehacer el capítulo 5 entero. Declararlo es
> más defendible que negarlo, y entra en el inventario de limitaciones de **6.1**.

> **NOTA FECHADA — 2026-08-15: la nota anterior estaba INCOMPLETA. Las decisiones tomadas
> mirando D2 son TRES, no dos: falta el set de características (54 frente a 122).**
> El texto de la nota del 2026-08-14 se conserva **tal cual** como historial —igual que aquella
> conservó H-2 y H-3—; esto es un añadido que da de alta la tercera decisión omitida, no una
> corrección del texto anterior. La nota del 2026-08-14 no dice nada falso sobre H-2 y H-3: lo
> que hace es enumerar dos casos cuando el fichero documentaba tres.
>
> **1. La tercera decisión: la elección del set de 54 características frente al de 122**
> (decisión **Q1/C** de este mismo fichero, resuelta por el experimento **H1**). Se tomó
> midiendo **sobre D2**. Evidencia, toda en disco:
> - `resumen-de-decisiones.md:64-68` y `:131-133` — Q1/C fija como métrica de decisión el
>   «**recall 0-day por tipo de ataque** (los 17 tipos de D2 ausentes del train) + **F1 macro**».
>   Esos 17 tipos 0-day **solo existen en D2**: la métrica de decisión es, por construcción,
>   una métrica de test.
> - `Obsidian_TFG_Vault\04 Implementación del sistema\4.3 Preprocesamiento de los datasets.md:242-259`
>   — la tabla del experimento H1 se titula literalmente «**Métrica (cascada AE→RF sobre D2)**»,
>   y `:259` concluye «se elige el set de 54 para las dos etapas».
> - `Resultados\GUIA_RESULTADOS.md:172` — «decisión final validada por el **experimento H1**».
>
> **2. Es la más estructural de las tres**, porque no elige una pieza dentro de una etapa: define
> el **espacio de características de todo el sistema publicado**, sobre el que se entrenan tanto el
> detector de la etapa 1 como el clasificador de la etapa 2.
>
> **3. El defecto es de la misma familia que el que la nota anterior venía a corregir:** declarar
> **menos** *data snooping* del que hubo. Aquella nota corrigió una formulación general y falsa
> («ninguna decisión se toma mirando D2») enumerando dos casos; al quedarse corta en la
> enumeración, el resultado seguía subdeclarando el alcance real. De ahí que se dé de alta aquí
> en vez de dejarlo implícito.
>
> **4. Formulación canónica** — es la que se ha llevado hoy a las notas del vault (`2.1.6`, `3.3`,
> `4.3`, `4.6`, `5.4`, `6.1`, `A.3`), y la que debe usarse en cualquier sitio donde vuelva a
> aparecer esta salvedad, para no tener dos redacciones de lo mismo:
>
> > Tres decisiones del sistema se tomaron mirando D2: el detector de la etapa 1, el clasificador
> > de la etapa 2 y **el set de características (54 frente a 122)**. Las tres son selección de
> > modelo sobre el conjunto de test, es decir *data snooping*, y por tanto las métricas publicadas
> > son optimistas respecto a lo que daría un test verdaderamente ciego.
>
> **5. Qué se hace con ello:** lo mismo que con H-2 y H-3 —**se declara, no se corrige a
> posteriori**—, y entra en el inventario de limitaciones de **6.1** junto a las otras dos. Lo que
> el punto 3 de la nota del 2026-08-14 daba por limpio (configuración dentro de cada algoritmo de
> la etapa 1, hiperparámetros de firmas, umbral p95 y `UMBRAL_CONF`) **sigue limpio**: esta nota no
> lo toca.

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

**Nota del 2026-08-18 — el `bin_accuracy` = 0,8605 es cifra de COMPARABILIDAD EXTERNA, no titular
del sistema (decisión de Francisco).** Qué se decide: la accuracy binaria del híbrido sobre D2
(**0,8605**) se presenta y se cita **solo** como referencia para situar el sistema frente a los
baselines canónicos publicados sobre NSL-KDD, **nunca** como cifra de titular de los resultados.
Por qué: el objetivo del trabajo es la **detección de 0-day**, y una accuracy binaria agregada sobre
D2 no captura ese objetivo —un sistema puede subirla degradando justo lo que aquí se mide—, así que
usarla de titular desplazaría el criterio de éxito. Dónde está aplicada: como callout en
`Obsidian_TFG_Vault/05 Evaluación/5.4 Conclusiones del capítulo.md`. **Es una decisión DISTINTA de
H-6 y no debe fundirse con ella:** H-6 rige el *scoring multiclase* del híbrido (matriz 5×6 y
métricas por alcance, sin número único); esta nota rige el **estatus retórico de una cifra binaria
concreta**. Son compatibles —esta nota no altera H-6 ni ninguna otra decisión previa—, pero H-6 no
la cubría, y por eso se registra aquí.

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
- **Nota del 2026-08-14 — la línea anterior queda SUPERADA (Decisión 8 de la Fase 0, Francisco).**
  Ya no es «territorio de Francisco» ni una divergencia pendiente de decidir: **no era una decisión
  de contenido, porque el término canónico ya estaba fijado en esta misma sección**. Es una
  **instrucción al redactor de `2.2.4`**, y `2.2.4` es una de las 8 notas del capítulo 2 que se
  redactan de todas formas — así que **no lleva ciclo propio: se resuelve dentro de una nota ya
  encargada**. La instrucción está escrita en la ficha de las 8 notas en guion de `features.md`, que
  es donde la ve quien redacte. Se aplazó dos veces (2026-08-09 y 2026-08-11) precisamente por
  plantearse como decisión sin serlo. El texto de arriba se conserva como registro de lo que se creyó
  hasta hoy.

---

## Decisiones del 2026-08-06 (grill de los cuatro informes del `researcher`)

Cerradas en el `grill-me` de 13 preguntas del **2026-08-06**, que convirtió los cuatro informes de
`Obsidian_TFG_Vault/99 Investigación/` en las 18 fichas T0-T17 de `features.md`. Registradas aquí el
**2026-08-09** (volcado parcial de T17: falta el bloque «Decisiones tomadas a partir de este informe»
en los cuatro informes y la deriva de documentación de `evaluacion.py`).

**Nota del 2026-08-18 — el paréntesis «volcado parcial de T17» ya no describe el disco: los cuatro
bloques EXISTEN.** El texto de arriba se conserva y **no se reescribe**, pero su primera mitad quedó
contradicha por la tanda de informes del 2026-08-18: `## Decisiones tomadas a partir de este informe`
está hoy en los **cuatro** informes de `Obsidian_TFG_Vault/99 Investigación/`, verificado en disco
(`aprendizaje-continuo-nested-learning.md`, `arquitecturas-hibridas-en-la-literatura.md`,
`benchmark-comparativo-nsl-kdd.md` y `clasificadores-tabulares-y-arquitecturas-hibridas.md`). La
segunda mitad —la **deriva de documentación de `evaluacion.py`**— está **cerrada solo en parte**: la
enumeración desfasada de la Q3 la repara la nota fechada de hoy en esa misma sección, y **sigue
pendiente `CLAUDE.md:64`**, que describe `evaluacion.py` con el contrato pre-T1 (sin esquema, sin
procedencia, sin `metricas_tiempo`). Ese resto **lo alinea el hilo principal**, por ser fichero de
andamiaje. **Ninguna decisión de diseño cambia aquí.**

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

> **Nota del 2026-08-14 — esa decisión ya está tomada, y cierra esta ficha sin ejecutarla.** Ver
> «Decisión 2» más abajo: **los splits NO se regeneran**, así que la ficha de las rutas absolutas
> **se retira sin tocarse** y pasa a declararse como límite conocido en `A.3` (encargo escrito dentro
> de T7).

> **NOTA FECHADA — 2026-08-16: la re-corrida de hoy supera el sello, el inventario de artefactos y
> el motivo mismo de la dependencia.** Todo el texto anterior de esta sección se conserva **tal cual**
> como historial: esto lo **supera** en los puntos que enumero, no lo reescribe ni lo corrige. Origen:
> el ciclo que añadió a `validacion.py` la emisión del reparto de D3 por categoría
> (`medir_composicion_d3()` + `_guardar_csv_composicion_d3()`), auditado y con las cifras correctas,
> y la re-corrida de las dos variantes que lo publicó.
>
> - **(a) Afirmaciones superadas, nombradas por línea.** Quedan describiendo un estado **anterior** y
>   no deben citarse como estado actual: `:696-697` (enumera los artefactos de `validacion.py` como
>   **cuatro**), `:745-748` (cita `fc1c6b4-sucio` y las fechas `2026-08-11T20:53:27` / `:46` como el
>   sello en disco), `:763` y `:772` (el sello dentro de los artefactos «sigue diciendo
>   `fc1c6b4-sucio`»; «los **cuatro** artefactos»), `:776-781` (la línea 4 del informe dice
>   `fc1c6b4-sucio` y la 5 la fecha del 2026-08-11). **En la bitácora del final son otras tres, y
>   se citan aquí por su FECHA Y SU TEXTO, no por número de línea** —la primera redacción de esta
>   nota las apuntó por línea y erró en las tres, desplazadas exactamente las 53 líneas que ocupa
>   la propia nota al insertarse; misma disciplina que ya se aplica a la cabecera de los informes—:
>   en la entrada `2026-08-11` **de la procedencia** («residuo 5, opción A»), la frase «los
>   artefactos en disco **ya llevan** el sello en la cabecera de los dos informes y en las dos
>   columnas del CSV del vocabulario»; en su **nota fechada del 2026-08-14**, la frase «el sello
>   impreso **dentro** de los cuatro artefactos sigue diciendo `fc1c6b4-sucio`»; y en la entrada
>   `2026-08-12` **del re-anclaje**, el inciso «sigue diciendo `fc1c6b4-sucio`, porque es una
>   salida generada». Las tres siguen en pie **como historial y no se reescriben allí**: se marcan
>   desde aquí. **Lo que hay hoy en disco es
>   `a8c20e9-sucio`**, común a las dos variantes; la marca temporal, distinta en la de **54** y en la
>   de **122**, la declara cada artefacto en su campo `Fecha de la corrida:` (informes) o en su
>   columna `fecha` (CSV), y **no se transcribe aquí**: caduca en cuanto se vuelve a correr, mientras
>   que el commit identifica el estado del código y sobrevive a la re-corrida.
>   El sello impreso **no se ha editado a mano** —lo estampa
>   `config.commit_actual()` y solo cambiaría re-corriendo con el árbol limpio—: cambió **porque se
>   re-corrió**. Sigue valiendo, sin matiz, la doctrina de qué vale y qué no vale un sello `-sucio`, y
>   sigue sin existir el commit de cierre de esta re-corrida: **no se anota aquí ningún hash futuro**.
>   La forma canónica de citar la cabecera sigue siendo **por nombre de campo**
>   (`Commit del código:` / `Fecha de la corrida:`), nunca por número de línea.
> - **(b) El inventario pasa de cuatro a SEIS artefactos sellados**: los dos
>   `*_validation_report.txt` (cabecera), los dos `*_vocabulario_onehot.csv` (dos últimas columnas)
>   y los dos `*_composicion_d3.csv` **nuevos** (mismas dos columnas). El commit es idéntico en los
>   seis; **la fecha no**: se captura una vez por invocación en el constructor, así que cada CSV
>   repite en todas sus filas el par de **su** variante.
> - **(c) Decisión de diseño nueva, que nadie había registrado: el reparto de D3 se emite desde
>   `validacion.py` y no desde `program.py`.** `program.py` es quien construye D3, así que a primera
>   vista era su sitio natural. **No puede serlo sin romper una frontera que este mismo documento
>   sostiene:** por la propia Q2, `program.py` **no depende de `config.py`** —y sus rutas siguen
>   hardcodeadas—, de modo que no podría llamar a `config.commit_actual()` para estampar procedencia
>   sin cruzarla. Un artefacto de reparto sin sello volvería a caer en el problema que esta sección
>   resolvió. `validacion.py` **ya** ha pagado ese cruce y además es, por rol, la puerta de calidad
>   que mide los splits: el reparto de D3 es una **medición** sobre un split ya generado, no un paso
>   del pipeline. Se emite ahí.
> - **Y eso ENSANCHA otra vez el motivo de la dependencia: de «rutas → procedencia» a
>   «+ vocabulario de categorías».** `medir_composicion_d3()` lee `config.CATEGORIAS_ATAQUE`
>   (`validacion.py:423-424` y `:436`), que **no es procedencia**. **La Q2 extendida registrada arriba
>   NO cubre esta extensión** y no debe leerse como si la cubriera: aquella amplió el alcance de las
>   rutas a la procedencia, y punto. **Acotación de lo que se usa:** ese vocabulario sirve **solo para
>   fijar el ORDEN de las filas** del CSV —para que no dependa del orden de frecuencia— y para marcar
>   la columna `declarada_en_config`; **nunca para inventar recuentos**, que salen de `value_counts()`
>   y `len()`, con una comprobación que revienta si las categorías no suman el `__total__`, y con las
>   categorías fuera del vocabulario publicadas igualmente al final en vez de perderse en silencio.
> - **Reversible**: quitar la lectura de `CATEGORIAS_ATAQUE` deja el orden de las filas al de
>   frecuencia y no mueve ninguna cifra; el `import config` seguiría en pie por la procedencia.
> - ~~**SEÑALADA PARA REVISIÓN DE FRANCISCO.**~~ El punto (c) era una **decisión de diseño tomada por
>   un agente**, no registrada en su momento, y su segunda mitad extendía un permiso —Q2— que solo
>   Francisco extiende. Se anotó aquí para que se viera, no para darla por bendecida.
>   **✅ APROBADA POR FRANCISCO EL 2026-08-16.** Preguntado explícitamente con las dos alternativas
>   sobre la mesa —aprobar la extensión o revertirla duplicando la lista de categorías por copia—,
>   eligió **aprobarla**. Razón que pesó: duplicar el vocabulario por copia es exactamente el
>   problema que Q2 vino a resolver, así que revertir habría comprado pureza de acoplamiento al
>   precio de reintroducir la avería original. **Queda por tanto registrado que la dependencia
>   `validacion.py` → `config.py` cubre HOY tres cosas: rutas, procedencia y el vocabulario de
>   categorías.** Lo que sigue sin cubrir, y que ningún agente debe dar por extendido: cualquier
>   lectura de `config.py` que **produzca o altere un recuento**. Los recuentos salen de
>   `value_counts()` y `len()`, y esa frontera no la ha movido nadie.
> - Documentación alineada en la misma pasada, **CUATRO sitios**: cabecera de
>   `Implementacion/app/validacion.py`, docstring de `Implementacion/app/config.py`,
>   `Implementacion/PIPELINE.md` (que decía «dos informes + el CSV del vocabulario» y se
>   contradecía con su propio recuadro de trazabilidad, ya correcto en seis) y
>   `Resultados/GUIA_RESULTADOS.md`. **La guía se alineó de forma sustancial** —alta de su §2.5
>   para los `..._composicion_d3.csv`, reescritura de §2.4, y actualización de la fila de
>   `validacion.py` en §1, de §3.2 y de la entrada de §7 (verificado en disco el 2026-08-16)—, y
>   la primera redacción de esta viñeta la omitía, al contrario que la entrada homóloga del ciclo
>   anterior, que sí la listaba. Se añade aquí; aquella queda intacta.
> - **PENDIENTE que NO está hecho: `CLAUDE.md`.** Su bloque del orden de ejecución (hoy `:85-89`)
>   sigue diciendo que `validacion.py` importa `config.py` «y solo por la **procedencia**», sin el
>   motivo (2) —vocabulario de categorías, ver la viñeta de arriba—, y su inventario de artefactos
>   sellados enumera solo «la cabecera de sus dos informes y … las columnas de su CSV del
>   vocabulario del one-hot», es decir, se queda corto frente a los **SEIS** actuales: omite los dos
>   `*_composicion_d3.csv`. **Lo alinea el hilo principal, no un agente**, por ser fichero de
>   andamiaje. Queda registrado aquí a propósito: hasta hoy ese pendiente vivía **solo** en un
>   comentario de `validacion.py`, y al alinear `CLAUDE.md` ese comentario se borrará y el pendiente
>   habría desaparecido sin dejar rastro en ningún registro.

**Nota del 2026-08-16 — la marca temporal de una corrida DEJA DE CITARSE en prosa (decisión de
Francisco).** `validacion.py` se volvió a correr ese mismo día y los seis artefactos cambiaron su
`Fecha de la corrida:` / columna `fecha`, mientras el campo `Commit del código:` seguía diciendo
`a8c20e9-sucio`. La prosa de `Resultados/GUIA_RESULTADOS.md` y de esta sección se quedó citando las
marcas temporales anteriores, que ya no existían en ningún fichero. El defecto **no es de
transcripción sino de raíz**: copiar los segundos a la documentación hace que **cada re-corrida
futura invalide lo escrito**, sin que nada avise. Desde hoy: **el `commit` se sigue citando** —
identifica el estado del código y no cambia al re-correr— y **la marca temporal se REMITE al campo
del artefacto** (`Fecha de la corrida:` en los informes, columna `fecha` en los CSV) en vez de
transcribirse. Aplicado en `Resultados/GUIA_RESULTADOS.md` (cuatro sitios) y en la viñeta (a) de
arriba, donde **se conserva íntegra** la garantía de que el sello **no se ha editado a mano**. Lo
anterior queda intacto como historial; en particular, **las marcas temporales que sirven para
DISTINGUIR entre varias pasadas del mismo artefacto** —las cuatro de `agregar_semillas.py`, que solo
se diferencian por la hora— siguen citándose: ahí la marca es identificadora, no decorativa.

**Nota del 2026-08-18 — el sello `a8c20e9-sucio` que esta sección cita en presente está CADUCADO;
en disco es `ac36b88` LIMPIO.** Afecta a dos frases que se conservan íntegras como historial y **no se
reescriben**: la de la viñeta (a) «**lo que hay hoy en disco es `a8c20e9-sucio`**, común a las dos
variantes», y la del párrafo anterior «el campo `Commit del código:` seguía diciendo
`a8c20e9-sucio`». **`validacion.py` se volvió a correr en el ciclo de Código del 2026-08-17, esta vez
con el árbol limpio**, y hoy los **seis** artefactos sellados declaran **`ac36b88`**, idéntico en los
seis —verificado leyendo el campo `Commit del código:` de los dos `*_validation_report.txt` y la
columna `commit` de los dos `*_vocabulario_onehot.csv` y los dos `*_composicion_d3.csv`—. Lo demás de
la viñeta (a) **sigue valiendo sin matiz**: el sello **no se ha editado a mano** —lo estampa
`config.commit_actual()`— y cambió **porque se re-corrió**; la forma canónica de citarlo sigue siendo
**por nombre de campo**, nunca por número de línea; y la marca temporal **se remite al artefacto**, no
se transcribe. Lo que **sí cambia de estado** es la coletilla «sigue sin existir el commit de cierre de
esta re-corrida»: al ser `ac36b88` un sello limpio, **ya existe** ese estado versionado. La doctrina de
qué vale y qué no vale un sello `-sucio` **no se toca**: sigue vigente para cualquier corrida futura
sobre árbol sucio.

---

## Decisiones del 2026-08-14

Las tomó Francisco el **2026-08-14**, en el cierre de la **Fase 0 del plan de cierre** — las ocho
decisiones que ningún agente podía tomar y que eran el cuello de botella declarado del plan. Aquí
quedan las **tres de diseño**; las otras cinco son de proceso o de andamiaje y viven en `features.md`
(Decisión 4, acceso institucional), en `CLAUDE.md` §Git (Decisión 7, commit por tanda) o en la ficha
de las 8 notas del capítulo 2 (Decisión 8, ya anotada arriba en la sección de terminología).
**Ninguna de las tres movió una sola cifra publicada ni tocó código.**

### Decisión 1 — el eje de balanceo de `4.3.4` **no se reabre: se declara NO CONSTANTE**

El barrido de 10 semillas dejó que `class_weight` ganara en **17 de 40 celdas (42,5 %)** frente a
SMOTE, y quedaba decidir si eso obligaba a rehacer la elección publicada. **No se reabre**, por tres
razones que se sostienen en el dato y no en el coste:

- **Con n=1 el reparto YA era 2-2.** Verificado en `Resultados/metricas_balanceo.csv` (16 filas,
  sello `1163c90`, 2026-08-09), eje SMOTE vs `class_weight` —que solo aplica a DecisionTree y
  RandomForest—: 54-DecisionTree `class_weight` **0,9530 ± 0,0087** vs SMOTE 0,9350 ± 0,0165;
  54-RandomForest SMOTE **0,9736 ± 0,0079** vs `class_weight` 0,9715 ± 0,0147; 122-DecisionTree
  `class_weight` **0,9568 ± 0,0118** vs SMOTE 0,9513 ± 0,0184; 122-RandomForest SMOTE
  **0,9795 ± 0,0099** vs `class_weight` 0,9751 ± 0,0186. Es decir: **el barrido no descubre que la
  decisión estuviera mal, confirma que ese eje nunca estuvo establecido.** Reabrirlo no lo
  establecería.
- **Los márgenes están dentro del ruido.** RandomForest-54 decide por **0,0021**, unas **7 veces
  menos que su propia `sd`** (0,0079 y 0,0147). Eso es un **desempate arbitrario**, y así se escribe
  en la memoria.
- **Reabrir tendría coste de invalidación, no de cómputo:** tocaría `firmas.py`, movería cifras
  publicadas y arrastraría por cascada a `hibrido.py` y `cascada_invertida.py`, rompiendo la
  coherencia del barrido de 10 semillas recién cerrado.

**Acotación obligatoria al redactar** — sin ella se entendería que todo `4.3.4` es arbitrario, **y no
lo es**: el «no es constante» vale **solo** para el eje SMOTE vs `class_weight`. **El eje SMOTE vs
NADA (KNN e HistGradientBoosting) SÍ está establecido**: SMOTE gana en las **4 celdas**, y en
HistGradientBoosting con holgura enorme — **0,9694 vs 0,8327** (54) y **0,9724 vs 0,8044** (122).

**Configuración publicada**, verificada en `firmas.py:146` (`self.balanceo_ganador` alimenta el
entrenamiento final) e **idéntica en las dos variantes**: DecisionTree → `class_weight`;
RandomForest, KNN e HistGradientBoosting → **SMOTE**.

**Causa mecánica del 17 de 40, a citar al lado del recuento** (`firmas.py:40`, cabecera): cambiar la
semilla cambia el `StratifiedKFold`, así que el ganador de `4.3.4` y la config del grid pueden
cambiar con ella.

Se consume en `5.4` / `4.3.4` (ficha **T11**). **Cero código tocado.**

### Decisión 2 — los splits **NO se regeneran**

Los splits D1/D2/D3 son del **2026-07-05** y de ellos cuelga **todo lo publicado**: 9 tablas, 20
`.joblib`, 39 figuras y las 2.320 filas del barrido de semillas. Regenerarlos obliga a re-correr el
pipeline entero **más las 2 h 29 min del barrido** y **no aporta ningún número nuevo**.

**Consecuencia sobre la ficha que bloqueaba** («Rutas absolutas hardcodeadas en `program.py` y
`validacion.py`»): **no se ejecuta**. Es **cosmética de portabilidad**, no afecta a ningún resultado,
y **tocar `program.py` sin re-correrlo dejaría código modificado no ejecutado, que es peor que la
deuda**. No se descarta en silencio: **se declara como límite conocido en `A.3`**, y ese encargo
queda escrito dentro de **T7**, que es quien redacta `A.3`.

### Decisión 3 — permiso del `ml-implementador` sobre este fichero: **ACOTADO a nota fechada**

El `ml-implementador` **puede añadir notas fechadas** a este documento; **no puede reescribir ni
borrar texto previo**, ni siquiera para corregirlo. Si algo anterior queda superado, lo dice **en la
nota nueva** y deja intacto lo viejo — la forma que este fichero ya venía usando (`9af842c`,
`419f4c7`) y que es la de la nota que abre esta misma sección.

**Por qué acotado y no general:** este documento es **el registro de decisiones del TFG**. Un permiso
libre permitiría **reescribir historial sin que nadie lo vea al leer**, que es exactamente lo que un
registro existe para impedir. Lo que exceda de una nota fechada —reordenar, refundir, corregir una
línea antigua— lo sigue aplicando el hilo principal con Francisco delante, que es el reparto que ya
funcionó en `c5ceca5`: el implementador **redacta y verifica**, el hilo principal **aplica**.

Aplicado en `.claude/agents/ml-implementador.md` el mismo 2026-08-14.

---

## 2026-08-16 — Decisiones técnicas de la TANDA 12 (T9, recorte del capítulo 3)

Nota fechada añadida al cierre de la Tanda 12. Recoge cuatro decisiones **delegadas por Francisco en
los agentes** durante el recorte de duplicidades del capítulo 3. Las cuatro son **reversibles** y se
registran con su motivo; **ninguna cifra ya publicada se mueve** y no se reescribe nada de lo
anterior de este fichero.

### Decisión 1 — Renumeración **local** de `3.3`, y de nada más

Al suprimir `3.3.2 Dónde se ajusta la normalización` (absorbido en `3.3.1`) y
`3.3.3 Recorrido de un flujo por la cascada` (absorbido en `3.2.1`), la nota `3.3` queda con **dos**
apartados:

| Antes | Después | Qué ha pasado |
|---|---|---|
| `3.3.1` | `3.3.1` | Se mantiene, y absorbe el contenido de la antigua `3.3.2` |
| `3.3.2 Dónde se ajusta la normalización` | — | Suprimido: absorbido en `3.3.1` |
| `3.3.3 Recorrido de un flujo por la cascada` | — | Suprimido: absorbido en `3.2.1` |
| `3.3.4 Protocolo de evaluación común` | `3.3.2 Protocolo de evaluación común` | Reetiquetado |

**No se renumera ningún otro apartado del capítulo 3.**

**Por qué es seguro renumerar aquí y solo aquí:** se comprobó con búsqueda sobre **todo el vault**
que **ninguna nota fuera del capítulo 3 cita subapartados `3.3.x`**; las remisiones externas al
capítulo 3 se hacen **por wikilink a nota**, no a subapartado. El renumerado es por tanto **local** a
`3.3` y no deja ninguna remisión rota.

**Reversible:** restaurar la numeración anterior exige únicamente **reetiquetar dos cabeceras**.

### Decisión 2 — El paso 1 de la antigua `3.3.3` **se trasplanta, no se pierde**

El informe de la Tanda 10 pieza B (`99 Investigación/Datos repetidos en el capítulo 3.md`, §S15)
advertía que la frase «se transforma con los codificadores y el escalador persistidos» **no estaba
presente en `3.2.1`**, y dejaba abierta la alternativa entre trasplantarla o **perderla
deliberadamente** al suprimir el apartado.

Se decide **trasplantarla** a la prosa de `3.2.1`, que pasa a ser la **sede canónica** del recorrido
de un flujo por la cascada.

**Motivo:** es **información de diseño** —el hecho de que en inferencia se reutilizan los
transformadores ya ajustados, y no se reajustan— que **no aparece en ningún otro punto del
capítulo**; suprimirla sería perder contenido, no eliminar una duplicidad.

### Decisión 3 — `2.3.3` pasa a remitir con **ancla de sección** `(§3.1.5)`

La Tanda 10 había decidido, con carácter **provisional**, dejar la remisión de `2.3.3` al modelo de
amenaza como **wikilink a nota** sin ancla, **a la espera de la renumeración del capítulo 3 prevista
en T9**. Cumplida esa condición, y **confirmado que `3.1.5` no se renumera** (T9 no toca `3.1`), el
ancla es estable y **esta decisión deroga la provisional del 2026-08-15**.

Formato adoptado, que **no rompe la convención de wikilink a nota** ya usada en el proyecto:

```
[[3.1 Requisitos del sistema|3.1]] (§3.1.5)
```

Aplicado a las **dos** remisiones de `2.3.3` que apuntan al modelo de amenaza (la del párrafo de
delimitación de alcance y la del callout «Remisión» de 2.3.3.3). **Reversible:** basta con retirar el
`(§3.1.5)` y el alias.

### Decisión 4 — El titular del recorte se publica **redondeado y con «≈»**

Magnitud estimada del recorte del capítulo 3:

| Alcance | Reducción |
|---|---|
| Capítulo 3 completo | **≈20 %** |
| `3.1`–`3.3` | **≈25 %** |
| `3.1`–`3.3`, descontando `3.1.5 Modelo de amenaza` | **≈35 %** |

`3.1.5` se descuenta en la tercera fila porque **se escribió después del comentario del profesor** y
**no duplica nada**: es contenido nuevo, de modo que incluirlo enmascara cuánto se ha recortado
realmente de lo que ya existía.

**Estas tres cifras son estimaciones a ojo, no una medición:** **no existe script de conteo de
palabras** en el proyecto. Por tanto, si alguna vez se trasladan a un correo al profesor o a la
memoria, van **siempre con «≈» y con la palabra *aproximadamente***, nunca como dato exacto. Si en
el futuro se dispone de una medición real, **estas cifras se sustituyen** por ella.

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

  > **NOTA FECHADA — 2026-08-14: el aviso de re-anclaje YA NO se mantiene; el re-anclaje está
  > hecho y su commit es `9af842c`.** La entrada de arriba se conserva **tal cual** como
  > historial —no se reescribe ni se borra ninguna de sus líneas—; esto la **supera** en el único
  > punto que quedó desfasado: la frase «**El aviso de re-anclaje de `PIPELINE.md` se mantiene
  > igualmente**» describía el estado del 2026-08-11, cuando el commit de cierre aún no existía.
  > Al día siguiente sí existió: el re-anclaje del sello `fc1c6b4-sucio` a **`9af842c`** se aplicó
  > por vía **textual** en `Implementacion/PIPELINE.md` y `Resultados/GUIA_RESULTADOS.md`, y está
  > registrado en la nota fechada del 2026-08-12 (dentro de la sección de procedencia) y en la
  > entrada `2026-08-12` de esta misma bitácora, justo debajo.
  >
  > Lo que **no** cambia y sigue siendo cierto de la entrada original: el sello impreso **dentro**
  > de los cuatro artefactos sigue diciendo `fc1c6b4-sucio` —es una salida generada y solo
  > cambiaría re-corriendo `validacion.py` con el árbol limpio—, y un sello `-sucio` sigue sin
  > identificar por sí solo una versión del código. La diferencia es dónde se resuelve: **ya no
  > hay un aviso pendiente**, hay un anclaje escrito que dice que ese sello corresponde al estado
  > de `validacion.py` en `9af842c`.
  >
  > Punto 5 de una auditoría anterior que había quedado sin aplicar porque el implementador no
  > tenía permiso de escritura en este fichero. Permiso concedido por Francisco el 2026-08-14
  > (Decisión 3 de la Fase 0) y **acotado a añadir nota fechada**, nunca a reescribir: por eso
  > esto es una nota y no una corrección de la línea de arriba.
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
- `2026-08-14` — **Fase 0 del plan de cierre, CERRADA: las ocho decisiones que solo podía tomar
  Francisco.** Registradas aquí las **tres de diseño** (§«Decisiones del 2026-08-14»): **1** el eje de
  balanceo de `4.3.4` no se reabre y se declara no constante —acotado a DecisionTree/RandomForest, con
  el ganador de la semilla 42 verificado en `Resultados/metricas_balanceo.csv` y en `firmas.py:146`—;
  **2** los splits no se regeneran, y la ficha de las rutas absolutas se retira sin ejecutarse hacia
  `A.3`; **3** permiso del `ml-implementador` sobre este fichero acotado a **nota fechada**. Las otras
  cinco no son de diseño y viven donde les toca: **4** acceso institucional —los puntos quedan
  **marcados**, no cerrados, para la relectura final de Francisco, con la regla de marcado aplicada en
  `.claude/agents/redactor-tfg.md`—; **5** los tres `grill-me` se aplazan a la Fase 6, detrás de todo
  el volcado; **6** el título queda aplazado; **7** un commit por tanda paralela, aplicado en
  `CLAUDE.md` §Git; **8** la divergencia de la terminología de `2.2.4` no era decisión sino
  instrucción al redactor —anotada en su sección—. **Cero código tocado, cero cifras publicadas
  movidas.**
- `2026-08-15` — **Localizador de página en las citas: REFINA la decisión del 2026-07-21 (`:531`), no
  la sustituye.** Francisco confirma que **el formato IEEE lo genera él en Zotero** —eso sigue igual—
  y precisa **qué necesita de los agentes**: (1) **de qué libro o página web salió cada afirmación** y
  (2) **el párrafo marcado con una numeración que apunte a esa fuente**. La (2) ya la cumplía el `[n]`
  desde siempre. La (1) estaba cubierta **a nivel de obra pero nunca de página**, y esa era la única
  pieza que faltaba para que él pudiera generar el formato sin volver a abrir las fuentes.
  **Falso amigo detectado al analizarlo:** los `pp. 222-232` que ya aparecen 28 veces en
  `Bibliografía.md` son **el rango del artículo dentro de su revista** —metadato de la referencia—,
  **no** el localizador de la afirmación. Por eso parecía resuelto y no lo estaba.
  **Lo acordado:** el marcador admite **localizador opcional en sintaxis IEEE nativa**
  (`[8, p. 45]`, `[5, cap. 1]`), que **no consume número del contador global** —`[8, p. 45]` y
  `[8, p. 90]` son la misma entrada `[8]`—; es **obligatorio solo en libros y documentos largos**,
  que son **ocho** (`[4]` Chio, `[5]` Géron, `[6]` Goodfellow, `[7]` Murphy, `[8]` Stallings,
  `[12]` Hastie, `[39]` Russell y Norvig y `[54]` Molnar — **la primera redacción decía «ocho» y
  enumeraba siete, olvidando a Molnar; corregido contra `Bibliografía.md` el mismo día**), porque en
  artículos IEEE no pide más que lo ya registrado; `Bibliografía.md` gana una columna **«Localizador por uso»** que escribe **solo el
  `researcher`**; y **la página que no se pueda establecer con honestidad SE MARCA, no se inventa**
  —misma disciplina que con las 47 citas reconstruidas—. El `redactor-tfg` anota la fuente dentro del
  propio `[CITA: …]` **mientras escribe el párrafo**, que es cuando la sabe: recuperarla después
  cuesta el triple. **El retrofit está acotado a esas 8 entradas, no son las 56.** **Dos de las ocho
  no se pueden cerrar aún, y conviene saberlo antes de despachar el pase:** `[6]` Goodfellow **está
  huérfana en todo el vault** —no la cita nadie, así que su localizador depende de que **T24** la
  ancle— y `[54]` Molnar **tiene la edición sin fijar** (su web sirve hoy la 3.ª y la literatura cita
  la 2.ª de 2022), de modo que la página depende de esa elección, que es de Francisco.
  **Consecuencia sobre las 5 citas no reconstruidas, que Francisco aún debe decidir:** de `[27]`,
  `[28]` y `[44]` no se conoce ni la obra, así que **bajo este criterio nunca serán citables** — lo
  cual no cierra la decisión, pero inclina el argumento hacia **retirar la afirmación** frente a
  buscar fuente alternativa. Aplicado en `CLAUDE.md`, `.claude/agents/leader.md`, `researcher.md` y
  `redactor-tfg.md`.
- `2026-08-15` — **DELEGACIÓN GENERAL DE DECISIONES TÉCNICAS A LOS AGENTES. Es un cambio de régimen,
  no una decisión puntual.** Francisco: «yo no debo ser bloqueante para nada». A partir de aquí **las
  decisiones técnicas las toma el agente con criterio técnico**, sin devolverlas a Francisco, **con
  dos condiciones que son las que hacen la delegación segura**: (1) **cada decisión se registra
  fechada en este fichero**, con su porqué, y (2) **debe ser REVERSIBLE** — si deshacerla es caro o
  imposible, no está delegada y vuelve a Francisco. **Siguen siendo SUYAS y explícitamente NO
  delegadas:** el **título** del TFG (aplazado por él a la Fase 7), la **bibliografía final en
  Zotero/IEEE**, la **revisión final de `6.2`**, y **cualquier borrado o acción irreversible** —el de
  `03 Desarrollo/` incluido, que sigue necesitando permiso expreso—. **Motivo de la delegación:** el
  cuello de botella no era la capacidad de decidir sino la **latencia** de tener que preguntar; con
  33 fichas abiertas, doce decisiones pendientes bloqueaban ejecuciones largas que no las necesitaban
  de verdad.
- `2026-08-15` — **ORDEN DE TRABAJO: se va por capítulos, PERO el orden estricto 1→2→3→4→5→6 NO es
  posible, y forzarlo produciría progreso ficticio.** Analizado contra disco. **Contenido
  estructuralmente terminal**, que no puede cerrarse hasta que exista el resto: `Resumen`, `Abstract`,
  el **título**, la **bibliografía final** y —el que no era obvio— **`1.4 Estructura`**, que describe
  los capítulos 1 a 5, **no menciona el 6 ni los apéndices** y atribuye las conclusiones al capítulo 5.
  **Por tanto el capítulo 1 NO puede cerrarse el primero.** **Dependencias cruzadas verificadas:**
  `2.3.3:11` y `2.3.3:91` remiten **dos veces** el modelo de amenaza concreto a `3.1`, así que
  **cerrar el capítulo 2 exige escribir antes un trozo del 3**; **T19** toca `4.4`, `5.1` y `5.2` a la
  vez, así que **el 4 no se cierra sin el 5**; y **T21** reparte entre `6.1` y `5.4`.
  **ORDEN APROBADO:** (0) desbloqueo — análisis de datos repetidos del cap. 3 + modelo de amenaza en
  `3.1`; (1) capítulo 2 completo; (2) capítulo 3, ya con el recorte decidido; (3) **capítulos 4 y 5
  juntos**; (4) capítulo 6 + `1.4` + preliminares + bibliografía.
  **Corrección al registro:** `3.1` **NO está vacía** —tiene `3.1.1`–`3.1.4` con prosa real—; lo que
  le falta es **una subsección** de modelo de amenaza. Añadir, no redactar de cero.
- `2026-08-15` — **Las 5 citas no reconstruidas: BÚSQUEDA ACOTADA y, lo que no aparezca, SE RETIRA.**
  Decisión de Francisco entre las tres opciones. El `researcher` hace **un intento acotado por cita**;
  la afirmación cuya fuente no aparezca **se retira o se reescribe como afirmación propia sin cita**,
  nunca se deja una cita inventada ni un `[n]` colgando. De `[27]`, `[28]` y `[44]` **no se conoce ni
  la obra**, así que se espera que caigan por esta vía. Cierra la ficha 🔴 heredada de la Tanda 6.
- `2026-08-15` — **`2.1.5 Métricas` se COMPLETA al nivel de `A.2`, no se degrada ni se funde.**
  Diagnóstico verificado: son 52 líneas con las métricas enumeradas —matriz de confusión, precisión,
  recall, MAE, RMSE, Silhouette— pero **sin las fórmulas** («TP es el número de verdaderos positivos»
  y nunca la escribe), con una frase cortada a mitad y sin citas, mientras `A.2 Métricas de desempeño`
  **sí tiene las fórmulas en LaTeX**. Se le añaden fórmulas, se cierra la frase rota y se le ponen
  citas. **Desbloquea T8** y los `[!todo]` de `2.1.6:166` y `2.3.3:33`. Se descartó fundirla con `A.2`
  porque `2.1.5` es marco teórico y `A.2` es material de consulta: la duplicación aquí es deliberada.
- `2026-08-15` — **La lista de sedes de la formulación canónica del *data snooping* (`:316-317`) estaba
  INCOMPLETA: nombraba SIETE y en disco hay DIEZ.** Detectado al analizar los datos repetidos del
  capítulo 3 (Tanda 10, pieza B, `3fadf13`). Aquella entrada listaba `2.1.6`, `3.3`, `4.3`, `4.6`,
  `5.4`, `6.1` y `A.3`; **faltan `5.0`, `5.1` y `5.2`**. No fue un descuido: **`5.0` no existía cuando
  se escribió** —la creó la Tanda 7— y `5.1`/`5.2` la llevan «cada una en su etapa», que es una forma
  distinta de repetirla y por eso se coló. **La formulación canónica NO se reabre** —la decisión 4 del
  bloque de arriba sigue vigente y es la redacción buena—; lo que se corrige es **el censo de dónde
  vive**. Importa porque **T9 va a recortar el capítulo 3 usando ese censo**: recortar `3.3.4` creyendo
  que quedan seis copias cuando quedan nueve no cambia la acción, pero sí cambia qué se declara como
  sede canónica y cuántas remisiones hay que insertar. **Regla que se deriva:** este censo se cuenta
  contra disco antes de usarlo, como el contador de `[n]`, y no se lee de memoria — es el segundo
  inventario de este proyecto que se queda corto por escribirse una vez y no recontarse.
- `2026-08-17` — **Se reescribió texto previo de este fichero y de `next-steps.md` para quitar la
  virgulilla del «~17» tipos 0-day.** Alcance exacto: **7 ocurrencias** —4 aquí (`:65`, `:153`,
  `:298`, `:299`) y 3 en `next-steps.md`—, donde se sustituyó «~17» por «17». **Lo que sobraba era
  el «~», no el número: 17 es EXACTO** (17 tipos 0-day, 3.750 filas de D2, verificado contra disco).
  **Esto es una reescritura de texto anterior, no una nota añadida**, y se hizo al amparo de una
  **excepción PUNTUAL Y EXPRESA que Francisco concedió el 2026-08-16**, preguntado con las
  alternativas sobre la mesa; pesa sobre la **Decisión 3 de la Fase 0** (que solo autoriza a añadir
  nota fechada aquí) y sobre el hecho de que **`next-steps.md` está CONGELADO**. **La Decisión 3
  sigue vigente para todo lo demás**: la excepción se agota en el dato del «~17» y no autoriza
  ninguna otra corrección en estos dos ficheros. No se tocaron los falsos positivos `~170 MB` de
  `.gitignore` y `README.md`.
- `2026-08-17` — **Reapertura del residuo de T22: el «`n_iter_total_grid` es determinista» queda
  SUPERADO; la banda de wall-clock pasa a magnitud OBSERVADA sin causa atribuida.** Autoriza
  **Francisco**, expresamente, el 2026-08-17. **Nota añadida, no reescritura**: la decisión original
  —su título en `:633`, su cuerpo en `:636` y su eco en la bitácora del `2026-08-09`, `:1154`— **se
  deja intacta y legible**, y esta nota es la que declara qué parte de ella deja de sostenerse.
  **Qué se supera, exactamente:** la afirmación de que el recuento de épocas es **determinista** y,
  con ella, la **atribución** de la banda de wall-clock del Autoencoder (4,8×; también los 1,29× y
  3,63× que cita `:636`) a **carga de máquina**. **Motivo:** los 162 (54) y 128 (122) salen iguales
  solo en las **dos únicas** corridas que registran la columna —`ac496cb` y `1163c90`—, y **ninguna
  de esas dos es una de las dos corridas del contraejemplo de tiempos**, que **no registran épocas**.
  Con n=2 y sin cubrir el contraejemplo, lo medido es **constancia observada**, no determinismo, y la
  banda **no tiene causa establecida**: no se puede afirmar que sea carga de máquina ni descartar que
  las épocas expliquen parte. Ya estaba así en `PIPELINE.md:923-929`, en `4.4` y en `A.3`; lo que
  faltaba era el registro aquí y en el código. **Qué NO cambia:** las columnas de tiempo siguen en
  bloque aparte y **siguen sin citarse como resultado** —eso se sostiene por ser wall-clock en
  máquina no dedicada, sin necesitar la atribución—, y **el eje 54-vs-122 sigue siendo indecidible
  sin medidas repetidas**, que era la consecuencia de diseño de T22 y no depende de la parte
  superada. **Ninguna cifra publicada se mueve.** Sedes de código corregidas en el mismo ciclo:
  `agregar_semillas.py` (comentario de `COLUMNAS_TIEMPO` y `RAZON_BLOQUE_MAQUINA`, que **regenera**
  `Resultados/dispersion_semillas.md`), `anomalias.py` y `config.ALCANCE_N_ITER_TOTAL`.
- `2026-08-17` — **Los recuentos pareados entre semillas los EMITE `agregar_semillas.py`.** Decisión
  de Francisco del 2026-08-17. Dos titulares portantes se contaban **a mano**: el «**8 de 10**»
  (RandomForest supera a HistGradientBoosting en `f1_macro`, pareado por semilla; `5.2:107` lo declara
  «la única formulación que debe usarse al afirmar que un algoritmo es mejor que el otro») y el
  «**40 de 40**» del eje SMOTE vs nada (`5.2:171`, `:181`, marcado con `[!todo]` en `:173`). Pasan a
  salir de un **artefacto nuevo**, `Resultados/comparaciones_pareadas.csv`, más una sección en
  `dispersion_semillas.md`; mismo patrón que el «13 de 98». **Tabla NUEVA y no una de las cuatro
  principales**, por la misma razón que la dispersión: su borrado por variante y su `CLAVE_UNICIDAD`
  sin `semilla` no admiten estas filas. Decisiones de implementación tomadas al hilo, por si hay que
  revisarlas: se emiten **tres** comparaciones (la de firmas y **los dos** ejes de balanceo, para que
  se lean sobre denominadores idénticos), con fila por bloque **y** fila `__global__`; los **empates
  no se reparten** (columna propia); el sentido «mayor es mejor» se **declara** por comparación y no
  se asume; y el total se contrasta contra un `pares_esperados` declarado, de modo que un barrido
  incompleto **aborta** en vez de publicar «8 de 9» rotulado como «de 10». **No se relanza el
  barrido** (2.320 filas ya en disco) y **no se reabre ningún eje**: solo se automatiza el recuento.
  **Aviso de homónimo:** existe otro «8 de 10» que es de **tiempos** de entrenamiento
  (`PIPELINE.md:596-611`); son cifras distintas y no se fusionan. **Estado verificado en disco el
  2026-08-17: el agregador YA se ha relanzado.** `Resultados/comparaciones_pareadas.csv`
  (**13 filas de datos** más cabecera, con `decisiones_no_constantes` entre sus columnas),
  `Resultados/dispersion_semillas.csv` y `Resultados/dispersion_semillas.md` —este último ya con la
  sección nueva de comparaciones pareadas— están escritos con fecha **`2026-08-17T18:56:18`** y sello
  **`commit_agregador = 0276039-sucio`**. Las tres cifras salen del artefacto y coinciden con la
  comprobación previa: **8 de 10** en `122_sin_seleccion`, **8 de 10** en `54`, **16 de 20** global
  (rotulado *(agregado de sus bloques)*), **40 de 40** en SMOTE vs nada, **23-17** en SMOTE vs
  `class_weight`, **cero empates**. El sello va **sucio** porque el código del bloque pareado aún no
  estaba commiteado cuando se corrió el agregador: queda como **re-anclaje pendiente —el sexto del
  proyecto—**, a resolver reanclando el sello a su commit una vez cerrado.

- `2026-08-17` — **El sexto re-anclaje de sello queda HECHO: `0276039-sucio` → `98a0289`.** Nota nueva,
  que **no reescribe** la entrada de arriba: lo que allí se declara «re-anclaje pendiente» ya está
  resuelto, y aquí queda dicho con qué hash. El commit que **sí contiene** el código que produjo
  `comparaciones_pareadas.csv` y la re-escritura de `dispersion_semillas.csv`/`.md` es **`98a0289`**
  («codigo: emitir el "8 de 10" pareado desde agregar_semillas.py y corregir el residuo de T22»), que
  versiona a la vez el cambio de `agregar_semillas.py` y los **tres** artefactos; verificado con
  `git show --stat 98a0289`. `0276039` es el commit **anterior** al cambio y además de track *informe*,
  así que el sello impreso no identifica ninguna versión del código del agregador. **El sello impreso
  dentro de los artefactos NO se ha tocado** —lo estampa `config.commit_actual()` y por construcción no
  puede llevar el hash del commit que lo versiona—: el re-anclaje va **en prosa**, en la tabla canónica
  de corridas de `PIPELINE.md`, en su tabla de las cinco pasadas del agregador, en su recuadro de
  re-anclajes, en la ficha del runbook de `comparaciones_pareadas.csv`, en §1, §6.2 y §7 de
  `GUIA_RESULTADOS.md`, en `A.3` y en la cita de procedencia de `5.2`. Cero corridas, cero `fit`, cero
  cifras movidas. **Sigue vivo el otro re-anclaje pendiente del proyecto**, el de la re-corrida de
  `validacion.py` (`a8c20e9-sucio`), que este ciclo no toca.

**Nota del 2026-08-18 — el re-anclaje de la re-corrida de `validacion.py` YA NO ESTÁ VIVO: quedó
CERRADO por el ciclo de Código del 2026-08-17.** La frase de arriba —«sigue vivo el otro re-anclaje
pendiente del proyecto… (`a8c20e9-sucio`)»— se conserva como historial y no se reescribe, pero
**dejó de ser verdad en presente**. Verificado en disco hoy: el campo `Commit del código:` de los dos
`Resultados/*_validation_report.txt` dice **`ac36b88`**, y la columna `commit` de los dos
`*_vocabulario_onehot.csv` y de los dos `*_composicion_d3.csv` dice lo mismo. **`ac36b88` es un sello
LIMPIO** —sin sufijo `-sucio`—, así que identifica un estado versionado del código y no hay nada que
re-anclar en prosa: es justo lo que el re-anclaje pendiente esperaba. La marca temporal **no se
transcribe aquí**, por la nota del 2026-08-16: se remite al campo `Fecha de la corrida:` de los
informes y a la columna `fecha` de los CSV. `PIPELINE.md`, `GUIA_RESULTADOS.md` y `features.md` sí
recogieron el cambio el 2026-08-17; **este fichero no**, y esa omisión silenciosa es lo que esta nota
repara. **Cero cifras movidas, cero criterios cambiados.**

**Nota del 2026-08-18 — TÍTULO DEL TFG FIJADO por Francisco. La Decisión 6 de la Fase 0 queda
CONSUMIDA.** Título definitivo, literal:

> **Sistema híbrido de detección de intrusiones en red basado en aprendizaje automático: detección de
> anomalías y firmas en cascada sobre NSL-KDD**

- **Quién y cuándo:** lo eligió **Francisco el 2026-08-18**, entre los **5 candidatos** que un agente
  propuso en `00 Preliminares/Resumen.md` durante la **Tanda 27**. Escogió el **candidato 1**, el más
  técnico y completo: nombra **arquitectura** (híbrido en cascada), **técnica** (anomalías + firmas
  con aprendizaje automático) y **dataset** (NSL-KDD).
- **Aplicado ya en tres sedes**, verificadas al registrar esta nota:

| Sede | Dónde | Qué se hizo |
|---|---|---|
| `00 Preliminares/Resumen.md` | `:12` | Título literal; **retirado** el callout con los cinco candidatos |
| `00 Preliminares/Abstract.md` | `:15` | Traducción al inglés del título fijado |
| `00 Índice TFG.md` | `:6` + callout en `:8-12` | **Forma corta** en el encabezado y **título literal declarado debajo** |

- **Por qué la forma corta en el índice:** 20 palabras son ilegibles como `H1`. El encabezado lleva la
  versión corta y el **literal** queda declarado en el callout inmediato, que es de donde el volcado
  al `.docx` debe tomar la **portada**. En las tres sedes se **retiró** el título de trabajo
  «H-NIDS con ML».
- **Estado de la Decisión 6 (Fase 0, 2026-08-14, `:1352`):** decía que **el título quedaba aplazado**
  y que un agente podría **proponer candidatos pero no fijarlo**. Se cumplió exactamente así —el
  agente propuso en la Tanda 27, Francisco eligió hoy—, de modo que **ya no está vigente**. Su texto
  original **no se reescribe**: es la traza de por qué se hizo en dos pasos. Lo mismo aplica a las
  menciones del título como decisión **no delegada** (`:1391`, `:1400`): siguen siendo historial
  correcto, pero **el punto ya está resuelto por su titular**.
- **Por qué importa registrarlo aquí:** hasta esta nota, el único respaldo de que Francisco eligió el
  título era la **autoafirmación de un callout dentro de `Resumen.md`**. Un registro de decisiones
  que no recoge la elección deja la decisión **sin aval fuera de la propia nota** que la afirma.
- **Alcance:** solo se registra. **Cero cifras movidas**, ningún otro fichero tocado desde esta nota
  (el cierre en `features.md` lo hace el pase de cronista).
