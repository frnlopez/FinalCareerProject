---
titulo: "Clasificadores tabulares modernos, modelos híbridos de entrenamiento y tratamiento de variables categóricas: ¿qué alternativas hay al RF/DecisionTree y a la cascada dura?"
numero: "-"
estado: informe
docx_ref: "-"
---

# Clasificadores tabulares modernos, modelos híbridos de entrenamiento y tratamiento de variables categóricas

- **Encargo:** ¿qué alternativas de modelado existen, más allá del RandomForest/DecisionTree de la
  etapa 2 y de la cascada dura actual, para un problema tabular como NSL-KDD? Tres bloques
  obligatorios: (1) clasificadores tabulares modernos y el debate «¿siguen ganando los árboles?»,
  con la evidencia a favor **y** en contra; (2) «modelos híbridos de entrenamiento» en sus dos
  lecturas —mezclar familias de modelos y mezclar fases/paradigmas de entrenamiento—, con peso
  especial en la segunda por su enganche con `EL_FUTURO.md:72-74`; (3) tratamiento de las
  variables categóricas más allá del One-Hot, incluida la arquitectura de dos ramas.
- **Fecha:** 2026-08-02
- **Alcance:**
  - **Entra:** literatura de aprendizaje tabular general (arquitecturas, *benchmarks*,
    preentrenamiento, codificación de categóricas), su contraste con los datos ya medidos de este
    proyecto, y una evaluación de cada candidato por **coste de implementación** y por **lo que
    aportaría a este sistema**, incluida su previsible interacción con el **recall 0-day por
    tipo**.
  - **Queda fuera** (por encargo, taxativo): cómo resuelven otros autores los NIDS híbridos
    anomalía+firmas (informe hermano `arquitecturas-hibridas-en-la-literatura.md`); comparar las
    cifras del TFG con lo publicado sobre NSL-KDD o definir un protocolo de *benchmark* (informe
    hermano `benchmark-comparativo-nsl-kdd.md`); aprendizaje continuo
    ([[aprendizaje-continuo-nested-learning]]); y **cualquier propuesta de código** —el track de
    código está cerrado desde el 2026-07-16.
- **Alimenta a:** [[6.2 Líneas futuras]] (**borrador del `redactor-tfg` con revisión final de
  Francisco**, según la decisión marco (b) del 2026-08-06; el respaldo se acumula en `EL_FUTURO.md`).

> [!warning] Este informe no es memoria
> Es insumo citable. No entra en [[00 Índice TFG]], no lleva número de capítulo y su prosa no se
> copia a un capítulo sin que lo decida Francisco. Todo lo de `## Implicaciones para el proyecto`
> son **candidatos** a línea futura, no tareas.

## Respuesta corta

**Los árboles siguen ganando en el régimen exacto de este problema, y la evidencia publicada lo
dice con los criterios que este dataset cumple**: D3 tiene 58 630 filas y 54 características
(≈1 086 muestras por característica), distribuciones muy sesgadas y decenas de características casi
inútiles —las tres condiciones que McElfresh et al. (NeurIPS 2023) identifican como favorables a
los GBDT y que Grinsztajn et al. (NeurIPS 2022) señalan como las debilidades estructurales de las
redes. Cambiar RandomForest por TabNet, FT-Transformer o TabPFN es **caro** (PyTorch, ruptura de la
persistencia `.joblib` y del protocolo homogéneo de comparación) y **no está respaldado** para este
régimen. Lo único que la propia literatura escéptica sí respalda es lo contrario de sustituir:
**mezclar familias** —Shwartz-Ziv y Armon, el artículo bandera del «los árboles ganan», cierran su
resumen diciendo que un *ensemble* de modelos profundos **con** XGBoost supera a XGBoost solo, y
TabArena (NeurIPS 2025) concluye que el *ensemble* entre modelos es hoy el estado del arte. De las
dos lecturas de «híbrido de entrenamiento», la de **mezclar fases** es la que
`EL_FUTURO.md:72-74` ya sembró y **no sale bien parada al aterrizarla**: el autoencoder está
entrenado **solo con D1 (tráfico normal)**, de modo que su latente de 32 dimensiones está optimizado
para reconstruir precisamente lo que no es un ataque, y las características que sostienen la clase
`u2r` (`num_shells`, `root_shell`, `su_attempted`) son ≈0 en D1 por construcción; además el latente
**destruye la extracción de reglas legibles**, que es lo que da sentido a la etapa de firmas. En el
bloque 3, el hallazgo con más recorrido es que el one-hot de `service` (70 niveles) genera 84 de las
122 características, y la selección supervisada tira **55 de los 70** `service_*` —entre ellos
`service_X11` y `service_domain`, justo los servicios de los 0-day `xlock`, `xsnoop` y `named`,
cuyo recall del detector sube de 0,33→0,78, 0,75→1,00 y 0,53→0,76 al pasar a 122.

## Hallazgos

### Bloque 1 — Clasificadores tabulares modernos y el debate de fondo

#### 1.1 El mapa: qué propone cada familia

Cinco familias, con lo que cada una aporta de distinto y lo que cuesta:

