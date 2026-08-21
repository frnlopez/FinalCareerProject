---
titulo: "Recorte capítulo 2 — bloque 2.1 (Machine Learning)"
tipo: informe de análisis
fecha: 2026-08-20
alcance: "Las 6 notas de 02 Marco Teórico/2.1 Machine Learning"
---


> [!danger] CORRECCIÓN DE LA CITA DEL PROFESOR — 2026-08-20, hilo principal
> Este informe citaba la frase del profesor con una **elipsis que tapaba su ÚNICO ejemplo concreto**:
> «sin dar todos los hiperparámetros **(por ejemplo, que aporta al lector saber si has usado como
> semilla el valor 42)**». **El error viene del encargo, no del agente**: el hilo principal redactó
> el brief con esa elipsis y los cuatro informes la reprodujeron fielmente.
>
> **Consecuencia sobre la atribución (a)/(b), que es el eje de este informe — y leída con precisión,
> porque una primera versión de esta nota se pasó de largo:**
> - **(a), y es exactamente lo que él pidió:** las **menciones de la semilla 42 y de
>   hiperparámetros dentro de las explicaciones del CUERPO**. Él habla de «las explicaciones de las
>   soluciones analizadas», no del apéndice. **Buena parte ya está hecha**: el pase D10 del
>   2026-08-19 movió las tablas de configuraciones ganadoras de `4.4` y `4.5` a `A.3.3`, dejando en el
>   cuerpo qué se buscó y por qué. Lo que quede de ese tipo en el cuerpo es **(a)** y se recorta
>   citándole a él.
> - **(b), y NO se le atribuye:** las **dos tablas de `A.3.6`** y el volumen de `2.1.6.7`. Son
>   apéndice, no «explicaciones», y el argumento para retirarlas es otro y es bueno por sí solo:
>   **reproducen a mano un CSV versionado y citable**. Eso es redundancia con el artefacto, no exceso
>   de detalle en la prosa.
>
> La distinción importa porque Francisco defiende esto ante el profesor: presentarle un recorte de
> apéndice como si lo hubiera pedido él es tan malo como no atender su único ejemplo concreto.
>
> Con la cita completa, además, el sentido general cambia de matiz: el profesor no pide *menos
> teoría*, pide **menos detalle de implementación en las explicaciones**. Eso apunta a los capítulos
> 4-5 y a los apéndices antes que al capítulo 2.
# Recorte del capítulo 2 — bloque 2.1 (Machine Learning)

> [!warning] Qué pidió el profesor y qué no
> El profesor **no pidió recortar el capítulo 2**. Su petición literal, recogida en
> `mis-apuntes-del-informe.md`, es: «El informe está bien en general, pero hay que mejorar
> bastante la redacción, simplificando las explicaciones de las soluciones analizadas sin dar
> todos los hiperparámetros **(por ejemplo, que aporta al lector saber si has usado como semilla el valor 42)**, quizás recortando algunos apartados (por ejemplo, los primeros
> apartados del Capítulo 3 no creo que sean necesarios y se podían unificar)». El apartado que
> señaló por su nombre es el **capítulo 3**.
>
> De esa cita, lo único que muerde dentro de 2.1 es **«sin dar todos los hiperparámetros»**, que
> alcanza a **un** sitio: la rejilla de `RandomForest` que hoy figura en `2.1.6.4`. Todo lo demás
> que este informe propone es **decisión de Francisco por volumen**, y así se etiqueta en la
> columna correspondiente. **Ninguna otra retirada debe atribuirse al profesor en la defensa.**

---

## 1. Resumen ejecutivo

Conteos obtenidos con `wc -w` sobre los ficheros en disco y con suma por encabezado (`awk`) para
el desglose interno. Los totales de nota incluyen el *frontmatter* YAML (15–27 palabras por nota);
los desgloses por apartado no.

| Nota | Palabras hoy | Objetivo tras recorte | Ahorro contado |
|---|---|---|---|
| 2.1.1 Introducción al ML | 1.030 | ~631 | **399** |
| 2.1.2 Tipos de ML | 1.926 | ~1.403 | **523** |
| 2.1.3 Ciclo de vida de un proyecto ML | 1.774 | ~639 | **1.135** |
| 2.1.4 Algoritmos de ML | 2.685 | ~1.763 | **922** |
| 2.1.5 Métricas de evaluación | 2.180 | ~1.642 | **538** |
| 2.1.6 Metodologías y buenas prácticas | 3.530 | ~2.792 | **738** |
| **Total 2.1** | **13.125** | **~8.870** | **4.255 (−32,4 %)** |

**Hallazgo estructural que ordena todo lo demás.** Se contaron los wikilinks entrantes desde los
capítulos 3, 4 y 5 hacia las seis notas de 2.1
(`grep -rno "\[\[2\.1\.[^]|]*"` sobre las tres carpetas): hay **ocho remisiones y las ocho apuntan
a `2.1.6 Metodologías y buenas prácticas`** (2 en `3.3`, 1 en `3.2`, 1 en `3.6`, 1 en `4.1`, 2 en
`4.3`, 1 en `6.1`). **`2.1.1`, `2.1.2`, `2.1.3`, `2.1.4` y `2.1.5` no reciben ni un solo enlace
desde el cuerpo posterior.** Eso no las deja huérfanas —varias se usan de forma implícita, y se ha
verificado término por término—, pero sí explica el reparto del recorte: `2.1.6` es la nota que el
resto de la memoria consume de verdad y es la que menos se toca en proporción; `2.1.3`, que solo
contiene remisiones hacia adelante, es la que más se comprime.

**Censo de uso implícito** (recuento de apariciones en las 17 notas de los capítulos 3, 4 y 5, con
`grep -Ec` fichero a fichero; se corrigieron los falsos positivos de `ROC` dentro de «protocolo» y
de `EDA` dentro de «queda»):

