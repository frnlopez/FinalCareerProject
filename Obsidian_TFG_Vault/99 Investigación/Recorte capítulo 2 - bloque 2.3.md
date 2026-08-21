---
titulo: "Recorte capítulo 2 — bloque 2.3 Inteligencia Artificial"
tipo: informe de análisis
fecha: 2026-08-20
alcance: "2.3.1, 2.3.2, 2.3.3"
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
# Recorte capítulo 2 — bloque 2.3 Inteligencia Artificial

> [!warning] Atribución: qué pidió el profesor y qué no
> El profesor **no pidió recortar el capítulo 2**. Su petición literal, recogida en
> `mis-apuntes-del-informe.md`, es: «*El informe está bien en general, pero hay que mejorar bastante
> la redacción, simplificando las explicaciones de las soluciones analizadas sin dar todos los
> hiperparámetros **(por ejemplo, que aporta al lector saber si has usado como semilla el valor 42)**, quizás recortando algunos apartados (por ejemplo, los primeros apartados del
> Capítulo 3 no creo que sean necesarios y se podían unificar)*». El capítulo que señaló es el **3**.
>
> En consecuencia, la columna **(a)/(b)** de este informe marca:
> - **(a)** solo tres partidas, y como **extensión por analogía** de su frase «simplificando las
>   explicaciones de las soluciones analizadas sin dar todos los hiperparámetros» — no como algo que
>   él dijera del capítulo 2. Están identificadas una por una en §3.
> - **(b)** todo lo demás: recorte por volumen, decidido por Francisco el 2026-08-20 bajo el
>   criterio «quién lo usa».
>
> Ante el tribunal, la defensa correcta de casi todo este informe es «*lo decidí yo por volumen y
> por criterio de uso*», no «*me lo pidió usted*».

---

## 1. Resumen ejecutivo

### Método de conteo

Todas las cifras de este informe se han contado con Python sobre el texto de las notas, **no
estimadas**. Se declaran dos magnitudes distintas para que no se confundan:

| Magnitud | 2.3.1 | 2.3.2 | 2.3.3 | Total 2.3 |
|---|---|---|---|---|
| **`wc -w` del fichero completo** (incluye *frontmatter* y encabezados) | 2.109 | 3.408 | 4.689 | **10.206** |
| **Cuerpo contable** (excluye *frontmatter* y las líneas de encabezado) | 2.011 | 3.333 | 4.578 | **9.922** |

La aritmética de ahorro se hace **sobre el cuerpo contable (9.922)**, porque los encabezados no se
recortan: sobreviven o desaparecen con su apartado. La diferencia entre ambas columnas son 284
palabras de títulos y metadatos.

### Balance

| Concepto | Palabras |
|---|---|
| Cuerpo actual de 2.3 | **9.922** |
| Se queda tal cual | 2.982 |
| Se queda comprimido (objetivo de compresión) | 2.671 |
| **Total que se queda** | **5.653** |
| **Ahorro** | **4.269 (43,0 % del bloque)** |

De ese ahorro, **660 palabras son andamiaje editorial** que no debería llegar al `.docx` en ningún
escenario: los dos *callouts* `[!warning] … RETIRADO/RETIRADA el 2026-08-18` (125 + 155) y los dos
`[!warning] Verificación pendiente — sin acceso al texto completo` (189 + 191). Son notas de proceso
del proyecto, no prosa de la memoria. **Ese recorte es de coste cero y no requiere ninguna decisión
editorial.**

### Los tres hallazgos que gobiernan el bloque

1. **2.3.1 y 2.3.2 no tienen ni una sola remisión entrante desde fuera del capítulo 2.** `grep` de
   `[[2.3.1`/`[[2.3.2` sobre los capítulos 1, 3, 4, 5, 6, Apéndices y Preliminares devuelve
   **cero**. Las dos únicas remisiones entrantes a 2.3.1 vienen de dentro del propio capítulo 2
   (2.1.1 y 2.1.4). En cambio **2.3.3 recibe ocho remisiones entrantes explícitas** desde `3.1`,
   `6.1` (cinco) y `A.3` (dos). Es exactamente lo contrario de lo que anticipaba el encargo: **la
   nota de ética es la más usada de las tres**, y la que menos se toca.
2. **El solapamiento más caro del bloque no es con 2.1 ni con 2.2, sino con `3.5`**: el argumento
   «árboles frente a arquitecturas tabulares profundas» está en 2.3.1.4 (1) con `[41]` y `[42]`, y
   **otra vez, más completo, en `3.5` § *Por qué familias clásicas y no una arquitectura tabular
   profunda***, con las mismas dos citas más `[71]` y `[72]`. La sede es 3.5.
3. **Tres apartados están estructuralmente huérfanos**, verificado por terminología y no por
   ausencia de *wikilink*: 2.3.1.2 (historia de la IA), 2.3.2.3 (IA ofensiva y doble uso) y 2.3.3.7
   (marco regulatorio). Búsquedas nulas en los capítulos 1/3/4/5/6/Apéndices/Preliminares:
   `Dartmouth`, `sistemas expertos`, `doble uso`, `phishing`, `malware`, `RGPD`, `AI Act`, `NIS2`,
   `privacidad`, `supervisión humana`. Suman 1.105 palabras.

---

## 2. Tabla apartado por apartado

Palabras = cuerpo del apartado, incluidos sus *callouts* y tablas, excluida la línea del propio
encabezado.

### 2.3.1 IA, ML y Deep Learning — 2.011 → ~951

| Apartado | Palabras | Quién lo usa | Veredicto | Destino de lo retirado | (a)/(b) |
|---|---|---|---|---|---|
| Preámbulo (*El bloque anterior…* + *La delimitación no es un preámbulo…*) | 153 | Nadie; es transición interna | **COMPRIME A UN PÁRRAFO** (~40) | Nada: es prosa de enlace | (b) |
| 2.3.1.1 La jerarquía IA ⊃ ML ⊃ Deep Learning | 387 | `2.1.1` §2.1.1.1 remite aquí como «referencia canónica del vocabulario»; el *callout* «Dónde queda este TFG» lo instancian `3.1` y `4.1` | **COMPRIME** (~185) | La tabla de 3 filas → exposición | (b) |
| 2.3.1.2 Un recorrido histórico mínimo | 211 | **Nadie** | **SALE DEL CUERPO** | **Solo exposición** | (b) |
| 2.3.1.3 Reglas escritas a mano frente a reglas aprendidas | 339 | `2.1.1` §2.1.1.2 remite aquí por nombre; el *callout* de conexión sostiene el argumento de firmas legibles de `3.5`/`4.5` | **COMPRIME** (~130: solo el *callout* y una entradilla) | Tabla de perfiles de coste → exposición | (b) |
| 2.3.1.4 entradilla (*La ausencia de aprendizaje profundo…*) | 29 | Sostiene el apartado | **SE QUEDA** | — | — |
| 2.3.1.4 (1) La naturaleza tabular de los datos | 280 | **Duplicado por `3.5`** § *Por qué familias clásicas y no una arquitectura tabular profunda*, con las mismas citas `[41]`/`[42]` y más completo | **COMPRIME A UN PÁRRAFO** (~50, remitiendo a 3.5) | Nada: el texto ya existe en 3.5 | **(a)-extensión** |
| 2.3.1.4 (2) El requisito de interpretabilidad | 75 | `3.1` (requisito), `3.5`, `4.5` | **SE QUEDA** | — | — |
| 2.3.1.4 (3) Coste computacional y reproducibilidad | 71 | `3.1` viñeta *Sin dependencias pesadas de Deep Learning*, `4.1`, `4.4` | **COMPRIME** (~30) | Nada: ya está en 3.1/4.1 | (b) |
| 2.3.1.4 El único componente neuronal, y por qué no es «profundo» | 301 | **`2.1.4` §2.1.4.3.4 remite aquí por nombre de bloque**; `3.4`, `4.4` | **SE QUEDA** (~240) | El punto 1, con la arquitectura y `anomalias.py:86-88` → `4.4` (ya está allí) | **(a)-extensión** |
| 2.3.1.5 Situación del trabajo y transición | 164 | La tabla duplica la de `2.1.2` §2.1.2.7 (etapa → paradigma) | **COMPRIME** (~55: solo el párrafo de transición) | Nada: la tabla ya existe en 2.1.2.7 | (b) |

