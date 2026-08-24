# Las tareas de Kiko

Revisión de `Proyecto_Fin_de_Grado-FJLM-2026.docx`, capítulos 1–6 + apéndices + bibliografía.
Cada tarea marca su sede: `vault` = se arregla en la nota `.md` · `Word` = se arregla en el `.docx`.

> **Orden recomendado:** primero el bloque transversal (T), luego capítulo por capítulo.
> La renumeración de la bibliografía (T4) es **la última tarea de todas**: si se hace antes,
> cada cita nueva vuelve a romperla.

> [!important] Numeración del `.docx` — versión del 2026-08-24 (tercera pasada)
> Todos los `[n]` de este fichero están en la **numeración del `.docx`**, reconstruida
> **por orden de aparición leyendo el binario `Proyecto_Fin_de_Grado-FJLM-2026.docx` de
> principio a fin**. Mapa completo en [[Bibliografia del docx - numeracion y anclas]] §2.
> Cuando aparece `(vault [xx])`, ese segundo número es solo la referencia para localizar la
> entrada en `Bibliografía.md`.
>
> **Las dos numeraciones anteriores están retiradas.** Se construyeron recorriendo el vault, y
> el Word no sigue ese orden: leídos de arriba abajo, los marcadores salían con saltos y
> retrocesos. **El `.docx` usa hoy 75 números: `[1]`–`[11]` congelados + `[12]`–`[75]`.**
>
> **Un número por obra.** Una obra citada varias veces conserva el número de su **primera**
> aparición y lo repite en las demás, aunque al leer seguido parezca que la secuencia
> retrocede. **Eso es IEEE correcto**, no un fallo de orden.

> [!danger] Cuatro discrepancias halladas al leer el binario — afectan al plan de trabajo
> 1. **El cuerpo del `.docx` ya tiene 50 marcadores, no 11** —y tampoco 46, cifra que estuvo
>    escrita aquí y era falsa—. Además de los 11 del rango congelado hay **39 apariciones con la
>    numeración VIEJA del vault ya pegadas** (`[17]`, `[18]`×6, `[20]`×2, `[23]`×6, `[24]`×3,
>    `[25]`×3, `[31]`, `[49]`×2, `[50]`, `[51]`, `[52]`, `[61]`×2, `[62]`, `[63]`, `[64]`, `[65]`,
>    `[66]`, `[67]`, `[74]`×2, `[77]`) que **colisionan** con la nueva: en el Word hay un `[23]`
>    puesto por Tavallaee, pero ahora **`[23]` es Dietterich 2000**.
>    **El pase de Word es de REESCRITURA, no de inserción.** Desglose párrafo a párrafo en
>    [[Bibliografia del docx - numeracion y anclas]] §5.1.
> 2. **§6.2 «Líneas futuras» NO está vacía** (párrafos 2179–2549). El mapa anterior lo afirmaba y
>    es falso: ahí viven **CIC-IDS2017** y **UNSW-NB15**, que por eso reciben `[74]` y `[75]`.
> 3. **Dos matches solo aproximados** — `[65]` McHugh y `[75]` Moustafa y Slay: el fragmento
>    literal no aparece verbatim y la sede se infirió por contenido. **Confirmarlos antes de
>    pegar.** **Chow ya no está en esta lista:** su sede real es el párrafo 800 (§3.5.5), con
>    ancla literal, y es `[56]`.
> 4. **Quedan 3 placeholders sin resolver** en el cuerpo: 2 de `[ enlace bibliografía: …]` y 1
>    de `[CITA: …]`.
>
> **Y un número sin ancla:** `[68]` Pineau no tiene entrada en el Anexo C. **No se puede pegar**
> hasta que se establezca su fragmento literal; no se inventa.

---

## T · Transversal (afecta a todo el documento)

### Bibliografía
- [X] **T1** · Verificar el mapa `[1]`–`[11]` entre el vault y el `.docx` antes de congelarlo. **RESUELTO:** el `[11]` **del `.docx`** es Snort/Roesch (= `[26]` del vault); el `[11]` **del vault** es CRISP-DM y **no tiene sede en el `.docx`**, así que no recibe número. `vault`
- [X] **T2** · Corregir la cita `[9]` **del vault** (cap. 2): es un número **quemado**, no existe entrada. Remapear a `[8]` o `[10]`, que son los mismos números en ambas numeraciones. `vault`
- [ ] **T3** · Volcar al Word las 75 entradas de la lista final ([[Bibliografia del docx - numeracion y anclas]] §3). Hoy el `.docx` tiene 11 escritas a mano y sin relación con el vault. `Word`
- [ ] **T4** · **(ÚLTIMA)** Aplicar la numeración `[12]`–`[75]` **solo en el `.docx`**, por orden de aparición en el Word. `[1]`–`[11]` se congelan. **El vault NO se renumera** (corregida la redacción anterior, que decía «en el vault y en el `.docx` a la vez»). Incluye **reescribir los 39 marcadores viejos** ya pegados (repartidos en 47 párrafos; el recuento «35» era falso). `Word`

### Maquetación
- [ ] **T5** · Eliminar los **21 wikilinks** `[[…]]` que sobrevivieron al volcado y sustituirlos por «véase §x.y». `Word`
- [ ] **T6** · Numerar y poner pie a **todas** las tablas del documento. Hoy no hay **ni una** con pie `Tabla x.y`. `Word`
- [X] **T7** · Llamar cada figura por su número desde la prosa («véase Figura 5.3»), no «las figuras siguientes». `vault`
- [X] **T8** · Actualizar los campos del índice en Word: pagina secciones que ya no existen y muestra dos entradas sin título. `Word`
- [X] **T9** · Borrar el **Apéndice B de plantilla** («Este texto está escrito en estilo Título 7/8») y el glosario de acrónimos que termina en `KJDFSLDLKJ`. `Word`

---

## Capítulo 1 · Introducción

**Citas:** 4 marcadores. Faltan 4 (1 alta, 3 medias) → ver Anexo A.

### Estructura
- [ ] **1.1** · Fundir 1.1 Motivación y 1.2 Preliminares: las dos hacen historia y se solapan. `vault`
- [ ] **1.2** · Subir el gancho del trabajo. Hoy «Este último punto es precisamente el que motiva el presente trabajo» es la última viñeta de una lista. `vault`
- [ ] **1.3** · Fundir los dos objetivos específicos que dicen lo mismo (medir la detección de desconocidos aparece dos veces). `vault`
- [ ] **1.4** · Decidir qué pasa con la promesa del objetivo general: comparar contra «cada etapa por separado **o** un clasificador monolítico». Solo se cumple la segunda mitad. O se cumple en el cap. 6, o se retira de aquí. `vault`

### Bibliografía
- [ ] **1.5** · Citar la «detección basada en el estado» → NIST SP 800-94 = `[14]`. `vault`
- [ ] **1.6** · Añadir las 3 citas medias del Anexo A. `vault`

---

## Capítulo 2 · Marco Teórico

**Citas:** 6 marcadores en 368 líneas. Faltan **67 (49 altas)** → ver Anexo A. Es el capítulo con el problema más grande del documento.

### Bibliografía
- [ ] **2.1** · **2.1.4 «Algoritmos de ML» — cero citas.** Añadir las **14 citas altas**: un algoritmo de terceros por cita (CART, Random Forest, Gradient Boosting, LightGBM, k-NN, Isolation Forest, One-Class SVM, LOF, MLP/backprop, autoencoders, k-means, ensembles, one-class). `vault`
- [ ] **2.2** · **2.1.5 «Métricas» — cero citas.** Añadir **10 altas + 5 medias**: matriz de confusión, precisión, recall, FPR, F1, macro/weighted y las **siete ecuaciones**, todas hoy sin fuente. `vault`
- [ ] **2.3** · Citar 2.2.2 «Sistemas de detección de intrusiones»: definición de intrusión, definición de IDS y la cadena de bloques del NIDS (4 altas). `vault`
- [ ] **2.4** · Citar 2.2.3 «Taxonomía de los IDS»: los cuatro ejes, HIDS/NIDS, inline/pasivo (5 altas). `vault`
- [ ] **2.5** · Citar 2.2.4 «Firmas frente a anomalías» y mapear Denning a `[3]` y Snort a `[11]` (5 altas). `vault`
- [ ] **2.6** · Citar 2.2.5 «Taxonomía de ataques»: DARPA/KDD y los ejemplos de cada categoría (5 altas). `vault`
- [ ] **2.7** · Citar 2.3 entera. ⚠️ **Ojo:** §2.3.3 «Límites y consideraciones éticas» **no existe en el `.docx`**, y por eso Rudin, RGPD, Reglamento de IA y NIS2 **no reciben número** (§4 del mapa). Si se volca la sección, esas cuatro entran **por detrás del `[75]`**. `vault`
- [ ] **2.8** · Poner marcador a la **cita textual en inglés** («each paper suffers from at least three pitfalls»): está entrecomillada y sin `[49]` Arp *et al.* `vault`
- [x] ~~**2.9** · Poner localizador de página a `[4]` Chio, `[5]` Géron (×2), `[7]` Murphy y `[8]` Stallings.~~ **ANULADA el 2026-08-24:** Francisco derogó los localizadores dentro del marcador — se escribe `[4]`, no `[4, p. 45]`. La página de cada afirmación se sigue registrando, pero en la columna «Localizador por uso» de `Bibliografía.md`, no aquí. `vault`

### Estructura
- [ ] **2.10** · **Añadir estado del arte / trabajos relacionados.** Es la carencia estructural más grave del TFG. Material aprovechable ya redactado en §5.4. `vault`
- [ ] **2.11** · Cumplir la promesa de §2.2.4: los tres trabajos que adoptan, invierten y paralelizan la cascada. Hoy se anuncian y no aparecen. `vault`
- [ ] **2.12** · Arreglar «dentro del sentido (a) fijado más arriba» (§2.2.4): apunta a un texto que se borró. `vault`
- [ ] **2.13** · Subir «IA, ML y DL» al principio del capítulo. Hoy §2.3 define lo que §2.1 lleva usando 300 líneas. `vault`
- [ ] **2.14** · Entregar los cuatro tramos que anuncia §2.3.2. Faltan «la cara ofensiva» y «el panorama de datasets». `vault`
- [ ] **2.15** · Arreglar el salto de nivel de 2.1.3: usa Título 3 y sus hijos saltan a **Título 5**. Se ve en el índice. `Word`

