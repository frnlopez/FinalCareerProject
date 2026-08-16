---
titulo: "Auditoría de las 10 entradas de Bibliografía.md: cita completa, verificación y nivel de fiabilidad"
numero: "-"
estado: informe
docx_ref: "-"
---

# Auditoría de las 10 entradas de `Bibliografía.md`

- **Encargo:** T15 · B1 — cerrar la auditoría de `Bibliografía.md`. Completar `[2]` (Anderson) y
  `[8]` (Stallings) con año y editorial; **fundir `[9]` en `[8]`** y retirarla de la numeración;
  **sustituir `[1]`** (prensa sectorial) por fuente de nivel 1-2 pública (ENISA, INCIBE o
  CCN-CERT); pasar `Bibliografía.md` a **tabla de *staging*** con cita completa, DOI/URL estable y
  **nivel de fiabilidad** por entrada; verificar de paso los metadatos de las demás entradas.
- **Fecha:** 2026-08-09
- **Alcance:** las **10 entradas existentes** y solo ellas. **Queda fuera** el volcado de fuentes
  nuevas de los cuatro informes de `99 Investigación/` (eso es **T16**, y va *después* de la
  redacción T8-T13). Queda fuera toda edición de notas de la memoria: las correcciones que las
  tocan se **proponen**, no se ejecutan.
- **Alimenta a:** [[Bibliografía]] (entregable principal) y al pase final a Zotero/IEEE, que hace
  Francisco a mano.

## Respuesta corta

Las 10 entradas quedan con cita completa y nivel asignado. **Ocho son nivel 1**, una es **nivel 2
declarado** (`[2]`, informe técnico de empresa: el Anderson de 1980, fuente primaria histórica
alojada por el NIST) y una era **nivel 3** y ha desaparecido: `[9]` era una copia no autorizada del
mismo libro que `[8]` y, además, hoy ya ni siquiera resuelve en abierto. `[1]` pasa de prensa
sectorial a la **nota de prensa oficial de INCIBE** sobre el *Balance de ciberseguridad 2024*, con
dato exacto: **97.348 incidentes gestionados, +16,6 % sobre 2023**. Quedan tres cosas que **no
puede tocar el researcher** y que hay que arreglar en las notas: repuntar `[9]`→`[8]`, reformular
la frase de `1.1` que nombra empresas concretas (INCIBE da magnitud, no nombres) y repuntar dos
citas de `2.1.2` que atribuyen a Goodfellow unas listas que son de Géron.

## Hallazgos

### 1. `[2]` Anderson 1980 — completada y verificada contra la portada