| Concepto de 2.1 | Notas de 3–5 que lo mencionan | Apariciones |
|---|---|---|
| RandomForest | 10 | 67 |
| autoencoder | 10 | 41 |
| HistGradientBoosting | 5 | 37 |
| DecisionTree / árbol de decisión | 7 | 35 |
| k-NN / vecinos | 6 | 31 |
| One-Class SVM | 6 | 23 |
| Isolation Forest | 6 | 22 |
| LOF / Local Outlier Factor | 6 | 20 |
| `f1_macro` | 8 | 58 |
| FPR | 8 | 59 |
| macro | 9 | 63 |
| ROC (palabra completa) / AUC | 5 | 16 / 15 |
| matriz de confusión | 4 | 13 |
| SMOTE / `class_weight` / balanceo | 12 | 80 |
| semilla / `random_state` | 11 | 54 |
| validación cruzada | 10 | 18 |
| fuga de información / *leakage* / *snooping* | 7 | 18 |
| accuracy / exactitud | 6 | 15 |
| **micro (promediado)** | **0** | **0** |
| **ponderado / weighted** | **1** | **1** |
| **MAE / RMSE / regresión** | **0** | **0** |
| **k-means / silueta / clustering / agrupamiento** | **0** | **0** |
| **regresión logística** | **0** | **0** |
| **ReLU / sigmoide / tanh** | **0** | **0** |
| **retropropagación / backprop** | **0** | **0** |
| **aprendizaje por refuerzo** | **0** | **0** |
| **auto-supervisado** | **0** | **0** |
| **CRISP-DM** | **0** | **0** |

Dos matices que impiden leer los ceros como sentencia automática:

- **`weighted` con una sola aparición en prosa sí se publica**: `Resultados/metricas_firmas.csv`
  tiene columna `f1_weighted`. El promediado ponderado, por tanto, **se queda**. El **micro no
  aparece en ninguna columna de ninguna tabla** ni en ninguna nota: ese sí sale.
- **`MLP` aparece 9 veces en 7 notas**, aunque «perceptrón», «ReLU» y «retropropagación» no
  aparezcan nunca. Lo que el sistema usa es `MLPRegressor` como autoencoder; el aparato de
  fundamentos neuronales que lo precede en `2.1.4.3` no lo usa nadie.

---

## 2. Tabla apartado por apartado

Leyenda de la última columna: **(a)** = lo pidió el profesor · **(b)** = volumen, lo decide
Francisco hoy.

### 2.1.1 Introducción al ML — 1.030 palabras

| Apartado | Palabras | Quién lo usa en 3–5 | Veredicto | Destino | (a)/(b) |
|---|---|---|---|---|---|
| Encabezado (hasta «2.1.1.1») | 129 | Entrada del capítulo | SE QUEDA | — | — |
| 2.1.1.1 Relación con la Inteligencia Artificial | 141 | Nadie de 3–5; la sede canónica es `2.3.1 IA, ML y Deep Learning`, que la propia nota declara | SE COMPRIME A UN PÁRRAFO (~70) | Nada al apéndice: es duplicado interno del capítulo 2 | (b) |
| 2.1.1.2 Programación tradicional frente a ML | 303 | Nadie de 3–5 por texto; sostiene las Figuras 2.2–2.4 | SE QUEDA recortado (~193) | El párrafo de **aprendizaje continuo** (159 contadas) a una frase con remisión a `6.2 Líneas futuras` | (b) |
| 2.1.1.3 Algoritmo y modelo | 180 | 0 apariciones de la pareja terminológica en 3–5, pero es convención de vocabulario | SE COMPRIME A UN PÁRRAFO (~80) | Solo exposición | (b) |
| 2.1.1.4 El papel de los datos (incluye el *callout* de cierre, 64) | 228 | Es casi toda remisiones a `2.1.3`, `2.1.6` y `4.3` | SE COMPRIME (~110) | El *callout* de cierre SALE (transición redundante) | (b) |

> Nota sobre figuras: esta nota embebe cuatro imágenes `fig-ml-intro-01…04` con pies **Figura 2.1**
> a **Figura 2.4**. Ninguna se retira, precisamente para no romper la serie contigua `2.1`–`2.5`
> del capítulo 2 que el censo de `assets/` da por verificada.

### 2.1.2 Tipos de ML — 1.926 palabras

| Apartado | Palabras | Quién lo usa en 3–5 | Veredicto | Destino | (a)/(b) |
|---|---|---|---|---|---|
| Encabezado | 190 | Entrada | SE QUEDA recortado (~130) | — | (b) |
| 2.1.2.1 Aprendizaje supervisado | 213 | `4.5 Entrenamiento del modelo … firmas` (clasificación multiclase sobre D3); «supervisado» 18 apariciones en 11 notas | SE QUEDA | — | — |
| 2.1.2.2 Aprendizaje no supervisado | 221 | Solo la fila «detección de anomalías» de su tabla; *clustering*, PCA/t-SNE y reglas de asociación tienen **0 apariciones** en 3–5 | SE COMPRIME (~140): se conserva la tabla porque es el enunciado que `2.1.2.6` corrige, se retiran las filas y la prosa que nadie usa | Solo exposición | (b) |
| 2.1.2.3 Aprendizaje por refuerzo | 155 | **Nadie.** 0 apariciones de «refuerzo» en 3–5 | SALE DEL CUERPO; queda la frase de `2.1.2.7` que declara que no se usa | **Solo exposición.** No merece apéndice: un apéndice justifica material que el sistema usa y no cabe en el cuerpo, y aquí no hay nada que el sistema use | (b) |
| 2.1.2.4 Aprendizaje semisupervisado | 169 | Funda el vocabulario que `3.4.1` y `4.4` usan («semisupervisado», 3 apariciones) | SE QUEDA recortado (~120) | — | (b) |
| 2.1.2.5 Aprendizaje auto-supervisado | 252 | «auto-supervisado»: **0 apariciones** en 3–5. Pero su *callout* «Relación con el autoencoder de este trabajo» (170) resuelve una ambigüedad real | SE COMPRIME: el texto general (86) a una frase (~25); el *callout* **se queda** | Solo exposición para el texto general | (b) |
| 2.1.2.6 El caso frontera: solo la clase normal | 480 | `3.4 Modelo de detección de anomalías` §3.4.1 y `4.4`. Es la sede de la regla terminológica de todo el trabajo | SE QUEDA recortado (~380) | El solapamiento con la argumentación paralela de `3.4.1` se resuelve dejando aquí la regla y allí la aplicación | (b) |
| 2.1.2.7 Situación de este trabajo y transición | 183 | La tabla etapa→paradigma→split la usa el lector de `3.4`/`4.5` | SE QUEDA recortado (~150) | — | (b) |

