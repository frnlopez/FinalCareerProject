---
titulo: "Recorte de la memoria — barrido de capítulos 1, 3, 4, 5, 6, preliminares y apéndices"
tipo: informe de análisis
fecha: 2026-08-20
alcance: "Capítulos 1, 3, 4, 5, 6, Preliminares y Apéndices. NO cubre el capítulo 2."
estado: "análisis; DESFASADO como registro — R1 y R2 se ejecutaron después (ver la reconciliación del §8, 2026-08-21)"
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

> [!danger] DOS RECORTES BLOQUEADOS por la auditoría (NO APTO) — verificados en disco el 2026-08-20
> **Ninguno de los dos se ejecuta.** Los dos son el mismo fallo: un recorte justificado con «ya está
> en otro sitio» **sin comprobar ese otro sitio**.
>
> 1. **`1.2 Preliminares` / «detección basada en el estado» — NO SE RECORTA.** Se propuso retirarla
>    por duplicar `2.2.2`. **Contado en disco: la expresión aparece SOLO en `1.2`.** No hay segunda
>    sede, así que el recorte no la unifica: la **borra del trabajo**. Agravante: el informe de `2.2`
>    comprime a la vez `2.2.2.2` alegando que «ya está en `1.2`». **Apoyo recíproco** — aplicados los
>    dos, el contenido desaparece de ambos lados.
> 2. **El «cifrado» — NO SE RETIRAN todas sus sedes.** El informe de `2.2` las retira todas, pero
>    `2.3.3.5` conserva a propósito un callout que **remite a `2.2.3`** justo para eso. Verificado:
>    `cifrad` vive hoy en `2.2.1`, `2.2.2`, `2.2.3`, `2.2.5` y `2.3.3`. Aplicar el recorte deja la
>    remisión de `2.3.3` **colgando**.
>
> **REGLA QUE QUEDA, y es la que este pase estuvo a punto de incumplir:** antes de recortar algo
> «porque ya está en X», **se verifica X en disco**; y **dos informes no pueden justificar cada uno su
> recorte con el otro**. Si dos sedes se señalan mutuamente, **una se designa canónica y la otra
> remite** — no se recortan las dos.
# Recorte de la memoria — barrido de capítulos 1, 3, 4, 5, 6, preliminares y apéndices

> [!warning] Qué es y qué no es este informe
> Es un **barrido de prescindibles evidentes**, no el análisis detallado que se está haciendo sobre
> los tres bloques del capítulo 2. **Ninguna nota de la memoria se había editado al redactarlo** —el
> único fichero escrito entonces fue este—. **Eso ya no describe el disco:** R1 y R2 se ejecutaron
> después sobre `A.3`. El estado real, partida por partida, está en la reconciliación del §8.
>
> **El capítulo 2 queda fuera del alcance** y no se analiza aquí: lo cubren tres informes hermanos.
> Donde una propuesta de este informe toca al capítulo 2, se limita a **señalar la sede canónica
> ajena** y a recortar el lado que sí es de mi alcance.

> [!important] Los dos carriles, y por qué no se mezclan
> El profesor pidió esto y **solo** esto (cita literal, `mis-apuntes-del-informe.md`):
> «*El informe está bien en general, pero hay que mejorar bastante la redacción, simplificando las
> explicaciones de las soluciones analizadas sin dar todos los hiperparámetros **(por ejemplo, que aporta al lector saber si has usado como semilla el valor 42)**, quizás recortando
> algunos apartados (por ejemplo, los primeros apartados del Capítulo 3 no creo que sean necesarios
> y se podían unificar)*».
>
> - **(a) Carril del profesor.** Solo tres cosas caben aquí: **simplificar la redacción**, **no
>   volcar todos los hiperparámetros** y **recortar/unificar apartados**, con el capítulo 3 como
>   único ejemplo que él nombró.
> - **(b) Carril de volumen.** Todo lo demás. Lo sugiere el tamaño (108.591 palabras, ~360 páginas)
>   y **lo decide Francisco**. **No se atribuye al profesor.**
>
> **Lo del capítulo 3 que el profesor señaló YA ESTÁ HECHO** y no se vuelve a proponer: verificado
> en `features.md` — la ficha `T9` («Cita en el punto de la decisión — capítulo 3») quedó resuelta y
> la Tanda B del 2026-08-18 registró que **S1–S15 no tenían nada que ejecutar, ya estaban en disco**
> (`3.3.3` suprimida con su paso 1 trasplantado a `3.2`, cero punteros caducados). Lo que este
> informe propone sobre el capítulo 3 es **otra cosa**, un solo excurso de `3.5`, y va marcado como tal.

> [!check] Reglas de conteo cumplidas
> Todas las cifras de este informe salen de **`wc -w` sobre disco** (2026-08-20). Donde el volumen
> de un pasaje **no se puede conocer antes de ejecutar el recorte** —los casos de *condensación*, en
> que el texto se reescribe más corto y no se suprime— **el delta se marca `PENDIENTE`** y se publica
> únicamente **la base contada**. Este proyecto lleva tres episodios de cifras infladas; ninguna
> estimación a ojo entra aquí.
>
> **La deduplicación cruzada de los capítulos 4-6 ya se ejecutó** (D1–D18, `99 Investigación/Datos
> repetidos en los capítulos 4-6.md`, resultado medido el 2026-08-19: **−1.545 palabras, −3,4 %**).
> Este barrido **no la repite**: parte de las bases post-D18, que son las que se verifican en disco
> hoy (cap. 4 = 15.702, cap. 5 = 19.400, cap. 6 = 8.404). Lo que se propone aquí es material que
> **no era duplicación** y por eso D1–D18 no lo tocó.

---

## 1. Resumen ejecutivo

### 1.1 Ahorro CONTADO (supresión o traslado de bloques delimitados)

