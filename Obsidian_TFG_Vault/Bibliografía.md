---
titulo: "Bibliografía"
numero: "-"
estado: borrador
docx_ref: "Desarrollo (referencias)"
---

# Bibliografía

> [!info] Tabla de *staging* — auditada el 2026-08-09 (T15)
> Este fichero **no es la bibliografía final**: es la tabla de trabajo desde la que Francisco hará
> el pase mecánico a Zotero en formato IEEE. Cada entrada lleva su **cita completa**, su **DOI o
> URL estable** y su **nivel de fiabilidad** a la vista, para que no se cuele una fuente de nivel
> 2-3 sosteniendo una afirmación fuerte.
>
> **Niveles:** **1** revisado por pares con DOI · norma o estándar · organismo oficial ·
> documentación oficial · libro con ISBN de editorial reconocida — cita sin reservas.
> **2** preprint, tesis, informe técnico de empresa, *white paper* — admisible declarando la
> reserva. **3** blog, prensa, web sin autor ni fecha, copia no autorizada — **no sostiene nada**.
>
> Informe de la auditoría: [[Auditoría de Bibliografía]].
> **La numeración no se reordena**: los `[n]` están usados en las notas. `[9]` queda retirada y su
> número **no se reutiliza**.

> [!danger] Reconstrucción de `[11]`-`[57]` — 2026-08-15
> Las 47 entradas de `[11]` a `[57]` se dieron de alta en un **pase de reparación**: los marcadores
> ya estaban puestos en las notas del capítulo 2 desde un pase anterior que murió antes de
> escribir aquí, de modo que la memoria arrastraba 47 referencias colgantes. El mapa `[n]` → fuente
> **no existía en ningún fichero** y se ha reconstruido leyendo el contexto de cada sitio de cita.
> Informe del pase: [[Reconstrucción de las 47 citas colgantes]].
>
> Por eso conviven tres grados de certeza, marcados **en la propia fila**:
> - **Sin marca** — la nota nombra a la fuente (autor, obra o pitfall) o la fuente ya estaba
>   verificada en `99 Investigación/`. Cita cerrada.
> - **⚠️ identidad inferida del contexto** — la obra es la candidata canónica para lo que el texto
>   afirma, y sus metadatos están verificados, **pero nadie ha confirmado que sea la que se
>   consultó**. Antes del pase a Zotero, Francisco debe confirmar cada una.
> - **⚠️ NO RECONSTRUIDA** — no se ha podido determinar la fuente. Son **cinco**: `[27]`, `[28]` y
>   `[44]`, sin pista alguna en el texto, y `[37]` y `[45]`, identificables como clase de documento
>   pero con la **edición indeterminable**. **No se ha inventado ninguna cita**: la fila lleva
>   candidatos propuestos y `—` en los campos que no se saben.
>
> **Ninguna de las 47 se ha puesto ni cambiado en las notas**: la numeración se toma como dada.

> [!info] Tanda 9 — conversión de `[CITA: …]` a `[n]` y columna «Localizador por uso» (2026-08-15)
> Pase **en serie**: se han convertido **36 marcadores `[CITA: …]` vivos** — **33 en las notas de la
> memoria** (`4.2` 6 · `5.0` 5 · `6.1` 7 · `6.2` 8 · `A.3` 7 = 33) **más los 3 de `EL_FUTURO.md`**.
> (La cifra decía «33 marcadores» y luego sumaba 3 aparte: la unidad y el número no casaban.
> Corregido el 2026-08-16, Tanda 13.)
> De ellos, **23 se han MAPEADO a entradas que ya existían** —`[17]`, `[18]`, `[20]`, `[22]`,
> `[23]`, `[25]`, `[31]`, `[49]`, `[50]`, `[51]`, `[52]`— y **13 han requerido alta nueva**:
> **`[58]`-`[67]`, diez entradas**, todas verificadas contra Crossref o contra la web oficial del
> editor. **Ningún `[n]` preexistente se ha renumerado ni reasignado**, y `[9]` sigue quemada.
> **El primer número libre pasó a ser el `[68]`** — y la **Tanda 13 ya lo consumió**: ver el callout
> siguiente. **Hoy el primer libre es el `[76]`** (la Tanda 14 dio de alta `[74]` y `[75]`).
>
> **Columna «Localizador por uso» (decisión de Francisco del 2026-08-15).** Francisco genera el
> formato IEEE en Zotero; de aquí necesita **de qué obra y de qué página** sale cada afirmación.
> El marcador admite localizador IEEE nativo —`[8, cap. 1]`, `[5, cap. 1]`, `[67, §4.5]`—, que
> **no consume número nuevo**. La columna es **obligatoria solo en los 8 libros**: `[4]`, `[5]`,
> `[6]`, `[7]`, `[8]`, `[12]`, `[39]` y `[54]`. En artículos dice `— (no es libro)`.
> **Cuidado con el falso amigo:** los `pp. 222-232` de la columna «Cita completa» son el **rango
> del artículo en su revista**, metadato de la referencia, **no** el localizador de la afirmación.
>
> **Lo que NO se ha podido establecer, y se marca en vez de inventarse** —misma disciplina que con
> las 47 citas reconstruidas—: ~~`[6]` Goodfellow (**huérfana**, depende de T24)~~ **— YA NO: T24 la ancló
> el 2026-08-15 (`296de24`) en `2.1.4.3` con `[6, cap. 6]`, 7 ocurrencias verificadas en disco el
> 2026-08-16**; `[54]` Molnar
> (**edición sin fijar**), `[4]` Chio (sin acceso al texto completo), `[7]` Murphy (además con una
> reserva de fondo sobre lo que la obra cubre) y el uso de `[5]` en `2.1.3`. Los cinco llevan su
> razón escrita en la propia celda.

> [!info] Tanda 13 — segundo pase en serie de `[CITA: …]` → `[n]` (2026-08-16)
> Pase **en serie**, con el vault en exclusiva. Se han convertido los **36 marcadores `[CITA: …]`
> vivos** del **capítulo 2** (`2.1.1` 3 · `2.1.3` 4 · `2.1.4` 16 · `2.1.5` 8 · `2.2.4` 3 = **34**) y del
> **capítulo 3** (`3.5` 2). **Censo contado contra disco antes y después**, no recordado.
> **30 se han MAPEADO a entradas ya existentes** —`[5]` Géron (×20), `[12]` Hastie (×7), `[6]`
> Goodfellow ya estaba puesto— y **6 han requerido alta nueva: `[68]`-`[73]`**, todas con DOI
> resuelto y todas con respaldo previo en `99 Investigación/`. **Ningún `[n]` preexistente se ha
> renumerado ni reasignado**, y `[9]` sigue quemada. **El primer número libre pasó a ser el `[74]`, hoy
> consumido por la Tanda 14: el primer libre es el `[76]`.**
>
> **Lo que quedan siendo `[CITA:` en disco NO son marcadores pendientes:** los 2 de este fichero y el
> de `4.2` son **prosa sobre la convención**, y los 11 de
> [[Reconstrucción de las 47 citas colgantes]] son informe, no memoria.
>
> **Localizadores sembrados en el texto, que es donde la decisión del 2026-08-15 los pedía:** 27 de
> los 36 marcadores bajan ya con capítulo (`[5, cap. 1]`…`[5, cap. 9]`, `[12, cap. 9]`…`[12, cap. 15]`).
>
> **Lo que NO se ha podido establecer, y se marca en vez de inventarse:**
> - **`2.1.5:114`** (MAE/RMSE): el marcador decía «Géron, cap. 4» y eso no cuadra —la contraposición
>   vive en el cap. 2—. Convertido a `[5]` **sin capítulo**. **Decide Francisco.**
> - **`2.1.4:77`** (Local Outlier Factor): el marcador decía «Hastie, cap. 14», capítulo que **no
>   trata LOF**. Convertido a `[12]` **sin capítulo**, con la fuente primaria propuesta en la fila de
>   `[12]`. **Decide Francisco**, porque reasignar una fuente por otra no lo decide un agente.
>
> **Una reasignación SÍ ejecutada, y por encargo escrito:** el `[CITA: Molnar, cap. 8]` de
> `2.1.4.2.1` (Isolation Forest) **no se ha convertido a `[54]`**. Un callout de la propia nota
> encargaba verificar esa atribución antes de convertirla; verificada, la cita se ha reasignado a la
> **fuente primaria del algoritmo**, `[73]` Liu, Ting y Zhou (2008). Efecto colateral bueno: la
> **edición sin fijar de `[54]` Molnar ya no bloquea ningún localizador del capítulo 2**.