### 2.1.3 Ciclo de vida de un proyecto ML — 1.774 palabras

**Es la nota con menos anclaje de las seis.** Ningún enlace entrante desde 3–5; su contenido es un
esqueleto de fases genéricas cuyo relleno concreto está en `4.2`, `4.3`, `4.4` y `4.5`, y cuyo rigor
está en `2.1.6`. Su propio encabezado lo admite: «No se repite aquí ninguno de esos contenidos».

| Apartado | Palabras | Quién lo usa en 3–5 | Veredicto | Destino | (a)/(b) |
|---|---|---|---|---|---|
| Encabezado + *callout* «Reparto con 2.1.6» (109 de ellas) | 229 | Nadie | SE COMPRIME (~100) | Solo exposición | (b) |
| 2.1.3.1 Comprensión y recolección de datos | 179 | «EDA» 5 apariciones en 2 notas, «exploratorio» 3 en 2; el contenido real está en `4.2` y `4.3` | SE COMPRIME A UN PÁRRAFO (~60) | Solo exposición | (b) |
| 2.1.3.2 Limpieza y preparación de datos | 162 | `4.3 Preprocesamiento de los datasets` hace el trabajo; aquí solo se enumera | SE COMPRIME A UN PÁRRAFO (~60) | Solo exposición | (b) |
| 2.1.3.3 Ingeniería y selección de características | 157 | `4.3.5 Selección de características` | SE COMPRIME A UN PÁRRAFO (~60) | Solo exposición | (b) |
| 2.1.3.4 Selección del tipo de modelo — pasos 1 a 6 | 172 | **Nadie ejecuta ese bucle.** El trabajo compara 4 algoritmos con rejilla fija en `4.4`/`4.5`; no hay rondas iterativas de reingeniería de características ni combinación de candidatos diversos | SALE DEL CUERPO | Solo exposición: describir un procedimiento que el sistema no siguió es peor que no describirlo | (b) |
| 2.1.3.4 «Tres conceptos que conviene no confundir» | 197 | **Duplicado**: `2.1.6.3` tiene el *callout* «Tres términos que no son sinónimos» (223 palabras) con la misma distinción CV / K-fold / desviación típica | SALE DEL CUERPO por duplicidad; sede única en `2.1.6.3` | Ni apéndice ni exposición: el contenido sobrevive en `2.1.6.3` | (b) |
| 2.1.3.4 «Criterios de comparación entre candidatos» | 194 | Los criterios que el trabajo aplica de verdad son `f1_macro` y la desviación típica; «diversidad de errores para combinar» no se usa (2 apariciones de «ensemble» en 3–5) | SE COMPRIME (~80) | Solo exposición | (b) |
| 2.1.3.5 Entrenamiento y ajuste de hiperparámetros | 146 | Remite a `2.1.6.4`; el material propio es la mención a métodos de conjuntos, que el sistema no usa como tal | SE COMPRIME A UN PÁRRAFO (~50) | Solo exposición | (b) |
| 2.1.3.6 Evaluación del rendimiento (incluye *callout* de despliegue, 73) | 256 | Todo remite a `2.1.6.2` y `2.1.6.6`. El «despliegue fuera de alcance» está **tres veces** en la memoria: aquí, en `2.1.6.1` y en `6.1` | SE COMPRIME (~90) | El *callout* de despliegue SALE: sede única en `2.1.6.1` | (b) |
| Cierre / transición | 40 | — | SE QUEDA | — | — |

### 2.1.4 Algoritmos de ML — 2.685 palabras

