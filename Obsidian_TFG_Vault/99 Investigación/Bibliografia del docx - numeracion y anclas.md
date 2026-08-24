---
titulo: "Bibliografía del .docx: numeración desde [12] por orden de aparición en el Word"
numero: "-"
estado: informe
docx_ref: "Proyecto_Fin_de_Grado-FJLM-2026.docx"
---

# Bibliografía del `.docx`: numeración desde `[12]` y sitio exacto de cada marcador

- **Encargo:** producir la lista de bibliografía del `.docx` **a partir de `[12]` y en orden de aparición**, con el sitio exacto donde va cada marcador. `[1]`-`[11]` del Word quedan congelados. La renumeración afecta **solo al `.docx`**: el vault no se toca ni se renumera.
- **Fecha de esta versión:** 2026-08-24 (**tercera pasada, y la que vale**), con **dos cambios de esa misma fecha por instrucción de Francisco**: (1) **fuera todos los localizadores IEEE** de los marcadores del `.docx`, y (2) la tabla es ahora **autosuficiente** —trae el texto completo de cada referencia, sin necesidad de abrir `Bibliografía.md`— y el informe cierra con la **bibliografía completa `[1]`-`[75]`** lista para pegar (§9).
- **Alcance:** entra todo lo que **tiene sede real en el documento final**. Lo que no tiene sede **no recibe número** — §4.
- **Alimenta a:** [[Bibliografía]] · tareas **T1**, **T3**, **T4** y **B1**-**B4** de `Las tareas de Kiko.md`

> [!important] Cómo se ha establecido el orden en esta versión, y por qué las dos anteriores no valían
> El orden de esta tabla se ha fijado **leyendo el binario `Proyecto_Fin_de_Grado-FJLM-2026.docx` de principio a fin** (2.570 párrafos), y la posición de cada primera aparición se expresa en **número de párrafo del propio Word**.
>
> Las dos versiones anteriores de este informe construyeron la secuencia **recorriendo el vault** (`01` → `06` → Apéndices) y dieron por hecho que el Word seguía ese mismo orden. **No lo sigue**: el `.docx` es un volcado más recortado y con secciones movidas, así que la numeración salía con saltos y retrocesos al leer el documento entregable. Esa es la causa raíz de los dos rechazos.
>
> **Se retira también la declaración de verificación de la versión anterior**, que decía haberse contrastado contra `Resultados/docx/COMPARACION/docx_limpio.md`. Ese volcado **está desfasado** respecto al `.docx` vigente y ya no sirve como referencia. Todo lo de este informe sale del binario.

> [!note] Criterio de aceptación
> Leyendo el Word de arriba abajo, **la primera aparición** de cada obra sale `[12]`, `[13]`, `[14]`, `[15]`… sin saltos ni retrocesos.

> [!warning] Un número por OBRA — las repeticiones NO son un fallo de orden
> Una obra citada varias veces **conserva un solo número**: el de su **primera** aparición. Las apariciones posteriores **repiten ese mismo número**, aunque al leer seguido parezca que la secuencia «retrocede» (p. ej. en el párrafo 885 vuelve a salir `[12]` cuando alrededor ya se está en los `[40]`). **Eso es IEEE correcto y no hay que tocarlo.** Lo que debe ser creciente es la secuencia de **primeras apariciones**, no la de todas las apariciones.
>
> La columna «Otras apariciones» de la tabla lista esos párrafos. En exactamente **cuatro** casos —`[54]`, `[57]`, `[58]` y `[59]`— alguna de esas otras apariciones tiene número de párrafo **menor** que el de la columna «Párr.». Se dejan tal cual: **el número de la obra no cambia**.
>
> **Excepción declarada de la columna «Párr.» en `[57]`, `[58]` y `[59]`.** Las tres declaran 829, 832 y 837 —sus **celdas** en la tabla de librerías de §4.1.3— y registran además una mención en el **párrafo introductorio 820**, anterior. La columna recoge aquí la **sede donde va el marcador**, no la primera mención absoluta. No afecta a la secuencia: 820 sigue siendo mayor que 794, el párrafo de la obra inmediatamente anterior (`[55]`).

> [!note] Las dos numeraciones
> **`Nº .docx` ≠ `Nº vault`.** Son independientes y esta tabla es el puente. Al pegar el marcador en el Word se escribe **el número del `.docx`**; para localizar la referencia en `Bibliografía.md` se usa **el del vault**.

---

## Respuesta corta

El `.docx` necesita **75 números**: los **11 congelados** más **64 obras, de `[12]` a `[75]`**.

**20 obras del vault se quedan SIN número** porque su sede no existe en el `.docx` vigente (§4). El `[11]` del Word es **Snort/Roesch** (`[26]` del vault); el `[11]` del vault es **CRISP-DM** y **no llega al `.docx`** — con eso queda resuelta **T1**.

---

## 1 · Los `[1]`-`[11]` del `.docx`, congelados

Transcritos tal como están en el Word. No se corrigen aquí: **T3**, **B2** y **B3** son tareas de Word.

| `[n]` `.docx` | Tal como está escrito hoy en el Word | Equivalente en el vault | Estado |
|---|---|---|---|
| [1] | `https://www.channelpartner.es/seguridad/principales-ciberataques-en-espana-en-2024/` | `[1]` INCIBE, balance de ciberseguridad 2024 | ⚠️ **Desajuste de fuente, no de número.** El Word cita prensa sectorial (**nivel 3**); el vault sostiene el mismo dato con INCIBE (nivel 1). El número se congela; **la fuente debería sustituirse**. Decide Francisco |
| [2] | «Computer Security Threat Monitoring and Surveillance». James P. Anderson Co. | `[2]` Anderson (1980) | ✅ Misma obra. **B3**: falta el año (1980) |
| [3] | Denning, Dorothy E. (1987). «An Intrusion-Detection Model». *IEEE TSE*, SE-13(2), 222-232 | `[3]` Denning (1987) | ✅ Coincide, y con páginas |
| [4] | Chio, C., & Freeman, D. (2018) *Machine Learning & Security*. O'Reilly | `[4]` Chio y Freeman (2018) | ✅ Coincide |
| [5] | Geron, A. (2019). *Hands-On Machine Learning…* (2nd Ed.). O'Reilly | `[5]` Géron (2019) | ✅ Coincide |
| [6] | Goodfellow, I., Bengio, Y., & Courville, A. (2016). *Deep Learning*. MIT Press | `[6]` Goodfellow *et al.* (2016) | ✅ Coincide. **B4**: el `[6]` del vault se cita en la memoria con capítulo, y ese capítulo **no llegó al Word**. Irrelevante ya: en el `.docx` **no se ponen localizadores** (decisión del 2026-08-24) |
| [7] | Murphy, K. P. (2012). *Machine Learning: A Probabilistic Perspective*. MIT Press | `[7]` Murphy (2012) | ✅ Coincide |
| [8] | «Computer Security : Principles and Practice» William Stallings | `[8]` Stallings y Brown, **5.ª ed., Pearson, 2023** | ⚠️ **B3**: faltan año, edición, coautor y editorial |
| [9] | `https://students.aiu.edu/.../j5V2a3_Computer_Security_Principles.pdf` | **NINGUNO** — el `[9]` del vault está **QUEMADO** desde el 2026-08-09, precisamente por ser esta copia | ⛔ **Duplica a `[8]`** y es una copia no autorizada (nivel 3). **B2**: fusionarla en `[8]`. **Si Francisco la elimina, el `[9]` del `.docx` queda quemado y NO se renumera** |
| [10] | `https://www.ccn-cert.cni.es/.../401-glosario_abreviaturas/…` | `[10]` CCN-STIC-401, *Glosario y Abreviaturas* | ✅ Misma fuente. **B2**: URL desnuda |
| [11] | `https://www.usenix.org/legacy/publications/library/proceedings/lisa99/roesch.html` | **`[26]`** Roesch, «Snort», LISA'99, pp. 229-238 | ⚠️ **ESTE ERA EL DESAJUSTE DE T1, Y QUEDA RESUELTO ASÍ:** `[11]` `.docx` = `[26]` vault. **El `[11]` del vault es CRISP-DM y NO va aquí** — ver §4. **B2**: URL desnuda |

---

## 2 · Tabla principal — orden de aparición **en el Word**

Una fila por obra. **«Párr.»** es el número de párrafo del `.docx` donde aparece **por primera vez**; la columna manda sobre cualquier otra consideración y es estrictamente creciente.

**Ancla:** el fragmento literal para Ctrl+F. **Las anclas se conservan intactas** respecto a la versión anterior: lo que ha cambiado es el número, nunca la sede.

> [!important] Los localizadores IEEE quedan DEROGADOS en el `.docx` — decisión de Francisco del 2026-08-24
> En el Word **todos los marcadores se pegan como `[n]` a secas**: nunca el número seguido de coma y
> una página, un capítulo o una sección. Esto **deroga para el `.docx`** la exigencia de localizador en los 9 libros largos
> establecida el 2026-08-15. **El vault no cambia:** allí los localizadores siguen puestos donde
> estaban.
>
> La última columna de la tabla ya **no es un marcador que haya que pegar**: conserva, a título
> informativo, el capítulo o sección que el vault documenta para ese uso, más las reservas de
> verificación que no deben perderse. `—` = no había localizador; **⚠️ = el vault no pudo
> establecerlo** y no se inventó.