### 2.3.2 La IA en ciberseguridad — 3.333 → ~1.924

| Apartado | Palabras | Quién lo usa | Veredicto | Destino de lo retirado | (a)/(b) |
|---|---|---|---|---|---|
| Preámbulo + *callout* «Qué no se trata aquí» | 208 | Nadie; enrutado editorial | **COMPRIME A UN PÁRRAFO** (~95) | Nada | (b) |
| 2.3.2.1 entradilla + tabla de 5 casos de uso | 160 | Nadie por nombre, pero es el panorama compacto del apartado | **SE QUEDA** | — | — |
| 2.3.2.1 *Detección de intrusiones en red* | 133 | `3.2`, `3.3`: el «doble encaje» de los dos paradigmas en una misma familia metodológica es el fundamento del híbrido | **SE QUEDA** | — | — |
| 2.3.2.1 *Análisis de malware* / *Anti-phishing y anti-spam* / *UEBA* | 273 | **Nadie.** `malware`, `phishing`, `spam`, `UEBA` → cero apariciones fuera del capítulo 2 | **COMPRIME A UN PÁRRAFO** (~70 los tres juntos) | **Solo exposición** | **(a)-extensión** |
| 2.3.2.1 *callout* «Caso de uso RETIRADO el 2026-08-18» | 125 | Nadie: nota de proceso | **SALE DEL CUERPO** | `99 Investigación/` | (b) |
| 2.3.2.1 *callout* «Dónde se sitúa este TFG» | 91 | `2.2.4` | **SE QUEDA** | — | — |
| 2.3.2.2 La motivación real: lo que no está en el catálogo | 406 | **Núcleo argumental**: `3.2` §3.2.3 *De dónde sale la capacidad de detectar lo desconocido*, `5.3`, `6.1` límite 5 | **SE QUEDA** (~325) | El párrafo final de Sommer y Paxson (137) es la tercera repetición de una remisión que ya hacen 2.2.3.4 y 2.3.3.2 → media línea | (b) |
| 2.3.2.3 La otra cara: IA ofensiva y doble uso | 380 | **Nadie.** Y contradice el modelo de amenaza de `3.1` §3.1.5, explícitamente **no adaptativo** | **SALE DEL CUERPO** (~30 de mención en 2.3.2.6) | **Solo exposición** | (b) |
| 2.3.2.4 Adversarial ML: evasión y envenenamiento | 457 | `3.1` §3.1.5 fija «no envenena el entrenamiento» y «no intenta evadirlo»; `2.3.3.3` remite aquí; `6.1` límite 3 | **COMPRIME** (~305) | La cadena de 4 pasos del envenenamiento por reentrenamiento periódico (79) → exposición: **este sistema no se reentrena en línea** | (b) |
| 2.3.2.4 *El modelo que no sabe decir «no lo sé»* (sin el *callout*) | 284 | **El más usado de la nota**: `3.3`, `5.3` punto 2, `5.4`, `6.1` límite 5, `6.2` §6.2.2 | **SE QUEDA** | — | — |
| 2.3.2.4 *callout* «Verificación pendiente» | 189 | Nadie: nota de proceso | **SALE DEL CUERPO** | `99 Investigación/` | (b) |
| 2.3.2.5 entradilla + *El problema de fondo es estructural* | 153 | Nadie: el argumento de privacidad del corpus lo recoge 2.3.3.5 | **COMPRIME A UN PÁRRAFO** (~45) | Nada | (b) |
| 2.3.2.5 tabla de datasets (DARPA → CIC-IDS2018) | 179 | `6.2` propone la validación cruzada sobre **UNSW-NB15** y **CIC-IDS2017/2018** por nombre; es el único sitio de la memoria donde se describen | **SE QUEDA** | — | — |
| 2.3.2.5 *Qué se sigue de este panorama* | 89 | Es una remisión pura a 2.2.5.4 y 4.2, declarada como tal en su propio texto | **COMPRIME** (~25) | Nada: ya está en 2.2.5.4 | (b) |
| 2.3.2.5 *Lo que este apartado añade* (validación cruzada entre datasets) | 76 | `6.2` | **SE QUEDA** | — | — |
| 2.3.2.6 Cierre | 121 | Cierra la nota y enlaza con 2.3.3 | **SE QUEDA** | — | — |

### 2.3.3 Límites y consideraciones éticas — 4.578 → ~2.778