| Apartado | Palabras | Quién lo usa en 3–5 | Veredicto | Destino | (a)/(b) |
|---|---|---|---|---|---|
| Encabezado | 173 | Entrada; ya declara el criterio «lo que el sistema usa» | SE QUEDA recortado (~130) | — | (b) |
| 2.1.4.1 Introducción a los supervisados (incluye la mención a regresión logística) | 99 | «regresión logística»: **0 apariciones** en 3–5, y ya está en `A.3 Ficha del sistema` §A.3.10.1 | SE QUEDA (la mención ya es de una frase) | — | — |
| 2.1.4.1.1 Árboles de decisión | 134 | `4.5` (DecisionTree candidato, `export_text` para las firmas legibles): 35 apariciones en 7 notas | SE QUEDA | — | — |
| 2.1.4.1.2 Random Forest y Gradient Boosting | 307 | `4.5` y `5.2` (RandomForest ganador, 67 apariciones; HistGradientBoosting, 37) | SE QUEDA recortado (~250) | — | (b) |
| 2.1.4.1.3 k-NN | 135 | `4.5` (KNN candidato): 31 apariciones | SE QUEDA | — | — |
| 2.1.4.2 Introducción a los *one-class* | 145 | `3.4`, `4.4`, `5.1` | SE QUEDA | — | — |
| 2.1.4.2.1 Isolation Forest | 255 | `4.4`, `5.1`, `5.3`: 22 apariciones | SE QUEDA | — | — |
| 2.1.4.2.1 *callout* «Atribución verificada y reasignada (2026-08-16)» | 107 | Nadie: es **nota de trabajo del proyecto**, no texto de memoria | SALE DEL CUERPO | Solo registro interno (`resumen-de-decisiones.md`); no va al `.docx` | (b) |
| 2.1.4.2.2 One-Class SVM | 137 | `4.4`, `5.1`: 23 apariciones | SE QUEDA | — | — |
| 2.1.4.2.3 LOF + *callout* «Tres nociones de anomalía» (114) | 236 | `4.4`, `5.1`: 20 apariciones. El *callout* es exactamente el argumento de diseño de `3.4.2` | SE QUEDA | — | — |
| **2.1.4.3 Redes neuronales artificiales (bloque completo: 2.1.4.3.1–2.1.4.3.4 + *callout*)** | **778** | «ReLU/sigmoide/tanh»: **0**. «retropropagación/backprop»: **0**. «perceptrón»: 1. Lo único que el sistema usa es `MLPRegressor` como autoencoder (41 apariciones de «autoencoder»), y la frontera con el *deep learning* la fija `2.3.1` | **SE COMPRIME** a una subsección única de ~200 palabras: neurona → capas ocultas → no linealidad → «se entrena minimizando una pérdida por descenso de gradiente con retropropagación» → el MLP de este trabajo | **Apéndice `A.3` §A.3.10 (nueva §A.3.10.3)** para neurona/perceptrón, funciones de activación y retropropagación. Aquí sí merece apéndice, a diferencia del refuerzo o el *clustering*: el sistema **sí** contiene un componente neuronal —el detector ganador de la etapa 1—, y el tribunal puede pedir su fundamento | (b), con el matiz de que el desglose de funciones de activación es material del tipo que el profesor pidió aligerar |
| 2.1.4.3 *callout* «Localizador de `[6]`» | 89 | Nadie: nota de trabajo bibliográfica | SALE DEL CUERPO | Registro del `researcher` | (b) |
| 2.1.4.4 Algoritmos no supervisados: agrupamiento | 102 | **0 apariciones** de k-means/agrupamiento/silueta en 3–5. Ya desarrollado en `A.3` §A.3.10.2 y `A.2` §A.2.2.2 | SE COMPRIME a una frase (~35) | El desarrollo **ya está** en el apéndice; no hay que mover nada | (b) |
| 2.1.4.5 Transición | 110 | — | SE COMPRIME (~40) | — | (b) |

### 2.1.5 Métricas de evaluación — 2.180 palabras

| Apartado | Palabras | Quién lo usa en 3–5 | Veredicto | Destino | (a)/(b) |
|---|---|---|---|---|---|
| Encabezado + *callout* «Reparto de roles con el Apéndice A.2» (130) | 299 | El reparto se explica dos veces (aquí y en `A.2`) | SE QUEDA recortado (~150) | Sede única del reparto en `A.2` | (b) |
| 2.1.5.1 Matriz de confusión | 278 | `5.0.3` la declara **artefacto primario** (punto 4); 13 apariciones en 4 notas; matrices 2×2, 5×5 y 5×6 en `5.1`–`5.3` | SE QUEDA | — | — |
| 2.1.5.2 Precisión, exhaustividad, FPR, exactitud y F1 | 339 | Las cinco se publican: columnas `bin_precision`, `bin_recall`, `bin_f1`, `bin_fpr`, `bin_accuracy` de `metricas_hibrido.csv` | SE QUEDA recortado (~290) | — | (b) |
| 2.1.5.3 Promediado macro, ponderado y micro | 386 | Macro: 63 apariciones. Ponderado: publicado como `f1_weighted` en `metricas_firmas.csv`. **Micro: 0 apariciones y ninguna columna en ningún CSV** | SE QUEDA recortado (~300): **la viñeta «Micro» (54 palabras) y su mención en la lista de efectos SALEN**; el título pasa a «macro y ponderado» | Solo exposición | (b) |
| 2.1.5.4 Precisión y recall no son complementarias: la necesidad del FPR | 310 | Es la **prohibición 2 de `5.0.4`** («ninguna cifra de recall sin su FPR al lado»); FPR con 59 apariciones en 8 notas | SE QUEDA recortado (~250) | — | (b) |
| 2.1.5.5 Curvas ROC y precisión-recall | 284 | Columnas `bin_roc_auc` y `bin_pr_auc` de `metricas_hibrido.csv`; ROC/AUC con 16/15 apariciones; curvas ROC/PR en `5.1` | SE QUEDA recortado (~240) | — | (b) |
| 2.1.5.6 Métricas ajenas a la clasificación | 122 | **0 apariciones** de MAE, RMSE o silueta en 3–5. Ya desarrolladas en `A.2` §A.2.2 | SALE DEL CUERPO; queda una frase (~20) declarando que no se reportan | El desarrollo **ya está** en `A.2`; no hay que mover nada | (b) |
| Cierre | 98 | — | SE COMPRIME (~50) | — | (b) |

### 2.1.6 Metodologías y buenas prácticas — 3.530 palabras

**La nota que el resto de la memoria consume de verdad**: recibe las 8 remisiones entrantes desde
3–5 y 6. Se recorta lo menos posible y solo por duplicidad probada.