| # | Bloque | Sede | Palabras | Carril | Destino |
|---|---|---|---:|---|---|
| **R1** | Tabla de 98 filas de `#### Bloque de calidad (98 celdas)` | `A.3` §A.3.6 | **3.366** | (b) | Fuera de la memoria → `Resultados/dispersion_semillas.csv` / `.md` (versionados) |
| **R2** | Tabla de 100 filas de `#### Bloque de máquina (NO es calidad y NO se cita como resultado)` | `A.3` §A.3.6 | **3.044** | (b) | Fuera de la memoria → mismos CSV |
| **R3** | Tabla de rejillas de `## Algoritmos y espacios de búsqueda` | `4.4` | **70** | **(a)** | Traslado a `A.3` §A.3.3 |
| **R4** | Las dos tablas de márgenes de balanceo de `### 5.2.4.4 La decisión de balanceo no es constante entre semillas` | `5.2` | **231** | **(a)** | Traslado a `A.3` §A.3.6 |
| | **Total que sale del cuerpo** | | **6.711** | | |
| | **Total que sale de la MEMORIA** (R1+R2) | | **6.410** | | |
| | **Total que solo se muda al apéndice** (R3+R4) | | **301** | | |

**Efecto en el reparto:** `A.3` pasa de **15.325** a **≈8.915 + 301 = ≈9.216** palabras, y los
apéndices de **18.323** a **≈12.214**. La memoria baja de **108.591** a **≈102.181** palabras
(**−5,9 %**) sin condensar una sola frase de prosa y **sin perder ningún dato**: R1 y R2 son la
transcripción literal de un CSV versionado (`Resultados/dispersion_semillas.csv`, **198 filas de
datos = 98 de calidad + 100 de máquina**, comprobado con `wc -l` y `git ls-files`).

### 1.2 Ahorro por CONDENSACIÓN (base contada, delta PENDIENTE)

Aquí no se suprime contenido: se reescribe más corto. **El porcentaje solo se conoce recontando
después**, así que se publica la base y nada más.

| # | Bloque | Sede | Base contada | Carril |
|---|---|---|---:|---|
| **C1** | `### 6.1.4.1 Los seis límites, uno a uno` | `6.1` | 1.982 | **(a)** redacción |
| **C2** | `## 5.0.6 El mismo filtro, aplicado a uno mismo` (+ sus tres subapartados) | `5.0` | 1.900 | **(a)** redacción |
| **C3** | `### 5.2.4.4` sin sus tablas (que ya van en R4) | `5.2` | 1.284 | **(a)** hiperparámetros |
| **C4** | `### Tamaño y reparto de los subconjuntos` | `4.2.1` | 1.530 | (b) |
| **C5** | `## El sistema frente a la literatura publicada sobre NSL-KDD` | `5.4` | 1.261 | (b) |
| **C6** | `## 5.0.4 Prohibiciones explícitas` | `5.0` | 1.150 | **(a)** redacción |
| **C7** | `# Preliminares` (relato histórico Anderson → Denning → Snort → desafíos) | `1.2` | 1.110 | **(a)** unificar apartados |
| **C8** | `### 6.1.4.2 Balance frente al catálogo de errores metodológicos` (prosa; la tabla de 10 filas **se queda**) | `6.1` | 1.011 (463 sin tabla) | (b) |
| **C9** | `### Por qué familias clásicas y no una arquitectura tabular profunda` | `3.5` | 844 | **(a)** simplificar soluciones analizadas |
| **C10** | `## 6.1.1 Grado de cumplimiento de los objetivos` | `6.1` | 748 | (b), baja prioridad |
| **C11** | `## Qué NO mide la latencia publicada` | `5.4` | 661 | (b) |
| **C12** | `# Sinopsis` frente a `# Estructura` | `1.0` / `1.4` | 534 + 663 | **(a)** unificar apartados |
| | **Base total sometida a condensación** | | **14.678** | |

**Titular honesto:** lo único que se puede afirmar hoy es el **−6.410 contado** (−5,9 % de la
memoria). Los 14.678 de C1–C12 son **base**, no ahorro: llamarlos ahorro sería el cuarto episodio de
cifra inflada de este proyecto.

---

## 2. Apéndices — 18.323 palabras, de las que `A.3` sola tiene 15.325

### 2.1 Qué es `A.3` y cómo se reparte

Contado con `wc -w` sobre `Apéndices/A.3 Ficha del sistema.md`:

| Sección | Palabras |
|---|---:|
| `A.3.1 Detalles del modelo` | 366 |
| `A.3.2 Particiones de datos` | 594 |
| `A.3.3 Configuraciones seleccionadas (semilla 42)` (3 subapartados) | 377 |
| `A.3.4 Alcance de cada métrica` | 370 |
| `A.3.5 Infraestructura de cómputo y entorno` | 139 |
| **`A.3.6 Análisis cuantitativo: dispersión entre semillas`** | **8.413** |
| `A.3.7 Limitaciones declaradas` (3 subapartados) | 1.278 |
| `A.3.8 Checklist de reproducibilidad` | 564 |
| `A.3.9 Procedencia de los datos de este apéndice` | 283 |
| `A.3.10 Algoritmos del marco teórico que el sistema no emplea` | 624 |
| `A.3.11 Desarrollo metodológico ampliado` (6 subapartados) | 1.909 |
| `Notas relacionadas` | 38 |

**Veredicto general: `A.3` está justificada como género y NO a su tamaño actual.** Una ficha del
sistema es exactamente el sitio correcto para rejillas, configuraciones ganadoras, umbrales,
infraestructura y *checklist* de reproducibilidad — es lo que el propio `1.4` promete al lector
(«*el cuerpo de la memoria explica qué se decidió y por qué, mientras que los valores concretos
[…] viven en la ficha del sistema*»). El problema es que **el 55 % del apéndice es una sola
sección**, `A.3.6`, y dentro de ella **el 82 % son dos tablas** que reproducen a mano un fichero
que ya está versionado.