### Recortes
- [ ] **2.16** · Comprimir §2.3.3 (P9): desarrolla cuatro factores para concluir que no aplica. `vault`
- [ ] **2.17** · Dejar la justificación one-class en un solo sitio (hoy en 2.1.2, 2.1.4 y 3.4.1). `vault`

### Redacción
- [ ] **2.18** · Corregir `Aviability` → **Availability**. `vault`

### Decisiones pendientes de Francisco (bibliografía sin equivalente en el `.docx`)
- [ ] **2.19** · **Bergstra y Bengio, *Random Search***. Sin equivalente en el `.docx`: su única cita viva estaba en `A.3`. Tocaría en §2.1.3 «Ciclo de vida», al hablar de la búsqueda de hiperparámetros. **Decidir:** escribir la frase que la sostenga en §2.1.3, o descartar la entrada. `vault`
- [ ] **2.20** · **Erickson *et al.*, TabArena** · **Micci-Barreca, *target encoding*** · **Pargent *et al.*, *regularized target encoding***. Sin equivalente en el `.docx`. Sede natural: §2.1.2/§2.1.4 (benchmarks tabulares) y §2.1.3 (codificación de categóricas). **Decidir:** dar sede o descartar. `vault`
- [ ] **2.21** · **Hwang *et al.*, hybrid IDS con firmas ponderadas.** Sin equivalente en el `.docx`. **Va junto a las tareas 2.10 y 2.11**: es material directo del estado del arte y uno de los híbridos que §2.2.4 promete. Si se escriben esas dos tareas, Hwang entra sola y necesita **el siguiente número libre por detrás del `[75]`**. `vault`
- [ ] **2.22** · **Pendlebury *et al.*, TESSERACT.** Sin equivalente en el `.docx`. Sede natural: §2.3.3, junto a `[49]` Arp *et al.* y el sesgo temporal de la evaluación. Depende de que §2.3.3 se volque (ver 2.7). **Decidir:** dar sede o descartar. `vault`
- [ ] **2.23** · **Behrouz *et al.*, Nested Learning.** Sin equivalente en el `.docx`. Sin sede clara en el marco teórico actual; si no se le encuentra una, **es un descarte limpio**. `vault`
- [ ] **2.24** · **Shostack 2014** / la frase «Un modelo de amenaza es la especificación explícita de las hipótesis sobre el adversario». **Su ancla NO existe en el `.docx`.** Sede que le tocaría: §2.3.2–§2.3.3 (modelo de amenaza), con reflejo en §3.1. **Decidir: escribir la frase —y entonces la cita entra— o descartarla.** Hoy no hay alta y no consume número. `vault`

---

## Capítulo 3 · Diseño del sistema

**Citas:** **1 marcador en todo el capítulo**. Faltan 11 (3 altas) → ver Anexo A.

### Bibliografía
- [ ] **3.1** · Citar los cuatro algoritmos de la tabla de candidatos de anomalías (§3.4.2): Isolation Forest `[29]`, One-Class SVM `[30]`, LOF `[31]` y autoencoder `[6]`. `vault`
- [ ] **3.2** · Citar la tabla de candidatos de firmas (§3.5.2): Random Forest `[24]` y boosting/XGBoost `[53]`. `vault`
- [ ] **3.3** · Citar **SMOTE** `[55]` en §3.5.4. Se nombra como decisión de diseño sin fuente. `vault`
- [ ] **3.4** · Añadir las 8 citas medias del Anexo A (categorías canónicas, anti-leakage, espacio-problema adversario, regla de presupuesto). `vault`

### Estructura
- [ ] **3.5** · Mover la medición de la **cascada invertida** al capítulo 5. Hoy da cifras de resultados (6.558/9.711, 67,53 %) dentro de Diseño, antes de que el lector conozca el protocolo. `vault`
- [ ] **3.6** · Dejar la confesión de **data snooping** en un solo sitio. Hoy está en §3.3.3 y en §4.3.5 casi con las mismas palabras. `vault`

### Decisiones pendientes de Francisco
- [ ] **3.7** · **La comparación tabular de §3.5 no está volcada al `.docx`**, y con ella se caen cuatro entradas que hoy **no reciben número**: Barbará (ADAM), Grinsztajn *et al.*, McElfresh *et al.*, Shwartz-Ziv y Armon, y Hollmann *et al.* (TabPFN). **Decidir:** volcar la comparación —y entonces entran por detrás del `[75]`— o descartarlas de la bibliografía final. `vault` + `Word`

---

## Capítulo 4 · Implementación del sistema

**Citas:** 2 marcadores en 590 líneas. Faltan 22 (11 altas) → ver Anexo A. `4.3`, `4.4` y `4.5` **enteras** no citan nada.

### Bibliografía
- [ ] **4.1** · **Resolver los placeholders visibles de §4.2**: `[enlace bibliografía: KDD Cup 99]` → `[62]` + `[43]`; `[… Tavallaee 2009]` ×2 → `[44]`; `[… McHugh 2000]` → `[63]`; `[CITA: Tavallaee 2009 + survey]` → `[44]` + `[72]`. ⚠️ **Además quedan 3 placeholders más sin resolver en el cuerpo** (2 de `[ enlace bibliografía: …]` y 1 de `[CITA: …]`): localizarlos y cerrarlos en el mismo pase. `vault`
- [ ] **4.2** · Citar las librerías de la tabla de §4.1.3: scikit-learn `[57]`, imbalanced-learn `[58]`, el test KS de scipy `[59]`, matplotlib `[60]`, seaborn `[61]`, NumPy `[55]`, pandas `[56]`. `vault`
- [ ] **4.3** · Citar §4.3: las 41 características (Lee y Stolfo `[46]`), el escalado, el one-hot, **SMOTE + leakage** (`[54]` + `[52]`), y las importancias de Random Forest `[24]`. `vault`
- [ ] **4.4** · Citar §4.4: complejidad O(n²) de One-Class SVM `[30]`, `novelty=True` de LOF `[64]` y el autoencoder como detector de anomalías `[65]`. `vault`
- [ ] **4.5** · Citar §4.5: el argumento de que «el accuracy miente» con u2r `[37]`, la interpretabilidad de las reglas `[66]` y la firma canónica del SYN flood `[45]`. `vault`

### Figuras y tablas
- [ ] **4.6** · **Numerar y poner pie a las 7 figuras del capítulo 4.** Es el único capítulo del documento sin ninguna figura numerada. `Word`

### Estructura
- [ ] **4.7** · Reordenar §4.3 al orden real del pipeline: codificación → normalización → selección. Hoy 4.3.2 dice «sobre la matriz completa post-codificación» y va antes que 4.3.3. `vault`
- [ ] **4.8** · Añadir en §4.3.4 el aviso de que el eje SMOTE vs `class_weight` **no está establecido** entre semillas (lo demuestra §5.2.4). Hoy se presenta como decisión cerrada. `vault`
- [ ] **4.9** · Mover el experimento 54 vs 122 (§4.3.5) o marcarlo claramente como adelanto: da métricas sobre D2 dentro de Implementación. `vault`

### Recortes
- [ ] **4.10** · Dejar el desbalance 883:1 en un solo sitio. Aparece 4 veces (2.2.5, 4.2.1, 4.3.4, 4.3.6). `vault`
- [ ] **4.11** · Dejar el umbral p95 en un solo sitio. Aparece 7 veces en el documento. `vault`
- [ ] **4.12** · No volver a tabular en §4.5.3 los ganadores de balanceo que ya están en §4.3.4. `vault`

### Decisiones pendientes de Francisco
- [ ] **4.13** · **La frase de §4.1 «Python es el lenguaje de referencia para el aprendizaje automático».** ⛔ **No hay fuente académica que la respalde**: lo que existe es prensa sectorial y encuestas de portales, **nivel 3**, que no sostiene una afirmación de la memoria. **Decidir: atenuar la frase** (p. ej. «uno de los lenguajes más extendidos en el ecosistema de ML, y el que usan las librerías empleadas en este trabajo», que sí se sostiene con `[57]` y `[56]`) **o retirarla.** Hoy queda **sin marcador**. `vault`
- [ ] **4.14** · **CRISP-DM** (vault `[11]`). Sin equivalente en el `.docx`: su única cita viva estaba en `A.3`, que no existe en el documento. Sede natural alternativa: §4.1, al describir la metodología de trabajo del proyecto. **Decidir:** darle sede en §4.1 —y entonces entra por detrás del `[75]`— o descartarla. `vault`

---

## Capítulo 5 · Evaluación

**Citas:** 21 marcadores, pero concentrados en §5.0 y en las conclusiones. **§5.1 y §5.2, las dos secciones de resultados, no citan nada.** Faltan 8 (4 altas) → ver Anexo A.

