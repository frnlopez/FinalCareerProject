---
titulo: "Bibliografía del .docx: numeración desde [12] y sitio exacto de cada marcador"
numero: "-"
estado: informe
docx_ref: "-"
---

# Bibliografía del `.docx`: numeración desde `[12]` y sitio exacto de cada marcador

- **Encargo:** producir la lista de bibliografía del `.docx` **a partir de `[12]` y en orden de aparición**, con el sitio exacto donde va cada marcador. `[1]`-`[11]` del Word quedan congelados. La renumeración afecta **solo al `.docx`**: el vault no se toca ni se renumera.
- **Fecha:** 2026-08-24
- **Alcance:** entra todo lo que tiene sede en el documento final (capítulos 1-6, Apéndice A, Apéndice B, bibliografía). Quedan fuera las sedes que hoy no existen o están vacías —§ propia al final—. No se toca ninguna nota del vault, no se renumera nada en el vault, y no se hace formato IEEE final (eso es Zotero, trabajo de Francisco).
- **Alimenta a:** [[Bibliografía]] · tareas **T1**, **T3**, **T4** y **B1**-**B4** de `Las tareas de Kiko.md`

## Respuesta corta

El `.docx` necesita **95 números**: los **11 congelados** más **84 nuevos, de `[12]` a `[95]`**. De esos 95, **62 son entradas que ya existían en el vault** —se mapean, no se dan de alta—, **32 son altas nuevas** (`[79]`-`[110]` del vault, escritas ya en `Bibliografía.md`) y **1 es exclusiva del `.docx`** (el `[9]` del Word, la copia pirata de Stallings). El desajuste que denunciaba **T1 es real y se confirma**: el `[11]` del Word es **Snort/Roesch**, que en el vault es `[26]`; el `[11]` del vault es **CRISP-DM** y **no llega al `.docx`**, porque su única cita viva está en `A.3`, un apéndice que hoy **no existe** en el documento.

> [!warning] Las dos reglas de lectura de este informe
> **(1) `Nº .docx` ≠ `Nº en el vault`.** Son dos numeraciones independientes y esta tabla es el puente. Al pasar los marcadores al Word se escribe **el número del `.docx`**; al buscar la referencia en `Bibliografía.md` se usa **el del vault**.
> **(2) Un número del `.docx` por OBRA**, reutilizado en todas sus apariciones. La tabla principal lista **la primera aparición**, que es la que fija el orden; la columna «Capítulo/sección» enumera las demás sedes de la misma obra cuando las hay.

---

## 1 · Los `[1]`-`[11]` del `.docx`, congelados

Transcritos **tal como están hoy** en el Word (leídos en `Resultados/docx/COMPARACION/docx_limpio.md`, sección «Bibliografía», que es el volcado en limpio del documento de Francisco). No se corrigen aquí: **T3**, **B2** y **B3** son tareas de Word.

| `[n]` `.docx` | Tal como está escrito hoy en el Word | Equivalente en el vault | Estado |
|---|---|---|---|
| [1] | `https://www.channelpartner.es/seguridad/principales-ciberataques-en-espana-en-2024/` | `[1]` INCIBE, balance de ciberseguridad 2024 | ⚠️ **Desajuste de fuente, no de número.** El Word cita prensa sectorial (**nivel 3**); el vault sostiene el mismo dato con la nota de prensa de **INCIBE** (nivel 1). El número se congela; **la fuente debería sustituirse por la del vault** en el pase de Word. Decide Francisco |
| [2] | «Computer Security Threat Monitoring and Surveillance». James P. Anderson Co. | `[2]` Anderson (1980) | ✅ Misma obra. **B3**: falta el año (1980) |
| [3] | Denning, Dorothy E. (1987). «An Intrusion-Detection Model». *IEEE TSE*, SE-13(2), 222-232 | `[3]` Denning (1987) | ✅ Coincide, y con páginas |
| [4] | Chio, C., & Freeman, D. (2018) *Machine Learning & Security*. O'Reilly | `[4]` Chio y Freeman (2018) | ✅ Coincide |
| [5] | Geron, A. (2019). *Hands-On Machine Learning…* (2nd Ed.). O'Reilly | `[5]` Géron (2019) | ✅ Coincide |
| [6] | Goodfellow, I., Bengio, Y., & Courville, A. (2016). *Deep Learning*. MIT Press | `[6]` Goodfellow *et al.* (2016) | ✅ Coincide. **B4**: el localizador `[6, cap. 6]` del vault **no llegó al Word** |
| [7] | Murphy, K. P. (2012). *Machine Learning: A Probabilistic Perspective*. MIT Press | `[7]` Murphy (2012) | ✅ Coincide |
| [8] | «Computer Security : Principles and Practice» William Stallings | `[8]` Stallings y Brown, **5.ª ed., Pearson, 2023** | ⚠️ **B3**: faltan año, edición, coautor y editorial. El vault los tiene fijados por decisión de Francisco (2026-08-18) |
| [9] | `https://students.aiu.edu/.../j5V2a3_Computer_Security_Principles.pdf` | **NINGUNO** — el `[9]` del vault está **QUEMADO** desde el 2026-08-09, precisamente por ser esta copia | ⛔ **Duplica a `[8]`** (mismo libro de Stallings) y es una **copia no autorizada, nivel 3**. Es el único de los once sin equivalente en el vault. **B2**: fusionarla en `[8]`. **Si Francisco la elimina, el `[9]` del `.docx` queda quemado y NO se renumera** — la secuencia de este informe sigue siendo válida |
| [10] | `https://www.ccn-cert.cni.es/.../401-glosario_abreviaturas/…` | `[10]` CCN-STIC-401, *Glosario y Abreviaturas* | ✅ Misma fuente. **B2**: URL desnuda, falta el formato IEEE |
| [11] | `https://www.usenix.org/legacy/publications/library/proceedings/lisa99/roesch.html` | **`[26]`** Roesch, «Snort — Lightweight Intrusion Detection for Networks», LISA'99, pp. 229-238 | ⚠️ **ESTE ES EL DESAJUSTE DE T1, Y QUEDA RESUELTO ASÍ:** `[11]` del `.docx` = `[26]` del vault. **El `[11]` del vault es CRISP-DM (Chapman *et al.*, 2000) y NO va aquí.** CRISP-DM **no recibe número en el `.docx`** — ver §4. **B2**: URL desnuda |

> [!note] Cómo se ha verificado
> Contando marcadores contra disco, no de memoria: el `.docx` en limpio tiene hoy **exactamente 11 marcadores `[n]`** en todo el cuerpo (líneas 307-664 de `docx_limpio.md`), todos en el capítulo 1 y en §2.2.1, y su lista de bibliografía tiene **11 entradas**. Los cuatro «URLs desnudas» de **B2** son `[1]`, `[9]`, `[10]` y `[11]`.

---

## 2 · Tabla principal — un marcador por obra, en orden de aparición

**Regla de orden, declarada porque importa:** se recorre el **vault** en orden `01` → `06` → `Apéndices`, y dentro de cada nota por posición en el fichero. Cuando el fragmento del Anexo C o D **ya no existe en el vault** (lo borró alguna tanda de recorte) pero **sí existe en el `.docx`**, se ordena por su posición en el `.docx`; esos casos están marcados con **`(§ solo .docx)`**.

**Localizador:** solo se rellena donde IEEE lo exige (libros y documentos largos). `—` significa «no aplica»; **⚠️ significa «aplica y no se ha podido establecer con honestidad»** — y entonces no se inventa.

### Capítulo 1 · Introducción