| Apartado | Palabras | Quién lo usa en 3–5 | Veredicto | Destino | (a)/(b) |
|---|---|---|---|---|---|
| Encabezado + tabla de reparto con `A.3.11` (133) | 256 | `4.1` la enlaza | SE QUEDA recortado (~200) | — | (b) |
| 2.1.6.1 CRISP-DM | 156 | **0 apariciones de «CRISP-DM»** en 3–5. El desarrollo completo ya está en `A.3.11.1` | SE COMPRIME A UN PÁRRAFO (~90), conservando la declaración de que el despliegue queda fuera de alcance (que pasa a ser su sede única) | El desarrollo **ya está** en `A.3.11.1` | (b) |
| 2.1.6.2 cuerpo (partición y línea roja) | 181 | `3.3` (×2), `4.3`, `6.1` | SE QUEDA | — | — |
| 2.1.6.2 *callout* «Conexión con el sistema implementado — el perímetro anti-fuga» | 295 | `3.3 Metodología de funcionamiento del sistema` remite aquí; es la respuesta directa a «¿cómo sé que no hubo *leakage*?» | SE QUEDA recortado (~240) | — | (b) |
| 2.1.6.2 *callout* «Declaración: tres decisiones del sistema se tomaron mirando D2» | 378 | Se usa mucho, pero el mismo inventario está **además** en `6.1`, en `4.3.5` y en `A.3.11.2` — la propia `4.3` dice que «las otras diez sedes son remisiones a este apartado» | SE COMPRIME (~120): se conserva la **lectura conceptual** (esto es *data snooping*, y el perímetro anterior no basta) y se remite al inventario | Sede única del inventario tabulado: `4.3.5` + `6.1`; ampliación en `A.3.11.2` | (b) |
| 2.1.6.3 Validación cruzada estratificada (incluye el *callout* «Tres términos que no son sinónimos», 223) | 326 | `4.5` (`StratifiedKFold(5, shuffle=True, random_state=42)`); 18 apariciones de «validación cruzada» en 10 notas; «estratificad», 2 | **SE QUEDA sin recorte**, y **absorbe** como sede única la distinción CV/K-fold/desviación típica que hoy se duplica en `2.1.3.4` | — | — |
| 2.1.6.4 Búsqueda de hiperparámetros | 267 | `4.5` (`GridSearchCV`, 7 apariciones); tabla parámetro/hiperparámetro | SE QUEDA recortado (~230): **se retira del capítulo 2 la rejilla concreta `n_estimators ∈ {100, 300}` × `max_depth ∈ {10, None}`**, que tiene su sede propia en `4.5` | Sede única: `4.5` | **(a)** — único punto de 2.1 alcanzado por «sin dar todos los hiperparámetros» |
| 2.1.6.4 *callout* «Un umbral de confianza no es una regla de rechazo óptima» | 103 | Funda la clase `unknown`, con 34 apariciones en 6 notas de 3–5; `5.3` mide su consecuencia | SE QUEDA | — | — |
| 2.1.6.5 Fuga de información | 373 | `4.3` la enlaza; las tres formas de fuga están materializadas una a una en el preprocesado | SE QUEDA sin recorte | — | — |
| 2.1.6.6 Por qué el *accuracy* miente | 263 | `f1_macro` es el criterio de todo el protocolo (58 apariciones); `4.5` lo justifica remitiendo aquí | SE QUEDA recortado (~200): **la tabla macro/weighted duplica la de `2.1.5.3`** y se retira, dejando la remisión | Sede única de la tabla: `2.1.5.3` | (b) |
| 2.1.6.7 Reproducibilidad | 302 | «semilla»/`random_state`: 54 apariciones en 11 notas; el barrido de 10 semillas se publica en `A.3` desde `dispersion_semillas.md` | SE QUEDA sin recorte | — | — |
| 2.1.6.8 cuerpo (la CV sobrestima frente al test) | 153 | «drift/KS/deriva», 43 apariciones en 9 notas; «0-day/conjunto abierto», 84 en 15 | SE QUEDA | — | — |
| 2.1.6.8 *callout* «Definición: el *semantic gap*» | 117 | `3.2 Arquitectura del sistema` lo invoca explícitamente para justificar por qué existe la etapa 2 | SE QUEDA | — | — |
| 2.1.6.8 *callout* «El caso medido en este trabajo» | 99 | `5.3` y `5.4` (caída del *baseline* entre CV y test) | SE QUEDA | — | — |
| 2.1.6.8 *callout* «Verificación pendiente — sin acceso al texto completo» | 148 | Nadie: es **nota de trabajo** sobre el estado de dos citas | SALE DEL CUERPO | Registro interno del `researcher` / `Auditoría de Bibliografía`; no va al `.docx` | (b) |
| 2.1.6.8 *callout* «Relación con otras notas» | 60 | Navegación de Obsidian, no texto de memoria | SALE DEL CUERPO | No va al `.docx` | (b) |

---

## 3. Justificación por apartado: los seis criterios aplicados

1. **Nadie lo usa y el sistema no lo contiene → sale, y no al apéndice.** Aprendizaje por refuerzo
   (`2.1.2.3`, 155), *clustering* en el cuerpo (`2.1.4.4`, 102), métricas de regresión y silueta
   (`2.1.5.6`, 122). Un apéndice sirve para sostener con detalle algo que el sistema **sí** hace y
   que no cabe en el cuerpo; no para almacenar taxonomía de manual. Además, dos de los tres **ya
   tienen** su desarrollo en `A.3.10.2` y `A.2.2`: no hay nada que mover, solo que dejar de repetir.
2. **Nadie lo usa pero el sistema sí contiene la pieza → apéndice.** Caso único: `2.1.4.3` (778
   palabras). El trabajo tiene un componente neuronal —el autoencoder `MLPRegressor`, detector
   **ganador** de la etapa 1— y por tanto el fundamento (neurona, capas, activaciones,
   retropropagación) es material legítimamente defendible. Pero ninguna de sus piezas se nombra en
   3–5, así que su sitio es `A.3` §A.3.10.3, con ~200 palabras de resumen en el cuerpo.
3. **Duplicidad probada → sede única.** Tres casos contados: la distinción CV/K-fold/desviación
   típica (`2.1.3.4`, 197, contra `2.1.6.3`, 223); la tabla macro/weighted (`2.1.6.6` contra
   `2.1.5.3`); el «despliegue fuera de alcance» (`2.1.3.6`, `2.1.6.1` y `6.1`). En los tres gana la
   sede que recibe remisiones desde 3–5.
4. **Notas de trabajo del proyecto → fuera del cuerpo sin discusión.** Suman 344 palabras contadas:
   el *callout* de atribución del Isolation Forest (107), el localizador de `[6]` (89) y la
   verificación pendiente de Arp y Chow (148). Son bitácora del `researcher`, no memoria; su
   presencia en el `.docx` sería un error de todos modos, independientemente del recorte.