> [!info] Tanda 14 — último `[CITA: …]` de la memoria y las dos reasignaciones aprobadas (2026-08-16)
> Pase **en serie**, censo contado contra disco antes y después: 72 filas antes (`[1]`-`[8]` y
> `[10]`-`[73]`), **74 después**. **`[9]` sigue quemada** y **ningún `[n]` preexistente se ha
> renumerado**. **El primer número libre es el `[76]`.**
>
> - **`[74]` Goldschmidt y Chudá (2025)** — alta nueva. Era el **único `[CITA: …]` vivo de toda la
>   memoria** (`4.2:62`). Cifras verificadas **verbatim** en el propio artículo: *«Only 23% (16%
>   since 2020) provide predefined train-test data splits… prone to biased evaluations and selective
>   reporting»*. **Pero la atribución que traía la nota era errónea**: no es §5.4 ni el marco de
>   «congresos CORE A*/A 2020-2023» —esa es la población de §5.4, 45 artículos, de donde sale «NSL-KDD
>   was used only three times»—, sino **§5.5.4**, medido sobre **los 89 datasets del *survey***. El
>   marcador se ha convertido a **`[74, §5.5.4]`** y la frase de `4.2` se ha corregido para no colgar
>   el dato de la población equivocada.
> - **`[75]` Breunig, Kriegel, Ng y Sander (2000)** — alta nueva **por reasignación aprobada por
>   Francisco**: el uso de **LOF** en `2.1.4.2.3` citaba `[12]` Hastie, cuyo cap. 14 no trata LOF.
>   Mismo precedente que el Isolation Forest → `[73]`.
> - **`[5, cap. 2]`** estampado en `2.1.5:114` (MAE frente a RMSE), también por decisión de Francisco:
>   el marcador original decía «cap. 4» y el cap. 4 es «Training Models». **Reserva declarada en la
>   celda de `[5]`:** el capítulo se establece por estructura del libro, no por texto paginado; la
>   **página exacta sigue sin establecerse**.
> - **Recuentos corregidos:** `[23]` en `4.2` era `×3` y en disco son **`×5`**; `[12]` en `2.1.4` era
>   `×7` y baja a **`×6`** tras la reasignación de LOF; `[17]` y `[18]` suman el uso de **`4.3`**
>   (§4.3.7 «Preprocesado sin fuga de datos», Arp por **P3** y **P5**).

