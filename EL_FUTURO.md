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
  - **Salvaguarda metodológica que hay que aplicar al montar el ensemble (aviso de TabArena).** No
    es una objeción a la línea: es la condición bajo la que su ganancia será real y no un espejismo.
    El *benchmark* TabArena documenta que algunos modelos aparecen **sobrerrepresentados** en los
    conjuntos entre modelos por **sobreajuste al conjunto de validación**: si los miembros se
    escogen mirando la misma partición con la que se mide, entra el que mejor se ajusta a esa
    partición, no el que mejor generaliza [62]. Traducido
    a este pipeline, el riesgo concreto es elegir qué detectores entran en el conjunto —o con qué
    pesos— **mirando `D1_val` o los pliegues OOF de D3**: la mejora se vería en esa medición y no se
    reproduciría en D2. La defensa correcta es la disciplina que el sistema **ya tiene** (`D1_val`
    se usa solo para fijar el percentil 95, la calibración de `UMBRAL_CONF` es *out-of-fold* sobre
    D3 y no ve D2, P-4); el peligro es diluirla al añadir un criterio de selección más. Regla
    práctica para el experimento: fijar la regla de combinación **a priori** (p. ej. OR de sospechas
    o max-score normalizado, sin pesos ajustados), y si se ajustan pesos, hacerlo sobre una
    partición reservada distinta de la que después reporte el resultado.
- **Cerrar el bucle: generación automática de firmas a partir de los `unknown`** — es la respuesta
  que la literatura ya publicó a la pregunta que este TFG deja abierta: **qué hacer con un
  `unknown` una vez detectado**. Hoy el sistema termina en la etiqueta: la etapa 2 marca `unknown`
  y ahí se acaba el recorrido; nada realimenta a la base de firmas. Hwang, Cai, Chen y Qin (2007)
  proponen un H-IDS que **no es serie ni paralelo, sino un bucle**: el detector de anomalías mina
  episodios de tráfico anómalo, un esquema de **generación de firmas ponderadas** extrae firmas de
  esos episodios y las **inserta en la base de datos de SNORT**, de modo que lo desconocido de hoy
  es firma conocida mañana [65]. Reportan
  60 % de detección frente al 30 % de SNORT y el 22 % de Bro con <3 % de falsas alarmas, y una
  mejora del 33 % sobre SNORT atribuida a las firmas generadas por el módulo de anomalías.
  - **Encaje con este sistema:** la pieza que faltaría es un minero de patrones sobre el subconjunto
    etiquetado `unknown` en D2 que produjera reglas candidatas en el mismo formato legible que ya
    emite `firmas.py` (`export_text` del DecisionTree, `firmas_rules.txt`), realimentando la etapa 2.
    Conecta de forma natural con la inducción de reglas RIPPER/OneR de la §1.
  - **Por qué es línea futura y no entrega:** exige un criterio de validación de la firma generada
    (una firma automática mal inducida es un generador de falsos positivos permanente) y un
    protocolo de realimentación que, tal como está el proyecto, **tocaría D2**, que es solo de
    reporte (P-4). Es decir, no cabe sin cambiar el protocolo de evaluación.
  - **Formulación defendible para 6.2 / 6.1:** que el sistema no cierre el bucle es un **límite
    consciente de alcance**, no un descuido; conviene nombrarlo así y citar a Hwang et al. como la
    vía publicada por la que se cerraría.
  > [!warning] Verificación pendiente — sin acceso al texto completo
  > Las cifras de Hwang et al. 2007 (60 % / 30 % / 22 %, <3 % de falsas alarmas, +33 % sobre SNORT)
  > proceden **solo del resumen**; el texto completo está tras muro de pago y el proyecto no tiene
  > acceso institucional. Antes de llevarlas a la memoria hay que comprobar en el texto completo
  > sobre qué tráfico se miden y con qué definición de «tasa de detección». Si no se logra acceso,
  > citar el mecanismo (el bucle de realimentación) **sin las cifras**.
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