Portada leída directamente (PDF alojado por NIST CSRC): **James P. Anderson Co., Box 42, Fort
Washington, Pa. 19034**, *Computer Security Threat Monitoring and Surveillance*, **contrato
79F296400**, **26 de febrero de 1980**, **revisado el 15 de abril de 1980**. Índice de 6 capítulos,
53+ páginas. ([PDF en csrc.nist.gov](http://csrc.nist.gov/publications/history/ande80.pdf),
1980) — **nivel 2**

Es un **informe técnico de empresa**, no una publicación revisada por pares: por la tabla de
fiabilidad es nivel 2, y así se declara. La reserva se compensa con dos hechos: es la **fuente
primaria** (no una glosa) y la copia está alojada por un **organismo oficial**, lo que garantiza su
integridad.

**Matiz que sí afecta a una afirmación del trabajo:** `1.2 Preliminares:14` dice que «este informe
se considera el punto de partida para los IDS». Eso es una afirmación *sobre* el informe y el
informe no la puede sostener; necesita un aval externo de nivel 1 (una revisión del área). No se
ha ejecutado nada: es texto de la memoria.

### 2. `[8]` Stallings — completada, con la edición aún por confirmar

La entrada era literalmente `"Computer Security : Principles and Practice" William Stallings`: sin
coautor, sin año, sin editorial. Verificado:

- **Coautor omitido: Lawrie Brown.** El libro es de Stallings **y** Brown.
- **4.ª ed., Pearson, 2018, ISBN 978-0-13-479410-5** (registro de editor/distribuidor).
- **5.ª ed., Pearson, publicada el 28-07-2023, ISBN impreso 978-0-13-809167-5**, e-book
  978-0-13-809171-2 ([Pearson](https://www.pearson.com/en-us/subject-catalog/p/computer-security-principles-and-practice/P200000010333/9780138091712),
  2023) — **nivel 1**
- 3.ª ed., Pearson, 2014, ISBN 978-0-13-377392-7 (por si la copia usada fuese esa).

Se ha fijado la **4.ª ed.** como cita por defecto, por ser la más difundida, **y se ha marcado en
`Bibliografía.md` que la edición está sin confirmar**. La definición citada en `2.2.1` (la de
*computer security* tomada del NIST, con el inciso «hardware, software, firmware, información/datos
y telecomunicaciones») aparece en el capítulo 1 de **todas** las ediciones, así que el texto de la
memoria no permite deducir cuál se usó. **Lo confirma Francisco mirando el ejemplar que tiene.**

### 3. `[9]` — fundida en `[8]` y retirada, sin renumerar

`[9]` era `students.aiu.edu/.../j5V2a3_Computer_Security_Principles.pdf`: **copia del mismo libro
de Stallings** alojada en un dominio de terceros, sin garantía de integridad → **nivel 3**.
Comprobado el 2026-08-09: el enlace **redirige a `aiu.edu/securelogin.html`**, es decir, ni siquiera
es ya una URL pública; por eso tampoco se ha podido determinar de qué edición era la copia.

**Cómo se ha ejecutado la baja, y por qué así:** la entrada se retira y **su número queda vacante,
sin reutilizar y sin renumerar el resto**. Renumerar habría obligado a mover `[10]` → `[9]` y a
editar `2.2.1:40`, y el encargo prohíbe expresamente tocar notas del vault fuera de
`Bibliografía.md`; renumerar sin editar las notas habría dejado dos referencias apuntando a fuentes
equivocadas, que es peor que un hueco. El hueco lo absorbe el pase a Zotero, que renumera solo.

> [!warning] Acción que queda abierta en la memoria
> `2.2.1 Introducción a la ciberseguridad.md:32` sigue citando `[9]` (frase de la autenticidad y la
> responsabilidad). Hay que **repuntarla a `[8]`** — mismo libro, mismo capítulo. La hace el
> `redactor-tfg` o Francisco.

### 4. `[1]` — sustituida por INCIBE, con el dato exacto

La entrada anterior (`channelpartner.es`, prensa sectorial) era **nivel 3** sosteniendo una
afirmación cuantitativa del capítulo 1: por la regla dura, no sostenía nada. Sustituida por:

> Instituto Nacional de Ciberseguridad (INCIBE), «INCIBE presenta su balance de ciberseguridad 2024
> con más de 97.000 incidentes gestionados», nota de prensa, **20 de marzo de 2025**.
> ([incibe.es](https://www.incibe.es/incibe/sala-de-prensa/incibe-presenta-su-balance-de-ciberseguridad-2024-con-mas-de-97000-incidentes),
> 2025-03-20) — **nivel 1** (organismo oficial, público y sin muro de pago)

Datos verificados en la propia nota: **97.348 incidentes gestionados en 2024** (+16,6 % sobre
2023); **65.808 (67,6 %) a la ciudadanía** y **31.540 (32,4 %) a empresas**, pymes, micropymes y
autónomos; **42.136 casos de *malware***, de ellos **357 de *ransomware***; más de 38.000 de fraude
en línea (43,2 % del total), con **21.571 de phishing**; **7.470 intrusiones o intentos de acceso
no autorizado**; **183.851 sistemas vulnerables relevantes** notificados.

Se ha elegido INCIBE sobre ENISA por dos razones: la afirmación de `1.1` es **sobre España**, y la
nota de INCIBE es de acceso libre y da la cifra en una línea citable, sin necesidad de un informe de
100 páginas.

> [!warning] Lo que esta fuente NO sostiene
> `1.1 Motivación:12` nombra **Santander, Telefónica, Iberdrola y la Universidad Complutense**.
> INCIBE publica agregados: **no nombra víctimas**. Con `[1]` sustituida, esa frase queda **sin
> respaldo**. Dos salidas, y **la elige Francisco**: (a) reformular hacia la cifra agregada —«en
> 2024 INCIBE gestionó 97.348 incidentes, un 16,6 % más que el año anterior; el 32,4 % afectó a
> empresas»—, que es lo que recomiendo porque es más fuerte que una lista de nombres; o (b)
> conservar los nombres, y entonces **cada uno necesita su propia fuente** (comunicado de la
> empresa, resolución de la AEPD), lo que son cuatro entradas nuevas y queda **fuera del alcance de
> T15**.

### 5. Las otras seis entradas: metadatos verificados y nivel asignado

| `[n]` | Estado | Nivel |
|---|---|---|
| [3] Denning 1987 | **Correcta tal cual.** DOI resuelto y comprobado vía Crossref: *IEEE Trans. Software Eng.*, vol. **SE-13**, n.º **2**, pp. **222-232**, 1987, DOI `10.1109/TSE.1987.232894`. Añadido el DOI, que faltaba | 1 |
| [4] Chio y Freeman | Título oficial ***Machine Learning and Security*** (la entrada usaba «&»). O'Reilly Media, **13-03-2018**, 383 pp., **ISBN 978-1-4919-7990-7**. Sin DOI | 1 |
| [5] Géron | 2.ª ed., O'Reilly Media, **2019**, **ISBN 978-1-492-03264-9**. Correcta; añadido ISBN | 1 |
| [6] Goodfellow, Bengio y Courville | MIT Press, **2016**, **ISBN 978-0-262-03561-3**. Correcta; añadido ISBN. **Pero ver el aviso de atribución de abajo** | 1 |
| [7] Murphy | MIT Press, **2012**, **ISBN 978-0-262-01802-9**. Correcta; añadido ISBN | 1 |
| [10] CCN-STIC-401 | Emisor oficial (Centro Criptológico Nacional), guía **CCN-STIC-401 «Glosario y Abreviaturas»**, entrada «ciberseguridad». Nivel 1 por emisor | 1 |

### 6. Hallazgo de paso: `[6]` sostiene en `2.1.2` algo que es de `[5]`

`2.1.2 Tipos de ML.md:30` y `:64` citan a **Goodfellow et al.** al pie de dos listas de algoritmos:
k-NN, regresión lineal, regresión logística, SVM, árboles y *random forests*, redes neuronales; y
K-Means, DBSCAN, HCA, One-class SVM, Isolation Forest, PCA, Kernel PCA, LLE, t-SNE, Apriori,
**Eclat**. Son las listas del **capítulo 1 de Géron `[5]`**: *Deep Learning* no trata Apriori, ni
Eclat, ni Isolation Forest. La cita está **apuntando al libro equivocado**.

No es una baja de bibliografía —`[6]` se usa bien en otros sitios y se queda— sino un **puntero mal
puesto en una nota de la memoria**. Propuesta: repuntar esas dos a `[5]`.

> [!success] EJECUTADO — verificado contra disco el 2026-08-16
> `2.1.2 Tipos de ML.md:30` y `:64` **ya citan `[5]`**. El repunte está hecho desde la Tanda 9
> (2026-08-15). Esta línea decía «Propuesta, no ejecutada»: era texto caducado, y es la corrección
> que **T25** encargaba sobre este fichero.
> **Y `[6]` tampoco quedó huérfana:** T24 la reancló el 2026-08-15 (`296de24`) en `2.1.4.3` con
> `[6, cap. 6]`, **7 ocurrencias en disco**.

### 7. Cambio de formato: `Bibliografía.md` es ya una tabla de *staging*

Cinco columnas: `[n]` · cita completa en estilo IEEE · **DOI o URL estable** · **nivel** ·
**dónde se usa**. La última no estaba en el encargo y se ha añadido porque hace mecánico el control
de la regla de T16 («ninguna entrada sin cita en el texto») y documenta que, en efecto, **las 10
están en uso**. Bajo la tabla van los **avisos por entrada** en callouts, con la reserva o la acción
pendiente de cada una.

## Lo que no he podido confirmar

- **La edición de Stallings que usó Francisco.** El texto citado es idéntico en las ediciones 3.ª,
  4.ª y 5.ª, y la copia de `[9]` que habría permitido comprobarlo ya no es accesible en abierto. Se
  cita la 4.ª ed. con la marca de «edición sin confirmar». **Sostiene la definición de *computer
  security* de `2.2.1`, así que conviene cerrarlo antes del pase a Zotero** — pero el riesgo es
  cosmético: cambia el año de la referencia, no la afirmación.
- **La versión y la fecha de la guía CCN-STIC-401**, y la transcripción literal de su entrada
  «ciberseguridad». `ccn-cert.cni.es` responde **403/503 a todo acceso automático** (test anti-bot
  «Voight-Kampff»), y lo mismo el espejo docente de la UPM (`dit.upm.es/~pepe/401/`). La búsqueda
  web sí devuelve la frase «asegurar, en la medida de lo posible, las redes y sistemas que
  constituyen el ciberespacio» **atribuida a CCN-STIC 401**, lo que corrobora la procedencia, pero
  **no es verificación de primera mano**. No es muro de pago ni falta de acceso institucional: es
  filtrado de bots, y **Francisco puede abrirlo a mano en su navegador en diez segundos**.
- **De qué edición era la copia de `[9]`**: el enlace exige registro desde 2026-08-09 (302 a
  `securelogin.html`). Irrelevante una vez retirada.
- **La cifra que sostenía la `[1]` antigua** no se ha intentado rescatar: la fuente era nivel 3 y la
  regla la deja fuera con independencia de si el número era correcto.

## Bajas y correcciones que PROPONGO (no ejecutadas)

Ninguna de estas la puede hacer el `researcher`: todas tocan notas de la memoria.

| # | Dónde | Qué propongo | Por qué |
|---|---|---|---|
| P1 | `2.2.1 Introducción a la ciberseguridad.md:32` | Repuntar `[9]` → `[8]` | `[9]` retirada; es el mismo libro |
| P2 | `1.1 Motivación.md:12` | Reformular hacia la cifra agregada de INCIBE, o dar fuente propia a cada empresa nombrada | INCIBE no nombra víctimas: hoy la frase quedaría sin respaldo |
| P3 | `2.1.2 Tipos de ML.md:30` y `:64` | Repuntar `[6]` → `[5]` | Las listas son del cap. 1 de Géron, no de *Deep Learning* |
| P4 | `1.2 Preliminares.md:14` | Añadir aval de nivel 1 a «se considera el punto de partida para los IDS» | Es una afirmación *sobre* el informe; el informe no la sostiene |
| P5 | `Bibliografía.md` `[8]` | Confirmar edición y, si procede, cambiar 4.ª ed. 2018 por la que corresponda | Único dato de la tabla que sigue marcado como sin confirmar |
| P6 | `Bibliografía.md` `[10]` | Sustituir el enlace profundo al término por la referencia a la guía completa con su versión | El *deep link* con `?n=189.html` es frágil |

**Ninguna baja adicional propuesta.** Las tres autorizadas el 2026-08-06 (fundir `[9]`, sustituir
`[1]`, completar `[2]` y `[8]`) están ejecutadas y no hay ninguna otra entrada que caiga por debajo
del nivel exigido.

## Fuentes

| # | Fuente | Nivel | Fecha | Cita completa | URL / DOI |
|---|---|---|---|---|---|
| 1 | Anderson, informe original (portada leída) | 2 | 1980-02-26, rev. 1980-04-15 | J. P. Anderson, *Computer Security Threat Monitoring and Surveillance*, James P. Anderson Co., Fort Washington PA, contrato 79F296400 | http://csrc.nist.gov/publications/history/ande80.pdf |
| 2 | INCIBE, nota de prensa del balance 2024 | 1 | 2025-03-20 | INCIBE, «INCIBE presenta su balance de ciberseguridad 2024 con más de 97.000 incidentes gestionados» | https://www.incibe.es/incibe/sala-de-prensa/incibe-presenta-su-balance-de-ciberseguridad-2024-con-mas-de-97000-incidentes |
| 3 | Registro Crossref del DOI de Denning | 1 | 1987 | D. E. Denning, «An Intrusion-Detection Model», *IEEE Trans. Softw. Eng.*, SE-13(2), 222-232 | 10.1109/TSE.1987.232894 |
| 4 | Ficha de editor de la 5.ª ed. de Stallings y Brown | 1 | 2023-07-28 | W. Stallings, L. Brown, *Computer Security: Principles and Practice*, 5.ª ed., Pearson, ISBN 978-0-13-809167-5 | https://www.pearson.com/en-us/subject-catalog/p/computer-security-principles-and-practice/P200000010333/9780138091712 |
| 5 | Registros de distribuidor de la 4.ª y 3.ª ed. de Stallings y Brown | 2 | 2018 / 2014 | ISBN 978-0-13-479410-5 (4.ª, 2018) e ISBN 978-0-13-377392-7 (3.ª, 2014) | AbeBooks / Goodreads (registros de catálogo) |
| 6 | Catálogo de O'Reilly y registros ISBN de Chio y Freeman | 1 | 2018-03-13 | C. Chio, D. Freeman, *Machine Learning and Security*, O'Reilly, 383 pp., ISBN 978-1-4919-7990-7 | https://mlsec.net/ |
| 7 | Catálogo de O'Reilly, Géron 2.ª ed. | 1 | 2019 | A. Géron, *Hands-On Machine Learning…*, 2.ª ed., O'Reilly, ISBN 978-1-492-03264-9 | https://www.oreilly.com/library/view/hands-on-machine-learning/9781492032632/ |
| 8 | Registros de MIT Press / ACM DL para Goodfellow y Murphy | 1 | 2016 / 2012 | ISBN 978-0-262-03561-3 y 978-0-262-01802-9 | https://www.deeplearningbook.org/ · https://dl.acm.org/doi/book/10.5555/2380985 |
| 9 | Comunicado del CCN sobre la guía 401 (1.069 términos) y frase de la entrada «ciberseguridad» localizada en búsqueda | 1 (emisor) / **sin verificación de primera mano** | s/f | CCN, *Guía CCN-STIC-401: Glosario y Abreviaturas* | https://www.ccn-cert.cni.es/es/pdf/guias/glosario-de-terminos |

> [!note] Sobre el uso de herramientas
> `WebFetch` primero en todos los casos. **Playwright solo en `ccn-cert.cni.es`,
> `dit.upm.es` y `web.archive.org`**, y solo después de que `WebFetch` devolviera 403: motivo,
> comprobar si el bloqueo era del cliente HTTP o del sitio. Resultó ser del sitio (test anti-bot y
> 503), así que **no se pudo leer igualmente**. No se inició sesión en ningún sitio, no se sorteó
> ningún muro y el navegador quedó cerrado.

## Cambios en Bibliografía.md

Se han tocado **las 10 entradas** (formato nuevo). Más de tres, como pide el protocolo, así que se
detalla una por una.

| `[n]` | Qué he hecho |
|---|---|
| [1] | **Sustituida** (baja autorizada): prensa sectorial nivel 3 → nota de prensa de INCIBE, nivel 1, con el dato exacto. Aviso sobre lo que la fuente no sostiene |
| [2] | **Completada**: editorial y dirección, contrato 79F296400, fecha y revisión de 1980, URL del NIST. Marcada **nivel 2** con su reserva |
| [3] | **Completada**: añadido el DOI verificado. Sin otros cambios |
| [4] | **Completada**: título oficial, edición, ciudad, año, páginas, ISBN |
| [5] | **Completada**: subtítulo, ciudad, ISBN |
| [6] | **Completada**: ciudad, ISBN. **Marcada** por posible atribución equivocada en `2.1.2` (propuesta P3) |
| [7] | **Completada**: ciudad, ISBN |
| [8] | **Completada**: coautor Brown, edición, editorial, año, ISBN. **Marcada**: edición sin confirmar, con los ISBN de la 5.ª ed. a mano |
| [9] | **Retirada de la numeración y fundida en [8]** (baja autorizada). Número **no reutilizado**, sin renumerar. Deja la acción P1 abierta en `2.2.1` |
| [10] | **Completada**: emisor, título y código de la guía, término citado. **Marcada**: versión/fecha sin verificar y URL frágil |
| — | **Cambio de formato**: el fichero pasa a **tabla de *staging*** (cita · DOI/URL · nivel · uso) con bloque de avisos |

## Implicaciones para el proyecto

- **La regla dura queda satisfecha:** ninguna afirmación de la memoria se apoya ya en una fuente de
  nivel 3. La única de nivel 2 es `[2]`, declarada, y es la fuente primaria del hecho histórico que
  sostiene.
- **T15 no puede cerrarse del todo sin el `redactor-tfg`.** Las propuestas **P1** (repuntar `[9]`) y
  **P2** (reformular `1.1`) son consecuencia directa de las bajas autorizadas: mientras no se
  apliquen, `2.2.1` cita un número retirado y `1.1` nombra empresas que su fuente no menciona. Son
  dos ediciones pequeñas y encajan de forma natural en **T8** (capítulo 2) y en la revisión del
  capítulo 1.
- **T16 se apoya en el formato nuevo:** la columna «Dónde se usa» convierte la regla «ninguna
  entrada sin cita en el texto» en algo comprobable de un vistazo. Al volcar las ≈25-30 fuentes de
  los cuatro informes, **la columna se rellena o la entrada no entra**.
- **No contradice ninguna decisión de `resumen-de-decisiones.md`.** Esta auditoría no toca diseño
  experimental: solo procedencia de citas.
- **Coste para Francisco antes del pase a Zotero:** dos comprobaciones manuales de un minuto —la
  edición de Stallings que tiene en la mano y la versión de la CCN-STIC-401 abierta en su
  navegador—, más decidir P2.
