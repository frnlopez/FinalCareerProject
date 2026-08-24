# Las tareas de Kiko

Revisión de `Proyecto_Fin_de_Grado-FJLM-2026.docx` leído en limpio, capítulos 1–6 + apéndices + bibliografía.
Cada tarea marca su sede: `vault` = se arregla en la nota `.md` · `Word` = se arregla en el `.docx`.

> **Orden recomendado:** primero el bloque transversal (T), luego capítulo por capítulo.
> La renumeración de la bibliografía (T4) es **la última tarea de todas**: si se hace antes,
> cada cita nueva vuelve a romperla.

---

## T · Transversal (afecta a todo el documento)

### Bibliografía
- [ ] **T1** · Verificar el mapa `[1]`–`[11]` entre el vault y el `.docx` antes de congelarlo. Hay desajuste: `[11]` cita a Snort/Roesch en el `.docx` y es CRISP-DM en `Bibliografía.md`. `vault`
- [X] **T2** · Corregir la cita `[9]` de la línea 479 (cap. 2): es un número **quemado**, no existe entrada. Remapear a `[8]` o `[10]`. `vault`
- [ ] **T3** · Volcar al Word las entradas de `Bibliografía.md` que queden en uso. Hoy el `.docx` tiene 11 escritas a mano y sin relación con el vault. `Word`
- [ ] **T4** · **(ÚLTIMA)** Renumerar de `[12]` en adelante por orden de aparición, en el vault y en el `.docx` **a la vez**. `[1]`–`[11]` se congelan. `vault` + `Word`

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
- [ ] **1.5** · Citar la «detección basada en el estado» → NIST SP 800-94. `vault`
- [ ] **1.6** · Añadir las 3 citas medias del Anexo A. `vault`

---

## Capítulo 2 · Marco Teórico

**Citas:** 6 marcadores en 368 líneas. Faltan **67 (49 altas)** → ver Anexo A. Es el capítulo con el problema más grande del documento.

### Bibliografía
- [ ] **2.1** · **2.1.4 «Algoritmos de ML» — cero citas.** Añadir las **14 citas altas**: un algoritmo de terceros por cita (CART, Random Forest, Gradient Boosting, LightGBM, k-NN, Isolation Forest, One-Class SVM, LOF, MLP/backprop, autoencoders, k-means, ensembles, one-class). `vault`
- [ ] **2.2** · **2.1.5 «Métricas» — cero citas.** Añadir **10 altas + 5 medias**: matriz de confusión, precisión, recall, FPR, F1, macro/weighted y las **siete ecuaciones**, todas hoy sin fuente. `vault`
- [ ] **2.3** · Citar 2.2.2 «Sistemas de detección de intrusiones»: definición de intrusión, definición de IDS y la cadena de bloques del NIDS (4 altas). `vault`
- [ ] **2.4** · Citar 2.2.3 «Taxonomía de los IDS»: los cuatro ejes, HIDS/NIDS, inline/pasivo (5 altas). `vault`
- [ ] **2.5** · Citar 2.2.4 «Firmas frente a anomalías» y mapear Denning a `[3]` y Snort a su entrada correcta (5 altas). `vault`
- [ ] **2.6** · Citar 2.2.5 «Taxonomía de ataques»: DARPA/KDD y los ejemplos de cada categoría (5 altas). `vault`
- [ ] **2.7** · Citar 2.3 entera —incluida 2.3.3 «Límites y consideraciones éticas», hoy sin ninguna fuente pese a tener `[53]` Rudin, `[54]` Molnar y `[55]`–`[57]` RGPD/AI Act/NIS2 vivas y sin usar. `vault`
- [ ] **2.8** · Poner marcador a la **cita textual en inglés** («each paper suffers from at least three pitfalls»): está entrecomillada y sin `[18]`. `vault`
- [ ] **2.9** · Poner localizador de página a `[4]` Chio, `[5]` Géron (×2), `[7]` Murphy y `[8]` Stallings. Ninguno lo lleva. `vault`

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

---

## Capítulo 3 · Diseño del sistema

**Citas:** **1 marcador en todo el capítulo**. Faltan 11 (3 altas) → ver Anexo A.

### Bibliografía
- [ ] **3.1** · Citar los cuatro algoritmos de la tabla de candidatos de anomalías (§3.4.2): Isolation Forest, One-Class SVM, LOF y autoencoder. `vault`
- [ ] **3.2** · Citar la tabla de candidatos de firmas (§3.5.2): Random Forest y boosting/XGBoost. `vault`
- [ ] **3.3** · Citar **SMOTE** en §3.5.4. Se nombra como decisión de diseño sin fuente. `vault`
- [ ] **3.4** · Añadir las 8 citas medias del Anexo A (categorías canónicas, anti-leakage, espacio-problema adversario, regla de presupuesto). `vault`