### 2.2 R1 y R2 — las dos tablas de `A.3.6` deben salir incluso del apéndice

| Bloque | Filas de tabla | Palabras de tabla | Palabras del bloque |
|---|---:|---:|---:|
| `#### Bloque de calidad (98 celdas)` | 98 + cabecera | **3.366** | 3.372 |
| `#### Bloque de máquina (NO es calidad y NO se cita como resultado)` | 100 + cabecera | **3.044** | 3.534 |

**Por qué salen, y por qué el argumento no es «son largas»:**

1. **Son una transcripción, no un análisis.** `Resultados/dispersion_semillas.csv` está **versionado**
   (`git ls-files Resultados` lo confirma, junto a `dispersion_semillas.md` y
   `comparaciones_pareadas.csv`) y contiene **198 filas de datos: las 98 de calidad y las 100 de
   máquina**. Las dos tablas del apéndice **no añaden ni una columna** al artefacto. Un apéndice de
   reproducibilidad cumple su función **citando el artefacto**; copiarlo dentro es lo que multiplica
   páginas sin añadir información, y encima introduce una segunda copia que puede desincronizarse.
2. **El propio texto declara que el bloque de máquina no es un resultado.** Su título literal es
   «*NO es calidad y NO se cita como resultado*» y el bloque remata: «*En ningún caso son estos
   segundos una propiedad del algoritmo*». Una tabla de 100 filas cuyo propio encabezado prohíbe
   citarla es el prescindible más limpio de toda la memoria fuera del capítulo 2.
3. **Lo que sostiene afirmaciones vivas se conserva, y está contado.** Las tres remisiones externas
   a `A.3.6` que existen en el vault (verificadas con `grep`) son:
   - `4.4`, párrafo «*Esos segundos son wall-clock de un pase único en una máquina no dedicada*» →
     apunta a «§A.3.6, *Bloque de máquina*». **Se repara solo**: lo que consume son los **cuatro
     párrafos en viñeta y el `[!warning]` de `ac496cb`**, que se quedan (el bloque son 3.534
     palabras, de las que **490 son prosa**). Solo desaparece la tabla.
   - `5.2`, «*Sobre el bloque de calidad del barrido, **13 de 98 celdas** […]*» → el «13 de 98» lo
     acredita la tabla `#### Celdas fuera de banda, por distancia` (**15 filas, 392 palabras**), que
     **se queda íntegra**. Es precisamente el resumen que hace innecesario el volcado.
   - `6.1`, límite 4, «*13 de 98 celdas de calidad*» y «*`Resultados/dispersion_semillas.md`*» →
     ya remite al artefacto, no a la tabla.

   **Ninguna remisión se rompe.** No hay ni una cita a una fila individual de los dos volcados.
4. **Qué queda en su lugar.** `A.3.6` conserva: su entradilla (135), `Alcance y método del barrido`
   (295), `El titular (semilla 42) frente a la banda` (525, **cero tablas**, es el análisis),
   `Celdas fuera de banda` (392, la tabla que sí se lee) y `Decisiones no constantes entre semillas`
   (295). Es decir **1.642 palabras de análisis** en lugar de 8.413, con una frase nueva de remisión
   al CSV. **Eso es lo que un tribunal puede leer.**

> [!note] Carril
> R1 y R2 son **(b) volumen** y los decide Francisco. El profesor no habló de apéndices. Lo que sí
> se le puede decir con honestidad es que **el criterio que él pidió —no volcar todos los
> hiperparámetros— se cumple mejor así**: la ficha pasa de volcar a referenciar.

### 2.3 Resto de `A.3` y los otros dos apéndices — veredicto por sección

| Bloque | Palabras | Veredicto | Destino | Carril |
|---|---:|---|---|---|
| `A.3.1`–`A.3.5` | 1.846 | **Se queda.** Es el núcleo de la ficha: modelo, particiones, configuraciones ganadoras, alcance de métricas y entorno. Justificado a su tamaño | — | — |
| `A.3.6` tabla de calidad | 3.366 | **Sale de la memoria** (R1) | CSV versionado | (b) |
| `A.3.6` tabla de máquina | 3.044 | **Sale de la memoria** (R2) | CSV versionado | (b) |
| `A.3.6` resto | 1.642 | **Se queda** | — | — |
| `A.3.7 Limitaciones declaradas` | 1.278 | **Se queda.** Material de defensa de primer orden (rutas *hardcodeadas*, las tres decisiones tomadas sobre D2). El subapartado `Límite de protocolo…` (918) es el más largo y el más valioso | — | — |
| `A.3.8 Checklist de reproducibilidad` | 564 | **Se queda.** Es lo que respalda el objetivo de reproducibilidad | — | — |
| `A.3.9 Procedencia de los datos de este apéndice` | 283 | **Se queda**, y gana importancia tras R1/R2: es donde vive el puntero al artefacto | Ampliar con la remisión de R1/R2 | — |
| `A.3.10 Algoritmos que el sistema no emplea` | 624 | **Se queda.** Llegó aquí en la Tanda A por la restricción T7 (nada se borra); devolverlo al cuerpo sería revertir esa decisión | — | — |
| `A.3.11 Desarrollo metodológico ampliado` | 1.909 | **Se queda**, misma razón que `A.3.10`. **Aviso: es el bloque a vigilar si Francisco quiere más recorte**, porque es marco teórico alojado en un apéndice y su sede natural es el capítulo 2 — que **no es alcance de este informe** | Decisión de Francisco, coordinada con los informes del cap. 2 | (b) |
| `A.1 Columnas del dataset NSL-KDD` | 1.280 | **Se queda.** Tabla de referencia de las 41 columnas; es el uso canónico de un apéndice | — | — |
| `A.2 Métricas de desempeño` | 1.718 | **Se queda.** Fórmulas + `A.2.2`, que también recibió excedente de T7 | — | — |

---

## 3. Capítulo 5 — 19.400 palabras

