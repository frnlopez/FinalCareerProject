# EL_FUTURO.md — Vías de diferenciación del TFG

> Documento **vivo** para acumular ideas de implementación alternativas que eviten "caer en
> lo común". No es objetivo de ninguna sesión concreta rellenarlo: se va nutriendo a medida
> que surjan ideas, y de aquí saldrán las **líneas futuras** de la memoria (cap. Conclusiones)
> y, si alguna madura a tiempo, algún experimento extra.
>
> Origen: comentario del profesor de seguimiento — *"todo el mundo acaba en un Random Forest
> para este dataset"*. El riesgo no es usar RF (es el mejor en las métricas), sino que el
> **proyecto entero** se reduzca a lo que hace todo el mundo y no aporte nada.

---

## 0. Marco: dónde está ya la diferenciación (para no repetirla como "futuro")

Lo que este TFG YA hace distinto del patrón dominante NSL-KDD (~99% accuracy en el split de
train con un RF monolítico):

- **Arquitectura híbrida en cascada** (anomalía → firmas), no un clasificador único.
- **Detección explícita de 0-day**: se mide el recall sobre los ~17 tipos de ataque que NO
  están en el train. El RF monolítico no puede — y `baseline.py` lo demuestra con datos
  (recall 0-day = 0.15, colapso CV→test 0.909→0.47).
- **Evaluación honesta sobre el test completo** con recall 0-day por tipo, no accuracy sobre
  el train-split (que es de donde sale el "99% de todo el mundo").

> Esto es lo que ya te separa del común. El resto del documento son formas de **subir la
> apuesta**.

---

## 1. Ideas — etapa 2 (firmas), más allá del RF

- **Inducción de reglas legibles (RIPPER / OneR)** — la etapa de firmas es, conceptualmente,
  un "IDS clásico basado en reglas". Un `RandomForest` es una caja negra que traiciona ese
  espíritu; el `export_text` del DecisionTree ya apunta ahí. Llevarlo más lejos con un
  algoritmo de inducción de reglas real (p. ej. `wittgenstein` → RIPPER) produce firmas
  humanas del tipo `if flag_S0 and srv_serror_rate>0.8 → dos(neptune)`. **Aporta
  interpretabilidad de verdad**, que es justo lo que un NIDS de firmas debe tener y lo que un
  RF no da. Buen candidato a experimento comparativo (RF preciso vs reglas interpretables).
- **Aprendizaje sensible al coste** para r2l/u2r en lugar de SMOTE genérico: penalizar más el
  fallo en las clases raras de alto impacto (u2r = escalada de privilegios) que en dos/probe.
- **Detectores especializados por familia** (one-vs-rest con un modelo afinado por clase) en
  vez de un multiclase único — permite optimizar el recall de u2r sin sacrificar dos.

## 2. Ideas — arquitectura / fusión

- **★ Ensemble de detectores de anomalías (etapa 1)** — **la línea futura nº1, respaldada con
  datos de `hibrido.py` (2026-07-15).** Ningún detector domina por tipo: son complementarios.
  Sobre el MISMO set de 54 features, el Autoencoder (elegido por AUC-ROC global) tiene puntos
  ciegos TOTALES que otro detector cubre bien:
  - `mailbomb` (n=293): Autoencoder **0.00**, IsolationForest 0.01, OneClassSVM 0.02 — pero
    **LocalOutlierFactor 0.82**.
  - `snmpguess` (n=331): Autoencoder **0.02**, OCSVM 0.01 — pero **IsolationForest 0.74**.

  Elegir "el mejor detector por AUC global" (H-2) deja recall 0-day sobre la mesa. Un ensemble
  (OR de sospechas, voto, o max-score normalizado) subiría el recall 0-day global por encima de
  cualquier detector individual, a costa de más FPR — trade-off a cuantificar. Es un experimento
  acotado (los 4 modelos YA están entrenados y persistidos; solo hay que combinar sus salidas)
  y responde con datos a "¿por qué un solo detector?". Fuerte candidato incluso para ESTA entrega.
- **Reconocimiento de conjunto abierto (open-set recognition)** — respaldado con datos: con
  `UMBRAL_CONF=0.5`, de los 0-day que la etapa 1 SÍ caza, **solo el 13.4% se enrutan a `unknown`**;
  el ~86% restante el RandomForest los mal-etiqueta con confianza como categoría conocida (probas
  altas fuera de distribución). Formalizar el "unknown/0-day" con teoría real (distancia al espacio
  de clases conocidas, OpenMax-style) en lugar del `UMBRAL_CONF` ad-hoc sobre `predict_proba`
  atacaría directamente ese 86%. Eleva el 0-day de "heurística" a "método".