| Nº .docx | Nº vault | Referencia completa | Sección | Fragmento literal para Ctrl+F | Localizador |
|---|---|---|---|---|---|
| **[1]** | [1] | INCIBE, balance de ciberseguridad 2024 | 1.1 Motivación | *ya puesto* | — |
| **[12]** | **[31]** | A. Khraisat, I. Gondal, P. Vamplew y J. Kamruzzaman, «Survey of intrusion detection systems: techniques, datasets and challenges», *Cybersecurity*, vol. 2, art. 20, 2019 | 1.1 Motivación · también 4.2, 5.4, 6.1 | «Se han creado algoritmos basados tanto en Machine Learning (ML) como en IA» | — |
| **[13]** | **[77]** | H. Hindy *et al.*, «Utilising Deep Learning Techniques for Effective Zero-Day Attack Detection», *Electronics*, vol. 9, n.º 10, art. 1684, 2020 | 1.1 Motivación · también 5.4 | «estos algoritmos han sido fundamentales para la detección de ataques desconocidos» | — |
| **[2]** | [2] | Anderson (1980) | 1.2 Preliminares · también 2.2.2 | *ya puesto* | — |
| **[3]** | [3] | Denning (1987) | 1.2 Preliminares · también 2.2.2, 2.2.4 ×2, 2.3.2 | *ya puesto* | — |
| **[11]** | **[26]** | Roesch, Snort (LISA'99) | 1.2 Preliminares ×2 · también 2.2.2 ×2, 2.2.4, 3.1 | *ya puesto* | — |
| **[14]** | **[25]** | K. Scarfone y P. Mell, *Guide to Intrusion Detection and Prevention Systems (IDPS)*, NIST SP 800-94, feb. 2007 | 1.2 Preliminares ×2 · también 2.2.2 ×2, 2.2.3, 2.2.4, 5.4 | «…el de detección basada en el estado» **y** «Evasión del IDS/NIDS – el atacante conoce el mecanismo de detección y lo esquiva» | — |

### Capítulo 2 · Marco Teórico — §2.1 Machine Learning

| Nº .docx | Nº vault | Referencia completa | Sección | Fragmento literal para Ctrl+F | Localizador |
|---|---|---|---|---|---|
| **[15]** | **[39]** | S. J. Russell y P. Norvig, *Artificial Intelligence: A Modern Approach*, 4.ª ed. Pearson, 2021 | 2.1.1 **(§ solo .docx)** | «los investigadores han perseguido enseñar a las computadoras a razonar» | **`[15, cap. 1]`** |
| **[16]** | **[79]** ⭐ | T. M. Mitchell, *Machine Learning*. McGraw-Hill, 1997 | 2.1.1 **(§ solo .docx)** | «algoritmos y procesos que «aprenden» en el sentido de que son capaces de generalizar datos» | **`[16, cap. 1]`** · ⚠️ página no establecida |
| **[4]** | [4] | Chio y Freeman (2018) | 2.1.1 · también 2.3.1, 2.3.2 | *ya puesto* | ⚠️ no establecido (sin acceso al texto) |
| **[5]** | [5] | Géron (2019) | 2.1.1 ×4, 2.1.2 ×3, 2.1.3 ×4, 2.1.4 ×4, 2.1.5 ×5, 4.3 ×2 | *ya puesto*; **T2.9**: falta localizador en el Word | `[5, cap. 1]` … `[5, cap. 9]` según uso |
| **[17]** | **[80]** ⭐ | I. T. Jolliffe, *Principal Component Analysis*, 2.ª ed. Springer, 2002 | 2.1.2 Tipos de ML | «Reducción de dimensionalidad y visualización» | **`[17, cap. 1]`** · ⚠️ página no establecida |
| **[18]** | **[81]** ⭐ | R. Agrawal y R. Srikant, «Fast Algorithms for Mining Association Rules», VLDB'94, pp. 487-499 | 2.1.2 Tipos de ML | «Reglas de asociación, que busca encontrar coocurrencias frecuentes» | — |
| **[19]** | **[82]** ⭐ | R. S. Sutton y A. G. Barto, *Reinforcement Learning: An Introduction*, 2.ª ed. MIT Press, 2018 | 2.1.2 Tipos de ML | «Un agente aprende por interacción con un entorno, guiado por recompensas y penalizaciones» | **`[19, cap. 1]`** · ⚠️ página no establecida |
| **[7]** | [7] | Murphy (2012) | 2.1.2 Tipos de ML | *ya puesto*; **T2.9**: falta localizador | ⚠️ no establecido |
| **[20]** | **[12]** | T. Hastie, R. Tibshirani y J. Friedman, *The Elements of Statistical Learning*, 2.ª ed. Springer, 2009 | 2.1.3 · también 2.1.4 ×5, 5.4 | «se limpian, transforman y dividen en subconjuntos de entrenamiento, validación y prueba» **(§ solo .docx)** y «un candidato algo peor pero mucho más estable puede ser preferible» | `[20, cap. 7]`, `[20, cap. 9]`, `[20, cap. 10]`, `[20, cap. 14]`, `[20, cap. 15]` según uso |
| **[21]** | **[13]** | R. Kohavi, «A Study of Cross-Validation and Bootstrap…», IJCAI'95, vol. 2, pp. 1137-1143 | 2.1.3 Ciclo de vida | «los valores que el algoritmo no aprende de los datos— mediante validación cruzada» | — |
| **[22]** | **[83]** ⭐ | L. Breiman, J. H. Friedman, R. A. Olshen y C. J. Stone, *Classification and Regression Trees*. Wadsworth, 1984 | 2.1.4 Algoritmos de ML | «Un árbol de decisión es una estructura jerárquica de nodos de decisión» | ⚠️ **no establecido** (ni capítulo ni página) |
| **[23]** | **[84]** ⭐ | T. G. Dietterich, «Ensemble Methods in Machine Learning», MCS 2000, LNCS 1857, pp. 1-15 | 2.1.4 | «Un conjunto (ensemble) combina varios clasificadores individuales» | — |
| **[24]** | **[85]** ⭐ | L. Breiman, «Random Forests», *Machine Learning*, vol. 45, n.º 1, pp. 5-32, 2001 | 2.1.4 · también 3.5, 4.3 | «El muestreo aleatorio decorrelaciona los árboles individuales y reduce la varianza» | — |
| **[25]** | **[86]** ⭐ | J. H. Friedman, «Greedy function approximation: A gradient boosting machine», *Annals of Statistics*, vol. 29, n.º 5, pp. 1189-1232, 2001 | 2.1.4 | «cada árbol nuevo se entrena para corregir los errores residuales del conjunto acumulado» | — |
| **[26]** | **[87]** ⭐ | G. Ke *et al.*, «LightGBM: A Highly Efficient Gradient Boosting Decision Tree», NIPS 2017, pp. 3146-3154 | 2.1.4 | «discretizando las características continuas en un número fijo de contenedores» | — |
| **[27]** | **[88]** ⭐ | T. M. Cover y P. E. Hart, «Nearest neighbor pattern classification», *IEEE Trans. Inf. Theory*, vol. 13, n.º 1, pp. 21-27, 1967 | 2.1.4 | «el ejemplo más conocido de aprendizaje perezoso» | — |
| **[28]** | **[30]** | V. Chandola, A. Banerjee y V. Kumar, «Anomaly detection: A survey», *ACM Computing Surveys*, vol. 41, n.º 3, art. 15, 2009 | 2.1.4 · también 2.2.3, 2.2.4 | «Estos algoritmos se denominan semisupervisados (one-class)» | — |
| **[29]** | **[73]** | F. T. Liu, K. M. Ting y Z.-H. Zhou, «Isolation Forest», ICDM 2008, pp. 413-422 | 2.1.4 ×2 · también 3.4 | «La longitud media del camino de aislamiento a través del conjunto de árboles» | — |
| **[30]** | **[89]** ⭐ | B. Schölkopf, J. C. Platt, J. Shawe-Taylor, A. J. Smola y R. C. Williamson, «Estimating the Support of a High-Dimensional Distribution», *Neural Computation*, vol. 13, n.º 7, pp. 1443-1471, 2001 | 2.1.4 · también 3.4, 4.4, 5.1 | «busca la frontera —en el espacio transformado por un núcleo (kernel), típicamente el radial (RBF)—» | — |
| **[31]** | **[75]** | M. M. Breunig, H.-P. Kriegel, R. T. Ng y J. Sander, «LOF: Identifying Density-Based Local Outliers», *ACM SIGMOD Record*, vol. 29, n.º 2, pp. 93-104, 2000 | 2.1.4 · también 3.4, 5.1 | «recibe una puntuación LOF elevada y se considera anómalo» | — |
| **[32]** | **[90]** ⭐ | D. E. Rumelhart, G. E. Hinton y R. J. Williams, «Learning representations by back-propagating errors», *Nature*, vol. 323, pp. 533-536, 1986 | 2.1.4 | «calculando los gradientes de todos los pesos mediante retropropagación» | — |
| **[6]** | [6] | Goodfellow, Bengio y Courville (2016) | 2.1.4 · también 3.4 | «un MLP empleado como autoencoder, que es el detector seleccionado para la etapa 1» | **`[6, cap. 14]`** aquí; `[6, cap. 6]` en el uso de retropropagación. **B4** |
| **[33]** | **[91]** ⭐ | T. Fawcett, «An introduction to ROC analysis», *Pattern Recognition Letters*, vol. 27, n.º 8, pp. 861-874, 2006 | 2.1.5 Métricas — **5 apariciones** | «La matriz de confusión es el punto de partida de toda métrica de clasificación» · «VP (verdadero positivo): un ataque correctamente señalado como ataque» · «Tasa de falsos positivos (FPR): de todo el tráfico normal» · «no produce directamente una etiqueta, sino una puntuación continua» · «Su resumen numérico habitual es el área bajo la curva (AUC-ROC)» | — |
| **[34]** | **[92]** ⭐ | M. Sokolova y G. Lapalme, «A systematic analysis of performance measures for classification tasks», *Information Processing & Management*, vol. 45, n.º 4, pp. 427-437, 2009 | 2.1.5 — **4 apariciones** | «la matriz pasa a ser de k x k, con k el número de clases» · «Exactitud (accuracy): la proporción de predicciones correctas sobre el total» · «se calculan primero por clase, con el esquema uno-contra-el-resto» · «Macro: se calcula la métrica de cada clase por separado y se promedian sin ponderar» | — |
| **[35]** | **[93]** ⭐ | D. M. W. Powers, «Evaluation: From Precision, Recall and F-Measure to ROC, Informedness, Markedness & Correlation», *J. Machine Learning Technologies*, vol. 2, n.º 1, pp. 37-63, 2011 | 2.1.5 — 2 apariciones | «Precisión: De todas las veces que el sistema levantó una alarma de ataque» · «Exhaustividad (recall): de todos los ataques reales, qué proporción detectó el sistema» | — · ⚠️ **NIVEL 2** — ver §5 |
| **[36]** | **[94]** ⭐ | C. J. van Rijsbergen, *Information Retrieval*, 2.ª ed. Butterworths, 1979 | 2.1.5 | «F1: la media armónica de precisión y recall» | ⚠️ **no establecido**; la medida E/F está en el cap. 7, pero la copia abierta no conserva la paginación original |
| **[37]** | **[19]** | H. He y E. A. Garcia, «Learning from Imbalanced Data», *IEEE TKDE*, vol. 21, n.º 9, pp. 1263-1284, 2009 | 2.1.5 · también 4.5, 6.1 | «un weighted alto, porque el peso n_i de la clase mayoritaria domina la suma» | — |
| **[38]** | **[95]** ⭐ | J. Davis y M. Goadrich, «The relationship between Precision-Recall and ROC curves», ICML'06, pp. 233-240 | 2.1.5 — 2 apariciones | «Enfrenta la precisión frente al recall en cada umbral, con su propia área bajo la curva» · «la curva ROC puede resultar engañosamente optimista» | — |

### Capítulo 2 · §2.2 Ciberseguridad

| Nº .docx | Nº vault | Referencia completa | Sección | Fragmento literal para Ctrl+F | Localizador |
|---|---|---|---|---|---|
| **[8]** | [8] | Stallings y Brown, 5.ª ed., Pearson, 2023 | 2.2.1 ×3 | *ya puesto*; **T2.9** pide localizador | `[8, cap. 1]` · ⚠️ página no establecida |
| **[10]** | [10] | CCN-STIC-401 | 2.2.1 | *ya puesto* | — |
| **[14]** | [25] | NIST SP 800-94 | 2.2.2 ×2, 2.2.3, 2.2.4 | «Una intrusión es cualquier acción, intencionada o no, que compromete la confidencialidad» · «monitoriza de forma continua los eventos que ocurren en un sistema o en una red» · «Sensor o captura. Obtiene el tráfico del segmento vigilado» · «Se diferencia en este punto entre HIDS (host-based IDS) y NIDS» · «es la modalidad que convierte al detector en un IPS» · «el momento del análisis: tiempo real… y diferido (offline)» | — |
| **[3]** | [3] | Denning (1987) | 2.2.2, 2.2.4 ×2 | «hereda de Denning (quien aportó el modelo IDES…)» · «La formulación original del enfoque se debe a Denning» | — |
| **[11]** | [26] | Roesch, Snort | 2.2.2 ×2, 2.2.4 | «entronca con la tradición de Snort» — ⚠️ **hoy el Word pone `[11]`… y acierta por casualidad**: `[11]` del `.docx` **es** Snort · «El conocimiento del analista de seguridad queda así codificado en una base de firmas» | — |
| **[39]** | **[96]** ⭐ | S. Axelsson, *Intrusion Detection Systems: A Survey and Taxonomy*, informe técnico 99-15, Chalmers, 2000 | 2.2.3 Taxonomía de los IDS | «La literatura no usa una taxonomía única sino varios ejes ortogonales» | — · ⚠️ **nivel 2**, y **no confundir con `[46]`** |
| **[40]** | **[29]** | P. García-Teodoro, J. Díaz-Verdejo, G. Maciá-Fernández y E. Vázquez, «Anomaly-based network intrusion detection: Techniques, systems and challenges», *Computers & Security*, vol. 28, n.º 1-2, pp. 18-28, 2009 | 2.2.3 · también 2.2.4, 6.1 | «Es la taxonomía más citada del área y la que enmarca el problema de este TFG» · «alta precisión sobre lo que cubre, alertas explicables y bajo volumen de falsas alarmas» | — |
| **[41]** | **[32]** | D. Barbará, J. Couto, S. Jajodia y N. Wu, «ADAM: a testbed for exploring the use of data mining in intrusion detection», *ACM SIGMOD Record*, vol. 30, n.º 4, pp. 15-24, 2001 | 2.2.3 · también 3.2, 3.6 | *ya puesto* | — |
| **[42]** | **[33]** | E. Tombini, H. Debar, L. Mé y M. Ducassé, «A serial combination of anomaly and misuse IDSes applied to HTTP traffic», ACSAC 2004, pp. 428-437 | 2.2.3 · también 3.2 y §2.2.4 | *ya puesto*; además es uno de los cinco de «existen trabajos que la adoptan, la invierten y la reformulan como conjunto paralelo» | — |
| **[43]** | **[34]** | T. H. Ptacek y T. N. Newsham, *Insertion, Evasion, and Denial of Service: Eluding Network Intrusion Detection*, informe técnico, Secure Networks Inc., 1998 | 2.2.3 | *ya puesto* | — · ⚠️ identidad inferida (ver su fila) |
| **[44]** | **[21]** | R. Sommer y V. Paxson, «Outside the Closed World: On Using Machine Learning for Network Intrusion Detection», IEEE S&P 2010, pp. 305-316 | 2.2.3 · también 2.2.4, 2.3.2, 3.2, 3.4, 5.4 | «mayor tasa de falsos positivos, alertas menos explicables y sensibilidad a la deriva (drift)» · «la captura del tráfico en la interfaz de red, el ensamblado de los paquetes en flujos» | — |
| **[45]** | **[35]** | Cisco / Snort Project, *Snort Users Manual*, sección «Writing Snort Rules» | 2.2.4 | *ya puesto* | — · ⚠️ falta fijar versión y fecha de consulta |
| **[46]** | **[24]** | S. Axelsson, «The base-rate fallacy and the difficulty of intrusion detection», *ACM TISSEC*, vol. 3, n.º 3, pp. 186-205, 2000 | 2.2.4 · también 2.3.3, 5.4 ×3 | *ya puesto* · ⚠️ **es el OTRO Axelsson**: no es `[39]` | — |
| **[47]** | **[68]** | S.-Y. Ji, B.-K. Jeong, S. Choi y D. H. Jeong, «A multi-level intrusion detection method for abnormal network behaviors», *J. Network and Computer Applications*, vol. 62, pp. 9-17, 2016 | 2.2.4 | *ya puesto*; uno de los tres de «existen trabajos que la adoptan, la invierten y la reformulan» | — |
| **[48]** | **[69]** | G. Kim, S. Lee y S. Kim, «A novel hybrid intrusion detection method integrating anomaly detection with misuse detection», *Expert Systems with Applications*, vol. 41, n.º 4, pp. 1690-1700, 2014 | 2.2.4 | *ya puesto* | — |
| **[49]** | **[70]** | A. Khraisat *et al.*, «Hybrid Intrusion Detection System Based on the Stacking Ensemble of C5 Decision Tree Classifier and One Class Support Vector Machine», *Electronics*, vol. 9, n.º 1, art. 173, 2020 | 2.2.4 | *ya puesto* · ⚠️ **distinta de `[12]`** (Khraisat 2019) | — |
| **[50]** | **[36]** | K. Kendall, *A Database of Computer Attacks for the Evaluation of Intrusion Detection Systems*, tesis de máster, MIT, 1999 | 2.2.5 · también 4.3, 4.5 | «Ejemplos en el dataset: neptune (inundación de segmentos SYN)…» · «…: nmap, portsweep, ipsweep, satan» · «…: guess_passwd (fuerza bruta…)» · «…: buffer_overflow, rootkit, loadmodule, perl» · «Es la firma canónica de un SYN flood tipo neptune» | — · ⚠️ identidad inferida |
| **[51]** | **[97]** ⭐ | R. Lippmann, J. W. Haines, D. J. Fried, J. Korba y K. Das, «Evaluating intrusion detection systems: the 1998 DARPA off-line intrusion detection evaluation», DISCEX'00, vol. 2, pp. 12-26 | 2.2.5 · también 4.2 | «procede de las campañas de evaluación… del MIT Lincoln Laboratory para DARPA (1998)» (junto a **[52]**) | — |
| **[52]** | **[23]** | M. Tavallaee, E. Bagheri, W. Lu y A. A. Ghorbani, «A Detailed Analysis of the KDD CUP 99 Data Set», CISDA 2009, pp. 1-6 | 2.2.5 · también 2.3.3, 3.1, 3.3, 4.2 ×5, 4.3, 5.1, 5.4 ×2 | «los 39 tipos de ataque específicos presentes en el corpus» · **sustituye los placeholders** `[ enlace bibliografía: Tavallaee 2009]` ×2 y `[CITA: Tavallaee 2009 + survey de datasets NIDS]` de §4.2 · **y sostiene** «El célebre "~99 % de accuracy" de la literatura no sobrevive al test oficial» — ver §5 | `[52, §I]` para el «~99 %»; `[52, §V]` para `#successfulPrediction` |
| **[53]** | **[38]** | B. E. Strom *et al.*, *MITRE ATT&CK®: Design and Philosophy*, informe técnico MITRE, 2018 (rev. 2020) | 2.2.5.3 | *ya puesto* | — · ⚠️ identidad inferida |
| **[54]** | **[22]** | J. McHugh, «Testing Intrusion Detection Systems: A Critique of the 1998 and 1999 DARPA…», *ACM TISSEC*, vol. 3, n.º 4, pp. 262-294, 2000 | 2.2.5 · también 2.3.2, 2.3.3, 4.2 | *ya puesto*; **sustituye el placeholder** `[ enlace bibliografía: McHugh 2000]` de §4.2 | — |

### Capítulo 2 · §2.3 Inteligencia Artificial

| Nº .docx | Nº vault | Referencia completa | Sección | Fragmento literal para Ctrl+F | Localizador |
|---|---|---|---|---|---|
| **[4]** | [4] | Chio y Freeman (2018) | 2.3.1, 2.3.2 | «designan conjuntos anidados: cada uno es un subconjunto estricto del anterior» · «Detección de intrusiones en red / Análisis de malware / Anti-phishing y anti-spam / UEBA» | ⚠️ **no establecido** — sin acceso al texto completo. Lo pide el Anexo C y **se marca, no se inventa** |
| **[55]** | **[98]** ⭐ | Y. LeCun, Y. Bengio y G. Hinton, «Deep learning», *Nature*, vol. 521, pp. 436-444, 2015 | 2.3.1 | «se habla de DL cuando la jerarquía de capas es lo bastante honda» | — |
| **[56]** | **[41]** | L. Grinsztajn, E. Oyallon y G. Varoquaux, «Why do tree-based models still outperform deep learning on tabular data?», NeurIPS 2022 D&B | 2.3.1 · también 3.5 | *ya puesto* | — |
| **[57]** | **[42]** | D. McElfresh *et al.*, «When Do Neural Nets Outperform Boosted Trees on Tabular Data?», NeurIPS 2023 D&B | 2.3.1 · también 3.5 ×2 | *ya puesto* | — |
| **[58]** | **[43]** | M. Sahami, S. Dumais, D. Heckerman y E. Horvitz, «A Bayesian Approach to Filtering Junk E-Mail», AAAI-98 Workshop, WS-98-05, pp. 55-62 | 2.3.2 | *ya puesto* | — · ⚠️ identidad inferida |
| **[59]** | **[61]** | W. J. Scheirer, A. de Rezende Rocha, A. Sapkota y T. E. Boult, «Toward Open Set Recognition», *IEEE TPAMI*, vol. 35, n.º 7, pp. 1757-1772, 2013 | 2.3.2 · también 3.3, 5.3, 6.1 | «no produce «ninguna de las anteriores»: produce la categoría conocida más parecida» | — |
| **[60]** | **[46]** | C. Szegedy *et al.*, «Intriguing properties of neural networks», ICLR 2014 | 2.3.2 | *ya puesto* | — · ⚠️ identidad inferida |
| **[61]** | **[47]** | I. J. Goodfellow, J. Shlens y C. Szegedy, «Explaining and Harnessing Adversarial Examples», ICLR 2015 | 2.3.2 | *ya puesto* | — · ⚠️ identidad inferida; el *venue* se apoya en el uso corriente, no en el registro |
| **[62]** | **[48]** | B. Biggio y F. Roli, «Wild patterns: Ten years after the rise of adversarial machine learning», *Pattern Recognition*, vol. 84, pp. 317-331, 2018 | 2.3.2 · también 2.3.3 | «equivale a suponer un adversario que no modifica su comportamiento» | — |
| **[63]** | **[49]** | A. Bendale y T. E. Boult, «Towards Open Set Deep Networks» (OpenMax), CVPR 2016, pp. 1563-1572 | 2.3.2 · también 5.3, 6.1 | *ya puesto* | — |
| **[64]** | **[50]** | N. Moustafa y J. Slay, «UNSW-NB15: a comprehensive data set for network intrusion detection systems», MilCIS 2015, pp. 1-6 | 2.3.2 | *ya puesto* | — |
| **[65]** | **[51]** | I. Sharafaldin, A. Habibi Lashkari y A. A. Ghorbani, «Toward Generating a New Intrusion Detection Dataset and Intrusion Traffic Characterization», ICISSP 2018, pp. 108-116 | 2.3.2 | *ya puesto* | — |
| **[66]** | **[18]** | D. Arp *et al.*, «Dos and Don'ts of Machine Learning in Computer Security», USENIX Security 2022, pp. 3971-3988 | 2.3.3 ×5 · también 3.1, 4.3, 5.4, 6.1 ×3 | «"each paper suffers from at least three pitfalls"» — **T2.8: cita textual hoy SIN marcador** · «El pitfall P9 de Arp et al., Lab-Only Evaluation» · «el pitfall P10, Inappropriate Threat Model» · «instanciar el caso, es decir, fijar un valor concreto en cada dimensión» · «selección de modelo sobre el conjunto de test, es decir data snooping» | `[66, §III]` para el catálogo de pitfalls; `[66, §II]` para la cita textual de prevalencia. ⚠️ **página exacta no establecida** |
| **[67]** | **[52]** | F. Pierazzi, F. Pendlebury, J. Cortellazzi y L. Cavallaro, «Intriguing Properties of Adversarial ML Attacks in the Problem Space», IEEE S&P 2020, pp. 1332-1349 | 2.3.3 · también 3.1, 6.1 | «produce puntos que ningún atacante real podría generar» | — · ⚠️ identidad inferida |
| **[68]** | **[53]** | C. Rudin, «Stop explaining black box machine learning models for high stakes decisions and use interpretable models instead», *Nature Machine Intelligence*, vol. 1, n.º 5, pp. 206-215, 2019 | 2.3.3 | *ya puesto* | — |
| **[69]** | **[54]** | C. Molnar, *Interpretable Machine Learning*, 2.ª ed., 2022 | 2.3.3 · también 3.5 ×2, 4.5 | *ya puesto* · «del árbol de decisión se extraen reglas legibles (mediante export_text)» · «las firmas deben poder leerse, auditarse y, llegado el caso, trasladarse a reglas» | ⚠️ **capítulo no establecido**; la edición **sí** está fijada (2.ª, 2022) |
| **[70]** | **[55]** | Reglamento (UE) 2016/679 (RGPD), DOUE L 119, pp. 1-88 | 2.3.3 ×2 | *ya puesto* | — |
| **[71]** | **[56]** | Reglamento (UE) 2024/1689 (Reglamento de IA), DOUE serie L, 12 jul. 2024 | 2.3.3 | *ya puesto* | — |
| **[72]** | **[57]** | Directiva (UE) 2022/2555 (NIS2), DOUE L 333, pp. 80-152 | 2.3.3 | *ya puesto* | — |

### Capítulo 3 · Diseño del sistema

| Nº .docx | Nº vault | Referencia completa | Sección | Fragmento literal para Ctrl+F | Localizador |
|---|---|---|---|---|---|
| **[52]** | [23] | Tavallaee *et al.* (2009) | 3.1, 3.3 | «las cuatro categorías canónicas del dataset NSL-KDD» · «al no re-particionar el test, D2 conserva los tipos de ataque que no aparecen» | — |
| **[11]** | [26] | Roesch, Snort | 3.1 | «siguiendo la línea de un IDS clásico basado en reglas» | — |
| **[73]** | **[17]** | S. Kapoor y A. Narayanan, «Leakage and the reproducibility crisis in machine-learning-based science», *Patterns*, vol. 4, n.º 9, art. 100804, 2023 | 3.3 · también 4.3, 5.0 | «se ajustan únicamente sobre el tráfico de entrenamiento (D1+D3)» | — · ⚠️ identidad inferida |
| **[74]** | **[60]** | M. Mitchell *et al.*, «Model Cards for Model Reporting», FAT\* '19, pp. 220-229 | 3.3 · también 5.0, A.3 | *ya puesto* · ⚠️ **NO es `[16]` del `.docx`** (Mitchell 1997, otro autor) | — |
| **[29]** | [73] | Liu, Ting y Zhou (2008) | 3.4.2 (tabla de candidatos, celda «NOCIÓN DE ANOMALÍA») | «Aísla las anomalías por particiones aleatorias» | — |
| **[30]** | [89] | Schölkopf *et al.* (2001) | 3.4.2 | «Aprende una frontera que encierra el comportamiento normal» | — |
| **[31]** | [75] | Breunig *et al.* (2000) | 3.4.2 | «Compara la densidad local de cada punto con la de sus vecinos» | — |
| **[6]** | [6] | Goodfellow *et al.* (2016) | 3.4.2 | «Error de reconstrucción: reconstruye mal lo que no se parece a lo normal» | **`[6, cap. 14]`** |
| **[24]** | [85] | Breiman (2001) | 3.5.2 (tabla de candidatos, celda «IDEA») | «Conjunto (ensemble) de árboles por bagging» | — |
| **[75]** | **[99]** ⭐ | T. Chen y C. Guestrin, «XGBoost: A Scalable Tree Boosting System», KDD'16, pp. 785-794 | 3.5.2 | «Conjunto por boosting (rendimiento tipo XGBoost)» | — |
| **[76]** | **[71]** | R. Shwartz-Ziv y A. Armon, «Tabular data: Deep learning is not all you need», *Information Fusion*, vol. 81, pp. 84-90, 2022 | 3.5 | *ya puesto* | — · ⚠️ solo resumen (muro de pago) |
| **[77]** | **[72]** | N. Hollmann *et al.*, «Accurate predictions on small data with a tabular foundation model» (TabPFN v2), *Nature*, vol. 637, pp. 319-326, 2025 | 3.5 | *ya puesto* | — |
| **[78]** | **[100]** ⭐ | N. V. Chawla, K. W. Bowyer, L. O. Hall y W. P. Kegelmeyer, «SMOTE: Synthetic Minority Over-sampling Technique», *JAIR*, vol. 16, pp. 321-357, 2002 | 3.5.4 · también 4.3, 6.1 | «Comparar el sobremuestreo sintético (SMOTE) frente al reponderado de clases» | — |

### Capítulo 4 · Implementación del sistema

| Nº .docx | Nº vault | Referencia completa | Sección | Fragmento literal para Ctrl+F | Localizador |
|---|---|---|---|---|---|
| **[79]** | **[101]** ⭐ | F. Pedregosa *et al.*, «Scikit-learn: Machine Learning in Python», *JMLR*, vol. 12, pp. 2825-2830, 2011 | 4.1.3, tabla de librerías | «Núcleo de ML: preprocesamiento (MinMaxScaler, LabelEncoder)» | — |
| **[80]** | **[102]** ⭐ | G. Lemaître, F. Nogueira y C. K. Aridas, «Imbalanced-learn: A Python Toolbox…», *JMLR*, vol. 18, n.º 17, pp. 1-5, 2017 | 4.1.3 | «Tratamiento del desbalance de clases: SMOTE dentro de un Pipeline» | — |
| **[81]** | **[103]** ⭐ | F. J. Massey Jr., «The Kolmogorov-Smirnov Test for Goodness of Fit», *JASA*, vol. 46, n.º 253, pp. 68-78, 1951 | 4.1.3 | «test de Kolmogórov-Smirnov para el análisis de drift» | — |
| **[82]** | **[104]** ⭐ | J. D. Hunter, «Matplotlib: A 2D Graphics Environment», *CiSE*, vol. 9, n.º 3, pp. 90-95, 2007 | 4.1.3 | fila «Matplotlib» de la tabla | — |
| **[83]** | **[105]** ⭐ | M. L. Waskom, «seaborn: statistical data visualization», *JOSS*, vol. 6, n.º 60, art. 3021, 2021 | 4.1.3 | fila «Seaborn» | — |
| **[84]** | **[106]** ⭐ | C. R. Harris *et al.*, «Array programming with NumPy», *Nature*, vol. 585, pp. 357-362, 2020 | 4.1.3 | fila «NumPy» | — |
| **[85]** | **[107]** ⭐ | W. McKinney, «Data Structures for Statistical Computing in Python», SciPy 2010, pp. 56-61 | 4.1.3 | fila «Pandas» | — |
| **[86]** | **[58]** | *KDD Cup 1999 Data*, The UCI KDD Archive, UC Irvine, 1999 | 4.2 | **sustituye el placeholder entero** `[enlace bibliografía: KDD Cup 99]`, junto a **[51]** | — |
| **[51]** | [97] | Lippmann *et al.* (2000) | 4.2 | mismo placeholder | — |
| **[52]** | [23] | Tavallaee *et al.* (2009) | 4.2 ×5 | **sustituye** `[ enlace bibliografía: Tavallaee 2009]` ×2 y la mitad de `[CITA: Tavallaee 2009 + survey…]` · «etiquetaron cada registro de KDDTest+ con un valor de #successfulPrediction» | `[52, §V]` |
| **[54]** | [22] | McHugh (2000) | 4.2 | **sustituye** `[ enlace bibliografía: McHugh 2000]` | — |
| **[87]** | **[59]** | W. Lee y S. J. Stolfo, «A framework for constructing features and models for intrusion detection systems», *ACM TISSEC*, vol. 3, n.º 4, pp. 227-261, 2000 | 4.2 · también A.1 | «Las 41 características se agrupan en tres familias» · «Huella en el tráfico» (las cuatro apariciones: `serror_rate`, `count`, `hot`, `root_shell`) | — |
| **[12]** | [31] | Khraisat *et al.* (2019) | 4.2 | *ya puesto* | — |
| **[88]** | **[74]** | P. Goldschmidt y D. Chudá, «Network intrusion datasets: A survey, limitations, and recommendations», *Computers & Security*, vol. 156, art. 104510, 2025 | 4.2 · también 5.4 ×3 | *ya puesto*; completa `[CITA: Tavallaee 2009 + survey de datasets NIDS]` | `[88, §5.5.4]` y `[88, §5.4]` según uso |
| **[50]** | [36] | Kendall (1999) | 4.3, 4.5 | «una de las cinco categorías canónicas de la literatura de NSL-KDD» (junto a **[52]**) · «Es la firma canónica de un SYN flood tipo neptune» | — |
| **[78]** | [100] | Chawla *et al.* (2002) | 4.3 | «las muestras sintéticas se interpolan a partir de vecinos reales» (junto a **[73]**) | — |
| **[24]** | [85] | Breiman (2001) | 4.3 | «se entrena un RandomForestClassifier (100 árboles, class_weight='balanced', semilla 42)» | — |
| **[5]** | [5] | Géron (2019) | 4.3 ×2 | «desde tasas en [0,1] hasta contadores de bytes con valores de cientos de millones» · «Se codifican mediante One-Hot Encoding (pd.get_dummies)» | `[5, cap. 2]` |
| **[30]** | [89] | Schölkopf *et al.* (2001) | 4.4 | «Su coste de entrenamiento es O(n²) en memoria y tiempo» | — |
| **[89]** | **[14]** | scikit-learn, «`sklearn.model_selection.GridSearchCV`» (documentación oficial) | 4.4 · también A.3 | «LocalOutlierFactor se instancia con novelty=True» | — · ⚠️ **la sede exacta pide la página de `LocalOutlierFactor`, no la de `GridSearchCV`**: la entrada `[14]` cubre la documentación oficial de scikit-learn como obra, pero **si Francisco quiere la página concreta, hay que fijarla en Zotero**. Se marca, no se inventa |
| **[90]** | **[108]** ⭐ | M. Sakurada y T. Yairi, «Anomaly Detection Using Autoencoders with Nonlinear Dimensionality Reduction», MLSDA 2014, pp. 4-11 | 4.4 | «las conexiones anómalas se reconstruyen mal y producen un MSE alto» | — |
| **[37]** | [19] | He y Garcia (2009) | 4.5 | «un clasificador que nunca predijera u2r conservaría un accuracy superior al 99,9 %» | — |
| **[69]** | [54] | Molnar (2022) | 4.5 | «las firmas deben poder leerse, auditarse y, llegado el caso, trasladarse a reglas» | ⚠️ capítulo no establecido |

### Capítulo 5 · Evaluación

| Nº .docx | Nº vault | Referencia completa | Sección | Fragmento literal para Ctrl+F | Localizador |
|---|---|---|---|---|---|
| **[52]** | [23] | Tavallaee *et al.* (2009) | 5.1, 5.4 ×2 | «refleja el desplazamiento distribucional D3→D2 propio del NSL-KDD» · **y el sostén de** «El célebre "~99 % de accuracy" de la literatura no sobrevive al test oficial» | `[52, §I]` |
| **[91]** | **[78]** | A. Storkey, «When Training and Test Sets Are Different: Characterizing Learning Transfer», cap. 1, en *Dataset Shift in Machine Learning*, MIT Press, 2009, pp. 3-28 | 5.1 | *ya puesto* | **`[91, pp. 3-28]`** · ⚠️ punto exacto no establecido |
| **[30]** | [89] | Schölkopf *et al.* (2001) | 5.1 | «su coste de entrenamiento O(n²) hace inviable ajustarlo con el conjunto completo» | — |
| **[31]** | [75] | Breunig *et al.* (2000) | 5.1 | «Su noción de anomalía basada en densidad local no captura bien la separación» | — |
| **[92]** | **[109]** ⭐ | J. Demšar, «Statistical Comparisons of Classifiers over Multiple Data Sets», *JMLR*, vol. 7, pp. 1-30, 2006 | 5.2.4 | «Comparación pareada (semilla a semilla)» | — |
| **[93]** | **[110]** ⭐ | T. G. Dietterich, «Approximate Statistical Tests for Comparing Supervised Classification Learning Algorithms», *Neural Computation*, vol. 10, n.º 7, pp. 1895-1923, 1998 | 5.2.4 | mismo fragmento; **complementa a [92]**, no lo sustituye | — |
| **[59]** | [61] | Scheirer *et al.* (2013) | 5.3 | *ya puesto* | — |
| **[63]** | [49] | Bendale y Boult (2016) | 5.3 | *ya puesto* | — |
| **[94]** | **[16]** | C. K. Chow, «On optimum recognition error and reject tradeoff», *IEEE Trans. Information Theory*, vol. 16, n.º 1, pp. 41-46, 1970 | 5.3 | *ya puesto* · ⚠️ el Anexo D la anclaba también en §3.5.4 («estimadas fuera de muestra…»), **fragmento que no existe hoy ni en el vault ni en el `.docx`** — contado contra disco. Por eso la primera aparición es §5.3 | — |
| **[66]** | [18] | Arp *et al.* (2022) | 5.4 | *ya puesto* | `[66, §III]` |
| **[88]** | [74] | Goldschmidt y Chudá (2025) | 5.4 ×3 | *ya puesto* | `[88, §5.4]` |
| **[13]** | [77] | Hindy *et al.* (2020) | 5.4 | *ya puesto* — ⚠️ **se cita por el método, NO por su 89-99 %** (decisión D7 de [[benchmark-comparativo-nsl-kdd]]) | — |
| **[46]** | [24] | Axelsson, *base-rate fallacy* (2000) | 5.4 ×3 | *ya puesto* | — |
| **[14]** | [25] | NIST SP 800-94 | 5.4 ×2 | *ya puesto* | — |
| **[12]** | [31] | Khraisat *et al.* (2019) | 5.4 | «el patrón dominante en la literatura sobre NSL-KDD: un RandomForest monolítico» (junto a **[52]**) — ver §5 | — |
| **[20]** | [12] | Hastie *et al.* (2009) | 5.4 | «el sobreajuste es invisible en validación cruzada» | **`[20, cap. 15]`** |
| **[44]** | [21] | Sommer y Paxson (2010) | 5.4 | «la captura del tráfico en la interfaz de red, el ensamblado de los paquetes en flujos» | — |

### Capítulo 6 · Conclusiones (solo §6.1; §6.2 está bloqueada)

| Nº .docx | Nº vault | Referencia completa | Sección | Fragmento literal para Ctrl+F | Localizador |
|---|---|---|---|---|---|
| **[66]** | [18] | Arp *et al.* (2022) | 6.1 ×3 | *ya puesto* | `[66, §III]` |
| **[67]** | [52] | Pierazzi *et al.* (2020) | 6.1 | *ya puesto* | — |
| **[62]** | [48] | Biggio y Roli (2018) | 6.1 | «equivale a suponer un adversario que no modifica su comportamiento» | — |
| **[95]** | **[20]** | J. Pineau *et al.*, «Improving Reproducibility in Machine Learning Research…», *JMLR*, vol. 22, n.º 164, pp. 1-20, 2021 | 6.1 | *ya puesto* · **primera aparición en una sede que existe**: sus otros usos están en §5.0 y `A.3`, ambas bloqueadas | — |
| **[59]** | [61] | Scheirer *et al.* (2013) | 6.1 | «el clasificador de firmas, cerrado, tiende a asignar con confianza etiquetas conocidas» (alternativa: **[63]**) | — |
| **[12]** | [31] | Khraisat *et al.* (2019) | 6.1 | «frente al enfoque supervisado que domina la literatura sobre el NSL-KDD» — **mismo sostén que en §5.4** | — |
| **[40]** | [29] | García-Teodoro *et al.* (2009) | 6.1 | «firmas y anomalías no compiten, sino que se complementan» | — |
| **[52]** | [23] | Tavallaee *et al.* (2009) | 6.1 | «debido al desplazamiento distribucional entre el tráfico normal de entrenamiento y el de test» | — |
| **[37]** | [19] | He y Garcia (2009) | 6.1 | «ningún algoritmo ni técnica de balanceo (SMOTE, class_weight) logra un rendimiento sólido» (junto a **[78]**) | — |
| **[78]** | [100] | Chawla *et al.* (2002) | 6.1 | mismo fragmento | — |

### Apéndice A

| Nº .docx | Nº vault | Referencia completa | Sección | Fragmento literal para Ctrl+F | Localizador |
|---|---|---|---|---|---|
| **[87]** | [59] | Lee y Stolfo (2000) | A.1 | «Huella en el tráfico» — **las cuatro apariciones** (`serror_rate`, `count`, `hot`, `root_shell`) | — |

⭐ = **alta nueva** de este pase en `Bibliografía.md`.

---

## 3 · La lista final, lista para pegar en Word

`[1]`-`[11]` **no se tocan**: van tal como están hoy, con las correcciones de **B2** y **B3** si Francisco las hace. De `[12]` en adelante:

```
[12]  A. Khraisat, I. Gondal, P. Vamplew y J. Kamruzzaman, «Survey of intrusion detection systems: techniques, datasets and challenges», Cybersecurity, vol. 2, art. 20, 2019.
[13]  H. Hindy, R. Atkinson, C. Tachtatzis, J.-N. Colin, E. Bayne y X. Bellekens, «Utilising Deep Learning Techniques for Effective Zero-Day Attack Detection», Electronics, vol. 9, n.º 10, art. 1684, 2020.
[14]  K. Scarfone y P. Mell, Guide to Intrusion Detection and Prevention Systems (IDPS), NIST Special Publication 800-94. Gaithersburg, MD: NIST, feb. 2007.
[15]  S. J. Russell y P. Norvig, Artificial Intelligence: A Modern Approach, 4.ª ed. Hoboken, NJ: Pearson, 2021.
[16]  T. M. Mitchell, Machine Learning. Nueva York: McGraw-Hill, 1997.
[17]  I. T. Jolliffe, Principal Component Analysis, 2.ª ed. Nueva York: Springer, 2002.
[18]  R. Agrawal y R. Srikant, «Fast Algorithms for Mining Association Rules», en Proc. 20th Int. Conf. on Very Large Data Bases (VLDB'94), Santiago de Chile, 1994, pp. 487-499.
[19]  R. S. Sutton y A. G. Barto, Reinforcement Learning: An Introduction, 2.ª ed. Cambridge, MA: MIT Press, 2018.
[20]  T. Hastie, R. Tibshirani y J. Friedman, The Elements of Statistical Learning: Data Mining, Inference, and Prediction, 2.ª ed. Nueva York: Springer, 2009.
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
[34]  M. Sokolova y G. Lapalme, «A systematic analysis of performance measures for classification tasks», Information Processing & Management, vol. 45, n.º 4, pp. 427-437, 2009.
[35]  D. M. W. Powers, «Evaluation: From Precision, Recall and F-Measure to ROC, Informedness, Markedness & Correlation», Journal of Machine Learning Technologies, vol. 2, n.º 1, pp. 37-63, 2011.
[36]  C. J. van Rijsbergen, Information Retrieval, 2.ª ed. Londres: Butterworths, 1979.
[37]  H. He y E. A. Garcia, «Learning from Imbalanced Data», IEEE Trans. Knowledge and Data Engineering, vol. 21, n.º 9, pp. 1263-1284, 2009.
[38]  J. Davis y M. Goadrich, «The relationship between Precision-Recall and ROC curves», en Proc. 23rd Int. Conf. on Machine Learning (ICML'06), ACM, 2006, pp. 233-240.
[39]  S. Axelsson, Intrusion Detection Systems: A Survey and Taxonomy, informe técnico 99-15. Göteborg: Chalmers University of Technology, mar. 2000.
[40]  P. García-Teodoro, J. Díaz-Verdejo, G. Maciá-Fernández y E. Vázquez, «Anomaly-based network intrusion detection: Techniques, systems and challenges», Computers & Security, vol. 28, n.º 1-2, pp. 18-28, 2009.
[41]  D. Barbará, J. Couto, S. Jajodia y N. Wu, «ADAM: a testbed for exploring the use of data mining in intrusion detection», ACM SIGMOD Record, vol. 30, n.º 4, pp. 15-24, 2001.
[42]  E. Tombini, H. Debar, L. Mé y M. Ducassé, «A serial combination of anomaly and misuse IDSes applied to HTTP traffic», en 20th Annual Computer Security Applications Conf. (ACSAC), IEEE, 2004, pp. 428-437.
[43]  T. H. Ptacek y T. N. Newsham, Insertion, Evasion, and Denial of Service: Eluding Network Intrusion Detection, informe técnico. Calgary: Secure Networks Inc., ene. 1998.
[44]  R. Sommer y V. Paxson, «Outside the Closed World: On Using Machine Learning for Network Intrusion Detection», en 2010 IEEE Symp. on Security and Privacy, Oakland, CA, 2010, pp. 305-316.
[45]  Cisco / Snort Project, Snort Users Manual, sección «Writing Snort Rules». Documentación oficial.
[46]  S. Axelsson, «The base-rate fallacy and the difficulty of intrusion detection», ACM Trans. Information and System Security, vol. 3, n.º 3, pp. 186-205, 2000.
[47]  S.-Y. Ji, B.-K. Jeong, S. Choi y D. H. Jeong, «A multi-level intrusion detection method for abnormal network behaviors», Journal of Network and Computer Applications, vol. 62, pp. 9-17, 2016.
[48]  G. Kim, S. Lee y S. Kim, «A novel hybrid intrusion detection method integrating anomaly detection with misuse detection», Expert Systems with Applications, vol. 41, n.º 4, pp. 1690-1700, 2014.
[49]  A. Khraisat, I. Gondal, P. Vamplew, J. Kamruzzaman y A. Alazab, «Hybrid Intrusion Detection System Based on the Stacking Ensemble of C5 Decision Tree Classifier and One Class Support Vector Machine», Electronics, vol. 9, n.º 1, art. 173, 2020.
[50]  K. Kendall, A Database of Computer Attacks for the Evaluation of Intrusion Detection Systems, tesis de máster, Massachusetts Institute of Technology, jun. 1999.
[51]  R. Lippmann, J. W. Haines, D. J. Fried, J. Korba y K. Das, «Evaluating intrusion detection systems: the 1998 DARPA off-line intrusion detection evaluation», en Proc. DISCEX'00, vol. 2, IEEE, 2000, pp. 12-26.
[52]  M. Tavallaee, E. Bagheri, W. Lu y A. A. Ghorbani, «A Detailed Analysis of the KDD CUP 99 Data Set», en Proc. 2nd IEEE Symp. on Computational Intelligence for Security and Defense Applications (CISDA), Ottawa, 2009, pp. 1-6.
[53]  B. E. Strom, A. Applebaum, D. P. Miller, K. C. Nickels, A. G. Pennington y C. B. Thomas, MITRE ATT&CK®: Design and Philosophy, informe técnico MITRE, jul. 2018 (rev. mar. 2020).
[54]  J. McHugh, «Testing Intrusion Detection Systems: A Critique of the 1998 and 1999 DARPA Intrusion Detection System Evaluations as Performed by Lincoln Laboratory», ACM Trans. Information and System Security, vol. 3, n.º 4, pp. 262-294, 2000.
[55]  Y. LeCun, Y. Bengio y G. Hinton, «Deep learning», Nature, vol. 521, n.º 7553, pp. 436-444, 2015.
[56]  L. Grinsztajn, E. Oyallon y G. Varoquaux, «Why do tree-based models still outperform deep learning on tabular data?», en Advances in NeurIPS 35, Datasets and Benchmarks Track, 2022.
[57]  D. McElfresh, S. Khandagale, J. Valverde, V. Prasad C., G. Ramakrishnan, M. Goldblum y C. White, «When Do Neural Nets Outperform Boosted Trees on Tabular Data?», en Advances in NeurIPS 36, Datasets and Benchmarks Track, 2023.
[58]  M. Sahami, S. Dumais, D. Heckerman y E. Horvitz, «A Bayesian Approach to Filtering Junk E-Mail», en Learning for Text Categorization: Papers from the 1998 AAAI Workshop, AAAI Technical Report WS-98-05, 1998, pp. 55-62.
[59]  W. J. Scheirer, A. de Rezende Rocha, A. Sapkota y T. E. Boult, «Toward Open Set Recognition», IEEE Trans. Pattern Analysis and Machine Intelligence, vol. 35, n.º 7, pp. 1757-1772, 2013.
[60]  C. Szegedy, W. Zaremba, I. Sutskever, J. Bruna, D. Erhan, I. Goodfellow y R. Fergus, «Intriguing properties of neural networks», en 2nd Int. Conf. on Learning Representations (ICLR 2014), 2014.
[61]  I. J. Goodfellow, J. Shlens y C. Szegedy, «Explaining and Harnessing Adversarial Examples», en 3rd Int. Conf. on Learning Representations (ICLR 2015), 2015.
[62]  B. Biggio y F. Roli, «Wild patterns: Ten years after the rise of adversarial machine learning», Pattern Recognition, vol. 84, pp. 317-331, 2018.
[63]  A. Bendale y T. E. Boult, «Towards Open Set Deep Networks», en 2016 IEEE Conf. on Computer Vision and Pattern Recognition (CVPR), 2016, pp. 1563-1572.
[64]  N. Moustafa y J. Slay, «UNSW-NB15: a comprehensive data set for network intrusion detection systems», en 2015 Military Communications and Information Systems Conf. (MilCIS), Canberra, 2015, pp. 1-6.
[65]  I. Sharafaldin, A. Habibi Lashkari y A. A. Ghorbani, «Toward Generating a New Intrusion Detection Dataset and Intrusion Traffic Characterization», en Proc. 4th Int. Conf. on Information Systems Security and Privacy (ICISSP), Funchal, 2018, pp. 108-116.
[66]  D. Arp, E. Quiring, F. Pendlebury, A. Warnecke, F. Pierazzi, C. Wressnegger, L. Cavallaro y K. Rieck, «Dos and Don'ts of Machine Learning in Computer Security», en 31st USENIX Security Symposium, 2022, pp. 3971-3988.
[67]  F. Pierazzi, F. Pendlebury, J. Cortellazzi y L. Cavallaro, «Intriguing Properties of Adversarial ML Attacks in the Problem Space», en 2020 IEEE Symp. on Security and Privacy, 2020, pp. 1332-1349.
[68]  C. Rudin, «Stop explaining black box machine learning models for high stakes decisions and use interpretable models instead», Nature Machine Intelligence, vol. 1, n.º 5, pp. 206-215, 2019.
[69]  C. Molnar, Interpretable Machine Learning: A Guide for Making Black Box Models Explainable, 2.ª ed. Edición del autor, 2022.
[70]  Parlamento Europeo y Consejo de la UE, Reglamento (UE) 2016/679 (RGPD), DOUE L 119, 4 de mayo de 2016, pp. 1-88.
[71]  Parlamento Europeo y Consejo de la UE, Reglamento (UE) 2024/1689 (Reglamento de Inteligencia Artificial), DOUE serie L, 12 de julio de 2024.
[72]  Parlamento Europeo y Consejo de la UE, Directiva (UE) 2022/2555 (NIS2), DOUE L 333, 27 de diciembre de 2022, pp. 80-152.
[73]  S. Kapoor y A. Narayanan, «Leakage and the reproducibility crisis in machine-learning-based science», Patterns, vol. 4, n.º 9, art. 100804, 2023.
[74]  M. Mitchell, S. Wu, A. Zaldivar, P. Barnes, L. Vasserman, B. Hutchinson, E. Spitzer, I. D. Raji y T. Gebru, «Model Cards for Model Reporting», en Proc. Conf. on Fairness, Accountability, and Transparency (FAT* '19), ACM, 2019, pp. 220-229.
[75]  T. Chen y C. Guestrin, «XGBoost: A Scalable Tree Boosting System», en Proc. 22nd ACM SIGKDD Int. Conf. on Knowledge Discovery and Data Mining (KDD'16), ACM, 2016, pp. 785-794.
[76]  R. Shwartz-Ziv y A. Armon, «Tabular data: Deep learning is not all you need», Information Fusion, vol. 81, pp. 84-90, 2022.
[77]  N. Hollmann, S. Müller, L. Purucker, A. Krishnakumar, M. Körfer, S. B. Hoo, R. T. Schirrmeister y F. Hutter, «Accurate predictions on small data with a tabular foundation model», Nature, vol. 637, n.º 8045, pp. 319-326, 2025.
[78]  N. V. Chawla, K. W. Bowyer, L. O. Hall y W. P. Kegelmeyer, «SMOTE: Synthetic Minority Over-sampling Technique», Journal of Artificial Intelligence Research, vol. 16, pp. 321-357, 2002.
[79]  F. Pedregosa, G. Varoquaux, A. Gramfort, V. Michel, B. Thirion, O. Grisel et al., «Scikit-learn: Machine Learning in Python», Journal of Machine Learning Research, vol. 12, pp. 2825-2830, 2011.
[80]  G. Lemaître, F. Nogueira y C. K. Aridas, «Imbalanced-learn: A Python Toolbox to Tackle the Curse of Imbalanced Datasets in Machine Learning», Journal of Machine Learning Research, vol. 18, n.º 17, pp. 1-5, 2017.
[81]  F. J. Massey Jr., «The Kolmogorov-Smirnov Test for Goodness of Fit», Journal of the American Statistical Association, vol. 46, n.º 253, pp. 68-78, 1951.
[82]  J. D. Hunter, «Matplotlib: A 2D Graphics Environment», Computing in Science & Engineering, vol. 9, n.º 3, pp. 90-95, 2007.
[83]  M. L. Waskom, «seaborn: statistical data visualization», Journal of Open Source Software, vol. 6, n.º 60, art. 3021, 2021.
[84]  C. R. Harris, K. J. Millman, S. J. van der Walt et al., «Array programming with NumPy», Nature, vol. 585, n.º 7825, pp. 357-362, 2020.
[85]  W. McKinney, «Data Structures for Statistical Computing in Python», en Proc. 9th Python in Science Conf. (SciPy 2010), Austin, TX, 2010, pp. 56-61.
[86]  KDD Cup 1999 Data, The UCI KDD Archive, Information and Computer Science, University of California, Irvine, 1999.
[87]  W. Lee y S. J. Stolfo, «A framework for constructing features and models for intrusion detection systems», ACM Trans. Information and System Security, vol. 3, n.º 4, pp. 227-261, 2000.
[88]  P. Goldschmidt y D. Chudá, «Network intrusion datasets: A survey, limitations, and recommendations», Computers & Security, vol. 156, art. 104510, 2025.
[89]  scikit-learn, documentación oficial de la API (módulo sklearn.model_selection / sklearn.neighbors).
[90]  M. Sakurada y T. Yairi, «Anomaly Detection Using Autoencoders with Nonlinear Dimensionality Reduction», en Proc. MLSDA 2014 2nd Workshop on Machine Learning for Sensory Data Analysis, ACM, 2014, pp. 4-11.
[91]  A. Storkey, «When Training and Test Sets Are Different: Characterizing Learning Transfer», cap. 1, en Dataset Shift in Machine Learning, J. Quiñonero-Candela, M. Sugiyama, A. Schwaighofer y N. D. Lawrence, Eds. Cambridge, MA: MIT Press, 2009, pp. 3-28.
[92]  J. Demšar, «Statistical Comparisons of Classifiers over Multiple Data Sets», Journal of Machine Learning Research, vol. 7, pp. 1-30, 2006.
[93]  T. G. Dietterich, «Approximate Statistical Tests for Comparing Supervised Classification Learning Algorithms», Neural Computation, vol. 10, n.º 7, pp. 1895-1923, 1998.
[94]  C. K. Chow, «On optimum recognition error and reject tradeoff», IEEE Trans. Information Theory, vol. 16, n.º 1, pp. 41-46, 1970.
[95]  J. Pineau, P. Vincent-Lamarre, K. Sinha, V. Larivière, A. Beygelzimer, F. d'Alché-Buc, E. Fox y H. Larochelle, «Improving Reproducibility in Machine Learning Research (A Report from the NeurIPS 2019 Reproducibility Program)», Journal of Machine Learning Research, vol. 22, n.º 164, pp. 1-20, 2021.
```

> [!note] Los DOI, para el pase por Zotero
> No se han metido en el bloque de arriba para no ensuciar el pegado, pero están **todos** en la columna «DOI / URL estable» de `Bibliografía.md`, entrada por entrada. Los de las 32 altas se dieron de alta con el DOI resuelto o con la URL oficial del editor.

---

## 4 · Bloqueadas: la sede no existe aún

Estas citas **no se pueden colocar hoy** y **no consumen número** en la secuencia del `.docx`. Si Francisco volca la sede, hay que darles número **por detrás del `[95]`**, no intercalarlo: renumerar rompería lo ya pegado.

### 4.1 · Sedes que el encargo ya daba por bloqueadas

| Sede | Estado en el `.docx` | Citas afectadas | Consecuencia |
|---|---|---|---|
| **§6.2 Líneas futuras** | **VACÍA** — solo el título (confirmado: el ToC la lista en la p. 111 y el cuerpo tiene `## Líneas futuras` sin nada debajo) | `[62]` Erickson (TabArena), `[63]` Micci-Barreca, `[64]` Pargent *et al.*, `[65]` Hwang *et al.*, `[66]` Pendlebury (TESSERACT), `[67]` Behrouz *et al.* (Nested Learning) — **numeración del vault** | **6 obras del vault se quedan sin número en el `.docx`.** Todas están redactadas en la nota `6.2` del vault: entran en bloque el día que se volque (tarea **6.1** de Kiko) |
| **§5.0 y sus subsecciones** | **NO EXISTE** como sección: el capítulo 5 del `.docx` arranca en §5.1 (ToC verificado) | usos de `[17]`, `[18]`, `[20]`, `[23]`, `[25]`, `[60]` | **Ninguna obra se pierde**: las seis tienen otra sede viva y ya están numeradas (`[73]`, `[66]`, `[95]`, `[52]`, `[14]`, `[74]` del `.docx`). Es la tarea **5.9** |
| **Apéndice A.2 «Métricas de desempeño»** | **solo el título** en el `.docx`; **el vault SÍ la tiene redactada** | usos de `[5]` (`[5, cap. 2]`, `[5, cap. 9]`) | Ninguna obra se pierde: `[5]` ya es `[5]` del `.docx`. Es la tarea **A8** |
| **Estado del arte (tareas 2.10 y 2.11)** | **NO EXISTE** — es la carencia estructural que Kiko marca como la más grave | ninguna adicional: los cinco híbridos que lo poblarían —`[33]`, `[65]`, `[68]`, `[69]`, `[70]` del vault— ya tienen número (`[42]`, **bloqueada**, `[47]`, `[48]`, `[49]`) **salvo `[65]` Hwang**, cuya única cita viva está en `6.2` | Si se escribe el estado del arte, **`[65]` Hwang entra y necesitaría el siguiente número libre** |

### 4.2 · Dos sedes más que TAMPOCO existen en el `.docx` de hoy — halladas al contar contra disco

No estaban en la lista del encargo. **Se señalan, no se silencian**, porque cada una se lleva por delante entradas que nadie más cita:

| Sede | Estado | Citas afectadas | Consecuencia |
|---|---|---|---|
| **§2.1.6 «Metodologías y buenas prácticas»** | **NO EXISTE en el `.docx`.** El ToC del capítulo 2 salta de §2.1.5 «Métricas de evaluación de modelos» a §2.2 «Ciberseguridad». En el vault la nota existe y **cita 12 marcadores** | `[12]`, `[13]`, `[14]`, `[16]`, `[17]`, `[18]`, `[19]`, `[20]`, `[21]`, `[22]`, `[23]`, `[24]` (vault) | **Ninguna obra se pierde por esto**, y es una suerte: las doce reaparecen en sedes vivas o en anclas de los Anexos C/D. Pero **el orden de aparición cambiaría** si la sección se volca: seis de ellas (`[13]`, `[14]`, `[16]`, `[17]`, `[19]`, `[20]`) adelantarían su primera aparición al capítulo 2 |
| **Apéndice A.3 «Ficha del sistema»** | **NO EXISTE en el `.docx`.** El Apéndice A solo tiene A.1 y A.2; el Apéndice B es la plantilla que **T9** manda borrar. En el vault, `A.3` cita **27 marcadores** | `[5]`, `[6]`, `[11]`, `[12]`, `[13]`, `[14]`, `[15]`, `[18]`, `[20]`, `[21]`, `[60]` (vault) | **Aquí sí se pierden dos obras:** `[11]` CRISP-DM y `[15]` Bergstra y Bengio (*Random Search*) **no se citan en ninguna otra parte del vault**, luego **no reciben número en el `.docx`** |

> [!warning] Consecuencia directa para T1, y respuesta a la pregunta que traía el encargo
> El **`[11]` del vault (CRISP-DM, Chapman *et al.* 2000) NO llega al `.docx`**, y por eso el mapa `[1]`-`[11]` queda limpio: el `[11]` del Word es **Snort/Roesch = `[26]` del vault** y no hay colisión que resolver. Si Francisco decide volcar `A.3`, entonces CRISP-DM **sí** necesita entrada nueva en el Word, y le tocaría el **`[96]`**, no el `[11]`.

### 4.3 · Una cita que no se bloquea por sede, sino por falta de fuente

| Ancla | Marcador que pedía el Anexo D | Estado |
|---|---|---|
| «Python es el lenguaje de referencia para el aprendizaje automático» (§4.1) | `[CITA: adopción de Python en ML]` | ⛔ **NO se ha dado de alta.** No hay fuente de nivel 1-2 que sostenga esa afirmación: lo que existe es prensa sectorial y encuestas de portales, **nivel 3**, que no sostiene nada. **Opciones: atenuar la frase o retirarla.** Decide Francisco |
| «Un modelo de amenaza es la especificación explícita de las hipótesis sobre el adversario» | `[CITA: Shostack 2014]` | ⛔ **El fragmento no existe** ni en el vault ni en el `.docx` —contado contra disco—. No hay sede, así que no hay alta |

---

## 5 · Lo que no he podido confirmar

- **La página exacta de siete libros y documentos largos.** `[16]` Mitchell, `[17]` Jolliffe, `[19]` Sutton y Barto, `[22]` Breiman *et al.* (CART), `[36]` van Rijsbergen, `[4]` Chio y `[8]` Stallings quedan **marcados, no inventados**: no hay acceso al texto paginado de ninguno. Tres llevan capítulo fijado **por estructura de la obra**, no por texto consultado; dos (`[22]`, `[36]`) ni eso. Misma disciplina que con las 47 citas reconstruidas.
- **`[35]` Powers (2011) es NIVEL 2, y sostiene dos definiciones de manual** (precisión y *recall*). Su revista de publicación original no tiene revisión por pares acreditada. Es enormemente citado, pero **la regla del proyecto es que una afirmación del marco teórico no se sostiene con material débil**: si Francisco quiere nivel 1 puro, el sustituto está a mano y ya está en la tabla — **`[33]` Fawcett** o **`[34]` Sokolova y Lapalme** cubren exactamente lo mismo. **No se ha sustituido por cuenta propia.**
- **`[39]` Axelsson (informe técnico de la taxonomía) es NIVEL 2** — informe universitario sin revisión por pares. Es la fuente canónica de los ejes de taxonomía de IDS y no hay equivalente revisado por pares del mismo contenido. Se declara la reserva.
- **El «patrón dominante en la literatura» y el «~99 %» se sostienen por mapeo, no por alta**, con `[52]` Tavallaee *et al.* y `[12]` Khraisat *et al.* El «~99 %» está **verificado verbatim** («*they achieve about 98% classification rate applying very simple machine learning methods*») en [[benchmark-comparativo-nsl-kdd]] §A.1. **El «RandomForest monolítico» como forma concreta del patrón dominante NO está verificado en una fuente**: es una lectura del proyecto, respaldada por el propio `baseline.py`. **Si el tribunal aprieta ahí, la frase debe atenuarse a «un clasificador supervisado monolítico», que es lo que las fuentes sí dicen.**
- **El orden exacto dentro de §2.1.5 y §5.1.** En esas dos secciones varias anclas conviven en un tramo corto y **el fragmento literal ya no está en el vault** (lo movió el recorte), así que el orden se ha fijado por la posición en el `.docx`. Si Francisco reordena esos párrafos al volcar, **la secuencia de números no se rompe** —cada obra ya tiene el suyo—, pero deja de ser estrictamente «orden de aparición».
- **La correspondencia de `[89]`** (`.docx`) con la sede que la pide. La entrada del vault `[14]` es la documentación de `GridSearchCV`, y el ancla del Anexo D es la de `LocalOutlierFactor(novelty=True)`. **Son dos páginas distintas de la misma documentación oficial.** No se ha dado de alta un número nuevo —sería duplicar la obra— pero **la página concreta hay que fijarla en Zotero**.
- **Los `[1]`-`[11]` del `.docx` no se han verificado contra el fichero `.docx` binario**, sino contra su volcado en limpio `Resultados/docx/COMPARACION/docx_limpio.md`. No tengo forma de abrir el `.docx` desde aquí. **Francisco debe confirmar las once líneas de un vistazo antes de dar la lista por buena.**

---

## 6 · Recuento explícito

| Magnitud | Valor |
|---|---|
| **Altas nuevas escritas en `Bibliografía.md`** | **32** — `[79]`-`[110]` del vault |
| **Entradas del vault mapeadas** (reciben número del `.docx` sin alta) | **62** — 10 en el tramo congelado + 52 de `[12]` en adelante |
| **Entradas exclusivas del `.docx`** | **1** — su `[9]`, la copia pirata de Stallings, sin equivalente en el vault |
| **Números que ocupa el `.docx` en total** | **95** — `[1]`-`[11]` congelados + `[12]`-`[95]` nuevos (84) |
| **Entradas vivas del vault que NO llegan al `.docx`** | **8** — `[11]` CRISP-DM, `[15]` Bergstra y Bengio, `[62]`, `[63]`, `[64]`, `[65]`, `[66]`, `[67]`. Cuadra: 102 vivas − 62 mapeadas − 32 altas colocadas = 8 |
| **Estado del contador global del vault** | 110 filas · **102 entradas vivas** · 8 quemadas (`[9]`, `[27]`, `[28]`, `[37]`, `[40]`, `[44]`, `[45]`, `[76]`) · **primer libre `[111]`** |
| **Marcadores que hay que insertar en el Word** | **~200 apariciones** sobre 95 obras. Los `[1]`-`[11]` ya están puestos (11 apariciones); **el resto del documento no tiene ni un marcador hoy** |

---

## 7 · Cambios en Bibliografía.md

| `[n]` vault | Qué he hecho |
|---|---|
| `[79]`-`[110]` | **32 altas nuevas**, con cita completa, DOI o URL estable, nivel, «Dónde se usa» (sede + fragmento literal) y «Localizador por uso». Cinco son libros y llevan localizador; en los cinco la **página se marca como no establecida** |
| Callout de cabecera | Anotado que las tres cifras del recuento del 2026-08-20 (70 vivas / 78 filas / primer libre `[79]`) **caducaron**, con el recuento nuevo contado contra disco |
| Callout nuevo del pase | Registrado el pase completo: contador antes y después, las dos altas evitadas por mapeo, las dos fuentes que **no** se han dado de alta y por qué, los dos avisos de identidad (`[96]`≠`[24]`, `[110]`≠`[84]`) y la ampliación de la lista de libros con localizador de 8 a 13 |

> **Más de tres entradas tocadas en un solo encargo:** sí, **32 altas y 2 callouts**. Es lo que pedía el encargo (dar de alta lo que falte para la lista del `.docx`), no una ampliación por cuenta propia. **Cero renumeraciones, cero retiradas, cero sustituciones.**

---

## 8 · Implicaciones para el proyecto

1. **T1 queda cerrada con un mapa, no con una renumeración.** El desajuste era real y su resolución es la de §1: `[11]` del `.docx` = `[26]` del vault. **El vault no se toca.** Esto también cierra el riesgo que el propio Kiko señalaba en T4 («si se hace antes, cada cita nueva vuelve a romperla»): la lista de §3 es estable **mientras no se volquen `2.1.6`, `A.3` ni `6.2`**, y para ese caso §4 ya dice qué hacer —añadir por detrás del `[95]`, nunca intercalar—.
2. **T4 puede ejecutarse ya en el Word, pero solo la mitad que le corresponde.** La renumeración es **exclusivamente del `.docx`**; la propia ficha T4 dice «en el vault y en el `.docx` a la vez», y **eso contradice la decisión del usuario de este encargo**. La ficha debería corregirse: el vault **mantiene su numeración**.
3. **B1 se resuelve casi sola, y mejor de lo que estimaba el Anexo B.** De las 51 huérfanas, **43 reciben número en el `.docx`** al colocar los Anexos C y D. La lista real de descartes de B1 baja de 51 a **8**, y de esas 8, **6 son de `6.2`** —que no es descarte, es sede pendiente—. **Los descartes de verdad son dos: `[11]` CRISP-DM y `[15]` Bergstra y Bengio.**
4. **Choca con `resumen-de-decisiones.md` en un punto y hay que decirlo:** el `.docx` sostiene con **nivel 3** el dato de apertura del capítulo 1 (la URL de `channelpartner.es`), mientras el vault ya tiene la fuente de nivel 1 (INCIBE). El proyecto tiene por regla dura que una afirmación del marco no se sostiene con nivel 3. **La corrección es de una línea en Word y no la decido yo.**
5. **El trabajo de inserción es grande y conviene medirlo antes de planificarlo:** hoy el `.docx` tiene **11 marcadores** y la lista final pide **~200 apariciones** sobre 95 obras. No es un pase de bibliografía: es un pase de citado capítulo por capítulo. El capítulo 2 solo se lleva más de la mitad.