| Familia | Representantes | Idea distintiva | Dependencia |
|---|---|---|---|
| **GBDT modernos** | XGBoost ([Chen y Guestrin, KDD 2016](https://doi.org/10.1145/2939672.2939785)), LightGBM ([Ke et al., NIPS 2017](https://papers.nips.cc/paper/6907-lightgbm-a-highly-efficient-gradient-boosting-decision-tree)), CatBoost ([Prokhorenkova et al., NeurIPS 2018](https://proceedings.neurips.cc/paper/2018/hash/14491b756b3a51daac41c24863285549-Abstract.html)) | Boosting de árboles con histogramas, crecimiento *leaf-wise*, y —en CatBoost— *ordered boosting* y estadísticos de destino ordenados para las categóricas | Librería nueva (no está en `requirements.txt`) |
| **Redes «con sabor a árbol»** | NODE ([Popov et al., ICLR 2020](https://arxiv.org/abs/1909.06312)) | Conjuntos de árboles *oblivious* diferenciables entrenados de extremo a extremo | PyTorch |
| **Atención sobre tabular** | TabNet ([Arik y Pfister, AAAI 2021](https://doi.org/10.1609/aaai.v35i8.16826)), FT-Transformer ([Gorishniy et al., NeurIPS 2021](https://arxiv.org/abs/2106.11959)), SAINT ([Somepalli et al., 2021](https://arxiv.org/abs/2106.01342)) | Selección secuencial de características con máscaras dispersas (TabNet); tokenización de características + Transformer (FT-T); atención sobre filas **y** columnas + preentrenamiento contrastivo (SAINT) | PyTorch |
| **MLP bien regularizado / *ensembling* barato** | Cócteles de regularización ([Kadra et al., NeurIPS 2021](https://proceedings.neurips.cc/paper/2021/hash/c902b497eb972281fb5b4e206db38ee6-Abstract.html)), TabM ([Gorishniy et al., ICLR 2025](https://proceedings.iclr.cc/paper_files/paper/2025/hash/c1ba41c694834aeef91ae161711d4939-Abstract-Conference.html)) | La arquitectura importa menos que la regularización y el *ensembling*: TabM imita un conjunto de MLP dentro de un solo modelo compartiendo pesos | PyTorch |
| **Modelos fundacionales tabulares** | TabPFN ([Hollmann et al., *Nature* 637, 2025](https://doi.org/10.1038/s41586-024-08328-6)) | Red preentrenada sobre datos sintéticos que resuelve la tarea por **aprendizaje en contexto**: no hay entrenamiento, se le pasa el conjunto de entrenamiento como contexto | Modelo preentrenado + PyTorch |

Dos matices sobre TabNet, porque es el que abre el encargo: (a) su venta no es solo la precisión
sino la **interpretabilidad** —las máscaras de atención dicen qué característica usó en cada paso—,
que es la misma promesa que aquí cubre el `export_text` del DecisionTree y que
`EL_FUTURO.md:33-39` quiere llevar más lejos con RIPPER; y (b) TabNet incorpora **preentrenamiento
no supervisado** por reconstrucción de características enmascaradas, lo que lo coloca a la vez en el
bloque 2b de este informe.

Sobre TabPFN conviene ser preciso con los límites, porque deciden si es siquiera aplicable. La
versión original ([arXiv:2207.01848](https://arxiv.org/abs/2207.01848), presentada como ICLR 2023)
se evaluaba con **≤1 000 muestras de entrenamiento, ≤100 características numéricas, sin faltantes y
≤10 clases**. La v2 de *Nature* sube a **10 000 muestras y 500 características, 10 clases**, y ya
maneja categóricas de forma nativa; la
[documentación oficial de Prior Labs](https://docs.priorlabs.ai/models) declara además versiones
posteriores (TabPFN-2.6: 100 000 × 2 000; TabPFN-3: hasta 1 M de filas). **D3 tiene 58 630 filas**,
así que la versión de *Nature* no lo admite sin submuestrear —y submuestrear es justo lo que no se
puede hacer con `u2r`, que tiene ~52 muestras en D3 (`firmas.py:98`).

#### 1.2 El polo escéptico: la evidencia de que los árboles siguen ganando

**Shwartz-Ziv y Armon (2022)**, *Tabular Data: Deep Learning is Not All You Need*
([DOI 10.1016/j.inffus.2021.11.011](https://doi.org/10.1016/j.inffus.2021.11.011)), comparan los
modelos profundos tabulares recién propuestos contra XGBoost **incluyendo los propios datasets con
los que cada artículo se vendía**. Conclusión textual del resumen: «*Our study shows that XGBoost
outperforms these deep models across the datasets, including the datasets used in the papers that
proposed the deep models. We also demonstrate that XGBoost requires much less tuning.*» El segundo
punto —el coste de ajuste— pesa tanto como el primero para un TFG con presupuesto de cómputo finito.

**Grinsztajn, Oyallon y Varoquaux (NeurIPS 2022, Datasets and Benchmarks Track)**,
[*Why do tree-based models still outperform deep learning on tabular data?*](https://proceedings.neurips.cc/paper_files/paper/2022/file/0378c7692da36807bdec87ab043cdadc-Paper-Datasets_and_Benchmarks.pdf),
van un paso más allá de «quién gana» y buscan **por qué**. Construyen un banco de 45 datasets y
20 000 horas de cómputo por aprendiz, y concluyen que los árboles siguen siendo estado del arte en
datos de tamaño medio (~10 K muestras). Su aportación útil aquí son los **tres retos** que una red
tabular tiene que resolver y no resuelve: «*(1) be robust to uninformative features, (2) preserve
the orientation of the data, and (3) be able to easily learn irregular functions*».

#### 1.3 El polo contrario y los que los rebaten

No es un debate cerrado, y presentarlo como cerrado sería tan falso como lo contrario.

**Kadra et al. (NeurIPS 2021)** atacan la premisa: si un MLP bien regularizado —buscando la
combinación óptima de 13 técnicas de regularización, el «cóctel»— supera a las arquitecturas
tabulares especializadas en 40 datasets, entonces buena parte de la ventaja atribuida a la
arquitectura era en realidad ventaja del ajuste. Es una crítica **a los dos polos**: si el MLP
simple gana a TabNet y compañía, el problema no es «profundo vs. árbol».

**Rubachev et al. (2022)**, [arXiv:2207.03208](https://arxiv.org/abs/2207.03208) —**nivel 2,
preprint**— sostienen que la comparación se hizo con modelos profundos **sin preentrenar**, y que
«*properly performed pretraining significantly increases the performance of tabular DL models, which
often leads to their superiority over GBDTs*». Su hallazgo concreto —que **usar las etiquetas
durante el preentrenamiento** (*target-aware*) mejora el rendimiento aguas abajo— vuelve en el
bloque 2b y es el argumento más fuerte **contra** un preentrenamiento puramente reconstructivo.

**McElfresh et al. (NeurIPS 2023, Datasets and Benchmarks Track)**,
[*When Do Neural Nets Outperform Boosted Trees on Tabular Data?*](https://proceedings.neurips.cc/paper_files/paper/2023/hash/f06d5ebd4ff40b40dd97e30cee632123-Abstract-Datasets_and_Benchmarks.html),
es el árbitro más citable: 19 algoritmos × 176 datasets, el análisis más grande hasta esa fecha. Su
veredicto **desinfla el debate entero**: «*the "NN vs. GBDT" debate is overemphasized: for a
surprisingly high number of datasets, either the performance difference between GBDTs and NNs is
negligible, or light hyperparameter tuning on a GBDT is more important than choosing between NNs and
GBDTs*». Y —esto es lo que hace transferible el resultado— **caracterizan qué datasets favorecen a
cada familia**: los GBDT ganan en datasets **más grandes**, con **alta razón muestras/características**
y con **distribuciones sesgadas e irregulares**.

**Erickson et al. (NeurIPS 2025, Datasets and Benchmarks Track, *spotlight*)**, TabArena
([arXiv:2506.16791](https://arxiv.org/abs/2506.16791)), es el estado más reciente y el más matizado:
51 datasets, 16 modelos, 25 millones de ejecuciones, con mantenimiento vivo. Conclusiones textuales:
«*While gradient-boosted trees are still strong contenders on practical tabular datasets, we observe
that deep learning methods have caught up under larger time budgets with ensembling. At the same
time, foundation models excel on smaller datasets. Finally, we show that ensembles across models
advance the state-of-the-art*». Tres cosas de golpe: los árboles siguen siendo fuertes; el *deep
learning* **empata si le das presupuesto y lo ensamblas**; y lo que de verdad manda es el
*ensemble* **entre** modelos. Añaden una advertencia metodológica que reaparece en el bloque 2a:
«*some deep learning models are overrepresented in cross-model ensembles due to validation set
overfitting*».

#### 1.4 Dónde cae *este* dataset en ese mapa de evidencia

Este es el paso que convierte el debate en una decisión defendible, y sale del cruce entre los
criterios de McElfresh y los números ya medidos en disco:

| Criterio de McElfresh | Valor en este proyecto | ¿A quién favorece? |
|---|---|---|
| Tamaño del dataset | D3 = **58 630** filas (`4.3 Preprocesamiento…:227`); D1 = 67 343 | **GBDT** (los datasets grandes los favorecen) |
| Razón muestras / características | 58 630 / 54 ≈ **1 086** | **GBDT** (alta razón) |
| Sesgo e irregularidad de las distribuciones | `src_bytes`, `dst_bytes`, `duration`, `count`: colas larguísimas típicas de tráfico de red | **GBDT** |
| Características no informativas | De las 122, **60 se eliminan por importancia** y su importancia individual llega a bajar a 0,000000 (`selected_features.txt:90-151`) | **GBDT** (reto nº 1 de Grinsztajn) |
| Nº de clases de la etapa 2 | **4** (`firmas.py:5`, `147`) | Indiferente |

Los cinco criterios apuntan al mismo sitio. La conclusión no es «el *deep learning* tabular no
sirve»: es que **este problema cae exactamente en el cuadrante donde la evidencia publicada dice
que no compensa**, y eso es una afirmación citable, no una preferencia.

Hay además una comprobación interna que apunta en la misma dirección y que ya está en disco: en
`metricas_firmas.csv`, el **HistGradientBoosting** —el GBDT que sí está en el sistema— no supera al
RandomForest en 54 características (`f1_macro` 0,804 frente a 0,822) pese a tardar más
(68,7 s frente a 54,8 s). Si el GBDT moderno de la propia `sklearn` no despega en este problema, la
probabilidad de que lo haga una arquitectura de atención con veinte veces más hiperparámetros es
baja.

#### 1.5 El límite que ningún *benchmark* de este bloque cubre — y hay que decirlo

**Ninguno de los cinco *benchmarks* citados mide lo que este TFG mide.** Todos evalúan
clasificación tabular cerrada: las clases del test son las del train. La seña de identidad de este
proyecto es el **recall 0-day por tipo** sobre los 17 tipos ausentes del train (3 750 filas de D2,
`metricas_hibrido_0day.csv`), que es un problema de **conjunto abierto**. Por tanto:

- Lo que la evidencia de este bloque **sí** sostiene: que cambiar el clasificador de la etapa 2 por
  una arquitectura profunda no va a mejorar `conocida_f1_macro` (hoy 0,748 con 54 características,
  `metricas_hibrido.csv`).
- Lo que **no** sostiene, en ninguna dirección: qué le pasaría al recall 0-day. Un modelo puede ser
  peor en la tarea cerrada y mejor calibrado fuera de distribución, o al revés. Afirmar que TabNet
  «mejoraría la detección de 0-day» sería inventar; afirmar que la empeoraría, también.

Esa laguna es, en sí misma, material para 6.2: es un hueco real de la literatura tabular.

### Bloque 2a — Mezclar familias de modelos: *ensembles* heterogéneos, *stacking*, votación

#### 2a.1 La evidencia converge aquí, y viene de los dos polos del bloque 1

Es el punto en el que escépticos y entusiastas coinciden, lo que lo hace inusualmente sólido:

- El artículo bandera del «los árboles ganan» **termina recomendando mezclar**: «*On the positive
  side, we show that an ensemble of deep models and XGBoost performs better on these datasets than
  XGBoost alone*» (Shwartz-Ziv y Armon, resumen).
- El *benchmark* más reciente lo eleva a conclusión principal: «*ensembles across models advance the
  state-of-the-art in tabular machine learning*» (TabArena, NeurIPS 2025), con un *ensemble* diverso
  que supera a todos los modelos individuales y a los sistemas AutoML líderes.
- Es también el mecanismo central de los sistemas AutoML tabulares: AutoGluon-Tabular
  ([Erickson et al., 2020, arXiv:2003.06505](https://arxiv.org/abs/2003.06505) — **nivel 2,
  preprint de empresa, con sesgo comercial declarado**) entrena aprendices base diversos en
  paralelo, aplica *k-fold bagging* para generar predicciones **fuera de pliegue** y las apila en
  varias capas.

El fundamento teórico es antiguo y perfectamente citable: la *stacked generalization* de
[Wolpert (1992)](https://doi.org/10.1016/S0893-6080(05)80023-1) —aprender un segundo modelo sobre
las predicciones de los primeros, entrenados sobre una parte del conjunto e interrogados sobre el
resto— y las *stacked regressions* de [Breiman (1996)](https://doi.org/10.1007/BF00117832), que
aporta la forma moderna: **validación cruzada interna** y coeficientes con restricción de no
negatividad.

#### 2a.2 La disciplina no negociable del *stacking*: predicciones fuera de pliegue

Todo el aparato de Wolpert y Breiman descansa en una sola condición: el meta-clasificador debe
entrenarse sobre predicciones que los modelos base hicieron **sobre datos que no vieron al
entrenarse**. Si se le pasan predicciones *in-sample*, el meta-modelo aprende a confiar en modelos
sobreajustados y el conjunto empeora.

**Aquí eso ya está resuelto para media ecuación**, y conviene que Francisco lo sepa antes de valorar
el coste: `hibrido.py` **ya genera probabilidades fuera de pliegue** del clasificador de firmas
sobre D3 mediante `cross_val_predict`, reconstruyendo el estimador desde su configuración guardada
(`hibrido.py:6-9`, `184-192`; decisión Q4 y H-1 de `resumen-de-decisiones.md`). La fontanería más
delicada de un *stacking* —la que la gente se salta y produce resultados inflados— **ya existe y ya
está auditada**.

#### 2a.3 Las tres trampas de la fusión por meta-clasificador *en esta cascada*

`EL_FUTURO.md:66-68` propone «fusión por meta-clasificador (*stacking*) en vez de cascada dura: un
modelo que combine `anomaly_score` + `predict_proba` de firmas». La idea es buena y la comparación
cascada-frente-a-fusión es una pregunta de diseño legítima. Pero al aterrizarla sobre esta
arquitectura aparecen tres problemas que no están escritos en ningún sitio del repositorio:

**Trampa 1 — el `anomaly_score` de las filas normales está contaminado por construcción.** Para
entrenar el meta-clasificador hacen falta filas de las dos clases. Las filas de ataque pueden venir
de D3, que el detector nunca vio (se entrenó solo con D1, `program.py:166`), así que sus *scores*
son honestos. Pero las filas **normales** solo pueden venir de D1 —y sobre D1 el detector **sí** se
entrenó: sus *scores* ahí son artificialmente bajos. Un meta-clasificador entrenado con eso aprende
una separación más limpia de la que existe. La salida natural es usar `D1_val`, el 20 % reservado
(`anomalias.py:139`), pero **`D1_val` es exactamente lo que ya calibra el umbral del percentil 95**
(`anomalias.py:89`, `259-261`, decisión 6): reutilizarlo para entrenar el meta-modelo gasta dos
veces el mismo conjunto reservado. No es imposible de resolver, pero es una decisión de protocolo,
no una línea de código.

**Trampa 2 — el meta-clasificador no puede aprender la clase que más importa.** El sistema reporta
una matriz de 5×6 con la clase `unknown` (decisión H-6). Un meta-clasificador supervisado necesita
ejemplos de cada clase que deba predecir, y **de `unknown` no hay ni un solo ejemplo en el
entrenamiento**: D3 contiene, por definición, únicamente ataques conocidos (`firmas.py:5`, `153-154`),
y los 17 tipos 0-day viven solo en D2, que no se toca. Es decir: la fusión por *stacking* puede
sustituir el `UMBRAL_CONF` ad hoc por algo aprendido **para las cuatro categorías conocidas**, pero
**no puede aprender a decir «no sé»**. El problema que `EL_FUTURO.md:60-65` documenta con datos —el
86 % de los 0-day cazados por la etapa 1 se mal-etiquetan con confianza como categoría conocida— es
un problema de **conjunto abierto**, y el *stacking* supervisado no es la herramienta: el
reconocimiento *open-set* sí. Conviene no confundir las dos líneas de `EL_FUTURO.md §2`, porque
atacan cosas distintas.

**Trampa 3 — el meta-clasificador borra la interpretabilidad.** La etapa de firmas existe para
producir reglas legibles (`firmas.py:349`, `export_text` con los nombres reales de las
características). Una capa de fusión encima devuelve una decisión que ya no se explica por una
regla. Es el mismo conflicto que `EL_FUTURO.md:33-39` plantea entre precisión y reglas
interpretables, y hay que nombrarlo, no absorberlo.

**Variantes más baratas y que no arrastran las tres trampas:** el *ensemble* de detectores de la
etapa 1 (`EL_FUTURO.md:47-59`) es una **votación / OR / max-score no supervisada**: no necesita
meta-entrenamiento, no necesita filas normales limpias, y por tanto **esquiva las trampas 1 y 2 por
completo**. Sigue siendo, con diferencia, la propuesta de mejor relación coste/valor de las dos, y
este informe no la mejora: la confirma desde la literatura (TabArena: el *ensemble* entre modelos
diversos supera a cualquier modelo individual).

**Coste, con la vista puesta en `requirements.txt`:** `StackingClassifier` y `VotingClassifier`
están en `scikit-learn` desde la 0.22 y por tanto en la **1.7.1** que fija
`requirements.txt:15`. **Cero dependencias nuevas.** Todo el coste es de protocolo, no de librería.

### Bloque 2b — Mezclar fases: preentrenamiento no supervisado + cabeza supervisada

Este es, como dice el encargo, el enganche más fuerte, porque `EL_FUTURO.md:72-74` ya lo sembró sin
desarrollarlo: «*espacio latente del autoencoder como entrada de la etapa 2*». Es literalmente esta
lectura del término «híbrido de entrenamiento», y merece un aterrizaje completo.

#### 2b.1 El paradigma y su literatura tabular

La idea general —aprender una representación sin etiquetas y luego enganchar una cabeza
supervisada— tiene raíz clásica: [Erhan et al., JMLR 11 (2010), 625-660](https://www.jmlr.org/papers/v11/erhan10a.html)
analizan **por qué** ayuda el preentrenamiento no supervisado y concluyen que actúa como
**regularizador** que sitúa los pesos en una cuenca de atracción favorable, con un efecto que es
**mayor cuanto más profunda es la red y más escasas las etiquetas**. Retén las dos condiciones:
volverán en 2b.2.

Sobre tabular en concreto hay cuatro propuestas con venue revisado:

| Método | Venue | Tarea de pretexto | Escenario que declara su propio resumen |
|---|---|---|---|
| **VIME** ([Yoon et al.](https://proceedings.neurips.cc/paper/2020/hash/7d97667a3e056acab9aaf653807b4a03-Abstract.html)) | NeurIPS 2020 | Estimar el **vector de máscara** además de reconstruir el valor imputado; aumento de datos tabular propio | Auto **y semi**supervisado |
| **SubTab** ([Ucar et al.](https://proceedings.neurips.cc/paper/2021/hash/9c8661befae6dbcd08304dbf4dcaf0db-Abstract.html)) | NeurIPS 2021 | Reconstruir el dato completo desde **subconjuntos de sus características** (multi-vista), no desde una versión corrompida | Representación autosupervisada |
| **SCARF** ([Bahri et al.](https://arxiv.org/abs/2106.15147)) | ICLR 2022 (*spotlight*) | Contrastivo: las vistas se forman **corrompiendo un subconjunto aleatorio de características** | Mejora «*in the presence of label noise and in the semi-supervised setting where only a fraction of the available training data is labeled*» |
| **SAINT** ([Somepalli et al.](https://arxiv.org/abs/2106.01342)) — **nivel 2, preprint** | arXiv 2021 | Preentrenamiento contrastivo + atención por filas y columnas | «*for use when labels are scarce*» |

A los que se suma **TabNet**, cuyo preentrenamiento no supervisado por reconstrucción de
características enmascaradas mejora, según sus autores, «*significantly … when unlabeled data is
abundant*».

#### 2b.2 Cuándo ayuda el preentrenamiento — y por qué aquí no se dan las condiciones

Léase la columna derecha de la tabla anterior como lo que es: **una declaración de régimen por parte
de los propios autores**. Los cinco métodos sitúan su ganancia en escasez de etiquetas, ruido de
etiqueta o abundancia de datos sin etiquetar. Es exactamente la condición que Erhan et al. ya habían
identificado en 2010.

**Ninguna de las tres se da en este proyecto:**

- **No hay escasez de etiquetas.** D3 aporta 58 630 ataques **todos etiquetados**, con su tipo
  concreto y su categoría (`firmas.py:147-154`).
- **No hay ruido de etiqueta** conocido ni denunciado en NSL-KDD para las cinco categorías.
- **No hay datos sin etiquetar.** Cada fila de NSL-KDD trae `attack` y `level`
  (`program.py:37-50`). El único conjunto «sin usar» es D2, y usarlo como corpus no etiquetado sería
  aprendizaje transductivo sobre el test: rompe el protocolo del proyecto y, aunque
  técnicamente no sería *label leakage*, sí sería una fuga de distribución que invalidaría la
  evaluación honesta que es la seña de identidad del TFG.

Y el contrapunto de Rubachev et al. cierra el argumento desde el otro lado: si el hallazgo es que el
preentrenamiento **con conocimiento de la etiqueta** (*target-aware*) es el que rinde, entonces con
58 630 etiquetas en la mano la vía razonable no es preentrenar sin ellas: es usarlas, que es lo que
ya hace `firmas.py`.

#### 2b.3 El latente del autoencoder como entrada de la etapa 2: aterrizaje completo

**Lo que hay hoy.** El autoencoder es un `MLPRegressor` que reconstruye su entrada
(`anomalias.py:12`, `198-199`), con configuración ganadora `hidden_layer_sizes=(64, 32, 64)` en las
**dos** variantes de características (`metricas_anomalias.csv`, filas `Autoencoder`). Su cuello de
botella es por tanto de **32 dimensiones**. La propuesta de `EL_FUTURO.md:72-74` sería alimentar
`firmas.py` con esas 32 en lugar de las 54 actuales.

**A favor, y no es poco.** (i) Coste de cómputo casi nulo: los `.joblib` ya existen y `hibrido.py`
ya demuestra que se pueden cargar sin reentrenar (`hibrido.py:6-9`). (ii) Une conceptualmente las
dos etapas bajo una sola representación, que es un argumento de diseño elegante y defendible en una
memoria. (iii) Es el paradigma clásico de Hinton/Erhan, con literatura de sobra para justificarlo en
prosa.

**En contra, y con esto no basta con marcar la reserva: hay cuatro objeciones y tres son graves.**

1. **El latente está entrenado para reconstruir lo que *no* es un ataque.** El autoencoder se ajusta
   **solo sobre D1**, que es tráfico normal puro (`program.py:166`, `anomalias.py:139`). Un cuello de
   botella entrenado con un objetivo de reconstrucción conserva las direcciones de mayor varianza
   **del tráfico normal** y descarta las que no varían en él. Las direcciones que separan `dos` de
   `probe` de `r2l` de `u2r` no tienen por qué estar entre ellas —y hay razones para pensar que no
   lo están. Es la crítica que DAGMM ([Zong et al., ICLR 2018](https://bzong.github.io/doc/iclr18-dagmm.pdf))
   formaliza para el caso de dos etapas: la reducción de dimensionalidad y la tarea posterior
   entrenadas por separado sufren de «*decoupled model learning with inconsistent optimization goals
   and incapability of preserving essential information in the low-dimensional space*», y su
   propuesta es justamente **optimizar ambas conjuntamente**, que es lo contrario de reutilizar un
   latente ya congelado.

2. **Se llevaría por delante `u2r`, que ya es el eslabón débil.** Este es el argumento decisivo y es
   específico de esta arquitectura. Entre las 54 características sobreviven `root_shell`,
   `num_shells`, `su_attempted`, `num_file_creations`, `num_failed_logins` —y la propia
   `program.py:408-415` documenta por qué se conservaron: son «*indicadores de ataques no vistos …
   que son ~0 en D1*». O sea: **son casi constantes en el único conjunto con el que se entrena el
   autoencoder**. Una característica constante no aporta varianza que reconstruir, y el cuello de
   botella no tiene incentivo alguno para reservarle una dirección. `u2r` tiene hoy `f1` = 0,452 con
   37 muestras en el test (`metricas_firmas.csv`); es difícil imaginar que sobreviva a que su señal
   se comprima con un criterio ciego a ella.

3. **Destruye la extracción de reglas legibles.** `firmas.py:349` exporta el árbol con
   `feature_names=list(self.X_D3.columns)`. Con el latente, esos nombres pasan a ser dimensiones
   anónimas y una «firma» se convierte en `if z_17 > 0.42 and z_03 <= -1.1 → dos`. Eso **no es una
   firma**: es lo contrario de lo que la etapa 2 existe para producir, y anula de paso la línea
   RIPPER de `EL_FUTURO.md:33-39`.

4. **Objeción menor, operativa:** `MLPRegressor` no expone un método `transform()`; el latente no es
   una salida de la API pública, hay que propagarlo a mano por los pesos aprendidos. Es hacedero,
   pero deja de ser «reutilizar un modelo persistido» y pasa a ser código nuevo —y el track de
   código está cerrado.

**Dos variantes que sí sobreviven al escrutinio.** No hay que tirar la idea entera; hay que
reformularla:

- **Concatenar en vez de sustituir.** Añadir las 32 dimensiones a las 54 en lugar de reemplazarlas
  mantiene intacto todo lo que hoy funciona y deja que el RandomForest decida por importancia si el
  latente aporta algo. Es una prueba barata y de riesgo acotado. Pero destruye igualmente la
  legibilidad de las reglas **si el árbol usa las nuevas**, así que hay que medir eso además del
  `f1_macro`.
- **★ Pasar el vector de error de reconstrucción por característica, no el latente.** Esta es la
  variante que este informe propone como la buena, y no está escrita en `EL_FUTURO.md`. El *score*
  de anomalía actual es el **MSE de reconstrucción agregado** (`anomalias.py:216-218`): un solo
  número que resume 54 errores. Ese vector de 54 errores —antes de agregarlo— tiene tres
  propiedades que el latente no tiene: (a) **es interpretable por construcción**, porque cada
  componente lleva el nombre de una característica real, así que una regla del tipo
  `if err_num_shells alto → u2r` **sigue siendo una firma legible**; (b) **conserva exactamente la
  información que sí discrimina**, porque un error de reconstrucción grande significa «esto no se
  parece a nada de D1», que es la señal de ataque; y (c) **es la unión conceptual entre las dos
  etapas que buscaba `EL_FUTURO.md:72-74`**, pero por el lado correcto: la etapa 2 recibe *en qué*
  se equivocó la etapa 1, no *qué comprimió*. Es, además, el único punto de este informe que podría
  ayudar al recall 0-day, porque un 0-day es por definición algo que el detector no sabe
  reconstruir.

#### 2b.4 Semisupervisado: la premisa no se da

Por completar el subbloque, con la referencia canónica:
[van Engelen y Hoos, *Machine Learning* 109, 373-440 (2020)](https://doi.org/10.1007/s10994-019-05855-6)
definen el aprendizaje semisupervisado como el uso de datos **etiquetados y no etiquetados** para
la misma tarea. **En este proyecto no hay datos no etiquetados**: la premisa entera del paradigma
está ausente (§2b.2). Cualquier mención en 6.2 debe formularse como *condicional a otro dataset*,
nunca como aplicable a NSL-KDD.

Una precisión de vocabulario que sí importa y que ya está cerrada: la etapa 1 **no** es
semisupervisada en el sentido de van Engelen y Hoos; es **semisupervisada one-class**, término
canónico fijado en `resumen-de-decisiones.md:453-462`. Son cosas distintas y conviene no mezclarlas
en la misma frase de 6.2.

### Bloque 3 — Tratamiento de las variables categóricas

#### 3.1 Cuánto pesa hoy el One-Hot en este pipeline (los números, verificados en disco)

Tres columnas categóricas —`protocol_type`, `service`, `flag` (`program.py:53`)— pasan por
`pd.get_dummies` (`program.py:283`) con alineación por la unión de columnas de D1+D3
(`program.py:292-305`). El resultado es cuantificable:

| | Recuento |
|---|---|
| Características numéricas originales | 41 − 3 = **38** |
| *Dummies* generados | `protocol_type` (3) + `flag` (11) + `service` (**70**) = **84** |
| Total tras el one-hot | 38 + 84 = **122** (`selected_features.txt:8`) |
| *Dummies* que sobreviven a la selección | **26** de 84 (15 `service_*`, 8 `flag_*`, 3 `protocol_type_*`) |
| Numéricas que sobreviven | 28 |
| Total final | **54** (`selected_features.txt:12`) |

Dos lecturas de esa tabla, ambas relevantes:

- **El one-hot es responsable del 69 % del espacio de características** (84 de 122). La «maldición
  de dimensionalidad» de este pipeline no viene de los datos: viene de la codificación.
- **De las 60 características eliminadas por importancia, 58 son *dummies*** (55 `service_*`, 3
  `flag_*`) y solo 2 son numéricas (`land`, `is_host_login`) —`selected_features.txt:90-151`. Es
  decir: la selección de características de 4.3.5 es, en la práctica, **un mecanismo de poda del
  one-hot de `service`**.

`service`, con **70 niveles**, es el caso de manual de *característica de alta cardinalidad* que
toda la literatura de este bloque estudia.

#### 3.2 Target encoding

**Qué es y de dónde viene.** [Micci-Barreca, *SIGKDD Explorations* 3(1), 27-32
(2001)](https://doi.org/10.1145/507533.507538) propone sustituir cada nivel por un estadístico del
destino condicionado a ese nivel, encogido hacia la media global mediante un estimador **Bayes
empírico**. Una columna de 70 niveles se convierte en **una sola columna numérica**.

**Qué dice la evidencia comparativa.** [Pargent, Pfisterer, Thomas y Bischl, *Computational
Statistics* 37(5), 2671-2692 (2022)](https://doi.org/10.1007/s00180-022-01207-6) es el *benchmark*
de referencia: cinco algoritmos (lasso, random forest, gradient boosting, k-NN, SVM) sobre tareas de
regresión y clasificación binaria y multiclase. Conclusión textual: «*regularized versions of target
encoding … consistently provided the best results*», y —textual también— las codificaciones
tradicionales «*to reduce the number of levels … before creating binary indicator variables (one-hot
or dummy encoding) were not as effective in comparison*». Nótese que **RandomForest y gradient
boosting están entre los cinco aprendices evaluados**: el resultado no es «target encoding para
redes».

**Disponibilidad, coste cero.** `sklearn.preprocessing.TargetEncoder` existe desde la **1.3** (el
soporte multiclase, desde la **1.4**), y el proyecto fija **`scikit-learn==1.7.1`**
(`requirements.txt:15`): **está disponible sin añadir una sola dependencia**. Su punto crítico es el
mismo que el del *stacking*: la
[documentación oficial](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.TargetEncoder.html)
advierte que `fit(X, y).transform(X)` **no** equivale a `fit_transform(X, y)`, porque este último
aplica un esquema de **ajuste cruzado interno** para evitar la fuga del destino. Usar el par
`fit`+`transform` sobre el train es la forma silenciosa de inflar los resultados.

**El bloqueo estructural que tiene aquí, y que no está documentado en ningún sitio.** El *target
encoding* necesita un destino. **La etapa 1 no tiene destino**: D1 es tráfico normal puro
(`program.py:166`), una sola clase; no hay nada que promediar. Y la decisión Q1/C se cerró en la
**opción A —el mismo set de características para las dos etapas**
(`resumen-de-decisiones.md:373-389`). Las dos cosas juntas dejan solo dos salidas, y ninguna es
gratis:

- Ajustar el codificador sobre **D1+D3 con el destino de 5 categorías** —lo que reintroduce
  exactamente el problema ya medido en `EL_FUTURO.md:77-89`: una transformación supervisada que
  **ciega parcialmente al detector no supervisado**.
- Romper la opción A y usar codificaciones distintas por etapa —que es la **opción B**, hoy
  clasificada como «vía correcta pendiente» con ganancia esperada pequeña.

Es una observación, no una reapertura: la decisión de 54/opción A **no queda desmentida** por este
informe (ver `## Implicaciones`). Pero cualquier mención del *target encoding* en 6.2 tiene que
llevar esta condición pegada, o es una propuesta que no se sostiene al primer examen.

#### 3.3 Manejo nativo por el modelo: CatBoost y `HistGradientBoosting`

**El argumento teórico contra el one-hot en árboles**, en palabras de la
[documentación oficial de LightGBM](https://lightgbm.readthedocs.io/en/latest/Features.html):

> «*It is common to represent categorical features with one-hot encoding, but this approach is
> suboptimal for tree learners. Particularly for high-cardinality categorical features, a tree built
> on one-hot features tends to be unbalanced and needs to grow very deep to achieve good accuracy.*»

La alternativa es partir sobre **subconjuntos de categorías** en un solo nodo, con el criterio de
agrupación óptima de Fisher (1958) y coste `O(k·log k)` para `k` categorías. Con `service` a 70
niveles, un árbol one-hot necesita hasta 70 cortes binarios encadenados para expresar lo que un
corte categórico expresa en uno.

**CatBoost** ([Prokhorenkova et al., NeurIPS 2018](https://proceedings.neurips.cc/paper/2018/hash/14491b756b3a51daac41c24863285549-Abstract.html))
lleva esto más lejos: sus dos aportaciones —*ordered boosting* y **estadísticos de destino
ordenados** para las categóricas— existen precisamente para combatir el **desplazamiento de
predicción causado por la fuga del destino** que sufren las implementaciones anteriores. Es decir:
CatBoost es *target encoding* hecho bien, integrado en el modelo. Coste: **dependencia nueva**, fuera
de `requirements.txt`.

**`HistGradientBoosting` ya está en el sistema y ya soporta categóricas de forma nativa.** Su
parámetro `categorical_features` acepta máscara booleana, índices, nombres o `'from_dtype'`
—[documentación oficial](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html);
añadido en la 0.24, `'from_dtype'` en la 1.4 y valor por defecto desde la **1.6**, luego **activo en
la 1.7.1 del proyecto**— y el modelo hace **particiones sobre las categorías directamente**, sin
one-hot. El límite documentado, `max_bins` categorías por característica (255 por defecto), deja
holgadísimos los 70 niveles de `service`.

**Por qué no es «gratis» pese a estar disponible.** Tres obstáculos, en orden de peso, y ninguno es
de código:

1. **El one-hot ocurre antes de que ningún modelo vea los datos.** `program.py:283` codifica y
   `program.py` escribe los CSV procesados; `firmas.py` consume `splits["D3"]["X"]` ya codificado
   (`firmas.py:148`). Para usar el soporte nativo, las columnas crudas `service`/`flag`/
   `protocol_type` tendrían que sobrevivir hasta la etapa 2 —lo que cambia el contrato de
   `load_specialized_splits()`, del que dependen **los cuatro** scripts de modelos.
2. **Rompe el protocolo de comparación homogénea.** De los cuatro algoritmos de la etapa 2
   (`firmas.py:66`), **solo HistGradientBoosting** admite categóricas nativas: DecisionTree,
   RandomForest y KNN de `sklearn` no. Darle a uno una representación distinta invalida la tabla
   comparativa de 5.2, cuya garantía es que los cuatro ven exactamente lo mismo.
3. **Tendría que reejecutarse también la selección de características**, porque 4.3.5 opera sobre
   los *dummies* (§3.1) y sin ellos no hay nada que podar.

Traducido: **es una decisión de arquitectura del pipeline, no un parámetro**. Encaja como línea
futura; no como retoque.

#### 3.4 Embeddings aprendidos y arquitectura de dos ramas

Los dos subtemas restantes del bloque, que en la práctica son el mismo.

**Embeddings de entidad.** [Guo y Berkhahn (2016), arXiv:1604.06737](https://arxiv.org/abs/1604.06737)
—**nivel 2, preprint**— proponen mapear cada nivel categórico a un vector denso aprendido por
descenso de gradiente junto con la tarea. Su argumento no es solo la compresión: «*by mapping similar
values close to each other in the embedding space it reveals the intrinsic properties of the
categorical variables*». Sobre NSL-KDD esto sería sustantivo: `service_http`, `service_http_443` y
`service_http_8001` son hoy tres columnas **ortogonales**, sin ninguna relación entre sí para el
modelo, cuando semánticamente son casi lo mismo. Un embedding las acercaría.

**La arquitectura de dos ramas.** Es un patrón consolidado, con dos representantes citables:

- **Wide & Deep** ([Cheng et al., DLRS @ RecSys 2016](https://doi.org/10.1145/2988450.2988454)):
  entrena **conjuntamente** un modelo lineal ancho —que **memoriza** coocurrencias concretas— y una
  red profunda sobre embeddings —que **generaliza**. Es la formulación canónica del reparto de
  trabajo entre las dos ramas, y su vocabulario (memorización / generalización) traduce
  sorprendentemente bien al reparto firmas / anomalías de este TFG.
- **TabTransformer** (Huang et al., 2020 — **nivel 2, preprint**;
  [ficha en Semantic Scholar](https://www.semanticscholar.org/paper/a2ec47b9bcc95d2456a8a42199233e5d9129ef18)):
  es literalmente la arquitectura de dos ramas que pide el encargo. Las **categóricas** pasan por
  embeddings y un codificador Transformer que las contextualiza; las **numéricas** se normalizan
  aparte y se concatenan justo antes de la cabeza de predicción.
- **FT-Transformer** (Gorishniy et al., NeurIPS 2021) generaliza la idea con un *feature tokenizer*
  que convierte **cada** característica —numérica o categórica— en un token, eliminando la asimetría
  entre ramas.

**Evaluación para este proyecto: no compensa, y por tres razones acumulativas.**

1. **Todas exigen PyTorch**, con lo que arrastran las cinco rupturas ya inventariadas para el
   autoencoder en [[aprendizaje-continuo-nested-learning]] §C: protocolo homogéneo, persistencia
   `.joblib` que `hibrido.py` consume, `requirements.txt` fijado, la prohibición explícita de
   `anomalias.py:12`, y la reapertura del track de código.
2. **El *benchmark* del bloque 1 ya dictaminó sobre ellas**: FT-Transformer y TabTransformer son
   exactamente los modelos que Shwartz-Ziv y Armon y Grinsztajn et al. midieron y encontraron por
   debajo de los árboles en este régimen.
3. **No resuelven el problema que este sistema tiene**, que es el 0-day. Un embedding aprendido sobre
   D3 **no tiene vector para un servicio que no apareció en D3** —el mismo problema de arranque en
   frío que el one-hot, sin ninguna mejora. Y sobre este dataset el problema es real: la alineación
   de columnas descarta a propósito las categorías exclusivas de D2 (`program.py:292-296`).

#### 3.5 El enganche del bloque 3 con el recall 0-day (hipótesis, con su confusor declarado)

Este es el hallazgo con más recorrido del bloque, y hay que enunciarlo con cuidado porque es una
correlación, no una demostración.

**El hecho.** Entre las 55 columnas `service_*` que la selección elimina por importancia figuran
`service_X11` (0,000042), `service_domain` (0,000028), `service_echo` (0,000007) y `service_sql_net`
(0,000001) —`selected_features.txt:97, 103, 119, 147`.

**La coincidencia.** Tres de los 17 tipos 0-day operan justo sobre esos servicios, y el recall del
detector sobre ellos **sube de forma marcada** cuando se conservan las 122 características
(`metricas_hibrido_0day.csv`, filas `Autoencoder`):

| Tipo 0-day | n | Recall AE, 54 | Recall AE, 122 |
|---|---|---|---|
| `xlock` (X11) | 9 | 0,333 | **0,778** |
| `xsnoop` (X11) | 4 | 0,750 | **1,000** |
| `named` (DNS) | 17 | 0,529 | **0,765** |
| `mailbomb` | 293 | 0,000 | 0,123 (ya recogido en `EL_FUTURO.md:86-89`) |

**La hipótesis.** La poda supervisada del one-hot elimina indicadores de servicios raros que, siendo
irrelevantes para clasificar los ataques **conocidos** de D3, son precisamente los que delatan
ataques **no vistos**. Es la misma lógica que `program.py:408-415` ya usó para subir el umbral de
importancia acumulada del 99 % al 99,9 %, aplicada un escalón más abajo.

**El confusor, declarado.** La variante de 122 cambia **todo** el espacio de características, no solo
esos cuatro *dummies*. La tabla es **consistente** con la hipótesis; no la prueba. Para probarla
haría falta un experimento de ablación que este informe **no propone** (track de código cerrado).

**Por qué esto conecta con el bloque 3 y no es solo un comentario sobre selección de características.**
Porque el *target encoding* **hace desaparecer el problema por construcción**: si `service` es **una
columna numérica** en vez de 70 indicadores, ningún selector basado en importancias puede tirar
`X11` por su cuenta —o entra la columna entera o no entra ninguna, y con una importancia agregada
que sería alta. La codificación no es un detalle de preprocesado: **determina qué puede podar el
selector**, y aquí ha podado señal de 0-day.

## Lo que no he podido confirmar

- **Texto completo de Shwartz-Ziv y Armon (2022).** Elsevier está tras muro de pago y no lo he
  sorteado. El DOI resuelve y los metadatos están verificados vía OpenAlex; **el resumen íntegro,
  del que salen las dos citas textuales que uso, está verificado vía la API de Semantic Scholar**,
  que refleja el registro del editor. Todo lo que afirmo de esa fuente sale del **resumen**, no del
  cuerpo.
- **Textos completos de Grinsztajn et al., McElfresh et al., TabArena, Kadra et al., VIME, SubTab,
  SCARF, DAGMM, CatBoost, NODE y TabM.** He trabajado con **resúmenes y páginas de actas**
  verificados en `proceedings.neurips.cc`, `proceedings.iclr.cc` y arXiv. Las citas textuales que
  entrecomillo proceden de esos resúmenes. No he leído las secciones experimentales.
- **Los rangos de página exactos** de Grinsztajn et al. (NeurIPS 2022 D&B) y de McElfresh et al.
  (NeurIPS 2023 D&B). Las actas de las pistas de *Datasets and Benchmarks* de NeurIPS no publican
  paginación consistente; cito por URL de actas, que es la forma canónica en ese venue.
- **El venue de TabPFN v1.** Lo he leído en su página de arXiv (nivel 2). Múltiples fuentes
  secundarias lo dan como ICLR 2023, pero **no lo he verificado contra las actas** en esta sesión.
  Lo trato como nivel 2 y los límites que cito (≤1 000 muestras, ≤100 características, ≤10 clases)
  salen del resumen de arXiv.
- **El identificador de arXiv de TabTransformer.** No lo he verificado; lo cito por su ficha de
  Semantic Scholar y lo clasifico nivel 2. La descripción de su arquitectura de dos ramas está
  contrastada en dos fuentes independientes.
- **Las cifras de rendimiento de TabPFN-2.6 y TabPFN-3.** Salen de la documentación del fabricante
  (Prior Labs). Los **límites de tamaño** los tomo como documentación oficial (nivel 1); cualquier
  **afirmación de superioridad** de ese mismo origen lleva **sesgo comercial** y no la uso para
  sostener nada.
- **Fisher (1958), «On Grouping for Maximum Homogeneity».** No he verificado sus metadatos de forma
  independiente: lo cito **como referencia interna de la documentación de LightGBM**, que es donde lo
  he leído. Si Francisco quisiera citarlo en la memoria, hay que verificarlo antes.
- **Que la hipótesis de §3.5 sea causal.** Es una correlación entre cuatro *dummies* eliminados y
  tres tipos 0-day mejorados en la variante de 122. El confusor está declarado en el propio hallazgo.
  **No hay experimento que lo separe** y este informe no lo propone.
- **Evidencia publicada de que un latente de autoencoder entrenado solo con la clase negativa
  perjudique a un clasificador multiclase aguas abajo.** El argumento de §2b.3 es **razonamiento
  propio apoyado en dos fuentes** (el diagnóstico de desacoplamiento de DAGMM y el hallazgo
  *target-aware* de Rubachev et al.), no un resultado publicado sobre este caso concreto. Lo señalo
  para que no se cite como si lo fuera.

## Fuentes

| # | Fuente | Nivel | Fecha | Cita completa | URL / DOI |
|---|---|---|---|---|---|
| 1 | Tabular data: Deep learning is not all you need | **1** | 2022 (en línea 2021-06) | R. Shwartz-Ziv y A. Armon, *Information Fusion*, vol. 81, pp. 84-90, 2022 | doi:10.1016/j.inffus.2021.11.011 |
| 2 | Why do tree-based models still outperform deep learning on tabular data? | **1** | 2022-12 | L. Grinsztajn, E. Oyallon y G. Varoquaux, en *Advances in Neural Information Processing Systems 35 (NeurIPS 2022)*, Datasets and Benchmarks Track | https://proceedings.neurips.cc/paper_files/paper/2022/file/0378c7692da36807bdec87ab043cdadc-Paper-Datasets_and_Benchmarks.pdf · preprint doi:10.48550/arXiv.2207.08815 |
| 3 | When Do Neural Nets Outperform Boosted Trees on Tabular Data? | **1** | 2023-12 | D. McElfresh, S. Khandagale, J. Valverde, V. Prasad C., G. Ramakrishnan, M. Goldblum y C. White, en *Advances in Neural Information Processing Systems 36 (NeurIPS 2023)*, Datasets and Benchmarks Track | https://proceedings.neurips.cc/paper_files/paper/2023/hash/f06d5ebd4ff40b40dd97e30cee632123-Abstract-Datasets_and_Benchmarks.html |
| 4 | Well-tuned Simple Nets Excel on Tabular Datasets | **1** | 2021-12 | A. Kadra, M. Lindauer, F. Hutter y J. Grabocka, en *Advances in Neural Information Processing Systems 34 (NeurIPS 2021)* | https://proceedings.neurips.cc/paper/2021/hash/c902b497eb972281fb5b4e206db38ee6-Abstract.html |
| 5 | TabArena: A Living Benchmark for Machine Learning on Tabular Data | **1** | 2025-12 (preprint 2025-06-20) | N. Erickson, L. Purucker, A. Tschalzev, D. Holzmüller, P. Mutalik Desai, D. Salinas y F. Hutter, en *Advances in Neural Information Processing Systems 39 (NeurIPS 2025)*, Datasets and Benchmarks Track (*spotlight*) | https://arxiv.org/abs/2506.16791 · actas: https://papers.neurips.cc/paper_files/paper/2025/file/1697e3fb412da11dc9488249f9e7bbc9-Paper-Datasets_and_Benchmarks_Track.pdf |
| 6 | TabNet: Attentive Interpretable Tabular Learning | **1** | 2021-05 | S. Ö. Arik y T. Pfister, *Proceedings of the AAAI Conference on Artificial Intelligence*, vol. 35, n.º 8, pp. 6679-6687, 2021 | doi:10.1609/aaai.v35i8.16826 |
| 7 | Revisiting Deep Learning Models for Tabular Data (FT-Transformer) | **1** | 2021-12 | Y. Gorishniy, I. Rubachev, V. Khrulkov y A. Babenko, en *Advances in Neural Information Processing Systems 34 (NeurIPS 2021)*, pp. 18932-18943 | https://arxiv.org/abs/2106.11959 · actas: https://dl.acm.org/doi/10.5555/3540261.3541708 |
| 8 | Neural Oblivious Decision Ensembles for Deep Learning on Tabular Data (NODE) | **1** | 2020-04 | S. Popov, S. Morozov y A. Babenko, en *8th International Conference on Learning Representations (ICLR 2020)* | https://arxiv.org/abs/1909.06312 |
| 9 | SAINT: Improved Neural Networks for Tabular Data via Row Attention and Contrastive Pre-Training | 2 | 2021-06 | G. Somepalli, M. Goldblum, A. Schwarzschild, C. B. Bruss y T. Goldstein. **Preprint arXiv, sin venue revisado localizado** | https://arxiv.org/abs/2106.01342 |
| 10 | Accurate predictions on small data with a tabular foundation model (TabPFN v2) | **1** | 2025-01 | N. Hollmann, S. Müller, L. Purucker, A. Krishnakumar, M. Körfer, S. B. Hoo, R. T. Schirrmeister y F. Hutter, *Nature*, vol. 637, n.º 8045, pp. 319-326, 2025 | doi:10.1038/s41586-024-08328-6 |
| 11 | TabPFN: A Transformer That Solves Small Tabular Classification Problems in a Second (v1) | 2 | 2022-07 | N. Hollmann, S. Müller, K. Eggensperger y F. Hutter. **Preprint arXiv; venue ICLR 2023 no verificado en esta sesión** | https://arxiv.org/abs/2207.01848 |
| 12 | Prior Labs — documentación oficial de los modelos TabPFN | **1** (documentación oficial) | consultada 2026-08-02 | Prior Labs, «Models». **Sesgo comercial: uso solo los límites de tamaño, no las afirmaciones de superioridad** | https://docs.priorlabs.ai/models |
| 13 | TabM: Advancing Tabular Deep Learning with Parameter-Efficient Ensembling | **1** | 2025-04 | Y. Gorishniy, A. Kotelnikov y A. Babenko, en *13th International Conference on Learning Representations (ICLR 2025)* | https://proceedings.iclr.cc/paper_files/paper/2025/hash/c1ba41c694834aeef91ae161711d4939-Abstract-Conference.html |
| 14 | XGBoost: A Scalable Tree Boosting System | **1** | 2016-08 | T. Chen y C. Guestrin, en *Proc. 22nd ACM SIGKDD Int. Conf. on Knowledge Discovery and Data Mining*, San Francisco, pp. 785-794, 2016 | doi:10.1145/2939672.2939785 |
| 15 | LightGBM: A Highly Efficient Gradient Boosting Decision Tree | **1** | 2017-12 | G. Ke, Q. Meng, T. Finley, T. Wang, W. Chen, W. Ma, Q. Ye y T.-Y. Liu, en *Advances in Neural Information Processing Systems 30 (NIPS 2017)*, pp. 3146-3154 | https://papers.nips.cc/paper/6907-lightgbm-a-highly-efficient-gradient-boosting-decision-tree |
| 16 | CatBoost: unbiased boosting with categorical features | **1** | 2018-12 | L. Prokhorenkova, G. Gusev, A. Vorobev, A. V. Dorogush y A. Gulin, en *Advances in Neural Information Processing Systems 31 (NeurIPS 2018)*, pp. 6639-6649 | https://proceedings.neurips.cc/paper/2018/hash/14491b756b3a51daac41c24863285549-Abstract.html |
| 17 | Stacked generalization | **1** | 1992 | D. H. Wolpert, *Neural Networks*, vol. 5, n.º 2, pp. 241-259, 1992 | doi:10.1016/S0893-6080(05)80023-1 |
| 18 | Stacked regressions | **1** | 1996 | L. Breiman, *Machine Learning*, vol. 24, n.º 1, pp. 49-64, 1996 | doi:10.1007/BF00117832 |
| 19 | AutoGluon-Tabular: Robust and Accurate AutoML for Structured Data | 2 | 2020-03 | N. Erickson, J. Mueller, A. Shirkov, H. Zhang, P. Larroy, M. Li y A. Smola. **Preprint arXiv de empresa (AWS): sesgo comercial declarado** | https://arxiv.org/abs/2003.06505 |
| 20 | VIME: Extending the Success of Self- and Semi-supervised Learning to Tabular Domain | **1** | 2020-12 | J. Yoon, Y. Zhang, J. Jordon y M. van der Schaar, en *Advances in Neural Information Processing Systems 33 (NeurIPS 2020)* | https://proceedings.neurips.cc/paper/2020/hash/7d97667a3e056acab9aaf653807b4a03-Abstract.html |
| 21 | SubTab: Subsetting Features of Tabular Data for Self-Supervised Representation Learning | **1** | 2021-12 | T. Ucar, E. Hajiramezanali y L. Edwards, en *Advances in Neural Information Processing Systems 34 (NeurIPS 2021)* | https://proceedings.neurips.cc/paper/2021/hash/9c8661befae6dbcd08304dbf4dcaf0db-Abstract.html |
| 22 | SCARF: Self-Supervised Contrastive Learning using Random Feature Corruption | **1** | 2022-04 | D. Bahri, H. Jiang, Y. Tay y D. Metzler, en *10th International Conference on Learning Representations (ICLR 2022)*, *spotlight* | https://iclr.cc/virtual/2022/spotlight/6297 · preprint https://arxiv.org/abs/2106.15147 |
| 23 | Revisiting Pretraining Objectives for Tabular Deep Learning | 2 | 2022-07 | I. Rubachev, A. Alekberov, Y. Gorishniy y A. Babenko. **Preprint arXiv (CoRR abs/2207.03208), sin venue revisado** | https://arxiv.org/abs/2207.03208 |
| 24 | Why Does Unsupervised Pre-training Help Deep Learning? | **1** | 2010-02 | D. Erhan, Y. Bengio, A. Courville, P.-A. Manzagol, P. Vincent y S. Bengio, *Journal of Machine Learning Research*, vol. 11, pp. 625-660, 2010 | https://www.jmlr.org/papers/v11/erhan10a.html · https://dl.acm.org/doi/10.5555/1756006.1756025 |
| 25 | Deep Autoencoding Gaussian Mixture Model for Unsupervised Anomaly Detection (DAGMM) | **1** | 2018-04 | B. Zong, Q. Song, M. R. Min, W. Cheng, C. Lumezanu, D. Cho y H. Chen, en *6th International Conference on Learning Representations (ICLR 2018)* | https://bzong.github.io/doc/iclr18-dagmm.pdf · https://iclr.cc/virtual/2018/poster/126 |
| 26 | A survey on semi-supervised learning | **1** | 2020 | J. E. van Engelen y H. H. Hoos, *Machine Learning*, vol. 109, n.º 2, pp. 373-440, 2020 | doi:10.1007/s10994-019-05855-6 |
| 27 | A preprocessing scheme for high-cardinality categorical attributes in classification and prediction problems | **1** | 2001-07 | D. Micci-Barreca, *ACM SIGKDD Explorations Newsletter*, vol. 3, n.º 1, pp. 27-32, 2001 | doi:10.1145/507533.507538 |
| 28 | Regularized target encoding outperforms traditional methods in supervised machine learning with high cardinality features | **1** | 2022-11 | F. Pargent, F. Pfisterer, J. Thomas y B. Bischl, *Computational Statistics*, vol. 37, n.º 5, pp. 2671-2692, 2022 | doi:10.1007/s00180-022-01207-6 |
| 29 | Entity Embeddings of Categorical Variables | 2 | 2016-04 | C. Guo y F. Berkhahn. **Preprint arXiv:1604.06737, sin venue revisado** | https://arxiv.org/abs/1604.06737 |
| 30 | TabTransformer: Tabular Data Modeling Using Contextual Embeddings | 2 | 2020-12 | X. Huang, A. Khetan, M. Cvitkovic y Z. Karnin. **Preprint; identificador de arXiv no verificado en esta sesión** | https://www.semanticscholar.org/paper/a2ec47b9bcc95d2456a8a42199233e5d9129ef18 |
| 31 | Wide & Deep Learning for Recommender Systems | **1** | 2016-09 | H.-T. Cheng, L. Koc, J. Harmsen, T. Shaked, T. Chandra, H. Aradhye *et al.*, en *Proc. 1st Workshop on Deep Learning for Recommender Systems (DLRS 2016)*, ACM, pp. 7-10 | doi:10.1145/2988450.2988454 |
| 32 | scikit-learn — `HistGradientBoostingClassifier` (documentación oficial) | **1** | consultada 2026-08-02 | Parámetro `categorical_features`: añadido en 0.24, `'from_dtype'` en 1.4, por defecto desde 1.6; límite `max_bins` categorías por característica | https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html |
| 33 | scikit-learn — `TargetEncoder` (documentación oficial) | **1** | consultada 2026-08-02 | Añadido en 1.3 (multiclase en 1.4). Ajuste cruzado interno en `fit_transform` para evitar la fuga del destino; parámetros `smooth` y `cv` | https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.TargetEncoder.html |
| 34 | LightGBM — «Optimal Split for Categorical Features» (documentación oficial) | **1** | consultada 2026-08-02 | Argumento contra el one-hot en aprendices de árbol; criterio de Fisher (1958); coste `O(k·log k)` | https://lightgbm.readthedocs.io/en/latest/Features.html |

**Evidencia interna (no son fuentes externas; verificada en disco el 2026-08-02):**
`Implementacion/app/program.py:37-50, 53, 166, 283, 292-305, 390-415` ·
`Implementacion/app/anomalias.py:12, 41-45, 77-79, 89, 139, 198-199, 216-218, 259-261` ·
`Implementacion/app/firmas.py:5, 66, 89-98, 147-154, 349` · `Implementacion/app/hibrido.py:6-9, 184-192` ·
`Implementacion/requirements.txt:15` · `Resultados/selected_features.txt:8-70, 90-151` ·
`Resultados/metricas_anomalias.csv` · `Resultados/metricas_firmas.csv` ·
`Resultados/metricas_hibrido.csv` · `Resultados/metricas_hibrido_0day.csv` ·
`resumen-de-decisiones.md:373-389, 453-462` · `EL_FUTURO.md:33-39, 47-68, 72-74, 77-89` ·
`Obsidian_TFG_Vault/04 Implementación del sistema/4.3 Preprocesamiento de los datasets.md:225-229`.

## Cambios en Bibliografía.md

**Ninguno.** Por encargo explícito: `Bibliografía.md` está bajo auditoría abierta
(`features.md:22-27`) y no se toca en este ciclo. Las 34 fuentes quedan completas y clasificadas en
la tabla `## Fuentes`; el trasvase, si Francisco decide citar alguna, se hará al cerrar esa
auditoría.

## Implicaciones para el proyecto

> [!warning] Propongo, no decido
> Nada de esta sección crea tarea, toca código ni reabre el track de código —cerrado el 2026-07-16.
> Es material para que Francisco nutra `EL_FUTURO.md` y escriba 6.2.

### A. Qué NO contradice de `resumen-de-decisiones.md`

**Ninguna decisión cerrada queda desmentida.** Tres quedan, de hecho, **reforzadas** por la
literatura, y merece la pena tenerlo a mano porque son las que un tribunal puede cuestionar:

- **H-3** (clasificador de la etapa 2 = **RandomForest**, `resumen-de-decisiones.md:218-237`). El
  cuadro de §1.4 dice que este problema cae en el cuadrante donde los árboles ganan, por los cinco
  criterios de McElfresh et al. La elección de RF deja de ser «lo que hace todo el mundo» y pasa a
  ser **la opción que la evidencia publicada respalda para este régimen** —que es un argumento
  bastante mejor en una defensa.
- **Decisión 2 / `anomalias.py:12`** (autoencoder como `MLPRegressor`, prohibido TF/Keras). Todo
  el bloque 1 y el §3.4 confirman que salir a PyTorch tiene un coste alto y un beneficio no
  respaldado en este régimen.
- **Q6** (no cruzar ejes experimentales, `resumen-de-decisiones.md:118-128`). Cualquiera de estas
  líneas futuras cruzaría dos o tres ejes a la vez si se aborda sin disciplina.

**Una observación —no una reapertura— sobre la decisión Q1/C (54 características, opción A,
`resumen-de-decisiones.md:373-389`).** El §3.2 encuentra que el *target encoding* es **estructuralmente
incompatible con la opción A**, porque la etapa 1 no tiene destino sobre el que ajustarlo (D1 es una
sola clase). Eso **no desmiente** la decisión: la decisión se tomó sobre one-hot, que es lo que hay,
y sigue siendo correcta con la evidencia con la que se tomó. Lo que hace es **añadir una razón nueva
a favor de la opción B** (sets distintos por etapa), que `EL_FUTURO.md:77-89` ya tenía identificada
como «la vía correcta pendiente»: si algún día se quiere cambiar la codificación de categóricas,
la opción A la bloquea. Lo mismo vale, por otro camino, para el §3.5. Decide Francisco si eso mueve
algo.

### B. Ranking coste / aporte de los candidatos a línea futura

Ordenados por relación coste-valor. «Nuevas deps» distingue lo que cabe en `scikit-learn==1.7.1` de
lo que no.

| # | Candidato | Bloque | Nuevas deps | Coste | Qué aportaría a **este** sistema | Efecto previsible en el **recall 0-day** | Veredicto |
|---|---|---|---|---|---|---|---|
| 1 | **★ Vector de error de reconstrucción por característica como entrada extra de la etapa 2** | 2b | **Ninguna** | Bajo-medio | Une las dos etapas por el lado correcto, **conservando reglas legibles** | **Potencialmente positivo** — el error alto es la firma de lo no visto | **La mejor de este informe.** No está en `EL_FUTURO.md` |
| 2 | **Target encoding de `service`** (contra `EL_FUTURO.md:77-89`) | 3 | **Ninguna** (`TargetEncoder`, sklearn ≥1.3) | Medio | 122 → ~41 características sin poda; el selector ya no puede tirar `service_X11` suelto | **Potencialmente positivo** (hipótesis §3.5) | **Fuerte, con la condición del §3.2**: exige romper la opción A o aceptar sesgo supervisado en el detector |
| 3 | **Ensemble de detectores de la etapa 1** (ya es la ★ nº1 de `EL_FUTURO.md:47-59`) | 2a | **Ninguna** | Bajo | Nada nuevo que decir; **este informe la confirma desde fuera** (TabArena) | Positivo, ya medido por tipo | **Sigue siendo la nº 1.** No la desplaza nada de aquí |
| 4 | **Concatenar el latente del AE a las 54** (variante suave de `EL_FUTURO.md:72-74`) | 2b | Ninguna | Medio | Riesgo acotado: el RF decide por importancia si el latente aporta | Neutro | Aceptable como experimento, **no como tesis** |
| 5 | **Añadir un GBDT externo (LightGBM/CatBoost) al comparador de la etapa 2** | 1 + 3 | **Sí** (1 librería) | Medio | CatBoost daría de paso el manejo nativo de categóricas del §3.3 | Desconocido | **Defendible**, pero HistGB ya está y no despega (§1.4) |
| 6 | **Fusión por meta-clasificador / *stacking*** (`EL_FUTURO.md:66-68`) | 2a | Ninguna | **Alto** (de protocolo) | Responde una pregunta de diseño legítima | **No ataca el 0-day** (trampa 2) | **Rebajar la expectativa.** Ver §2a.3: tres trampas, y no es la herramienta para `unknown` |
| 7 | **Sustituir las 54 por el latente de 32** (lectura literal de `EL_FUTURO.md:72-74`) | 2b | Ninguna | Medio | Elegancia conceptual | **Probablemente negativo**, sobre todo en `u2r` | **No compensa.** Ver §2b.3, objeciones 1-3 |
| 8 | **TabNet / FT-Transformer / SAINT / TabTransformer / NODE / TabM** | 1 + 3 | **Sí** (PyTorch) | **Muy alto** | Ninguno respaldado en este régimen | Desconocido, sin evidencia en ninguna dirección | **No compensa.** Mencionar en 6.2 **como descartado con razón**, no como pendiente |
| 9 | **TabPFN** | 1 | **Sí** (PyTorch + pesos) | Alto | La v2 de *Nature* **ni siquiera admite D3** (58 630 > 10 000) | Desconocido | **No aplicable hoy.** Reevaluable si se migra a un dataset menor |
| 10 | **Aprendizaje semisupervisado** | 2b | Varía | — | **La premisa no existe: no hay datos sin etiquetar** (§2b.4) | — | **Descartado.** Solo mencionable condicionado a otro dataset |

### C. Tres formulaciones concretas para 6.2

Redactadas para que se puedan usar tal cual, con su cita:

1. **Sobre por qué RandomForest y no una arquitectura profunda** —convierte una posible crítica en un
   punto a favor: *«La elección de un clasificador basado en árboles para la etapa de firmas no es
   una concesión a la simplicidad. La evidencia empírica publicada sitúa a los modelos de árboles por
   delante del aprendizaje profundo en datos tabulares de tamaño medio (Grinsztajn et al., NeurIPS
   2022), y el análisis más amplio disponible —19 algoritmos sobre 176 conjuntos de datos
   (McElfresh et al., NeurIPS 2023)— identifica como favorables a los árboles precisamente las
   condiciones que reúne D3: gran número de muestras, razón muy alta de muestras por característica
   y distribuciones sesgadas. El propio trabajo que compara los modelos profundos con XGBoost sobre
   los conjuntos con los que estos se presentaron concluye que XGBoost los supera y exige mucho menos
   ajuste (Shwartz-Ziv y Armon, 2022).»*
2. **Sobre lo que sí propone la literatura, que es mezclar y no sustituir** —enlaza el bloque 1 con la
   línea nº 1 ya existente: *«La misma literatura que desaconseja sustituir los árboles recomienda
   combinarlos: Shwartz-Ziv y Armon observan que un conjunto de modelos profundos con XGBoost supera
   a XGBoost solo, y el* benchmark *vivo TabArena (NeurIPS 2025) concluye que los conjuntos entre
   modelos constituyen hoy el estado del arte en datos tabulares. Esto respalda desde fuera la línea
   futura principal de este trabajo —el conjunto de detectores de la etapa 1—, cuya complementariedad
   por tipo de ataque ya se ha medido aquí con datos propios.»*
3. **Sobre la codificación de las categóricas, que es la línea nueva de este informe** —y es
   defendible porque nace de datos del propio TFG: *«La codificación one-hot genera 84 de las 122
   características del sistema, de las cuales 70 provienen de una sola variable,* service*. La
   selección supervisada descarta 55 de esas 70, entre ellas los indicadores de servicios sobre los
   que operan varios ataques no vistos. La literatura de codificación de variables categóricas de
   alta cardinalidad (Micci-Barreca, 2001; Pargent et al., 2022) muestra que las versiones
   regularizadas del* target encoding *superan de forma consistente al one-hot, y la documentación de
   los* frameworks *de* boosting *moderno señala que el one-hot es subóptimo para aprendices de
   árbol. Sustituirlo abre una línea futura que no solo reduce la dimensionalidad, sino que impide
   que el selector de características descarte por separado indicadores de servicios raros.»*

### D. Un aviso metodológico que conviene no perder


TabArena documenta que algunos modelos profundos aparecen **sobrerrepresentados** en los conjuntos
entre modelos por **sobreajuste al conjunto de validación**. Es directamente aplicable a cualquiera
de las líneas 1, 3, 4 y 6 de la tabla B: si los miembros de un conjunto —o las características
extra— se eligen mirando `D1_val` o los pliegues OOF de D3, el que más se sobreajuste a esa
validación entrará, y la ganancia no se reproducirá en D2. La disciplina que el proyecto ya tiene
(`D1_val` solo para el p95, calibración OOF que no ve D2) es la defensa correcta; el riesgo es
diluirla al añadir un criterio de selección más.

## Decisiones tomadas a partir de este informe

> [!note] Qué es este bloque
> Cierre de trazabilidad exigido por la ficha **T17, punto 1**. Recoge **solo** lo que ya está
> registrado en `resumen-de-decisiones.md` o en `features.md`: qué se convirtió en decisión y qué se
> descartó. Todo lo demás del apartado `## Implicaciones para el proyecto` **sigue siendo candidato**,
> no decisión.

### D.1 Lo que se convirtió en decisión

| Decisión registrada | Qué dice | Dónde está registrada |
|---|---|---|
| **`6.2 Líneas futuras` la redacta un agente, con revisión final de Francisco** | Decisión marco (b) del 2026-08-06: se retira la regla «lo escribe Francisco» en dos velocidades. Afecta directamente a este informe, que **alimenta** esa sección | `resumen-de-decisiones.md`, § Decisiones del 2026-08-06, decisión marco (b) |

### D.2 Lo que se descartó

| Descartado | Motivo registrado |
|---|---|
| *(sin entradas propias de este informe: los descartes técnicos internos —TabNet/FT-Transformer, TabPFN, semisupervisado— están argumentados en el cuerpo, pero no elevados a decisión de proyecto; ver § D.3)* | — |

### D.2-bis Contexto del lote que **no sale de este informe**

> [!warning] No atribuir a este informe
> Las decisiones de esta tabla se tomaron en el mismo lote de trabajo, pero **su sede de origen
> documentada es [[benchmark-comparativo-nsl-kdd]]** (filas D4 y D5 de su bloque de decisiones), no
> este informe. El alcance declarado aquí (`:26-29`) **excluye expresamente el protocolo de
> métricas**. Se conservan como contexto de lectura, y solo con esa etiqueta.

| Decisión del lote | Qué dice | Sede de origen |
|---|---|---|
| **T18 — el CSV publica solo lo estable** | `metricas_*.csv` publica únicamente lo estable (qué tramos de tiempo entran, cuáles no y el aviso de P9); **todos los números** de reparto viven en `PIPELINE.md`, anclados a commits y editables sin re-correr. Las dos frases empíricas que el CSV llegó a publicar salen a 0/8 y 0/8 | `resumen-de-decisiones.md`, § Decisiones del 2026-08-09 (T18); contexto en [[benchmark-comparativo-nsl-kdd]] |
| **T22 — `n_iter_total_grid` es determinista** | 162 a 54 características y 128 a 122, idénticos entre corridas; con las épocas congeladas, la variación de *wall-clock* del Autoencoder es carga de máquina. Consecuencia: el eje 54-vs-122 es indecidible sin medidas repetidas | `resumen-de-decisiones.md`, § Decisiones del 2026-08-09 (T22); contexto en [[benchmark-comparativo-nsl-kdd]] |
| **Renuncia declarada al p-valor sobre las 10 semillas** | Sin p-valor, con la renuncia y su razón declaradas: 10 puntos sobre un único dataset no sostienen un contraste. Si los intervalos se solapan, se dice y no se establece el orden | [[benchmark-comparativo-nsl-kdd]], fila D5; registrada en `resumen-de-decisiones.md`, § Decisiones del 2026-08-06 |

Derivados de esas tres —**también contexto del lote, no descartes de este informe**: (1) diseñar las
10 semillas de T4 para resolver la duda del número de épocas, resuelta ya por T22; (2) publicar en
`metricas_*.csv` las dos frases empíricas sobre reparto de tiempo, que salen a 0/8 por T18; y (3)
contrastar con p-valor el orden entre RandomForest/HistGradientBoosting y entre
Autoencoder/IsolationForest, cubierto por la renuncia declarada.

Lo que sí conecta con el cuerpo de este informe: el aviso metodológico del **§ D** (sobreajuste al
conjunto de validación documentado por TabArena) apunta en la misma dirección que esa disciplina de
lote — **no sobreinterpretar una dispersión pequeña** —, pero es una observación de este informe,
no la fuente de aquellas decisiones.

### D.3 Lo que este informe propone y **sigue sin ser decisión**

Los diez candidatos de la **tabla B** —incluida la ★ nº 1 de este informe (vector de error de
reconstrucción por característica) y el *target encoding* de `service`— **no tienen decisión
registrada** ni en `resumen-de-decisiones.md` ni en `features.md`: entran en `6.2` como **líneas
futuras**, no como trabajo comprometido. Lo mismo vale para los descartes técnicos internos del
informe (TabNet/FT-Transformer, TabPFN, semisupervisado): están argumentados **aquí**, con su
evidencia, pero no están elevados a decisión de proyecto.

> [!todo] Respaldo pendiente
> No consta en `resumen-de-decisiones.md` ni en `features.md` ninguna decisión formal sobre los
> candidatos de la tabla B (ni de alta ni de descarte). Si alguno debe pasar de candidato a decisión
> —en particular el nº 1 y el nº 2, que son los únicos sin dependencias nuevas—, hace falta una
> entrada explícita en `resumen-de-decisiones.md`; no se escribe aquí por iniciativa propia.