| Nº `.docx` | Nº vault | Obra | Párr. | Sección | Ancla literal (Ctrl+F) | Otras apariciones (párr.) | Localizador del vault (**informativo, NO se pega**) |
|---|---|---|---|---|---|---|---|
| **[12]** | [31] | Khraisat *et al.*, survey de IDS (2019) | 234 | 1.1 | «Se han creado algoritmos basados tanto en Machine Learning (ML) como en IA» | 885, 2044, 2116 | — |
| **[13]** | [77] | Hindy *et al.*, zero-day con DL (2020) | 236 | 1.1 | «estos algoritmos han sido fundamentales para la detección de ataques desconocidos» | 1978 | — · ⚠️ se cita **por el método**, no por su 89-99 % |
| **[14]** | [25] | Scarfone y Mell, NIST SP 800-94 (2007) | 248 | 1.2 | «…el de detección basada en el estado» | 501, 503, 524, 535, 570, 1436, 1438, 1999, 2032 | — |
| **[15]** | [39] | Russell y Norvig, *AIMA* (2021) | 302 | 2.1.1 | «los investigadores han perseguido enseñar a las computadoras a razonar» | — | cap. 1 |
| **[16]** | [79] | Mitchell, *Machine Learning* (1997) | 304 | 2.1.1 | «algoritmos y procesos que «aprenden» en el sentido de que son capaces de generalizar datos» | — | cap. 1 · ⚠️ página no establecida |
| **[17]** | [12] | Hastie, Tibshirani y Friedman, *ESL* (2009) | 328 | 2.1.3 | «se limpian, transforman y dividen en subconjuntos de entrenamiento, validación y prueba» | 364, 375, 377, 379, 382, 408, 1671 | caps. 7 · 14 · 15, según uso |
| **[18]** | [80] | Jolliffe, *Principal Component Analysis* (2002) | 344 | 2.1.2 | «Reducción de dimensionalidad y visualización» | — | cap. 1 · ⚠️ página no establecida |
| **[19]** | [81] | Agrawal y Srikant, reglas de asociación (1994) | 345 | 2.1.2 | «Reglas de asociación, que busca encontrar coocurrencias frecuentes» | — | — |
| **[20]** | [82] | Sutton y Barto, *Reinforcement Learning* (2018) | 349 | 2.1.2 | «Un agente aprende por interacción con un entorno, guiado por recompensas y penalizaciones» | — | cap. 1 · ⚠️ página no establecida |
| **[21]** | [13] | Kohavi, validación cruzada y bootstrap (1995) | 366 | 2.1.3 | «los valores que el algoritmo no aprende de los datos— mediante validación cruzada» | — | — |
| **[22]** | [83] | Breiman *et al.*, CART (1984) | 375 | 2.1.4 | «Un árbol de decisión es una estructura jerárquica de nodos de decisión» | — | ⚠️ **no establecido** (ni capítulo ni página) |
| **[23]** | [84] | Dietterich, *Ensemble Methods* (2000) | 377 | 2.1.4 | «Un conjunto (ensemble) combina varios clasificadores individuales» | — | — |
| **[24]** | [85] | Breiman, *Random Forests* (2001) | 379 | 2.1.4 | «El muestreo aleatorio decorrelaciona los árboles individuales y reduce la varianza» | 782, 1105 | — |
| **[25]** | [86] | Friedman, gradient boosting (2001) | 382 | 2.1.4 | «cada árbol nuevo se entrena para corregir los errores residuales del conjunto acumulado» | — | — |
| **[26]** | [87] | Ke *et al.*, LightGBM (2017) | 383 | 2.1.4 | «discretizando las características continuas en un número fijo de contenedores» | — | — |
| **[27]** | [88] | Cover y Hart, vecino más cercano (1967) | 385 | 2.1.4 | «el ejemplo más conocido de aprendizaje perezoso» | — | — |
| **[28]** | [30] | Chandola, Banerjee y Kumar, *Anomaly detection* (2009) | 389 | 2.1.4 | «Estos algoritmos se denominan semisupervisados (one-class)» | 530 | — |
| **[29]** | [73] | Liu, Ting y Zhou, *Isolation Forest* (2008) | 392 | 2.1.4 | «La longitud media del camino de aislamiento a través del conjunto de árboles» | 393, 749 | — |
| **[30]** | [89] | Schölkopf *et al.*, One-Class SVM (2001) | 395 | 2.1.4 | «busca la frontera —en el espacio transformado por un núcleo (kernel), típicamente el radial (RBF)—» | 752 | — |
| **[31]** | [75] | Breunig *et al.*, LOF (2000) | 398 | 2.1.4 | «recibe una puntuación LOF elevada y se considera anómalo» | 755 | — |
| **[32]** | [90] | Rumelhart, Hinton y Williams, retropropagación (1986) | 402 | 2.1.4 | «calculando los gradientes de todos los pesos mediante retropropagación» | — | — |
| **[33]** | [91] | Fawcett, análisis ROC (2006) | 412 | 2.1.5 | «La matriz de confusión es el punto de partida de toda métrica de clasificación» | 464 | — |
| **[34]** | [93] | Powers, *Evaluation…* (2011) | 423 | 2.1.5 | «Precisión: De todas las veces que el sistema levantó una alarma de ataque» | 427 («Exhaustividad (recall): de todos los ataques reales…») | — · ⚠️ **NIVEL 2** — ver §6 |
| **[35]** | [92] | Sokolova y Lapalme, medidas de rendimiento (2009) | 436 | 2.1.5 | «la matriz pasa a ser de k x k, con k el número de clases» | 446, 447 | — |
| **[36]** | [94] | van Rijsbergen, *Information Retrieval* (1979) | 440 | 2.1.5 | «F1: la media armónica de precisión y recall» | — | ⚠️ **no establecido**; la medida E/F está en el cap. 7, pero la copia abierta no conserva la paginación original |
| **[37]** | [19] | He y Garcia, *Learning from Imbalanced Data* (2009) | 459 | 2.1.5 | «un weighted alto, porque el peso n_i de la clase mayoritaria domina la suma» | 1300, 2071 | — |
| **[38]** | [95] | Davis y Goadrich, PR vs ROC (2006) | 469 | 2.1.5 | «Enfrenta la precisión frente al recall en cada umbral, con su propia área bajo la curva» | 470 | — |
| **[39]** | [96] | Axelsson, *IDS: A Survey and Taxonomy* (2000) | 521 | 2.2.3 | «La literatura no usa una taxonomía única sino varios ejes ortogonales» | — | — · ⚠️ **nivel 2**, y **no confundir con `[73]`** |
| **[40]** | [29] | García-Teodoro *et al.*, anomaly-based NIDS (2009) | 528 | 2.2.3 | «Es la taxonomía más citada del área y la que enmarca el problema de este TFG» | 530, 546, 2067 | — |
| **[41]** | [21] | Sommer y Paxson, *Outside the Closed World* (2010) | 554 | 2.2.3 | «mayor tasa de falsos positivos, alertas menos explicables y sensibilidad a la deriva (drift)» | 626, 820, 862, 2037 | — |
| **[42]** | [33] | Tombini *et al.*, combinación serial (2004) | 568 | 2.2.3 | «existen trabajos que la adoptan, la invierten y la reformulan como conjunto paralelo» | — | — |
| **[43]** | [97] | Lippmann *et al.*, DARPA 1998 (2000) | 571 | 2.2.5 | «procede de las campañas de evaluación… del MIT Lincoln Laboratory para DARPA (1998)» | 862 | — |
| **[44]** | [23] | Tavallaee *et al.*, análisis de KDD CUP 99 (2009) | 573 | 2.2.5 | «los 39 tipos de ataque específicos presentes en el corpus» | 670, 732, 864, 866, 873, 885, 1432, 1441, 1611, 1914, 1931, 2070 | §I para el «~99 %»; §V para `#successfulPrediction` |
| **[45]** | [36] | Kendall, base de datos de ataques (1999) | 577 | 2.2.5 | «Ejemplos en el dataset: neptune (inundación de segmentos SYN)…» | 581, 586, 591, 967, 990, 995, 1361 | — · ⚠️ identidad inferida |
| **[46]** | [59] | Lee y Stolfo, features y modelos para IDS (2000) | 578 | 2.2.5 · también 4.2 y A.1 | «Huella en el tráfico» | 582, 587, 593, 875, 879 | — |
| **[47]** | [98] | LeCun, Bengio y Hinton, *Deep learning* (2015) | 606 | 2.3.1 | «se habla de DL cuando la jerarquía de capas es lo bastante honda» | — | — |
| **[48]** | [61] | Scheirer *et al.*, *Toward Open Set Recognition* (2013) | 624 | 2.3.2 | «no produce «ninguna de las anteriores»: produce la categoría conocida más parecida» | 1835, 2072, 2111, 2225 | — |
| **[49]** | [18] | Arp *et al.*, *Dos and Don'ts of ML in Computer Security* (2022) | 631 | 2.3.2 | «"each paper suffers from at least three pitfalls"» — **cita textual hoy SIN marcador (tarea 2.8)** | 634, 643, 684, 737, 1435, 1436, 1443, 1929, 2077, 2093, 2100, 2120, 2273 | §III catálogo de pitfalls; §II cita textual. ⚠️ página exacta no establecida |
| **[50]** | [48] | Biggio y Roli, *Wild patterns* (2018) | 657 | 2.3.2 | «equivale a suponer un adversario que no modifica su comportamiento» | — | — |
| **[51]** | [52] | Pierazzi *et al.*, adversarial en el espacio del problema (2020) | 699 | **3.1.5 «Modelo de amenaza»** | «produce puntos que ningún atacante real podría generar» | 2101 | — · ⚠️ identidad inferida |
| **[52]** | [17] | Kapoor y Narayanan, *Leakage and the reproducibility crisis* (2023) | 733 | 3.3 | «se ajustan únicamente sobre el tráfico de entrenamiento (D1+D3)» | 1038, 1438, 1441 | — · ⚠️ identidad inferida |
| **[53]** | [99] | Chen y Guestrin, XGBoost (2016) | 788 | 3.5.2 | «Conjunto por boosting (rendimiento tipo XGBoost)» | — | — |
| **[54]** | [54] | Molnar, *Interpretable Machine Learning* (2022) | **791** | **3.5.3 «Firmas interpretables»** | «del árbol de decisión se extraen reglas legibles (mediante export_text)» | 1354 | ⚠️ **capítulo no establecido**; la edición sí (2.ª, 2022) |
| **[55]** | [100] | Chawla *et al.*, SMOTE (2002) | 794 | 3.5.4 | «Comparar el sobremuestreo sintético (SMOTE) frente al reponderado de clases» | 1038 | — |
| **[56]** | [16] | Chow, *error/reject tradeoff* (1970) | **800** | **3.5.5** | «estimadas fuera de muestra (out-of-fold, mediante validación cruzada sobre D3)» | — | — |
| **[57]** | [106] | Harris *et al.*, NumPy (2020) | 829 | 4.1.3 | fila «NumPy» de la tabla de librerías | 820 | — |
| **[58]** | [107] | McKinney, pandas (2010) | 832 | 4.1.3 | fila «Pandas» | 820 | — |
| **[59]** | [101] | Pedregosa *et al.*, scikit-learn (2011) | 837 | 4.1.3 | «Núcleo de ML: preprocesamiento (MinMaxScaler, LabelEncoder)» | 820 | — |
| **[60]** | [102] | Lemaître, Nogueira y Aridas, imbalanced-learn (2017) | 840 | 4.1.3 | «Tratamiento del desbalance de clases: SMOTE dentro de un Pipeline» | — | — |
| **[61]** | [103] | Massey, test de Kolmogórov-Smirnov (1951) | 843 | 4.1.3 | «test de Kolmogórov-Smirnov para el análisis de drift» | 944, 1021, 2052, 2090, 2307 | — |
| **[62]** | [104] | Hunter, Matplotlib (2007) | 844 | 4.1.3 | fila «Matplotlib» | 846 | — |
| **[63]** | [105] | Waskom, seaborn (2021) | 847 | 4.1.3 | fila «Seaborn» | 849 | — |
| **[64]** | [58] | *KDD Cup 1999 Data*, UCI KDD Archive | 862 | 4.2 | **sustituye el placeholder entero** `[enlace bibliografía: KDD Cup 99]` (junto a `[43]`) | — | — |
| **[65]** | [22] | McHugh, crítica a las evaluaciones DARPA (2000) | 864 | 4.2 | **sustituye** `[ enlace bibliografía: McHugh 2000]` | — | — · ⚠️ **MATCH APROXIMADO** (§5.3) |
| **[66]** | [14] | scikit-learn, documentación oficial de la API | 1260 | 4.4 | «LocalOutlierFactor se instancia con novelty=True» | — | — · ⚠️ la sede pide la página de `LocalOutlierFactor`, no la de `GridSearchCV`: fijarla en Zotero |
| **[67]** | [108] | Sakurada y Yairi, autoencoders para anomalías (2014) | 1261 | 4.4 | «las conexiones anómalas se reconstruyen mal y producen un MSE alto» | — | — |
| **[68]** | [20] | Pineau *et al.*, reproducibilidad en ML (2021) | 1434 | 5 (protocolo) | ⛔ **SIN ANCLA LITERAL** — el Anexo C de Kiko no tiene entrada para esta obra. **No se puede pegar hasta establecerla; no se inventa aquí** | 1999, 2096, 2106 | — |
| **[69]** | [109] | Demšar, comparación estadística de clasificadores (2006) | 1704 | 5.2.4 | «Comparación pareada (semilla a semilla)» | — | — |
| **[70]** | [110] | Dietterich, tests estadísticos aproximados (1998) | 1704 | 5.2.4 | mismo fragmento; **complementa a `[69]`**, no lo sustituye | — | — |
| **[71]** | [49] | Bendale y Boult, OpenMax (2016) | 1837 | 5.3 | «el clasificador de firmas, cerrado, tiende a asignar con confianza etiquetas conocidas» | 2225, 2228 | — |
| **[72]** | [74] | Goldschmidt y Chudá, survey de datasets NIDS (2025) | 1970 | 5.4 | completa `[CITA: Tavallaee 2009 + survey de datasets NIDS]` | 1972, 1975 | §5.5.4 y §5.4, según uso |
| **[73]** | [24] | Axelsson, *base-rate fallacy* (2000) | 1999 | 5.4 | ancla de la falacia de la tasa base | 2024, 2032 | — · ⚠️ **es el OTRO Axelsson**: no es `[39]` |
| **[74]** | [51] | Sharafaldin *et al.*, CIC-IDS2017 (2018) | 2298 | **6.2 Líneas futuras** | ancla del dataset CIC-IDS2017 | 2300, 2301 | — |
| **[75]** | [50] | Moustafa y Slay, UNSW-NB15 (2015) | 2300 | **6.2 Líneas futuras** | ancla del dataset UNSW-NB15 | — | — · ⚠️ **MATCH APROXIMADO** (§5.3) |