| Apartado | Palabras | Quién lo usa | Veredicto | Destino de lo retirado | (a)/(b) |
|---|---|---|---|---|---|
| Preámbulo (3 párrafos: marco de Arp et al. y la cita textual) | 270 | `6.1` §6.1.4.2 se ordena sobre «el catálogo de diez errores metodológicos […] introducido en 2.3.3» | **SE QUEDA** (~210) | El párrafo *El tratamiento es deliberadamente de marco teórico…* (95) es meta-comentario que `6.1` ya hace por su lado → una línea | (b) |
| 2.3.3.1 El coste de los falsos positivos en operación | 521 | **`2.2.4` §2.2.4.3 ya tiene la cadena completa Y la regla** «la tasa de falsos positivos se reporta siempre junto al recall» en su propio *callout* | **COMPRIME A UN PÁRRAFO** (~140: las dos viñetas propias) | Nada: es duplicado interno del capítulo 2, no material de exposición | (b) |
| 2.3.3.2 Evaluación de laboratorio frente a operativa (P9) | 625 | **`6.1` cita su *callout* «Alcance de este trabajo» por nombre**; fila P9 de `6.1.4.2` | **SE QUEDA** (~425) | Los factores 3 y 4 y el párrafo de Sommer y Paxson (133) → exposición | (b) |
| 2.3.3.3 El modelo de amenaza como requisito metodológico (P10) — los 4 bloques | 784 | **El apartado más citado de todo 2.3**: `3.1` §3.1.5 (por título), `6.1` límite 3 (por título), `A.3` dos veces (por título) | **SE QUEDA ÍNTEGRO** | — | — |
| 2.3.3.4 Explicabilidad: por qué en seguridad no es opcional | 512 | El requisito está en `3.1`/`3.5`; las reglas legibles en `4.5`. Pero **`SHAP`, `LIME` y *post-hoc* no aparecen en ningún otro capítulo** | **COMPRIME** (~330) | La entradilla y el párrafo de `[53]`/`[54]` (65) → exposición | (b) |
| 2.3.3.5 Privacidad del tráfico de red | 361 | **Nadie.** Cero apariciones de `privacidad`, `RGPD`, `minimización` fuera de esta nota. Su *callout* de conexión (sin carga útil ⇒ menos invasivo) sí es argumento propio | **COMPRIME A UN PÁRRAFO** (~130: el *callout*) | **Apéndice `A.3.11.7`**, junto con 2.3.3.7 | (b) |
| 2.3.3.6 Obsolescencia y sesgo de los datos de entrenamiento | 503 | *Límite de representación* → `6.1.3` *Tipos ciegos por el propio dataset*; el **macro-promedio** → `5.0`, `A.2`; el *callout* `snmpgetattack` → `5.x`, `6.2` | **SE QUEDA** (~390) | El párrafo *Límite de sesgo y obsolescencia del corpus* (113) duplica 2.2.5.4 y la contrapartida 5 de `4.2` → una línea con remisión | (b) |
| 2.3.3.7 Marco regulatorio y supervisión humana | 514 | Solo el *callout* «Postura adoptada»: modo pasivo, no bloquea, apoyo al analista → `3.2`, `2.2.3`. La tabla de tres normas: **nadie** | **SALE DEL CUERPO salvo el cierre** (~125) | Tabla RGPD/AI Act/NIS2 → **Apéndice `A.3.11.7`**. El *callout* «no se determina la categoría de riesgo» (155) → **solo exposición** | (b) |
| 2.3.3.8 Síntesis (tabla de 7 límites + conclusión) | 297 | La tabla solapa parcialmente con `6.1.4.1` (seis límites) y `6.1.4.2` (P9/P10) | **COMPRIME** (~230) | Nada | (b) |
| 2.3.3.8 *callout* «Verificación pendiente — Arp et al.» | 191 | Nadie: nota de proceso | **SALE DEL CUERPO** | `99 Investigación/` | (b) |

---

## 3. Las tres partidas marcadas (a), y por qué son extensión y no cita

El profesor no habló del capítulo 2. Estas tres partidas se marcan **(a)-extensión** porque la frase
que sí dijo —«*simplificando las explicaciones de las soluciones analizadas sin dar todos los
hiperparámetros*»— describe literalmente lo que hacen, aunque él lo dijera mirando el capítulo 3.
**La defensa honesta es: «apliqué su criterio de redacción también aquí», no «usted pidió recortar
el 2.3».**

1. **2.3.1.4 (1) *La naturaleza tabular de los datos* (280 palabras).** Es una revisión de
   literatura —Grinsztajn et al. `[41]`, el estudio comparativo `[42]`— sobre *soluciones
   analizadas* que no son la del trabajo. Y está **duplicada** en `3.5` § *Por qué familias clásicas
   y no una arquitectura tabular profunda*, donde además es mejor: enumera las cinco condiciones, da
   los números (19 algoritmos, 176 conjuntos) y añade `[71]` y `[72]` con el límite de 10.000
   muestras de TabPFN frente a las 58.630 de D3. Mantener las dos versiones es precisamente el
   defecto de redacción señalado.
2. **2.3.1.4 *El único componente neuronal*, punto 1 (dentro de las 301 palabras).** Dice
   «*perceptrones multicapa de tres capas ocultas y anchura decreciente-creciente, del orden de
   decenas de neuronas por capa (`anomalias.py:86-88`)*». Es **dar los hiperparámetros en el marco
   teórico**, exactamente lo que él pide no hacer, y además está ya en `4.4`, que es su sede.
   Añadido: la referencia `anomalias.py:86-88` incumple la norma del propio proyecto de citar por
   título y no por `fichero:línea`.
3. **2.3.2.1 *Análisis de malware* / *Anti-phishing y anti-spam* / *UEBA* (273 palabras).** Tres
   explicaciones de soluciones analizadas que el trabajo no usa: análisis estático frente a
   dinámico, filtros bayesianos, perfilado de identidades. Es (a)-extensión por la misma frase, y
   además (b) por volumen, porque ninguna tiene consumidor.

Todo lo demás de este informe es **(b)**: decisión de Francisco del 2026-08-20 por volumen y por
criterio de uso.

---

## 4. Justificación por apartado

### 4.1 Lo que se queda entero, y por qué no se toca

- **2.3.3.3 (P10, modelo de amenaza), 784 palabras.** Es el apartado de mayor rendimiento por
  palabra de todo el bloque. `3.1` §3.1.5 dice literalmente «*El marco conceptual —qué es un modelo
  de amenaza, en qué seis dimensiones se especifica y por qué un trabajo de detección debe
  escribirlo en lugar de asumirlo— está en 2.3.3 § El modelo de amenaza como requisito metodológico
  (P10), y **no se repite aquí***». La tabla de seis dimensiones se instancia fila a fila en `3.1`;
  `6.1` límite 3 y la fila P10 de `6.1.4.2` la citan por título; `A.3` la cita dos veces. Recortarla
  rompería cuatro remisiones vivas.
- **2.3.2.4 *El modelo que no sabe decir «no lo sé»*, 284 palabras.** Es la teoría que explica una
  cifra publicada: el 13,4 % de 0-day detectados que llegan a `unknown`. `5.3` la usa como punto 2
  de su lectura, `5.4` la cita en sus conclusiones, `6.1` la hace su límite 5, `6.2` §6.2.2 la
  convierte en línea futura, `3.3` la invoca en el protocolo. Cinco consumidores.
- **2.3.2.2 (0-day como motivación de la arquitectura), 406 palabras.** Es el argumento por el que
  el sistema es híbrido. `3.2` §3.2.3 se titula *De dónde sale la capacidad de detectar lo
  desconocido*: sin 2.3.2.2 ese título no tiene antecedente.
- **2.3.3.2 (P9), 625 palabras.** `6.1` la cita **por el nombre de su *callout*** («*callout
  «Alcance de este trabajo»*»), que es el enunciado de marco del que su límite 2 es la instancia.
  Una remisión a un *callout* concreto es la forma más fuerte de uso que hay en esta memoria.
- **2.3.2.5 tabla de datasets, 179 palabras.** `6.2` propone entrenar sobre NSL-KDD y evaluar sobre
  UNSW-NB15 y CIC-IDS2017/2018. Es el único lugar de la memoria que dice qué son esos conjuntos.

### 4.2 Lo que sale del cuerpo

- **2.3.1.2 *Un recorrido histórico mínimo* (211).** Dartmouth 1956, los inviernos de la IA, los
  sistemas expertos, ImageNet 2012. Verificado por terminología: `Dartmouth` y `sistemas expertos`
  no aparecen en ningún otro fichero de la memoria. El propio apartado se justifica diciendo que la
  historia «*se recoge aquí solo en la medida en que explica el vocabulario que se acaba de
  fijar*» — pero el vocabulario ya lo fija la tabla de 2.3.1.1, así que la tabla histórica es la
  segunda vez. **Destino: solo exposición, no apéndice.** Un apéndice de esta memoria es material de
  verificación (columnas del dataset, fórmulas de métricas, ficha del sistema); una cronología de la
  IA no se verifica ni se reproduce, y un lector que la quiera la encuentra en `[39, cap. 1]`, que ya
  está citado. Meterla en el apéndice sería mover el bulto, no resolverlo.