5. **Andamiaje de remisiones → una tabla.** `2.1.3` es el caso extremo: seis apartados cuyo cuerpo
   es en buena parte «esto se hace en `4.3`». Sustituirlos por un párrafo de fases más una tabla
   fase → sede conserva el 100 % de su función (ordenar el relato) con un tercio de las palabras.
6. **Lo que 3–5 consume, no se toca.** Ninguna métrica publicada pierde su definición: matriz de
   confusión, precisión, recall, FPR, exactitud, F1, macro, ponderado, ROC/AUC y PR/AUC siguen
   definidas en `2.1.5`. Ningún algoritmo implementado pierde su descripción: los cuatro *one-class*
   y los cuatro supervisados siguen en `2.1.4`. Y `2.1.6` pierde solo duplicados y bitácora.

**Riesgo declarado.** El recorte de `2.1.3` deja el capítulo 2 sin una descripción autónoma del
ciclo de vida, que pasa a apoyarse en CRISP-DM (`2.1.6.1`, comprimido) y en `A.3.11.1`. Es
coherente —CRISP-DM ya es un marco de fases— pero conviene que Francisco lo sepa: si el tribunal
pregunta por «las etapas de un proyecto de ML», la respuesta vive en `2.1.6.1` más la tabla
fase → sede, no en una sección propia.

---

## 4. Material retirado, orientado a la DEFENSA ORAL

> [!success] RECONCILIACIÓN CON EL DISCO — 2026-08-21 (ficha F3)
> Este §4 se redactó en tiempo futuro-hecho («retirado de …») **antes de ejecutar el recorte**, igual
> que el §5 del informe de `2.2`. La diferencia es el resultado: **verificado apartado por apartado
> sobre las seis notas de `2.1` el 2026-08-21, el recorte de este bloque SÍ se ejecutó**, y las diez
> partidas D-1…D-10 describen el disco. **Este §4 puede usarse como registro**, con las tres
> salvedades que se marcan abajo.
>
> | Partida | Sede | Estado real en disco |
> |---|---|---|
> | D-1 aprendizaje por refuerzo | `2.1.2.3` | **APLICADO** — el apartado **subsiste como una sola frase** de declaración («*Este trabajo no lo emplea —no hay agente ni entorno…*»); el desarrollo del paradigma se fue. El plan pedía que solo quedara la frase de `2.1.2.7`: quedan las dos, y no es un defecto |
> | D-2 marco general del auto-supervisado | `2.1.2.5` | **APLICADO** — hoy son una frase de definición más el *callout* «Relación con el autoencoder de este trabajo», que se conservó como estaba previsto |
> | D-3 fundamentos neuronales | `2.1.4.3` → `A.3.10.3` | **APLICADO, y el destino existe** — `A.3` tiene hoy `A.3.10.3 Redes neuronales artificiales (excedente de 2.1.4.3)` con sus cuatro subapartados (neurona y perceptrón · MLP · retropropagación y descenso de gradiente · qué las distingue del ML clásico). En el cuerpo queda el resumen con `[6, cap. 6]` |
> | D-4 agrupamiento | `2.1.4.4` | **APLICADO** — un párrafo que declara que no se emplea y remite a `A.3` §A.3.10.2 y `A.2` §A.2.2.2 |
> | D-5 micro-F1 | `2.1.5.3` | **APLICADO** — el apartado se titula hoy «*Promediado multiclase: macro y ponderado*» y la viñeta «Micro» no está. **Salvedad, abajo** |
> | D-6 métricas ajenas a la clasificación | `2.1.5.6` | **APLICADO** — reducido a una frase que declara que no se reportan y remite a `A.2` §A.2.2 |
> | D-7 ciclo de vida y CRISP-DM | `2.1.3`, `2.1.6.1` | **APLICADO** — los seis apartados de `2.1.3` son hoy remisiones breves; los «pasos 1 a 6» y el *callout* de despliegue no están, y la distinción CV / *K-fold* / desviación típica vive **solo** en el *callout* «Tres términos que no son sinónimos» de `2.1.6.3`, con `2.1.3.4` remitiendo a él |
> | D-8 rejilla de hiperparámetros | `2.1.6.4` | **APLICADO. Pero la sede NO es la que dice D-8: ver la corrección abajo** |
> | D-9 inventario de las tres decisiones sobre D2 | `2.1.6.2` | **APLICADO** — el *callout* «Declaración: tres decisiones…» conserva la lectura conceptual y remite el inventario a `4.3.5`, `6.1` §6.1.3 y `A.3` §A.3.11.2 |
> | D-10 tres notas de trabajo | `2.1.4.2.1`, `2.1.4.3`, `2.1.6.8` | **APLICADO** — ninguno de los tres *callouts* (atribución del Isolation Forest, localizador de `[6]`, verificación pendiente de Arp y Chow) sigue en las notas. La reasignación a `[73]` Liu, Ting y Zhou **sí** quedó en el texto de `2.1.4.2.1`, que es lo que se quería conservar |
>
> **Las tres salvedades, y ninguna es un «no aplicado»:**
>
> 1. **D-8 apunta a una sede equivocada.** Dice «*la rejilla no desaparece de la memoria: vive en
>    `4.5`, que es su sede*». **Falso en disco:** `2.1.6.4` remite a «*la ficha del sistema, `A.3`
>    (§A.3.3)*» y `4.5` remite exactamente a lo mismo («*Los valores concretos de cada rejilla están
>    en el Apéndice A.3 (§A.3.3)*»). **La sede de los valores es `A.3` §A.3.3**; `4.5` describe qué
>    ejes se exploran y con cuántas combinaciones, pero no los tabula. El argumento de defensa de
>    D-8 —rejilla pequeña y publicada— no cambia; el sitio al que hay que señalar, sí.
> 2. **Residuo de redacción de D-5, en la nota y no en este informe.** `2.1.5.3` retiró la viñeta
>    «Micro» pero conserva dos menciones al recuento anterior: «*mediante alguno de **tres** esquemas
>    de promediado*» y «*La elección entre **estos tres** esquemas*». **No se corrige desde aquí**:
>    es una nota de la memoria y esta ficha es de solo lectura sobre ellas. Queda señalado para que
>    se despache.
> 3. **`2.1.4.5` conserva el título «Transición»** con ~110 palabras, cuando el plan lo dejaba en
>    ~40. Es compresión pendiente, no material retirado: no afecta a ninguna partida de este §4.