- **★ Vector de error de reconstrucción por característica como entrada extra de la etapa 2** — la
  variante *buena* de la idea de "unir las dos etapas por la representación", y la única de este
  bloque que **podría subir el recall 0-day conservando reglas legibles**. Hoy el *score* de anomalía
  del Autoencoder es el **MSE de reconstrucción agregado** (`anomalias.py:216-218`): un único número
  que resume 54 errores, uno por característica. La propuesta es no agregarlo: tomar el vector de 54
  errores `err_i = (x_i − x̂_i)²` y **concatenarlo a las 54 features originales** como entrada de la
  etapa de firmas. Tres propiedades lo hacen preferible al espacio latente:
  1. **Es interpretable por construcción.** Cada componente hereda el nombre de una característica
     real, así que una regla del tipo `if err_num_shells alto → u2r` **sigue siendo una firma
     legible**. El latente de 32 dimensiones, en cambio, no tiene nombres: cualquier regla que lo
     use es opaca y traiciona el espíritu de la etapa de firmas.
  2. **Conserva justo la información que discrimina.** Un error de reconstrucción grande en una
     componente significa literalmente «este valor no se parece a nada de D1». Esa es la señal de
     ataque, y llega a la etapa 2 **localizada** en qué característica se produjo, no promediada.
  3. **Es la unión conceptual entre etapas, por el lado correcto.** La etapa 2 recibe *en qué* se
     equivocó la etapa 1, no *qué comprimió* la etapa 1.
  Es el candidato con mejor relación coste/aporte del lote: **cero dependencias nuevas** (el
  autoencoder ya está entrenado y persistido; solo hay que exponer el error por componente antes de
  agregarlo) y coste bajo-medio, casi todo de fontanería en el paso de la cascada. Razón de fondo
  para esperar efecto en 0-day: un 0-day es, por definición, algo que el detector **no sabe
  reconstruir**, así que el error por característica es la señal más directa de "no visto" que el
  sistema produce y hoy se está tirando al agregarla.
  - **Qué habría que medir para que cuente**: `f1_macro` de la etapa 2 con y sin el vector extra,
    recall 0-day por tipo, **y además** cuántas de las reglas extraídas usan componentes `err_*` —
    si el árbol las ignora, la línea no aporta; si las usa, hay que comprobar que la regla resultante
    sigue siendo legible.
  - Aplica aquí la misma salvaguarda de TabArena anotada en la §2: si se decide **qué componentes
    `err_*` entran** mirando `D1_val` o los pliegues OOF de D3, la ganancia no se reproducirá en D2.
    Lo limpio es entrar con las 54 componentes o con ninguna, y dejar que el RF decida por
    importancia.
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
  - **Anotación a favor de la opción B, que NO reabre Q1/C.** Que quede dicho antes que nada: la
    decisión Q1/C —**54 características para ambas etapas, opción A**
    (`resumen-de-decisiones.md:373-389`)— **sigue siendo correcta y no se reabre aquí**. Se tomó
    sobre codificación **one-hot**, que es la que el pipeline usa, y con la evidencia disponible
    entonces; nada de lo que sigue la desmiente. Lo que se añade es **una razón nueva a favor de la
    opción B**, para el día en que alguien decida moverla: si alguna vez se quisiera cambiar la
    codificación de las categóricas de alta cardinalidad —el caso obvio es `service`, que genera 70
    de los 84 *dummies*— por un ***target encoding***, la opción A **lo bloquea por construcción**.
    El razonamiento es estructural, no empírico:
    - El *target encoding* sustituye cada categoría por un estadístico del **destino** (la etiqueta)
      condicionado a esa categoría. Necesita, por tanto, **un destino con más de un valor** sobre el
      que ajustarse.
    - La etapa 1 se entrena sobre **D1, que es de una sola clase** (solo tráfico normal). Ahí no hay
      destino que codificar: el estadístico sería constante y la transformación, vacía.
    - Bajo la opción A las dos etapas comparten **un único conjunto de características**, luego una
      codificación válida para la etapa 2 (supervisada, 5 clases sobre D3) tendría que serlo también
      para la etapa 1. Solo hay dos salidas, ambas malas: renunciar al *target encoding*, o ajustarlo
      con las etiquetas de D3 e inyectar así **sesgo supervisado en un detector que debe ser
      no supervisado** (y, de paso, contaminarlo con información de ataques).
    - Bajo la **opción B** —sets distintos por etapa— el conflicto desaparece: la etapa 1 se queda
      con su representación sin supervisar y la etapa 2 puede usar la codificación que le convenga.
    En términos de lo que ya dice esta misma línea: la opción B no solo era «la vía correcta
    pendiente» por el dato del Autoencoder con 122; es también **la precondición** de cualquier
    experimento futuro sobre la codificación de categóricas. Decidir si eso mueve algo es de
    Francisco; esta entrada solo lo deja anotado. [63], [64]

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
- `2026-08-15` — **Nutrido desde los informes de `99 Investigación/`** (T13). Tres entradas nuevas y
  una anotación:
  1. **★ Vector de error de reconstrucción por característica** como entrada extra de la etapa 2
     (§3) — nueva ★, procedente de
     [[clasificadores-tabulares-y-arquitecturas-hibridas]] §2b: la única vía identificada que podría
     mejorar el recall 0-day **sin perder reglas legibles**, y con cero dependencias nuevas.
  2. **Salvaguarda de TabArena** sobre sobreajuste al conjunto de validación, pegada a la ★ nº 1
     (§2) — protege la línea del ensemble fijando cómo elegir sus miembros; no la debilita.
  3. **Bucle de generación automática de firmas de Hwang et al. 2007** (§2) — la respuesta publicada
     a «¿qué hago con un `unknown`?», que hoy el sistema deja abierta al terminar en la etiqueta.
     Fuente **solo por resumen**: sus cifras quedan marcadas como verificación pendiente.
  4. **Anotación (no reapertura) sobre Q1/C** en la línea de la opción B (§3): el *target encoding*
     es estructuralmente incompatible con la opción A porque la etapa 1 no tiene destino sobre el
     que ajustarlo. **La decisión Q1/C sigue vigente y correcta**; esto solo suma un argumento a
     favor de la opción B.