### Rigor — lo primero
- [ ] **5.1** · **Corregir el intercambio D2/D3 en §5.0 «Particiones y su función».** Dice que D2 entrena la etapa 2 y da las OOF, y que D3 es la evaluación. Es al revés. Error más grave del documento. `vault`
- [ ] **5.2** · Reescribir el párrafo de particiones: enumera «D1, D1_train y D1_val» como tres particiones con función exclusiva, cuando D1 es el conjunto y las otras dos su división 80/20. `vault`
- [ ] **5.3** · Citar el `0,8223` **con su banda [0,7779–0,8205] y su media 0,8035 las cuatro veces** que reaparece. Hoy §5.2.4 impone esa regla y el resto del capítulo la incumple. `vault`
- [ ] **5.4** · Dar diccionario a `H-2…H-6`, `P-2`, `P-5`, `Q1/C`, o eliminarlos del cuerpo. `P-2` y `P-5` se usan unas 8 veces sin referente. `vault`
- [ ] **5.5** · Sacar del cuerpo los `commit`, las rutas de `Resultados\` y `EL_FUTURO.md`. A apéndice o nota al pie. `vault`

### Bibliografía
- [ ] **5.6** · Respaldar las dos afirmaciones sobre el estado del arte que sostienen la tesis: «el patrón dominante en la literatura» (`[12]` + `[44]`) y «el célebre ~99 % de accuracy» (`[44]`). Hoy no apuntan a ninguna fuente. `vault`
- [ ] **5.7** · Citar el criterio estadístico pareado vs no pareado de §5.2.4 → `[68]` + `[69]`, **complementarias**. `vault`
- [ ] **5.8** · Citar en §5.1 el LOF `[31]` y la complejidad O(n²) del One-Class SVM `[30]`, hoy explicados sin fuente. `vault`

### Estructura
- [ ] **5.9** · **Crear §5.0 como sección con sus subsecciones.** El texto se refiere 4 veces a `5.0.3`, `5.0.5` y `5.0.6`, que no existen. `vault`
- [ ] **5.10** · **Enunciar los criterios C1–C7.** Hoy solo aparece su respaldo bibliográfico, nunca el criterio en sí. Y «se desarrollan en 5.0.6» remite al propio párrafo. `vault`
- [ ] **5.11** · Titular las subsecciones de §5.3 y §5.4. Hoy son texto plano y en el índice quedan como un bloque ciego frente a §5.1 y §5.2. `Word`
- [ ] **5.12** · Partir §5.4 en **Discusión** (literatura, Hindy, prevalencia, latencia) y **Conclusiones**. Hoy «Conclusiones del capítulo» es donde está el mejor material nuevo. `vault`
- [ ] **5.13** · Unificar el nombre de los apartados de cierre de §5.1 («Resultados finales») y §5.2 («Comparación de los resultados de cada algoritmo»): hacen lo mismo. `vault`
- [ ] **5.14** · Corregir la referencia de §5.1: anuncia que las 122 características se retoman en §5.3, pero están en §5.2.3. `vault`
- [ ] **5.15** · Unificar el estilo de referencia cruzada dentro del capítulo: hoy conviven wikilinks, referencias planas y mixtas. `Word`

### Figuras, tablas y ecuaciones
- [ ] **5.16** · **Convertir a tabla de Word las 53 líneas en Markdown** (`| … |`), incluida la **tabla de recall 0-day por tipo**, que es la aportación defendible del trabajo. `Word`
- [ ] **5.17** · Convertir los 23 `###` y `- ` de Markdown que quedaron como texto plano, y quitar los backticks. `Word`
- [ ] **5.18** · Añadir la **tabla de tiempos y latencia**: §5.4 critica en detalle unas columnas que nunca se muestran. `vault`
- [ ] **5.19** · Renumerar la ecuación de la proyección de prevalencia: `(1)` ya está usada en el capítulo 2. `Word`
- [ ] **5.20** · Arreglar el pie pegado de la Figura 5.11 («…sobre D2 completoFigura 5.11.») y el **markup XML crudo** visible tras la Figura 5.12. `Word`
- [ ] **5.24** · **Eliminar la fila vacía de la tabla del eje de balanceo** en `5.2 Resultados del modelo de detección basado en firmas.md`: la metió el editor de tablas de Obsidian y viaja al `.docx` como fila en blanco. `vault`

### Recortes
- [ ] **5.21** · Dejar los tres hallazgos (complementariedad / 13,4 % / `snmpgetattack`) en un solo sitio. Hoy están en §5.3 y §5.4 casi literales. `vault`
- [ ] **5.22** · Dejar los cuatro puntos del baseline en un solo sitio, por el mismo motivo. `vault`

### Redacción
- [ ] **5.23** · Reescribir las tres frases rotas: «de modo qua ser deriva de código», «mientras que la dispes dos configuraciones comparadas», `7 vecesmayor`. `vault`
      ⚠️ «dispes» está sin resolver: hay que decidir qué debería decir ahí.

### Decisiones pendientes de Francisco
- [ ] **5.25** · **Storkey, *When Training and Test Sets Are Different*** (vault `[78]`). Su ancla de §5.1 **no sobrevive en el `.docx`**, así que **no recibe número**. **Decidir:** reintroducir la frase sobre *dataset shift* en §5.1 —donde encaja con el desplazamiento D3→D2 que el capítulo ya describe— o descartar la entrada. `vault`
- [ ] **5.26** · **Mitchell *et al.*, Model Cards** (vault `[60]`). Sin sede porque `A.3` no existe en el `.docx`. Ligada a **A14**. `vault`

---

## Capítulo 6 · Conclusiones

**Citas:** **cero marcadores en todo el capítulo.** Faltan 5 → ver Anexo A.

### Contenido — lo primero
- [X] **6.1** · **Redactar §6.2 «Líneas futuras».** ✅ **Está redactada** en el `.docx` (párrafos 2179–2549); la afirmación anterior de que estaba vacía era falsa. De ahí salen `[74]` CIC-IDS2017 y `[75]` UNSW-NB15. `vault`
- [X] **6.2** · **Añadir el data snooping a «Limitaciones».** El capítulo 5 declara tres decisiones tomadas mirando el test y el 6 no lo menciona. `vault`
- [ ] **6.3** · **Matizar la frase «bajo una disciplina anti-leakage estricta —umbrales fijados sin ver el test—»**: hoy contradice directamente lo que declara el capítulo 5. `vault`
- [ ] **6.4** · Añadir a «Limitaciones» el supuesto de **adversario estático no adaptativo** del modelo de amenaza de §3.1 → `[50]` Biggio y Roli. `vault`
- [ ] **6.5** · Añadir a «Limitaciones» que el FPR del ~10 % debe leerse **a prevalencia realista** (`[73]` Axelsson, *base-rate fallacy*) y que la latencia publicada es **techo de laboratorio**. `vault`
- [ ] **6.6** · Añadir el titular `f1_macro` 0,8223 **con su banda** y la mención de que es el mejor de once corridas. Hoy el lector termina el TFG sin el número. `vault`
- [ ] **6.7** · Desdoblar el punto de limitaciones que fusiona **u2r y r2l**: el capítulo 5 las mide por separado y se comportan distinto. `vault`

### Estructura
- [ ] **6.8** · Responder a los **tres objetivos específicos** del capítulo 1 que hoy no se contestan: algoritmos de ML, baseline de control y medición crítica de 0-day. `vault`
- [ ] **6.9** · Declarar si el objetivo general de comparar contra «cada etapa por separado» se cumplió (ligada a la tarea 1.4). `vault`
- [ ] **6.10** · Renombrar el Título 2 «Conclusiones» de §6.1 para que no repita literalmente el título del capítulo. `Word`

### Recortes
- [ ] **6.11** · Convertir en conclusión el párrafo que hoy describe lo que hace el capítulo 5, y suprimir la repetición «firmas y anomalías se complementan». `vault`

---

## Apéndices