Cada bloque, con la pregunta previsible que responde y lo que hay que llevar sabido.

### D-1. «¿Por qué no ha usado aprendizaje por refuerzo?» — retirado de `2.1.2.3` (155 palabras)
Porque no hay entorno, ni acción, ni política que optimizar: la detección opera sobre datos
estáticos ya recogidos (NSL-KDD), y la recompensa demorada que el refuerzo necesita no existe en
este planteamiento. El refuerzo tendría sentido en un IDS **de respuesta**, que decidiera qué acción
de contención tomar y recibiera realimentación del analista; eso es otro sistema, y encaja como
línea futura, no como componente de este.

### D-2. «Su detector de anomalías, ¿es supervisado, no supervisado o semisupervisado?» — se queda `2.1.2.6`; se retira el marco general de `2.1.2.5`
La respuesta canónica **se queda en el cuerpo** y es la más probable de todas las preguntas de
vocabulario. Lo que se retira es solo el marco general del aprendizaje auto-supervisado. Para la
defensa: el autoencoder tiene **mecanismo** auto-supervisado (la señal de entrenamiento es la propia
entrada reconstruida) y **régimen de supervisión** *one-class* (solo ve tráfico normal, el split D1,
seleccionado con la etiqueta que sí existe). Las dos lecturas son compatibles; la memoria usa la
segunda porque es la relevante para detección. Que `scikit-learn` lo documente como «no supervisado»
no es una contradicción, es otra convención.

### D-3. «Explíqueme cómo funciona por dentro el autoencoder que ha elegido» — retirado de `2.1.4.3` al apéndice `A.3` (778 palabras)
El bloque más valioso de todo lo retirado, y el que **hay que llevar preparado**, porque el
autoencoder es el detector ganador de la etapa 1. Cadena a saber: neurona artificial = combinación
lineal ponderada más sesgo, seguida de una activación no lineal → el perceptrón simple solo separa
linealmente (limitación XOR) → apilar capas ocultas con activación no lineal levanta esa limitación
(aproximación universal) → se entrena minimizando una pérdida con descenso de gradiente estocástico
por lotes, y el gradiente respecto a todos los pesos se calcula con retropropagación (regla de la
cadena desde la salida hacia la entrada) → activaciones habituales: sigmoide y tanh saturan y
atenúan el gradiente, ReLU es el estándar actual → en este trabajo, un `MLPRegressor` de
`scikit-learn` entrenado con `fit(X, X)`, arquitecturas `(64, 32, 64)` y `(32, 16, 32)`,
`early_stopping=True`, `max_iter=300`, y **puntuación de anomalía = MSE de reconstrucción por
muestra** (de ahí la magnitud de 10⁻⁵ sobre datos normalizados). Pregunta trampa asociada: **no es
*deep learning***, y la razón está en `2.3.1` — profundidad insuficiente y ausencia de jerarquía de
representaciones; se eligió así a propósito para no salir del ecosistema `scikit-learn`.

### D-4. «¿Y si el problema hubiera sido de agrupamiento? ¿Por qué no probó k-means?» — retirado de `2.1.4.4`; desarrollo ya en `A.3.10.2`
Porque el agrupamiento no usa la etiqueta, y aquí la etiqueta «normal» **existe y es
aprovechable**: usarla para aislar D1 es información legítimamente disponible, y renunciar a ella
sería mutilar el entrenamiento sin ganar nada. Como métrica interna, un agrupamiento se evaluaría
con el coeficiente de silueta (`A.2` §A.2.2.2), que valora cohesión frente a separación sin
etiquetas — precisamente por eso no es comparable con el recall y el FPR que este trabajo publica.

### D-5. «¿Por qué no reporta micro-F1?» — retirado de `2.1.5.3` (54 palabras)
Porque en un problema multiclase de una sola etiqueta por muestra el **micro-F1 coincide con la
exactitud global**, y la exactitud es exactamente la métrica que este trabajo descarta por engañosa
bajo desbalance (`dos` con 45.927 muestras frente a 52 de `u2r` en D3). Reportar micro sería
reportar dos veces el mismo número engañoso. Se publican macro —que impide que la clase mayoritaria
tape a `u2r`— y ponderado, este último como columna `f1_weighted`, precisamente para que se vea el
contraste entre ambos.

### D-6. «¿Y las métricas de regresión? ¿MAE, RMSE?» — retirado de `2.1.5.6`; desarrollo ya en `A.2.2`
No aplican: no hay ninguna tarea de regresión en el sistema. El único regresor del proyecto, el
`MLPRegressor`, no se evalúa como regresor: su error de reconstrucción es la **entrada** de una
decisión de clasificación, no una predicción numérica que haya que medir con MAE o RMSE. Quedan
definidas en `A.2` §A.2.2 por completitud del marco.

### D-7. «¿Siguió una metodología reconocida? Descríbame las fases» — comprimido de `2.1.3` y `2.1.6.1` (~1.200 palabras retiradas del cuerpo)
CRISP-DM, seis fases, iterativo, adoptado como marco de ordenación y no como corsé. Mapeo:
comprensión del problema y de los datos → EDA y validación de splits (`program.py`,
`validacion.py`); preparación → `4.3`; modelado → `4.4` y `4.5` por separado; evaluación → pase
único de extremo a extremo sobre D2 (`5.3`). **La sexta fase, el despliegue, queda fuera del alcance
de forma declarada**, y esa declaración es deliberada: presentar resultados de laboratorio como
capacidades operativas es una de las críticas recurrentes al ML aplicado a la seguridad. Si
preguntan por el orden fino de fases de un proyecto de ML genérico, ahí está el material retirado
de `2.1.3`: comprensión → limpieza y escalado → ingeniería y selección de características →
exploración de varios candidatos con configuración estándar → ajuste de hiperparámetros por
validación cruzada → medida final sobre datos no vistos, con retrocesos entre fases cuando una
decisión posterior revela un problema anterior.