- **2.3.2.3 *La otra cara: IA ofensiva y doble uso* (380).** Ingeniería social a escala,
  suplantación audiovisual, descubrimiento de vulnerabilidades asistido, malware adaptativo. Es el
  apartado más desconectado del bloque, y no solo por falta de remisión: **contradice el alcance
  declarado**. `3.1` §3.1.5 fija un adversario no adaptativo y sin conocimiento del modelo, y `6.1`
  límite 3 lo repite. Un apartado sobre atacantes que usan IA generativa describe justamente el
  adversario que el trabajo declara no evaluar. Ya perdió su párrafo de cierre el 2026-08-18 al
  retirarse `[37]` y `[45]`, de modo que hoy son cuatro viñetas descriptivas sin tesis. **Destino:
  solo exposición.** Es material de conversación, no de consulta.
- **2.3.3.7 tabla RGPD / AI Act / NIS2 (139) y el *callout* «no se determina la categoría de riesgo»
  (155).** Sin ningún consumidor. La tabla **sí va a apéndice** (ver §4.4); el *callout*, no:
  declara que el trabajo **no** determinó la categoría de riesgo del sistema. Un límite declarado es
  un activo cuando alguien lo va a usar —P9 y P10 lo son, `6.1` los instancia—, pero este no lo usa
  nadie y su único efecto en el cuerpo es abrir en el lector la pregunta que no responde. **Destino:
  solo exposición**, con la respuesta preparada (§6, P4).
- **Los cuatro *callouts* editoriales (660).** Dos «RETIRADO/RETIRADA el 2026-08-18» y dos
  «Verificación pendiente — sin acceso al texto completo». Documentan decisiones de gestión de citas
  y estados de verificación. **Destino: `99 Investigación/`**, donde ya viven `Reconstrucción de las
  47 citas colgantes.md` y `pase-bibliografia-2026-08-18.md`. No son material de defensa ni de
  apéndice: son bitácora.

### 4.3 Lo que se comprime porque se menciona pero no se usa

- **2.3.3.1 (521 → ~140).** El caso más claro de duplicación interna del capítulo 2. `2.2.4`
  §2.2.4.3 *El falso positivo como coste operativo real* ya desarrolla la falacia de la tasa base
  con Axelsson `[24]`, ya tabula la cadena de cuatro pasos hasta el abandono del IDS, y ya enuncia
  en su propio *callout* la regla operativa: «*la tasa de falsos positivos se reporta siempre junto
  al recall, nunca por separado*». 2.3.3.1 lo vuelve a contar en 521 palabras para llegar a la misma
  regla, y su *callout* de conexión (el umbral p95 sobre `D1_val`) es la **cuarta** vez que se cuenta
  esa decisión: está en 2.2.4.2, en `3.4` y en `4.4`. Lo único propio son las dos viñetas —triaje
  por heurísticas informales y pérdida de cobertura no documentada—. Se quedan esas.
- **2.3.1.1 (387 → ~185).** El *callout* «Dónde queda este TFG» se queda: es la declaración de
  casilla que `3.1` y `4.1` instancian. La tabla de tres filas se va: `2.1.1` §2.1.1.1 ya tiene la
  **Figura 2.1** con la relación anidada y la explica con `[4]`. El criterio de separación ML/DL en
  prosa (95 palabras) también se queda, porque es lo que hace falta para el argumento de 2.3.1.4, y
  `2.1.4` §2.1.4.3.4 remite aquí para él.
- **2.3.1.3 (339 → ~130).** Se queda el *callout* de conexión, que es donde está el argumento vivo:
  en lugar de escribir las firmas se aprenden y se devuelven legibles con `export_text`, y de ahí
  tiran `3.5` y `4.5`. Se va la tabla de perfiles de coste, porque `2.1.1` §2.1.1.2 ya opone
  programación tradicional y ML con **tres figuras (2.2, 2.3, 2.4)** y `2.2.4` §2.2.4.4 ya compara
  los dos paradigmas de detección en tabla. Sería la tercera tabla de la misma oposición.
- **2.3.3.4 (512 → ~330).** La interpretabilidad como requisito ya está en `3.1`, la elección de
  familias en `3.5`, las reglas extraídas en `4.5`. Lo propio de este apartado son las tres razones
  operativas (triaje, justificación ante terceros, depuración) y la tabla interpretable-por-
  construcción frente a *post-hoc*, que sitúa al sistema en la primera fila. Eso se queda. El
  párrafo de `[53]` y `[54]` se va: `SHAP`, `LIME` y *post-hoc* no aparecen en ningún otro capítulo.
  **Nota para el `researcher`:** ese párrafo es el **último uso vivo de `[54]` Molnar**, y
  `CLAUDE.md` registra que a `[54]` solo le queda pendiente el localizador «*para su uso en 2.3.3*».
  Si el párrafo se recorta, `[54]` queda sin marcador vivo y hay que decidir si se quema o se
  conserva. **No lo he tocado y no debe decidirse desde este informe.**
- **2.3.3.5 (361 → ~130).** Se queda el *callout* de conexión, que hace un argumento real y propio:
  NSL-KDD no conserva carga útil, luego el diseño es menos invasivo **por construcción**, con la
  salvedad honesta de que reduce la exposición del contenido pero no la de los metadatos, y con la
  convergencia con el cifrado generalizado de `2.2.3`. Los cinco principios del RGPD aplicados al
  diseño del sensor se van: son correctos y no los usa nadie.
- **2.3.3.6 (503 → ~390).** Se queda el *límite de representación* (`6.1.3` lo instancia como *Tipos
  ciegos por el propio dataset*), el criterio de macro-promedio (lo aplican `5.0` y `A.2`) y el
  *callout* de `snmpgetattack`. Se va el párrafo de sesgo y obsolescencia del corpus, que repite
  `2.2.5` §2.2.5.4 con las mismas citas `[22]` y `[23]` y la contrapartida 5 de `4.2`.
- **2.3.3.8 (488 → ~230).** La tabla de siete límites se queda comprimida: es útil como cierre del
  capítulo, pero cuatro de sus siete filas (P9, P10, sesgo/obsolescencia, límite de representación)
  reaparecen en `6.1.4.1` y `6.1.4.2` con instancia y cifras. La conclusión metodológica —«ninguno
  de los siete se resuelve dentro del modelo, luego se declaran»— se queda: es la tesis que `6.1`
  ejecuta.

### 4.4 Apéndice: una sola incorporación, y por qué solo una

De las 4.269 palabras retiradas, **solo ~250 van a apéndice**. El criterio: un apéndice de esta
memoria es material que alguien podría querer **consultar o verificar** (A.1 columnas del dataset,
A.2 fórmulas de métricas, A.3 ficha del sistema). Lo que sale de 2.3 por falta de uso es en su
mayoría **argumentación**, y la argumentación no se consulta: o convence en el cuerpo o no hace
falta.