| `[n]` | Cita completa | DOI / URL estable | Nivel | Dónde se usa | Localizador por uso |
|---|---|---|---|---|---|
| [1] | Instituto Nacional de Ciberseguridad (INCIBE), «INCIBE presenta su balance de ciberseguridad 2024 con más de 97.000 incidentes gestionados», nota de prensa, 20 de marzo de 2025. **Dato citado:** 97.348 incidentes gestionados en 2024, un 16,6 % más que en 2023; 65.808 (67,6 %) afectaron a la ciudadanía y 31.540 (32,4 %) a empresas; 7.470 intrusiones o intentos de acceso no autorizado; 42.136 casos de *malware*, de ellos 357 de *ransomware* | https://www.incibe.es/incibe/sala-de-prensa/incibe-presenta-su-balance-de-ciberseguridad-2024-con-mas-de-97000-incidentes | **1** | `1.1 Motivación` |
| [2] | J. P. Anderson, *Computer Security Threat Monitoring and Surveillance*. Fort Washington, PA: James P. Anderson Co. (Box 42, Fort Washington, PA 19034), contrato 79F296400, 26 de febrero de 1980 (revisado el 15 de abril de 1980) | http://csrc.nist.gov/publications/history/ande80.pdf | **2** | `1.2 Preliminares` |
| [3] | D. E. Denning, «An Intrusion-Detection Model», *IEEE Transactions on Software Engineering*, vol. SE-13, n.º 2, pp. 222-232, feb. 1987 | 10.1109/TSE.1987.232894 | **1** | `1.2 Preliminares` |
| [4] | C. Chio y D. Freeman, *Machine Learning and Security: Protecting Systems with Data and Algorithms*, 1.ª ed. Sebastopol, CA: O'Reilly Media, 2018, 383 pp. ISBN 978-1-4919-7990-7 | ISBN 978-1-4919-7990-7 (sin DOI; sitio oficial del libro: https://mlsec.net/) | **1** | `2.1.1 Introducción al ML` | ⚠️ **NO ESTABLECIDO.** Uso único: `2.1.1:18` (el DL como subconjunto estricto del ML). Candidato razonable: cap. 1 «Why Machine Learning and Security?», donde el libro fija la terminología — **sin acceso al texto completo, no se confirma**. No se inventa página |
| [5] | A. Géron, *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow: Concepts, Tools, and Techniques to Build Intelligent Systems*, 2.ª ed. Sebastopol, CA: O'Reilly Media, 2019. ISBN 978-1-492-03264-9 | https://www.oreilly.com/library/view/hands-on-machine-learning/9781492032632/ | **1** | `2.1.1 Introducción al ML` (×3), `2.1.2 Tipos de ML`, `2.1.3 Ciclo de vida de un proyecto ML` (×5), `2.1.4 Algoritmos de ML` (×6), `2.1.5 Métricas de evaluación` (×8) | **`[5, cap. 1]`** para `2.1.1:12`, `:34` y `:40` (definición de ML y ciclo de trabajo; el texto cita además la **Figura 1.4**, que es del cap. 1) y para `2.1.2:30` y `:64` (las dos listas de algoritmos, que son las del cap. 1 «The Machine Learning Landscape» — es el hallazgo que motivó el aviso de [6]). · **`[5, cap. 2]`** para `2.1.1:59` (calidad y cantidad de los datos) y para `2.1.3:10`, `:19` y `:86` (secuencia del proyecto, repositorios públicos y las dos fases de despliegue), **y para `2.1.5:114` (MAE frente a RMSE, §«Select a Performance Measure»)**, todo ello «End-to-End Machine Learning Project». · **`[5, cap. 3]`** («Classification») para `2.1.4:46` y `:51` (k-NN) y para los seis usos de `2.1.5` sobre matriz de confusión, precisión/recall, micro-F1 y curvas ROC/PR. · **`[5, cap. 4]`** («Training Models») para `2.1.4:20`, `:22` y `:28` (regresión logística). · **`[5, cap. 5]`** («Support Vector Machines») para `2.1.4:71` (principio del hiperplano y del núcleo que One-Class SVM adapta). · **`[5, cap. 7]`** («Ensemble Learning and Random Forests») para `2.1.3:75`. · **`[5, cap. 9]`** («Unsupervised Learning Techniques») para `2.1.5:124` (coeficiente de silueta). · **Índice de capítulos verificado el 2026-08-16** contra el repositorio oficial del autor (`github.com/ageron/handson-ml2`). · ⚠️ **NO ESTABLECIDO** para `2.1.3:81` (estimar el error de generalización sobre el test): cabe tanto el cap. 1 («Testing and Validating») como el cap. 2, y el texto no permite decidir. · ✅ **RESUELTO el 2026-08-16** para `2.1.5:114` (MAE frente a RMSE): el marcador original decía «cap. 4» y no cuadraba —el cap. 4 es «Training Models»—; la contraposición MAE/RMSE vive en el **cap. 2, «Select a Performance Measure»**, donde Géron presenta las dos medidas y contrapone su sensibilidad a los valores atípicos. **Francisco aprobó fijarlo**, y la nota lleva ya **`[5, cap. 2]`**. ⚠️ **Reserva de verificación:** el capítulo se ha establecido por la **estructura del libro** (cap. 2 = proyecto de extremo a extremo, con la selección de la medida de rendimiento; cap. 4 = entrenamiento de modelos) y por resúmenes coincidentes del contenido de esa sección; **el texto paginado no es accesible** (la ficha oficial de O'Reilly devuelve 403 a cualquier acceso automático), así que **la página exacta NO se establece** · ⚠️ **Reserva menor** sobre `2.1.4:46` y `:51`: el cap. 3 usa k-NN en sus ejercicios pero no desarrolla el aprendizaje perezoso ni las métricas de distancia con el detalle que el texto atribuye |
| [6] | I. Goodfellow, Y. Bengio y A. Courville, *Deep Learning*. Cambridge, MA: MIT Press, 2016. ISBN 978-0-262-03561-3 | https://www.deeplearningbook.org/ | **1** | `2.1.4 Algoritmos de ML` (2.1.4.3, **7 ocurrencias**: neurona artificial y perceptrón, MLP y aproximación universal, funciones de activación, descenso de gradiente y retropropagación). **YA NO ESTÁ HUÉRFANA** — T24 la ancló el 2026-08-15 (`296de24`) y el recuento está **verificado contra disco el 2026-08-16** | **`[6, cap. 6]`** — «Deep Feedforward Networks», que es el capítulo dedicado a MLP, funciones de activación y retropropagación. ⚠️ **La página exacta NO se establece**: no hay acceso al texto paginado. La propia nota lo declara en un `[!todo]` de `2.1.4.3.4` |
| [7] | K. P. Murphy, *Machine Learning: A Probabilistic Perspective*. Cambridge, MA: MIT Press, 2012. ISBN 978-0-262-01802-9 | https://dl.acm.org/doi/book/10.5555/2380985 | **1** | `2.1.2 Tipos de ML` (2.1.2:68, aprendizaje semi-supervisado y auto-supervisado) | ⚠️ **NO ESTABLECIDO**, y con **reserva de fondo**: el uso menciona el aprendizaje **auto-supervisado**, término que no es vocabulario de *MLaPP* (2012) — el semi-supervisado sí lo trata el cap. 1. Antes de fijar página hay que decidir si la fuente cubre de verdad las dos mitades de la frase. **Decide Francisco** |
| [8] | W. Stallings y L. Brown, *Computer Security: Principles and Practice*, 4.ª ed. Pearson, 2018. ISBN 978-0-13-479410-5 | https://www.pearson.com/en-us/subject-catalog/p/computer-security-principles-and-practice/P200000010333 | **1** | `2.2.1 Introducción a la ciberseguridad` (definición de *Computer Security* y conceptos añadidos) | **`[8, cap. 1]`** — los dos usos (`2.2.1:10`, definición del NIST, y `2.2.1:32`, autenticidad y responsabilidad) viven en el **cap. 1, §1.1 «Computer Security Concepts»**, que es la sección que la abre en todas las ediciones. · ⚠️ **Página exacta NO ESTABLECIDA a propósito**: depende de la edición, que sigue sin confirmar (ver aviso de [8]). No se inventa |
| ~~[9]~~ | **RETIRADA el 2026-08-09 — fundida en [8]** (baja autorizada por Francisco el 2026-08-06) | — | ~~3~~ | ver aviso |
| [10] | Centro Criptológico Nacional (CCN-CERT), *Guía de Seguridad de las TIC CCN-STIC-401: Glosario y Abreviaturas*, entrada «ciberseguridad» | https://www.ccn-cert.cni.es/publico/seriesCCN-STIC/series/400-Guias_Generales/401-glosario_abreviaturas/index.html?n=189.html | **1** | `2.2.1 Introducción a la ciberseguridad` |
| [11] | P. Chapman, J. Clinton, R. Kerber, T. Khabaza, T. Reinartz, C. Shearer y R. Wirth, *CRISP-DM 1.0: Step-by-step data mining guide*. CRISP-DM Consortium / SPSS Inc., 2000 | https://www.kde.cs.uni-kassel.de/wp-content/uploads/lehre/ws2012-13/kdd/files/CRISPWP-0800.pdf | **2** | `2.1.6 Metodologías y buenas prácticas` (2.1.6.1, las seis fases) |
| [12] | T. Hastie, R. Tibshirani y J. Friedman, *The Elements of Statistical Learning: Data Mining, Inference, and Prediction*, 2.ª ed. Nueva York: Springer, 2009. ISBN 978-0-387-84857-0 · ⚠️ **identidad inferida del contexto** | 10.1007/978-0-387-84858-7 · https://hastie.su.domains/ElemStatLearn/ | **1** | `2.1.6` (2.1.6.2, error de generalización sobre datos no vistos), `2.1.4 Algoritmos de ML` (**×6 desde el 2026-08-16**: árboles, bosques, *boosting* y agrupamiento; eran ×7 hasta que el uso de **LOF** se reasignó a `[75]`, su fuente primaria) | **`[12, cap. 7]`** — «Model Assessment and Selection», **pp. 219-259** de la 2.ª ed. (rango del capítulo verificado en el registro Springer del propio capítulo, DOI 10.1007/978-0-387-84858-7_7). ⚠️ **La página exacta dentro del capítulo no se establece**: la identidad de la fuente sigue siendo inferida del contexto. · **`[12, cap. 9]`** («Additive Models, Trees, and Related Methods») para `2.1.4:32` (árboles de decisión, CART). · **`[12, cap. 10]`** («Boosting and Additive Trees») para `2.1.4:41` (*gradient boosting*). · **`[12, cap. 15]`** («Random Forests») para `2.1.4:38` y `:40`. · **`[12, cap. 14]`** («Unsupervised Learning») para `2.1.4:126` (k-means, §14.3.6) y `:130` (agrupamiento jerárquico, §14.3.12). · ✅ **RESUELTO el 2026-08-16 — el uso de LOF ya NO es de esta entrada.** El marcador de `2.1.4` (Local Outlier Factor) decía «Hastie, cap. 14» y ese capítulo no trata LOF. **Francisco aprobó la reasignación a la fuente primaria**, ejecutada ese día: la cita es hoy **`[75]`** (Breunig, Kriegel, Ng y Sander, 2000). Mismo precedente que el Isolation Forest → `[73]`. Con ello `[12]` queda con los seis usos de `2.1.4` localizados arriba y **ningún uso sin capítulo** |
| [13] | R. Kohavi, «A Study of Cross-Validation and Bootstrap for Accuracy Estimation and Model Selection», en *Proc. 14th International Joint Conference on Artificial Intelligence (IJCAI'95)*, vol. 2, Morgan Kaufmann, 1995, pp. 1137-1143 | https://dl.acm.org/doi/10.5555/1643031.1643047 | **1** | `2.1.6` (2.1.6.3, validación cruzada K-fold) |
| [14] | scikit-learn, «`sklearn.model_selection.GridSearchCV`» — documentación oficial · ⚠️ **identidad inferida del contexto** (alternativa: F. Pedregosa *et al.*, «Scikit-learn: Machine Learning in Python», *JMLR*, vol. 12, pp. 2825-2830, 2011) | https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html | **1** | `2.1.6` (2.1.6.4, búsqueda exhaustiva en rejilla) |
| [15] | J. Bergstra e Y. Bengio, «Random Search for Hyper-Parameter Optimization», *Journal of Machine Learning Research*, vol. 13, pp. 281-305, 2012 | https://jmlr.org/papers/v13/bergstra12a.html | **1** | `2.1.6` (2.1.6.4, alternativa a la rejilla) |
| [16] | C. K. Chow, «On optimum recognition error and reject tradeoff», *IEEE Transactions on Information Theory*, vol. 16, n.º 1, pp. 41-46, ene. 1970 | 10.1109/TIT.1970.1054406 | **1** | `2.1.6` (2.1.6.4, regla de rechazo óptima) |
| [17] | S. Kapoor y A. Narayanan, «Leakage and the reproducibility crisis in machine-learning-based science», *Patterns*, vol. 4, n.º 9, art. 100804, 2023 · ⚠️ **identidad inferida del contexto** | 10.1016/j.patter.2023.100804 | **1** | `2.1.6` (2.1.6.5, fuga de información), `5.0 Protocolo de evaluación` (preprocesado previo al *split*), `4.3 Preprocesamiento de los datasets` (4.3.7, taxonomía de la fuga: preprocesado ajustado sobre el conjunto completo antes de partirlo) |
| [18] | D. Arp, E. Quiring, F. Pendlebury, A. Warnecke, F. Pierazzi, C. Wressnegger, L. Cavallaro y K. Rieck, «Dos and Don'ts of Machine Learning in Computer Security», en *31st USENIX Security Symposium*, USENIX Association, 2022, pp. 3971-3988 | https://www.usenix.org/conference/usenixsecurity22/presentation/arp · preprint arXiv:2010.09470 | **1** | `2.1.6` (2.1.6.2, 2.1.6.5, 2.1.6.6), `2.3.3 Límites y consideraciones éticas` (P9, P10), `5.0 Protocolo de evaluación` (P5), `6.1 Conclusiones` (P9, P10 y el catálogo de los diez *pitfalls*), `A.3 Ficha del sistema` (contaminación por selección sobre el test), `4.3 Preprocesamiento de los datasets` (4.3.7, *pitfalls* **P3** *Data Snooping* y **P5** *Biased Parameter Selection*) |
| [19] | H. He y E. A. Garcia, «Learning from Imbalanced Data», *IEEE Transactions on Knowledge and Data Engineering*, vol. 21, n.º 9, pp. 1263-1284, sept. 2009 · ⚠️ **identidad inferida del contexto** | 10.1109/TKDE.2008.239 | **1** | `2.1.6` (2.1.6.6, aprendizaje con clases desequilibradas) |
| [20] | J. Pineau, P. Vincent-Lamarre, K. Sinha, V. Larivière, A. Beygelzimer, F. d'Alché-Buc, E. Fox y H. Larochelle, «Improving Reproducibility in Machine Learning Research (A Report from the NeurIPS 2019 Reproducibility Program)», *Journal of Machine Learning Research*, vol. 22, n.º 164, pp. 1-20, 2021 | https://www.jmlr.org/papers/v22/20-303.html | **1** | `2.1.6` (2.1.6.7, lista de comprobación de reproducibilidad), `5.0 Protocolo de evaluación` (terminología reproducible/replicable), `6.1 Conclusiones` (ítems *number of runs*, *error bars*, *central tendency*), `A.3 Ficha del sistema` (×4: ítem *statistics*, vocabulario de replicabilidad y los 11 ítems «FT») |
| [21] | R. Sommer y V. Paxson, «Outside the Closed World: On Using Machine Learning for Network Intrusion Detection», en *2010 IEEE Symposium on Security and Privacy*, Oakland, CA, 2010, pp. 305-316. Premio *Test of Time* IEEE S&P 2020 | 10.1109/SP.2010.25 | **1** | `2.1.6` (2.1.6.8 y definición de *semantic gap*, ×2), `2.2.3 Taxonomía de los IDS`, `2.3.2 La IA en ciberseguridad`, `2.3.3 Límites y consideraciones éticas`, `3.2 Arquitectura del sistema`, `3.4 Modelo de detección de anomalías` — **recontado contra disco el 2026-08-16: 6 notas, 7 ocurrencias** |
| [22] | J. McHugh, «Testing Intrusion Detection Systems: A Critique of the 1998 and 1999 DARPA Intrusion Detection System Evaluations as Performed by Lincoln Laboratory», *ACM Transactions on Information and System Security*, vol. 3, n.º 4, pp. 262-294, nov. 2000 | 10.1145/382912.382923 | **1** | `2.1.6` (2.1.6.8), `2.2.5 Taxonomía de ataques…`, `2.3.2`, `2.3.3`, `4.2 Base de datos utilizada` (crítica original a la evaluación DARPA/KDD) |
| [23] | M. Tavallaee, E. Bagheri, W. Lu y A. A. Ghorbani, «A Detailed Analysis of the KDD CUP 99 Data Set», en *Proc. 2nd IEEE Symposium on Computational Intelligence for Security and Defense Applications (CISDA)*, Ottawa, 2009, pp. 1-6 | 10.1109/CISDA.2009.5356528 · https://www.ee.torontomu.ca/~bagheri/papers/cisda.pdf | **1** | `2.1.6` (2.1.6.8), `2.2.5`, `2.3.2`, `2.3.3`, `4.2 Base de datos utilizada` (**×5, recontado contra disco el 2026-08-16**: los dos defectos del KDD'99 y la corrección de NSL-KDD —dos marcadores en el mismo párrafo—, la tabla de las tres particiones oficiales, el 20 % de KDDTrain+ con que se entrenaron los *baselines* canónicos, y la comparabilidad con la literatura. La columna decía ×3 y era un recuento caducado: los dos marcadores de Tavallaee que se convirtieron el 2026-08-16 no se habían sumado) |
| [24] | S. Axelsson, «The base-rate fallacy and the difficulty of intrusion detection», *ACM Transactions on Information and System Security*, vol. 3, n.º 3, pp. 186-205, ago. 2000 | 10.1145/357830.357849 | **1** | `2.1.6` (2.1.6.6), `2.2.4 Detección por firmas frente a…`, `2.3.3` |
| [25] | K. Scarfone y P. Mell, *Guide to Intrusion Detection and Prevention Systems (IDPS)*, NIST Special Publication 800-94. Gaithersburg, MD: National Institute of Standards and Technology, feb. 2007 | 10.6028/NIST.SP.800-94 | **1** | `2.2.2 Sistemas de detección de intrusiones` (2.2.2.1 y 2.2.2.3), `2.2.3`, `2.2.4`, `5.0 Protocolo de evaluación` (criterio de *tuning* de IDPS) |
| [26] | M. Roesch, «Snort — Lightweight Intrusion Detection for Networks», en *Proc. 13th USENIX Conference on System Administration (LISA'99)*, Seattle, WA, 7-12 nov. 1999, USENIX Association, pp. 229-238 · ⚠️ **identidad inferida del contexto** | https://www.usenix.org/legacy/publications/library/proceedings/lisa99/roesch.html | **1** | `2.2.2` (2.2.2.2, generación *open source* basada en reglas) |
| [27] | ⚠️ **NO RECONSTRUIDA** — sostiene «el IDS como productor de eventos dentro de plataformas SIEM/XDR» en `2.2.2:43`. Candidatos propuestos, **ninguno confirmado**: K. Kent y M. Souppaya, *Guide to Computer Security Log Management*, NIST SP 800-92, 2006 (10.6028/NIST.SP.800-92); o el capítulo de correlación de eventos de Stallings y Brown [8]. **Decide Francisco** | — | — | `2.2.2` (2.2.2.2, actualidad) |
| [28] | ⚠️ **NO RECONSTRUIDA** — sostiene el principio de **defensa en profundidad** en `2.2.2:91`. Candidatos propuestos, **ninguno confirmado**: W. Stallings y L. Brown [8] (cap. 1); NIST SP 800-53 Rev. 5, *Security and Privacy Controls for Information Systems and Organizations*, 2020 (10.6028/NIST.SP.800-53r5); o material del CCN-CERT. **Decide Francisco** | — | — | `2.2.2` (2.2.2.5, defensa en profundidad) |
| [29] | P. García-Teodoro, J. Díaz-Verdejo, G. Maciá-Fernández y E. Vázquez, «Anomaly-based network intrusion detection: Techniques, systems and challenges», *Computers & Security*, vol. 28, n.º 1-2, pp. 18-28, feb. 2009 · ⚠️ **identidad inferida del contexto** | 10.1016/j.cose.2008.08.003 | **1** | `2.2.3` (2.2.3.2, modelo de lo normal) |
| [30] | V. Chandola, A. Banerjee y V. Kumar, «Anomaly detection: A survey», *ACM Computing Surveys*, vol. 41, n.º 3, art. 15, pp. 1-58, jul. 2009 | 10.1145/1541880.1541882 | **1** | `2.2.3` (2.2.3.2), `2.2.4` (deriva del perfil normal) |
| [31] | A. Khraisat, I. Gondal, P. Vamplew y J. Kamruzzaman, «Survey of intrusion detection systems: techniques, datasets and challenges», *Cybersecurity*, vol. 2, art. 20, 2019 | 10.1186/s42400-019-0038-7 | **1** | `2.2.3` (2.2.3.3, SIDS/AIDS y el párrafo único sobre híbridos), `4.2 Base de datos utilizada` (*survey* de datasets NIDS), `6.1 Conclusiones` (los conjuntos KDD/DARPA ya no representan los 0-day contemporáneos) |
| [32] | D. Barbará, J. Couto, S. Jajodia y N. Wu, «ADAM: a testbed for exploring the use of data mining in intrusion detection», *ACM SIGMOD Record*, vol. 30, n.º 4, pp. 15-24, dic. 2001 | 10.1145/604264.604268 | **1** | `2.2.3` (antecedentes de la combinación anomalías + firmas), `3.2 Arquitectura del sistema`, `3.6 Conclusiones del capítulo` — **recontado contra disco el 2026-08-16** |
| [33] | E. Tombini, H. Debar, L. Mé y M. Ducassé, «A serial combination of anomaly and misuse IDSes applied to HTTP traffic», en *20th Annual Computer Security Applications Conference (ACSAC)*, IEEE, 2004, pp. 428-437 | 10.1109/CSAC.2004.4 | **1** | `2.2.3` (antecedentes de la cascada en serie), `3.2 Arquitectura del sistema` — **recontado contra disco el 2026-08-16** |
| [34] | T. H. Ptacek y T. N. Newsham, *Insertion, Evasion, and Denial of Service: Eluding Network Intrusion Detection*, informe técnico. Calgary: Secure Networks Inc., ene. 1998 · ⚠️ **identidad inferida del contexto** | https://apps.dtic.mil/sti/html/tr/ADA391565/index.html (copia archivada en DTIC) | **2** | `2.2.3` (2.2.3.4, técnicas de evasión) |
| [35] | Cisco / Snort Project, *Snort Users Manual* — sección «Writing Snort Rules» (documentación oficial) · ⚠️ **identidad inferida del contexto**; **falta fijar versión y fecha de consulta** | https://docs.snort.org/rules/ | **1** | `2.2.4` (2.2.4.1, ejemplo de regla) |
| [36] | K. Kendall, *A Database of Computer Attacks for the Evaluation of Intrusion Detection Systems*, tesis de máster (S.B./M.Eng.), Massachusetts Institute of Technology, jun. 1999 · ⚠️ **identidad inferida del contexto** (alternativa: R. Lippmann *et al.*, «Evaluating intrusion detection systems: the 1998 DARPA off-line intrusion detection evaluation», *DISCEX'00*, 2000, 10.1109/DISCEX.2000.821506) | https://archive.ll.mit.edu/ideval/files/kkendall_thesis.pdf · https://dspace.mit.edu/handle/1721.1/9459 | **2** | `2.2.5` (2.2.5.1, origen de las cuatro categorías) |
| [37] | ⚠️ **NO RECONSTRUIDA — falta fijar la edición.** Informe anual de panorama de amenazas de organismo público europeo. Candidato propuesto: ENISA, *ENISA Threat Landscape* (edición **por determinar**). El propio texto declara en `2.2.5:73-77` que la edición debe fijarse antes de la entrega y que no se cita ninguna cifra de ella. **Decide Francisco** | https://www.enisa.europa.eu/topics/cyber-threats/threats-and-trends (índice de la serie) | — | `2.2.5` (2.2.5.3), `2.3.2` (2.3.2.3) |
| [38] | B. E. Strom, A. Applebaum, D. P. Miller, K. C. Nickels, A. G. Pennington y C. B. Thomas, *MITRE ATT&CK®: Design and Philosophy*, informe técnico MITRE, jul. 2018 (rev. marzo 2020) · ⚠️ **identidad inferida del contexto** | https://www.mitre.org/sites/default/files/2021-11/prs-19-01075-28-mitre-attack-design-and-philosophy.pdf · matriz: https://attack.mitre.org/ | **2** | `2.2.5` (2.2.5.4, marco moderno de descripción de adversarios) |
| [39] | S. J. Russell y P. Norvig, *Artificial Intelligence: A Modern Approach*, 4.ª ed. Hoboken, NJ: Pearson, 2021. ISBN 978-0-13-461099-3 · ⚠️ **identidad inferida del contexto**; **falta confirmar la edición que maneja el autor** | https://aima.cs.berkeley.edu/ | **1** | `2.3.1 IA, ML y Deep Learning` (2.3.1.2, recorrido histórico) | **`[39, cap. 1]`** — el uso (`2.3.1:34`, el recorrido histórico como contexto del vocabulario) corresponde al **cap. 1, §1.3 «The History of Artificial Intelligence»**. ⚠️ **Páginas NO ESTABLECIDAS**: cambian entre la 3.ª y la 4.ª edición, y la edición que maneja el autor sigue sin confirmar |
| [40] | A. Krizhevsky, I. Sutskever y G. E. Hinton, «ImageNet Classification with Deep Convolutional Neural Networks», en *Advances in Neural Information Processing Systems 25 (NIPS 2012)*, pp. 1097-1105 · ⚠️ **identidad inferida del contexto** | https://papers.nips.cc/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html · versión CACM: 10.1145/3065386 | **1** | `2.3.1` (2.3.1.2, ImageNet 2012) |
| [41] | L. Grinsztajn, E. Oyallon y G. Varoquaux, «Why do tree-based models still outperform deep learning on tabular data?», en *Advances in Neural Information Processing Systems 35 (NeurIPS 2022)*, Datasets and Benchmarks Track, 2022 | https://proceedings.neurips.cc/paper_files/paper/2022/file/0378c7692da36807bdec87ab043cdadc-Paper-Datasets_and_Benchmarks.pdf · preprint 10.48550/arXiv.2207.08815 | **1** | `2.3.1` (2.3.1.3, datos tabulares), `3.5 Modelo de detección basado en firmas` — **recontado contra disco el 2026-08-16** |
| [42] | D. McElfresh, S. Khandagale, J. Valverde, V. Prasad C., G. Ramakrishnan, M. Goldblum y C. White, «When Do Neural Nets Outperform Boosted Trees on Tabular Data?», en *Advances in Neural Information Processing Systems 36 (NeurIPS 2023)*, Datasets and Benchmarks Track, 2023 | https://proceedings.neurips.cc/paper_files/paper/2023/hash/f06d5ebd4ff40b40dd97e30cee632123-Abstract-Datasets_and_Benchmarks.html | **1** | `2.3.1` (2.3.1.3, encaje con NSL-KDD), `3.5 Modelo de detección basado en firmas` (×2) — **recontado contra disco el 2026-08-16** |
| [43] | M. Sahami, S. Dumais, D. Heckerman y E. Horvitz, «A Bayesian Approach to Filtering Junk E-Mail», en *Learning for Text Categorization: Papers from the 1998 AAAI Workshop*, AAAI Technical Report WS-98-05, 1998, pp. 55-62 · ⚠️ **identidad inferida del contexto** | https://aaai.org/papers/055-ws98-05-009/ · https://cdn.aaai.org/Workshops/1998/WS-98-05/WS98-05-009.pdf | **1** | `2.3.2` (2.3.2.1, filtros bayesianos anti-spam) |
| [44] | ⚠️ **NO RECONSTRUIDA** — sostiene el párrafo «Apoyo al analista en el SOC» (triaje, agrupación de alertas y modelos de lenguaje como asistentes) en `2.3.2:38`. **No hay ninguna pista de autor en el texto ni fuente equivalente en `99 Investigación/`.** El propio texto declara el punto fuera de alcance. **Decide Francisco**: o se localiza una revisión de nivel 1 sobre automatización del triaje en SOC, o se retira el marcador y la frase se deja sin cita | — | — | `2.3.2` (2.3.2.1, SOC) |
| [45] | ⚠️ **NO RECONSTRUIDA — falta fijar la edición.** Informe de agencia europea de aplicación de la ley sobre IA y cibercrimen. Candidatos propuestos: Europol, *Internet Organised Crime Threat Assessment (IOCTA)* (edición por determinar); o Europol Innovation Lab, *ChatGPT: The impact of Large Language Models on Law Enforcement*, 2023. El callout de `2.3.2:109` ya declara que la edición debe fijarse antes del pase a Zotero. **Decide Francisco** | https://www.europol.europa.eu/publications-events/publications | — | `2.3.2` (2.3.2.3, descenso de la barrera de entrada) |
| [46] | C. Szegedy, W. Zaremba, I. Sutskever, J. Bruna, D. Erhan, I. Goodfellow y R. Fergus, «Intriguing properties of neural networks», en *2nd International Conference on Learning Representations (ICLR 2014)*, 2014 · ⚠️ **identidad inferida del contexto** | https://arxiv.org/abs/1312.6199 · 10.48550/arXiv.1312.6199 | **1** | `2.3.2` (2.3.2.4, evasión / ejemplos adversariales) |
| [47] | I. J. Goodfellow, J. Shlens y C. Szegedy, «Explaining and Harnessing Adversarial Examples», en *3rd International Conference on Learning Representations (ICLR 2015)*, 2015 · ⚠️ **identidad inferida del contexto** | https://arxiv.org/abs/1412.6572 · 10.48550/arXiv.1412.6572 | **1** | `2.3.2` (2.3.2.4, evasión / ejemplos adversariales) |
| [48] | B. Biggio y F. Roli, «Wild patterns: Ten years after the rise of adversarial machine learning», *Pattern Recognition*, vol. 84, pp. 317-331, dic. 2018 | 10.1016/j.patcog.2018.07.023 | **1** | `2.3.2` (2.3.2.4, evasión y envenenamiento) |
| [49] | A. Bendale y T. E. Boult, «Towards Open Set Deep Networks» (OpenMax), en *2016 IEEE Conference on Computer Vision and Pattern Recognition (CVPR)*, 2016, pp. 1563-1572 | 10.1109/CVPR.2016.173 | **1** | `2.3.2` (2.3.2.5, reconocimiento de conjunto abierto), `6.2 Líneas futuras` (6.2.2, *OpenMax* como sustituto del umbral) |
| [50] | N. Moustafa y J. Slay, «UNSW-NB15: a comprehensive data set for network intrusion detection systems (UNSW-NB15 network data set)», en *2015 Military Communications and Information Systems Conference (MilCIS)*, Canberra, 10-12 nov. 2015, IEEE, pp. 1-6 | 10.1109/MilCIS.2015.7348942 · https://research.unsw.edu.au/projects/unsw-nb15-dataset | **1** | `2.3.2` (tabla de datasets), `6.2 Líneas futuras` (UNSW-NB15 como alternativa con tiempo en origen) |
| [51] | I. Sharafaldin, A. Habibi Lashkari y A. A. Ghorbani, «Toward Generating a New Intrusion Detection Dataset and Intrusion Traffic Characterization», en *Proc. 4th International Conference on Information Systems Security and Privacy (ICISSP)*, Funchal, 22-24 ene. 2018, SciTePress, pp. 108-116 | 10.5220/0006639801080116 · https://www.unb.ca/cic/datasets/ids-2017.html | **1** | `2.3.2` (tabla de datasets, CIC-IDS2017/2018), `6.2 Líneas futuras` (peldaño 1: cinco días laborables y etiquetado con marca de tiempo) |
| [52] | F. Pierazzi, F. Pendlebury, J. Cortellazzi y L. Cavallaro, «Intriguing Properties of Adversarial ML Attacks in the Problem Space», en *2020 IEEE Symposium on Security and Privacy (S&P)*, 2020, pp. 1332-1349 · ⚠️ **identidad inferida del contexto** (el texto la describe como «la línea de trabajo sobre aprendizaje automático adversario en el espacio del problema») | 10.1109/SP40000.2020.00073 · preprint arXiv:1911.02142 | **1** | `2.3.3` (espacio de características frente a espacio del problema), `6.1 Conclusiones` (por qué el dataset impide el experimento adversario) — **recontado contra disco el 2026-08-16: la columna era CORRECTA, son esos dos usos y no hay más** |
| [53] | C. Rudin, «Stop explaining black box machine learning models for high stakes decisions and use interpretable models instead», *Nature Machine Intelligence*, vol. 1, n.º 5, pp. 206-215, 2019 | 10.1038/s42256-019-0048-x | **1** | `2.3.3` (interpretabilidad frente a explicación *a posteriori*) |
| [54] | C. Molnar, *Interpretable Machine Learning: A Guide for Making Black Box Models Explainable*. Edición del autor · ⚠️ **falta fijar la edición y el año**: la web oficial sirve hoy (consultada 2026-08-15) la **3.ª edición**; la más citada en la literatura es la 2.ª (2022) | https://christophm.github.io/interpretable-ml-book/ | **2** | `2.3.3` (sistematización del ML interpretable) | ⚠️ **NO PROCEDE todavía:** el capítulo y la página dependen de qué edición se cite, y la edición **no está fijada** (la web sirve hoy la 3.ª; la literatura cita la 2.ª de 2022, y su paginación no coincide). **Decide Francisco**, y solo después se fija el localizador. · **Nota del 2026-08-16 (Tanda 13):** `2.1.4.2.1` llevaba un marcador `[CITA: Molnar, cap. 8]` sobre Isolation Forest. **No se ha convertido a `[54]`**: la obra de Molnar no es la fuente del algoritmo, y la cita se ha reasignado a la primaria, `[73]` (Liu, Ting y Zhou, 2008), como pedía el callout de esa sección. Con ello **la edición sin fijar de Molnar ya no bloquea ningún localizador del capítulo 2**, solo el uso de `2.3.3` |
| [55] | Parlamento Europeo y Consejo de la Unión Europea, *Reglamento (UE) 2016/679, de 27 de abril de 2016, relativo a la protección de las personas físicas en lo que respecta al tratamiento de datos personales y a la libre circulación de estos datos (RGPD)*, DOUE L 119, 4 de mayo de 2016, pp. 1-88 | http://data.europa.eu/eli/reg/2016/679/oj | **1** | `2.3.3` (2.3.3.5, marco normativo) |
| [56] | Parlamento Europeo y Consejo de la Unión Europea, *Reglamento (UE) 2024/1689, de 13 de junio de 2024, por el que se establecen normas armonizadas en materia de inteligencia artificial (Reglamento de Inteligencia Artificial)*, DOUE serie L, 12 de julio de 2024 | http://data.europa.eu/eli/reg/2024/1689/oj | **1** | `2.3.3` (2.3.3.5, marco normativo) |
| [57] | Parlamento Europeo y Consejo de la Unión Europea, *Directiva (UE) 2022/2555, de 14 de diciembre de 2022, relativa a las medidas destinadas a garantizar un elevado nivel común de ciberseguridad en toda la Unión (Directiva SRI 2 / NIS2)*, DOUE L 333, 27 de diciembre de 2022, pp. 80-152 | http://data.europa.eu/eli/dir/2022/2555/oj | **1** | `2.3.3` (2.3.3.5, marco normativo) |
| [58] | *KDD Cup 1999 Data*, The UCI KDD Archive, Information and Computer Science, University of California, Irvine, 1999 (página modificada por última vez el 28 de octubre de 1999). Ficha oficial de la tarea de la competición: construir un modelo predictivo que distinga conexiones «malas» (intrusiones o ataques) de conexiones «buenas» normales | http://kdd.ics.uci.edu/databases/kddcup99/kddcup99.html | **1** | `4.2 Base de datos utilizada` (el KDD Cup 99 como banco de pruebas estándar y origen de los registros por conexión) | — (no es libro) |
| [59] | W. Lee y S. J. Stolfo, «A framework for constructing features and models for intrusion detection systems», *ACM Transactions on Information and System Security*, vol. 3, n.º 4, pp. 227-261, nov. 2000 | 10.1145/382912.382914 | **1** | `4.2 Base de datos utilizada` (construcción de características para detección de intrusiones y su correspondencia con el tipo de ataque) | — (no es libro) |
| [60] | M. Mitchell, S. Wu, A. Zaldivar, P. Barnes, L. Vasserman, B. Hutchinson, E. Spitzer, I. D. Raji y T. Gebru, «Model Cards for Model Reporting», en *Proc. Conference on Fairness, Accountability, and Transparency (FAT\* '19)*, Atlanta, GA, ACM, 2019, pp. 220-229 | 10.1145/3287560.3287596 | **1** | `5.0 Protocolo de evaluación` (evaluación desagregada por subgrupo), `A.3 Ficha del sistema` (plantilla de *model card*), `3.3 Metodología de funcionamiento del sistema` — **recontado contra disco el 2026-08-16** | — (no es libro) |
| [61] | W. J. Scheirer, A. de Rezende Rocha, A. Sapkota y T. E. Boult, «Toward Open Set Recognition», *IEEE Transactions on Pattern Analysis and Machine Intelligence*, vol. 35, n.º 7, pp. 1757-1772, jul. 2013 | 10.1109/TPAMI.2012.256 | **1** | `6.1 Conclusiones` (límite 5: el *riesgo de espacio abierto* que un umbral sobre un clasificador cerrado no acota), `3.3 Metodología de funcionamiento del sistema` — **recontado contra disco el 2026-08-16** | — (no es libro) |
| [62] | N. Erickson *et al.*, «TabArena: A Living Benchmark for Machine Learning on Tabular Data», en *Advances in Neural Information Processing Systems 38 (NeurIPS 2025)*, Datasets and Benchmarks Track, 2025 (*spotlight*) | https://papers.neurips.cc/paper_files/paper/2025/file/1697e3fb412da11dc9488249f9e7bbc9-Paper-Datasets_and_Benchmarks_Track.pdf · https://openreview.net/forum?id=jZqCqpCLdU · https://tabarena.ai | **1** | `6.2 Líneas futuras` (6.2.1, sobreajuste al conjunto de validación al elegir los miembros de un *ensemble*), `EL_FUTURO.md` | — (no es libro) |
| [63] | D. Micci-Barreca, «A preprocessing scheme for high-cardinality categorical attributes in classification and prediction problems», *ACM SIGKDD Explorations Newsletter*, vol. 3, n.º 1, pp. 27-32, jul. 2001 | 10.1145/507533.507538 | **1** | `6.2 Líneas futuras` (6.2.4, *target encoding* de categóricas de alta cardinalidad), `EL_FUTURO.md` | — (no es libro) |
| [64] | F. Pargent, F. Pfisterer, J. Thomas y B. Bischl, «Regularized target encoding outperforms traditional methods in supervised machine learning with high cardinality features», *Computational Statistics*, vol. 37, n.º 5, pp. 2671-2692, 2022 | 10.1007/s00180-022-01207-6 | **1** | `6.2 Líneas futuras` (6.2.4, evidencia comparativa del *target encoding* regularizado), `EL_FUTURO.md` | — (no es libro) |
| [65] | K. Hwang, M. Cai, Y. Chen y M. Qin, «Hybrid Intrusion Detection with Weighted Signature Generation over Anomalous Internet Episodes», *IEEE Transactions on Dependable and Secure Computing*, vol. 4, n.º 1, pp. 41-55, ene.-mar. 2007 | 10.1109/TDSC.2007.9 | **1** | `6.2 Líneas futuras` (6.2.5, H-IDS en bucle con generación de firmas ponderadas), `EL_FUTURO.md` | — (no es libro) |
| [66] | F. Pendlebury, F. Pierazzi, R. Jordaney, J. Kinder y L. Cavallaro, «TESSERACT: Eliminating Experimental Bias in Malware Classification across Space and Time», en *28th USENIX Security Symposium*, Santa Clara, CA, ago. 2019, USENIX Association, pp. 729-746 | https://www.usenix.org/conference/usenixsecurity19/presentation/pendlebury · https://www.usenix.org/system/files/sec19-pendlebury.pdf | **1** | `6.2 Líneas futuras` (peldaño 2: sesgo temporal, restricciones de diseño y métrica AUT) | — (no es libro) |
| [67] | A. Behrouz, M. Razaviyayn, P. Zhong y V. Mirrokni, «Nested Learning: The Illusion of Deep Learning Architectures», en *Advances in Neural Information Processing Systems 38 (NeurIPS 2025)*, 2025 | https://proceedings.neurips.cc/paper_files/paper/2025/hash/4309616aaed8e848009bc4a7ef73b493-Abstract-Conference.html · preprint arXiv:2512.24695 | **1** | `6.2 Líneas futuras` (peldaño 3, con localizador `[67, §4.5 y §9]`); respaldo interno en [[aprendizaje-continuo-nested-learning]] | `[67, §4.5]` (supuesto no i.i.d.) y `[67, §9]` (evaluación limitada a modelos de lenguaje) — **secciones**, no páginas: el artículo se cita por su versión de actas |
| [68] | S.-Y. Ji, B.-K. Jeong, S. Choi y D. H. Jeong, «A multi-level intrusion detection method for abnormal network behaviors», *Journal of Network and Computer Applications*, vol. 62, pp. 9-17, feb. 2016 · ⚠️ **solo resumen**: el texto completo está tras muro de pago (Elsevier) y el proyecto no tiene acceso institucional | 10.1016/j.jnca.2015.12.004 | **1** | `2.2.4 Detección por firmas frente a…` (cascada del mismo orden sobre NSL-KDD: reglas minadas → categorización del tipo de ataque); respaldo interno en [[arquitecturas-hibridas-en-la-literatura]] | — (no es libro) |
| [69] | G. Kim, S. Lee y S. Kim, «A novel hybrid intrusion detection method integrating anomaly detection with misuse detection», *Expert Systems with Applications*, vol. 41, n.º 4, pp. 1690-1700, mar. 2014 · ⚠️ **solo resumen**: texto completo tras muro de pago (Elsevier). La nota que la cita ya declara esa reserva en un callout propio y **no reproduce ninguna cifra** del trabajo | 10.1016/j.eswa.2013.08.066 | **1** | `2.2.4` (orden inverso sobre NSL-KDD: C4.5 → one-class SVM por subconjunto; **antagonista directo** del diseño del TFG); respaldo interno en [[arquitecturas-hibridas-en-la-literatura]] | — (no es libro) |
| [70] | A. Khraisat, I. Gondal, P. Vamplew, J. Kamruzzaman y A. Alazab, «Hybrid Intrusion Detection System Based on the Stacking Ensemble of C5 Decision Tree Classifier and One Class Support Vector Machine», *Electronics*, vol. 9, n.º 1, art. 173, 2020 · ⚠️ **solo resumen y metadatos**: MDPI devolvió 403 al texto completo durante la investigación. **Distinta de [31]** (Khraisat *et al.* 2019, el *survey*): no confundirlas | 10.3390/electronics9010173 | **1** | `2.2.4` (*stacking ensemble* como topología alternativa a la cascada); respaldo interno en [[arquitecturas-hibridas-en-la-literatura]] | — (no es libro) |
| [71] | R. Shwartz-Ziv y A. Armon, «Tabular data: Deep learning is not all you need», *Information Fusion*, vol. 81, pp. 84-90, 2022 (en línea desde jun. 2021) · ⚠️ **solo resumen**: texto completo tras muro de pago (Elsevier) | 10.1016/j.inffus.2021.11.011 | **1** | `3.5 Modelo de detección basado en firmas` (el *boosting* de gradiente supera a las arquitecturas profundas tabulares sobre sus propios conjuntos, con mucho menos ajuste); respaldo interno en [[clasificadores-tabulares-y-arquitecturas-hibridas]] | — (no es libro) |
| [72] | N. Hollmann, S. Müller, L. Purucker, A. Krishnakumar, M. Körfer, S. B. Hoo, R. T. Schirrmeister y F. Hutter, «Accurate predictions on small data with a tabular foundation model» (TabPFN v2), *Nature*, vol. 637, n.º 8045, pp. 319-326, ene. 2025 | 10.1038/s41586-024-08328-6 | **1** | `3.5` (límite de **10.000 muestras** de la v2 frente a las 58.630 filas de D3); respaldo interno en [[clasificadores-tabulares-y-arquitecturas-hibridas]] | — (no es libro) |
| [73] | F. T. Liu, K. M. Ting y Z.-H. Zhou, «Isolation Forest», en *2008 Eighth IEEE International Conference on Data Mining (ICDM)*, Pisa, dic. 2008, IEEE, pp. 413-422 · **fuente primaria del algoritmo**, verificada contra Crossref el 2026-08-16 | 10.1109/ICDM.2008.17 | **1** | `2.1.4 Algoritmos de ML` (2.1.4.2.1, ×2: árboles de aislamiento y longitud media del camino como puntuación de anomalía) | — (no es libro) |
| [74] | P. Goldschmidt y D. Chudá, «Network intrusion datasets: A survey, limitations, and recommendations», *Computers & Security*, vol. 156, art. 104510, 2025 · **revisión sistemática de 89 datasets públicos de NIDS**, analizados según 13 características · metadatos verificados contra Crossref y contra arXiv el 2026-08-16 | 10.1016/j.cose.2025.104510 · preprint arXiv:2502.06688 (v3, 22 may. 2025) | **1** | `4.2 Base de datos utilizada` (razón 4 de «Por qué se eligió NSL-KDD»: la partición train/test predefinida es menos frecuente de lo que parece); respaldo interno en [[benchmark-comparativo-nsl-kdd]] | **`[74, §5.5.4]`** («Other Observations») para el dato citado: *«Only 23% (16% since 2020) provide predefined train-test data splits. As mentioned, this design offers greater flexibility but is prone to biased evaluations and selective reporting»* — **verbatim, verificado en la versión HTML de arXiv el 2026-08-16**. La propiedad se define en **§4.5 «Evaluation»** (campo *Split*). ⚠️ **Corrección de atribución:** la nota y el informe interno colgaban ese 23 %/16 % de **§5.4** y del marco «congresos CORE A*/A, 2020-2023»; **es otra población**. §5.4 («Dataset Popularity») analiza **45 artículos** de conferencias Tier 1-2 y es de donde sale «NSL-KDD was used only three times»; el 23 %/16 % se mide sobre **los 89 datasets del *survey***, sin filtro de *venue* ni de año. No es libro: se cita por sección, no por página |
| [75] | M. M. Breunig, H.-P. Kriegel, R. T. Ng y J. Sander, «LOF: Identifying Density-Based Local Outliers», *ACM SIGMOD Record*, vol. 29, n.º 2, pp. 93-104, jun. 2000 · **fuente primaria del algoritmo**, metadatos verificados contra Crossref el 2026-08-16 | 10.1145/335191.335388 | **1** | `2.1.4 Algoritmos de ML` (2.1.4.2.3, Local Outlier Factor: densidad local frente a la de los vecinos más próximos). **Alta por reasignación aprobada por Francisco el 2026-08-16**: este uso citaba `[12]` Hastie, cuyo cap. 14 no trata LOF | — (no es libro) |

## Avisos y reservas por entrada

> [!warning] [9] — retirada de la numeración, fundida en [8]
> Era `students.aiu.edu/.../j5V2a3_Computer_Security_Principles.pdf`: **copia no autorizada del
> mismo libro de Stallings que ya es [8]**, alojada en un dominio de terceros, sin garantía de
> integridad → **nivel 3**. Comprobado el 2026-08-09: el enlace **ya ni siquiera resuelve en
> abierto** (302 a `aiu.edu/securelogin.html`), así que tampoco era una URL estable.
> **Su número no se reutiliza** para no romper los `[n]` de las notas.
> **✅ EJECUTADO — verificado contra disco el 2026-08-15:** `2.2.1 Introducción a la
> ciberseguridad.md:32` **ya cita `[8]`**, no `[9]`. El repunte está hecho y **no queda ninguna
> aparición de `[9]` en el vault**. (Esta nota decía «acción pendiente, NO ejecutada»; era texto
> caducado.)

> [!warning] [8] — edición sin confirmar
> El libro se citaba **sin autor completo, sin año y sin editorial**. Completado con los
> metadatos verificados de la 4.ª edición (Pearson, 2018, ISBN 978-0-13-479410-5), que es la más
> difundida. **Existe una 5.ª edición: Pearson, 2023, ISBN impreso 978-0-13-809167-5**
> (e-book 978-0-13-809171-2). La definición citada en `2.2.1` (la de *computer security* tomada
> del NIST) aparece en el capítulo 1 de **todas** las ediciones, así que el texto no permite
> deducir cuál se usó, y la copia de [9] ya no es accesible para comprobarlo.
> **Francisco debe confirmar la edición que tiene delante antes del pase a Zotero.**
> Coautor añadido: **Lawrie Brown**, que faltaba.

> [!note] [2] — nivel 2, y qué sostiene exactamente
> Es un **informe técnico de empresa** (James P. Anderson Co.), no una publicación revisada por
> pares: **nivel 2**. Se cita como **fuente primaria histórica** y la copia enlazada la aloja el
> **NIST CSRC**, lo que da garantía de integridad. Portada verificada el 2026-08-09: título,
> contrato 79F296400, 26-02-1980 y revisión de 15-04-1980.
> **Reserva:** la frase de `1.2 Preliminares` «este informe se considera el punto de partida para
> los IDS» es una afirmación *sobre* el informe, que el propio informe no puede sostener.
> Necesita un aval de nivel 1 (una revisión del área). **Propuesta, no ejecutada.**

> [!note] [1] — sustituida (baja autorizada el 2026-08-06)
> Antes era `channelpartner.es` (**prensa sectorial, nivel 3**) sosteniendo una cifra de
> ciberataques. Sustituida por la **nota de prensa oficial de INCIBE** sobre el *Balance de
> ciberseguridad 2024* (nivel 1), con el dato exacto ya recogido en la tabla.
> **Reserva importante:** INCIBE da la **magnitud del fenómeno**, no los **nombres propios**
> (Santander, Telefónica, Iberdrola, UCM) que aparecían en `1.1 Motivación:12`. Con esta fuente,
> la frase debía reformularse hacia la cifra agregada.
> **✅ EJECUTADO — verificado contra disco el 2026-08-15:** `1.1 Motivación:12` ya no nombra
> ninguna empresa; cita los **97.348 incidentes gestionados por INCIBE en 2024, un 16,6 % más que
> el año anterior**, que es exactamente lo que la fuente sostiene. (Esta nota decía «Propuesta, no
> ejecutada»; era texto caducado.)

> [!note] [10] — organismo oficial, URL con protección anti-bot
> Nivel 1 por emisor (Centro Criptológico Nacional). El 2026-08-09 la URL devuelve **403/503 a
> cualquier acceso automático** (`ccn-cert.cni.es` filtra herramientas), igual que el espejo
> docente de la UPM. **No es un enlace roto**: es verificable a mano desde un navegador.
> **Sin verificar:** la **versión y la fecha** de la guía. Antes del pase a Zotero conviene citar
> la guía completa («CCN-STIC-401 Glosario y Abreviaturas», con su versión) en lugar del
> enlace profundo al término, que es frágil.

> [!warning] [6] — posible atribución equivocada, detectada de paso
> En `2.1.2 Tipos de ML.md:30` y `:64` se atribuyen a **Goodfellow et al.** dos listas
> (k-NN / regresión lineal / SVM / árboles / redes neuronales, y K-Means / DBSCAN / HCA /
> One-class SVM / Isolation Forest / PCA / Kernel PCA / LLE / t-SNE / Apriori / **Eclat**). Esas
> listas son las del **capítulo 1 de Géron [5]**; *Deep Learning* no trata Eclat, Apriori ni
> Isolation Forest.
> **✅ EJECUTADO — verificado contra disco el 2026-08-15:** `2.1.2 Tipos de ML.md:30` y `:64`
> **ya citan `[5]`**. El repunte está hecho. (Esta nota decía «Propuesta, no ejecutada»; era texto
> caducado.)
> **Consecuencia que quedó abierta y HOY ESTÁ CERRADA:** con aquel repunte, `[6]` se quedó sin ningún
> sitio de cita en todo el vault. **T24 la reancló el 2026-08-15 (`296de24`):** `2.1.4.3` la cita con
> **`[6, cap. 6]`**, con **7 ocurrencias verificadas contra disco el 2026-08-16**. **`[6] ya NO está
> huérfana** y su fila lleva ya el localizador. Lo único que sigue sin establecerse de esa entrada es
> la **página exacta**, por falta de acceso al texto paginado.