Es el capítulo donde el criterio del profesor muerde de verdad: **«simplificando las explicaciones
de las soluciones analizadas sin dar todos los hiperparámetros»**.

| Bloque | Palabras | Veredicto | Destino | Carril |
|---|---:|---|---|---|
| `5.0.1` + `5.0.2` + `5.0.3` + `5.0.5` | 1.391 | **Se queda.** Protocolo estricto y compacto | — | — |
| `## 5.0.4 Prohibiciones explícitas` | 1.150 (371 de tabla) | **Condensar (C6).** Siete prohibiciones, cada una con su desarrollo; el contenido es doctrina viva del trabajo, pero la forma es larga. **Se conserva el enunciado de las siete y su fuente; se recortan los desarrollos que ya se instancian en `5.1`–`5.4`** | En la propia nota | **(a)** redacción |
| `## 5.0.6 El mismo filtro, aplicado a uno mismo` + `C4 con detalle` + `C5 con detalle` + `C3 y C6` | 1.900 (612 de tabla, 30 filas) | **Condensar (C2), no suprimir.** Es la autoauditoría contra la propia rejilla C1-C7 y **es defensa oral pura** — pero hoy tiene **tres tablas y tres subapartados de detalle** para siete criterios. Propuesta: **una sola tabla C1-C7 con estado y evidencia en una línea**, y los tres subapartados `C4`/`C5`/`C3 y C6` (1.220 juntos) condensados a un párrafo cada uno o remitidos a `A.3.7`, que ya trata las mismas tres cosas | En la nota; excedente a `A.3.7` si se mantiene T7 | **(a)** redacción y unificación |
| `5.1` completo | 2.862 | **Se queda.** Es el capítulo de resultados más ajustado; `5.1.3` es sede canónica del FPR por variante tras D8 | — | — |
| `5.2.1`–`5.2.3` | 1.490 | **Se queda.** `5.2.3 Comparación de los resultados de cada algoritmo` (859) es justo la «explicación de la solución analizada» que el profesor quiere legible: **no se recorta, se revisa de estilo** | — | — |
| `5.2.4.1`–`5.2.4.3` | 861 | **Se queda.** Robustez frente a la semilla; incluye la declaración de que el titular es el punto más favorable de once corridas — honestidad que no se toca | — | — |
| **`### 5.2.4.4 La decisión de balanceo no es constante entre semillas`** | **1.515**, de las que **231 son sus dos tablas de 16 filas** | **R4 + C3.** Es **el caso más claro del carril (a) en el capítulo 5**: dos tablas de márgenes de `f1_macro` con `±` de desviación entre *folds*, más la aritmética de «*3,8 y unas 7 veces menor*», «*40 celdas*», «*0,0021 frente a 0,0079*». **La conclusión es valiosísima y se queda entera** («el eje SMOTE vs `class_weight` nunca estuvo establecido»; «SMOTE gana 40 de 40 en el otro eje»). **Lo que se va son las dos tablas** y el desarrollo numérico intermedio | Tablas → `A.3.6`; prosa condensada en la nota | **(a)** hiperparámetros |
| `5.3` completo | 3.496 | **Se queda.** Canónica de cinco solapes tras D14–D18; el bloque `El enrutado a unknown: el 13,4 %, explicado` (1.005) es el resultado central del trabajo | — | — |
| `## El sistema frente a la literatura publicada sobre NSL-KDD` (+ sus 5 subapartados) | 1.261 | **Condensar (C5).** Contenido de altísimo valor (los 7 baselines canónicos, `[74, §5.4]`, Hindy et al.) pero con **dos callouts largos de reservas** sobre una tabla de 8 filas. Propuesta: fundir `Los criterios de admisión` (143) y `La magnitud del descarte` (168) en un párrafo, y comprimir las dos reservas obligatorias a un solo callout de cuatro líneas. **Las dos reservas no se suprimen**: sin ellas la tabla miente | En la nota | (b) |
| `## Qué NO mide la latencia publicada` | 661 | **Condensar (C11).** El alcance de las columnas de tiempo ya vive en `5.0.4` (prohibición 4, canónica tras D1) y en `A.3.6`. Aquí basta la lectura para el lector del capítulo 5 | En la nota | (b) |
| `## Qué significa este FPR a prevalencia realista` | 596 | **Se queda.** Es la respuesta a la primera pregunta previsible del tribunal | — | — |
| Resto de `5.4` | 1.552 | **Se queda.** Recién recortado por D3/D12–D18 (−461); volver a pasar por ahí es riesgo de romper remisiones sin ganancia | — | — |

---

## 4. Capítulo 4 — 15.702 palabras

> [!warning] `4.2` (5.289) y `4.3` (5.688) NO se proponen por tamaño
> Son **sedes canónicas**, no duplicación: `4.3` es la sede de cuatro de los 18 solapes ya
> resueltos (D5, D6, D9, D11) y `4.2` la del *drift* y del reparto de D2. El propio informe de
> D1–D18 lo dejó escrito y este barrido lo confirma. Lo que sigue es **contenido**, no tamaño.