**Propuesta: `A.3.11.7 Privacidad y marco regulatorio (excedente de 2.3.3.5 y 2.3.3.7)`.**

- **Precedente exacto en disco.** `A.3` ya tiene `A.3.10 Algoritmos del marco teórico que el sistema
  no emplea`, con subsecciones rotuladas «*excedente de 2.1.4.1*» y «*excedente de 2.1.4.4*», y
  `A.3.11 Desarrollo metodológico ampliado`, que aloja seis desarrollos sacados de 2.1.3 y 2.1.6. El
  patrón está establecido y el rótulo también.
- **Contenido:** los cinco principios de diseño del sensor derivados del RGPD (112) y la tabla de
  las tres normas con sus citas `[55]`, `[56]`, `[57]` (139), más el marco mínimo que las hace
  legibles.
- **Por qué estas dos y no las otras.** Son las únicas dos partidas retiradas que tienen forma de
  **referencia**: una lista cerrada de principios y una tabla de tres normas con su reglamento y su
  año. Un lector o un tribunal puede querer verlas. La historia de la IA, la IA ofensiva y las
  cadenas argumentales duplicadas no tienen esa forma: son prosa que se lee una vez.
- **Bonus de coherencia.** Las tres citas `[55]`, `[56]` y `[57]` conservan así su marcador vivo y no
  hay que decidir si se queman.

---

## 5. Solapamientos detectados con 2.1 y 2.2 (y con el capítulo 3)

Esta es la sección que el hilo principal debe cruzar con los informes de 2.1 y 2.2.

| # | Contenido duplicado | Sedes | Sede que debe quedarse | Palabras recuperables en 2.3 |
|---|---|---|---|---|
| 1 | Argumento «árboles frente a arquitecturas tabulares profundas», citas `[41]` y `[42]` | 2.3.1.4 (1) · **`3.5` § *Por qué familias clásicas y no una arquitectura tabular profunda*** | **`3.5`** (más completo: 5 condiciones, `[71]`, `[72]`, límite de TabPFN) | ~230 |
| 2 | Jerarquía anidada IA ⊃ ML ⊃ DL | 2.3.1.1 (tabla de 3 filas) · **`2.1.1` §2.1.1.1 (Figura 2.1 + prosa + `[4]`)** | Reparto: la figura y la definición se quedan en `2.1.1`; 2.3.1.1 conserva **solo** el criterio de separación ML/DL (que `2.1.4` §2.1.4.3.4 necesita) y el *callout* de casilla | ~200 |
| 3 | Reglas escritas a mano frente a reglas inducidas de datos | 2.3.1.3 · **`2.1.1` §2.1.1.2 (Figuras 2.2–2.4)** · `2.2.4` §2.2.4.4 | `2.1.1` para el concepto general, `2.2.4` para la oposición de paradigmas de detección. 2.3.1.3 conserva **solo** el puente al sistema (firmas aprendidas y devueltas legibles) | ~209 |
| 4 | Falacia de la tasa base, fatiga de alertas, regla «recall siempre con FPR» | 2.3.3.1 · **`2.2.4` §2.2.4.3** (con `[24]`, tabla de 4 pasos y la regla en su *callout*) | **`2.2.4` §2.2.4.3** | ~380 |
| 5 | Umbral p95 sobre `D1_val` como decisión de diseño | 2.3.3.1 *callout* · `2.2.4` §2.2.4.2 · `3.4` · `4.4` | `3.4` (decisión) y `4.4` (implementación) | ~129 |
| 6 | Tabla etapa → paradigma de supervisión | 2.3.1.5 · **`2.1.2` §2.1.2.7** | **`2.1.2` §2.1.2.7** | ~110 |
| 7 | Sesgo y obsolescencia del corpus DARPA/KDD, citas `[22]` y `[23]` | 2.3.3.6 · **`2.2.5` §2.2.5.4** · `4.2` contrapartida 5 | **`2.2.5` §2.2.5.4** | ~113 |
| 8 | Sommer y Paxson / *semantic gap* | **Se enuncian en `2.2.3` §2.2.3.4 y `2.1.6`**, y se «no-reenuncian» explícitamente en 2.3.2.2 (137) y en 2.3.3.2 (133) | `2.2.3` §2.2.3.4 | ~200: **decir tres veces que no se va a repetir algo cuesta más que repetirlo una vez.** Basta media línea de remisión en cada sede |
| 9 | Régimen *one-class* como caso frontera | 2.3.1.4 punto 4 · 2.3.2.1 (*doble encaje*) · **`2.1.2` §2.1.2.6** (que además fija la regla terminológica canónica) | `2.1.2` §2.1.2.6 para el término; 2.3.2.1 conserva el *doble encaje*, que es argumento propio del híbrido | ~40 |
| 10 | Espacio de características frente a espacio del problema, cita `[52]` | **2.3.3.3** (200) · `3.1` viñeta *La representación no admite una perturbación realizable* (62) · `6.1` límite 3 (~100) | **2.3.3.3 es la sede y se queda entera.** Las copias a recortar están en `3.1` y `6.1`, **fuera de mi alcance** | 0 en 2.3 · **~100 recuperables en `6.1`** |

**El solapamiento que se temía no existe.** El encargo anticipaba que 2.3.2 duplicaría a 2.2 en «IA
aplicada a ciberseguridad». No ocurre: 2.3.2 se protege con un *callout* explícito («Qué no se trata
aquí») y cumple lo que promete —la taxonomía de IDS y la oposición firmas/anomalías no se
reenuncian—. El solapamiento real de 2.3.2 es **hacia adentro**: su §2.3.2.1 desarrolla cuatro casos
de uso que el trabajo no usa, y su §2.3.2.3 desarrolla un adversario que el trabajo declara no
evaluar.

> [!warning] Dependencia dura entre los tres informes de recorte
> He comprimido 2.3.3.1, 2.3.3.6 y las tres remisiones a Sommer y Paxson **apoyándome en que
> `2.2.4` §2.2.4.3, `2.2.5` §2.2.5.4 y `2.2.3` §2.2.3.4 sobreviven**. Si el informe de 2.2 propone
> recortar cualquiera de esas tres sedes, **los ítems 4, 5, 7 y 8 de esta tabla dejan de ser
> válidos** y hay que rehacer esos veredictos. En particular: si `2.2.4` §2.2.4.3 se recortara, la
> regla «recall siempre junto al FPR» se quedaría **sin sede** en toda la memoria. 2.3 comprime
> **contra** 2.2, no en paralelo a ella.

---

## 6. Material para la DEFENSA ORAL