### Estructura
- [ ] **3.5** · Mover la medición de la **cascada invertida** al capítulo 5. Hoy da cifras de resultados (6.558/9.711, 67,53 %) dentro de Diseño, antes de que el lector conozca el protocolo. `vault`
- [ ] **3.6** · Dejar la confesión de **data snooping** en un solo sitio. Hoy está en §3.3.3 y en §4.3.5 casi con las mismas palabras. `vault`

---

## Capítulo 4 · Implementación del sistema

**Citas:** 2 marcadores en 590 líneas. Faltan 22 (11 altas) → ver Anexo A. `4.3`, `4.4` y `4.5` **enteras** no citan nada.

### Bibliografía
- [ ] **4.1** · **Resolver los 3 placeholders visibles de §4.2**: `[enlace bibliografía: KDD Cup 99]`, `[… Tavallaee 2009]`, `[… McHugh 2000]` y `[CITA: Tavallaee 2009 + survey]`. Se ven a simple vista en el documento final. `vault`
- [ ] **4.2** · Citar las librerías de la tabla de §4.1.3: scikit-learn, imbalanced-learn, el test KS de scipy, matplotlib, seaborn, NumPy, pandas. `vault`
- [ ] **4.3** · Citar §4.3: las 41 características (Lee y Stolfo), el escalado, el one-hot, **SMOTE + leakage**, y las importancias de Random Forest. `vault`
- [ ] **4.4** · Citar §4.4: complejidad O(n²) de One-Class SVM, `novelty=True` de LOF y el autoencoder como detector de anomalías. `vault`
- [ ] **4.5** · Citar §4.5: el argumento de que «el accuracy miente» con u2r, la interpretabilidad de las reglas y la firma canónica del SYN flood. `vault`

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
- [ ] **5.6** · Respaldar las dos afirmaciones sobre el estado del arte que sostienen la tesis: «el patrón dominante en la literatura» y «el célebre ~99 % de accuracy». Hoy no apuntan a ninguna fuente. `vault`
- [ ] **5.7** · Citar el criterio estadístico pareado vs no pareado de §5.2.4. `vault`
- [ ] **5.8** · Citar en §5.1 el LOF y la complejidad O(n²) del One-Class SVM, hoy explicados sin fuente. `vault`

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

### Recortes
- [ ] **5.21** · Dejar los tres hallazgos (complementariedad / 13,4 % / `snmpgetattack`) en un solo sitio. Hoy están en §5.3 y §5.4 casi literales. `vault`
- [ ] **5.22** · Dejar los cuatro puntos del baseline en un solo sitio, por el mismo motivo. `vault`

### Redacción
- [ ] **5.23** · Reescribir las tres frases rotas: «de modo qua ser deriva de código», «mientras que la dispes dos configuraciones comparadas», `7 vecesmayor`. `vault`
¿?¿?¿? dispes? que debería de ir ahi
---

## Capítulo 6 · Conclusiones

**Citas:** **cero marcadores en todo el capítulo.** Faltan 5 → ver Anexo A.

### Contenido — lo primero
- [X] **6.1** · **Redactar §6.2 «Líneas futuras». Hoy está VACÍA** (solo el título) y la referencian el índice, el capítulo 1 y el propio §6.1.3. Material de respaldo en `EL_FUTURO.md`. `vault`
- [X] **6.2** · **Añadir el data snooping a «Limitaciones».** El capítulo 5 declara tres decisiones tomadas mirando el test y el 6 no lo menciona. `vault`
- [ ] **6.3** · **Matizar la frase «bajo una disciplina anti-leakage estricta —umbrales fijados sin ver el test—»**: hoy contradice directamente lo que declara el capítulo 5. `vault`
- [ ] **6.4** · Añadir a «Limitaciones» el supuesto de **adversario estático no adaptativo** del modelo de amenaza de §3.1. `vault`
- [ ] **6.5** · Añadir a «Limitaciones» que el FPR del ~10 % debe leerse **a prevalencia realista** y que la latencia publicada es **techo de laboratorio**. `vault`
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

---

## Bibliografía

**Estado medido:** 70 entradas vivas en el vault · **20 citadas** · **51 huérfanas** · 1 colgando (`[9]`).
La memoria usa el **27 %** de su propia bibliografía.

- [ ] **B1** · **Revisar las 51 huérfanas una a una** (lista en el Anexo B) y decidir: se rescatan poniéndoles marcador, o se excluyen del `.docx`.
      ⚠️ **No borrar antes de hacer las tareas de citas.** Muchas son huérfanas porque **falta el marcador**, no porque sobre la fuente: `[73]` Isolation Forest, `[75]` LOF, `[26]` Snort, `[58]` KDD Cup 99, `[22]` McHugh, `[19]` desbalance, `[13]` validación cruzada, `[16]` reject option, `[53]`–`[57]` ética y normativa. `vault`