| Bloque | Palabras | Veredicto | Destino | Carril |
|---|---:|---|---|---|
| `4.1` completo | 706 | **Se queda.** Ya es mínimo | — | — |
| `## Algoritmos y espacios de búsqueda` de `4.4` — **la tabla de rejillas** | 70 (de 280 del apartado) | **R3 — traslado.** Es el **único resto de volcado de rejilla que queda en el cuerpo**, y crea una **asimetría con `4.5`, que ya hace lo correcto**: «*Los valores concretos de cada rejilla están en el Apéndice A.3 (§A.3.3)*». Mismo tratamiento aquí: el cuerpo dice **qué ejes se exploran y con cuántas combinaciones**, `A.3.3` da los valores | Tabla → `A.3.3` | **(a)** hiperparámetros |
| Resto de ese apartado (submuestra del OCSVM, `novelty=True`, autoencoder sin frameworks) | 210 | **Se queda.** No son hiperparámetros: son **decisiones de implementación con justificación**, exactamente lo que el profesor quiere que se explique bien | — | — |
| `## Configuraciones ganadoras` de `4.4` | 626 | **Se queda.** Ya remite a `A.3.3` («*no se reproducen aquí*») tras D10, y su callout «*El AUC-ROC de validación no es el de §5.1.2*» es una vacuna contra una lectura errónea real | — | — |
| `4.5` completo | 1.564 | **Se queda.** Ya está en el patrón correcto post-D10. El párrafo del redondeo de KNN/HGB (`0,969377` vs `0,969391`, «*artefacto de redondeo sin significado práctico*») es candidato de estilo, no de recorte: **su cifra está verificada y su ficha se cerró en `2d48cfd`** | — | — |
| `### Tamaño y reparto de los subconjuntos` de `4.2.1` | 1.530 | **Condensar (C4).** Contiene la **Figura 4.1** con la lectura de sus nueve gráficos, el desbalance 883,21:1, la tabla de dos denominadores de D2 y su callout de procedencia. **La tabla de dos denominadores NO se toca** (es la vacuna contra comparar 78,3 % con 33,1 %) ni el callout de procedencia del «17» (sede acreditativa, así lo fijó la auditoría de D4). Lo condensable es la **enumeración de conclusiones del panel**, que reitera lo que la figura ya muestra | En la nota | (b) |
| `### Desplazamiento de distribución entre entrenamiento y test (drift)` | 1.032 | **Se queda.** Sede canónica de las dos mediciones KS y de su callout de no descomposición (D7 revertido a propósito) | — | — |
| `### Valores atípicos (outliers)` | 797 | **Se queda** | — | — |
| `4.3.5` + `Qué se poda realmente` + `Decisión experimental 54 frente a 122` | 1.820 | **Se queda.** Es el experimento H1, y la lista de 17 nombres **acredita** el recuento; la auditoría de D4 ya avisó de que recortarla rompe la acreditación | — | — |
| `4.6 Conclusiones del capítulo` | 934 | **Se queda.** Recién pasado por D3/D9/D11/D18 | — | — |

---

## 5. Capítulos 6 y 1, y el solapamiento entre ambos

### 5.1 Capítulo 6 — 8.404 palabras

| Bloque | Palabras | Veredicto | Destino | Carril |
|---|---:|---|---|---|
| `## 6.1.1 Grado de cumplimiento de los objetivos` | 748 | **Condensar (C10), baja prioridad.** Re-narra los nueve objetivos de `1.3` bloque a bloque. Es **género obligatorio** en un TFG y el tribunal lo lee: el riesgo de recortarlo supera la ganancia. Si se toca, solo los incisos que reproducen argumento de `6.1.3`/`6.1.4` en lugar de remitir | En la nota | (b) |
| `## 6.1.2` + `## 6.1.3` | 861 | **Se queda.** `6.1.3` es sede canónica de las limitaciones tras D17 | — | — |
| `### 6.1.4.1 Los seis límites, uno a uno` | 1.982 | **Condensar (C1) — el mayor candidato del capítulo.** **Su contenido es el mejor material de defensa de toda la memoria y no se suprime nada.** Lo que sobra es **la plantilla**: los seis límites repiten el mismo esqueleto de cuatro epígrafes (*Razón técnica* / *Qué queda fuera* / *Qué se hizo en su lugar* / *Continuación*), y varios sub-bloques **reproducen** en lugar de remitir — el 4,8× del `tiempo_s` (canónico en `A.3.6`), el reparto de D2 (en `5.0`), el 13,4 % (en `5.3`), el «13 de 98» (en `5.2.4.3`). Propuesta: **conservar los seis límites y sus cuatro epígrafes**, sustituyendo cada cifra reproducida por su remisión | En la nota | **(a)** redacción |
| `### 6.1.4.2 Balance frente al catálogo de errores metodológicos` | 1.011, de las que **548 son la tabla P1-P10** | **La tabla se queda entera (C8 afecta solo a la prosa).** Es la pieza que un tribunal metodológico mira primero. Los párrafos de cierre y el `[!warning]` de verificación pendiente **tampoco se tocan** (el callout lo exige la regla permanente del 2026-08-14). Margen real: **463 palabras de prosa**, y es poco | En la nota | (b) |
| `6.2 Líneas futuras` completo | 3.561 | **Se queda.** Cinco refinamientos + tres peldaños + nota de aprendizaje continuo, respaldados en `EL_FUTURO.md`. Es un entregable del encargo, no relleno | — | — |

### 5.2 Capítulo 1 — 3.643 palabras, y el solape 1.x ↔ 6.x

**Resultado del barrido: el solape 1.x ↔ 6.x que se buscaba NO es el que se esperaba.** No hay
duplicación de cifras ni de conclusiones entre planteamiento y conclusiones: `6.1.1` **remite** a
`1.3` en lugar de reproducirlo, y lo hace objetivo por objetivo declarando la correspondencia. El
solape real del capítulo 1 es **con el capítulo 2**, y es de contenido:

| Bloque | Palabras | Veredicto | Destino | Carril |
|---|---:|---|---|---|
| `1.1 Motivación` | 321 | **Se queda.** Ya es mínima | — | — |
| **`1.2 Preliminares`** | **1.110** | **Condensar (C7).** Es un **relato histórico completo** —Anderson 1980 `[2]`, Denning/IDES `[3]`, Roesch/Snort 1998 `[26]`, las tres aproximaciones de detección, y cinco desafíos abiertos (evasión, volumen, FP/FN, SIEM, híbridos)— cuya **sede canónica es `2.2.2 Sistemas de detección de intrusiones`**, y la propia nota lo admite: «*se desarrollan con detalle en el capítulo 2*». **Es un apartado de introducción haciendo el trabajo del marco teórico.** Propuesta: reducir al **párrafo mínimo que motiva la propuesta híbrida** (Anderson/Denning en una frase → firmas con Snort en otra → «ninguno resuelve el problema por separado, de ahí lo híbrido»), remitiendo a `2.2.2`/`2.2.4` para el resto | En la nota, con remisión a `2.2.2` | **(a)** unificar apartados |
| `1.3 Objetivo` | 1.015 | **Se queda entera.** Objetivo general + nueve objetivos específicos con criterio de cumplimiento. Es la referencia que `6.1.1` audita; recortarla rompería esa auditoría | — | — |
| `1.0 Sinopsis` **frente a** `1.4 Estructura` | 534 + 663 = **1.197** | **Unificar (C12).** Los dos anuncian el contenido de la memoria: `1.0` resume los cuatro apartados del capítulo 1 **y ya enumera los cinco bloques de objetivos**, mientras `1.4` recorre los seis capítulos y los apéndices. **Y `1.3` enumera los nueve objetivos por tercera vez.** Propuesta: `1.0` se queda como sinopsis **breve del capítulo 1** (sin la enumeración de bloques de objetivos, que es de `1.3`), y `1.4` conserva el recorrido por capítulos, que es su función y **no se duplica en ningún otro sitio** | En las dos notas | **(a)** unificar apartados |

> [!warning] `1.4` tiene ficha propia abierta y va LA ÚLTIMA
> `features.md` lo repite en varios sitios: «**`1.4` sigue siendo LA ÚLTIMA**». Cualquier retoque de
> `1.4` debe ejecutarse **después** de que el resto de recortes esté cerrado, porque `1.4` describe
> la estructura resultante — incluida la frase sobre qué vive en el apéndice, que R1/R2 cambian.

### 5.3 Preliminares — 1.088 palabras

`Resumen.md` (565) y `Abstract.md` (523). **Se quedan.** Son obligatorios, están dentro de la
extensión habitual y el `Abstract` es la traducción del `Resumen`: la coincidencia entre ambos **no
es duplicación**. Sin acción.

---

## 6. Capítulo 3 — 6.670 palabras

> [!important] Lo que el profesor pidió aquí YA ESTÁ HECHO
> «*Los primeros apartados del Capítulo 3 no creo que sean necesarios y se podían unificar*» se
> ejecutó en la Tanda 12 (2026-08-16) y se verificó en la Tanda B (2026-08-18): `3.3.3` suprimida
> con su paso 1 trasplantado a `3.2`, capítulo renumerado, cero punteros caducados. **No se vuelve a
> proponer.**

Un único hallazgo nuevo, y **no es del carril de unificación sino del de simplificar las soluciones
analizadas**:

| Bloque | Palabras | Veredicto | Destino | Carril |
|---|---:|---|---|---|
| `### Por qué familias clásicas y no una arquitectura tabular profunda` (dentro de `3.5.2`) | 844 | **Condensar (C9).** Es **el 52 % de `3.5`** (1.617) y **el 12,7 % del capítulo entero**, dedicado a justificar una solución **que el sistema no usa**. Se apoya en `[41]` y en el análisis de 19 algoritmos sobre 176 conjuntos `[42]`, con **cinco condiciones** desarrolladas una a una. El argumento es correcto y **debe quedarse** —es respuesta directa a una pregunta previsible del tribunal—, pero cabe en **un párrafo con las cinco condiciones en una lista de una línea cada una**. **Aviso de coordinación:** su solapamiento con `2.1.4` es del alcance de otro informe; **aquí solo se propone comprimir el lado de `3.5`, sin mover nada al capítulo 2** | En la nota (o excedente a `A.3.10`, que ya aloja «algoritmos que el sistema no emplea») | **(a)** simplificar soluciones analizadas |
| Resto de `3.1`–`3.6` | 5.826 | **Se queda.** El capítulo ya está en 6.670 palabras, es el segundo más corto de la memoria, y `3.1.5 Modelo de amenaza` es la sede que `6.1.4` **consume** para acotar el alcance de los resultados | — | — |

---

## 7. Duplicaciones cruzadas nuevas (recorte de coste cero)

D1–D18 ya barrieron 4-6 y se ejecutaron. Lo que sigue es **lo que ese barrido no cubría**, porque
cruza hacia el capítulo 1, el 3 y los apéndices:

| # | Qué se cuenta dos veces | Sedes | Sede canónica propuesta | Reparación |
|---|---|---|---|---|
| **X1** | El volcado del barrido de semillas | `A.3.6` (dos tablas, 6.410) **y** `Resultados/dispersion_semillas.csv`/`.md` (versionados) | El **CSV** | R1/R2. Ampliar `A.3.9 Procedencia` con la remisión explícita. Ninguna remisión del cuerpo se rompe (§2.2, punto 3) |
| **X2** | Historia de la detección de intrusiones (Anderson, Denning, Snort, tres aproximaciones, desafíos abiertos) | `1.2` (1.110) **y** `2.2.2` | **`2.2.2`** (capítulo 2, alcance ajeno) | C7. `1.2` conserva solo el hilo que motiva lo híbrido y remite. **Coordinar con el informe de `2.2`** antes de ejecutar |
| **X3** | Rejilla de hiperparámetros de la etapa 1 | tabla de `4.4` (70) **y** `A.3.3` | **`A.3.3`** | R3. `4.4` pasa al patrón que `4.5` ya usa |
| **X4** | Márgenes de `f1_macro` del mini-experimento de balanceo | tablas de `5.2.4.4` (231), `4.3.4` **y** `metricas_balanceo.csv` | **`A.3.6`** para las tablas; `4.3.4` mantiene la decisión | R4 |
| **X5** | El alcance de las columnas de tiempo y el 4,8× | `5.0.4` prohib. 4 (canónica tras D1), `A.3.6` *Bloque de máquina* (canónica del análisis), `5.4 Qué NO mide la latencia`, `6.1.4.1` límite 2 | `5.0.4` + `A.3.6` | C11 y C1: las otras dos sedes remiten en lugar de reproducir la banda |
| **X6** | La rejilla C1-C7 y su autoauditoría | `5.0.6` (sede única declarada, 1.900) y `5.4 Los criterios de admisión` (143, **ya remite bien**) | `5.0.6` | Solo C2 (condensar la sede). **`5.4` ya es el patrón correcto y no se toca** |
| **X7** | El anuncio del contenido de la memoria | `1.0` (534), `1.4` (663) y los bloques de objetivos de `1.3` | `1.4` para capítulos, `1.3` para objetivos | C12 |
| **X8** | Marco metodológico (CRISP-DM, partición, validación cruzada, deriva) alojado en apéndice | `A.3.11` (1.909) y el capítulo 2 | **Sin decidir aquí** | Llegó por la restricción T7. **Requiere decisión de Francisco y coordinación con los informes del cap. 2**; este informe NO lo propone |