- [ ] **A1** · **Convertir en tablas reales de Word las cuatro tablas de las 41 características** (~190 líneas). Hoy están volcadas **una celda por párrafo**. `Word`
- [ ] **A2** · Convertir en tablas de Word las dos tablas Markdown con pipes (codificación de categorías y tipos por categoría). `Word`
- [ ] **A3** · Convertir los dos encabezados `###` en Título 8. `Word`
- [ ] **A4** · Aplicar estilo de lista a las 8 viñetas con guion literal. `Word`
- [ ] **A5** · Numerar y poner pie a las seis tablas del apéndice A. `Word`
- [ ] **A6** · Deduplicar el encabezado A.1: hoy Título 6 y Título 7 tienen el mismo texto. `Word`
- [ ] **A7** · Nombrar el Título 1 vacío como «Apéndices» y eliminar el Título 7 vacío que sigue a A.2. `Word`
- [ ] **A8** · Redactar el apéndice A.2 «Métricas de desempeño», hoy solo título. `vault`
- [ ] **A9** · Arreglar la referencia rota «véase 4.3 Preprocesamiento de los datasets sección 4.3.5» → «véase §4.3.5». `vault`
- [ ] **A10** · Corregir la fila `su_attempted`: el tipo dice «Discreta» y la descripción es binaria. `vault`
- [ ] **A11** · Unificar la notación de flags: `s0/s1/s2/s3` en mayúsculas, como en el resto. `vault`
- [ ] **A12** · Sustituir las comillas rectas por comillas españolas (6 apariciones). `Word`
- [ ] **A13** · Dar formato monoespaciado a `program.py`, la ruta de `Resultados\…` y `y_attack/y_category`. `Word`
- [ ] **A14** · **Decidir si se vuelca `A.3 «Ficha del sistema»**, que existe en el vault y **no en el `.docx`**. De ello dependen dos entradas que hoy **no reciben número**: **CRISP-DM** (vault `[11]`, ver 4.14) y **Bergstra y Bengio** (ver 2.19), más la sede principal de **Model Cards** (ver 5.26). `vault` + `Word`

---

## Bibliografía

**Estado medido:** 102 entradas vivas en el vault · **64 reciben número en el `.docx`** (`[12]`–`[75]`) + 10 en el tramo congelado · **20 sin sede** (§4 del mapa) + CRISP-DM y Bergstra y Bengio.

- [ ] **B1** · **Revisar las huérfanas y decidir: se rescatan poniéndoles marcador, o se excluyen del `.docx`.** Con los Anexos C y D colocados, la lista real de descartes **no son 51, sino las 20 de §4 del mapa más 2**. Y de esas, muchas **no son descarte sino sede pendiente de volcar** (tareas 2.7, 2.19–2.24, 3.7, 4.14, 5.25, A14).
      ⚠️ **No borrar antes de hacer las tareas de citas.** `vault`
- [ ] **B2** · Dar formato IEEE a las 4 entradas del `.docx` que son **URLs desnudas** (`[1]`, `[9]`, `[10]`, `[11]`), y fusionar la que duplica el enlace de Stallings. `Word`
- [ ] **B3** · Añadir año y edición al Stallings (5.ª ed., 2023) y año al Anderson. `Word`
- [ ] **B4** · Recuperar `[6]` Goodfellow: existe en el vault y **no llegó al `.docx`**. `Word`
- [ ] **B5** · **Confirmar los tres matches aproximados** — `[63]` McHugh (párr. 864), `[70]` Chow (párr. 1833) y `[75]` Moustafa y Slay (párr. 2300) — **antes de pegar nada**. Si alguno cae en otro párrafo, su número puede moverse. `Word`

---

# Anexo A · Citas faltantes por capítulo

**117 en total: 69 altas y 48 medias.** «Alta» = un tribunal lo señalaría con seguridad (definición de manual, algoritmo de terceros, dato externo).

| Capítulo | Altas | Medias | Total |
|---|---:|---:|---:|
| 1 Introducción | 1 | 3 | 4 |
| 2 Marco Teórico | **49** | 18 | **67** |
| 3 Diseño | 3 | 8 | 11 |
| 4 Implementación | 11 | 11 | 22 |
| 5 Evaluación | 4 | 4 | 8 |
| 6 Conclusiones | 1 | 4 | 5 |

## Las 14 altas de 2.1.4 «Algoritmos de ML»

| Concepto | Cita | Nº `.docx` |
|---|---|---|
| Árbol de decisión | Breiman *et al.* 1984 (CART) | `[22]` (vault `[83]`) |
| Ensembles | Dietterich 2000 | `[23]` (vault `[84]`) |
| Random Forest | Breiman 2001 | `[24]` (vault `[85]`) |
| Gradient Boosting | Friedman 2001 | `[25]` (vault `[86]`) |
| HistGradientBoosting | Ke *et al.* 2017 (LightGBM) | `[26]` (vault `[87]`) |
| k-NN | Cover y Hart 1967 | `[27]` (vault `[88]`) |
| Semisupervisado one-class | Chandola *et al.* 2009 | `[28]` (vault `[30]`) |
| Isolation Forest | Liu, Ting y Zhou 2008 | `[29]` (vault `[73]`) |
| One-Class SVM | Schölkopf *et al.* 2001 | `[30]` (vault `[89]`) |
| LOF | Breunig *et al.* 2000 | `[31]` (vault `[75]`) |
| MLP / retropropagación | Rumelhart, Hinton y Williams 1986 | `[32]` (vault `[90]`) |
| Autoencoder | Goodfellow *et al.* 2016, cap. 14 | `[6]` |
| k-means / clustering | Hastie *et al.*, cap. 14 | `[17]` (vault `[12]`) |

## Las 10 altas de 2.1.5 «Métricas»

Matriz de confusión, precisión (ec. 1), recall (ec. 2), FPR (ec. 3), F1 (ec. 5), macro y ponderado (ec. 6 y 7), curva ROC y AUC, curva PR, y el argumento de que PR es más informativa bajo desbalance.

Fuentes: **`[33]` Fawcett 2006** · **`[34]` Powers 2011** ⚠️ nivel 2 · **`[35]` Sokolova y Lapalme 2009** · **`[36]` van Rijsbergen 1979** · **`[38]` Davis y Goadrich 2006** · **`[37]` He y García 2009**.

## Altas de 2.2 y 2.3

Definición de intrusión y de IDS, cadena de bloques del NIDS, despliegue inline/pasivo (**NIST SP 800-94 → `[14]`**) · ejes de la taxonomía (**Axelsson 2000 → `[39]`**) · propiedades de firmas y anomalías (**García-Teodoro *et al.* → `[40]`**) · deriva y falsos positivos (**Sommer y Paxson → `[41]`**) · DARPA 1998 (**Lippmann *et al.* → `[43]`**) · ejemplos de ataque por categoría (**Kendall → `[45]`**) · criterio de DL (**LeCun, Bengio y Hinton → `[47]`**) · casos de uso defensivos (**`[4]` Chio, con localizador**) · conjunto cerrado (**`[48]` Scheirer**) · los tres usos de Arp *et al.* (**`[49]`, con localizador**).

## Altas de 3, 4, 5 y 6

- **Cap. 3:** los cuatro algoritmos de la tabla de anomalías (`[29]`, `[30]`, `[31]`, `[6]`) · Random Forest `[24]` y XGBoost `[53]` en la de firmas · **SMOTE `[54]`**.
- **Cap. 4:** los placeholders de §4.2 · imbalanced-learn `[58]` · test KS `[59]` · las 41 características (Lee y Stolfo `[46]`) · categorías canónicas · SMOTE + leakage · importancias de RF · O(n²) de OC-SVM `[30]` · autoencoder para anomalías `[65]`.
- **Cap. 5:** «el patrón dominante en la literatura» · «el célebre ~99 %» · comparación pareada (`[68]` + `[69]`) · O(n²) de OC-SVM.
- **Cap. 6:** la afirmación sobre el enfoque supervisado que domina la literatura → `[12]`.

---

# Anexo B · Las huérfanas

Entradas vivas en `Bibliografía.md` que **no se citan ni una vez** en la memoria.
Las marcadas con **←** son las que el texto **sí usa conceptualmente** y solo les falta el marcador: rescatarlas debería ser el primer movimiento.

La columna **n (Word)** es el número del `.docx`; entre paréntesis va el del vault, para poder
localizar la entrada en `Bibliografía.md`. **«⛔ sin número»** = la obra no tiene sede en el `.docx`
y **no entra en la secuencia** (ver §4 del mapa y las «Decisiones pendientes» de cada capítulo).

| n (Word) | (vault) | Referencia | |
|---|---|---|---|
| 6 | (6) | Goodfellow, Bengio y Courville, *Deep Learning* | ← |
| 17 | (12) | Hastie, Tibshirani y Friedman, *ESL* | ← |
| 21 | (13) | Kohavi, validación cruzada y bootstrap | ← |
| 64 | (14) | scikit-learn, documentación oficial | ← |
| ⛔ sin número | (15) | Bergstra y Bengio, Random Search | tarea 2.19 |
| 70 | (16) | Chow, error/reject tradeoff | ← ⚠️ match aproximado |
| 37 | (19) | He y García, *Learning from Imbalanced Data* | ← |
| 41 | (21) | Sommer y Paxson, *Outside the Closed World* | ← |
| 63 | (22) | McHugh, crítica a las evaluaciones DARPA | ← ⚠️ match aproximado |
| 11 | (26) | Roesch, Snort (LISA'99) | ← |
| 40 | (29) | García-Teodoro *et al.*, anomaly-based NIDS | ← |
| 28 | (30) | Chandola, Banerjee y Kumar, *Anomaly detection: A survey* | ← |
| 12 | (31) | Khraisat *et al.*, survey de IDS | ← |
| ⛔ sin número | (32) | Barbará *et al.*, ADAM | tarea 3.7 |
| 42 | (33) | Tombini *et al.*, combinación serial anomalía + misuse | ← |
| ⛔ sin número | (34) | Ptacek y Newsham, *Insertion, Evasion and DoS* | |
| ⛔ sin número | (35) | Snort Users Manual, «Writing Snort Rules» | |
| 45 | (36) | Kendall, base de datos de ataques (tesis MIT) | ← |
| ⛔ sin número | (38) | Strom *et al.*, MITRE ATT&CK | |
| 15 | (39) | Russell y Norvig, *AIMA* | ← |
| ⛔ sin número | (41) | Grinsztajn *et al.*, árboles vs DL en tabular | tarea 3.7 |
| ⛔ sin número | (42) | McElfresh *et al.*, redes vs boosted trees | tarea 3.7 |
| ⛔ sin número | (43) | Sahami *et al.*, filtrado bayesiano de spam | |
| ⛔ sin número | (46) | Szegedy *et al.*, *Intriguing properties of neural networks* | tarea 2.14 |
| ⛔ sin número | (47) | Goodfellow, Shlens y Szegedy, FGSM | tarea 2.14 |
| 50 | (48) | Biggio y Roli, *Wild patterns* | ← |
| 75 | (50) | Moustafa y Slay, UNSW-NB15 | ← ⚠️ match aproximado |
| 74 | (51) | Sharafaldin *et al.*, CIC-IDS2017 | ← |
| 51 | (52) | Pierazzi *et al.*, adversarial ML en el espacio del problema | ← |
| ⛔ sin número | (53) | Rudin, modelos interpretables en decisiones críticas | tarea 2.7 |
| 66 | (54) | Molnar, *Interpretable Machine Learning* | ← |
| ⛔ sin número | (55) | RGPD — Reglamento (UE) 2016/679 | tarea 2.7 |
| ⛔ sin número | (56) | Reglamento de IA — (UE) 2024/1689 | tarea 2.7 |
| ⛔ sin número | (57) | Directiva NIS2 — (UE) 2022/2555 | tarea 2.7 |
| 62 | (58) | *KDD Cup 1999 Data*, UCI KDD Archive | ← |
| 46 | (59) | Lee y Stolfo, features y modelos para IDS | ← |
| ⛔ sin número | (60) | Mitchell *et al.*, Model Cards | tareas 5.26 y A14 |
| ⛔ sin número | (62) | Erickson *et al.*, TabArena | tarea 2.20 |
| ⛔ sin número | (63) | Micci-Barreca, target encoding | tarea 2.20 |
| ⛔ sin número | (64) | Pargent *et al.*, regularized target encoding | tarea 2.20 |
| ⛔ sin número | (65) | Hwang *et al.*, hybrid IDS con firmas ponderadas | ← tarea 2.21 |
| ⛔ sin número | (66) | Pendlebury *et al.*, TESSERACT | tarea 2.22 |
| ⛔ sin número | (67) | Behrouz *et al.*, Nested Learning | tarea 2.23 |
| ⛔ sin número | (68) | Ji *et al.*, IDS multinivel | ← tarea 2.11 |
| ⛔ sin número | (69) | Kim, Lee y Kim, híbrido anomalía + misuse | ← tarea 2.11 |
| ⛔ sin número | (70) | Khraisat *et al.*, stacking C5 + OC-SVM | ← tarea 2.11 |
| ⛔ sin número | (71) | Shwartz-Ziv y Armon, *DL is not all you need* | tarea 3.7 |
| ⛔ sin número | (72) | Hollmann *et al.*, TabPFN | tarea 3.7 |
| 29 | (73) | Liu, Ting y Zhou, *Isolation Forest* | ← |
| 31 | (75) | Breunig *et al.*, LOF | ← |
| ⛔ sin número | (78) | Storkey, *When Training and Test Sets Are Different* | ← tarea 5.25 |

**Los híbridos de IDS —Hwang (vault `[65]`), Ji (68), Kim (69), Khraisat 2020 (70) y Tombini (33) = `[42]`—** son exactamente el material que necesita el estado del arte de la tarea **2.10** y los tres trabajos de la **2.11**. Cuatro de los cinco **no tienen número hoy** precisamente porque esa sección no existe: **escribirla los rescata a todos de golpe**.

---

# Anexo C · Dónde va exactamente cada cita

> [!important] Estado real del Word ahora mismo (2026-08-24, mapa [[Bibliografia del docx - numeracion y anclas]])
> Este anexo es la **hoja de trabajo autosuficiente**: se recorre de arriba abajo con el `.docx`
> abierto y **sin consultar nada más**. Lo que hay que hacer en Word son cuatro cosas:
>
> | Trabajo | Cantidad | Dónde está en este anexo |
> |---|---|---|
> | **Reescribir** marcadores que ya están puestos con la numeración VIEJA del vault | **39** (en 47 párrafos; 1999, 2032 y 2262 llevan dos) | §C.0 |
> | **Insertar** marcadores que faltan | **~165 apariciones** | §C.1–§C.10 |
> | **Sustituir** placeholders visibles en el cuerpo | **3** (2 × `[ enlace bibliografía: …]` + 1 × `[CITA: …]`) | §C.8, primeras filas |
> | **Pegar** el apartado Bibliografía completo, sustituyendo el actual | lista `[1]`–`[75]` | §9 del mapa |

> [!warning] Obras ≠ apariciones — por qué las cifras no son la misma
> - **64 obras** es lo que numera el mapa (`[12]`–`[75]`), más los 11 congelados: **75 números**.
> - **~165 apariciones** es cuántas veces hay que **pegar** un marcador; una obra citada nueve
>   veces cuenta una vez como obra y nueve como apariciones.
> - **Las «69 altas» que este anexo declaraba antes eran ANCLAS**, no obras ni apariciones: una
>   fila de esta hoja puede llevar dos marcadores y una obra puede tener varias filas. La cifra se
>   retira y se sustituye por el recuento real de filas: **74 filas de ancla** (§C.1–§C.10), de las
>   que **1 está bloqueada** (`[68]` Pineau). Las citas medias van en el Anexo D.

> **Cómo se usa.** Cada fila trae el **párrafo del Word** para ir directo, y el **fragmento
> literal** para confirmar con Ctrl+F. El marcador va **al final de esa frase, antes del punto**, y
> **siempre a pelo**: `[n]`, nunca `[n, p. …]` (decisión del 2026-08-24). Dentro de cada capítulo
> las filas van **ordenadas por número de párrafo ascendente**.
>
> **Leyenda de la columna Párr.**
> - `123` — párrafo tomado del mapa, ancla literal.
> - `123 ⚠️inf.` — el párrafo está en el mapa, pero **cuál de las apariciones de esa obra es esta
>   fila** se ha deducido por orden. Confirma con Ctrl+F antes de pegar.
> - `—` — el mapa **no da** párrafo para esta ancla. No se ha inventado: localízala por Ctrl+F.
>
> La correspondencia con la numeración del vault (para volver a `Bibliografía.md`) está **al final
> del anexo, en §C.11**, fuera de la hoja de trabajo.

## C.0 · Las 39 reescrituras — marcadores que HOY están mal

Estos marcadores ya están en el documento, pero con la numeración vieja del vault: **cada número
significa hoy otra obra**. Se recorren por párrafo y se **traducen**; no se insertan de nuevo.

| ☐ | Párr. | Marcador | Qué obra es |
|---|---|---|---|
| ☐ | 737 | reescribir `[18]` → `[49]` | Arp *et al.* (2022), *Dos and Don'ts of ML in Computer Security* |
| ☐ | 868 | reescribir `[23]` → `[44]` | Tavallaee *et al.* (2009), análisis de KDD CUP 99 |
| ☐ | 873 | reescribir `[23]` → `[44]` | Tavallaee *et al.* (2009) |
| ☐ | 1432 | reescribir `[23]` → `[44]` | Tavallaee *et al.* (2009) |
| ☐ | 1434 | reescribir `[20]` → `[68]` | Pineau *et al.* (2021), reproducibilidad en ML |
| ☐ | 1436 | reescribir `[18]` → `[49]` | Arp *et al.* (2022) |
| ☐ | 1438 | reescribir `[25]` → `[14]` | Scarfone y Mell (2007), NIST SP 800-94 |
| ☐ | 1441 | reescribir `[17]` → `[52]` | Kapoor y Narayanan (2023), *Leakage and the reproducibility crisis* |
| ☐ | 1443 | reescribir `[23]` → `[44]` | Tavallaee *et al.* (2009) |
| ☐ | 1835 | reescribir `[61]` → `[48]` | Scheirer *et al.* (2013), *Toward Open Set Recognition* |
| ☐ | 1837 | reescribir `[49]` → `[71]` | Bendale y Boult (2016), OpenMax |
| ☐ | 1929 | reescribir `[18]` → `[49]` | Arp *et al.* (2022) |
| ☐ | 1931 | reescribir `[23]` → `[44]` | Tavallaee *et al.* (2009) |
| ☐ | 1934 | reescribir `[23]` → `[44]` | Tavallaee *et al.* (2009) |
| ☐ | 1970 | reescribir `[74]` → `[72]` | Goldschmidt y Chudá (2025), survey de datasets NIDS — **mismo párrafo que el placeholder `[CITA: …]` de §C.8** |
| ☐ | 1972 | reescribir `[74]` → `[72]` | Goldschmidt y Chudá (2025) |
| ☐ | 1978 | reescribir `[77]` → `[13]` | Hindy *et al.* (2020), zero-day con DL |
| ☐ | 1999 | reescribir `[24]` → `[73]` | Axelsson (2000), *base-rate fallacy* — **párrafo con DOS marcadores** |
| ☐ | 1999 | reescribir `[25]` → `[14]` | Scarfone y Mell (2007), NIST SP 800-94 — el segundo del párrafo |
| ☐ | 2024 | reescribir `[24]` → `[73]` | Axelsson (2000), *base-rate fallacy* |
| ☐ | 2032 | reescribir `[24]` → `[73]` | Axelsson (2000), *base-rate fallacy* — **párrafo con DOS marcadores** |
| ☐ | 2032 | reescribir `[25]` → `[14]` | Scarfone y Mell (2007), NIST SP 800-94 — el segundo del párrafo |
| ☐ | 2093 | reescribir `[18]` → `[49]` | Arp *et al.* (2022) |
| ☐ | 2100 | reescribir `[18]` → `[49]` | Arp *et al.* (2022) |
| ☐ | 2101 | reescribir `[52]` → `[51]` | Pierazzi *et al.* (2020), adversarial en el espacio del problema |
| ☐ | 2106 | reescribir `[20]` → `[68]` | Pineau *et al.* (2021) |
| ☐ | 2111 | reescribir `[61]` → `[48]` | Scheirer *et al.* (2013) |
| ☐ | 2116 | reescribir `[31]` → `[12]` | Khraisat *et al.* (2019), survey de IDS |
| ☐ | 2120 | reescribir `[18]` → `[49]` | Arp *et al.* (2022) |
| ☐ | 2224 | ⛔ `[62]` **sin equivalencia** | La obra que el vault numera `[62]` **no recibe número en el `.docx`** (no está en §2 del mapa). **Decisión en Word: retirar el marcador o volcar su sede.** No se traduce a ciegas |
| ☐ | 2228 | reescribir `[49]` → `[71]` | Bendale y Boult (2016), OpenMax |
| ☐ | 2262 | ⛔ `[63]` **sin equivalencia** | Ídem: vault `[63]` sin número en el `.docx`. **Párrafo con DOS marcadores** |
| ☐ | 2262 | ⛔ `[64]` **sin equivalencia** | Ídem: vault `[64]` sin número en el `.docx`. El segundo del párrafo |
| ☐ | 2269 | ⛔ `[65]` **sin equivalencia** | Es **Hwang** (híbrido de IDS), una de las obras que el Anexo B marca ⛔ sin número por falta de sede. Ver tarea **2.11** |
| ☐ | 2298 | reescribir `[51]` → `[74]` | Sharafaldin *et al.* (2018), CIC-IDS2017 |
| ☐ | 2300 | reescribir `[50]` → `[75]` | Moustafa y Slay (2015), UNSW-NB15 |
| ☐ | 2303 | ⛔ `[66]` **sin equivalencia** | Vault `[66]` sin número en el `.docx`. Misma decisión que 2224 |
| ☐ | 2317 | ⛔ `[67]` **sin equivalencia** | Vault `[67]` sin número en el `.docx` |
| ☐ | 2318 | ⛔ `[67]` **sin equivalencia** | Ídem |

> [!warning] Las seis sin equivalencia no se traducen por analogía
> `[62]`, `[63]`, `[64]`, `[65]`, `[66]` y `[67]` del vault **no aparecen en la tabla de numeración
> del `.docx`**: sus obras no tienen sede numerada en el documento entregable (§4 del mapa). Poner
> ahí cualquier número del rango `[12]`–`[75]` sería atribuir la cita a **otra obra**. Son **9 de
> los 39 marcadores** y hay que decidirlos uno a uno en Word.

## C.1 · Capítulo 1 (1 fila)

| ☐ | Párr. | Buscar este texto | Marcador | Qué obra es |
|---|---|---|---|---|
| ☐ | 248 | «…el de detección basada en el estado. Este último monitorea las sesiones de red» | `[14]` | Scarfone y Mell (2007), NIST SP 800-94, *Guide to IDPS* |

## C.2 · Capítulo 2 · §2.1.1–2.1.3 (1 fila)

| ☐ | Párr. | Buscar este texto | Marcador | Qué obra es |
|---|---|---|---|---|
| ☐ | 304 | «algoritmos y procesos que «aprenden» en el sentido de que son capaces de generalizar datos» | `[16]` | Mitchell (1997), *Machine Learning* |

## C.3 · Capítulo 2 · §2.1.4 «Algoritmos de ML» (13 filas)

Todas al final del párrafo que describe cada algoritmo.

| ☐ | Párr. | Buscar este texto | Marcador | Qué obra es |
|---|---|---|---|---|
| ☐ | 375 | «Un árbol de decisión es una estructura jerárquica de nodos de decisión» | `[22]` | Breiman, Friedman, Olshen y Stone (1984), *Classification and Regression Trees* |
| ☐ | 377 | «Un conjunto (ensemble) combina varios clasificadores individuales» | `[23]` | Dietterich (2000), *Ensemble Methods in Machine Learning* |
| ☐ | 379 | «El muestreo aleatorio decorrelaciona los árboles individuales y reduce la varianza» | `[24]` | Breiman (2001), *Random Forests* |
| ☐ | 382 | «cada árbol nuevo se entrena para corregir los errores residuales del conjunto acumulado» | `[25]` | Friedman (2001), gradient boosting |
| ☐ | 383 | «discretizando las características continuas en un número fijo de contenedores» | `[26]` | Ke *et al.* (2017), LightGBM |
| ☐ | 385 | «el ejemplo más conocido de aprendizaje perezoso» | `[27]` | Cover y Hart (1967), vecino más cercano |
| ☐ | 389 | «Estos algoritmos se denominan semisupervisados (one-class)» | `[28]` | Chandola, Banerjee y Kumar (2009), *Anomaly detection: A survey* |
| ☐ | 392 | «La longitud media del camino de aislamiento a través del conjunto de árboles» | `[29]` | Liu, Ting y Zhou (2008), *Isolation Forest* |
| ☐ | 395 | «busca la frontera —en el espacio transformado por un núcleo (kernel), típicamente el radial (RBF)—» | `[30]` | Schölkopf *et al.* (2001), One-Class SVM |
| ☐ | 398 | «recibe una puntuación LOF elevada y se considera anómalo» | `[31]` | Breunig *et al.* (2000), LOF |
| ☐ | 402 | «calculando los gradientes de todos los pesos mediante retropropagación» | `[32]` | Rumelhart, Hinton y Williams (1986), retropropagación |
| ☐ | — | «un MLP empleado como autoencoder, que es el detector seleccionado para la etapa 1» | `[6]` | Goodfellow, Bengio y Courville (2016), *Deep Learning* — **`[6]` no aparece hoy ni una vez en el cuerpo** (tarea B4) |
| ☐ | — | «k-means y el agrupamiento jerárquico como exponentes principales» | `[17]` | Hastie, Tibshirani y Friedman (2009), *The Elements of Statistical Learning* |

## C.4 · Capítulo 2 · §2.1.5 «Métricas» (10 filas)

Las de las ecuaciones van **en la frase que introduce la fórmula**, no en la fórmula.

| ☐ | Párr. | Buscar este texto | Marcador | Qué obra es |
|---|---|---|---|---|
| ☐ | 412 | «La matriz de confusión es el punto de partida de toda métrica de clasificación» | `[33]` | Fawcett (2006), *An introduction to ROC analysis* |
| ☐ | 423 | «Precisión: De todas las veces que el sistema levantó una alarma de ataque» | `[34]` ⚠️ nivel 2 | Powers (2011), *Evaluation: From Precision, Recall and F-Measure…* |
| ☐ | 427 | «Exhaustividad (recall): de todos los ataques reales, qué proporción detectó el sistema» | `[34]` ⚠️ nivel 2 | Powers (2011) |
| ☐ | 436 | «se calculan primero por clase, con el esquema uno-contra-el-resto» | `[35]` | Sokolova y Lapalme (2009), medidas de rendimiento |
| ☐ | 440 | «F1: la media armónica de precisión y recall» | `[36]` | van Rijsbergen (1979), *Information Retrieval* |
| ☐ | 446 ⚠️inf. | «Macro: se calcula la métrica de cada clase por separado y se promedian sin ponderar» | `[35]` | Sokolova y Lapalme (2009) |
| ☐ | 464 ⚠️inf. | «Su resumen numérico habitual es el área bajo la curva (AUC-ROC)» | `[33]` | Fawcett (2006) |
| ☐ | 469 | «Enfrenta la precisión frente al recall en cada umbral, con su propia área bajo la curva» | `[38]` | Davis y Goadrich (2006), PR vs ROC |
| ☐ | 470 ⚠️inf. | «la curva ROC puede resultar engañosamente optimista» | `[38]` | Davis y Goadrich (2006) |
| ☐ | — | «Tasa de falsos positivos (FPR): de todo el tráfico normal» | `[33]` | Fawcett (2006) — el mapa no asigna párrafo a esta ancla |

## C.5 · Capítulo 2 · §2.2 (19 filas)

> [!note] Las seis anclas de NIST SP 800-94 de este bloque
> El mapa registra apariciones de `[14]` en los párrafos **501, 503, 524, 535 y 570** dentro de
> §2.2, pero **no dice qué ancla corresponde a cuál**. No se reparten a ciegas: las filas van con
> `—` y se localizan por Ctrl+F, que en este rango es una pasada corta.

| ☐ | Párr. | Buscar este texto | Marcador | Qué obra es |
|---|---|---|---|---|
| ☐ | 521 | «La literatura no usa una taxonomía única sino varios ejes ortogonales» | `[39]` ⚠️ nivel 2 | Axelsson (2000), *IDS: A Survey and Taxonomy* (informe Chalmers) — **no confundir con `[73]`**, el otro Axelsson |
| ☐ | 528 | «Es la taxonomía más citada del área y la que enmarca el problema de este TFG» | `[40]` | García-Teodoro *et al.* (2009), anomaly-based NIDS |
| ☐ | 554 | «mayor tasa de falsos positivos, alertas menos explicables y sensibilidad a la deriva (drift)» | `[41]` | Sommer y Paxson (2010), *Outside the Closed World* |
| ☐ | 568 | «existen trabajos que la adoptan, la invierten y la reformulan como conjunto paralelo» | `[42]` + ⛔ | Tombini *et al.* (2004), combinación serial. Los otros cuatro híbridos (Ji, Kim, Khraisat 2020, Hwang) **no tienen número hoy**: son la tarea **2.11** |
| ☐ | 571 | «procede de las campañas de evaluación… del MIT Lincoln Laboratory para DARPA (1998)» | `[43]` + `[44]` | Lippmann *et al.* (2000), DARPA 1998 · Tavallaee *et al.* (2009) |
| ☐ | 577 | «Ejemplos en el dataset: neptune (inundación de segmentos SYN)…» | `[45]` | Kendall (1999), *A Database of Computer Attacks* |
| ☐ | 581 ⚠️inf. | «Ejemplos en el dataset: nmap, portsweep, ipsweep, satan» | `[45]` | Kendall (1999) |
| ☐ | 586 ⚠️inf. | «Ejemplos en el dataset: guess_passwd (fuerza bruta…)» | `[45]` | Kendall (1999) |
| ☐ | 591 ⚠️inf. | «Ejemplos en el dataset: buffer_overflow, rootkit, loadmodule, perl» | `[45]` | Kendall (1999) |
| ☐ | — | «Una intrusión es cualquier acción, intencionada o no, que compromete la confidencialidad» | `[14]` | Scarfone y Mell (2007), NIST SP 800-94 |
| ☐ | — | «monitoriza de forma continua los eventos que ocurren en un sistema o en una red» | `[14]` | Scarfone y Mell (2007) |
| ☐ | — | «Sensor o captura. Obtiene el tráfico del segmento vigilado» | `[14]` | Scarfone y Mell (2007) |
| ☐ | — | «Se diferencia en este punto entre HIDS (host-based IDS) y NIDS» | `[14]` | Scarfone y Mell (2007) |
| ☐ | — | «es la modalidad que convierte al detector en un IPS» | `[14]` | Scarfone y Mell (2007) |
| ☐ | — | «hereda de Denning (quien aportó el modelo IDES…)» | `[3]` — **mapear, no dar de alta** | Denning (1987), *An Intrusion-Detection Model* |
| ☐ | — | «La formulación original del enfoque se debe a Denning» | `[3]` — mapear | Denning (1987) |
| ☐ | — | «entronca con la tradición de Snort» | `[11]` | Roesch (1999), «Snort», LISA'99 — **el `[11]` del `.docx` ES Snort; el `[11]` del vault es CRISP-DM y no llega al Word** |
| ☐ | — | «El conocimiento del analista de seguridad queda así codificado en una base de firmas» | `[11]` | Roesch (1999) |
| ☐ | — | «alta precisión sobre lo que cubre, alertas explicables y bajo volumen de falsas alarmas» | `[40]` | García-Teodoro *et al.* (2009) |

## C.6 · Capítulo 2 · §2.3 (5 filas)

| ☐ | Párr. | Buscar este texto | Marcador | Qué obra es |
|---|---|---|---|---|
| ☐ | 606 | «se habla de DL cuando la jerarquía de capas es lo bastante honda» | `[47]` | LeCun, Bengio y Hinton (2015), *Deep learning* (Nature) |
| ☐ | 624 | «no produce «ninguna de las anteriores»: produce la categoría conocida más parecida» | `[48]` | Scheirer *et al.* (2013), *Toward Open Set Recognition* |
| ☐ | 631 | ««each paper suffers from at least three pitfalls»» | `[49]` — **cita textual hoy SIN marcador** | Arp *et al.* (2022), *Dos and Don'ts of ML in Computer Security* |
| ☐ | 634 ⚠️inf. | «El pitfall P9 de Arp et al., Lab-Only Evaluation» | `[49]` | Arp *et al.* (2022) |
| ☐ | 643 ⚠️inf. | «el pitfall P10, Inappropriate Threat Model» | `[49]` | Arp *et al.* (2022) |

## C.7 · Capítulo 3 (7 filas)

En las **tablas de candidatos**, el marcador va en la celda «NOCIÓN DE ANOMALÍA» / «IDEA».

| ☐ | Párr. | Buscar este texto | Marcador | Qué obra es |
|---|---|---|---|---|
| ☐ | 749 ⚠️inf. | «Aísla las anomalías por particiones aleatorias» | `[29]` | Liu, Ting y Zhou (2008), *Isolation Forest* |
| ☐ | 752 ⚠️inf. | «Aprende una frontera que encierra el comportamiento normal» | `[30]` | Schölkopf *et al.* (2001), One-Class SVM |
| ☐ | 755 ⚠️inf. | «Compara la densidad local de cada punto con la de sus vecinos» | `[31]` | Breunig *et al.* (2000), LOF |
| ☐ | 782 ⚠️inf. | «Conjunto (ensemble) de árboles por bagging» | `[24]` | Breiman (2001), *Random Forests* |
| ☐ | 788 | «Conjunto por boosting (rendimiento tipo XGBoost)» | `[53]` | Chen y Guestrin (2016), XGBoost |
| ☐ | 794 | «Comparar el sobremuestreo sintético (SMOTE) frente al reponderado de clases» | `[55]` | Chawla *et al.* (2002), SMOTE |
| ☐ | — | «Error de reconstrucción: reconstruye mal lo que no se parece a lo normal» | `[6]` | Goodfellow, Bengio y Courville (2016), *Deep Learning* |

## C.8 · Capítulo 4 (12 filas) — incluye los 3 placeholders visibles

Las tres primeras filas **sustituyen texto visible en el documento**, no añaden un marcador al final
de una frase.

| ☐ | Párr. | Buscar este texto | Marcador | Qué obra es |
|---|---|---|---|---|
| ☐ | 840 | «Tratamiento del desbalance de clases: SMOTE dentro de un Pipeline» (tabla de librerías) | `[60]` | Lemaître, Nogueira y Aridas (2017), imbalanced-learn |
| ☐ | 843 | «test de Kolmogórov-Smirnov para el análisis de drift» (tabla de librerías) | `[61]` | Massey (1951), test de Kolmogórov-Smirnov |
| ☐ | 862 | **PLACEHOLDER** — sustituir entero: `[enlace bibliografía: KDD Cup 99]` | `[64]` + `[43]` | *KDD Cup 1999 Data*, UCI KDD Archive · Lippmann *et al.* (2000), DARPA 1998 |
| ☐ | 864 | **PLACEHOLDER** — sustituir: `[ enlace bibliografía: McHugh 2000]` | `[65]` ⚠️ **sede INFERIDA por contenido, no literal** | McHugh (2000), crítica a las evaluaciones DARPA. **Confirma el sitio antes de pegar**: el fragmento no aparece verbatim en el `.docx` (§5.3 del mapa) |
| ☐ | 875 ⚠️inf. | «Las 41 características se agrupan en tres familias» | `[46]` | Lee y Stolfo (2000), features y modelos para IDS |
| ☐ | 1038 | «las muestras sintéticas se interpolan a partir de vecinos reales» | `[55]` + `[52]` | Chawla *et al.* (2002), SMOTE · Kapoor y Narayanan (2023), *Leakage…* |
| ☐ | 1105 ⚠️inf. | «se entrena un RandomForestClassifier (100 árboles, class_weight='balanced', semilla 42)» | `[24]` | Breiman (2001), *Random Forests* |
| ☐ | 1261 | «las conexiones anómalas se reconstruyen mal y producen un MSE alto» | `[67]` | Sakurada y Yairi (2014), autoencoders para detección de anomalías |
| ☐ | 1970 | **PLACEHOLDER** — sustituir: `[CITA: Tavallaee 2009 + survey de datasets NIDS]` | `[44]` + `[72]` | Tavallaee *et al.* (2009) · Goldschmidt y Chudá (2025), survey de datasets NIDS. **Este párrafo también lleva una reescritura** (`[74]` → `[72]`, §C.0) |
| ☐ | — | **PLACEHOLDER ¿residual?** — `[ enlace bibliografía: Tavallaee 2009]`, ×2 | `[44]` | Tavallaee *et al.* (2009). ⚠️ **Comprobar con Ctrl+F si siguen existiendo:** §5.4 del mapa cuenta **solo 2** placeholders `[ enlace bibliografía: …]` en el cuerpo, y son el de KDD Cup 99 y el de McHugh. Si estos dos no aparecen, la fila se tacha sin más |
| ☐ | — | «una de las cinco categorías canónicas de la literatura de NSL-KDD» | `[45]` + `[44]` | Kendall (1999) · Tavallaee *et al.* (2009) |
| ☐ | — | «Su coste de entrenamiento es O(n²) en memoria y tiempo» | `[30]` | Schölkopf *et al.* (2001), One-Class SVM |

## C.9 · Capítulo 5 (5 filas, 1 de ellas bloqueada)

| ☐ | Párr. | Buscar este texto | Marcador | Qué obra es |
|---|---|---|---|---|
| ☐ | 1434 · 2106 | ⛔ **BLOQUEADA — sin ancla literal.** No hay fragmento establecido para esta obra en §5.0 (protocolo). **No se inventa uno.** Lo único accionable hoy son sus dos reescrituras de §C.0 (`[20]` → `[68]`) | `[68]` | Pineau *et al.* (2021), *Improving Reproducibility in ML Research* (NeurIPS Reproducibility Program). **Pendiente: localizar la frase que sostiene la cita** |
| ☐ | 1704 | «Comparación pareada (semilla a semilla)» | `[69]` + `[70]` — **complementarias, no alternativas** | Demšar (2006), comparación estadística de clasificadores · Dietterich (1998), tests estadísticos aproximados |
| ☐ | — | «su coste de entrenamiento O(n²) hace inviable ajustarlo con el conjunto completo» | `[30]` | Schölkopf *et al.* (2001), One-Class SVM |
| ☐ | — | «el patrón dominante en la literatura sobre NSL-KDD: un RandomForest monolítico» | `[12]` + `[44]` | Khraisat *et al.* (2019), survey de IDS · Tavallaee *et al.* (2009). ⚠️ «RandomForest monolítico» **no está verificado en fuente**: atenuar a «clasificador supervisado monolítico» si aprietan |
| ☐ | — | «El célebre "~99 % de accuracy" de la literatura no sobrevive al test oficial» | `[44]` | Tavallaee *et al.* (2009), análisis de KDD CUP 99 |

## C.10 · Capítulo 6 (1 fila)

| ☐ | Párr. | Buscar este texto | Marcador | Qué obra es |
|---|---|---|---|---|
| ☐ | — | «frente al enfoque supervisado que domina la literatura sobre el NSL-KDD» | `[12]` | Khraisat *et al.* (2019), survey de IDS — mismo sostén que en el cap. 5 |

> [!note] La otra sede inferida del mapa, `[75]`
> `[75]` Moustafa y Slay (2015), UNSW-NB15, tiene **sede inferida por contenido, no literal**
> (párr. 2300, §5.3 del mapa). No tiene fila de alta en esta hoja porque en ese párrafo el
> marcador **ya está puesto**: entra como **reescritura** `[50]` → `[75]` en §C.0. Igual que con
> `[65]` McHugh, **confirma el sitio antes de dejarlo fijo**.

## C.11 · Trazabilidad al vault (no se usa al pegar)

Solo para volver a `Bibliografía.md` —por ejemplo, a buscar un DOI—. **Nunca se escribe en el
Word.** Los localizadores de página del vault **no se trasladan al `.docx`** (decisión del
2026-08-24).

| `.docx` → vault | | | |
|---|---|---|---|
| `[11]`→`[26]` · `[12]`→`[31]` · `[13]`→`[77]` · `[14]`→`[25]` | `[16]`→`[79]` · `[17]`→`[12]` · `[22]`→`[83]` · `[23]`→`[84]` | `[24]`→`[85]` · `[25]`→`[86]` · `[26]`→`[87]` · `[27]`→`[88]` | `[28]`→`[30]` · `[29]`→`[73]` · `[30]`→`[89]` · `[31]`→`[75]` |
| `[32]`→`[90]` · `[33]`→`[91]` · `[34]`→`[93]` · `[35]`→`[92]` | `[36]`→`[94]` · `[38]`→`[95]` · `[39]`→`[96]` · `[40]`→`[29]` | `[41]`→`[21]` · `[42]`→`[33]` · `[43]`→`[97]` · `[44]`→`[23]` | `[45]`→`[36]` · `[46]`→`[59]` · `[47]`→`[98]` · `[48]`→`[61]` |
| `[49]`→`[18]` · `[51]`→`[52]` · `[52]`→`[17]` · `[53]`→`[99]` | `[55]`→`[100]` · `[60]`→`[102]` · `[61]`→`[103]` · `[64]`→`[58]` | `[65]`→`[22]` · `[67]`→`[108]` · `[68]`→`[20]` · `[69]`→`[109]` | `[70]`→`[110]` · `[71]`→`[49]` · `[72]`→`[74]` · `[74]`→`[51]` · `[75]`→`[50]` |

> Las equivalencias que no aparecen aquí (`[1]`–`[10]`, `[15]`, `[18]`–`[21]`, `[37]`, `[50]`,
> `[54]`, `[56]`–`[59]`, `[62]`, `[63]`, `[66]`, `[73]`) o son del tramo congelado o solo se usan
> en el Anexo D; están todas en §2 del mapa.

---

# Anexo D · Anclas de las 48 citas medias

> [!note] Numeración del `.docx`
> Desde el **2026-08-24 (tercera pasada)** este anexo está **íntegramente en la numeración del `.docx` por orden de aparición en el Word** (mapa en [[Bibliografia del docx - numeracion y anclas]] §2). El `(vault [xx])` entre paréntesis es solo la referencia para localizar la entrada en `Bibliografía.md`.

Mismo criterio que el Anexo C: busca el fragmento con Ctrl+F, el marcador va al final de la frase.
Estas son **defendibles sin cita**, pero suman rigor. Si vas justo de tiempo, haz primero el Anexo C.

## Capítulo 1 (3)

| Buscar este texto | Marcador |
|---|---|
| «Se han creado algoritmos basados tanto en Machine Learning (ML) como en IA» | `[12]` (vault `[31]`) Khraisat *et al.* 2019 |
| «estos algoritmos han sido fundamentales para la detección de ataques desconocidos» | `[13]` (vault `[77]`) Hindy *et al.* 2020 — ⚠️ se cita por el método, **no** por su 89-99 % |
| «Evasión del IDS/NIDS – el atacante conoce el mecanismo de detección y lo esquiva» | `[14]` (vault `[25]`) NIST SP 800-94 |

## Capítulo 2 · §2.1.1–2.1.3 (8)

| Buscar este texto | Marcador |
|---|---|
| «los investigadores han perseguido enseñar a las computadoras a razonar» | `[15]` (vault `[39]`) Russell y Norvig |
| «el algoritmo es el conjunto de instrucciones que dicen como aprender de los datos» | `[5]` Géron |
| «se limpian, transforman y dividen en subconjuntos de entrenamiento, validación y prueba» | `[17]` (vault `[12]`) Hastie |
| «Reducción de dimensionalidad y visualización» | `[18]` (vault `[80]`) — página sin establecer (solo para `Bibliografía.md`; el marcador va a pelo) |
| «Reglas de asociación, que busca encontrar coocurrencias frecuentes» | `[19]` (vault `[81]`) |
| «Un agente aprende por interacción con un entorno, guiado por recompensas y penalizaciones» | `[20]` (vault `[82]`) — página sin establecer (solo para `Bibliografía.md`; el marcador va a pelo) |
| «un candidato algo peor pero mucho más estable puede ser preferible» | `[17]` (vault `[12]`) |
| «los valores que el algoritmo no aprende de los datos— mediante validación cruzada» | `[5]` + `[21]` (vault `[13]`) Kohavi |

## Capítulo 2 · §2.1.5 «Métricas» (5)

| Buscar este texto | Marcador |
|---|---|
| «VP (verdadero positivo): un ataque correctamente señalado como ataque» | `[33]` (vault `[91]`) |
| «la matriz pasa a ser de k x k, con k el número de clases» | `[35]` (vault `[92]`) |
| «Exactitud (accuracy): la proporción de predicciones correctas sobre el total» | `[35]` (vault `[92]`) |
| «un weighted alto, porque el peso n_i de la clase mayoritaria domina la suma» | `[37]` (vault `[19]`) He y García |
| «no produce directamente una etiqueta, sino una puntuación continua» | `[33]` (vault `[91]`) |

## Capítulo 2 · §2.2 y §2.3 (5)

| Buscar este texto | Marcador |
|---|---|
| «el momento del análisis: tiempo real… y diferido (offline)» | `[14]` (vault `[25]`) |
| «los 39 tipos de ataque específicos presentes en el corpus» | `[44]` (vault `[23]`) |
| «Huella en el tráfico» (las cuatro apariciones: `serror_rate`, `count`, `hot`, `root_shell`) | `[46]` (vault `[59]`) Lee y Stolfo |
| «designan conjuntos anidados: cada uno es un subconjunto estricto del anterior» | `[4]` — ya usada antes |
| «Un modelo de amenaza es la especificación explícita de las hipótesis sobre el adversario» | ⛔ **SIN NÚMERO — el ancla no existe en el `.docx`. Decisión pendiente: tarea 2.24 (Shostack 2014)** |
| «equivale a suponer un adversario que no modifica su comportamiento» | `[50]` (vault `[48]`) Biggio y Roli |

## Capítulo 3 (8)

| Buscar este texto | Marcador |
|---|---|
| «las cuatro categorías canónicas del dataset NSL-KDD» | `[44]` (vault `[23]`) |
| «siguiendo la línea de un IDS clásico basado en reglas» | `[11]` (vault `[26]`) Roesch |
| «instanciar el caso, es decir, fijar un valor concreto en cada dimensión» | `[49]` (vault `[18]`) Arp *et al.* |
| «produce puntos que ningún atacante real podría generar» | `[51]` (vault `[52]`) Pierazzi *et al.* |
| «al no re-particionar el test, D2 conserva los tipos de ataque que no aparecen» | `[44]` (vault `[23]`) |
| «se ajustan únicamente sobre el tráfico de entrenamiento (D1+D3)» | `[52]` (vault `[17]`) Kapoor y Narayanan |
| «del árbol de decisión se extraen reglas legibles (mediante export_text)» | `[66]` (vault `[54]`) Molnar |
| «estimadas fuera de muestra (out-of-fold, mediante validación cruzada sobre D3)» | `[70]` (vault `[16]`) Chow, reject option ⚠️ match aproximado |

## Capítulo 4 (11)

| Buscar este texto | Marcador |
|---|---|
| «Python es el lenguaje de referencia para el aprendizaje automático» | ⛔ **SIN NÚMERO — no hay fuente de nivel 1-2. Decisión pendiente: tarea 4.13 (atenuar o retirar)** |
| «Núcleo de ML: preprocesamiento (MinMaxScaler, LabelEncoder)» (fila de la tabla) | `[57]` (vault `[101]`) |
| Filas de NumPy · Pandas · Matplotlib · Seaborn de la misma tabla | `[55]` Harris 2020 · `[56]` McKinney 2010 · `[60]` Hunter 2007 · `[61]` Waskom 2021 |
| «etiquetaron cada registro de KDDTest+ con un valor de #successfulPrediction» | `[44]` (vault `[23]`) |
| «desde tasas en [0,1] hasta contadores de bytes con valores de cientos de millones» | `[5]` |
| «Se codifican mediante One-Hot Encoding (pd.get_dummies)» | `[5]` |
| «selección de modelo sobre el conjunto de test, es decir data snooping» | `[49]` (vault `[18]`) Arp *et al.* |
| «LocalOutlierFactor se instancia con novelty=True» | `[64]` (vault `[14]`) doc. scikit-learn |
| «un clasificador que nunca predijera u2r conservaría un accuracy superior al 99,9 %» | `[37]` (vault `[19]`) |
| «las firmas deben poder leerse, auditarse y, llegado el caso, trasladarse a reglas» | `[66]` (vault `[54]`) Molnar |
| «Es la firma canónica de un SYN flood tipo neptune» | `[45]` (vault `[36]`) Kendall |

## Capítulo 5 (4)

| Buscar este texto | Marcador |
|---|---|
| «Su noción de anomalía basada en densidad local no captura bien la separación» | `[31]` (vault `[75]`) Breunig *et al.* |
| «refleja el desplazamiento distribucional D3→D2 propio del NSL-KDD» | `[44]` (vault `[23]`) |
| «el sobreajuste es invisible en validación cruzada» | `[17]` (vault `[12]`) |
| «la captura del tráfico en la interfaz de red, el ensamblado de los paquetes en flujos» | `[41]` (vault `[21]`) Sommer y Paxson |

## Capítulo 6 (4)

| Buscar este texto | Marcador |
|---|---|
| «firmas y anomalías no compiten, sino que se complementan» | `[40]` (vault `[29]`) García-Teodoro *et al.* |
| «debido al desplazamiento distribucional entre el tráfico normal de entrenamiento y el de test» | `[44]` (vault `[23]`) |
| «ningún algoritmo ni técnica de balanceo (SMOTE, class_weight) logra un rendimiento sólido» | `[37]` (vault `[19]`) + `[54]` (vault `[100]`) |
| «el clasificador de firmas, cerrado, tiende a asignar con confianza etiquetas conocidas» | `[48]` (vault `[61]`) Scheirer / `[71]` (vault `[49]`) Bendale |

---

## Cuántas huérfanas se rescatan solas

Si haces los Anexos C y D completos, quedan citadas **sin decidir nada** estas entradas, hoy huérfanas.
Números del `.docx`, con el del vault entre paréntesis:

`[4]` (4) · `[11]` (26) · `[12]` (31) · `[15]` (39) · `[17]` (12) · `[21]` (13) · `[28]` (30) ·
`[29]` (73) · `[31]` (75) · `[37]` (19) · `[40]` (29) · `[41]` (21) · `[42]` (33) · `[45]` (36) ·
`[46]` (59) · `[50]` (48) · `[51]` (52) · `[62]` (58) · `[63]` (22) · `[64]` (14) · `[66]` (54) ·
`[70]` (16) · `[74]` (51) · `[75]` (50)

El resto **no se rescata escribiendo marcadores**, sino **decidiendo si se vuelca su sede**: son las
tareas 2.7, 2.11, 2.19–2.24, 3.7, 4.14, 5.25 y A14. Por eso **B1 va al final** del bloque de bibliografía.