- [ ] **B2** · Dar formato IEEE a las 4 entradas del `.docx` que son **URLs desnudas**, y fusionar la que duplica el enlace de Stallings. `Word`
- [ ] **B3** · Añadir año y edición al Stallings (5.ª ed., 2023) y año al Anderson. `Word`
- [ ] **B4** · Recuperar `[6, cap. 6]` Goodfellow: existe en el vault y **no llegó al `.docx`**. `Word`

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

| Concepto | Cita propuesta |
|---|---|
| Árbol de decisión | Breiman et al. 1984 (CART) / Quinlan 1986 |
| Ensembles | Dietterich 2000 |
| Random Forest | Breiman 2001 |
| Gradient Boosting | Friedman 2001 |
| HistGradientBoosting | Ke et al. 2017 (LightGBM) |
| k-NN | Cover y Hart 1967 |
| Semisupervisado one-class | Chandola et al. 2009 → `[30]`, viva |
| Isolation Forest | Liu, Ting y Zhou 2008 → `[73]`, viva |
| One-Class SVM | Schölkopf et al. 2001 (+ Cortes y Vapnik 1995) |
| LOF | Breunig et al. 2000 → `[75]`, viva |
| MLP / retropropagación | Rumelhart, Hinton y Williams 1986, o `[6, cap. 6]` |
| Autoencoder | Goodfellow et al. 2016, cap. 14 → `[6]` |
| k-means / clustering | MacQueen 1967 / Hastie et al. cap. 14 → `[12]` |

## Las 10 altas de 2.1.5 «Métricas»

Matriz de confusión, precisión (ec. 1), recall (ec. 2), FPR (ec. 3), F1 (ec. 5), macro y ponderado (ec. 6 y 7), curva ROC y AUC, curva PR, y el argumento de que PR es más informativa bajo desbalance.

Fuentes: **Fawcett 2006**, **Powers 2011**, **Sokolova y Lapalme 2009**, **van Rijsbergen 1979**, **Davis y Goadrich 2006**, **He y García 2009** → `[19]`, viva.

## Altas de 2.2 y 2.3

Definición de intrusión y de IDS, cadena de bloques del NIDS, despliegue inline/pasivo (**NIST SP 800-94** → `[25]`, viva) · ejes de la taxonomía (**Axelsson 2000**, **Debar et al. 1999**) · propiedades de firmas y anomalías (**García-Teodoro et al. 2009** → `[29]`, viva) · deriva y falsos positivos (**Sommer y Paxson 2010** → `[21]`, viva) · DARPA 1998 (**Lippmann et al. 2000**) · ejemplos de ataque por categoría (**Kendall 1999** → `[36]`, viva) · criterio de DL (**LeCun, Bengio y Hinton 2015**) · casos de uso defensivos (**`[4]` Chio, con localizador**) · conjunto cerrado (**`[61]` Scheirer**, ya usada en §5.3) · los tres usos de Arp et al. (**`[18]`, con localizador**).

## Altas de 3, 4, 5 y 6

- **Cap. 3:** los cuatro algoritmos de la tabla de anomalías · Random Forest y XGBoost en la de firmas · **SMOTE (Chawla et al. 2002)**.
- **Cap. 4:** los 3 placeholders de §4.2 · imbalanced-learn (Lemaître et al. 2017) · test KS (Massey 1951) · las 41 características (Lee y Stolfo 2000 → `[59]`, viva) · categorías canónicas · SMOTE + leakage · importancias de RF · O(n²) de OC-SVM · autoencoder para anomalías (Sakurada y Yairi 2014).
- **Cap. 5:** «el patrón dominante en la literatura» · «el célebre ~99 %» · comparación pareada (Demšar 2006 / Dietterich 1998) · O(n²) de OC-SVM.
- **Cap. 6:** la afirmación sobre el enfoque supervisado que domina la literatura.

---

# Anexo B · Las 51 huérfanas

Entradas vivas en `Bibliografía.md` que **no se citan ni una vez** en la memoria.
Las marcadas con **←** son las que el texto **sí usa conceptualmente** y solo les falta el marcador: rescatarlas debería ser el primer movimiento.