---

## 8. Material para la DEFENSA ORAL

> [!warning] RECONCILIACIÓN CON EL DISCO — 2026-08-21 (ficha F3)
> La columna «**Dónde vive tras el recorte**» de la tabla de abajo describe un estado **posterior a
> la ejecución**, y el *frontmatter* de este informe todavía dice «*ninguna nota de la memoria ha
> sido modificada*». **Las dos cosas están hoy desfasadas, en direcciones opuestas.** Estado real,
> verificado en disco el 2026-08-21:
>
> | Partida | Sede | Estado real |
> |---|---|---|
> | **R1** tabla de calidad (98 filas) | `A.3` §A.3.6 | **EJECUTADO** — el encabezado «Bloque de calidad (98 celdas)» sigue, pero su contenido es hoy un *callout* de remisión: «*Las 98 celdas NO se transcriben aquí […] `Resultados/dispersion_semillas.csv` y `.md`, ambos versionados*» |
> | **R2** tabla de máquina (100 filas) | `A.3` §A.3.6 | **EJECUTADO** — la tabla no está; se conservan la prosa en viñetas (el 4,8×, el recuento de épocas) y el *callout* de `ac496cb`, que era exactamente lo previsto en §2.2 punto 3 |
> | **R3** tabla de rejillas de la etapa 1 | `4.4` | **NO EJECUTADO** — la tabla de cuatro filas (`n_estimators`, `nu`/`gamma`, `n_neighbors`, `hidden_layer_sizes`) sigue en `## Algoritmos y espacios de búsqueda`. **La asimetría con `4.5` que denuncia el §4 sigue viva** |
> | **R4** dos tablas de márgenes de balanceo | `5.2` §5.2.4.4 | **NO EJECUTADO** — las tablas de márgenes de `f1_macro` con su `±` entre *folds* siguen en el cuerpo de `5.2.4.4` |
> | **C1–C12** condensaciones | varias | **NINGUNA EJECUTADA** que se haya podido verificar. Comprobadas una a una las dos que dejan huella inequívoca: `3.5.2 § Por qué familias clásicas…` (C9) conserva sus **cinco condiciones con tabla**, y `1.2 Preliminares` (C7) conserva el relato histórico completo |
>
> **Consecuencias que hay que leer con cuidado:**
>
> - **El −6.410 contado SÍ se materializó**, y es R1+R2. Ese titular del §1.1 es real.
> - **El +301 de «solo se muda al apéndice» NO**: R3 y R4 siguen pendientes, así que las 301 palabras
>   siguen en el cuerpo y `A.3.3`/`A.3.6` no las han recibido.
> - **El orden de ejecución del §9 se cumplió solo en su paso 1.** El paso 2 (R3/R4, «mecánicos, 301
>   palabras, cierran el carril de hiperparámetros que el profesor pidió») **está sin hacer**, y es el
>   pendiente más barato y más defendible de todo este informe.
> - **La fila «¿Los hiperparámetros son reproducibles?» de la tabla de abajo es la que más engaña
>   hoy:** dice que tras R3/R4 `A.3` es «*el único sitio de la memoria donde viven*». Aún **no** lo es
>   —`4.4` y `5.2.4.4` siguen tabulándolos—, aunque `2.1.6.4` y `4.5` sí remiten ya a `A.3` §A.3.3.
>
> **`5.2` estaba siendo editada por otro agente el 2026-08-21**, así que el estado de R4 debe
> reconfirmarse contra el disco antes de darlo por pendiente.

Todo lo que este informe retira del cuerpo **sigue existiendo**: en un CSV versionado, en el
apéndice o en `Resultados/`. Esta sección empareja cada pieza retirada con la pregunta del tribunal
que responde, para que Francisco la tenga localizada.