### D-8. «¿Cuál era la rejilla exacta de hiperparámetros?» — retirado de `2.1.6.4` por petición del profesor
Es el **único** recorte de 2.1 atribuible a él. La rejilla no desaparece de la memoria: **sus valores
viven en `A.3 Ficha del sistema` §A.3.3**, que es su sede única —verificado en disco el 2026-08-21;
`4.5` declara los ejes y el número de combinaciones y remite allí para las cifras, igual que hace
hoy `2.1.6.4`—. El argumento a defender es el criterio, no los números: **rejilla pequeña y
publicada**, por dos razones — se comparan arquitecturas, no se exprime un algoritmo (un presupuesto
de búsqueda desigual contaminaría la comparación, porque el ganador podría serlo por haber recibido
más ajuste), y una rejilla publicada es auditable. En la etapa de anomalías el mecanismo no puede
ser el mismo, porque sin etiquetas de ataque no hay validación cruzada supervisada que puntúe: la
configuración se resuelve por AUC-ROC sobre `D1_val` más una muestra de 5.000 filas de D3, y el
umbral se fija después en el percentil 95 sobre `D1_val`.

### D-9. «Ha declarado que tres decisiones se tomaron mirando el test. ¿No invalida eso sus resultados?» — comprimido en `2.1.6.2`; inventario en `4.3.5` y `6.1`
El inventario se comprime en `2.1.6.2` pero **no se pierde**: se defiende con las sedes de `4.3.5` y
`6.1`. Detector de la etapa 1 (Autoencoder-MLP, por AUC-ROC y F1 sobre D2), clasificador de la
etapa 2 (RandomForest, por `f1_macro` sobre D2) y set de características (54 frente a 122, por
recall 0-day y `f1_macro` sobre D2). Las tres son selección de modelo sobre el test, es decir *data
snooping*, y las métricas publicadas son por tanto optimistas. La tercera es la más estructural: no
elige un modelo dentro de un espacio de características dado, **define ese espacio** para todo el
sistema publicado. La magnitud del sesgo **no se estima** —haría falta un conjunto de decisión
independiente de D2— y la corrección queda como línea futura. Lo que sí se sostiene es que el resto
del perímetro es estructural y no de disciplina: `hibrido.py::_calibrar_umbral_conf` **no recibe D2
en su firma**, así que calibrar mirando el test es imposible por construcción.

### D-10. Notas de trabajo retiradas (344 palabras) — no son material de defensa, pero conviene saber qué dicen
- **Atribución del Isolation Forest** (107): la descripción del algoritmo se citaba a Molnar `[54]`,
  obra de interpretabilidad que no es la fuente original; se reasignó a la fuente primaria, Liu,
  Ting y Zhou (2008), `[73]`. Si preguntan por rigor bibliográfico, es un buen ejemplo de auditoría
  propia.
- **Localizador de `[6]`** (89): Goodfellow está anclada a `cap. 6` («Deep Feedforward Networks»);
  la página exacta no se pudo verificar sin el texto paginado, y se marca en lugar de inventarse.
- **Verificación pendiente** (148): de Arp et al. (2022) `[18]` se toman solo la existencia y la
  denominación de los errores catalogados (P3 *Data Snooping*, P5 *Biased Parameter Selection*,
  P7 *Inappropriate Performance Measures*, P8 *Base Rate Fallacy*), **sin ninguna cifra**, y cada
  afirmación se sostiene con el ejemplo del propio proyecto; de Chow (1970) `[16]` depende solo la
  **salvedad** de que la optimalidad de la regla de rechazo se define sobre posteriores verdaderas,
  que limita lo afirmable del umbral en vez de respaldar un resultado.

---

## 5. Método y trazabilidad de las cifras

- Totales por nota: `wc -w` sobre los seis ficheros de `02 Marco Teórico/2.1 Machine Learning/`.
- Desglose por apartado: suma de palabras entre encabezados con `awk`, atribuyendo cada bloque al
  encabezado que lo precede. No incluye el *frontmatter* YAML (15–27 palabras por nota), que sí
  entra en los totales de `wc -w`; de ahí que la suma de apartados quede unas decenas de palabras
  por debajo del total de cada nota.
- Bloques internos (*callouts*, viñetas, párrafos) contados por rango de líneas con `awk` en el
  momento de redactar este informe. **Ninguna cifra de este informe es una estimación a ojo.** Si
  alguien reedita una nota, los rangos de línea caducan: los bloques se identifican aquí por su
  **título o su primera frase**, que es lo que hay que buscar para relocalizarlos.
- Uso implícito: recuento con `grep -Ec` fichero a fichero sobre las 17 notas de
  `03 Diseño del sistema/`, `04 Implementación del sistema/` y `05 Evaluación/`. Se descartaron dos
  falsos positivos detectados al revisar: `ROC` sin delimitador coincide con «protocolo» y
  «procesamiento», y `EDA` coincide con «queda» y «puede»; ambos se recontaron con `\b`.
- Métricas publicadas: verificadas contra las cabeceras de `Resultados/metricas_firmas.csv` y
  `Resultados/metricas_hibrido.csv`, no contra la prosa.
- Los objetivos de palabras por apartado son **presupuestos de redacción**, no medidas: el ahorro de
  4.255 palabras es la suma de los recortes propuestos sobre bloques contados, y habrá que
  reverificarlo con `wc -w` cuando la reescritura esté hecha.