- **Fusión por meta-clasificador (stacking)** en vez de cascada dura: un modelo que combine
  `anomaly_score` + `predict_proba` de firmas. Comparar cascada vs fusión responde una
  pregunta de diseño legítima y da una tabla comparativa propia.

## 3. Ideas — representación / features

- **Espacio latente del autoencoder como entrada de la etapa 2**: en vez de las 54 features
  crudas, alimentar firmas con la representación aprendida por el detector de anomalías. Une
  las dos etapas conceptualmente (una sola representación) y es un experimento acotado.
- **Selección de features vía SHAP** en lugar de importancias de RF (menos sesgada hacia
  variables de alta cardinalidad).
- **Sets de features por etapa (opción B de Q1/C)** — respaldado con datos (`hibrido.py`,
  2026-07-15). La selección supervisada de 54 (importancias RF sobre D1+D3) **ciega un poco al
  detector no supervisado**: con las 122 completas el Autoencoder es marginalmente mejor en la
  tarea pura de anomalías (AUC-ROC 0.947 vs 0.929; recall 0-day 0.785 vs 0.771 a FPR menor,
  0.085 vs 0.102 — Pareto). Pero las 122 estropean la etapa 2 (RF sobreajusta los dummies extra
  de D3: `conocida f1_macro` 0.655 vs 0.748). El sistema se cerró en **54 para ambas etapas
  (opción A)** porque el efecto en el detector es pequeño y no mueve la tesis. La opción B —**122
  para anomalías, 54 para firmas**— es la vía "correcta" pendiente: exige que la cascada cargue
  las dos representaciones de X en paralelo (mismas filas, distintas columnas). Ganancia esperada
  pequeña pero defendible como refinamiento. Dato a favor (fe de erratas 2026-07-16 en
  `resumen-de-decisiones.md`): con 122 el Autoencoder saca a `mailbomb` de cero (0.00 → 0.123,
  36/293) — la selección supervisada le costó al detector un tipo 0-day entero, aunque siga
  esencialmente fallado; el grueso de mailbomb solo lo caza LOF (0.82) → combina con el ensemble (§2).

## 4. Ideas — evaluación / generalización

- **Generalización cruzada de dataset**: entrenar en NSL-KDD y evaluar en otro (CIC-IDS2017 /
  UNSW-NB15). Es la prueba de fuego que casi nadie hace y la que de verdad distingue un TFG.
  Coste alto (re-mapeo de features), candidato claro a "línea futura" más que a esta entrega.
- **Análisis de deriva (concept drift)** D1→D2 ya asomó (el FPR real ~8-10% en vez de ~5%);
  cuantificarlo y discutirlo es material propio poco explotado en la literatura NSL-KDD.
- **Punto ciego universal por limitación de features (a documentar, no "resolver")**:
  `snmpgetattack` (n=178) lo fallan los **4** detectores en ambos sets (recall máx ~0.15). Son
  ataques SNMP/volumétricos que apenas perturban las features por-flujo de NSL-KDD → es un
  límite del **dataset/representación**, no de los modelos. Un análisis de qué familias de
  ataque son intrínsecamente indetectables con features por-flujo (vs las que necesitarían
  features de secuencia/temporales) es discusión honesta y poco común en la literatura.

---

## Bitácora

- `2026-07-14` — Creado. Semillas iniciales sembradas (secciones 1-4) a raíz del comentario
  del profesor durante el grill de `hibrido.py`. Pendiente de que el autor lo vaya nutriendo.
- `2026-07-15` — **Nutrido con hallazgos empíricos de la ejecución de `hibrido.py`** (54 y 122).
  Tres líneas ahora respaldadas con datos, no solo intuición: (1) **ensemble de detectores** —
  ★ nº1, la complementariedad por tipo es medible (LOF cubre `mailbomb`, IF cubre `snmpguess`,
  el AE los falla) y los 4 modelos ya están entrenados; (2) **open-set recognition** — el 86% de
  los 0-day cazados se mal-etiquetan como conocidos; (3) **sets por etapa (opción B)** — las 122
  dan mejor detector pero peor firma. Añadido el punto ciego universal `snmpgetattack` (límite de
  features, no de modelo).
