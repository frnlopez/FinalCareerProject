# Las tareas de Kiko

Repaso del 2026-08-25 contra `Proyecto_Fin_de_Grado-FJLM-2026.docx` (2.968 párrafos, 94 marcadores,
49 tablas, 23 imágenes, 34 pies de tabla **numérica** —la regex del extractor solo captura dígito
tras «Tabla», así que los tres pies del Apéndice A quedan fuera de esa cuenta—, 22 pies de figura). Volcado en
`Resultados\docx\REPASO_20260825\`.

- `Word` = se arregla en el `.docx` · `vault` = se arregla en la nota `.md`.
- **Todas las tareas resueltas se han borrado.** El censo de lo retirado está al final.
- Autoridad de numeración: [[Bibliografia del docx - numeracion y anclas]] §2. **Ningún `[n]` nuevo.**
- **Los números de párrafo se han retirado de todo el fichero**: los del volcado anterior estaban
  desplazados. Cada tarea se localiza por **fragmento literal (Ctrl+F)**.
- **Pies de tabla:** todo lo de defectos de pies vive en `Leyenda_tablas.md`. Aquí no se duplica.

---

## 🔴 PRIORITARIO · Citas erróneas en el documento

**31 marcadores designan hoy una obra distinta de la que sostiene la frase**, más **2 que exigen
decisión**. No son pendientes: son errores. Se reescriben *in situ*, sin insertar nada nuevo.

> [!warning] Por qué son errores y no pendientes
> El `.docx` conserva marcadores con la **numeración del vault**. En la numeración del `.docx`
> (§2 del mapa) esos mismos números ya están adjudicados a otras obras: `[18]`=Jolliffe,
> `[23]`=Dietterich, `[20]`=Sutton y Barto, `[25]`=Friedman, `[17]`=Hastie, `[61]`=Massey,
> `[24]`=Breiman, `[31]`=Breunig, `[49]`=Arp, `[52]`=Kapoor, `[51]`=Pierazzi, `[50]`=Biggio,
> `[63]`=Waskom. Dejarlos atribuye la afirmación a un autor que no la hizo.

### Arp *et al.* → `[49]` (6 reescrituras)

- [ ] **X1** · SEDE: «…es decir data snooping —el pitfall P3 del catálogo de Arp et al. **[18]**—, y por tanto las métricas publicadas son optimistas respecto…». ACCIÓN: reescribir `[18]` → `[49]`. `Word`
- [ ] **X2** · SEDE: «La taxonomía de errores metodológicos en machine learning aplicado a seguridad **[18]**, que cataloga como defecto reportar una métrica sin declarar sobre qué población y con qué etiquetas se calcula». ACCIÓN: reescribir `[18]` → `[49]`. `Word`
- [ ] **X3** · SEDE: «…daría apariencia de comparación donde no la hay, que es justamente el error que **[18]** documenta como endémico en seguridad». ACCIÓN: reescribir `[18]` → `[49]`. `Word`
- [ ] **X4** · SEDE: «Arp et al. clasifican esta situación como el pitfall P9, Lab-Only Evaluation **[18]**.». ACCIÓN: reescribir `[18]` → `[49]`. `Word`
- [ ] **X5** · SEDE: «…en respuesta a la defensa —el pitfall P10, Inappropriate Threat Model **[18]**—». ACCIÓN: reescribir `[18]` → `[49]`. `Word`
- [ ] **X6** · SEDE: «…aprendizaje automático a seguridad informática de Arp et al. **[18]**, introducido en 2.3.3». ACCIÓN: reescribir `[18]` → `[49]`. `Word`
### Pierazzi *et al.* → `[51]` (1 reescritura)

- [ ] **X7** · SEDE: «…la distinción feature space / problem space **[52]**—. Forzar el experimento produciría una medición vistosa…». ACCIÓN: reescribir `[52]` → `[51]` (Pierazzi, no Kapoor). `Word`

### Tavallaee *et al.* → `[44]` (6 reescrituras)

- [ ] **X8** · SEDE: «…se distribuye en tres ficheros con tamaños y funciones distintos **[23]**. KDDTrain+ reúne 125.973 instancias…». ACCIÓN: reescribir `[23]` → `[44]`. `Word`
- [ ] **X9** · SEDE: «…no se entrenaron sobre KDDTrain+ entero, sino sobre el primer 20 % de sus registros **[23]**». ACCIÓN: reescribir `[23]` → `[44]`. `Word`
- [ ] **X10** · SEDE: «…la partición de evaluación definida por el artículo que creó el dataset **[23]**, que publica sus baselines sobre KDDTest+». ACCIÓN: reescribir `[23]` → `[44]`. `Word`
- [ ] **X11** · SEDE: «La composición de KDDTest+ frente a KDDTrain+ **[23]**: los 17 tipos ausentes del entrenamiento…». ACCIÓN: reescribir `[23]` → `[44]`. `Word`
- [ ] **X12** · SEDE: «…los siete baselines canónicos del artículo que creó el dataset **[23]**, medidos sobre KDDTest+…». ACCIÓN: reescribir `[23]` → `[44]`. `Word`
- [ ] **X13** · SEDE: la celda de cabecera de la tabla de baselines, «Clasificador **[23]**» (el espacio ya está bien en el `.docx`). ACCIÓN: reescribir `[23]` → `[44]`. `Word`

### Axelsson *base-rate fallacy* → `[73]` y NIST SP 800-94 → `[14]` (6 reescrituras, 2 en el mismo párrafo)

- [ ] **X14** · SEDE: «…los ataques son sucesos raros dentro de un volumen abrumador de conexiones legítimas **[24] [25]**. Este es el razonamiento de la falacia de la tasa base…». ACCIÓN: reescribir el par a `[73] [14]`, **sin perder ninguno de los dos**. `Word`
- [ ] **X15** · SEDE: «…no depende del valor exacto elegido, sino del orden de magnitud **[24]**». ACCIÓN: reescribir `[24]` → `[73]`. `Word`
- [ ] **X16** · SEDE: «…consiste en cambiar falsos negativos por falsos positivos **[25]**; y la conclusión clásica de la falacia de la tasa base…». ACCIÓN: reescribir `[25]` → `[14]`. `Word`
- [ ] **X17** · SEDE: «…de intrusiones es la tasa de falsos positivos, no la sensibilidad **[24]**. Esta prioridad queda enunciada aquí…». ACCIÓN: reescribir `[24]` → `[73]`. `Word`
- [ ] **X18** · SEDE: «El criterio de tuning de IDPS de la guía NIST SP 800-94 **[25]**, el mismo que respalda la métrica obligatoria 1 de §5.0.3». ACCIÓN: reescribir `[25]` → `[14]`. `Word`

### Reconocimiento de conjunto abierto: Scheirer → `[48]`, Bendale → `[71]` (4 reescrituras)

- [ ] **X19** · SEDE: «…el riesgo de espacio abierto, cualquiera que sea el umbral elegido **[61]**. La consecuencia práctica es la observada…». ACCIÓN: reescribir `[61]` → `[48]`. `Word`
- [ ] **X20** · SEDE: «…la región del espacio de características que sus datos de entrenamiento no cubren —el riesgo de espacio abierto **[61]**—». ACCIÓN: reescribir `[61]` → `[48]`. `Word`
- [ ] **X21** · SEDE: «…uso no calibrado de la salida probabilística como línea base a superar **[49]**. El mecanismo de UMBRAL_CONF no es una elección desafortunada…». ACCIÓN: reescribir `[49]` → `[71]`. `Word`
- [ ] **X22** · SEDE: «…la probabilidad de que la muestra no pertenezca a ninguna clase vista **[49]**. Es la vía que atacadirectamente la fracción de 0-day mal etiquetados como conocidos» (la errata «atacadirectamente» es real en el `.docx`; se corrige en **5.32**). ACCIÓN: reescribir `[49]` → `[71]`. `Word`

### Reproducibilidad, fugas y surveys (4 reescrituras)

- [ ] **X23** · SEDE: «El ítem de asignación de muestras a particiones del checklist de reproducibilidad adoptado en §5.0.5 **[20]**». ACCIÓN: reescribir `[20]` → `[68]` (Pineau). `Word`
- [ ] **X24** · SEDE: «…los error bars y central tendency del ML Reproducibility Checklist **[20]**». ACCIÓN: reescribir `[20]` → `[68]`. `Word`
- [ ] **X25** · SEDE: «La taxonomía de fugas de datos **[17]**, y en concreto su categoría de preprocesado previo al split». ACCIÓN: reescribir `[17]` → `[52]` (Kapoor y Narayanan). `Word`
- [ ] **X26** · SEDE: «…de la evaluación real y puede dar lugar a afirmaciones inexactas **[31]**». ACCIÓN: reescribir `[31]` → `[12]` (Khraisat *et al.* 2019). `Word`

### Números fuera del rango del `.docx` (4 reescrituras)

- [ ] **X27** · SEDE: «…el banco de pruebas estándar de la detección de intrusiones (**[63]** + [64])». ACCIÓN: reescribir `[63]` → `[43]` (Lippmann). El `[64]` de ese mismo paréntesis **es correcto** y no se toca. `Word`
- [ ] **X28** · SEDE: «…reporta una «zero-day detection accuracy» del 89-99 % en su tabla 3 y en su §5 **[77]**». ACCIÓN: reescribir `[77]` → `[13]` (Hindy *et al.*). `Word`
- [ ] **X29** · SEDE: «…con tráfico exclusivamente benigno y ataques en los cuatro restantes **[51]**. Eso habilita de golpe la división cronológica real…». ACCIÓN: reescribir `[51]` → `[74]` (Sharafaldin, CIC-IDS2017). `Word`
- [ ] **X30** · SEDE: «…capturado, por lo que la información temporal existe en origen **[50]**. Ahora bien, este trabajo no ha podidoverificar…» (la errata «podidoverificar» es real en el `.docx`; se corrige en **5.33**). ACCIÓN: reescribir `[50]` → `[75]` (Moustafa y Slay, UNSW-NB15). ⚠️ identidad de la obra marcada como MATCH APROXIMADO en §5.3 «Dos matches solo aproximados» del mapa: confirmar antes de pegar. `Word`

### Decisiones que solo puede tomar Francisco

- [ ] **X31** · **DECISIÓN:** SEDE: «…la magnitud del problema sin medirla. El dato citable es el de **[74]**». ACCIÓN: decidir si es `[74]` (Sharafaldin, CIC-IDS2017) o `[72]` (Goldschmidt y Chudá), como las otras dos apariciones del mismo apartado. `Word`
- [ ] **X32** · **DECISIÓN:** SEDE: «Ese análisis consistió en revisar la propuesta original **[67]** y contrastar sus supuestos con las condiciones del presente…». ACCIÓN: `[67]` del vault **no tiene equivalencia** en la numeración del `.docx`; decidir entre retirar el marcador o volcar la obra al final de la lista. **No traducir por analogía.** `Word`

---

## T · Transversal

- [ ] **T3** · SEDE: el apartado «Bibliografía», hoy con la lista antigua del Word. ACCIÓN: volcar las 75 entradas de [[Bibliografia del docx - numeracion y anclas]] §9. `Word`
- [ ] **T4** · **(ÚLTIMA)** SEDE: todo el cuerpo del `.docx`. ACCIÓN: aplicar `[12]`–`[75]` según el Anexo C, después de las **30 tareas (X1–X30) sobre 31 marcadores** del bloque prioritario (X14 toca dos marcadores en el mismo párrafo). `[1]`–`[11]` congelados. `Word`
- [ ] **T5** · SEDE: los wikilinks `[[…]]` supervivientes — **18 ocurrencias repartidas en 16 párrafos** (dos de ellos llevan dos cada uno), p. ej. «…que se aborda en **[[5.1 Resultados del modelo de detección de anomalías el capítulo 5]]**». ACCIÓN: sustituir cada uno por «véase §x.y». `Word`
- [ ] **T6** · SEDE: los pies de tabla y de figura del documento — los 34 «Tabla x.y» que cuenta el extractor **más los tres del Apéndice A** («Tabla A.1», «A.2», «A.3»), que su regex no captura. ACCIÓN: aplicar lo registrado en `Leyenda_tablas.md`. Aquí no se enumera nada más. `Word`
- [ ] **T7** · SEDE: las figuras que **no se llaman por número desde la prosa**: 3.1, 4.1, 4.2, 4.3, 4.4, 4.5, 5.5, 5.6, 5.7, 5.8, 5.9, 5.10, 5.11 y 5.12 (su número aparece solo en el pie). **Sí llevan llamada** la 2.1 («tal y como se ilustra en la Figura 2.1»), la 2.5 («representada en la Figura 2.5») y las 5.1–5.4 («Las cuatro figuras siguientes (Figura 5.1, 5.2, 5.3 y 5.4)»). ACCIÓN: añadir la llamada por número en la prosa que las introduce. El detalle vive en `Leyenda_tablas.md`; aquí solo se remite. `Word`
- [ ] **T8** · SEDE: el índice de contenido, entradas «A.1.5. Etiquetas: tipos de ataque y categorías» y «A.2. Métricas de desempeño». ACCIÓN: regenerar el índice **después** de A3, A6, A7/A8 y A15; hoy el TOC rotula «A.1.5» lo que el cuerpo deja como Título 8 sin número visible. `Word`
- [ ] **T9** · SEDE: el párrafo que dice literalmente «EDAKJDFSLDLKJ». ACCIÓN: cerrar el glosario de acrónimos y borrar ese residuo. `Word`
- [ ] **T10** · **DECISIÓN:** hoy no existe índice de figuras ni de tablas. ACCIÓN: decidir si se añaden ambos, solo uno o ninguno. `Word`

---

## Capítulo 1 · Introducción

- [ ] **1.1** · SEDE: los Título 2 «Motivación» y «Preliminares», consecutivos. ACCIÓN: fundirlos en uno solo. `vault`
- [ ] **1.2** · SEDE: la viñeta que dice «Este último punto es precisamente el que motiva el presente trabajo.». ACCIÓN: sacarla de la lista y convertirla en párrafo de cierre del apartado. `vault`
- [ ] **1.3** · SEDE: las viñetas «Estudiar los resultados obtenidos tras la integración de ambas etapas, validando los resultados y midiendo la capacidad de detección de ataques desconocidos» y «Medir la capacidad de detección de ataques desconocidos y analizar críticamente los resultados obtenidos». ACCIÓN: fundirlas en un solo objetivo específico. `vault`

---

## Capítulo 2 · Marco Teórico

- [ ] **2.10** · SEDE: el capítulo 2 completo; no existe ningún Título 2 ni Título 3 de estado del arte. ACCIÓN: añadir una sección de trabajos relacionados. Material aprovechable en §5.4. Carencia estructural más grave. `vault`
- [ ] **2.11** · SEDE: el párrafo que termina por «…existen trabajos que la adoptan, la invierten y la reformulan como conjunto paralelo. Situar este trabajo frente a esos tres casos permite precisar en qué se apoya y en qué se aparta [42]». ACCIÓN: escribir los tres trabajos que la promesa anuncia; hoy solo se cita Tombini. `vault`
- [ ] **2.12** · SEDE: ese mismo párrafo, en el inciso «es, **dentro del sentido (a) fijado más arriba**, uno de los patrones con más recorrido». ACCIÓN: apunta a texto que ya no está en el `.docx`; reescribir el inciso o restituir el sentido (a). `vault`
- [ ] **2.13** · SEDE: el Título 3 «IA, ML y DL», hoy dentro de §2.3 «Inteligencia Artificial», al final del capítulo. ACCIÓN: pasarlo al principio del capítulo 2, delante del Título 2 «Machine Learning». `vault`
- [ ] **2.14** · SEDE: el párrafo que empieza por «El recorrido va en cuatro tramos: los casos de uso defensivos, el problema de lo desconocido» y termina por «…que condiciona lo que hoy puede evaluarse en investigación de NIDS». ACCIÓN: entregar los dos tramos que anuncia y no desarrolla, «la cara ofensiva» y «el panorama de datasets». `vault`
- [ ] **2.15** · SEDE: el Título 3 «Etapas del Ciclo de vida de un proyecto de ML» y sus cinco hijos en Título 5 («Comprensión y recolección de datos», « Selección del tipo de modelo», …). ACCIÓN: bajar los cinco hijos a Título 4. Efecto actual: §2.1.3 no tiene ninguna subentrada en el índice. `Word`
- [ ] **2.16** · SEDE: el Título 3 «Límites y consideraciones éticas» y todo su contenido. ACCIÓN: comprimirlo; hoy desarrolla P9 y P10 con extensión de capítulo de resultados. `vault`
- [ ] **2.17** · SEDE: las tres formulaciones de la justificación one-class: «Estos algoritmos se denominan semisupervisados (one-class)», «…para permitir por contraste el régimen semisupervisado (one-class) [17]» y «La etapa 1 materializa este paradigma con detectores semisupervisados (one-class) entrenados solo con tráfico normal (D1)». ACCIÓN: dejarla en un solo sitio y remitir desde los otros dos. `vault`
- [ ] **2.18** · SEDE: «…el corazón de la Seguridad Informática (CIA: Confidentiality, Integrity and **Aviability**)». ACCIÓN: corregir a **Availability**. `vault`
- [ ] **2.24** · SEDE: el párrafo que empieza por «Un modelo de amenaza es la especificación explícita de las hipótesis sobre el adversario» y termina por «…Se construye fijando un valor en cada una de estas dimensiones». ACCIÓN: añadir el marcador `[CITA: Shostack, *Threat Modeling*, 2014]` al final de la primera frase; la obra no tiene número asignado en el `.docx`. `Word`
- [ ] **2.25** · SEDE: el Título 3 **vacío** que cierra el capítulo 2, inmediatamente antes del Título 1 «Diseño del sistema». ACCIÓN: eliminarlo. `Word`
- [ ] **2.26** · SEDE: la viñeta que empieza por «Reducción de dimensionalidad y visualización» y termina por «…conservando su estructura (como por ejemplo PCA)», y la «Lista de Acrónimos». ACCIÓN: desarrollar la sigla en la viñeta — «(como por ejemplo el análisis de componentes principales, PCA)» — y añadir la fila `PCA	Principal Component Analysis` a la lista, que hoy no la tiene. `Word`
- [ ] **2.27** · SEDE: la «Lista de Acrónimos» completa. ACCIÓN: **`EDAKJDFSLDLKJ` es texto de relleno sin borrar**; dejarlo en `EDA	Exploratory Data Analysis`. **`CIA` y `ROC` no tienen desarrollo**: añadir «Confidentiality, Integrity and Availability» y «Receiver Operating Characteristic». **Falta el espacio entre sigla y desarrollo** en `IDSIntrusion`, `NIDSNetwork` y `H-NIDSHybrid`. `Word`

### Decisiones de Francisco (obras sin sede en el `.docx`)

- [ ] **2.19** · **DECISIÓN:** Bergstra y Bengio, *Random Search*: sin sede en el documento. ACCIÓN: escribirle una frase en §2.1.3 (Título 5 «Entrenamiento del modelo y ajuste de hiperparámetros») o descartar la obra. `vault`
- [ ] **2.20** · **DECISIÓN:** TabArena · Micci-Barreca · Pargent: tienen sede en el capítulo 5 pero no tienen número en el `.docx`. ACCIÓN: decidir entre volcarlas al final de la lista o retirarlas. `vault` + `Word`
- [ ] **2.21** · **DECISIÓN:** Hwang *et al.*, IDS híbrido: misma situación; va junto a 2.10 y 2.11. ACCIÓN: decidir entre darle número al final de la lista o retirarla. `vault` + `Word`
- [ ] **2.22** · **DECISIÓN:** Pendlebury *et al.*, TESSERACT: sin sede. ACCIÓN: escribirle sede en §2.3.3 o descartar. `vault`
- [ ] **2.23** · **DECISIÓN:** Behrouz *et al.*, *Nested Learning*: sin sede clara. ACCIÓN: descarte limpio salvo que se le encuentre una. `vault`

---

## Capítulo 3 · Diseño del sistema

- [ ] **3.1** · SEDE: la celda «Error de reconstrucción: reconstruye mal lo que no se parece a lo normal» de la Tabla 3.2. ACCIÓN: añadir `[6]`. En el cuerpo ya está puesto. `Word`
- [ ] **3.5** · SEDE: los tres párrafos que empiezan por «Para comprobar que el orden de la cascada fijado en §3.2.1 es el adecuado» y terminan por «…El coste real de invertir el orden sería, por tanto, superior al medido». ACCIÓN: pasarlos al capítulo 5, detrás del apartado «Resultados del sistema híbrido»; hoy dan cifras (6.558/9.711, 67,53 %) dentro de Diseño. `vault`
- [ ] **3.6** · SEDE: «Las tres son, formalmente, selección de modelo sobre el conjunto de test, es decir data snooping» (cap. 6) y «…es decir data snooping —el pitfall P3 del catálogo de Arp et al.» (cap. 3). ACCIÓN: dejar la confesión desarrollada en un solo sitio y remitir desde el otro. `vault`
- [ ] **3.7** · **DECISIÓN:** la comparación tabular de §3.5 no está volcada al `.docx`. Con ella se caen Barbará (ADAM), Grinsztajn, McElfresh, Shwartz-Ziv y Armon, y Hollmann (TabPFN). ACCIÓN: volcarla o descartar esas cinco obras. `vault` + `Word`
> [!note] Pies del capítulo 3
> Los defectos de pie de este capítulo (entre ellos el punto final de «Figura 3.1. Flujo del
> proyecto») están registrados en `Leyenda_tablas.md` y los cubre **T6**. Aquí no se duplican.

- [ ] **3.9** · **DECISIÓN:** la Figura 3.1 está en el `.docx` pero fuera del censo de `assets/` del vault. ACCIÓN: incorporarla al censo o declararla figura solo del Word. `vault` + `Word`
- [ ] **3.10** · SEDE: el Título 3 **vacío** que separa el pie «Tabla 3.1. Subconjuntos especializados…» del párrafo «Esta separación es lo que hace posible medir la detección de 0-day». ACCIÓN: eliminarlo o darle título. `Word`

---

## Capítulo 4 · Implementación del sistema

- [ ] **4.7** · SEDE: los Título 3 «Normalización de variables numéricas», «Codificación de variables categóricas» y «Selección de características», en ese orden. ACCIÓN: reordenar a codificación → normalización → selección, el orden real del pipeline. `vault`
- [ ] **4.8** · SEDE: el párrafo que empieza por «El conjunto D3, con el que se entrena el clasificador de firmas, está fuertemente desbalanceado» y termina por «…sus dos opciones disponibles». ACCIÓN: añadir el aviso de que el eje SMOTE vs `class_weight` no queda establecido entre semillas (§5.2.4). `vault`
- [ ] **4.9** · SEDE: el Título 3 «Selección de características» y su pie «Tabla 4.6. Experimento H1: comparación del sistema híbrido completo sobre D2 con los conjuntos de 54 y 122 características». ACCIÓN: mover el experimento al capítulo 5 o marcarlo como adelanto; hoy da métricas sobre D2 dentro de Implementación. `vault`
- [ ] **4.10** · SEDE: las cuatro apariciones del desbalance **883:1** — «…ratio ≈ 883:1 entre DoS y U2R», «…supera a la minoritaria (u2r) en una proporción cercana a 883:1», el pie «Tabla 4.8. Distribución de D3 por categoría de ataque…» y «La proporción entre la clase mayoritaria y la minoritaria es ≈ 883:1». ACCIÓN: dejarlo desarrollado en una sola y remitir desde las otras tres. `vault`
- [ ] **4.11** · SEDE: las apariciones del umbral **p95**, entre ellas «El umbral se fija en el percentil 95 de la puntuación de anomalía sobre validación», «El umbral se fija en el percentil 95 del score de anomalía sobre un subconjunto de validación reservado de D1» y «…para D1_val es el fijado del umbral de decisión, que quedó como el percentil 95 del score». ACCIÓN: dejar la justificación en un solo sitio; en el resto, mención escueta. `vault`
- [ ] **4.12** · SEDE: el párrafo «Balanceo: el ganador por algoritmo del mini-experimento de …4.3.4 (class_weight='balanced' para DecisionTree; SMOTE para el resto)» y la viñeta «Ganadores por algoritmo: class_weight para DecisionTree; SMOTE para RandomForest, KNN y HistGradientBoosting». ACCIÓN: no volver a tabular los ganadores; dejar solo la remisión. `vault`
- [ ] **4.15** · SEDE: la Figura 4.3 y su pie «Figura 4.3. Histogramas superpuestos de las doce características más discriminantes». ACCIÓN: mantenerlos en la misma página (salto de página entre imagen y pie). ⚠️ NO VERIFICADO: la paginación no es observable en el volcado de texto. `Word`
- [ ] **4.16** · SEDE: el párrafo que empieza por «El mapeo (attack_mapping en program.py) cubre deliberadamente también los tipos que solo aparecen» y termina por «…permite medir la detección de ataques "0-day" por tipo». ACCIÓN: sustituir las comillas rectas de `"0-day"` por comillas españolas. `Word`

### Decisiones de Francisco

- [ ] **4.13** · **DECISIÓN:** SEDE: «Ecosistema científico maduro: **Python es el lenguaje de referencia para el aprendizaje automático**, con librerías consolidadas (scikit-learn, pandas, numpy) que cubren todo el pipeline sin necesidad de herramientas externas». ACCIÓN: atenuar a «uno de los lenguajes más extendidos… y el que usan las librerías empleadas» y decir con qué obra se respalda, o retirar la afirmación. `vault`
- [ ] **4.14** · **DECISIÓN:** CRISP-DM no aparece en el `.docx` (0 ocurrencias). ACCIÓN: darle sede en §4.1 o descartar la obra. `vault`

---

## Capítulo 5 · Evaluación

### Rigor — lo primero

- [ ] **5.1** · SEDE: el párrafo que empieza por «D2 y D3 no se dividen, por lo que nos quedamos con sus funciones ya mencionadas» y termina por «…y la evaluación de los modelos para D3». ACCIÓN: **invertir la atribución**: D3 entrena la etapa 2 y aporta las probabilidades out-of-fold; D2 es el conjunto de evaluación. Error más grave del documento. `vault`
- [ ] **5.2** · SEDE: el párrafo que empieza por «D1 se divide en dos particiones, una D1_train (80% de D1) y otra D1_val» y termina por «…que quedó como el percentil 95 del score». ACCIÓN: reescribirlo: D1 es el conjunto; D1_train y D1_val son su división 80/20. Hoy asigna a D1 una función propia además de a sus dos mitades. `vault`
- [ ] **5.3** · SEDE: las apariciones sueltas de `0,8223` en las tablas de robustez, frente al párrafo «Por esta razón, siempre que se cite el 0,8223 debe citarse junto a su banda [0,7779–0,8205] y su media 0,8035». ACCIÓN: cumplir esa regla también donde la cifra aparece sola. `vault`
- [ ] **5.4** · SEDE: las siglas sin definir «decisión H-2», «(H-6)», «decisión H-3» y «Q1/C» (esta última, tres apariciones; la variante `Q1\C` **no existe en el `.docx`**: 0 ocurrencias). ACCIÓN: dar diccionario en §5.0 o eliminarlas del cuerpo. `vault`
- [ ] **5.5** · SEDE: «…está en **Resultados\selected_features.txt**», «…se persisten en **Resultados\specialized_nsl_kdd_mappings_and_info.txt**» y «la evidencia de **Resultados/metricas_hibrido_0day.csv**». ACCIÓN: sacar del cuerpo las rutas de artefacto; a apéndice o a nota al pie. `vault`

### Estructura

- [ ] **5.9** · SEDE: los rótulos en texto plano «Particiones y su función», «Elementos congelados» y «Métricas Obligatorias», entre el Título 1 «Evaluación» y el Título 2 «Resultados del modelo de detección de anomalías». ACCIÓN: convertirlos en §5.0 con subsecciones numeradas; el texto remite a «§5.0.5» y «§5.0.3», que hoy no existen. `Word` + `vault`
- [ ] **5.11** · SEDE: §5.3 «Resultados del sistema híbrido» y §5.4 «Conclusiones del capítulo», sin ningún Título 3 en su interior. ACCIÓN: titular con estilo de encabezado sus apartados; por eso son las dos únicas secciones del capítulo sin subentradas en el índice. `Word`
- [ ] **5.12** · SEDE: el Título 2 «Conclusiones del capítulo» del capítulo 5, que empieza por «Este capítulo ha evaluado por separado las dos etapas del sistema». ACCIÓN: partirlo en **Discusión** y **Conclusiones**. `vault`
- [ ] **5.13** · SEDE: los Título 3 «Resultados finales» (§5.1) y «Comparación de los resultados de cada algoritmo» (§5.2). ACCIÓN: unificar el nombre de los dos apartados de cierre. `vault`
- [ ] **5.15** · SEDE: las referencias cruzadas del capítulo, hoy en tres formatos: «§4.3.5», «(4.3.5)» y «en 3.3.2 y 5.4». ACCIÓN: unificar a un solo estilo. `Word`

### Figuras, tablas y ecuaciones

- [ ] **5.17** · SEDE: «La proyección es aritmética elemental sobre dos cifras ya publicadas —`bin_recall` = 0,8318 y `bin_fpr` = 0,1017— y una prevalencia de ataque *p* que se hace variar». ACCIÓN: quitar los backticks vivos y los asteriscos de cursiva Markdown; dar formato de Word. `Word`
- [ ] **5.18** · SEDE: el párrafo que empieza por «Junto al FPR conviene acotar la segunda cifra que invita a la sobrelectura: la velocidad» y termina por «…residentes en memoria». ACCIÓN: añadir la tabla de tiempos y latencia; el texto critica las columnas `latencia_ms_por_flujo` y `flujos_por_segundo`, que no se muestran en ninguna tabla. `vault`
- [ ] **5.19** · SEDE: los dos párrafos de estilo `FiguraTablaEcuacin` rotulados «(1)», uno en el capítulo 2 y otro en «La proyección es aritmética elemental…». ACCIÓN: renumerar el segundo. `Word`
- [ ] **5.24** · SEDE: la fila vacía de la tabla del eje de balanceo en `5.2 Resultados del modelo de detección basado en firmas.md`. ACCIÓN: eliminarla. `vault`
> [!note] Pies y celdas del capítulo 5
> Los defectos de pie y de celda de este capítulo —las dos celdas de la Tabla 5.8 que empiezan por
> pipe, el pie de la Figura 5.6 pegado a su imagen y el pie de la Figura 5.11 pegado a la prosa—
> están registrados en `Leyenda_tablas.md` y los cubre **T6**. Aquí no se duplican.

- [ ] **5.28** · SEDE: la Tabla 5.11 y su pie «Tabla 5.11. Sistema híbrido frente al baseline de control». ACCIÓN: mantenerlos en la misma página. ⚠️ NO VERIFICADO: la paginación no es observable en el volcado. `Word`

### Recortes y redacción

- [ ] **5.21** · SEDE: las **siete** apariciones del **13,4 %** (una de ellas, celda de tabla), entre ellas «Este 13,4 % no es un defecto de ejecución, sino el comportamiento que la teoría predice», «solo el 13,4 % termina etiquetado como unknown», «de los 0-day que la etapa 1 sí detecta, solo el 13,4 % se enruta a unknown» y «Es la explicación teórica del 13,4 % de 0-day detectados que llegan a etiquetarse como unknown». ACCIÓN: dejar la explicación en un sitio y remitir desde el resto. `vault`
- [ ] **5.22** · SEDE: la viñeta que empieza por «El baseline también falla donde su CV prometía: su f1_macro cae de 0.909 en validación cruzada» y la casi idéntica «El baseline también falla donde su validación cruzada prometía: su f1_macro se desploma de 0.909». ACCIÓN: dejar una sola. `vault`
- [ ] **5.23** · SEDE: «…el titular y la banda no salen del mismo commit, **de modo qua ser deriva** de código y no dispersión por semilla». ACCIÓN: reescribir a «de modo que se deriva de código». `vault`
- [ ] **5.32** · SEDE: «Es la vía que **atacadirectamente** la fracción de 0-day mal etiquetados como conocidos». ACCIÓN: separar las dos palabras, «ataca directamente». `Word`
- [ ] **5.33** · SEDE: «…este trabajo no ha **podidoverificar** que los ficheros CSV publicados expongan columnas de tiempo». ACCIÓN: separar las dos palabras, «podido verificar». `Word`
- [ ] **5.31** · SEDE: ese mismo párrafo, que empieza por «El **13** se cita con tres salvedades que son parte de la cifra». ACCIÓN: restituir la cifra completa, «El 13,4 %»; hoy ha perdido los decimales y el símbolo de porcentaje. `vault`

### Decisiones de Francisco

- [ ] **5.25** · **DECISIÓN:** Storkey, *When Training and Test Sets Are Different*: su ancla de §5.1 no sobrevive en el `.docx`. ACCIÓN: reintroducir la frase sobre *dataset shift* o descartar la obra. `vault`
- [ ] **5.26** · **DECISIÓN:** Mitchell *et al.*, *Model Cards*: sin sede porque `A.3` no está volcada. ACCIÓN: ligada a **A14**; se decide con ella. `vault`

---

## Capítulo 6 · Conclusiones

- [ ] **6.4** · SEDE: el bloque del capítulo 6 «3. No hay adversario adaptativo (P10, Inappropriate Threat Model).» y su razón técnica «Evaluar sobre un conjunto de tráfico fijo equivale a suponer un adversario estático, que no modifica su comportamiento en respuesta a la defensa —el pitfall P10, Inappropriate Threat Model [18]—». ACCIÓN: el supuesto **ya está declarado** en el capítulo 6, así que lo que queda es (a) poner el marcador `[50]` (Biggio y Roli) a esa formulación y (b) decidir si se deduplica con la formulación gemela del capítulo 2 («Medir un detector sobre un conjunto de tráfico fijo equivale a suponer un adversario que no modifica su comportamiento en respuesta a la defensa»), que es el **candidato a recorte nº 6**. `vault`
- [ ] **6.5** · SEDE: la viñeta que empieza por «Tasa de falsos positivos condicionada por el drift. El detector de anomalías opera a un FPR efectivo del ~10 %» y termina por «…ambas cifras deben leerse juntas». ACCIÓN: añadir que ese FPR debe leerse **a prevalencia realista** (`[73]`, falacia de la tasa base) y que la latencia publicada es **techo de laboratorio**. `vault`
- [ ] **6.6** · SEDE: el apartado «Validación de la tesis del híbrido». ACCIÓN: añadir el titular `f1_macro` 0,8223 con su banda [0,7779–0,8205] y la mención de que es el mejor de once corridas. `vault`
- [ ] **6.7** · SEDE: la viñeta que empieza por «Clases minoritarias u2r y r2l. Con muy pocas muestras de entrenamiento» y termina por «…Es el punto débil universal de la etapa de firmas». ACCIÓN: desdoblarla en dos limitaciones, una por clase. `vault`
- [ ] **6.9** · SEDE: «Objetivo general — implementar un H-NIDS. Cumplido. El sistema se materializó como una cascada de dos etapas». ACCIÓN: declarar expresamente si se cumplió la parte del objetivo general que exige comparar contra «cada etapa por separado»; hoy solo se declara el contraste con el monolítico. `vault`
- [ ] **6.10** · SEDE: el Título 1 «Conclusiones» seguido inmediatamente del Título 2 «Conclusiones». ACCIÓN: renombrar el Título 2. `Word`
- [ ] **6.11** · SEDE: «La conclusión de fondo es que firmas y anomalías no compiten, sino que se complementan», que repite «En síntesis, el capítulo demuestra con datos que un enfoque híbrido orientado a la detección de lo desconocido aporta una capacidad…» del capítulo 5. ACCIÓN: suprimir la repetición y dejar la conclusión formulada una sola vez. `vault`

---

## Apéndices

- [ ] **A1** · **DECISIÓN:** la tabla de las 41 características es hoy una única tabla real de Word, continua y partida por subtítulos. ACCIÓN: decidir la numeración del Apéndice A (ligada a **A5**). `Word`
- [ ] **A3** · SEDE: los encabezados «A.1.2 Características de contenido (10–22)» (estilo `Ttulo3`), «A.1.3 Características de tráfico basadas en tiempo (23–31)» y «A.1.4 Características de tráfico basadas en host (32–41)» (estilo `Ttulo3deApndice`). ACCIÓN: reestilarlos a Título 8, como «Características básicas (1–9)»; los tres salen renumerados y corrompidos en el cuerpo. `Word`
- [ ] **A5** · **DECISIÓN:** el Apéndice A tiene hoy **tres** pies de tabla —«Tabla A.1. Características del dataset completo NSL-KDD», «Tabla A.2. Codificación numérica de las cinco categorías por el LabelEncoder del pipeline.» y «Tabla A.3. Los 40 tipos de etiqueta agrupados por categoría…»— frente a **cuatro** bloques de tabla de características, de los que **tres quedan sin pie**. ACCIÓN: decidir la numeración (cuatro bloques con pie propio A.1–A.4, desplazando los actuales A.2 y A.3; o una sola tabla continua con un único pie A.1). El detalle está en `Leyenda_tablas.md`. ⚠️ El «34 pies» del recuento automático es una limitación de la regex del extractor —solo captura dígito tras «Tabla»—, no un hecho del documento. `Word`
- [ ] **A6** · SEDE: el Título 6 «Columnas del dataset NSL-KDD» seguido del Título 7 con el mismo texto. ACCIÓN: eliminar el duplicado. `Word`
- [ ] **A7 + A8** · SEDE: el **Título 7 vacío** que precede inmediatamente a «Bibliografía» — es la posición que el índice rotula «A.2. Métricas de desempeño». ACCIÓN: **DECISIÓN:** o se redacta y vuelca el apéndice A.2, o se borra el Título 7 vacío y se retira su entrada del índice. Son el mismo objeto: no se tratan por separado. `vault` + `Word`
- [ ] **A9** · SEDE: «Constante a 0 en todo el NSL-KDD (por eso el filtro de varianza la elimina, **véase 4.3 Preprocesamiento de los datasets §4.3.5**)». ACCIÓN: reducir a «véase §4.3.5». `vault`
- [ ] **A10** · SEDE: la fila `su_attempted` de la tabla de características. ACCIÓN: corregir el tipo, que dice «Discreta» cuando la descripción es binaria. `vault`
- [ ] **A11** · SEDE: las menciones a los flags de conexión en las descripciones del apéndice. ACCIÓN: unificar a mayúsculas `S0/S1/S2/S3`. ⚠️ NO VERIFICADO: la variante en minúsculas no se localiza en el volcado; comprobar en el `.docx` antes de tocar nada. `vault`
- [ ] **A12** · SEDE: «Número de fragmentos **“erróneos”** en la conexión», «Número de indicadores **“sensibles”** (accesos a directorios de sistema…)» y «Número de condiciones **“comprometidas”** observadas». ACCIÓN: sustituir las comillas tipográficas inglesas por comillas españolas. `Word`
- [ ] **A13** · SEDE: «El pipeline (**program.py**) codifica las etiquetas en dos niveles», la ruta «**Resultados\specialized_nsl_kdd_mappings_and_info.txt**» y «los ficheros **y_attack/y_category** del capítulo 5». ACCIÓN: darles formato monoespaciado. ⚠️ NO VERIFICADO: la fuente no es observable en el volcado de texto. `Word`
- [ ] **A14** · **DECISIÓN:** `A.3 «Ficha del sistema»` no existe en el `.docx` ni como encabezado, y el capítulo 5 le apunta. ACCIÓN: volcar el apéndice o retirar las llamadas colgantes. De ello dependen **4.14** (CRISP-DM), **2.19** (Bergstra y Bengio) y **5.26** (Model Cards). `vault` + `Word`
- [ ] **A17** · SEDE: el pie «Tabla A.1. Características del dataset completo NSL-KDD», que hoy **termina sin punto final**. ACCIÓN: la registra `Leyenda_tablas.md`; aquí solo se remite. Su alcance queda cerrado con la decisión de **A5**. `Word`
- [ ] **A15** · SEDE: el encabezado de página de las 13 páginas del Apéndice A, que lleva «Capítulo 6. Conclusiones». ACCIÓN: corregirlo. ⚠️ NO VERIFICADO: los encabezados de página no están en el volcado del cuerpo. `Word`

---

## Bibliografía · decisiones

- [ ] **B1** · **DECISIÓN:** las obras huérfanas. ACCIÓN: rescatar con marcador o excluir del `.docx`. **No borrar antes de hacer los Anexos C y D.** Muchas no son descarte sino sede pendiente (2.19–2.23, 3.7, 4.14, 5.25, A14, X32). `vault`
- [ ] **B2** · SEDE: las entradas `[1]`, `[9]`, `[10]` y `[11]` de la bibliografía, hoy URLs desnudas. ACCIÓN: darles formato IEEE y fusionar `[9]` en `[8]` (duplica el enlace de Stallings). `Word`
- [ ] **B3** · SEDE: las entradas `[2]` («Computer Security Threat Monitoring and Surveillance». James P. Anderson Co.) y `[8]` («Computer Security : Principles and Practice» William Stallings). ACCIÓN: añadir el año 1980 a Anderson, y a Stallings el año, la 5.ª edición, el coautor Brown y la editorial Pearson. `Word`
- [ ] **B5** · **DECISIÓN:** los dos matches aproximados, `[65]` McHugh y `[75]` Moustafa y Slay (§5.3 «Dos matches solo aproximados» del mapa). ACCIÓN: confirmarlos antes de pegar. `[65]` **ya está pegado hoy** en «La crítica original a la metodología de evaluación del DARPA/KDD se remonta a [65]»: confirmarlo es urgente. `Word`

---

# Anexo C · Dónde va exactamente cada cita

Hoja de trabajo: se recorre con el `.docx` abierto y **se localiza cada fila por su fragmento
literal (Ctrl+F)**. El marcador va al final de la frase, antes del punto, y **siempre a pelo**.

> [!important] Sin números de párrafo
> La columna «Párr.» se ha retirado de todo el anexo: procedía de un volcado de ~2.793 párrafos y
> hoy el documento tiene 2.968. Todos los números estaban desplazados y mandaban a la frase
> equivocada. La regla del proyecto («referenciar por título, nunca por `fichero:línea`») los
> prohíbe como referencia única.

> [!note] Las reescrituras ya no viven aquí
> La antigua §C.0 se ha promovido íntegra al bloque **🔴 PRIORITARIO** del principio del fichero,
> revalidada contra los 94 marcadores del `.docx` actual. **§C.2 y §C.3 se han retirado por
> completo: sus 15 marcadores ya están puestos y correctos en el documento.**

## C.1 · Capítulo 1

✅ **Retirada:** el `[14]` ya está puesto en «…el de detección basada en el estado. Este último
monitorea las sesiones de red, con el objetivo de detectar anomalías en el flujo de comunicación [14]».

## C.4 · Capítulo 2 · §2.1.5 «Métricas» (5 filas vivas)

Las de las ecuaciones van **en la frase que introduce la fórmula**, no en la fórmula.

| ☐ | Buscar este texto | Marcador | Qué obra es |
|---|---|---|---|
| ☐ | «Precisión: De todas las veces que el sistema levantó una alarma de ataque» | `[34]` ⚠️ nivel 2 | Powers (2011) |
| ☐ | «se calculan primero por clase, con el esquema uno-contra-el-resto» | `[35]` | Sokolova y Lapalme (2009). ⚠️ el `[35]` de ese párrafo está al **final**; decidir si basta |
| ☐ | «Su resumen numérico habitual es el área bajo la curva (AUC-ROC)» | `[33]` | Fawcett (2006) |
| ☐ | «la curva ROC puede resultar engañosamente optimista» | `[38]` | Davis y Goadrich (2006). ⛔ **SIN ANCLA — no se pega a ciegas**: el fragmento no aparece literal en el `.docx` |
| ☐ | «Tasa de falsos positivos (FPR): de todo el tráfico normal, qué proporción se marcó por error como ataque» | `[33]` | Fawcett (2006) |

✅ **Retiradas por resueltas:** «La matriz de confusión es el punto de partida…» `[33]`,
«Exhaustividad (recall)…» `[34]`, «F1: la media armónica…» `[36]`, «Macro: se calcula la métrica de
cada clase…» `[35]`, «Enfrenta la precisión frente al recall…» `[38]`.

## C.5 · Capítulo 2 · §2.2 (11 filas vivas)

| ☐ | Buscar este texto | Marcador | Qué obra es |
|---|---|---|---|
| ☐ | «procede de las campañas de evaluación… del MIT Lincoln Laboratory para DARPA (1998)» | añadir `[44]` junto al `[43]` ya puesto | Tavallaee *et al.* (2009) |
| ☐ | «Ejemplos en el dataset: neptune (inundación de segmentos SYN…» | `[45]` | Kendall (1999) |
| ☐ | «Ejemplos en el dataset: nmap, portsweep, ipsweep, satan» | `[45]` | Kendall (1999) |
| ☐ | «Ejemplos en el dataset: guess_passwd (fuerza bruta o adivinación de contraseñas)» | `[45]` | Kendall (1999) |
| ☐ | «Ejemplos en el dataset: buffer_overflow, rootkit, loadmodule, perl» | `[45]` | Kendall (1999) |
| ☐ | «Una intrusión es cualquier acción, intencionada o no, que compromete la confidencialidad» | `[14]` | Scarfone y Mell (2007) |
| ☐ | «Sensor o captura. Obtiene el tráfico del segmento vigilado» | `[14]` | Scarfone y Mell (2007) |
| ☐ | «es la modalidad que convierte al detector en un IPS» | `[14]` | Scarfone y Mell (2007) |
| ☐ | «El conocimiento del analista de seguridad queda así codificado en una base de firmas» | `[11]` | Roesch (1999) — el `[11]` del `.docx` **es Snort** |
| ☐ | «entronca con la tradición de Snort» | `[11]` | Roesch (1999). ⛔ **SIN ANCLA — no se pega a ciegas**: no aparece literal en el `.docx` |
| ☐ | «alta precisión sobre lo que cubre, alertas explicables y bajo volumen de falsas alarmas» | `[40]` | García-Teodoro *et al.* (2009). ⛔ **SIN ANCLA — no se pega a ciegas** |

✅ **Retiradas por resueltas:** las anclas de `[39]`, `[40]` (taxonomía), `[41]`, `[42]`, `[43]`,
«monitoriza de forma continua los eventos…» `[14]`, «Se diferencia en este punto entre HIDS y
NIDS» `[14]`, y las dos de Denning `[3]`.

## C.6 · Capítulo 2 · §2.3 (1 fila viva)

| ☐ | Buscar este texto | Marcador | Qué obra es |
|---|---|---|---|
| ☐ | «Un modelo de amenaza es la especificación explícita de las hipótesis sobre el adversario» | `[CITA: Shostack, *Threat Modeling: Designing for Security*, 2014]` | Sin número en el `.docx` — tarea **2.24** |

✅ **Retiradas por resueltas:** `[47]` LeCun, `[48]` Scheirer, y las dos apariciones de `[49]` en los
pitfalls P9 y P10 (que **sí necesitan reescritura**: ver X4 y X5).

## C.7 · Capítulo 3 (1 fila viva)

| ☐ | Buscar este texto | Marcador | Qué obra es |
|---|---|---|---|
| ☐ | «Error de reconstrucción: reconstruye mal lo que no se parece a lo normal» (celda de la Tabla 3.2) | `[6]` | Goodfellow, Bengio y Courville (2016) — tarea **3.1** |

✅ **Retiradas por resueltas:** `[29]`, `[30]`, `[31]`, `[24]`, `[53]` y `[55]`, todas puestas ya en
las celdas de las tablas de candidatos.

## C.8 · Capítulo 4 (6 filas vivas)

| ☐ | Buscar este texto | Marcador | Qué obra es |
|---|---|---|---|
| ☐ | «se entrena un RandomForestClassifier (100 árboles, class_weight='balanced', semilla 42)» | `[24]` | Breiman (2001). ⛔ **SIN ANCLA — no se pega a ciegas**: el fragmento no aparece literal |
| ☐ | «las muestras sintéticas se interpolan a partir de vecinos reales» | `[55]` + `[52]` | Chawla *et al.* (2002) · Kapoor y Narayanan (2023). ⛔ **SIN ANCLA — no se pega a ciegas** |
| ☐ | «las conexiones anómalas se reconstruyen mal y producen un MSE alto» | `[67]` | Sakurada y Yairi (2014). ⛔ **SIN ANCLA — no se pega a ciegas** |
| ☐ | «una de las cinco categorías canónicas de la literatura de NSL-KDD» | `[45]` + `[44]` | Kendall (1999) · Tavallaee *et al.* (2009). ⛔ **SIN ANCLA — no se pega a ciegas** |
| ☐ | «Su coste de entrenamiento es O(n²) en memoria y tiempo, lo que hace inviable ajustar 9 configuraciones» | `[30]` | Schölkopf *et al.* (2001) |
| ☐ | «≈4·10⁶ flujos/s a 54 características» | `[CITA: medición propia, artefacto de `Resultados/`]` | ⛔ **SIN ANCLA — no se pega a ciegas**: no aparece literal. Si reaparece, respaldarlo con el artefacto en nota al pie |

✅ **Retiradas por resueltas:** `[60]` imbalanced-learn, `[61]` KS, `[65]` McHugh, `[46]` Lee y
Stolfo («Las 41 características se agrupan en tres familias… [46]») y el par `[44]`+`[72]`.
El `[63]`+`[64]` de KDD Cup 99 **no está resuelto**: es el error **X27**.

## C.9 · Capítulo 5 (4 filas vivas)

| ☐ | Buscar este texto | Marcador | Qué obra es |
|---|---|---|---|
| ☐ | «Comparación pareada (semilla a semilla)» | `[69]` + `[70]` — complementarias | Demšar (2006) · Dietterich (1998). ⛔ **SIN ANCLA — no se pega a ciegas**: no aparece literal |
| ☐ | «su coste de entrenamiento O(n²) hace inviable ajustarlo con el conjunto completo» | `[30]` | Schölkopf *et al.* (2001). ⛔ **SIN ANCLA** — la formulación literal está en el cap. 4, no en el 5 |
| ☐ | «el patrón dominante en la literatura sobre NSL-KDD: un RandomForest monolítico entrenado sobre todo el train» | `[12]` + `[44]` | Khraisat *et al.* (2019) · Tavallaee *et al.* (2009). ⚠️ «RandomForest monolítico» no está verificado en fuente: atenuar a «clasificador supervisado monolítico» si aprietan |
| ☐ | «El célebre "~99 % de accuracy" de la literatura no sobrevive al test oficial del NSL-KDD» | `[44]` | Tavallaee *et al.* (2009) |

⛔ **Pineau `[68]` sigue sin ancla literal propia.** Lo accionable hoy son sus dos reescrituras,
**X23** y **X24**.

## C.10 · Capítulo 6 (1 fila viva)

| ☐ | Buscar este texto | Marcador | Qué obra es |
|---|---|---|---|
| ☐ | «frente al enfoque supervisado que domina la literatura sobre el NSL-KDD» | `[12]` | Khraisat *et al.* (2019) |

## C.11 · Trazabilidad al vault (no se usa al pegar)

Solo para volver a `Bibliografía.md`. **Nunca se escribe en el Word.**

| `.docx` → vault | | | |
|---|---|---|---|
| `[11]`→`[26]` · `[12]`→`[31]` · `[13]`→`[77]` · `[14]`→`[25]` | `[16]`→`[79]` · `[17]`→`[12]` · `[22]`→`[83]` · `[23]`→`[84]` | `[24]`→`[85]` · `[25]`→`[86]` · `[26]`→`[87]` · `[27]`→`[88]` | `[28]`→`[30]` · `[29]`→`[73]` · `[30]`→`[89]` · `[31]`→`[75]` |
| `[32]`→`[90]` · `[33]`→`[91]` · `[34]`→`[93]` · `[35]`→`[92]` | `[36]`→`[94]` · `[38]`→`[95]` · `[39]`→`[96]` · `[40]`→`[29]` | `[41]`→`[21]` · `[42]`→`[33]` · `[43]`→`[97]` · `[44]`→`[23]` | `[45]`→`[36]` · `[46]`→`[59]` · `[47]`→`[98]` · `[48]`→`[61]` |
| `[49]`→`[18]` · `[51]`→`[52]` · `[52]`→`[17]` · `[53]`→`[99]` | `[55]`→`[100]` · `[60]`→`[102]` · `[61]`→`[103]` · `[64]`→`[58]` | `[65]`→`[22]` · `[67]`→`[108]` · `[68]`→`[20]` · `[69]`→`[109]` | `[70]`→`[110]` · `[71]`→`[49]` · `[72]`→`[74]` · `[74]`→`[51]` · `[75]`→`[50]` |

---

# Anexo D · Anclas de las citas medias

Mismo criterio que el Anexo C: Ctrl+F del fragmento, marcador al final de la frase, **sin números de
párrafo**. Son **defendibles sin cita**, pero suman rigor: si vas justo de tiempo, haz primero el
Anexo C y las reescrituras del bloque prioritario.

## Capítulo 1

| Buscar este texto | Marcador |
|---|---|
| «Se han creado algoritmos basados tanto en Machine Learning (ML) como en IA» | `[12]` Khraisat *et al.* 2019 |
| «estos algoritmos han sido fundamentales para la detección de ataques desconocidos» | `[13]` Hindy *et al.* 2020 — ⚠️ se cita por el método, **no** por su 89-99 % |
| «Evasión del IDS/NIDS – el atacante conoce el mecanismo de detección y lo esquiva» | `[14]` NIST SP 800-94 |

## Capítulo 2 · §2.1.1–2.1.3

| Buscar este texto | Marcador |
|---|---|
| «los investigadores han perseguido enseñar a las computadoras a razonar» | `[15]` Russell y Norvig |
| «el algoritmo es el conjunto de instrucciones que dicen como aprender de los datos» | `[5]` Géron |
| «se limpian, transforman y dividen en subconjuntos de entrenamiento, validación y prueba» | `[17]` Hastie |
| «Reducción de dimensionalidad y visualización» | `[18]` Jolliffe |
| «Reglas de asociación, que busca encontrar coocurrencias frecuentes» | `[19]` Agrawal y Srikant |
| «Un agente aprende por interacción con un entorno, guiado por recompensas y penalizaciones» | `[20]` Sutton y Barto |
| «un candidato algo peor pero mucho más estable puede ser preferible» | `[17]` Hastie |
| «los valores que el algoritmo no aprende de los datos— mediante validación cruzada» | `[5]` + `[21]` Kohavi |

## Capítulo 2 · §2.1.5 «Métricas»

| Buscar este texto | Marcador |
|---|---|
| «VP (verdadero positivo): un ataque correctamente señalado como ataque» | `[33]` Fawcett |
| «la matriz pasa a ser de k x k, con k el número de clases» | `[35]` Sokolova y Lapalme |
| «Exactitud (accuracy): la proporción de predicciones correctas sobre el total» | `[35]` Sokolova y Lapalme |
| «un weighted alto, porque el peso n_i de la clase mayoritaria domina la suma» | `[37]` He y García |
| «no produce directamente una etiqueta, sino una puntuación continua» | `[33]` Fawcett |

## Capítulo 2 · §2.2 y §2.3

| Buscar este texto | Marcador |
|---|---|
| «el momento del análisis: tiempo real… y diferido (offline)» | `[14]` NIST SP 800-94 |
| «los 39 tipos de ataque específicos presentes en el corpus» | `[44]` Tavallaee *et al.* |
| «Huella en el tráfico» (las cuatro apariciones) | `[46]` Lee y Stolfo |
| «designan conjuntos anidados: cada uno es un subconjunto estricto del anterior» | `[4]` Chio y Freeman — ya usada antes |
| «equivale a suponer un adversario que no modifica su comportamiento en respuesta a la defensa» | `[50]` Biggio y Roli |

## Capítulo 3

| Buscar este texto | Marcador |
|---|---|
| «las cuatro categorías canónicas del dataset NSL-KDD» | `[44]` Tavallaee *et al.* |
| «siguiendo la línea de un IDS clásico basado en reglas» | `[11]` Roesch |
| «instanciar el caso, es decir, fijar un valor concreto en cada dimensión» | `[49]` Arp *et al.* |
| «produce puntos que ningún atacante real podría generar» | `[51]` Pierazzi *et al.* |
| «al no re-particionar el test, D2 conserva los tipos de ataque que no aparecen en el entrenamiento» | `[44]` Tavallaee *et al.* |
| «se ajustan únicamente sobre el tráfico de entrenamiento (D1+D3)» | `[52]` Kapoor y Narayanan |
| «del árbol de decisión se extraen reglas legibles (mediante export_text)» | `[54]` Molnar |
| «estimadas fuera de muestra (out-of-fold, mediante validación cruzada sobre D3)» | `[56]` Chow |

## Capítulo 4

| Buscar este texto | Marcador |
|---|---|
| «Python es el lenguaje de referencia para el aprendizaje automático» | ⛔ **SIN NÚMERO — tarea 4.13: atenuar o retirar** |
| «Núcleo de ML: preprocesamiento (MinMaxScaler, LabelEncoder)» (fila de la tabla) | `[59]` Pedregosa |
| Filas de NumPy · Pandas · Matplotlib · Seaborn de la misma tabla | `[57]` Harris · `[58]` McKinney · `[62]` Hunter · `[63]` Waskom |
| «etiquetaron cada registro de KDDTest+ con un valor de #successfulPrediction» | `[44]` Tavallaee *et al.* |
| «desde tasas en [0,1] hasta contadores de bytes con valores de cientos de millones» | `[5]` Géron |
| «Se codifican mediante One-Hot Encoding (pd.get_dummies)» | `[5]` Géron |
| «selección de modelo sobre el conjunto de test, es decir data snooping» | `[49]` Arp *et al.* |
| «LocalOutlierFactor se instancia con novelty=True» | `[66]` doc. scikit-learn ⚠️ fijar en Zotero la página de `LocalOutlierFactor`, no la de `GridSearchCV` |
| «un clasificador que nunca predijera u2r conservaría un accuracy superior al 99,9 %» | `[37]` He y García |
| «las firmas deben poder leerse, auditarse y, llegado el caso, trasladarse a reglas» | `[54]` Molnar |
| «Es la firma canónica de un SYN flood tipo neptune» | `[45]` Kendall |

## Capítulo 5

| Buscar este texto | Marcador |
|---|---|
| «Su noción de anomalía basada en densidad local no captura bien la separación» | `[31]` Breunig *et al.* |
| «refleja el desplazamiento distribucional D3→D2 propio del NSL-KDD» | `[44]` Tavallaee *et al.* |
| «el sobreajuste es invisible en validación cruzada» | `[17]` Hastie |
| «la captura del tráfico en la interfaz de red, el ensamblado de los paquetes en flujos» | `[41]` Sommer y Paxson |

## Capítulo 6

| Buscar este texto | Marcador |
|---|---|
| «firmas y anomalías no compiten, sino que se complementan» | `[40]` García-Teodoro *et al.* |
| «debido al desplazamiento distribucional entre el tráfico normal de entrenamiento y el de test» | `[44]` Tavallaee *et al.* |
| «ningún algoritmo ni técnica de balanceo (SMOTE, class_weight) logra un rendimiento sólido» | `[37]` He y García + `[55]` Chawla |
| «el clasificador de firmas, cerrado, tiende a asignar con confianza excesiva una categoría conocida» | `[48]` Scheirer / `[71]` Bendale |

---

## Candidatos a recorte

Puntos que repiten algo ya dicho. Cada uno con sus dos sedes literales.

1. **Desbalance 883:1, tabulado dos veces.** Primera: «Este desbalance extremo (ratio ≈ 883:1 entre DoS y U2R) es lo que motiva el mini-experimento de balanceo del capítulo anterior». Repetición: «La proporción entre la clase mayoritaria y la minoritaria es ≈ 883:1. Este desbalance es el que motiva el mini-experimento de balanceo de y la elección sistemática de f1_macro».
2. **Fracaso del baseline, viñeta casi calcada.** Primera: «El baseline también falla donde su CV prometía: su f1_macro cae de 0.909 en validación cruzada sobre el train a 0.472 sobre D2». Repetición: «El baseline también falla donde su validación cruzada prometía: su f1_macro se desploma de 0.909 (CV sobre el train) a 0.472 sobre D2».
3. **El 13,4 % explicado tres veces** (la cifra aparece **siete** veces en total; tres de ellas desarrollan la explicación, que es lo que aquí se propone recortar). Primera: «Este 13,4 % no es un defecto de ejecución, sino el comportamiento que la teoría predice para el mecanismo empleado». Repeticiones: «Es la explicación teórica del 13,4 % de 0-day detectados que llegan a etiquetarse como unknown» y «La consecuencia está medida: de los 0-day que la etapa 1 sí detecta, solo el 13,4 % llegan a etiquetarse unknown».
4. **Justificación del percentil 95, dos veces con el mismo argumento.** Primera: «El umbral se fija en el percentil 95 de la puntuación de anomalía sobre validación, lo que equivale a aceptar por diseño en torno a un 5 % de falsas alarmas». Repetición: «El umbral se fija en el percentil 95 del score de anomalía sobre un subconjunto de validación reservado de D1. Esto equivale a aceptar, por diseño, una 5% de los falsos positivos».
5. **Tabla de subconjuntos D1/D2/D3, duplicada entre capítulos.** Primera: pie «Tabla 3.1. Subconjuntos especializados derivados del NSL-KDD: contenido de cada uno y etapa del sistema a la que sirve». Repetición: pie «Tabla 4.7. División especializada del NSL-KDD en D1, D2 y D3, con su tamaño y su función experimental».
6. **Adversario estático, argumentado dos veces.** Primera: «Medir un detector sobre un conjunto de tráfico fijo equivale a suponer un adversario que no modifica su comportamiento en respuesta a la defensa». Repetición: «Evaluar sobre un conjunto de tráfico fijo equivale a suponer un adversario estático, que no modifica su comportamiento en respuesta a la defensa».
7. **`snmpgetattack` como punto ciego, dos veces.** Primera: «snmpgetattack es un punto ciego universal (los cuatro detectores lo fallan, en ambos conjuntos de características)». Repetición: «El tipo de ataque snmpgetattack (n = 178) lo fallan los cuatro detectores en los dos conjuntos de características».
8. **«Patrón dominante en la literatura», tres veces.** Primera: «enfrenta el sistema híbrido al patrón dominante en la literatura sobre NSL-KDD: un RandomForest monolítico». Repeticiones: «…el sistema híbrido completo frente al patrón dominante en la literatura sobre NSL-KDD» y «Baseline no trivial: RandomForest monolítico de cinco clases, que además es el patrón dominante en la literatura sobre este dataset (5.3)».
9. **Complementariedad firmas/anomalías, dos cierres consecutivos.** Primera: «En síntesis, el capítulo demuestra con datos que un enfoque híbrido orientado a la detección de lo desconocido aporta una capacidad que el clasificador monolítico… no tiene». Repetición: «La conclusión de fondo es que firmas y anomalías no compiten, sino que se complementan».
10. **Rótulo «Métricas de desempeño», tres veces como Título 3.** En §5.1, en §5.2 y en el índice como «A.2. Métricas de desempeño»: los tres apuntan a contenidos distintos y el índice no permite distinguirlos.

---

## Resueltas y retiradas en el repaso del 2026-08-25

- **T1** · Mapa `[1]`–`[11]` verificado entre vault y `.docx` · resuelto
- **T2** · Cita `[9]` del vault remapeada · resuelto
- **T8 (parte)** · «¡Error! Marcador no definido.» · 0 ocurrencias en el `.docx` actual · resuelto
- **T6 (desglose)** · Todo el detalle de pies de tabla · trasladado a `Leyenda_tablas.md`, no se duplica
- **1.4** · Comparación contra el clasificador monolítico en el cap. 6 · resuelto
- **1.5** · «Detección basada en el estado» cita NIST SP 800-94 · resuelto
- **2.1** · §2.1.4 cita los 14 algoritmos · resuelto
- **2.2** · §2.1.5 cita `[33]`–`[38]` · resuelto
- **2.3 · 2.4 · 2.5 · 2.6** · §2.2.2 a §2.2.5 citadas · resuelto
- **2.7** · §2.3.3 «Límites y consideraciones éticas» · **ya existe en el `.docx`** como Título 3 · resuelto
- **2.8** (y su fila de **C.6**) · Cita textual «each paper suffers from at least three pitfalls» · **ya tiene marcador**: el párrafo termina en «…y no en el capítulo de resultados [49]» · resuelto
- **2.9** · Localizadores de página derogados el 2026-08-24 · resuelto
- **3.2** · Tabla de candidatos de firmas citada · resuelto
- **3.3** · SMOTE citado en §3.5.4 · resuelto
- **4.1** · Sin placeholders en el cuerpo · resuelto
- **4.6** · Figuras 4.6 y 4.7 · **ya no aplica**: Francisco las borró a propósito por duplicar la 4.1 y la 4.2; la serie 4.1–4.5 está completa y con pie
- **5.10** · Criterios C1–C7 · enunciados uno a uno («una rejilla propia de siete criterios (C1-C7)») · resuelto
- **5.14** · Referencia de §5.1 a las 122 características · resuelto
- **5.16** · Las 53 líneas en Markdown son hoy la Tabla 5.10 · resuelto
- **5.20** · Pie pegado de la Figura 5.11 y markup XML tras la 5.12 · el markup se fue; el pie pegado de la Figura 5.11 lo lleva `Leyenda_tablas.md` bajo **T6**
- **5.23 (parte)** · «dispes» y «7 vecesmayor» · corregidos · resuelto
- **6.1** · §6.2 «Líneas futuras» redactada · resuelto
- **6.2** · Data snooping en «Limitaciones» · resuelto
- **6.3** · «disciplina anti-leakage estricta» · hoy dice «La disciplina anti-leakage del trabajo es acotada» · resuelto
- **6.8** · Respuesta a los objetivos específicos · resuelto: cuatro bloques A–D cubren los nueve objetivos
- **A2** · Las dos tablas Markdown con pipes son hoy tablas reales de Word · resuelto
- **A4** · Viñetas con guion literal · 0 ocurrencias · resuelto
- **A16** · Rotular A.1.5 el apartado de etiquetas · el índice ya lo rotula «A.1.5. Etiquetas: tipos de ataque y categorías» · resuelto
- **B4** · Goodfellow está en la bibliografía del `.docx` · resuelto
- **Huérfanas que se rescatan solas** · sección retirada: su contenido está hoy en **B1** y en las tareas de sede (2.19–2.23, 3.7, 4.14, 5.25, A14, X32)