| n | Referencia | |
|---|---|---|
| 6 | Goodfellow, Bengio y Courville, *Deep Learning* | ← |
| 12 | Hastie, Tibshirani y Friedman, *ESL* | ← |
| 13 | Kohavi, validación cruzada y bootstrap | ← |
| 14 | scikit-learn, doc. `GridSearchCV` | ← |
| 15 | Bergstra y Bengio, Random Search | |
| 16 | Chow, error/reject tradeoff | ← |
| 19 | He y García, *Learning from Imbalanced Data* | ← |
| 21 | Sommer y Paxson, *Outside the Closed World* | ← |
| 22 | McHugh, crítica a las evaluaciones DARPA | ← |
| 26 | Roesch, Snort (LISA'99) | ← |
| 29 | García-Teodoro et al., anomaly-based NIDS | ← |
| 30 | Chandola, Banerjee y Kumar, *Anomaly detection: A survey* | ← |
| 31 | Khraisat et al., survey de IDS | ← |
| 32 | Barbará et al., ADAM | |
| 33 | Tombini et al., combinación serial anomalía + misuse | ← |
| 34 | Ptacek y Newsham, *Insertion, Evasion and DoS* | |
| 35 | Snort Users Manual, «Writing Snort Rules» | ← |
| 36 | Kendall, base de datos de ataques (tesis MIT) | ← |
| 38 | Strom et al., MITRE ATT&CK | |
| 39 | Russell y Norvig, *AIMA* | ← |
| 41 | Grinsztajn et al., árboles vs DL en tabular | |
| 42 | McElfresh et al., redes vs boosted trees | |
| 43 | Sahami et al., filtrado bayesiano de spam | |
| 46 | Szegedy et al., *Intriguing properties of neural networks* | |
| 47 | Goodfellow, Shlens y Szegedy, FGSM | |
| 48 | Biggio y Roli, *Wild patterns* | ← |
| 50 | Moustafa y Slay, UNSW-NB15 | ← |
| 51 | Sharafaldin et al., CIC-IDS2017 | ← |
| 52 | Pierazzi et al., adversarial ML en el espacio del problema | ← |
| 53 | Rudin, modelos interpretables en decisiones críticas | ← |
| 54 | Molnar, *Interpretable Machine Learning* | ← |
| 55 | RGPD — Reglamento (UE) 2016/679 | ← |
| 56 | Reglamento de IA — (UE) 2024/1689 | ← |
| 57 | Directiva NIS2 — (UE) 2022/2555 | ← |
| 58 | *KDD Cup 1999 Data*, UCI KDD Archive | ← |
| 59 | Lee y Stolfo, features y modelos para IDS | ← |
| 60 | Mitchell et al., Model Cards | |
| 62 | Erickson et al., TabArena | |
| 63 | Micci-Barreca, target encoding | |
| 64 | Pargent et al., regularized target encoding | |
| 65 | Hwang et al., hybrid IDS con firmas ponderadas | ← |
| 66 | Pendlebury et al., TESSERACT | |
| 67 | Behrouz et al., Nested Learning | |
| 68 | Ji et al., IDS multinivel | ← |
| 69 | Kim, Lee y Kim, híbrido anomalía + misuse | ← |
| 70 | Khraisat et al., stacking C5 + OC-SVM | ← |
| 71 | Shwartz-Ziv y Armon, *DL is not all you need* | |
| 72 | Hollmann et al., TabPFN | |
| 73 | Liu, Ting y Zhou, *Isolation Forest* | ← |
| 75 | Breunig et al., LOF | ← |
| 78 | Storkey, *When Training and Test Sets Are Different* | ← |

**Las de `[65]`, `[68]`, `[69]`, `[70]` y `[33]` son híbridos de IDS**: son exactamente el material que necesita el estado del arte de la tarea 2.10 y los tres trabajos de la 2.11.

---

# Anexo C · Dónde va exactamente cada cita

> [!warning] Los números de la columna «Marcador» que vienen del pase del 2026-08-24 son **números del `.docx`** (`[12]`-`[95]`, mapa en [[Bibliografia del docx - numeracion y anclas]] §2). Los números planos que ya estaban antes (`[25]`, `[36]`, `[73]`…) son **del vault** y siguen **pendientes de traducir** al Word.

> **Cómo se usa.** No hay números de línea a propósito: los de Word y los del vault se
> desplazan en cuanto editas algo por encima, y este proyecto ya ha mandado corregir líneas
> que habían dejado de existir. El ancla es el **fragmento literal**: cópialo en Ctrl+F,
> y el marcador va **al final de esa frase, antes del punto**.
>
> Aquí están las **69 altas**. Las medias están descritas en el Anexo A.

## Capítulo 1 (1 alta)

| Buscar este texto | Marcador |
|---|---|
| «…el de detección basada en el estado. Este último monitorea las sesiones de red» | NIST SP 800-94 → `[25]` |

## Capítulo 2 · §2.1.1–2.1.3 (1 alta)

| Buscar este texto | Marcador |
|---|---|
| «algoritmos y procesos que «aprenden» en el sentido de que son capaces de generalizar datos» | `[16, cap. 1]` (vault `[79]`) ⚠️ localizador no establecido (página) |

## Capítulo 2 · §2.1.4 «Algoritmos de ML» (14 altas, 13 anclas)

Todas al final del párrafo que describe cada algoritmo.

| Buscar este texto | Marcador |
|---|---|
| «Un árbol de decisión es una estructura jerárquica de nodos de decisión» | `[22]` (vault `[83]`) ⚠️ localizador no establecido |
| «Un conjunto (ensemble) combina varios clasificadores individuales» | `[23]` (vault `[84]`) |
| «El muestreo aleatorio decorrelaciona los árboles individuales y reduce la varianza» | `[24]` (vault `[85]`) |
| «cada árbol nuevo se entrena para corregir los errores residuales del conjunto acumulado» | `[25]` (vault `[86]`) |
| «discretizando las características continuas en un número fijo de contenedores» | `[26]` (vault `[87]`) |
| «el ejemplo más conocido de aprendizaje perezoso» | `[27]` (vault `[88]`) |
| «Estos algoritmos se denominan semisupervisados (one-class)» | `[30]` Chandola et al. |
| «La longitud media del camino de aislamiento a través del conjunto de árboles» | `[73]` Liu, Ting y Zhou |
| «busca la frontera —en el espacio transformado por un núcleo (kernel), típicamente el radial (RBF)—» | `[30]` (vault `[89]`) |
| «recibe una puntuación LOF elevada y se considera anómalo» | `[75]` Breunig et al. |
| «calculando los gradientes de todos los pesos mediante retropropagación» | `[32]` (vault `[90]`) |
| «un MLP empleado como autoencoder, que es el detector seleccionado para la etapa 1» | `[6, cap. 14]` |
| «k-means y el agrupamiento jerárquico como exponentes principales» | `[12, cap. 14]` |

## Capítulo 2 · §2.1.5 «Métricas» (10 altas)

Las de las ecuaciones van **en la frase que introduce la fórmula**, no en la fórmula.

| Buscar este texto | Marcador |
|---|---|
| «La matriz de confusión es el punto de partida de toda métrica de clasificación» | `[33]` (vault `[91]`) |
| «Precisión: De todas las veces que el sistema levantó una alarma de ataque» | `[35]` (vault `[93]`) ⚠️ nivel 2 — ver §5 del mapa |
| «Exhaustividad (recall): de todos los ataques reales, qué proporción detectó el sistema» | `[35]` (vault `[93]`) ⚠️ nivel 2 — ver §5 del mapa |
| «Tasa de falsos positivos (FPR): de todo el tráfico normal» | `[33]` (vault `[91]`) |
| «F1: la media armónica de precisión y recall» | `[36]` (vault `[94]`) ⚠️ localizador no establecido |
| «se calculan primero por clase, con el esquema uno-contra-el-resto» | `[34]` (vault `[92]`) |
| «Macro: se calcula la métrica de cada clase por separado y se promedian sin ponderar» | `[34]` (vault `[92]`) |
| «Su resumen numérico habitual es el área bajo la curva (AUC-ROC)» | `[33]` (vault `[91]`) |
| «Enfrenta la precisión frente al recall en cada umbral, con su propia área bajo la curva» | `[38]` (vault `[95]`) |
| «la curva ROC puede resultar engañosamente optimista» | `[38]` (vault `[95]`) |

## Capítulo 2 · §2.2 (19 altas)

| Buscar este texto | Marcador |
|---|---|
| «Una intrusión es cualquier acción, intencionada o no, que compromete la confidencialidad» | `[25]` NIST SP 800-94 |
| «monitoriza de forma continua los eventos que ocurren en un sistema o en una red» | `[25]` |
| «hereda de Denning (quien aportó el modelo IDES…)» | `[3]` — **mapear, no dar de alta** |
| «entronca con la tradición de Snort» | `[26]` Roesch — **ojo: hoy pone `[11]`, que es CRISP-DM** |
| «Sensor o captura. Obtiene el tráfico del segmento vigilado» | `[25]` |
| «La literatura no usa una taxonomía única sino varios ejes ortogonales» | `[39]` (vault `[96]`) ⚠️ nivel 2; **no confundir con `[46]`**, el otro Axelsson |
| «Se diferencia en este punto entre HIDS (host-based IDS) y NIDS» | `[25]` |
| «Es la taxonomía más citada del área y la que enmarca el problema de este TFG» | `[29]` García-Teodoro et al. |
| «es la modalidad que convierte al detector en un IPS» | `[25]` |
| «El conocimiento del analista de seguridad queda así codificado en una base de firmas» | `[26]` Roesch |
| «alta precisión sobre lo que cubre, alertas explicables y bajo volumen de falsas alarmas» | `[29]` |
| «La formulación original del enfoque se debe a Denning» | `[3]` — mapear |
| «mayor tasa de falsos positivos, alertas menos explicables y sensibilidad a la deriva (drift)» | `[21]` Sommer y Paxson |
| «existen trabajos que la adoptan, la invierten y la reformulan como conjunto paralelo» | `[33]` `[65]` `[68]` `[69]` `[70]` — **son la tarea 2.11** |
| «procede de las campañas de evaluación… del MIT Lincoln Laboratory para DARPA (1998)» | `[51]` (vault `[97]`) + `[23]` |
| «Ejemplos en el dataset: neptune (inundación de segmentos SYN)…» | `[36]` Kendall |
| «Ejemplos en el dataset: nmap, portsweep, ipsweep, satan» | `[36]` |
| «Ejemplos en el dataset: guess_passwd (fuerza bruta…)» | `[36]` |
| «Ejemplos en el dataset: buffer_overflow, rootkit, loadmodule, perl» | `[36]` |

## Capítulo 2 · §2.3 (5 altas)

| Buscar este texto | Marcador |
|---|---|
| «se habla de DL cuando la jerarquía de capas es lo bastante honda» | `[55]` (vault `[98]`) |
| «Detección de intrusiones en red / Análisis de malware / Anti-phishing y anti-spam / UEBA» | `[4, cap. …]` con localizador |
| «no produce «ninguna de las anteriores»: produce la categoría conocida más parecida» | `[61]` Scheirer et al. |
| ««each paper suffers from at least three pitfalls»» | `[18, p. …]` — **cita textual sin marcador** |
| «El pitfall P9 de Arp et al., Lab-Only Evaluation» y «el pitfall P10, Inappropriate Threat Model» | `[18, §…]` en ambas |

## Capítulo 3 (3 altas, 7 anclas)

En las **tablas de candidatos**, el marcador va en la celda «NOCIÓN DE ANOMALÍA» / «IDEA».

| Buscar este texto | Marcador |
|---|---|
| «Aísla las anomalías por particiones aleatorias» | `[73]` |
| «Aprende una frontera que encierra el comportamiento normal» | `[30]` (vault `[89]`) |
| «Compara la densidad local de cada punto con la de sus vecinos» | `[75]` |
| «Error de reconstrucción: reconstruye mal lo que no se parece a lo normal» | `[6, cap. 14]` |
| «Conjunto (ensemble) de árboles por bagging» | `[24]` (vault `[85]`) |
| «Conjunto por boosting (rendimiento tipo XGBoost)» | `[75]` (vault `[99]`) |
| «Comparar el sobremuestreo sintético (SMOTE) frente al reponderado de clases» | `[78]` (vault `[100]`) |

## Capítulo 4 (11 altas, 12 anclas)

| Buscar este texto | Marcador |
|---|---|
| `[enlace bibliografía: KDD Cup 99]` — **sustituir el placeholder entero** | `[58]` + `[51]` (vault `[97]`) |
| `[ enlace bibliografía: Tavallaee 2009]` — ×2, sustituir | `[23]` |
| `[ enlace bibliografía: McHugh 2000]` — sustituir | `[22]` |
| `[CITA: Tavallaee 2009 + survey de datasets NIDS]` — sustituir | `[52]` (vault `[23]`) + `[88, §5.5.4]` (vault `[74]`) |
| «Tratamiento del desbalance de clases: SMOTE dentro de un Pipeline» (tabla de librerías) | `[80]` (vault `[102]`) |
| «test de Kolmogórov-Smirnov para el análisis de drift» (tabla de librerías) | `[81]` (vault `[103]`) |
| «Las 41 características se agrupan en tres familias» | `[59]` Lee y Stolfo |
| «una de las cinco categorías canónicas de la literatura de NSL-KDD» | `[36]` + `[23]` |
| «las muestras sintéticas se interpolan a partir de vecinos reales» | `[78]` (vault `[100]`) + `[17]` |
| «se entrena un RandomForestClassifier (100 árboles, class_weight='balanced', semilla 42)» | `[24]` (vault `[85]`) |
| «Su coste de entrenamiento es O(n²) en memoria y tiempo» | `[30]` (vault `[89]`) |
| «las conexiones anómalas se reconstruyen mal y producen un MSE alto» | `[90]` (vault `[108]`) |

## Capítulo 5 (4 altas)

| Buscar este texto | Marcador |
|---|---|
| «su coste de entrenamiento O(n²) hace inviable ajustarlo con el conjunto completo» | `[30]` (vault `[89]`) |
| «Comparación pareada (semilla a semilla)» | `[92]` (vault `[109]`) + `[93]` (vault `[110]`) — **complementarias, no alternativas** |
| «el patrón dominante en la literatura sobre NSL-KDD: un RandomForest monolítico» | `[12]` (vault `[31]`) + `[52]` (vault `[23]`) — **sostiene la tesis**; ⚠️ «RandomForest monolítico» no está verificado en fuente: atenuar a «clasificador supervisado monolítico» si aprietan (§5 del mapa) |
| «El célebre "~99 % de accuracy" de la literatura no sobrevive al test oficial» | `[52, §I]` (vault `[23]`) Tavallaee *et al.* |

## Capítulo 6 (1 alta)

| Buscar este texto | Marcador |
|---|---|
| «frente al enfoque supervisado que domina la literatura sobre el NSL-KDD» | `[12]` (vault `[31]`) Khraisat *et al.* — mismo sostén que en el cap. 5 |


---

# Anexo D · Anclas de las 48 citas medias

> [!warning] Los números de la columna «Marcador» que vienen del pase del 2026-08-24 son **números del `.docx`** (`[12]`-`[95]`, mapa en [[Bibliografia del docx - numeracion y anclas]] §2). Los números planos que ya estaban antes (`[25]`, `[39, cap. 1]`, `[19]`…) son **del vault** y siguen **pendientes de traducir** al Word.

Mismo criterio que el Anexo C: busca el fragmento con Ctrl+F, el marcador va al final de la frase.
Estas son **defendibles sin cita**, pero suman rigor. Si vas justo de tiempo, haz primero el Anexo C.

## Capítulo 1 (3)

| Buscar este texto | Marcador |
|---|---|
| «Se han creado algoritmos basados tanto en Machine Learning (ML) como en IA» | `[12]` (vault `[31]`) Khraisat *et al.* 2019 |
| «estos algoritmos han sido fundamentales para la detección de ataques desconocidos» | `[13]` (vault `[77]`) Hindy *et al.* 2020 — ⚠️ se cita por el método, **no** por su 89-99 % |
| «Evasión del IDS/NIDS – el atacante conoce el mecanismo de detección y lo esquiva» | `[25]` NIST SP 800-94 |

## Capítulo 2 · §2.1.1–2.1.3 (8)

| Buscar este texto | Marcador |
|---|---|
| «los investigadores han perseguido enseñar a las computadoras a razonar» | `[39, cap. 1]` Russell y Norvig |
| «el algoritmo es el conjunto de instrucciones que dicen como aprender de los datos» | `[5, cap. 1]` Géron |
| «se limpian, transforman y dividen en subconjuntos de entrenamiento, validación y prueba» | `[12, cap. 7]` Hastie |
| «Reducción de dimensionalidad y visualización» | `[17, cap. 1]` (vault `[80]`) ⚠️ localizador no establecido (página) |
| «Reglas de asociación, que busca encontrar coocurrencias frecuentes» | `[18]` (vault `[81]`) |
| «Un agente aprende por interacción con un entorno, guiado por recompensas y penalizaciones» | `[19, cap. 1]` (vault `[82]`) ⚠️ localizador no establecido (página) |
| «un candidato algo peor pero mucho más estable puede ser preferible» | `[12, cap. 7]` |
| «los valores que el algoritmo no aprende de los datos— mediante validación cruzada» | `[5, cap. 2]` + `[13]` Kohavi |

## Capítulo 2 · §2.1.5 «Métricas» (5)

| Buscar este texto | Marcador |
|---|---|
| «VP (verdadero positivo): un ataque correctamente señalado como ataque» | `[33]` (vault `[91]`) |
| «la matriz pasa a ser de k x k, con k el número de clases» | `[34]` (vault `[92]`) |
| «Exactitud (accuracy): la proporción de predicciones correctas sobre el total» | `[34]` (vault `[92]`) |
| «un weighted alto, porque el peso n_i de la clase mayoritaria domina la suma» | `[19]` He y García |
| «no produce directamente una etiqueta, sino una puntuación continua» | `[33]` (vault `[91]`) |

## Capítulo 2 · §2.2 y §2.3 (5)

| Buscar este texto | Marcador |
|---|---|
| «el momento del análisis: tiempo real… y diferido (offline)» | `[25]` |
| «los 39 tipos de ataque específicos presentes en el corpus» | `[23]` |
| «Huella en el tráfico» (las cuatro apariciones: `serror_rate`, `count`, `hot`, `root_shell`) | `[59]` Lee y Stolfo |
| «designan conjuntos anidados: cada uno es un subconjunto estricto del anterior» | `[4]` — ya usada antes |
| «Un modelo de amenaza es la especificación explícita de las hipótesis sobre el adversario» | ⛔ **SIN NÚMERO — el fragmento no existe hoy ni en el vault ni en el `.docx`: no hay sede** (mapa §4.3) |
| «equivale a suponer un adversario que no modifica su comportamiento» | `[48]` Biggio y Roli |

## Capítulo 3 (8)

| Buscar este texto | Marcador |
|---|---|
| «las cuatro categorías canónicas del dataset NSL-KDD» | `[23]` |
| «siguiendo la línea de un IDS clásico basado en reglas» | `[26]` Roesch |
| «instanciar el caso, es decir, fijar un valor concreto en cada dimensión» | `[18]` |
| «produce puntos que ningún atacante real podría generar» | `[52]` Pierazzi et al. |
| «al no re-particionar el test, D2 conserva los tipos de ataque que no aparecen» | `[23]` |
| «se ajustan únicamente sobre el tráfico de entrenamiento (D1+D3)» | `[17]` Kapoor y Narayanan |
| «del árbol de decisión se extraen reglas legibles (mediante export_text)» | `[54, cap. …]` Molnar |
| «estimadas fuera de muestra (out-of-fold, mediante validación cruzada sobre D3)» | `[16]` Chow, reject option |

## Capítulo 4 (11)

| Buscar este texto | Marcador |
|---|---|
| «Python es el lenguaje de referencia para el aprendizaje automático» | ⛔ **SIN NÚMERO — no hay fuente de nivel 1-2; decide Francisco: atenuar la frase o retirarla** (mapa §4.3) |
| «Núcleo de ML: preprocesamiento (MinMaxScaler, LabelEncoder)» (fila de la tabla) | `[79]` (vault `[101]`) |
| Filas de NumPy · Pandas · Matplotlib · Seaborn de la misma tabla | Harris 2020 · McKinney 2010 · Hunter 2007 · Waskom 2021 |
| «etiquetaron cada registro de KDDTest+ con un valor de #successfulPrediction» | `[23, §…]` |
| «desde tasas en [0,1] hasta contadores de bytes con valores de cientos de millones» | `[5, cap. 2]` |
| «Se codifican mediante One-Hot Encoding (pd.get_dummies)» | `[5, cap. 2]` |
| «selección de modelo sobre el conjunto de test, es decir data snooping» | `[18]` — ya está, verificar |
| «LocalOutlierFactor se instancia con novelty=True» | `[14]` doc. scikit-learn |
| «un clasificador que nunca predijera u2r conservaría un accuracy superior al 99,9 %» | `[19]` |
| «las firmas deben poder leerse, auditarse y, llegado el caso, trasladarse a reglas» | `[54]` Molnar |
| «Es la firma canónica de un SYN flood tipo neptune» | `[36]` Kendall |

## Capítulo 5 (4)

| Buscar este texto | Marcador |
|---|---|
| «Su noción de anomalía basada en densidad local no captura bien la separación» | `[75]` Breunig et al. |
| «refleja el desplazamiento distribucional D3→D2 propio del NSL-KDD» | `[23]` |
| «el sobreajuste es invisible en validación cruzada» | `[12, cap. 15]` |
| «la captura del tráfico en la interfaz de red, el ensamblado de los paquetes en flujos» | `[21]` Sommer y Paxson |

## Capítulo 6 (4)

| Buscar este texto | Marcador |
|---|---|
| «firmas y anomalías no compiten, sino que se complementan» | `[29]` García-Teodoro et al. |
| «debido al desplazamiento distribucional entre el tráfico normal de entrenamiento y el de test» | `[23]` |
| «ningún algoritmo ni técnica de balanceo (SMOTE, class_weight) logra un rendimiento sólido» | `[19]` + `[78]` (vault `[100]`) |
| «el clasificador de firmas, cerrado, tiende a asignar con confianza etiquetas conocidas» | `[61]` Scheirer / `[49]` Bendale |

---

## Cuántas huérfanas se rescatan solas

Si haces los Anexos C y D completos, **quedan citadas 21 de las 51 huérfanas** sin decidir nada:

`[4]` `[12]` `[13]` `[14]` `[16]` `[19]` `[21]` `[22]` `[26]` `[29]` `[30]` `[33]` `[36]` `[39]` `[48]` `[52]` `[54]` `[58]` `[59]` `[73]` `[75]`
más `[65]` `[68]` `[69]` `[70]` si haces el estado del arte (tareas 2.10 y 2.11).

Es decir: **la lista real de descartes de la tarea B1 no son 51, sino unas 26**, y solo se puede
decidir *después* de las tareas de citas. Por eso B1 va al final del bloque de bibliografía.
