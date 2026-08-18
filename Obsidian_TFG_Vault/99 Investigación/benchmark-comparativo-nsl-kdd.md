---
titulo: "¿Qué significa «definir un benchmark» para este TFG, y cuál de las dos acepciones le sirve?"
numero: "-"
estado: informe
docx_ref: "-"
---

# ¿Qué significa «definir un benchmark» para este TFG, y cuál de las dos acepciones le sirve?

- **Encargo:** investigar las dos acepciones de «definir un benchmark» — (a) situar las cifras del TFG frente a lo publicado sobre NSL-KDD, y (b) fijar un protocolo interno de comparación justa entre variantes del propio sistema — y cerrar con un pronunciamiento razonado sobre cuál adoptar, en qué orden y con qué reparto entre capítulos.
- **Fecha:** 2026-08-02
- **Alcance.** **Entra:** criterios de comparabilidad de cifras publicadas sobre NSL-KDD y su aplicación; formalización de protocolos de evaluación en la literatura (reproducibilidad en ML, model cards, checklists, protocolos de benchmarking de NIDS); evaluación de `app/evaluacion.py` como base del protocolo interno. **Queda fuera:** alternativas de modelado y taxonomía de arquitecturas H-NIDS ajenas (van a `clasificadores-tabulares-y-arquitecturas-hibridas.md` y `arquitecturas-hibridas-en-la-literatura.md`); ejecutar nada; proponer cambios de código — el track de código está cerrado desde el 2026-07-16, así que lo que el protocolo exigiría se describe como **requisito**, no como tarea.
- **Alimenta a:** [[5.3 Resultados del sistema híbrido]] y [[05 Evaluación/5.4 Conclusiones del capítulo|5.4 Conclusiones del capítulo]]; la parte (b) alimenta además a [[3.3 Metodología de funcionamiento del sistema]] y a las limitaciones de [[6.1 Conclusiones]].

## Respuesta corta

Son dos cosas distintas y ninguna sustituye a la otra, pero **no valen lo mismo para este TFG**. La acepción (b) —protocolo interno— es la que sostiene el trabajo: ya está tomada en decisiones dispersas (Q4, Q6, H-1…H-7, P-1…P-5) y solo falta **escribirla junta y respaldarla con literatura citable**; el coste es casi nulo y el retorno es la justificación metodológica del capítulo 3. La acepción (a) —comparación hacia fuera— es imprescindible para el tribunal pero **rinde sobre todo un resultado negativo**: al aplicar un filtro de comparabilidad honesto, la inmensa mayoría de las cifras publicadas sobre NSL-KDD se cae, y las que sobreviven son poquísimas. Recomendación: **adoptar (b) primero y completa, y (a) en versión reducida** — criterios explícitos, dos o tres referencias supervivientes y el porcentaje de descarte documentado como material de discusión, **nunca una tabla grande de *accuracies***.

## Hallazgos

### Parte A — Benchmark hacia fuera

#### A.1 · El «99 % que saca todo el mundo» tiene fuente primaria, y es el propio paper del dataset

El comentario del profesor de seguimiento que originó `EL_FUTURO.md` no necesita apoyarse en una impresión: está escrito, literalmente, en el artículo que creó NSL-KDD. Tavallaee et al. observan que

> «in many papers, random parts of the KDD train set are used as test sets. As a result, they achieve about 98% classification rate applying very simple machine learning methods»

y añaden el corolario que interesa aquí:

> «Even applying the KDD test set will result in having a minimum classification rate of 86%, which makes the comparison of IDSs quite difficult since they all vary in the range of 86% to 100%»