---

## 3 · Tabla de trabajo AUTOSUFICIENTE: número · referencia · ancla · párrafo

> [!important] Esta tabla se usa SIN abrir ningún otro fichero
> Cada fila trae la **referencia completa**, el **fragmento literal para Ctrl+F** y el **párrafo del
> Word**. El `Nº vault` es una **columna auxiliar** para volver a `Bibliografía.md` si hace falta el
> DOI: **no es la vía para identificar la obra**, que se lee aquí mismo.
>
> **Los marcadores se pegan como `[n]` a secas.** Sin localizador (decisión del 2026-08-24).
>
> `[1]`-`[11]` **no se tocan**: van tal como están hoy en el Word, con las correcciones de **B2** y
> **B3** si Francisco las hace. Su texto está en §1 y también en la lista completa de §9.

| `[n]` | Referencia completa | Ancla literal (Ctrl+F) | Párr. | Nº vault |
|---|---|---|---|---|
| **[12]** | A. Khraisat, I. Gondal, P. Vamplew y J. Kamruzzaman, «Survey of intrusion detection systems: techniques, datasets and challenges», *Cybersecurity*, vol. 2, art. 20, 2019 | «Se han creado algoritmos basados tanto en Machine Learning (ML) como en IA» | 234 | [31] |
| **[13]** | H. Hindy, R. Atkinson, C. Tachtatzis, J.-N. Colin, E. Bayne y X. Bellekens, «Utilising Deep Learning Techniques for Effective Zero-Day Attack Detection», *Electronics*, vol. 9, n.º 10, art. 1684, 2020 | «estos algoritmos han sido fundamentales para la detección de ataques desconocidos» | 236 | [77] |
| **[14]** | K. Scarfone y P. Mell, *Guide to Intrusion Detection and Prevention Systems (IDPS)*, NIST Special Publication 800-94. Gaithersburg, MD: NIST, feb. 2007 | «…el de detección basada en el estado» | 248 | [25] |
| **[15]** | S. J. Russell y P. Norvig, *Artificial Intelligence: A Modern Approach*, 4.ª ed. Hoboken, NJ: Pearson, 2021 | «los investigadores han perseguido enseñar a las computadoras a razonar» | 302 | [39] |
| **[16]** | T. M. Mitchell, *Machine Learning*. Nueva York: McGraw-Hill, 1997 | «algoritmos y procesos que «aprenden» en el sentido de que son capaces de generalizar datos» | 304 | [79] |
| **[17]** | T. Hastie, R. Tibshirani y J. Friedman, *The Elements of Statistical Learning: Data Mining, Inference, and Prediction*, 2.ª ed. Nueva York: Springer, 2009 | «se limpian, transforman y dividen en subconjuntos de entrenamiento, validación y prueba» | 328 | [12] |
| **[18]** | I. T. Jolliffe, *Principal Component Analysis*, 2.ª ed. Nueva York: Springer, 2002 | «Reducción de dimensionalidad y visualización» | 344 | [80] |
| **[19]** | R. Agrawal y R. Srikant, «Fast Algorithms for Mining Association Rules», en *Proc. 20th Int. Conf. on Very Large Data Bases (VLDB'94)*, Santiago de Chile, 1994, pp. 487-499 | «Reglas de asociación, que busca encontrar coocurrencias frecuentes» | 345 | [81] |
| **[20]** | R. S. Sutton y A. G. Barto, *Reinforcement Learning: An Introduction*, 2.ª ed. Cambridge, MA: MIT Press, 2018 | «Un agente aprende por interacción con un entorno, guiado por recompensas y penalizaciones» | 349 | [82] |
| **[21]** | R. Kohavi, «A Study of Cross-Validation and Bootstrap for Accuracy Estimation and Model Selection», en *Proc. 14th IJCAI*, vol. 2, Morgan Kaufmann, 1995, pp. 1137-1143 | «los valores que el algoritmo no aprende de los datos— mediante validación cruzada» | 366 | [13] |
| **[22]** | L. Breiman, J. H. Friedman, R. A. Olshen y C. J. Stone, *Classification and Regression Trees*. Belmont, CA: Wadsworth, 1984 | «Un árbol de decisión es una estructura jerárquica de nodos de decisión» | 375 | [83] |
| **[23]** | T. G. Dietterich, «Ensemble Methods in Machine Learning», en *Multiple Classifier Systems (MCS 2000)*, LNCS vol. 1857, Springer, 2000, pp. 1-15 | «Un conjunto (ensemble) combina varios clasificadores individuales» | 377 | [84] |
| **[24]** | L. Breiman, «Random Forests», *Machine Learning*, vol. 45, n.º 1, pp. 5-32, 2001 | «El muestreo aleatorio decorrelaciona los árboles individuales y reduce la varianza» | 379 | [85] |
| **[25]** | J. H. Friedman, «Greedy function approximation: A gradient boosting machine», *The Annals of Statistics*, vol. 29, n.º 5, pp. 1189-1232, 2001 | «cada árbol nuevo se entrena para corregir los errores residuales del conjunto acumulado» | 382 | [86] |
| **[26]** | G. Ke, Q. Meng, T. Finley, T. Wang, W. Chen, W. Ma, Q. Ye y T.-Y. Liu, «LightGBM: A Highly Efficient Gradient Boosting Decision Tree», en *Advances in NIPS 30*, 2017, pp. 3146-3154 | «discretizando las características continuas en un número fijo de contenedores» | 383 | [87] |
| **[27]** | T. M. Cover y P. E. Hart, «Nearest neighbor pattern classification», *IEEE Trans. Information Theory*, vol. 13, n.º 1, pp. 21-27, 1967 | «el ejemplo más conocido de aprendizaje perezoso» | 385 | [88] |
| **[28]** | V. Chandola, A. Banerjee y V. Kumar, «Anomaly detection: A survey», *ACM Computing Surveys*, vol. 41, n.º 3, art. 15, pp. 1-58, 2009 | «Estos algoritmos se denominan semisupervisados (one-class)» | 389 | [30] |
| **[29]** | F. T. Liu, K. M. Ting y Z.-H. Zhou, «Isolation Forest», en *2008 Eighth IEEE Int. Conf. on Data Mining (ICDM)*, Pisa, 2008, pp. 413-422 | «La longitud media del camino de aislamiento a través del conjunto de árboles» | 392 | [73] |
| **[30]** | B. Schölkopf, J. C. Platt, J. Shawe-Taylor, A. J. Smola y R. C. Williamson, «Estimating the Support of a High-Dimensional Distribution», *Neural Computation*, vol. 13, n.º 7, pp. 1443-1471, 2001 | «busca la frontera —en el espacio transformado por un núcleo (kernel), típicamente el radial (RBF)—» | 395 | [89] |
| **[31]** | M. M. Breunig, H.-P. Kriegel, R. T. Ng y J. Sander, «LOF: Identifying Density-Based Local Outliers», *ACM SIGMOD Record*, vol. 29, n.º 2, pp. 93-104, 2000 | «recibe una puntuación LOF elevada y se considera anómalo» | 398 | [75] |
| **[32]** | D. E. Rumelhart, G. E. Hinton y R. J. Williams, «Learning representations by back-propagating errors», *Nature*, vol. 323, n.º 6088, pp. 533-536, 1986 | «calculando los gradientes de todos los pesos mediante retropropagación» | 402 | [90] |
| **[33]** | T. Fawcett, «An introduction to ROC analysis», *Pattern Recognition Letters*, vol. 27, n.º 8, pp. 861-874, 2006 | «La matriz de confusión es el punto de partida de toda métrica de clasificación» | 412 | [91] |
| **[34]** | D. M. W. Powers, «Evaluation: From Precision, Recall and F-Measure to ROC, Informedness, Markedness & Correlation», *Journal of Machine Learning Technologies*, vol. 2, n.º 1, pp. 37-63, 2011 | «Precisión: De todas las veces que el sistema levantó una alarma de ataque» | 423 | [93] |
| **[35]** | M. Sokolova y G. Lapalme, «A systematic analysis of performance measures for classification tasks», *Information Processing & Management*, vol. 45, n.º 4, pp. 427-437, 2009 | «la matriz pasa a ser de k x k, con k el número de clases» | 436 | [92] |
| **[36]** | C. J. van Rijsbergen, *Information Retrieval*, 2.ª ed. Londres: Butterworths, 1979 | «F1: la media armónica de precisión y recall» | 440 | [94] |
| **[37]** | H. He y E. A. Garcia, «Learning from Imbalanced Data», *IEEE Trans. Knowledge and Data Engineering*, vol. 21, n.º 9, pp. 1263-1284, 2009 | «un weighted alto, porque el peso n_i de la clase mayoritaria domina la suma» | 459 | [19] |
| **[38]** | J. Davis y M. Goadrich, «The relationship between Precision-Recall and ROC curves», en *Proc. 23rd Int. Conf. on Machine Learning (ICML'06)*, ACM, 2006, pp. 233-240 | «Enfrenta la precisión frente al recall en cada umbral, con su propia área bajo la curva» | 469 | [95] |
| **[39]** | S. Axelsson, *Intrusion Detection Systems: A Survey and Taxonomy*, informe técnico 99-15. Göteborg: Chalmers University of Technology, mar. 2000 | «La literatura no usa una taxonomía única sino varios ejes ortogonales» | 521 | [96] |
| **[40]** | P. García-Teodoro, J. Díaz-Verdejo, G. Maciá-Fernández y E. Vázquez, «Anomaly-based network intrusion detection: Techniques, systems and challenges», *Computers & Security*, vol. 28, n.º 1-2, pp. 18-28, 2009 | «Es la taxonomía más citada del área y la que enmarca el problema de este TFG» | 528 | [29] |
| **[41]** | R. Sommer y V. Paxson, «Outside the Closed World: On Using Machine Learning for Network Intrusion Detection», en *2010 IEEE Symp. on Security and Privacy*, Oakland, CA, 2010, pp. 305-316 | «mayor tasa de falsos positivos, alertas menos explicables y sensibilidad a la deriva (drift)» | 554 | [21] |
| **[42]** | E. Tombini, H. Debar, L. Mé y M. Ducassé, «A serial combination of anomaly and misuse IDSes applied to HTTP traffic», en *20th Annual Computer Security Applications Conf. (ACSAC)*, IEEE, 2004, pp. 428-437 | «existen trabajos que la adoptan, la invierten y la reformulan como conjunto paralelo» | 568 | [33] |
| **[43]** | R. Lippmann, J. W. Haines, D. J. Fried, J. Korba y K. Das, «Evaluating intrusion detection systems: the 1998 DARPA off-line intrusion detection evaluation», en *Proc. DISCEX'00*, vol. 2, IEEE, 2000, pp. 12-26 | «procede de las campañas de evaluación… del MIT Lincoln Laboratory para DARPA (1998)» | 571 | [97] |
| **[44]** | M. Tavallaee, E. Bagheri, W. Lu y A. A. Ghorbani, «A Detailed Analysis of the KDD CUP 99 Data Set», en *Proc. 2nd IEEE Symp. on Computational Intelligence for Security and Defense Applications (CISDA)*, Ottawa, 2009, pp. 1-6 | «los 39 tipos de ataque específicos presentes en el corpus» | 573 | [23] |
| **[45]** | K. Kendall, *A Database of Computer Attacks for the Evaluation of Intrusion Detection Systems*, tesis de máster, Massachusetts Institute of Technology, jun. 1999 | «Ejemplos en el dataset: neptune (inundación de segmentos SYN)…» | 577 | [36] |
| **[46]** | W. Lee y S. J. Stolfo, «A framework for constructing features and models for intrusion detection systems», *ACM Trans. Information and System Security*, vol. 3, n.º 4, pp. 227-261, 2000 | «Huella en el tráfico» | 578 | [59] |
| **[47]** | Y. LeCun, Y. Bengio y G. Hinton, «Deep learning», *Nature*, vol. 521, n.º 7553, pp. 436-444, 2015 | «se habla de DL cuando la jerarquía de capas es lo bastante honda» | 606 | [98] |
| **[48]** | W. J. Scheirer, A. de Rezende Rocha, A. Sapkota y T. E. Boult, «Toward Open Set Recognition», *IEEE Trans. Pattern Analysis and Machine Intelligence*, vol. 35, n.º 7, pp. 1757-1772, 2013 | «no produce «ninguna de las anteriores»: produce la categoría conocida más parecida» | 624 | [61] |
| **[49]** | D. Arp, E. Quiring, F. Pendlebury, A. Warnecke, F. Pierazzi, C. Wressnegger, L. Cavallaro y K. Rieck, «Dos and Don'ts of Machine Learning in Computer Security», en *31st USENIX Security Symposium*, 2022, pp. 3971-3988 | «"each paper suffers from at least three pitfalls"» — **cita textual hoy SIN marcador (tarea 2.8)** | 631 | [18] |
| **[50]** | B. Biggio y F. Roli, «Wild patterns: Ten years after the rise of adversarial machine learning», *Pattern Recognition*, vol. 84, pp. 317-331, 2018 | «equivale a suponer un adversario que no modifica su comportamiento» | 657 | [48] |
| **[51]** | F. Pierazzi, F. Pendlebury, J. Cortellazzi y L. Cavallaro, «Intriguing Properties of Adversarial ML Attacks in the Problem Space», en *2020 IEEE Symp. on Security and Privacy*, 2020, pp. 1332-1349 | «produce puntos que ningún atacante real podría generar» | 699 | [52] |
| **[52]** | S. Kapoor y A. Narayanan, «Leakage and the reproducibility crisis in machine-learning-based science», *Patterns*, vol. 4, n.º 9, art. 100804, 2023 | «se ajustan únicamente sobre el tráfico de entrenamiento (D1+D3)» | 733 | [17] |
| **[53]** | T. Chen y C. Guestrin, «XGBoost: A Scalable Tree Boosting System», en *Proc. 22nd ACM SIGKDD Int. Conf. on Knowledge Discovery and Data Mining (KDD'16)*, ACM, 2016, pp. 785-794 | «Conjunto por boosting (rendimiento tipo XGBoost)» | 788 | [99] |
| **[54]** | C. Molnar, *Interpretable Machine Learning: A Guide for Making Black Box Models Explainable*, 2.ª ed. Edición del autor, 2022 | «del árbol de decisión se extraen reglas legibles (mediante export_text)» | 791 | [54] |
| **[55]** | N. V. Chawla, K. W. Bowyer, L. O. Hall y W. P. Kegelmeyer, «SMOTE: Synthetic Minority Over-sampling Technique», *Journal of Artificial Intelligence Research*, vol. 16, pp. 321-357, 2002 | «Comparar el sobremuestreo sintético (SMOTE) frente al reponderado de clases» | 794 | [100] |
| **[56]** | C. K. Chow, «On optimum recognition error and reject tradeoff», *IEEE Trans. Information Theory*, vol. 16, n.º 1, pp. 41-46, 1970 | «estimadas fuera de muestra (out-of-fold, mediante validación cruzada sobre D3)» | 800 | [16] |
| **[57]** | C. R. Harris, K. J. Millman, S. J. van der Walt *et al.*, «Array programming with NumPy», *Nature*, vol. 585, n.º 7825, pp. 357-362, 2020 | fila «NumPy» de la tabla de librerías | 829 | [106] |
| **[58]** | W. McKinney, «Data Structures for Statistical Computing in Python», en *Proc. 9th Python in Science Conf. (SciPy 2010)*, Austin, TX, 2010, pp. 56-61 | fila «Pandas» | 832 | [107] |
| **[59]** | F. Pedregosa, G. Varoquaux, A. Gramfort, V. Michel, B. Thirion, O. Grisel *et al.*, «Scikit-learn: Machine Learning in Python», *Journal of Machine Learning Research*, vol. 12, pp. 2825-2830, 2011 | «Núcleo de ML: preprocesamiento (MinMaxScaler, LabelEncoder)» | 837 | [101] |
| **[60]** | G. Lemaître, F. Nogueira y C. K. Aridas, «Imbalanced-learn: A Python Toolbox to Tackle the Curse of Imbalanced Datasets in Machine Learning», *Journal of Machine Learning Research*, vol. 18, n.º 17, pp. 1-5, 2017 | «Tratamiento del desbalance de clases: SMOTE dentro de un Pipeline» | 840 | [102] |
| **[61]** | F. J. Massey Jr., «The Kolmogorov-Smirnov Test for Goodness of Fit», *Journal of the American Statistical Association*, vol. 46, n.º 253, pp. 68-78, 1951 | «test de Kolmogórov-Smirnov para el análisis de drift» | 843 | [103] |
| **[62]** | J. D. Hunter, «Matplotlib: A 2D Graphics Environment», *Computing in Science & Engineering*, vol. 9, n.º 3, pp. 90-95, 2007 | fila «Matplotlib» | 844 | [104] |
| **[63]** | M. L. Waskom, «seaborn: statistical data visualization», *Journal of Open Source Software*, vol. 6, n.º 60, art. 3021, 2021 | fila «Seaborn» | 847 | [105] |
| **[64]** | *KDD Cup 1999 Data*, The UCI KDD Archive, Information and Computer Science, University of California, Irvine, 1999. Disponible en: http://kdd.ics.uci.edu/databases/kddcup99/kddcup99.html | **sustituye el placeholder entero** `[enlace bibliografía: KDD Cup 99]` (junto a `[43]`) | 862 | [58] |
| **[65]** | J. McHugh, «Testing Intrusion Detection Systems: A Critique of the 1998 and 1999 DARPA Intrusion Detection System Evaluations as Performed by Lincoln Laboratory», *ACM Trans. Information and System Security*, vol. 3, n.º 4, pp. 262-294, 2000 | **sustituye** `[ enlace bibliografía: McHugh 2000]` — ⚠️ **sede INFERIDA por contenido, no literal** (§5.3) | 864 | [22] |
| **[66]** | scikit-learn, documentación oficial de la API (módulos `sklearn.model_selection` / `sklearn.neighbors`) · ⚠️ **REFERENCIA INCOMPLETA:** sin año ni fecha de consulta, y la URL del vault apunta a `GridSearchCV`, no a `LocalOutlierFactor`, que es lo que pide esta sede. Fijar en Zotero | «LocalOutlierFactor se instancia con novelty=True» | 1260 | [14] |
| **[67]** | M. Sakurada y T. Yairi, «Anomaly Detection Using Autoencoders with Nonlinear Dimensionality Reduction», en *Proc. MLSDA 2014 2nd Workshop on Machine Learning for Sensory Data Analysis*, ACM, 2014, pp. 4-11 | «las conexiones anómalas se reconstruyen mal y producen un MSE alto» | 1261 | [108] |
| **[68]** | J. Pineau, P. Vincent-Lamarre, K. Sinha, V. Larivière, A. Beygelzimer, F. d'Alché-Buc, E. Fox y H. Larochelle, «Improving Reproducibility in Machine Learning Research (A Report from the NeurIPS 2019 Reproducibility Program)», *Journal of Machine Learning Research*, vol. 22, n.º 164, pp. 1-20, 2021 | ⛔ **SIN ANCLA LITERAL** — el Anexo C de Kiko no tiene entrada para esta obra. **No se puede pegar hasta establecerla; no se inventa aquí** | 1434 | [20] |
| **[69]** | J. Demšar, «Statistical Comparisons of Classifiers over Multiple Data Sets», *Journal of Machine Learning Research*, vol. 7, pp. 1-30, 2006 | «Comparación pareada (semilla a semilla)» | 1704 | [109] |
| **[70]** | T. G. Dietterich, «Approximate Statistical Tests for Comparing Supervised Classification Learning Algorithms», *Neural Computation*, vol. 10, n.º 7, pp. 1895-1923, 1998 | mismo fragmento que `[69]`; **complementa, no sustituye** | 1704 | [110] |
| **[71]** | A. Bendale y T. E. Boult, «Towards Open Set Deep Networks», en *2016 IEEE Conf. on Computer Vision and Pattern Recognition (CVPR)*, 2016, pp. 1563-1572 | «el clasificador de firmas, cerrado, tiende a asignar con confianza etiquetas conocidas» | 1837 | [49] |
| **[72]** | P. Goldschmidt y D. Chudá, «Network intrusion datasets: A survey, limitations, and recommendations», *Computers & Security*, vol. 156, art. 104510, 2025 | completa `[CITA: Tavallaee 2009 + survey de datasets NIDS]` | 1970 | [74] |
| **[73]** | S. Axelsson, «The base-rate fallacy and the difficulty of intrusion detection», *ACM Trans. Information and System Security*, vol. 3, n.º 3, pp. 186-205, 2000 | ancla de la falacia de la tasa base — **es el OTRO Axelsson**: no es `[39]` | 1999 | [24] |
| **[74]** | I. Sharafaldin, A. Habibi Lashkari y A. A. Ghorbani, «Toward Generating a New Intrusion Detection Dataset and Intrusion Traffic Characterization», en *Proc. 4th Int. Conf. on Information Systems Security and Privacy (ICISSP)*, Funchal, 2018, pp. 108-116 | ancla del dataset CIC-IDS2017 | 2298 | [51] |
| **[75]** | N. Moustafa y J. Slay, «UNSW-NB15: a comprehensive data set for network intrusion detection systems», en *2015 Military Communications and Information Systems Conf. (MilCIS)*, Canberra, 2015, pp. 1-6 | ancla del dataset UNSW-NB15 — ⚠️ **sede INFERIDA por contenido, no literal** (§5.3) | 2300 | [50] |

### 3.1 · El mismo listado, en bloque, para pegado rápido

Solo los números y el texto. Las anclas y los párrafos están arriba.

```
[12]  A. Khraisat, I. Gondal, P. Vamplew y J. Kamruzzaman, «Survey of intrusion detection systems: techniques, datasets and challenges», Cybersecurity, vol. 2, art. 20, 2019.
[13]  H. Hindy, R. Atkinson, C. Tachtatzis, J.-N. Colin, E. Bayne y X. Bellekens, «Utilising Deep Learning Techniques for Effective Zero-Day Attack Detection», Electronics, vol. 9, n.º 10, art. 1684, 2020.
[14]  K. Scarfone y P. Mell, Guide to Intrusion Detection and Prevention Systems (IDPS), NIST Special Publication 800-94. Gaithersburg, MD: NIST, feb. 2007.
[15]  S. J. Russell y P. Norvig, Artificial Intelligence: A Modern Approach, 4.ª ed. Hoboken, NJ: Pearson, 2021.
[16]  T. M. Mitchell, Machine Learning. Nueva York: McGraw-Hill, 1997.
[17]  T. Hastie, R. Tibshirani y J. Friedman, The Elements of Statistical Learning: Data Mining, Inference, and Prediction, 2.ª ed. Nueva York: Springer, 2009.
[18]  I. T. Jolliffe, Principal Component Analysis, 2.ª ed. Nueva York: Springer, 2002.
[19]  R. Agrawal y R. Srikant, «Fast Algorithms for Mining Association Rules», en Proc. 20th Int. Conf. on Very Large Data Bases (VLDB'94), Santiago de Chile, 1994, pp. 487-499.
[20]  R. S. Sutton y A. G. Barto, Reinforcement Learning: An Introduction, 2.ª ed. Cambridge, MA: MIT Press, 2018.
[21]  R. Kohavi, «A Study of Cross-Validation and Bootstrap for Accuracy Estimation and Model Selection», en Proc. 14th IJCAI, vol. 2, Morgan Kaufmann, 1995, pp. 1137-1143.
[22]  L. Breiman, J. H. Friedman, R. A. Olshen y C. J. Stone, Classification and Regression Trees. Belmont, CA: Wadsworth, 1984.
[23]  T. G. Dietterich, «Ensemble Methods in Machine Learning», en Multiple Classifier Systems (MCS 2000), LNCS vol. 1857, Springer, 2000, pp. 1-15.
[24]  L. Breiman, «Random Forests», Machine Learning, vol. 45, n.º 1, pp. 5-32, 2001.
[25]  J. H. Friedman, «Greedy function approximation: A gradient boosting machine», The Annals of Statistics, vol. 29, n.º 5, pp. 1189-1232, 2001.
[26]  G. Ke, Q. Meng, T. Finley, T. Wang, W. Chen, W. Ma, Q. Ye y T.-Y. Liu, «LightGBM: A Highly Efficient Gradient Boosting Decision Tree», en Advances in NIPS 30, 2017, pp. 3146-3154.
[27]  T. M. Cover y P. E. Hart, «Nearest neighbor pattern classification», IEEE Trans. Information Theory, vol. 13, n.º 1, pp. 21-27, 1967.
[28]  V. Chandola, A. Banerjee y V. Kumar, «Anomaly detection: A survey», ACM Computing Surveys, vol. 41, n.º 3, art. 15, pp. 1-58, 2009.
[29]  F. T. Liu, K. M. Ting y Z.-H. Zhou, «Isolation Forest», en 2008 Eighth IEEE Int. Conf. on Data Mining (ICDM), Pisa, 2008, pp. 413-422.
[30]  B. Schölkopf, J. C. Platt, J. Shawe-Taylor, A. J. Smola y R. C. Williamson, «Estimating the Support of a High-Dimensional Distribution», Neural Computation, vol. 13, n.º 7, pp. 1443-1471, 2001.
[31]  M. M. Breunig, H.-P. Kriegel, R. T. Ng y J. Sander, «LOF: Identifying Density-Based Local Outliers», ACM SIGMOD Record, vol. 29, n.º 2, pp. 93-104, 2000.
[32]  D. E. Rumelhart, G. E. Hinton y R. J. Williams, «Learning representations by back-propagating errors», Nature, vol. 323, n.º 6088, pp. 533-536, 1986.
[33]  T. Fawcett, «An introduction to ROC analysis», Pattern Recognition Letters, vol. 27, n.º 8, pp. 861-874, 2006.
[34]  D. M. W. Powers, «Evaluation: From Precision, Recall and F-Measure to ROC, Informedness, Markedness & Correlation», Journal of Machine Learning Technologies, vol. 2, n.º 1, pp. 37-63, 2011.
[35]  M. Sokolova y G. Lapalme, «A systematic analysis of performance measures for classification tasks», Information Processing & Management, vol. 45, n.º 4, pp. 427-437, 2009.
[36]  C. J. van Rijsbergen, Information Retrieval, 2.ª ed. Londres: Butterworths, 1979.
[37]  H. He y E. A. Garcia, «Learning from Imbalanced Data», IEEE Trans. Knowledge and Data Engineering, vol. 21, n.º 9, pp. 1263-1284, 2009.
[38]  J. Davis y M. Goadrich, «The relationship between Precision-Recall and ROC curves», en Proc. 23rd Int. Conf. on Machine Learning (ICML'06), ACM, 2006, pp. 233-240.
[39]  S. Axelsson, Intrusion Detection Systems: A Survey and Taxonomy, informe técnico 99-15. Göteborg: Chalmers University of Technology, mar. 2000.
[40]  P. García-Teodoro, J. Díaz-Verdejo, G. Maciá-Fernández y E. Vázquez, «Anomaly-based network intrusion detection: Techniques, systems and challenges», Computers & Security, vol. 28, n.º 1-2, pp. 18-28, 2009.
[41]  R. Sommer y V. Paxson, «Outside the Closed World: On Using Machine Learning for Network Intrusion Detection», en 2010 IEEE Symp. on Security and Privacy, Oakland, CA, 2010, pp. 305-316.
[42]  E. Tombini, H. Debar, L. Mé y M. Ducassé, «A serial combination of anomaly and misuse IDSes applied to HTTP traffic», en 20th Annual Computer Security Applications Conf. (ACSAC), IEEE, 2004, pp. 428-437.
[43]  R. Lippmann, J. W. Haines, D. J. Fried, J. Korba y K. Das, «Evaluating intrusion detection systems: the 1998 DARPA off-line intrusion detection evaluation», en Proc. DISCEX'00, vol. 2, IEEE, 2000, pp. 12-26.
[44]  M. Tavallaee, E. Bagheri, W. Lu y A. A. Ghorbani, «A Detailed Analysis of the KDD CUP 99 Data Set», en Proc. 2nd IEEE Symp. on Computational Intelligence for Security and Defense Applications (CISDA), Ottawa, 2009, pp. 1-6.
[45]  K. Kendall, A Database of Computer Attacks for the Evaluation of Intrusion Detection Systems, tesis de máster, Massachusetts Institute of Technology, jun. 1999.
[46]  W. Lee y S. J. Stolfo, «A framework for constructing features and models for intrusion detection systems», ACM Trans. Information and System Security, vol. 3, n.º 4, pp. 227-261, 2000.
[47]  Y. LeCun, Y. Bengio y G. Hinton, «Deep learning», Nature, vol. 521, n.º 7553, pp. 436-444, 2015.
[48]  W. J. Scheirer, A. de Rezende Rocha, A. Sapkota y T. E. Boult, «Toward Open Set Recognition», IEEE Trans. Pattern Analysis and Machine Intelligence, vol. 35, n.º 7, pp. 1757-1772, 2013.
[49]  D. Arp, E. Quiring, F. Pendlebury, A. Warnecke, F. Pierazzi, C. Wressnegger, L. Cavallaro y K. Rieck, «Dos and Don'ts of Machine Learning in Computer Security», en 31st USENIX Security Symposium, 2022, pp. 3971-3988.
[50]  B. Biggio y F. Roli, «Wild patterns: Ten years after the rise of adversarial machine learning», Pattern Recognition, vol. 84, pp. 317-331, 2018.
[51]  F. Pierazzi, F. Pendlebury, J. Cortellazzi y L. Cavallaro, «Intriguing Properties of Adversarial ML Attacks in the Problem Space», en 2020 IEEE Symp. on Security and Privacy, 2020, pp. 1332-1349.
[52]  S. Kapoor y A. Narayanan, «Leakage and the reproducibility crisis in machine-learning-based science», Patterns, vol. 4, n.º 9, art. 100804, 2023.
[53]  T. Chen y C. Guestrin, «XGBoost: A Scalable Tree Boosting System», en Proc. 22nd ACM SIGKDD Int. Conf. on Knowledge Discovery and Data Mining (KDD'16), ACM, 2016, pp. 785-794.
[54]  C. Molnar, Interpretable Machine Learning: A Guide for Making Black Box Models Explainable, 2.ª ed. Edición del autor, 2022.
[55]  N. V. Chawla, K. W. Bowyer, L. O. Hall y W. P. Kegelmeyer, «SMOTE: Synthetic Minority Over-sampling Technique», Journal of Artificial Intelligence Research, vol. 16, pp. 321-357, 2002.
[56]  C. K. Chow, «On optimum recognition error and reject tradeoff», IEEE Trans. Information Theory, vol. 16, n.º 1, pp. 41-46, 1970.
[57]  C. R. Harris, K. J. Millman, S. J. van der Walt et al., «Array programming with NumPy», Nature, vol. 585, n.º 7825, pp. 357-362, 2020.
[58]  W. McKinney, «Data Structures for Statistical Computing in Python», en Proc. 9th Python in Science Conf. (SciPy 2010), Austin, TX, 2010, pp. 56-61.
[59]  F. Pedregosa, G. Varoquaux, A. Gramfort, V. Michel, B. Thirion, O. Grisel et al., «Scikit-learn: Machine Learning in Python», Journal of Machine Learning Research, vol. 12, pp. 2825-2830, 2011.
[60]  G. Lemaître, F. Nogueira y C. K. Aridas, «Imbalanced-learn: A Python Toolbox to Tackle the Curse of Imbalanced Datasets in Machine Learning», Journal of Machine Learning Research, vol. 18, n.º 17, pp. 1-5, 2017.
[61]  F. J. Massey Jr., «The Kolmogorov-Smirnov Test for Goodness of Fit», Journal of the American Statistical Association, vol. 46, n.º 253, pp. 68-78, 1951.
[62]  J. D. Hunter, «Matplotlib: A 2D Graphics Environment», Computing in Science & Engineering, vol. 9, n.º 3, pp. 90-95, 2007.
[63]  M. L. Waskom, «seaborn: statistical data visualization», Journal of Open Source Software, vol. 6, n.º 60, art. 3021, 2021.
[64]  KDD Cup 1999 Data, The UCI KDD Archive, Information and Computer Science, University of California, Irvine, 1999.
[65]  J. McHugh, «Testing Intrusion Detection Systems: A Critique of the 1998 and 1999 DARPA Intrusion Detection System Evaluations as Performed by Lincoln Laboratory», ACM Trans. Information and System Security, vol. 3, n.º 4, pp. 262-294, 2000.
[66]  scikit-learn, documentación oficial de la API (módulos sklearn.model_selection / sklearn.neighbors).   <-- INCOMPLETA: falta año/fecha de consulta y la URL de LocalOutlierFactor
[67]  M. Sakurada y T. Yairi, «Anomaly Detection Using Autoencoders with Nonlinear Dimensionality Reduction», en Proc. MLSDA 2014 2nd Workshop on Machine Learning for Sensory Data Analysis, ACM, 2014, pp. 4-11.
[68]  J. Pineau, P. Vincent-Lamarre, K. Sinha, V. Larivière, A. Beygelzimer, F. d'Alché-Buc, E. Fox y H. Larochelle, «Improving Reproducibility in Machine Learning Research (A Report from the NeurIPS 2019 Reproducibility Program)», Journal of Machine Learning Research, vol. 22, n.º 164, pp. 1-20, 2021.
[69]  J. Demšar, «Statistical Comparisons of Classifiers over Multiple Data Sets», Journal of Machine Learning Research, vol. 7, pp. 1-30, 2006.
[70]  T. G. Dietterich, «Approximate Statistical Tests for Comparing Supervised Classification Learning Algorithms», Neural Computation, vol. 10, n.º 7, pp. 1895-1923, 1998.
[71]  A. Bendale y T. E. Boult, «Towards Open Set Deep Networks», en 2016 IEEE Conf. on Computer Vision and Pattern Recognition (CVPR), 2016, pp. 1563-1572.
[72]  P. Goldschmidt y D. Chudá, «Network intrusion datasets: A survey, limitations, and recommendations», Computers & Security, vol. 156, art. 104510, 2025.
[73]  S. Axelsson, «The base-rate fallacy and the difficulty of intrusion detection», ACM Trans. Information and System Security, vol. 3, n.º 3, pp. 186-205, 2000.
[74]  I. Sharafaldin, A. Habibi Lashkari y A. A. Ghorbani, «Toward Generating a New Intrusion Detection Dataset and Intrusion Traffic Characterization», en Proc. 4th Int. Conf. on Information Systems Security and Privacy (ICISSP), Funchal, 2018, pp. 108-116.
[75]  N. Moustafa y J. Slay, «UNSW-NB15: a comprehensive data set for network intrusion detection systems», en 2015 Military Communications and Information Systems Conf. (MilCIS), Canberra, 2015, pp. 1-6.
```

> [!note] Los DOI, para el pase por Zotero
> No se han metido en el bloque de arriba para no ensuciar el pegado, pero están **todos** en la columna «DOI / URL estable» de `Bibliografía.md`, entrada por entrada, bajo **la numeración del vault** (columna «Nº vault» de §2).

---

## 4 · Las 20 obras que NO reciben número: no tienen sede en el `.docx`

**Regla:** una obra sin sede en el documento entregable **no entra en la secuencia**. Meterla obligaría a inventar un sitio donde ponerle el marcador, y una entrada de bibliografía que nadie cita en el cuerpo es exactamente la huérfana que la tarea **B1** quiere eliminar.

Los números que estas obras tenían en el **mapa anterior** quedan **retirados**: ya no significan nada.

| Obra | Nº vault | Nº que tenía en el mapa anterior (retirado) | Por qué no tiene sede hoy |
|---|---|---|---|
| Barbará *et al.*, ADAM | [32] | ~~[41]~~ | comparación tabular de §3.5 no volcada |
| Ptacek y Newsham, *Insertion, Evasion and DoS* | [34] | ~~[43]~~ | sede de §2.2.3 no volcada |
| Snort Users Manual, «Writing Snort Rules» | [35] | ~~[45]~~ | sede de §2.2.4 no volcada |
| Ji *et al.*, IDS multinivel | [68] | ~~[47]~~ | los tres híbridos de §2.2.4 se anuncian y no aparecen (tarea **2.11**) |
| Kim, Lee y Kim, híbrido anomalía + misuse | [69] | ~~[48]~~ | ídem |
| Khraisat *et al.* 2020, stacking C5 + OC-SVM | [70] | ~~[49]~~ | ídem |
| Strom *et al.*, MITRE ATT&CK | [38] | ~~[53]~~ | §2.2.5.3 no volcada |
| Grinsztajn *et al.*, árboles vs DL en tabular | [41] | ~~[56]~~ | comparación tabular de §3.5 no volcada |
| McElfresh *et al.*, redes vs boosted trees | [42] | ~~[57]~~ | ídem |
| Sahami *et al.*, filtrado bayesiano de spam | [43] | ~~[58]~~ | bloque histórico de §2.3.2 no volcado |
| Szegedy *et al.*, *Intriguing properties…* | [46] | ~~[60]~~ | **bloque adversarial de §2.3.2 no volcado** |
| Goodfellow, Shlens y Szegedy, FGSM | [47] | ~~[61]~~ | ídem |
| Rudin, modelos interpretables | [53] | ~~[68]~~ | **§2.3.3 entera falta en el `.docx`** |
| RGPD — Reglamento (UE) 2016/679 | [55] | ~~[70]~~ | ídem |
| Reglamento de IA — (UE) 2024/1689 | [56] | ~~[71]~~ | ídem |
| Directiva NIS2 — (UE) 2022/2555 | [57] | ~~[72]~~ | ídem |
| Mitchell *et al.*, Model Cards | [60] | ~~[74]~~ | `A.3` «Ficha del sistema» no existe en el `.docx` |
| Shwartz-Ziv y Armon, *DL is not all you need* | [71] | ~~[76]~~ | comparación tabular de §3.5 no volcada |
| Hollmann *et al.*, TabPFN | [72] | ~~[77]~~ | ídem |
| Storkey, *When Training and Test Sets Are Different* | [78] | ~~[91]~~ | su ancla de §5.1 no sobrevive en el `.docx` |

**Motivo de fondo:** el `.docx` es un volcado **más recortado** que el vault. Faltan **§2.3.3 entera**, el **bloque adversarial de §2.3.2**, la **comparación tabular de §3.5**, las sedes de Ptacek y del Snort Users Manual en **§2.2.3-2.2.4**, y el apéndice **`A.3`**.

Además siguen sin número, por causas distintas:

- **`[11]` CRISP-DM** y **`[15]` Bergstra y Bengio** (vault): su única cita viva estaba en `A.3`.
- Las **8 obras marcadas ⚠️ «sin equivalente en el `.docx`»** del Anexo B de Kiko: CRISP-DM, Bergstra y Bengio, TabArena, Micci-Barreca, Pargent, Hwang, TESSERACT y Nested Learning. (Antes se decían «7» y se enumeraban 8; **son 8**.)
- Las **2 anclas ⛔ sin número** de §5.4 de este informe (Python como lenguaje de referencia · Shostack / modelo de amenaza).

> [!important] El total de obras sin número son **28**, no 22
> Aritmética verificada: **102 vivas − 74 con número = 28**. Son las **20 sin sede** de la tabla de
> arriba, más **CRISP-DM** y **Bergstra y Bengio**, más las **seis** que el Anexo B de Kiko marca
> también con ⛔ y que la cuenta anterior omitía: **TabArena**, **Micci-Barreca**, **Pargent**,
> **Hwang**, **TESSERACT** y **Nested Learning**. La lista de descartes de la tarea **B1** es esta,
> completa.
>
> (Los 74 «con número» son las 64 de `[12]`–`[75]` más las 10 del tramo congelado con equivalente
> en el vault: el `[9]` del `.docx` no tiene ninguno.)

> [!warning] Si Francisco volca alguna de estas sedes
> **No se intercala.** Las obras que entren reciben números **por detrás del `[75]`** (`[76]`, `[77]`…), aunque su sede esté en el capítulo 2. Intercalar rompería todo lo ya pegado, y el coste de romperlo es mucho mayor que el de un número «fuera de orden» al final de la lista.

---

## 5 · Cuatro discrepancias detectadas al leer el binario

Ninguna de las cuatro estaba en las versiones anteriores del mapa. Se registran aquí porque **cambian el trabajo que hay que hacer en Word**, no solo su descripción.

### 5.1 · El cuerpo del `.docx` ya tiene **50 marcadores, no 11** — y 39 están MAL

La versión anterior afirmaba que el Word tenía «exactamente 11 marcadores» y que «el resto del documento no tiene ni un marcador hoy». **Es falso.** Y la cifra que la sustituyó —«46, de los que 35 están mal»— **también lo era**: el recuento correcto, verificado sobre el texto extraído del binario, es **50 marcadores en total, 11 del rango congelado y 39 con la numeración VIEJA del vault**, repartidos en **47 párrafos** (los párrafos 1999, 2032 y 2262 llevan **dos** cada uno).

**Ámbito de la cuenta:** párrafos **198–2549**; quedan fuera el índice y la bibliografía final. Se han descartado los falsos positivos de intervalos numéricos del tipo `[0,1]`, y **sí cuentan** los marcadores que traen localizador (número seguido de coma y capítulo o sección) — que, por la decisión del 2026-08-24, hay que **reescribir como `[n]` a secas** al traducirlos.

**Rango congelado (11 apariciones):**

| Marcador | Párrafos |
|---|---|
| `[1]` | 230 |
| `[2]` | 242 |
| `[3]` | 244 |
| `[4]` | 306 |
| `[5]` | 321, 369 |
| `[7]` | 351 |
| `[8]` | 477 |
| `[9]` | 498 |
| `[10]` | 478 |
| `[11]` | 246 |

**`[6]` no aparece ni una vez en el cuerpo** — que es exactamente lo que sostiene la tarea **B4**.

**Numeración vieja del vault (39 apariciones, 20 números distintos):**

| Marcador | Párrafos |
|---|---|
| `[17]` | 1441 |
| `[18]` | 737, 1436, 1929, 2093, 2100, 2120 |
| `[20]` | 1434, 2106 |
| `[23]` | 868, 873, 1432, 1443, 1931, 1934 |
| `[24]` | 1999, 2024, 2032 |
| `[25]` | 1438, 1999, 2032 |
| `[31]` | 2116 |
| `[49]` | 1837, 2228 |
| `[50]` | 2300 |
| `[51]` | 2298 |
| `[52]` | 2101 |
| `[61]` | 1835, 2111 |
| `[62]` | 2224 |
| `[63]` | 2262 |
| `[64]` | 2262 |
| `[65]` | 2269 |
| `[66]` | 2303 |
| `[67]` | 2317, 2318 |
| `[74]` | 1970, 1972 |
| `[77]` | 1978 |

> [!danger] Colisionan con la numeración nueva
> Esos 39 marcadores **no son «los que ya están hechos»**: son números que hoy significan **otra obra**. Ejemplo claro: en el Word hay un `[23]` puesto por **Tavallaee**, pero en la numeración de este informe **`[23]` es Dietterich 2000**. Si se dejan y se insertan los que faltan, el documento queda con dos obras compartiendo número.
>
> **Consecuencia operativa: el pase de Word es de REESCRITURA, no de inserción.** Hay que repasar los 39 uno a uno y traducirlos, además de insertar los ~165 que faltan. La estimación de esfuerzo de **T4** se ajusta en consecuencia: **39 reescrituras**, no 35.

### 5.2 · §6.2 «Líneas futuras» **NO está vacía**

El mapa anterior la daba por vacía («solo el título») y bloqueaba por eso seis obras. **Es falso:** §6.2 ocupa los párrafos **2179-2549** del `.docx`. Ahí viven **CIC-IDS2017** y **UNSW-NB15**, que por eso sí reciben número en esta versión: `[74]` y `[75]`, las dos últimas de la secuencia.

### 5.3 · Dos matches solo **aproximados**

En dos casos el fragmento literal **no aparece verbatim** en el `.docx` y la sede se ha **inferido por contenido**:

| Nº | Obra | Párr. inferido |
|---|---|---|
| **[65]** | McHugh (2000) | 864 |
| **[75]** | Moustafa y Slay (2015) | 2300 |

> [!note] Chow ya NO es aproximado
> Se le atribuía el párrafo **1833** por inferencia a partir de la palabra «rechazo». Esa sede es
> **falsa**: el 1833 habla de la decisión interna **P-5** y de la calidad del etiquetado, no del
> *error-reject tradeoff*. La sede real es el párrafo **800** (§3.5.5), cuyo texto —«estimadas
> fuera de muestra (out-of-fold, mediante validación cruzada sobre D3)»— **es literalmente** el
> compromiso error/rechazo de Chow. Con ancla literal, `[56]` pasa a ser **match exacto** y sale de
> esta lista.

### 5.4 · Quedan **3 placeholders sin resolver** en el cuerpo

- **2** de la forma `[ enlace bibliografía: …]`
- **1** de la forma `[CITA: …]`

Son visibles a simple vista en el documento final. Los **cinco** marcadores que la tarea **4.1** enumeraba se cubren con `[64]`, `[43]`, `[44]`, `[65]` y `[72]`, pero **estos tres siguen ahí** y hay que sustituirlos en el mismo pase.

---

## 6 · Lo que no he podido confirmar

- **La página exacta de siete libros y documentos largos.** `[16]` Mitchell, `[18]` Jolliffe, `[20]` Sutton y Barto, `[22]` Breiman *et al.* (CART), `[36]` van Rijsbergen, `[4]` Chio y `[8]` Stallings quedan **marcados, no inventados**. Tres llevan capítulo fijado **por estructura de la obra**, no por texto consultado; dos (`[22]`, `[36]`) ni eso. **Deja de ser un bloqueo para el `.docx`** desde la decisión del 2026-08-24: allí los marcadores van **sin localizador**. Sigue siendo una reserva **del vault**, donde los localizadores sí se usan.
- **`[34]` Powers (2011) es NIVEL 2, y sostiene dos definiciones de manual** (precisión y *recall*). Su revista original no tiene revisión por pares acreditada. Si Francisco quiere nivel 1 puro, el sustituto ya está en la lista: **`[33]` Fawcett** o **`[35]` Sokolova y Lapalme** cubren lo mismo. **No se ha sustituido por cuenta propia.**
- **`[39]` Axelsson (taxonomía) es NIVEL 2** — informe universitario sin revisión por pares. Es la fuente canónica de los ejes de taxonomía de IDS y no hay equivalente revisado por pares del mismo contenido. Se declara la reserva.
- **El «RandomForest monolítico» como forma concreta del «patrón dominante» NO está verificado en fuente**: es una lectura del proyecto, respaldada por `baseline.py`. El «~99 %» sí está verificado verbatim en [[benchmark-comparativo-nsl-kdd]] §A.1, con `[44]` Tavallaee. **Si el tribunal aprieta, atenuar a «un clasificador supervisado monolítico».**
- **El ancla de `[68]` Pineau** (reproducibilidad en ML). **Es el único número de la secuencia sin ancla literal utilizable:** el Anexo C de `Las tareas de Kiko.md` no tiene entrada para esta obra, así que **hoy no se puede pegar**. No se inventa un fragmento: queda **pendiente explícito** de localizar la frase de §5.0 que sostiene la cita.
- **La correspondencia de `[66]`** (documentación de scikit-learn). La entrada del vault `[14]` es la página de `GridSearchCV` y la sede del `.docx` pide la de `LocalOutlierFactor(novelty=True)`. Son dos páginas de la misma obra: **no se da de alta un número nuevo, pero la página concreta hay que fijarla en Zotero**.

---

## 7 · Recuento explícito

| Magnitud | Valor |
|---|---|
| **Números que ocupa el `.docx`** | **75** — `[1]`-`[11]` congelados + `[12]`-`[75]` (64 obras) |
| **Obras del vault que NO llegan al `.docx`** | **28** — las 20 sin sede (§4) + CRISP-DM, Bergstra y Bengio, TabArena, Micci-Barreca, Pargent, Hwang, TESSERACT y Nested Learning |
| **Marcadores ya presentes en el cuerpo del Word** | **50** en 47 párrafos — 11 correctos + **39 con numeración vieja, a reescribir** (§5.1) |
| **Marcadores que faltan por insertar** | ~165 apariciones |
| **Matches aproximados a confirmar** | **2** — `[65]` McHugh y `[75]` Moustafa y Slay |
| **Números sin ancla literal** | **1** — `[68]` Pineau: no se puede pegar hasta establecerla |
| **Placeholders sin resolver en el cuerpo** | **3** — 2 de `[ enlace bibliografía: …]` y 1 de `[CITA: …]` |
| **Estado del contador global del VAULT** (no cambia con esto) | 110 filas · 102 vivas · 8 quemadas · primer libre `[111]` |

---

## 8 · Implicaciones para el proyecto

1. **T1 queda cerrada con un mapa, no con una renumeración.** `[11]` del `.docx` = `[26]` del vault. **El vault no se toca.**
2. **T4 se ejecuta solo en el Word.** La ficha dice «en el vault y en el `.docx` a la vez» y **eso contradice la decisión del usuario**: el vault **mantiene su numeración**. La ficha se ha corregido en `Las tareas de Kiko.md`.
3. **B1 se resuelve casi sola:** al colocar los Anexos C y D, las huérfanas que reciben número dejan de serlo. La lista real de descartes son **28 obras** —las 20 de §4 más CRISP-DM, Bergstra y Bengio, TabArena, Micci-Barreca, Pargent, Hwang, TESSERACT y Nested Learning— y muchas de ellas no son descarte, sino **sede pendiente de volcar**.
4. **El trabajo de Word es mayor de lo estimado**, por §5.1: no es insertar, es **reescribir 39 y añadir ~165**. El capítulo 2 se lleva más de la mitad.
5. **Choca con `resumen-de-decisiones.md` en un punto:** el `.docx` sostiene con **nivel 3** el dato de apertura del capítulo 1 (`channelpartner.es`) mientras el vault tiene la fuente de nivel 1 (INCIBE). Es una línea en Word y no la decide un agente.

---

## 9 · Bibliografía completa `[1]`-`[75]`, para pegar en el apartado Bibliografía del Word

> [!important] Qué es esta sección y qué no
> Es la lista **completa y en orden**, incluidos los **11 congelados**. El texto sale **únicamente** de
> `Bibliografía.md`; **no se ha inventado ningún dato**. El formato IEEE final lo genera Francisco en
> Zotero, así que aquí lo que importa es que los **datos estén completos**.
>
> **Sin localizadores** (decisión del 2026-08-24). Las entradas con datos que faltan van marcadas
> `⚠️ INCOMPLETA` con lo que falta escrito al lado: **son cuatro** —`[1]`, `[8]`, `[9]` y `[66]`— y
> están enumeradas al final de la sección.

**Tramo congelado `[1]`-`[11]`.** Se transcribe **la obra que el Word cita hoy**, con los datos
completos del vault cuando existen. Si Francisco ejecuta **B2** y **B3**, estas cuatro filas son el
texto de destino.

| `[n]` | Referencia | Nº vault |
|---|---|---|
| **[1]** | ⚠️ **INCOMPLETA — hay que decidir la fuente primero.** El Word cita hoy una URL desnuda de prensa sectorial (`https://www.channelpartner.es/seguridad/principales-ciberataques-en-espana-en-2024/`), **sin autor, título ni fecha**, y es **nivel 3**. La fuente equivalente de nivel 1, ya completa en el vault, es: Instituto Nacional de Ciberseguridad (INCIBE), «INCIBE presenta su balance de ciberseguridad 2024 con más de 97.000 incidentes gestionados», nota de prensa, 20 de marzo de 2025. Disponible en: https://www.incibe.es/incibe/sala-de-prensa/incibe-presenta-su-balance-de-ciberseguridad-2024-con-mas-de-97000-incidentes. **Decide Francisco** | [1] |
| **[2]** | J. P. Anderson, *Computer Security Threat Monitoring and Surveillance*. Fort Washington, PA: James P. Anderson Co., contrato 79F296400, 26 de febrero de 1980 (revisado el 15 de abril de 1980). Disponible en: http://csrc.nist.gov/publications/history/ande80.pdf | [2] |
| **[3]** | D. E. Denning, «An Intrusion-Detection Model», *IEEE Transactions on Software Engineering*, vol. SE-13, n.º 2, pp. 222-232, feb. 1987. DOI: 10.1109/TSE.1987.232894 | [3] |
| **[4]** | C. Chio y D. Freeman, *Machine Learning and Security: Protecting Systems with Data and Algorithms*, 1.ª ed. Sebastopol, CA: O'Reilly Media, 2018, 383 pp. ISBN 978-1-4919-7990-7 | [4] |
| **[5]** | A. Géron, *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow: Concepts, Tools, and Techniques to Build Intelligent Systems*, 2.ª ed. Sebastopol, CA: O'Reilly Media, 2019. ISBN 978-1-492-03264-9 | [5] |
| **[6]** | I. Goodfellow, Y. Bengio y A. Courville, *Deep Learning*. Cambridge, MA: MIT Press, 2016. ISBN 978-0-262-03561-3 | [6] |
| **[7]** | K. P. Murphy, *Machine Learning: A Probabilistic Perspective*. Cambridge, MA: MIT Press, 2012. ISBN 978-0-262-01802-9 | [7] |
| **[8]** | W. Stallings y L. Brown, *Computer Security: Principles and Practice*, 5.ª ed. Hoboken, NJ: Pearson, 2023. ISBN 978-0-13-809167-5 · ⚠️ **INCOMPLETA EN EL WORD, no aquí:** el Word tiene hoy solo «Computer Security : Principles and Practice» y «William Stallings». Este es el texto de destino de **B3**; los datos ya están completos | [8] |
| **[9]** | ⚠️ **INCOMPLETA, y no se puede completar: NO ES UNA OBRA DISTINTA.** El Word tiene aquí una URL a una copia PDF no autorizada de la misma obra que `[8]` (`https://students.aiu.edu/.../j5V2a3_Computer_Security_Principles.pdf`), **nivel 3**. **Tarea B2: fundirla en `[8]` y eliminar esta entrada.** Si se elimina, el `[9]` del `.docx` queda **quemado y NO se renumera**. En el vault el `[9]` está quemado desde el 2026-08-09 por esta misma razón | — (ninguno) |
| **[10]** | Centro Criptológico Nacional (CCN-CERT), *Guía de Seguridad de las TIC CCN-STIC-401: Glosario y Abreviaturas*, entrada «ciberseguridad». Disponible en: https://www.ccn-cert.cni.es/es/series-ccn-stic/guias/glosario-de-terminos.html · **Se cita sin versión ni fecha por decisión de Francisco del 2026-08-18** (la guía es un documento vivo y la ficha del CCN es su referencia estable): **esa ausencia NO es un dato que falte, es la forma de cita decidida** | [10] |
| **[11]** | M. Roesch, «Snort — Lightweight Intrusion Detection for Networks», en *Proc. 13th USENIX Conference on System Administration (LISA'99)*, Seattle, WA, 7-12 nov. 1999, USENIX Association, pp. 229-238. Disponible en: https://www.usenix.org/legacy/publications/library/proceedings/lisa99/roesch.html | [26] |

**Tramo `[12]`-`[75]`.** Idéntico al bloque de §3.1; se repite aquí para que esta sección se pueda
pegar de una sola vez.

```
[12]  A. Khraisat, I. Gondal, P. Vamplew y J. Kamruzzaman, «Survey of intrusion detection systems: techniques, datasets and challenges», Cybersecurity, vol. 2, art. 20, 2019.
[13]  H. Hindy, R. Atkinson, C. Tachtatzis, J.-N. Colin, E. Bayne y X. Bellekens, «Utilising Deep Learning Techniques for Effective Zero-Day Attack Detection», Electronics, vol. 9, n.º 10, art. 1684, 2020.
[14]  K. Scarfone y P. Mell, Guide to Intrusion Detection and Prevention Systems (IDPS), NIST Special Publication 800-94. Gaithersburg, MD: NIST, feb. 2007.
[15]  S. J. Russell y P. Norvig, Artificial Intelligence: A Modern Approach, 4.ª ed. Hoboken, NJ: Pearson, 2021.
[16]  T. M. Mitchell, Machine Learning. Nueva York: McGraw-Hill, 1997.
[17]  T. Hastie, R. Tibshirani y J. Friedman, The Elements of Statistical Learning: Data Mining, Inference, and Prediction, 2.ª ed. Nueva York: Springer, 2009. ISBN 978-0-387-84857-0.
[18]  I. T. Jolliffe, Principal Component Analysis, 2.ª ed. Nueva York: Springer, 2002.
[19]  R. Agrawal y R. Srikant, «Fast Algorithms for Mining Association Rules», en Proc. 20th Int. Conf. on Very Large Data Bases (VLDB'94), Santiago de Chile, 1994, pp. 487-499.
[20]  R. S. Sutton y A. G. Barto, Reinforcement Learning: An Introduction, 2.ª ed. Cambridge, MA: MIT Press, 2018.
[21]  R. Kohavi, «A Study of Cross-Validation and Bootstrap for Accuracy Estimation and Model Selection», en Proc. 14th IJCAI, vol. 2, Morgan Kaufmann, 1995, pp. 1137-1143.
[22]  L. Breiman, J. H. Friedman, R. A. Olshen y C. J. Stone, Classification and Regression Trees. Belmont, CA: Wadsworth, 1984.
[23]  T. G. Dietterich, «Ensemble Methods in Machine Learning», en Multiple Classifier Systems (MCS 2000), LNCS vol. 1857, Springer, 2000, pp. 1-15.
[24]  L. Breiman, «Random Forests», Machine Learning, vol. 45, n.º 1, pp. 5-32, 2001.
[25]  J. H. Friedman, «Greedy function approximation: A gradient boosting machine», The Annals of Statistics, vol. 29, n.º 5, pp. 1189-1232, 2001.
[26]  G. Ke, Q. Meng, T. Finley, T. Wang, W. Chen, W. Ma, Q. Ye y T.-Y. Liu, «LightGBM: A Highly Efficient Gradient Boosting Decision Tree», en Advances in NIPS 30, 2017, pp. 3146-3154.
[27]  T. M. Cover y P. E. Hart, «Nearest neighbor pattern classification», IEEE Trans. Information Theory, vol. 13, n.º 1, pp. 21-27, 1967.
[28]  V. Chandola, A. Banerjee y V. Kumar, «Anomaly detection: A survey», ACM Computing Surveys, vol. 41, n.º 3, art. 15, pp. 1-58, 2009.
[29]  F. T. Liu, K. M. Ting y Z.-H. Zhou, «Isolation Forest», en 2008 Eighth IEEE Int. Conf. on Data Mining (ICDM), Pisa, 2008, pp. 413-422.
[30]  B. Schölkopf, J. C. Platt, J. Shawe-Taylor, A. J. Smola y R. C. Williamson, «Estimating the Support of a High-Dimensional Distribution», Neural Computation, vol. 13, n.º 7, pp. 1443-1471, 2001.
[31]  M. M. Breunig, H.-P. Kriegel, R. T. Ng y J. Sander, «LOF: Identifying Density-Based Local Outliers», ACM SIGMOD Record, vol. 29, n.º 2, pp. 93-104, 2000.
[32]  D. E. Rumelhart, G. E. Hinton y R. J. Williams, «Learning representations by back-propagating errors», Nature, vol. 323, n.º 6088, pp. 533-536, 1986.
[33]  T. Fawcett, «An introduction to ROC analysis», Pattern Recognition Letters, vol. 27, n.º 8, pp. 861-874, 2006.
[34]  D. M. W. Powers, «Evaluation: From Precision, Recall and F-Measure to ROC, Informedness, Markedness & Correlation», Journal of Machine Learning Technologies, vol. 2, n.º 1, pp. 37-63, 2011.
[35]  M. Sokolova y G. Lapalme, «A systematic analysis of performance measures for classification tasks», Information Processing & Management, vol. 45, n.º 4, pp. 427-437, 2009.
[36]  C. J. van Rijsbergen, Information Retrieval, 2.ª ed. Londres: Butterworths, 1979.
[37]  H. He y E. A. Garcia, «Learning from Imbalanced Data», IEEE Trans. Knowledge and Data Engineering, vol. 21, n.º 9, pp. 1263-1284, 2009.
[38]  J. Davis y M. Goadrich, «The relationship between Precision-Recall and ROC curves», en Proc. 23rd Int. Conf. on Machine Learning (ICML'06), ACM, 2006, pp. 233-240.
[39]  S. Axelsson, Intrusion Detection Systems: A Survey and Taxonomy, informe técnico 99-15. Göteborg: Chalmers University of Technology, mar. 2000.
[40]  P. García-Teodoro, J. Díaz-Verdejo, G. Maciá-Fernández y E. Vázquez, «Anomaly-based network intrusion detection: Techniques, systems and challenges», Computers & Security, vol. 28, n.º 1-2, pp. 18-28, 2009.
[41]  R. Sommer y V. Paxson, «Outside the Closed World: On Using Machine Learning for Network Intrusion Detection», en 2010 IEEE Symp. on Security and Privacy, Oakland, CA, 2010, pp. 305-316.
[42]  E. Tombini, H. Debar, L. Mé y M. Ducassé, «A serial combination of anomaly and misuse IDSes applied to HTTP traffic», en 20th Annual Computer Security Applications Conf. (ACSAC), IEEE, 2004, pp. 428-437.
[43]  R. Lippmann, J. W. Haines, D. J. Fried, J. Korba y K. Das, «Evaluating intrusion detection systems: the 1998 DARPA off-line intrusion detection evaluation», en Proc. DISCEX'00, vol. 2, IEEE, 2000, pp. 12-26.
[44]  M. Tavallaee, E. Bagheri, W. Lu y A. A. Ghorbani, «A Detailed Analysis of the KDD CUP 99 Data Set», en Proc. 2nd IEEE Symp. on Computational Intelligence for Security and Defense Applications (CISDA), Ottawa, 2009, pp. 1-6.
[45]  K. Kendall, A Database of Computer Attacks for the Evaluation of Intrusion Detection Systems, tesis de máster, Massachusetts Institute of Technology, jun. 1999.
[46]  W. Lee y S. J. Stolfo, «A framework for constructing features and models for intrusion detection systems», ACM Trans. Information and System Security, vol. 3, n.º 4, pp. 227-261, 2000.
[47]  Y. LeCun, Y. Bengio y G. Hinton, «Deep learning», Nature, vol. 521, n.º 7553, pp. 436-444, 2015.
[48]  W. J. Scheirer, A. de Rezende Rocha, A. Sapkota y T. E. Boult, «Toward Open Set Recognition», IEEE Trans. Pattern Analysis and Machine Intelligence, vol. 35, n.º 7, pp. 1757-1772, 2013.
[49]  D. Arp, E. Quiring, F. Pendlebury, A. Warnecke, F. Pierazzi, C. Wressnegger, L. Cavallaro y K. Rieck, «Dos and Don'ts of Machine Learning in Computer Security», en 31st USENIX Security Symposium, 2022, pp. 3971-3988.
[50]  B. Biggio y F. Roli, «Wild patterns: Ten years after the rise of adversarial machine learning», Pattern Recognition, vol. 84, pp. 317-331, 2018.
[51]  F. Pierazzi, F. Pendlebury, J. Cortellazzi y L. Cavallaro, «Intriguing Properties of Adversarial ML Attacks in the Problem Space», en 2020 IEEE Symp. on Security and Privacy, 2020, pp. 1332-1349.
[52]  S. Kapoor y A. Narayanan, «Leakage and the reproducibility crisis in machine-learning-based science», Patterns, vol. 4, n.º 9, art. 100804, 2023.
[53]  T. Chen y C. Guestrin, «XGBoost: A Scalable Tree Boosting System», en Proc. 22nd ACM SIGKDD Int. Conf. on Knowledge Discovery and Data Mining (KDD'16), ACM, 2016, pp. 785-794.
[54]  C. Molnar, Interpretable Machine Learning: A Guide for Making Black Box Models Explainable, 2.ª ed. Edición del autor, 2022.
[55]  N. V. Chawla, K. W. Bowyer, L. O. Hall y W. P. Kegelmeyer, «SMOTE: Synthetic Minority Over-sampling Technique», Journal of Artificial Intelligence Research, vol. 16, pp. 321-357, 2002.
[56]  C. K. Chow, «On optimum recognition error and reject tradeoff», IEEE Trans. Information Theory, vol. 16, n.º 1, pp. 41-46, 1970.
[57]  C. R. Harris, K. J. Millman, S. J. van der Walt et al., «Array programming with NumPy», Nature, vol. 585, n.º 7825, pp. 357-362, 2020.
[58]  W. McKinney, «Data Structures for Statistical Computing in Python», en Proc. 9th Python in Science Conf. (SciPy 2010), Austin, TX, 2010, pp. 56-61.
[59]  F. Pedregosa, G. Varoquaux, A. Gramfort, V. Michel, B. Thirion, O. Grisel et al., «Scikit-learn: Machine Learning in Python», Journal of Machine Learning Research, vol. 12, pp. 2825-2830, 2011.
[60]  G. Lemaître, F. Nogueira y C. K. Aridas, «Imbalanced-learn: A Python Toolbox to Tackle the Curse of Imbalanced Datasets in Machine Learning», Journal of Machine Learning Research, vol. 18, n.º 17, pp. 1-5, 2017.
[61]  F. J. Massey Jr., «The Kolmogorov-Smirnov Test for Goodness of Fit», Journal of the American Statistical Association, vol. 46, n.º 253, pp. 68-78, 1951.
[62]  J. D. Hunter, «Matplotlib: A 2D Graphics Environment», Computing in Science & Engineering, vol. 9, n.º 3, pp. 90-95, 2007.
[63]  M. L. Waskom, «seaborn: statistical data visualization», Journal of Open Source Software, vol. 6, n.º 60, art. 3021, 2021.
[64]  KDD Cup 1999 Data, The UCI KDD Archive, Information and Computer Science, University of California, Irvine, 1999. [En línea]. Disponible en: http://kdd.ics.uci.edu/databases/kddcup99/kddcup99.html
[65]  J. McHugh, «Testing Intrusion Detection Systems: A Critique of the 1998 and 1999 DARPA Intrusion Detection System Evaluations as Performed by Lincoln Laboratory», ACM Trans. Information and System Security, vol. 3, n.º 4, pp. 262-294, 2000.
[66]  scikit-learn, documentación oficial de la API (módulos sklearn.model_selection / sklearn.neighbors).   <-- INCOMPLETA: falta año/fecha de consulta y la URL de LocalOutlierFactor
[67]  M. Sakurada y T. Yairi, «Anomaly Detection Using Autoencoders with Nonlinear Dimensionality Reduction», en Proc. MLSDA 2014 2nd Workshop on Machine Learning for Sensory Data Analysis, ACM, 2014, pp. 4-11.
[68]  J. Pineau, P. Vincent-Lamarre, K. Sinha, V. Larivière, A. Beygelzimer, F. d'Alché-Buc, E. Fox y H. Larochelle, «Improving Reproducibility in Machine Learning Research (A Report from the NeurIPS 2019 Reproducibility Program)», Journal of Machine Learning Research, vol. 22, n.º 164, pp. 1-20, 2021.
[69]  J. Demšar, «Statistical Comparisons of Classifiers over Multiple Data Sets», Journal of Machine Learning Research, vol. 7, pp. 1-30, 2006.
[70]  T. G. Dietterich, «Approximate Statistical Tests for Comparing Supervised Classification Learning Algorithms», Neural Computation, vol. 10, n.º 7, pp. 1895-1923, 1998.
[71]  A. Bendale y T. E. Boult, «Towards Open Set Deep Networks», en 2016 IEEE Conf. on Computer Vision and Pattern Recognition (CVPR), 2016, pp. 1563-1572.
[72]  P. Goldschmidt y D. Chudá, «Network intrusion datasets: A survey, limitations, and recommendations», Computers & Security, vol. 156, art. 104510, 2025.
[73]  S. Axelsson, «The base-rate fallacy and the difficulty of intrusion detection», ACM Trans. Information and System Security, vol. 3, n.º 3, pp. 186-205, 2000.
[74]  I. Sharafaldin, A. Habibi Lashkari y A. A. Ghorbani, «Toward Generating a New Intrusion Detection Dataset and Intrusion Traffic Characterization», en Proc. 4th Int. Conf. on Information Systems Security and Privacy (ICISSP), Funchal, 2018, pp. 108-116.
[75]  N. Moustafa y J. Slay, «UNSW-NB15: a comprehensive data set for network intrusion detection systems», en 2015 Military Communications and Information Systems Conf. (MilCIS), Canberra, 2015, pp. 1-6.
```

### 9.1 · Las cuatro entradas INCOMPLETAS

No se han rellenado con datos inventados. Son estas, con lo que falta en cada una:

| `[n]` | Obra | Qué falta |
|---|---|---|
| **[1]** | apertura del capítulo 1 | El Word tiene una **URL desnuda de prensa** sin autor, título ni fecha (nivel 3). No es que falten datos: **falta decidir la fuente**. El sustituto de nivel 1 (INCIBE) está completo en el vault y transcrito arriba. **Decide Francisco** |
| **[8]** | Stallings y Brown | **Nada falta aquí:** los datos están completos (5.ª ed., Pearson, 2023, ISBN). Lo incompleto es **lo que hoy hay escrito en el Word** (solo título y autor). Es el trabajo de **B3** |
| **[9]** | copia PDF de Stallings | **No se puede completar: no es una obra distinta.** Duplica `[8]` y es una copia no autorizada. **B2** la funde en `[8]`; si se elimina, el número queda **quemado** |
| **[66]** | documentación de scikit-learn | **Sin año ni fecha de consulta**, y la URL registrada en el vault es la de `GridSearchCV` mientras la sede del `.docx` pide la de `LocalOutlierFactor(novelty=True)`. Son dos páginas de la misma obra: **no se da de alta número nuevo**, pero la página y la fecha hay que fijarlas en Zotero |

> [!note] Las dos reservas que este pase NO ha tocado
> Siguen exactamente como estaban: **`[68]` Pineau sin ancla literal** (no se puede pegar hasta
> establecerla) y **`[65]` McHugh y `[75]` Moustafa y Slay con sede inferida por contenido**, no
> literal. Ver §5.3 y §6.