| Pregunta previsible del tribunal | Con qué se responde | Dónde vive tras el recorte |
|---|---|---|
| «¿Sus resultados son robustos o son producto de una sola semilla?» | El barrido de 10 semillas: `n`, media, `sd`, mín y máx **por celda**, y el recuento automatizado de **13 de 98 celdas** del titular fuera de banda | La tabla `Celdas fuera de banda` y `El titular frente a la banda` **se quedan en `A.3.6`**. El volcado completo, en `Resultados/dispersion_semillas.csv` (versionado, se puede proyectar) |
| «¿Por qué la semilla 42 y no otra?» | 42 es `SEMILLA_POR_DEFECTO` y es la de **todo lo publicado**; el barrido usa 1-10 **excluyendo la 42 a propósito**, para que sea un punto independiente **al lado** de la banda y no dentro de ella | `A.3.6 Alcance y método del barrido` (se queda) |
| «Estos tiempos, ¿son capacidad operativa del sistema?» | **No**, y está declarado: son *wall-clock* en máquina no dedicada, miden solo `predict`/`score` sobre características ya en memoria, y una misma configuración varió **4,8×** entre dos corridas con calidad idéntica al bit | Los **cuatro párrafos en viñeta y el `[!warning]` de `ac496cb`** de `A.3.6 Bloque de máquina` **se quedan** (490 palabras). Solo se retira la tabla de 100 filas, que el propio texto prohíbe citar |
| «¿Y la corrida `ac496cb`, es reproducible?» | **No**, y se declara: sus CSV nunca se commitearon y `1163c90` los sobrescribió; sobrevive citada en `Implementacion/PIPELINE.md` | `A.3.6`, callout `[!warning]` (se queda) |
| «¿La decisión de balanceo está establecida?» | **Un eje sí y el otro no**, y se dice: SMOTE vs `class_weight` **no** está establecido (17 de 40 celdas para `class_weight`, ningún par unánime, tres de los cuatro márgenes por debajo del ruido entre *folds* de la propia corrida que los produjo); SMOTE vs nada **sí** (40 de 40) | Conclusión y los dos recuentos **se quedan en `5.2.4.4`**; las **dos tablas de márgenes** pasan a `A.3.6`, donde siguen proyectables |
| «¿Por qué no usó una arquitectura profunda para datos tabulares?» | Las **cinco condiciones** de `[42]` (19 algoritmos, 176 conjuntos) se cumplen en D3, y `[41]` sitúa los árboles por delante en tabular de tamaño medio | `3.5.2`, condensado a un párrafo + lista. El desarrollo largo, si se quiere conservar literal, cabe en `A.3.10` |
| «¿Se compara con la literatura?» | Los **siete baselines canónicos** de `[23]` sobre KDDTest+ frente al **86,05 %** propio, con sus **dos reservas obligatorias** (granularidad de etiqueta no declarada en el artículo original; presupuesto de datos distinto) y con el **NSL-KDD apareciendo solo 3 veces** en congresos de primer nivel 2020-2023 `[74, §5.4]` | `5.4`, condensado. **Las dos reservas y la tabla se quedan** |
| «¿Cumple los estándares metodológicos del área?» | **8 de los 10** errores de `[18]` cubiertos, y **P9/P10 «cubiertos hasta donde el dataset permite»**, con la razón técnica escrita | `6.1.4.2`, **tabla P1-P10 intacta** |
| «¿Qué no pudo medir, y por qué no fue falta de tiempo?» | Los **seis límites** de `6.1.4.1`: sin marca de tiempo, sin despliegue, sin adversario adaptativo, una sola semilla (resuelto con el barrido), umbral cerrado frente al riesgo de espacio abierto, y qué es exactamente un «0-day» del NSL-KDD | `6.1.4.1`, condensado **sin perder ninguno de los seis ni sus cuatro epígrafes** |
| «¿Se auditó a sí mismo con el filtro que aplica a los demás?» | Sí: la rejilla C1-C7 aplicada al propio trabajo, con **dos criterios que NO cumplía (C3 y C6) y se corrigieron** | `5.0.6`, condensado a una tabla de estado + evidencia. **El «no cumplía, corregido» no se suaviza** |
| «¿Los hiperparámetros son reproducibles?» | Rejillas, configuraciones ganadoras, umbrales y *checklist* de reproducibilidad | `A.3.1`–`A.3.3` y `A.3.8`, **intactos**, y tras R3/R4 son el **único** sitio de la memoria donde viven — que es lo que el profesor pidió |

> [!note] Lo que NO conviene retirar aunque sea largo
> Cinco bloques largos son **precisamente** el material que distingue este TFG y ninguno se propone
> para supresión: `A.3.7 Limitaciones declaradas` (1.278), la tabla P1-P10 de `6.1.4.2` (548), los
> seis límites de `6.1.4.1` (1.982, solo condensación), `6.2 Líneas futuras` (3.561) y
> `5.3 El enrutado a unknown: el 13,4 %, explicado` (1.005).

---

## 9. Orden recomendado de ejecución

1. **R1 y R2** (`A.3.6`). Es el **−6.410** entero, es supresión mecánica de dos tablas, **no toca
   ninguna nota del cuerpo** y no puede romper nada. Antes: añadir la remisión al CSV en
   `A.3.9 Procedencia` y verificar con `grep` que sigue habiendo cero citas a filas individuales.
2. **R3 y R4** (traslados a `A.3.3` y `A.3.6`). Mecánicos, 301 palabras; cierran el carril de
   hiperparámetros que el profesor pidió.
3. **C1, C2, C3, C6, C9** — el carril **(a)** de redacción. Son los que se le pueden enseñar al
   profesor como respuesta directa a su revisión.
4. **C4, C5, C8, C10, C11** — carril **(b)**. Solo si Francisco quiere más volumen.
5. **C7** (`1.2`) — **coordinar antes con el informe de `2.2`**, porque su sede canónica está allí.
6. **C12** (`1.0` / `1.4`) — **LA ÚLTIMA**, por la ficha abierta de `1.4`.
7. **Recontar con `wc -w`** al terminar y publicar los porcentajes **contra las bases de este
   informe**, nunca antes.

---

## Fuentes de este informe

- Conteos: `wc -w` y `wc -l` sobre disco, 2026-08-20, sobre `00 Preliminares/`, `01 Introducción/`,
  `03 Diseño del sistema/`, `04 Implementación del sistema/`, `05 Evaluación/`, `06 Conclusiones/`
  y `Apéndices/`; desglose por encabezado calculado sección a sección.
- `git ls-files Resultados` y `wc -l Resultados/dispersion_semillas.csv` para verificar que el
  artefacto que sustituye a R1/R2 está versionado y contiene las 198 filas de datos.
- `grep` sobre todo el vault para verificar las remisiones a `A.3.6`, «Bloque de calidad»,
  «Bloque de máquina» y «13 de 98».
- `features.md` (solo lectura) para el estado del capítulo 3 y de la ficha de `1.4`.
- `99 Investigación/Datos repetidos en los capítulos 4-6.md` para no repetir D1–D18.
- `mis-apuntes-del-informe.md` para la cita literal del profesor.