([Tavallaee et al., 2009, §I](https://www.ee.torontomu.ca/~bagheri/papers/cisda.pdf), 2009) — nivel 1.

Esto es un hallazgo de peso para la memoria: la crítica al patrón dominante **no es una opinión del autor del TFG**, es la motivación declarada del dataset que el TFG usa. Y el segundo fragmento dice algo más incómodo y más útil: incluso usando el test correcto, el rango útil de discriminación es estrecho (86-100 %), de modo que **una diferencia de dos puntos de *accuracy* entre dos sistemas no significa gran cosa**. Es un argumento directo a favor de no jugar la tesis a la *accuracy*.

#### A.2 · Las unidades de comparación, verificadas en la fuente primaria

Del mismo artículo, verificado sobre el PDF (no sobre resúmenes de terceros):

| Fichero | Registros | Qué es |
|---|---|---|
| KDDTrain+ | 125.973 | Muestreo sin duplicados del train de KDD'99 |
| KDDTest+ | 22.544 | Muestreo sin duplicados del test de KDD'99 |
| KDDTest-21 | 11.850 | KDDTest+ **menos** todos los registros que los 21 clasificadores acertaron |

> [!warning] Corrección de un error que circula
> KDDTest-21 **no** es «el subconjunto con 21 tipos de ataque». Es el subconjunto de dificultad alta: los autores etiquetaron cada registro con un `#successfulPrediction` ∈ [0, 21] usando **21 máquinas aprendidas (7 algoritmos × 3 entrenamientos)** y generaron KDDTest-21 excluyendo los registros que **todas** acertaron. La lectura errónea («21 tipos de ataque») me la devolvió un resumen automático del propio PDF y solo se cae al leer el original; conviene no propagarla en la memoria.

Dato relevante para este TFG: **D2 tiene 22.544 registros** (`metricas_baseline.csv`, columna `n_test`), es decir, D2 **es** KDDTest+ completo. El proyecto ya está en la partición correcta; ese es el requisito de entrada a cualquier comparación externa y buena parte de la literatura no lo cumple.

Un matiz que importa y que casi nunca se cita: los **baselines canónicos del propio paper** no se entrenaron sobre KDDTrain+ entero, sino sobre **el primer 20 % de sus registros** («we employed the first 20% of the records in KDDTrain+ as the train set»). Incluso la referencia más canónica del dataset tiene un protocolo de entrenamiento que hay que declarar al citarla.

#### A.3 · Criterios de comparabilidad (el entregable real de esta parte)

Una cifra publicada sobre NSL-KDD es comparable con las de este proyecto **solo si** cumple todo lo siguiente. Cada criterio está respaldado por literatura, no por preferencia:

| # | Criterio | Por qué, y qué descarta |
|---|---|---|
| **C1** | **Partición de evaluación = KDDTest+ completo** | Es la única partición que contiene los tipos ausentes del entrenamiento. Descarta: *split* interno de KDDTrain+, validación cruzada sobre KDDTrain+, muestreos propios y KDDTest-21 (comparable consigo mismo, no con D2). Fuente del problema: Tavallaee et al., 2009 |
| **C2** | **Partición de entrenamiento declarada** | Sin saber si se entrenó con KDDTrain+ entero, con el 20 %, o mezclando ficheros, la cifra no es reproducible. Corresponde al ítem «sample allocation» del checklist de reproducibilidad ([Pineau et al., 2021](https://www.jmlr.org/papers/v22/20-303.html)) |
| **C3** | **Granularidad de etiqueta declarada** (binaria, 5 clases) | Una *accuracy* binaria y una de 5 clases no se comparan. Los esquemas de 23 o 40 clases tampoco cruzan con ninguno de los dos |
| **C4** | **Punto de operación declarado: FPR o especificidad junto al recall** | Un recall sin su tasa de falsas alarmas no dice nada en detección: es el pitfall P7 (*Inappropriate Performance Measures*) y P8 (*Base Rate Fallacy*) de [Arp et al., 2022](https://www.usenix.org/conference/usenixsecurity22/presentation/arp). NIST SP 800-94 lo dice en términos operativos: ajustar un IDPS es *cambiar* falsos negativos por falsos positivos, así que un punto sin el otro no describe el sistema |
| **C5** | **Preprocesado sin fuga**: *one-hot*, escalado y selección ajustados solo con datos de entrenamiento | Pitfalls P3 (*Data Snooping*) y P5 (*Biased Parameter Selection*) de Arp et al.; taxonomía de fugas de [Kapoor y Narayanan, 2023](https://www.cell.com/patterns/fulltext/S2666-3899(23)00159-9) |
| **C6** | **Métrica con alcance declarado** | Una *accuracy* global solo contrasta con otra *accuracy* global. Para el 0-day hace falta desglose por tipo |
| **C7** | *(solo para afirmaciones de 0-day)* **Definición de 0-day = tipos presentes en KDDTest+ y ausentes de KDDTrain+** | Si el trabajo «simula» un 0-day apartando una clase del entrenamiento, está midiendo otra cosa. Ver A.5 |

**Regla derivada, y es la importante:** una cifra que incumpla C1, C3 o C4 **no entra en la tabla con una nota al pie — se descarta**. Meterla anotada da la apariencia de comparación donde no la hay, que es exactamente el error que Arp et al. documentan como endémico.

#### A.4 · Qué sobrevive al filtro, y en qué proporción

Revisé **16 fuentes** con cifras sobre NSL-KDD que emergieron de las búsquedas (artículos primarios y cifras citadas de segunda mano dentro de ellos). El resultado:

| Situación | N | Fuentes |
|---|---|---|
| **Verificadas en origen y comparables** | **2** | Tavallaee et al. 2009 (completa); Hindy et al. 2020 (parcial, ver A.5) |
| Conocidas solo de segunda mano (citadas dentro de otro paper, sin protocolo declarado) | 6 | Gharib et al. (90,17 % KDDTest+), *denoising AE* (88,28/88,65 %), Kunang et al. (86,96 %), Kherlenchimeg y Nakaya (80 %), Shaikh y Shashikala (94,3 %), Shone et al. — todas vía Hindy et al., 2020 |
| Inaccesibles para verificar (muro de pago o bloqueo antibot) | 2 | Yin et al. 2017 (IEEE Access); MDPI *Algorithms* 18(12):749 |
| Preprints sin protocolo verificado (nivel 2), no usados | 6 | Varios arXiv sobre NSL-KDD surgidos en las búsquedas |

**Proporción de descarte: 14 de 16 (≈ 87 %).** Con la advertencia honesta de que **esto es una muestra acotada de búsqueda web, no una revisión sistemática**: el porcentaje ilustra la magnitud del problema, no la mide.

Para el dato *medido* —que es el que debe ir a la memoria— hay una fuente mucho mejor que mi propio conteo. Goldschmidt y Chudá hacen una revisión sistemática de los datasets usados en la investigación NIDS **de primer nivel** (2020-2023, solo congresos CORE A*/A) y encuentran que

> «NSL-KDD was used only three times, whereas KDD99 only once, contradicting other surveys»

([Goldschmidt y Chudá, 2025, §5.4](https://arxiv.org/pdf/2502.06688), 2025) — nivel 1.

Es decir: **NSL-KDD ha desaparecido prácticamente de los venues de primer nivel**. Eso explica por qué la literatura de NSL-KDD que uno encuentra está concentrada en revistas y congresos de calidad heterogénea, y convierte el nivel de fiabilidad de cada fuente en parte del argumento, no en un adorno. La misma revisión aporta un dato que juega **a favor** de la elección del proyecto: solo el 23 % de los datasets NIDS (16 % desde 2020) traen partición train/test predefinida, y su ausencia es «*prone to biased evaluations and selective reporting*». NSL-KDD sí la trae — y este TFG la respeta.

Complementa Di Mauro et al., que al revisar la literatura de NIDS neuronal califican explícitamente de «*non-homogeneous*» las comparaciones entre técnicas de familias distintas, «*thus, hardly comparable*» ([Di Mauro et al., 2020](https://doi.org/10.1109/TNSM.2020.3024225), 2020) — nivel 1.

#### A.5 · La comparación que sí se sostiene

**Comparables (C1-C6).** Baselines canónicos sobre KDDTest+ del paper del dataset, entrenados sobre el primer 20 % de KDDTrain+:

| Clasificador (Tavallaee et al., 2009, Fig. 4) | Accuracy KDDTest+ | Accuracy KDDTest-21 (Fig. 5) |
|---|---|---|
| NBTree | 82,02 % | 66,16 % |
| Random Tree | 81,59 % | 58,51 % |
| J48 | 81,05 % | 63,97 % |
| Random Forest | 80,67 % | 63,26 % |
| MLP | 77,41 % | 57,34 % |
| Naïve Bayes | 76,56 % | 55,77 % |
| SVM | 69,53 % | 42,29 % |

Frente a ellos, la cifra homóloga de este proyecto, leída de `Resultados\metricas_hibrido.csv` (fila `set_features=54`): el híbrido Autoencoder→RandomForest da **`bin_accuracy` = 0,8605** sobre D2, con `bin_fpr` = 0,1017 y `bin_recall` = 0,8318. Está **por encima del mejor baseline canónico** (NBTree, 82,02 %), en la misma partición y en la misma tarea binaria.

> [!warning] Dos reservas que hay que declarar al usar esta tabla
> 1. **La granularidad de etiqueta de los baselines canónicos no está declarada en el artículo.** El paper habla de «accuracy rate of the classifiers» sin decir si es binaria o multiclase; el contexto («most of the anomaly detection systems work with binary labels, i.e., anomalous and normal») **sugiere** binaria, pero es una inferencia mía, no un dato verificado. Es decir: ni siquiera la referencia canónica satisface C3 de forma limpia. Vale la pena decirlo en la memoria — refuerza la tesis del apartado.
> 2. Los baselines se entrenaron con el 20 % de KDDTrain+; este proyecto entrena la etapa 2 con D3 (ataques conocidos de KDDTrain+) y la etapa 1 con D1 (normal). No son el mismo presupuesto de datos.

**Comparable solo parcialmente: el único trabajo hermano en 0-day que encontré verificable.** Hindy et al. proponen un autoencoder para detección de 0-day sobre NSL-KDD y CICIDS2017, con One-Class SVM como baseline — la misma pareja de la etapa 1 de este TFG ([Hindy et al., 2020](https://www.mdpi.com/2079-9292/9/10/1684), 2020) — nivel 1. Reportan «*a zero-day detection accuracy of 89–99% for the NSL-KDD dataset*». Sus números sobre KDDTest+ (Tabla 3, umbral 0,25): Normal 84,42 %, DoS 94,67 %, Probe 100 %, R2L 96,5 %, U2R 89,19 %.

**No se puede poner ese 89-99 % al lado del 0,771 de este proyecto.** Incumple C7, y no es un tecnicismo:

- Su «0-day» es **toda clase de ataque**, porque el detector es *one-class* y nunca vio ataques. El de este TFG son los **17 tipos concretos presentes en KDDTest+ y ausentes del entrenamiento** (`apache2`, `httptunnel`, `mailbomb`, `mscan`, `named`, `processtable`, `ps`, `saint`, `sendmail`, `snmpgetattack`, `snmpguess`, `sqlattack`, `udpstorm`, `worm`, `xlock`, `xsnoop`, `xterm`; n = 3.750, contados en `metricas_hibrido_0day.csv`).
- **Agrupan ataques de KDDTrain+ y de KDDTest+** en la evaluación («attacks in both the KDDTrain+ and KDDTest+ files are used in order to evaluate the model»), de modo que sus categorías mezclan tipos conocidos y novedosos.
- Reportan un **barrido de umbral** (0,3 / 0,25 / 0,2) sin fijar un punto de operación, con especificidad sobre normal entre 84,42 % y 84,82 % en KDDTest+ (FPR ≈ 15 %) y hasta 78,81 % en validación (FPR ≈ 21 %). Este proyecto opera a **FPR 0,1017**, sensiblemente más bajo.

Lo que **sí** es comparable, y es valioso, es la forma: Hindy et al. son un precedente publicado y de nivel 1 de que **el desglose por clase es la manera correcta de reportar un detector de 0-day**, y de que un autoencoder supera a un One-Class SVM en esa tarea — que es exactamente lo que `metricas_anomalias.csv` mide en este proyecto (AE `roc_auc` 0,9288 vs OCSVM 0,8360 sobre 54 características). Se cita por el método y por el contraste AE/OCSVM, no por el número.

**Y el hueco sigue abierto.** No encontré ningún trabajo verificable que reporte **recall por tipo de ataque sobre los 17 tipos genuinamente ausentes de KDDTrain+, evaluado sobre KDDTest+ completo y con FPR declarado**. Esa combinación —que es lo que produce `metricas_hibrido_0day.csv`— es la seña de identidad defendible del TFG. La afirmación honesta para la memoria no es «nadie lo hace» (no lo puedo demostrar), sino «**no lo he encontrado en la literatura revisada, y la revisión sistemática de Goldschmidt y Chudá explica por qué es difícil que exista**».

### Parte B — Benchmark hacia dentro

#### B.1 · Cómo formaliza la literatura un protocolo de evaluación, y qué le pide a este

No hay un estándar único para «protocolo de benchmarking de NIDS»; lo que hay son cuatro tradiciones que convergen y que, juntas, dan una plantilla citable.

**(i) Los pitfalls de seguridad — Arp et al., 2022.** Diez trampas agrupadas por fase del flujo de trabajo de ML, sobre una revisión de 30 artículos de ACM CCS, IEEE S&P, USENIX Security y NDSS de la década anterior. El dato que hay que citar es demoledor y verbatim: «*each paper suffers from at least three pitfalls; even worse, several pitfalls affect most of the papers*». Los diez: P1 *Sampling Bias*, P2 *Label Inaccuracy*, P3 *Data Snooping*, P4 *Spurious Correlations*, P5 *Biased Parameter Selection*, P6 *Inappropriate Baseline*, P7 *Inappropriate Performance Measures*, P8 *Base Rate Fallacy*, P9 *Lab-Only Evaluation*, P10 *Inappropriate Threat Model*.

**El hallazgo aquí es que las decisiones ya cerradas del proyecto responden una a una a los pitfalls relevantes.** Esto no es una coincidencia que haya que celebrar: es prosa lista para el capítulo 3, y le da nombre y cita a lo que hoy son decisiones internas sin respaldo bibliográfico.

| Pitfall (Arp et al., 2022) | Qué exige | Qué ya hace este TFG |
|---|---|---|
| **P3 · Data Snooping** | Aislar el test desde el principio | D2 no se toca; la calibración recibe **solo D3** en su firma (P-4: separación estructural, no disciplina) |
| **P5 · Biased Parameter Selection** — «*the detection threshold for a NIDS may be chosen using a ROC curve obtained on the test set*» | El umbral no se elige mirando el test | Línea roja de H-4: `UMBRAL_CONF` se elige por la regla de presupuesto τ=2 pp sobre probabilidades OOF de D3; el umbral p95 se fija sobre el 20 % de D1 reservado. D2 solo reporta |
| **P6 · Inappropriate Baseline** — «*simple models should also be considered*» | Comparar contra un baseline no trivial | `baseline.py`: RandomForest monolítico, que además **es** el patrón dominante de la literatura |
| **P7 · Inappropriate Performance Measures** | No un valor único; precision/recall y curvas PR en clases raras | H-6 prohíbe el número único; `evaluacion.py` calcula PR-AUC además de ROC-AUC |
| **P8 · Base Rate Fallacy** | No interpretar métricas ignorando el desbalanceo | Desglose por clase obligatorio; u2r (**37 muestras de tipo conocido en D2**, ver la corrección de abajo) se reporta aparte y no se esconde en el macro |

> [!warning] Corrección verificada contra disco el 2026-08-18 — «37 muestras en D2» era una cifra mal etiquetada
> El **37 es correcto como número, pero no es «el u2r de D2»**: es el `soporte_u2r` de
> `Resultados/metricas_firmas.csv`, cuyo alcance declarado en la propia columna es «los ataques de
> **D2 de tipo conocido**» (9.083 flujos). Los u2r **0-day** de D2 son otros **163** —`httptunnel` 133,
> `ps` 15, `xterm` 13 y `sqlattack` 2, listados en
> `Resultados/specialized_nsl_kdd_validation_report.txt`—, de modo que **D2 contiene 200 u2r en total**
> y solo 37 llegan a la etapa de firmas. La diferencia no es cosmética: 37 es el denominador del
> `f1_u2r`, y 200 el del recall 0-day. **No confundirlos.** (Recordatorio aparte: en D3, u2r son **52**,
> según `specialized_nsl_kdd_composicion_d3.csv`.)

Los dos pitfalls que este TFG **no** cubre son P9 (*Lab-Only Evaluation*) y P10 (*Inappropriate Threat Model*): no hay despliegue real ni adversario adaptativo. Eso no es un defecto subsanable en un TFG — es una **limitación que conviene declarar en 6.1 citando a Arp et al.**, en lugar de dejar que la detecte el tribunal.

**(ii) Reproducibilidad en ML — Pineau et al., 2021.** El *Machine Learning Reproducibility Checklist* (17 ítems, desplegado en NeurIPS 2019 sobre 6.743 envíos). Sus ítems «FT» —los que aplican a toda figura o tabla con resultados empíricos— son literalmente la lista de lo que un protocolo interno debe congelar: *data collection, link to data, pre-processing, sample allocation, hyper-parameters, number of runs, description, statistics, error bars, central tendency, computing infrastructure*. Aportan además el vocabulario preciso que la memoria puede usar sin ambigüedad: **Reproducible** (mismos datos, mismo código) · **Replicable** (datos distintos, mismo código) · **Robust** (mismos datos, análisis distinto) · **Generalisable** (datos y análisis distintos).

**Contraste con este proyecto:** cumple *data collection*, *pre-processing*, *sample allocation*, *hyper-parameters* (la `config_ganadora` se persiste en cada CSV) y *link to data*. **No cumple** *number of runs*, *error bars* ni *central tendency*: todo corre con semilla 42 una sola vez y se reporta estimación puntual sin dispersión. Es la mayor brecha del proyecto contra el checklist. Consuelo relativo, y también citable: Pineau et al. reportan que el 36 % de los autores de NeurIPS 2019 juzgó que las barras de error «no aplicaban» a sus resultados. El proyecto está en compañía mayoritaria, pero eso lo convierte en **limitación declarada**, no en práctica defendible.

**(iii) Documentación de modelos — Mitchell et al., 2019.** Las *model cards* institucionalizan la **evaluación desagregada**: no reportar solo el agregado, sino el desempeño por subgrupo. Trasladado aquí, el **recall 0-day por tipo** de este TFG *es* evaluación desagregada, y las model cards le dan un nombre, un precedente y una cita ([Mitchell et al., 2019](https://doi.org/10.1145/3287560.3287596)) — nivel 1. Es un buen apoyo para 3.3: la métrica insignia del proyecto no es una excentricidad, es una práctica documentada de reporte responsable.

**(iv) Reconocimiento de conjunto abierto — Scheirer et al., 2013.** La clase `unknown` del híbrido es, formalmente, un problema de *open set recognition* ([Scheirer et al., 2013](https://doi.org/10.1109/TPAMI.2012.256)) — nivel 1. Importa para el protocolo porque justifica que la tasa de enrutado a `unknown` (hoy 13,4 % de los 0-day cazados) se reporte como **métrica propia con su alcance**, y no se mezcle en un F1 a 5 clases — que es justamente lo que decidió H-6. Da marco teórico a una decisión que hoy se justifica solo por sentido común.

**(v) El marco operativo.** NIST SP 800-94 (Scarfone y Mell, 2007) define *tuning* como alterar la configuración de un IDPS para mejorar su exactitud de detección, y describe el compromiso explícito: se afina para reducir falsos negativos **a costa de** aumentar falsos positivos, que consumen recursos de análisis. Es la fuente oficial —organismo público— para la regla «ningún recall sin su FPR» (P-2 del proyecto) y para discutir por qué un FPR observado del 8-10 % es un problema operativo real y no un decimal.

#### B.2 · `evaluacion.py` como base: qué cubre y qué le faltaría

**Sirve de base. Cubre el cálculo casi entero:**

- `evaluar_binario` devuelve precision, recall, f1, **accuracy**, **fpr**, la matriz 2×2 completa (tn/fp/fn/tp) y, con `y_score`, roc_auc y pr_auc. Cubre C4 y P7/P8 por construcción.
- `evaluar_multiclase` devuelve por clase (precision/recall/f1/soporte), macro, weighted, matriz y `classification_report`, con orden de etiquetas fijo desde `config`.
- `evaluar_0day_por_tipo` devuelve `{tipo: {n, detectados, recall}}` más `__global__`. Es la evaluación desagregada de B.1(iii), ya implementada.
- `plot_matriz_confusion` y `plot_roc_pr` a 300 dpi con títulos en español.

**Lo que le faltaría para ser un protocolo, no solo una librería de métricas.** Todo esto son **requisitos**, no tareas — el track de código está cerrado:

1. **`guardar_metricas` no impone esquema.** Su propio docstring delega el contrato en el buen criterio de quien llama: *«para columnas consistentes, pasar siempre el mismo conjunto de claves por CSV»*. Y el contrato ya se ha roto: **`metricas_baseline.csv` no tiene columna `bin_accuracy`**, mientras que `metricas_hibrido.csv` sí. La consecuencia es concreta y molesta justo donde más duele: la *accuracy* binaria sobre KDDTest+ es **la cifra que la literatura usa para comparar** (A.5), y para el baseline monolítico no se puede leer del CSV — habría que derivarla. Un protocolo debe fijar un **conjunto mínimo obligatorio de columnas** común a las cuatro tablas.
2. **La idempotencia vive fuera del módulo común.** `guardar_metricas` siempre hace *append*; la garantía «una fila por variante» la implementa cada script con su propio `_limpiar_variante_csv`, repetido cuatro veces. El protocolo debería declarar la clave de unicidad de una fila (variante × algoritmo × alcance).
3. **No hay dispersión.** Nada calcula ni almacena variabilidad entre semillas o entre *folds*. Es la brecha frente a los ítems *number of runs* / *error bars* / *central tendency* de Pineau et al.
4. **No hay procedencia por fila.** Se registra `fecha`, pero en los CSV que he leído no aparecen como columnas la semilla, las versiones de librería ni el commit. La semilla vive en `config.py` (`RANDOM_STATE=42`) pero no viaja con el dato.
5. **No hay campo de alcance.** H-6 obliga a declarar el alcance de cada métrica, pero el esquema no lo codifica: el `f1_macro` de `metricas_firmas.csv` (4 clases de ataque sobre D3 conocidos) y el `f1_macro_5_conservador` de `metricas_hibrido.csv` (5 clases sobre D2, con `unknown` contando como error) se leen igual y no son lo mismo. Un lector externo puede compararlos sin darse cuenta. **Un campo `alcance` explícito por fila cerraría el riesgo.**

#### B.3 · Qué debería congelar el protocolo interno

Recopilado de decisiones ya cerradas, sin inventar nada. El valor está en que hoy está disperso en cuatro documentos.

- **Particiones y su función, invariable.** D1 (solo normal) entrena la etapa 1 y su 20 % reservado fija el umbral p95. D3 (solo ataques conocidos) entrena la etapa 2 y aporta las probabilidades OOF que calibran `UMBRAL_CONF`. **D2 (KDDTest+, 22.544 registros) solo evalúa y nunca ajusta nada** — línea roja de H-4, blindada estructuralmente por P-4.
- **Congelado entre variantes:** semilla 42, umbral percentil 95, τ = 2 pp, `StratifiedKFold(5)`, set de 54 características, orden de clases `['normal','dos','probe','r2l','u2r','unknown']`, detector y clasificador fijos al comparar sets (H-2, H-3).
- **Métricas obligatorias para toda variante candidata:** (i) binaria **con FPR siempre**; (ii) multiclase por clase + macro **con alcance declarado**; (iii) **recall 0-day por tipo**, con `n` y con el FPR del detector en la misma fila (P-2); (iv) matriz de confusión.
- **Prohibiciones explícitas:** ningún número único global como titular (H-6); ninguna cifra de recall sin su FPR; ninguna elección de hiperparámetro o umbral mirando D2 (P5 de Arp et al.).

## Lo que no he podido confirmar

- **Yin et al., 2017 (RNN-IDS, IEEE Access).** Es la referencia moderna más citada con protocolo limpio sobre KDDTest+, y las cifras 83,28 % (binaria) / 81,29 % (5 clases) circulan por todas partes. **No las he verificado en origen:** IEEE Xplore devolvió HTTP 418 tanto por `WebFetch` como por navegador; no intenté sortear el bloqueo ni iniciar sesión, y no hallé espejo abierto legítimo pese a ser IEEE Access. **No deben citarse con número hasta verificarlas** con acceso institucional.
- **MDPI *Algorithms* 18(12):749**, «A Deterministic Comparison of Classical ML and Hybrid Deep Representation Models…» (2025). Por título es la comparación con protocolo determinista y sin fuga más pertinente que encontré; MDPI devolvió HTTP 403. Sin verificar.
- **Las seis cifras de segunda mano** listadas en A.4 (Gharib et al. 90,17 %; *denoising AE* 88,28/88,65 %; Kunang et al. 86,96 %; Kherlenchimeg y Nakaya 80 %; Shaikh y Shashikala 94,3 %; Shone et al.). Solo las conozco a través de Hindy et al., 2020. **No se citan como cifras propias de esas fuentes.**
- **Que Shone et al. evalúen por validación cruzada sobre KDDTrain+.** Es la afirmación que circula y sería el ejemplo perfecto de paper descartado por C1; **no la he verificado**, así que no la uso nominalmente como ejemplo de descarte.
- **Reconciliación del número de tipos novedosos: 14 frente a 17.** Tavallaee et al. dicen que los datasets contienen «24 training attack types, with an additional 14 types in the test data only» — pero eso se refiere a KDD'99. Este proyecto mide **17** tipos en D2 ausentes del entrenamiento (contados en `metricas_hibrido_0day.csv`). La diferencia se explica presumiblemente por el submuestreo que produce KDDTrain+/KDDTest+, pero **no he encontrado fuente primaria que lo declare** para NSL-KDD. Al escribir la memoria, la cifra 17 debe justificarse **por medición sobre el disco**, no por cita.
- **Prevalencia exacta por pitfall en Arp et al.** Las barras de la Figura 1 llevan porcentajes, pero no los transcribo como valores exactos desde la imagen. La afirmación segura y verbatim es «*each paper suffers from at least three pitfalls*» sobre 30 artículos de los cuatro congresos top.
- **Mi proporción de descarte (≈ 87 %) no es un dato de revisión sistemática.** Es una muestra acotada de búsqueda web. Para la memoria, el dato citable es el de Goldschmidt y Chudá (NSL-KDD aparece 3 veces en la investigación NIDS de primer nivel 2020-2023), no mi conteo.

## Fuentes

| # | Fuente | Nivel | Fecha | Cita completa | URL / DOI |
|---|---|---|---|---|---|
| 1 | A Detailed Analysis of the KDD CUP 99 Data Set | 1 | 2009 | M. Tavallaee, E. Bagheri, W. Lu, A. A. Ghorbani, *Proc. 2nd IEEE Symposium on Computational Intelligence for Security and Defense Applications (CISDA)*, Ottawa, 2009, pp. 1-6 | [10.1109/CISDA.2009.5356528](https://doi.org/10.1109/CISDA.2009.5356528) · [PDF autor](https://www.ee.torontomu.ca/~bagheri/papers/cisda.pdf) |
| 2 | Dos and Don'ts of Machine Learning in Computer Security | 1 | 2022 | D. Arp, E. Quiring, F. Pendlebury, A. Warnecke, F. Pierazzi, C. Wressnegger, L. Cavallaro, K. Rieck, *31st USENIX Security Symposium*, 2022, pp. 3971-3988 | [usenix.org](https://www.usenix.org/conference/usenixsecurity22/presentation/arp) · [arXiv:2010.09470](https://arxiv.org/abs/2010.09470) |
| 3 | Outside the Closed World: On Using Machine Learning for Network Intrusion Detection | 1 | 2010 | R. Sommer, V. Paxson, *2010 IEEE Symposium on Security and Privacy*, Oakland, pp. 305-316. Premio *Test of Time* IEEE S&P 2020 | [10.1109/SP.2010.25](https://doi.org/10.1109/SP.2010.25) |
| 4 | SoK: Pragmatic Assessment of Machine Learning for Network Intrusion Detection | 1 | 2023 | G. Apruzzese, P. Laskov, J. Schneider, *2023 IEEE 8th European Symposium on Security and Privacy (EuroS&P)*, pp. 592-614 | [10.1109/EuroSP57164.2023.00042](https://doi.org/10.1109/EuroSP57164.2023.00042) · [arXiv:2305.00550](https://arxiv.org/abs/2305.00550) |
| 5 | Network intrusion datasets: A survey, limitations, and recommendations | 1 | 2025 | P. Goldschmidt, D. Chudá, *Computers & Security*, vol. 156, art. 104510, 2025 | [10.1016/j.cose.2025.104510](https://doi.org/10.1016/j.cose.2025.104510) · [arXiv:2502.06688](https://arxiv.org/abs/2502.06688) |
| 6 | A survey of network-based intrusion detection data sets | 1 | 2019 | M. Ring, S. Wunderlich, D. Scheuring, D. Landes, A. Hotho, *Computers & Security*, vol. 86, pp. 147-167, 2019 | [10.1016/j.cose.2019.06.005](https://doi.org/10.1016/j.cose.2019.06.005) |
| 7 | Improving Reproducibility in Machine Learning Research (A Report from the NeurIPS 2019 Reproducibility Program) | 1 | 2021 | J. Pineau, P. Vincent-Lamarre, K. Sinha, V. Larivière, A. Beygelzimer, F. d'Alché-Buc, E. Fox, H. Larochelle, *Journal of Machine Learning Research*, vol. 22, n.º 164, pp. 1-20, 2021 | [jmlr.org/papers/v22/20-303](https://www.jmlr.org/papers/v22/20-303.html) |
| 8 | Model Cards for Model Reporting | 1 | 2019 | M. Mitchell, S. Wu, A. Zaldivar, P. Barnes, L. Vasserman, B. Hutchinson, E. Spitzer, I. D. Raji, T. Gebru, *Proc. Conference on Fairness, Accountability, and Transparency (FAT\* '19)*, pp. 220-229 | [10.1145/3287560.3287596](https://doi.org/10.1145/3287560.3287596) |
| 9 | Leakage and the reproducibility crisis in machine-learning-based science | 1 | 2023 | S. Kapoor, A. Narayanan, *Patterns*, vol. 4, n.º 9, art. 100804, 2023 | [10.1016/j.patter.2023.100804](https://doi.org/10.1016/j.patter.2023.100804) |
| 10 | Utilising Deep Learning Techniques for Effective Zero-Day Attack Detection | 1 | 2020 | H. Hindy, R. Atkinson, C. Tachtatzis, J.-N. Colin, E. Bayne, X. Bellekens, *Electronics*, vol. 9, n.º 10, art. 1684, 2020 | [10.3390/electronics9101684](https://doi.org/10.3390/electronics9101684) |
| 11 | Experimental Review of Neural-Based Approaches for Network Intrusion Management | 1 | 2020 | M. Di Mauro, G. Galatro, A. Liotta, *IEEE Transactions on Network and Service Management*, vol. 17, n.º 4, pp. 2480-2495, 2020 | [10.1109/TNSM.2020.3024225](https://doi.org/10.1109/TNSM.2020.3024225) |
| 12 | Toward Open Set Recognition | 1 | 2013 | W. J. Scheirer, A. de Rezende Rocha, A. Sapkota, T. E. Boult, *IEEE Transactions on Pattern Analysis and Machine Intelligence*, vol. 35, n.º 7, pp. 1757-1772, 2013 | [10.1109/TPAMI.2012.256](https://doi.org/10.1109/TPAMI.2012.256) |
| 13 | Guide to Intrusion Detection and Prevention Systems (IDPS) | 1 | 2007-02 | K. Scarfone, P. Mell, *NIST Special Publication 800-94*, National Institute of Standards and Technology, feb. 2007 | [10.6028/NIST.SP.800-94](https://doi.org/10.6028/NIST.SP.800-94) |
| 14 | A Deep Learning Approach for Intrusion Detection Using Recurrent Neural Networks | 1 | 2017 | C. Yin, Y. Zhu, J. Fei, X. He, *IEEE Access*, vol. 5, pp. 21954-21961, 2017. **Metadatos verificados; cifras NO verificadas** (ver «Lo que no he podido confirmar») | [10.1109/ACCESS.2017.2762418](https://doi.org/10.1109/ACCESS.2017.2762418) |

**Fuentes internas consultadas (disco, el disco manda):** `Resultados\metricas_hibrido.csv`, `metricas_hibrido_0day.csv`, `metricas_baseline.csv`, `metricas_anomalias.csv`, `metricas_firmas.csv`; `Implementacion\app\evaluacion.py`; `resumen-de-decisiones.md`; `EL_FUTURO.md`.

## Cambios en Bibliografía.md

**Ninguno.** Por instrucción explícita del encargo: `Bibliografía.md` está bajo auditoría abierta (`features.md:22-27`) y no se toca en este ciclo. Las 14 fuentes van completas en la tabla anterior, con datos de cita y nivel de fiabilidad, listas para volcarse a Zotero cuando la auditoría cierre.

## Implicaciones para el proyecto

### Pronunciamiento: adoptar las dos, en este orden y con este reparto

**No son alternativas excluyentes, pero sí tienen prioridades muy distintas.** (b) es un cimiento; (a) es un acabado. Construir (a) sin (b) produce una comparación que no se sabe defender; construir (b) sin (a) deja al tribunal con la pregunta «¿y esto respecto a qué?» sin responder.

**Primero (b), completo — coste bajo, retorno alto.**

- **Dónde:** una sección corta de **protocolo de evaluación** al principio del capítulo 5 (antes de 5.1), más el respaldo bibliográfico en [[3.3 Metodología de funcionamiento del sistema]].
- **Qué:** exactamente lo de B.3, que ya está decidido. **El trabajo no es decidir, es escribirlo junto y citarlo.** Hoy está disperso entre Q4, Q6, H-1…H-7 y P-1…P-5 de `resumen-de-decisiones.md`, que es un documento interno que no va a la memoria.
- **Por qué rinde tanto:** convierte cinco decisiones que hoy se justifican por sentido común en decisiones con respaldo de nivel 1. En particular, la tabla de B.1 (pitfalls de Arp et al. ↔ decisiones del proyecto) es material casi listo para redactar: permite escribir «esta decisión evita el pitfall P5 documentado por Arp et al. sobre 30 artículos de los cuatro congresos de seguridad de primer nivel» en lugar de «se decidió no mirar el test».
- **Coste:** redacción. Cero código.

**Después (a), pero reducido y con otro nombre — coste medio, riesgo alto si se hace mal.**

- **Dónde:** la discusión de [[05 Evaluación/5.4 Conclusiones del capítulo|5.4]].
- **Qué NO hacer:** una tabla de *accuracies* de la literatura. Con un 87 % de descarte en mi muestra y con NSL-KDD prácticamente ausente de los venues de primer nivel (Goldschmidt y Chudá), cualquier tabla grande sería una colección de cifras indefendibles una por una.
- **Qué sí hacer, en cuatro párrafos:** (1) los criterios C1-C7 de A.3; (2) la tabla pequeña de supervivientes de A.5 (los 7 baselines canónicos frente a `bin_accuracy` 0,8605 del híbrido), con sus dos reservas declaradas; (3) el descarte y su magnitud, apoyado en el dato citable de Goldschmidt y Chudá, **no** en mi conteo; (4) el hueco: el recall 0-day por tipo con FPR declarado no aparece en la literatura revisada.
- **El descarte es el hallazgo, no un residuo.** Un TFG que explica *por qué* no puede comparar demuestra más criterio que uno que compara mal. Y encaja con la posición del proyecto en `EL_FUTURO.md §0`: la diferenciación no está en el algoritmo, está en la honestidad de la evaluación.

### Fricciones con decisiones ya cerradas — ninguna contradicción, dos avisos

Revisado `resumen-de-decisiones.md`. **No he encontrado nada que desmienta una decisión cerrada.** La literatura refuerza H-4 (P5 de Arp et al. describe exactamente la trampa que H-4 evita), P-2 (NIST SP 800-94 sobre el compromiso FN/FP), H-6 (Scheirer et al. da marco de *open set* a la clase `unknown`) y la elección de baseline (P6). Pero hay dos roces que conviene nombrar antes de redactar:

1. **H-6 prohíbe el número único global como titular; la comparación externa necesita justamente uno.** Para contrastar con la literatura hace falta la *accuracy* binaria sobre KDDTest+ (0,8605), que es precisamente el tipo de cifra que H-6 desaconseja. **No es una contradicción, pero lo parecerá** si 5.4 exhibe un número que 5.3 declaró poco informativo. **Propuesta:** presentarla etiquetada como *«cifra de comparabilidad externa, no titular del sistema»*, con una frase que remita a H-6. Decide Francisco.
2. **La convención de semilla única (42, una corrida) es una brecha declarada frente al checklist de Pineau et al.** No contradice ninguna decisión — ninguna afirma reportar dispersión — pero es la crítica metodológica más fácil de hacer desde fuera. **Propuesta:** declararla en [[6.1 Conclusiones]] como limitación, junto con P9/P10 de Arp et al. (sin despliegue real ni adversario adaptativo). Vale mucho más declararla que esperar a que la pregunten.

### Requisito detectado, no tarea

**`metricas_baseline.csv` no persiste `bin_accuracy`, y `metricas_hibrido.csv` sí.** El cálculo no falta: `evaluar_binario` devuelve `accuracy` (`evaluacion.py:80`); lo que falta es la columna en la fila que persiste `baseline.py`. Consecuencia práctica: **la cifra que la literatura usa para comparar no se puede leer del CSV para el baseline monolítico** — habría que derivarla de `bin_recall`, `bin_fpr` y los soportes, y un número derivado a mano en una memoria es un número que nadie vuelve a comprobar.

Lo anoto como **requisito del protocolo** (conjunto mínimo obligatorio de columnas común a las cuatro tablas, más un campo `alcance` por fila), no como tarea de código: **el track de código está cerrado desde el 2026-07-16 y no propongo reabrirlo.** Si Francisco decide que la comparación externa de 5.4 necesita esa cifra para el baseline, hay dos salidas y las dos son suyas: derivarla y declararla como derivada en la memoria, o abrir ficha en `features.md`.

---

## Decisiones tomadas a partir de este informe

> [!note] Alcance de este bloque
> Registro **posterior** al informe, añadido el 2026-08-18 al ejecutar el punto 1 de la ficha **T17**.
> Recoge únicamente lo que quedó **cerrado por escrito** en el `grill-me` del **2026-08-06** y sus
> volcados —`resumen-de-decisiones.md` (§ «Decisiones del 2026-08-06» y § «Decisiones del
> 2026-08-09») y el lote **T0-T17** de `features.md`—. Lo que este informe **propuso** y no llegó a
> decisión registrada aparece abajo como pendiente, no como decisión.

### Lo que se convirtió en decisión

| # | Decisión cerrada | De dónde sale en este informe | Dónde queda registrada / aplicada |
|---|---|---|---|
| **D1** | **Criterio rector del lote:** nada que no refine el proyecto o no enseñe el límite; las imposibilidades se declaran con su razón técnica, sin sucedáneos sintéticos. Y **el dataset tiene argumento positivo propio**, que va **antes** de cualquier límite | A.4 (Goldschmidt y Chudá: solo el **23 %** de los datasets NIDS trae partición train/test predefinida, **16 %** desde 2020; NSL-KDD sí la trae y este TFG la respeta) | `resumen-de-decisiones.md` § 2026-08-06; **aplicado en `4.2` («por qué NSL-KDD») en la TANDA 14**, con marcador `[CITA: Goldschmidt y Chudá 2025]` |
| **D2** | **Se REABRE el track de código**, cerrado el 2026-07-16, de forma declarada y acotada (decisión marco (a)) | B.2: la auditoría C1-C7 **no se cumplía en C3 ni en C6** — `accuracy_D2` era una columna homónima con dos alcances (0,9683 en firmas, 0,7395 en baseline) | `resumen-de-decisiones.md` § 2026-08-06 |
| **D3** | **Nivel 1 — rediseño del esquema de métricas** (ficha **T1**): conjunto mínimo de columnas y campo de **alcance** por fila. Condición: **no mueve ningún número publicado** | B.2, puntos 1 y 5 (esquema no impuesto; `f1_macro` de firmas y `f1_macro_5_conservador` del híbrido se leen igual sin serlo) | `features.md`, lote T0-T17 |
| **D4** | **Nivel 2 acotado — 10 semillas** (ficha **T4**), con los **titulares de 5.1-5.3 fijos en la semilla 42** y la dispersión como tabla nueva en `A.3` más un párrafo en `5.4` | B.2, punto 3, y B.1(ii): brecha frente a los ítems *number of runs*, *error bars* y *central tendency* del checklist de Pineau et al. | `resumen-de-decisiones.md` § 2026-08-06; **T4 cerrada en la TANDA 19 (2026-08-17)** |
| **D5** | **Renuncia declarada al p-valor** sobre las 10 semillas, con su razón escrita: 10 puntos sobre un único dataset no sostienen un contraste. Si los intervalos se solapan, **se dice y no se establece el orden** | B.1(ii): declarar la renuncia **cumple** el ítem *statistics* de Pineau et al.; callarla no | `resumen-de-decisiones.md` § 2026-08-06 |
| **D6** | **La comparación externa de `5.4` va reducida: cuatro párrafos y ninguna tabla grande de *accuracies*** — (1) criterios C1-C7; (2) tabla pequeña de supervivientes con sus **dos reservas declaradas**; (3) el descarte y su magnitud; (4) el hueco, formulado como «no se ha encontrado en la literatura revisada» | A.3, A.4 y A.5, más el pronunciamiento de «Implicaciones» | `features.md`, mapa de T13 (`5.4`) |
| **D7** | **Hindy et al. 2020 se cita por el método, no por el número:** su 89-99 % incumple C7 y no se pone al lado de las cifras del proyecto | A.5 | `features.md`, mapa de T13 (`5.4`) |
| **D8** | **La magnitud del descarte se apoya en el dato citable de Goldschmidt y Chudá** (NSL-KDD aparece 3 veces en la investigación NIDS de primer nivel 2020-2023) | A.4 | `features.md`, mapa de T13 (`5.4`) |

### Lo que se descartó

| # | Descartado | Por qué |
|---|---|---|
| **X1** | **Una tabla grande de *accuracies* de la literatura** en `5.4` | Con el filtro C1-C7 aplicado honestamente, casi todas las cifras se caen; una tabla así sería una colección de números indefendibles uno a uno (A.3, regla derivada; A.4) |
| **X2** | **Meter una cifra incomparable «con nota al pie»** | Incumplir C1, C3 o C4 se salda con **descarte**, no con anotación: anotarla da apariencia de comparación donde no la hay |
| **X3** | **Usar el ≈87 % de descarte propio como dato citable** | Es una muestra acotada de búsqueda web, no una revisión sistemática; se declara como tal y el dato publicable es el de Goldschmidt y Chudá (D8) |
| **X4** | **Citar con número las cifras no verificadas** — Yin et al. 2017, MDPI *Algorithms* 18(12):749 y las seis cifras conocidas solo de segunda mano vía Hindy et al. | Sin acceso al texto completo no se verifican en origen; se citan **sin cifra** o no se citan |
| **X5** | **Usar a Shone et al. como ejemplo nominal de paper descartado por C1** | La afirmación de que evalúan por validación cruzada sobre KDDTrain+ **no está verificada** |
| **X6** | **Justificar por cita el número de tipos novedosos (17)** | Tavallaee et al. dicen 14, pero sobre KDD'99; la cifra 17 se justifica **por medición sobre disco** (`metricas_hibrido_0day.csv`) |
| **X7** | **Reabrir el código para añadir `bin_accuracy` a `metricas_baseline.csv`** desde este informe | Queda como **requisito del protocolo**, no como tarea: la reapertura del track (D2) tiene alcance tasado y nada más entra en ella |

### Lo que quedó abierto y no es decisión

> [!todo] Dos propuestas de este informe sin decisión registrada
> 1. **Etiquetar el `bin_accuracy` 0,8605 como «cifra de comparabilidad externa, no titular del sistema»** para resolver el roce con H-6 (ver «Fricciones», punto 1). El informe lo propone y lo deja explícitamente a Francisco; **no consta cerrado** en `resumen-de-decisiones.md`.
> 2. **Declarar en `6.1` como limitaciones** la semilla única y los pitfalls **P9** (*Lab-Only Evaluation*) y **P10** (*Inappropriate Threat Model*). Es propuesta de B.1(i) y de «Fricciones», punto 2; falta el respaldo escrito que la convierta en decisión.
>
> Si alguna de las dos se cierra, actualizar este bloque y no darla por decidida antes.