> [!danger] RECONCILIACIÓN CON EL DISCO — 2026-08-21 (ficha F3)
> Este §6 se redactó en tiempo futuro-hecho («*retirado del cuerpo*», «*el desarrollo va a…*»)
> **antes de ejecutar el recorte**, y el recorte que después se ejecutó sobre `2.3` **fue parcial**:
> de las nueve partidas P1–P9, **solo dos se aplicaron**. Es el mismo defecto que el §5 del informe
> de `2.2`, y la corrección es la misma:
>
> **En todo este §6 hay que leer «retirado del cuerpo» como «material de esa sede, retirado o no».**
> El valor del bloque para la defensa oral **no cambia** —el guion de respuesta sirve igual—; lo que
> **no** puede hacerse es usarlo como registro de qué se recortó. Estado real, verificado apartado
> por apartado sobre las tres notas de `2.3` el **2026-08-21**:
>
> | Partida | Sede declarada | Estado real |
> |---|---|---|
> | **P1** naturaleza tabular de los datos | `2.3.1.4 (1)` | **NO APLICADO** — íntegro, hoy en **`2.3.1.3 § (1)`** (ver la renumeración abajo), con `[41]`, `[42]` y el enlace a `[[clasificadores-tabulares-y-arquitecturas-hibridas]]`. La duplicación con `3.5` **sigue viva en las dos sedes** |
> | **P2** detalle de arquitectura del autoencoder | `2.3.1.4` → `4.4` | **NO APLICADO** — el punto 1 conserva «*tres capas ocultas y anchura decreciente-creciente, del orden de decenas de neuronas por capa (`anomalias.py:86-88`)*», con la referencia `fichero:línea` incluida. Era la única partida **(a)** ejecutable de forma mecánica y no se ejecutó |
> | **P3** privacidad y RGPD | `2.3.3.5` → `A.3.11.7` | **NO APLICADO, y el destino NO EXISTE** — los cinco principios siguen en el cuerpo, y **`A.3` no tiene ninguna sección `A.3.11.7`**: `A.3.11` sigue con seis subapartados. `A.3.11.7` era una **propuesta** del §4.4, y este §6 la daba por hecha |
> | **P4** categoría de riesgo del AI Act | `2.3.3.7`, *callout* | **NO APLICADO** — el *callout* «Alcance declarado: no se determina la categoría de riesgo» sigue en el cuerpo, y con él la tabla RGPD / AI Act / NIS2 de tres filas |
> | **P5** IA ofensiva y doble uso | `2.3.2.3` | **APLICADO** — el apartado conserva el encabezado y una declaración de tres líneas que remite a `3.1` §3.1.5; las cuatro viñetas descriptivas no están. `[37]` y `[45]` no reaparecen |
> | **P6** malware · anti-phishing · UEBA | `2.3.2.1` | **NO APLICADO** — los tres siguen desarrollados en un párrafo cada uno, con `[43]` y `[3]`. Lo que sí se fue es la fila «Apoyo al SOC» como texto: **queda solo como fila de la tabla**, sin párrafo y sin `[44]` |
> | **P7** recorrido histórico de la IA | `2.3.1.2` | **APLICADO** — retirado íntegro. `Dartmouth`, `sistemas expertos` e ImageNet no aparecen en `2.3.1`, y `[40]` Krizhevsky quedó quemada en consecuencia (R1, 2026-08-20) |
> | **P8** cadena del envenenamiento | `2.3.2.4` | **NO APLICADO** — los cuatro pasos siguen enumerados en el cuerpo, con su frase de cierre |
> | **P9** explicabilidad | `2.3.3.4` | **NO APLICADO** — la entradilla, las tres razones operativas, la tabla interpretable/*post-hoc* y el párrafo con `[53]` **y `[54]`** siguen íntegros. **Consecuencia para el `researcher`: `[54]` Molnar conserva su marcador vivo** y el cabo 1 del §7 sigue abierto, no resuelto |
>
> **Renumeración que hay que tener presente al buscar cualquier apartado de `2.3.1`.** Al retirarse
> el antiguo `2.3.1.2` (P7), los tres siguientes subieron un número. Correspondencia verificada:
>
> | En este informe | Hoy en disco |
> |---|---|
> | `2.3.1.2` recorrido histórico | **no existe** (retirado) |
> | `2.3.1.3` reglas escritas a mano frente a aprendidas | `2.3.1.2` |
> | `2.3.1.4` por qué ML clásico y no *deep learning* (y sus tres puntos y «El único componente neuronal») | `2.3.1.3` |
> | `2.3.1.5` situación del trabajo y transición | `2.3.1.4` |
>
> Ojo con el efecto colateral: **`2.3.3.4` remite a «`2.3.1` (§2.3.1.2)»** para el mecanismo de las
> reglas legibles, y con la numeración nueva ese puntero **acierta por casualidad** —`2.3.1.2` es hoy
> justamente el apartado de reglas escritas a mano frente a aprendidas—. No hay nada que arreglar,
> pero conviene saber que no es una remisión revisada, es una coincidencia.
>
> **Lectura correcta:** los §1–§5 siguen siendo defendibles como plan, pero **el ahorro de 4.269
> palabras que anuncia el §1 no se ha realizado**, y las 9.922 palabras contadas allí siguen siendo,
> en su mayor parte, las que hay. Reabrir cualquiera de los siete «NO APLICADO» es **una decisión
> nueva de Francisco**, no la ejecución de un pendiente.

Lo retirado del cuerpo, ordenado por la pregunta previsible del tribunal que responde. Cada bloque
lleva lo suficiente para contestar sin volver a la nota.

### P1. «¿Por qué no ha usado *deep learning*? Hoy todo el mundo lo usa.»

**Fuente:** 2.3.1.4 (1) *La naturaleza tabular de los datos* — **hoy `2.3.1.3 § (1)`; recorte
PLANIFICADO, NO EJECUTADO:** sigue íntegro en el cuerpo, y la duplicación con `3.5` sigue viva en las
dos sedes. La respuesta oral vale igual, y además **se puede señalar en la memoria**.

**Respuesta:** tres argumentos independientes, cada uno suficiente. (i) NSL-KDD es tabular y
estructurado: 41 características por conexión, 125.973 registros de entrenamiento, sin imágenes ni
texto libre, es decir sin ninguna de las modalidades donde el DL saca su ventaja, que viene de
aprender la representación en lugar de recibirla. (ii) La evidencia empírica: Grinsztajn et al.
`[41]`, sobre 45 conjuntos, sitúa los modelos de árboles como estado del arte en tamaños medios e
identifica tres propiedades que las redes tabulares no resuelven —robustez frente a características
no informativas, preservación de la orientación de los datos y aprendizaje de funciones
irregulares—. Y el estudio comparativo más amplio `[42]`, 19 algoritmos sobre 176 conjuntos,
caracteriza qué conjuntos favorecen a los árboles: **grandes, con razón alta entre muestras y
características, y distribuciones sesgadas e irregulares** — los tres rasgos de NSL-KDD tras el
preprocesado. (iii) TabPFN v2, el modelo fundacional tabular publicado en *Nature*, está especificado
para hasta **10.000 muestras**, y D3 tiene **58.630** `[72]`.

**Cierre:** «No sostengo que el DL tabular no sirva; sostengo que este problema cae en el cuadrante
donde la evidencia publicada dice que no compensa. Y el argumento está en el capítulo 3, donde se
toma la decisión, no en el marco teórico.»

### P2. «Su sistema tiene un autoencoder. ¿No es eso una red neuronal? ¿No es *deep learning*?»

**Fuente:** 2.3.1.4 *El único componente neuronal* — **hoy dentro de `2.3.1.3`**. Se queda en el
cuerpo, como estaba previsto, pero **el traslado del detalle de arquitectura a `4.4` NO se ejecutó**:
el punto 1 sigue dando las tres capas ocultas y la referencia `anomalias.py:86-88`.

**Respuesta:** cuatro hechos. (i) Escala: perceptrón multicapa de tres capas ocultas, decenas de
neuronas por capa. (ii) Implementación: `MLPRegressor` de scikit-learn, sin TensorFlow ni Keras, sin
GPU. (iii) Papel: no alimenta a nadie con una representación jerárquica; produce **un escalar**, el
error de reconstrucción, que se compara con un umbral. (iv) Régimen: semisupervisado *one-class*,
solo con D1. «Una red neuronal, sí. Profunda, no: el criterio no es usar neuronas, es que el
aprendizaje de representaciones sea el mecanismo principal del modelo.»

### P3. «¿Y la privacidad? Está monitorizando el tráfico de personas. ¿Ha considerado el RGPD?»

**Fuente:** 2.3.3.5. **Recorte PLANIFICADO, NO EJECUTADO:** el apartado sigue completo en el cuerpo,
con los cinco principios y el *callout*, y **`A.3.11.7` no existe en `A.3`** — era una propuesta del
§4.4, no un destino creado.

**Respuesta:** sí, y con una precisión honesta. Una IP asociable a una persona física identificable
es **dato personal**, luego un IDS cae en el ámbito del RGPD `[55]`. Hay una tensión estructural: más
observación, mejor detección; menos observación, menos intrusión. Se gestiona con cinco principios
sobre el diseño del sensor: **minimización** (solo los atributos necesarios, no captura íntegra por
defecto), **limitación de la finalidad** (no reutilizar para vigilar el rendimiento de empleados),
**limitación del plazo de conservación**, **seudonimización** de identificadores de red, y **trabajo
sobre metadatos en lugar de contenido**.

**La parte fuerte:** la quinta mitigación describe exactamente este trabajo: NSL-KDD **no contiene
carga útil**, cada registro es un resumen estadístico de una conexión. El diseño es menos invasivo
por construcción.

**La parte honesta, que hay que decir sin que la pregunten:** reduce la exposición del **contenido**,
no la de los **metadatos**, que siguen siendo datos personales cuando son atribuibles. Y converge
con una restricción técnica ya expuesta en `2.2.3`: el cifrado generalizado hace inaccesible el
contenido de todos modos. «Lo que aquí es virtud ética es también, en buena medida, necesidad
práctica.»

### P4. «¿En qué categoría del AI Act cae su sistema? ¿Es de alto riesgo?»

**Fuente:** 2.3.3.7, *callout* «Alcance declarado: no se determina la categoría de riesgo». **Recorte
PLANIFICADO, NO EJECUTADO:** el *callout* y la tabla de las tres normas siguen en el cuerpo, así que
la respuesta de abajo **está escrita en la memoria** y no solo en este guion.

**Respuesta:** «**No lo he determinado, y no lo voy a afirmar sin haber leído el texto consolidado y
sus anexos en EUR-Lex.** Lo que sí expongo es el enfoque basado en riesgo del Reglamento (UE)
2024/1689 `[56]` —prácticas prohibidas, alto riesgo, riesgo limitado, riesgo mínimo— y sus
obligaciones transversales: gestión de riesgos, calidad de los datos, documentación técnica,
transparencia y **supervisión humana**. Afirmar una categoría sin ese respaldo sería exactamente el
tipo de afirmación sin sustento que este trabajo evita en cualquier otro terreno. Es una limitación
declarada, y es reversible: se cierra consultando el texto oficial.»

**Complemento si insisten:** las otras dos normas relevantes son el RGPD `[55]`, por el dato
personal, y NIS2 —Directiva (UE) 2022/2555 `[57]`—, que impone a sectores esenciales e importantes
medidas de gestión de riesgos y **obligaciones de detección y notificación de incidentes**: es el
contexto normativo que empuja el despliegue de sistemas como este.

### P5. «¿Y si el atacante usa IA? ¿Su sistema resiste a un atacante con IA generativa?»

**Fuente:** 2.3.2.3 *La otra cara: IA ofensiva y doble uso* — **RECORTE EJECUTADO**: del cuerpo queda
solo el encabezado y una declaración de tres líneas que remite a `3.1` §3.1.5. Las cuatro
manifestaciones de abajo **ya no están en la memoria**, así que este guion es su única sede.

**Respuesta en dos tiempos.** Primero, el reconocimiento: el doble uso no es un riesgo emergente, es
una **característica estructural del campo**, porque la tecnología es genérica, pública y de coste
decreciente, y nada en ella distingue el propósito. Cuatro manifestaciones: **ingeniería social a
escala** (la generación de texto elimina los indicios que delataban el *phishing* —errores
gramaticales, traducción torpe, registro impersonal— y permite personalizar con información pública
de la víctima, difuminando la frontera entre correo masivo y ataque dirigido); **suplantación
audiovisual** (síntesis de voz e imagen contra procedimientos de autorización que descansan en el
reconocimiento humano); **descubrimiento de vulnerabilidades asistido** (*fuzzing* dirigido, revisión
de código en busca de patrones explotables — la misma herramienta que usa el defensor para auditar);
y **automatización y adaptación del malware** (selección automática de objetivos, evasión adaptativa,
variación del comportamiento según el entorno observado).

Segundo, el acotamiento: «**Mi modelo de amenaza, escrito en `3.1` §3.1.5, es explícitamente un
adversario no adaptativo que no conoce el modelo. Un atacante asistido por IA es adaptativo. Está
fuera de lo que este trabajo mide, y lo digo antes de que me lo pregunten.**»

> [!warning] Salvedad que hay que respetar en la defensa
> La afirmación agregada de que «*el efecto principal es el descenso de la barrera de entrada y el
> aumento de escala de los ataques existentes, no un ataque cualitativamente nuevo*» **se retiró el
> 2026-08-18** porque las dos citas que la sostenían (`[37]`, `[45]`) son informes de agencia cuya
> edición no se pudo fijar. **No usarla como afirmación respaldada.** Si sale, decir que es
> apreciación propia sin fuente fechada.

### P6. «El *machine learning* en seguridad no es nuevo. ¿Qué más se hace con él?»

**Fuente:** 2.3.2.1. **Recorte PLANIFICADO, NO EJECUTADO:** los tres casos de uso siguen desarrollados
en un párrafo cada uno. Lo único que cambió es «Apoyo al SOC», que **hoy es solo una fila de la tabla**
—sin párrafo propio— tras retirarse `[44]` el 2026-08-18.

**Respuesta:** cuatro familias además de la propia. **Análisis de malware**, en dos vías: estático
(cadenas, secciones, entropía, funciones importadas, *n-gramas* de opcodes — rápido, pero lo degradan
la ofuscación y el empaquetado) y dinámico (ejecución en *sandbox*: llamadas al sistema, escrituras
en registro, conexiones de red — resiste la ofuscación, pero cuesta mucho más y el malware puede
detectar el entorno e inhibirse). **Anti-phishing y anti-spam**: el caso de éxito más antiguo y
consolidado — los filtros bayesianos demostraron que un modelo estadístico entrenado con ejemplos
supera a una lista de reglas mantenida a mano, y sobre todo que **se adapta** cuando el remitente
cambia de táctica, mientras que la lista hay que reescribirla `[43]`. **UEBA**: perfil de
comportamiento habitual por usuario y por equipo —horarios, volúmenes, recursos, ubicaciones— y
alerta por desviación; conceptualmente **no es una técnica nueva, es detección de anomalías aplicada
a identidades en lugar de a flujos**, la línea que abre Denning `[3]` con los perfiles estadísticos
de uso legítimo, llevada al producto comercial décadas después con telemetría corporativa masiva.
**Apoyo al SOC**: priorización y correlación de alertas — mencionable, pero **sin cita respaldada**,
porque `[44]` se retiró el 2026-08-18 por irreconstruible.

**El puente:** «UEBA y mi etapa 1 comparten fundamento: se modela lo normal y se alerta por
desviación. Heredan las mismas virtudes —cobertura de lo no catalogado— y los mismos costes —falsas
alarmas y sensibilidad a la deriva del perfil.»

### P7. «¿De dónde viene todo esto? ¿Cuándo empezó la IA?»

**Fuente:** 2.3.1.2, **RECORTE EJECUTADO**: retirada íntegra del cuerpo, y con ella el último uso de
`[40]` Krizhevsky, **hoy quemada**. Los cinco hitos de abajo **ya no están en la memoria**: no se puede
señalar el apartado, hay que contarlos. Y **`[40]` no se cita**, porque la entrada está retirada.

**Respuesta:** cinco hitos. **1956**, Conferencia de Dartmouth: acta fundacional de la disciplina y
del propio término. **Décadas de 1970 y 1980**: ciclos de expectativa y retracción, los «inviernos
de la IA» — el campo avanza por oleadas y las promesas han excedido a los resultados más de una vez.
**Años 80**: auge de los **sistemas expertos**, cumbre del paradigma de reglas, con el conocimiento
del especialista codificado a mano en una base de reglas. **Años 90 y 2000**: consolidación del **ML
estadístico** — el conocimiento deja de escribirse y pasa a estimarse a partir de datos. **Desde
2012**: los resultados de las convolucionales profundas en ImageNet dan nombre y tracción al
aprendizaje profundo como subcampo diferenciado `[40]`.

**Por qué importa aquí:** «La transición entre las dos etapas centrales es exactamente la que
atraviesa mi trabajo en su propio dominio: el paso del conocimiento escrito a mano al conocimiento
inducido de los datos. Y mi etapa 2 hace las dos cosas: induce las reglas con ML y las devuelve con
la explicabilidad del enfoque clásico.»

### P8. «¿Cómo se envenena un detector de anomalías?»

**Fuente:** 2.3.2.4. **Recorte PLANIFICADO, NO EJECUTADO:** la cadena de cuatro pasos sigue enumerada
en el cuerpo, con su frase de cierre.

**Respuesta:** cuatro pasos. (1) El detector define «normal» a partir del tráfico que ve en
producción. (2) Un atacante con presencia persistente inyecta poco a poco tráfico de su propio
ataque, en cantidades que no disparan alarma. (3) En cada reentrenamiento ese tráfico entra en la
definición de normalidad. (4) Tras suficientes ciclos, el ataque **ya no es una desviación del
perfil: forma parte de él**, y el detector deja de señalarlo por el mecanismo mismo que lo hacía
eficaz. «La propiedad que da al detector su capacidad de adaptación —aprender de lo que observa— es
la misma que lo hace vulnerable a que le enseñen lo que no debe.»

**El acotamiento:** «Mi sistema **no se reentrena en línea**: se entrena una vez sobre D1 y se evalúa
en diferido sobre D2. El envenenamiento por reentrenamiento periódico no le aplica, y por eso `3.1`
§3.1.5 declara un adversario que no envenena el entrenamiento. Es una condición del montaje
experimental, no una defensa que yo haya construido.»

### P9. «¿Por qué explicabilidad? ¿No basta con que acierte?»

**Fuente:** 2.3.3.4. **Recorte PLANIFICADO, NO EJECUTADO:** la entradilla, las tres razones operativas,
la tabla interpretable/*post-hoc* y el párrafo con `[53]` y `[54]` siguen íntegros en el cuerpo. **Por
tanto `[54]` Molnar conserva su marcador vivo** y el cabo 1 del §7 sigue abierto.

**Respuesta:** tres razones operativas, no estéticas. **Triaje**: el analista decide en minutos;
«anómalo, puntuación 0,87» no orienta esa decisión, «coincide con el patrón de conexiones
semiabiertas hacia un mismo puerto» sí — es la manifestación operativa del *semantic gap*.
**Justificación ante terceros**: bloquear una dirección, aislar un equipo o notificar un incidente
tiene consecuencias para personas y para el negocio, y debe poder motivarse ante una auditoría o ante
el afectado. **Depuración**: sin explicación no se distingue un acierto por la razón correcta de un
acierto por **correlación espuria** del corpus — es la única vía práctica para detectar que el modelo
aprendió un artefacto del dataset en lugar del fenómeno.

**El argumento fuerte, que sí queda en el cuerpo:** se ha defendido que en decisiones de alto riesgo
es preferible **sustituir** la explicación *post-hoc* de un modelo opaco por un modelo interpretable
desde el diseño, precisamente porque una explicación aproximada puede diferir de la lógica efectiva
del sistema `[53]`. «Mi etapa de firmas está en la primera fila de esa tabla, no en la segunda:
devuelve las reglas del árbol, no una aproximación de SHAP. Un analista puede leerlas, contrastarlas
con su conocimiento del dominio y discutirlas — impracticable con un *ensemble* de cientos de
árboles.»

---

## 7. Cabos que este informe deja abiertos (no los he tocado)

1. **`[54]` Molnar se queda sin marcador vivo** si se recorta el párrafo final de 2.3.3.4, que es su
   único uso restante según `CLAUDE.md`. Decisión del `researcher`, en pase serie, no desde aquí.
2. **Varias citas cambian de estado** si se aplican estos recortes. **Actualizado el 2026-08-21:**
   `[40]` (ImageNet) ya perdió su único uso al ejecutarse la retirada de 2.3.1.2 y **está quemada**
   desde R1 (2026-08-20); `[54]` **sigue viva**, porque el recorte de 2.3.3.4 no se ejecutó. `[43]` (filtros bayesianos) sobrevive solo si el párrafo comprimido de 2.3.2.1
   conserva la mención; `[55]`, `[56]` y `[57]` sobreviven **porque van al apéndice** — ese es parte
   del motivo de proponerlo. **Requiere un pase del `researcher` posterior a la edición, con recuento
   en disco**, no una estimación.
3. **Triplicación de *espacio de características / espacio del problema*** (ítem 10 de §5): la sede
   es 2.3.3.3 y se queda; las ~100 palabras recuperables están en `6.1` límite 3. **Fuera de mi
   alcance**; se traslada al hilo principal.
4. **Dependencia dura con los informes de 2.1 y 2.2**: ver el *callout* al final de §5.
5. **Cifras a recontar tras editar.** Las palabras «que se quedan» son **objetivos de compresión**,
   no medidas de un texto que exista: lo contado con exactitud es el estado **actual** (9.922
   palabras, desglosado hasta el párrafo). Cuando la edición se aplique, hay que volver a contar con
   `wc -w`. **No dar 5.653 como una cifra medida.**
