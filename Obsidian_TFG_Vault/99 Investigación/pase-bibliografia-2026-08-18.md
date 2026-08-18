---
titulo: "Pase en serie de bibliografía del 2026-08-18: Roesch, Anderson, Stallings, CCN-STIC-401 y el desdoble de [76]"
numero: "-"
estado: informe
docx_ref: "-"
---

# Pase en serie de bibliografía del 2026-08-18

- **Encargo:** nueve puntos cerrados — P4 (anclar Roesch/Snort en `1.2:27`), P4-bis (deshacer o
  reetiquetar lo que la Tanda 25 puso sobre Anderson en `1.2:14`), P5 (edición de Stallings `[8]`),
  P6 (deep link de CCN-STIC-401 `[10]`), desdoble de `[76]` a Storkey, cuatro declaraciones
  caducadas del rango en `Bibliografía.md`, corrección (6) de «Dónde se usa» de `[2]` y `[3]`,
  verificación de «37 muestras en D2» y ejecución o descarte de **T16**.
- **Fecha:** 2026-08-18
- **Alcance:** entra `Bibliografía.md`, el pasaje `1.2:14`/`1.2:27` y dos informes de
  `99 Investigación/`. **Queda fuera**, y no se ha tocado: `[54]` Molnar, el resto del capítulo 1,
  `features.md` (solo lectura) y cualquier prosa nueva.
- **Alimenta a:** [[Bibliografía]], [[1.2 Preliminares]], [[benchmark-comparativo-nsl-kdd]],
  [[clasificadores-tabulares-y-arquitecturas-hibridas]]

## Respuesta corta

**El pase cierra los nueve puntos sin dar de alta ni un número nuevo: el primer libre sigue siendo
el `[78]`.** Roesch ya existía como `[26]` y se ha **mapeado**, no duplicado. La atribución
historiográfica a Anderson **se ha deshecho** porque el aval de nivel 1 no existe en abierto y no se
cita a ciegas. La edición de Stallings y la versión de la guía del CCN **se MARCAN**, no se eligen.
`[76]` **no se desdobla** —repuntar el marcador de `5.1` no es mano del `researcher`—, pero su
capítulo queda con página verificada (**pp. 3-28**). El «37 en D2» estaba **mal etiquetado**: son 37
u2r **de tipo conocido**, de los 200 que hay en D2.

## Hallazgos

### P4 — Roesch/Snort: la entrada ya estaba, y el riesgo era duplicarla
`Bibliografía.md` **ya tenía** `[26]` = M. Roesch, «Snort — Lightweight Intrusion Detection for
Networks», LISA'99, USENIX, pp. 229-238, usada por `2.2.2`. El pasaje de `1.2` (hoy línea 32) se ha
anclado a **`[26]`**. Dar de alta un `[78]` habría duplicado una referencia existente, que es
exactamente lo que el aviso de T16 advierte para Anderson y Denning.
**Reserva declarada:** la URL de USENIX devuelve **403** a todo acceso automático (PDF e índice,
comprobado hoy); los metadatos se conservan de la reconstrucción previa y **no se han reinventado**.
**Fecha:** la nota dice «1998» (publicación de la herramienta) y el artículo es de **1999**; ambas
son correctas y la nota lo explica en un callout, sin reescribir la prosa.

### P4-bis — la atribución a Anderson no se sostenía y se ha retirado
`1.2:14` afirmaba, con `[2]` y un `[CITA: …]`, que «la literatura del área lo señala de forma
recurrente como el punto de partida de la detección de intrusiones». Es una afirmación **sobre** el
informe de Anderson, y `[2]` —informe técnico de empresa, **nivel 2**— no puede sostenerla sobre sí
mismo. Se buscó el aval:

- **Khraisat *et al.* 2019 `[31]`** (*Cybersecurity*, nivel 1): **no menciona a Anderson**.
  Verificado sobre el PDF del editor alojado por la Deutsche Nationalbibliothek
  ([d-nb.info/1201309239/34](https://d-nb.info/1201309239/34), 2019) — nivel 1.
- **J. R. Yost, «The March of IDES: Early History of Intrusion-Detection Expert Systems»**, *IEEE
  Annals of the History of Computing*, vol. 38, n.º 4, pp. 42-54, 2016,
  [DOI 10.1109/MAHC.2015.41](https://doi.org/10.1109/MAHC.2015.41) — metadatos **verificados en
  Crossref**, nivel 1. Es el candidato historiográfico idóneo, **pero está tras muro de pago** y su
  resumen habla de IDES, no de Anderson: **no se puede confirmar que haga la atribución explícita**.
  Project MUSE e IEEE Xplore bloquean el texto.

Sin aval, se aplica la regla dura: **la afirmación sale del cuerpo**. `[2]` queda anclado a lo que el
informe dice. Queda documentado en la nota y en la fila de `[2]`.

### P5 — la edición de Stallings NO se establece
Coexisten la **4.ª ed.** (Pearson, 2018, ISBN 978-0-13-479410-5) y la **5.ª** (Pearson, 2023, ISBN
978-0-13-809167-5). Los tres usos de `2.2.1` viven en el **cap. 1, §1.1**, sección presente en
**todas** las ediciones, así que el texto **no discrimina**, y la única copia consultable era la de
`[9]`, retirada e inaccesible. Se marca **⚠️ EDICIÓN NO ESTABLECIDA** y se declara explícitamente
que **no se elige la 4.ª «por ser la más difundida»**: eso sería inventar un dato bibliográfico.

### P6 — deep link del CCN: mejorado y marcado
El enlace apuntaba al **término suelto** dentro del visor HTML
(`…401-glosario_abreviaturas/index.html?n=189.html`), que es frágil. Se ha sustituido por **la ficha
oficial de la guía**:
`https://www.ccn-cert.cni.es/es/series-ccn-stic/guias/glosario-de-terminos.html`.
**No se ha podido verificar en línea, y se marca:** `WebFetch` da **403**; el navegador real da
**403 contra un test anti-bot «Voight-Kampff»**, y la ruta `/es/pdf/guias/…` da **503**. **No se ha
inventado ninguna URL de descarga del PDF.** **Versión y fecha siguen sin fijar** (un comunicado del
CCN-CERT habla de 1.069 términos, dato de segunda mano y sin verificar).

### Desdoble de `[76]` — decidido que NO, con la alternativa ejecutada
`[76]` es el volumen editado; el uso de `5.1:86` es la taxonomía del **cap. 1, de A. Storkey**. En
IEEE, un capítulo de obra colectiva se cita por el autor del capítulo, así que el desdoble sería lo
canónico — **pero exige repuntar el marcador de `5.1:86` de `[76]` a `[78]`, y editar un `[n]`
dentro de una nota de la memoria está fuera de la mano del `researcher`**; además dejaría `[76]`
huérfana, que es justo lo que prohíbe la regla dura de T16. Se ejecuta la alternativa equivalente:
**la fila lleva ya los datos completos del capítulo**, de modo que el pase a Zotero no dependa de
ninguna búsqueda:

> A. Storkey, «When Training and Test Sets Are Different: Characterizing Learning Transfer», cap. 1,
> en *Dataset Shift in Machine Learning*, J. Quiñonero-Candela, M. Sugiyama, A. Schwaighofer y
> N. D. Lawrence, Eds. Cambridge, MA: MIT Press, 2009, **pp. 3-28**.

Verificado contra el **registro institucional del autor** (University of Edinburgh Research
Explorer) y coincidente con MIT Press Scholarship Online — nivel 1. Con ello **la página deja de
estar sin establecer a nivel de capítulo**.

### «37 muestras en D2» — el número es bueno, la etiqueta no
Verificado contra `Resultados/`:

| Dato | Valor | Fuente en disco |
|---|---|---|
| u2r **de tipo conocido** en D2 (los que llegan a firmas) | **37** | `metricas_firmas.csv`, `soporte_u2r`, alcance «ataques de D2 de tipo conocido» (9.083 flujos) |
| u2r **0-day** en D2 | **163** | `specialized_nsl_kdd_validation_report.txt`: `httptunnel` 133, `ps` 15, `xterm` 13, `sqlattack` 2 |
| u2r **totales en D2** | **200** | suma de los dos anteriores |
| u2r en **D3** | **52** | `specialized_nsl_kdd_composicion_d3.csv` |

Los dos informes decían «37 muestras en D2» / «37 muestras en el test», que se lee como los 200.
**Corregidos ambos**, con la razón escrita: 37 es el denominador del `f1_u2r`; 200, el del recall
0-day.

### T16 — satisfecha por agotamiento, no ejecutada como volcado
La ficha (`features.md`, solo lectura) manda volcar las ≈40 fuentes de los cuatro informes **con la
regla dura «ninguna entrada sin cita en el texto»**. Contado hoy contra disco: **no queda ni un
`[CITA: …]` vivo en la memoria** —el último era el de `1.2:14`, retirado en este pase; los restantes
en disco son prosa sobre la convención o texto de informes—. Luego **no hay ninguna fuente citada en
el texto que siga sin entrada**, y volcar las no citadas es justo lo que esa ficha prohíbe.
**No se ha tocado `features.md`**: la casilla la cierra el `cronista`.

## Lo que no he podido confirmar

- **Que alguna revisión de nivel 1 atribuya explícitamente a Anderson (1980) el origen de los IDS.**
  Khraisat 2019 no lo menciona; Yost 2016 está tras muro de pago. La frase se ha retirado.
- **La edición de Stallings `[8]`.** El texto no discrimina. Decide Francisco, con el libro delante.
- **Versión, fecha y URL del PDF de la guía CCN-STIC-401 `[10]`.** El dominio bloquea incluso
  navegador real.
- **La página exacta dentro del cap. 1 de `[76]`.** El rango (3-28) sí; el punto exacto no: MIT
  Press devuelve 403.
- **Los metadatos de `[26]` contra la fuente viva.** USENIX da 403; se conservan los previos.

## Fuentes

| # | Fuente | Nivel | Fecha | Cita completa | URL / DOI |
|---|---|---|---|---|---|
| 1 | Khraisat *et al.*, *Survey of intrusion detection systems* (PDF del editor) | 1 | 2019 | A. Khraisat, I. Gondal, P. Vamplew y J. Kamruzzaman, *Cybersecurity*, vol. 2, art. 20 | https://d-nb.info/1201309239/34 · 10.1186/s42400-019-0038-7 |
| 2 | Registro Crossref de «The March of IDES» | 1 | 2016 | J. R. Yost, *IEEE Annals of the History of Computing*, vol. 38, n.º 4, pp. 42-54 | 10.1109/MAHC.2015.41 |
| 3 | University of Edinburgh Research Explorer — capítulo de Storkey | 1 | 2008/2009 | A. Storkey, cap. 1 de *Dataset Shift in Machine Learning*, pp. 3-28 | https://www.research.ed.ac.uk/en/publications/when-training-and-test-sets-are-different-characterizing-learning/ |
| 4 | CCN-CERT — ficha de la guía CCN-STIC-401 | 1 (emisor) | s. f. | Centro Criptológico Nacional, *CCN-STIC-401: Glosario y Abreviaturas* | https://www.ccn-cert.cni.es/es/series-ccn-stic/guias/glosario-de-terminos.html (403 a acceso automático) |
| 5 | `Resultados/metricas_firmas.csv`, `…_validation_report.txt`, `…_composicion_d3.csv` | 1 (dato propio) | 2026-08 | artefactos del proyecto | en disco |

## Cambios en Bibliografía.md

| `[n]` | Qué he hecho |
|---|---|
| [2] | «Dónde se usa» reescrito al uso real (`1.2:14` acotado a lo descriptivo, `2.2.2:35`); documentada la retirada de la atribución historiográfica. Aviso de abajo actualizado: la propuesta pasa de «no ejecutada» a **ejecutada por la vía negativa** |
| [3] | «Dónde se usa» corregido: decía `1.2:16`, que **no contiene la cita**; es **`1.2:30`** tras el callout nuevo. Las otras 4 ocurrencias se reverificaron y estaban bien |
| [8] | **Marcada ⚠️ EDICIÓN NO ESTABLECIDA** (P5), con las dos candidatas y la razón de por qué no se elige |
| [10] | URL sustituida por la ficha oficial de la guía (P6) y **marcado** lo no verificable; se conserva el enlace anterior como rastro |
| [26] | **Mapeada** al uso nuevo `1.2:32` (P4). Celda «Localizador por uso» rellenada con la reserva de la URL y la aclaración 1998/1999 |
| [76] | Documentado el **no desdoble** con su razón, y añadidos los datos completos y verificados del capítulo de Storkey (**pp. 3-28**), con las dos discrepancias del registro declaradas |

Más **cuatro declaraciones caducadas del rango corregidas** (decían `[76]` o `[74]` como primer
libre) y **un callout nuevo** que resume el pase. **Son 6 entradas tocadas: más de tres, y se declara
aquí como manda el protocolo.** **Cero altas: el primer número libre sigue siendo el `[78]`.**

## Implicaciones para el proyecto

1. **`1.2 Preliminares` pierde una afirmación.** No es una pérdida de rigor sino lo contrario, pero
   **Francisco puede querer recuperarla**: bastaría con acceso al Yost 2016 o a otra revisión de
   nivel 1. Sería un alta, la primera del `[78]`.
2. **Dos decisiones siguen pendientes de Francisco y bloquean el pase a Zotero**: la **edición de
   `[8]`** y la **versión de `[10]`**. Ninguna la puede cerrar un agente.
3. **El desdoble de `[76]` sigue disponible** si Francisco acepta repuntar `5.1:86` a un `[78]`. Con
   los datos ya en la fila, es un cambio de dos líneas. **No contradice ninguna decisión cerrada de
   `resumen-de-decisiones.md`.**
4. **La corrección del «37» toca cifras que la memoria puede estar usando.** Aquí solo se han
   corregido los **dos informes** de `99 Investigación/`; **si el capítulo 5 repite ese «37 en D2»,
   hay que revisarlo aparte** — queda fuera de este encargo y no se ha inspeccionado.

---

# Adenda — SEGUNDO pase en serie del 2026-08-18: las 11 decisiones de Francisco

Los tres puntos que este informe dejaba «pendientes de Francisco» (implicaciones 1, 2 y 3) **los ha
decidido él ese mismo día**, junto con ocho más. Este segundo pase **no investiga: ejecuta**.

- **Contador:** 76 filas antes, **77 después**. **Una sola alta, `[78]`.** `[9]` sigue quemada,
  ningún `[n]` preexistente renumerado. **El primer libre pasa a ser el `[79]`** — donde este informe
  dice `[78]` como «primer libre», está caducado.
- **`[8]` Stallings — edición FIJADA:** 5.ª ed., Pearson, 2023, ISBN 978-0-13-809167-5. Cae la marca
  de P5. La **página** sigue sin establecerse: no hay acceso al texto paginado de esa edición.
- **`[10]` CCN-STIC-401 —** se cita **la ficha oficial, sin versión ni fecha**, y eso es la forma de
  cita decidida, no un pendiente. **El «1.069 términos» queda retirado** por ser de segunda mano;
  comprobado en disco que no aparecía en ninguna nota de la memoria.
- **`[26]` Roesch —** metadatos reconstruidos **aceptados tal cual**; se retira el «⚠️ identidad
  inferida del contexto» e **incidencia cerrada**.
- **`[76]` DESDOBLADA.** Alta de **`[78]` A. Storkey, «When Training and Test Sets Are Different:
  Characterizing Learning Transfer», cap. 1, en *Dataset Shift in Machine Learning*, MIT Press, 2009,
  pp. 3-28** (rango reverificado el 2026-08-18), y **marcador de `5.1` repuntado de `[76, cap. 1]` a
  `[78, pp. 3-28]`**. Lo que este informe declaraba fuera de la mano del `researcher` **lo ha
  encargado Francisco por escrito**. `[76]` queda como volumen contenedor **sin uso en el texto**.
- **Contradicción interna de la fila `[76]` — resuelta:** decía a la vez «rango establecido» y «no se
  desdobla», y devolvía a Francisco una decisión ya tomada.
- **`2.1.5:114`** ya llevaba `[5, cap. 2]`: verificado, no tocado.
- **`2.1.4:46` y `:51` (k-NN):** localizador **retirado**, queda `[5]` a secas. La reserva que ya
  constaba en la fila de `[5]` —el cap. 3 no desarrolla el aprendizaje perezoso— era correcta.
- **LOF en `2.1.4` — NO se ha dado de alta nada, y esa es la noticia.** El encargo pedía dar de alta
  Breunig, Kriegel, Ng y Sander (2000), SIGMOD, **10.1145/335191.335388**, y reapuntar ahí la cita.
  **Eso es exactamente `[75]`**, alta de la Tanda 14 por esa misma corrección de atribución (venía de
  `[12]` Hastie), y `2.1.4:76` **ya cita `[75]`**. DOI reverificado contra Crossref: coincide autor
  por autor, *ACM SIGMOD Record*, vol. 29, n.º 2, pp. 93-104, 2000. Dar un número nuevo **habría
  duplicado la referencia**, así que **el segundo número que el encargo reservaba no se consume**.
- **Anderson en `1.2` —** la frase queda **retirada en firme**: ya no es recuperable «si aparece el
  aval». El callout de la nota lo declara cerrado.
- **Las 5 citas colgantes irreconstruibles — sus afirmaciones, RETIRADAS**, no solo sus marcadores:
  `[27]` (viñeta SIEM/XDR de `2.2.2`), `[28]` (enunciado de defensa en profundidad de `2.2.2`, con el
  párrafo reescrito para que la sección siga leyéndose), `[37]` (atribución del panorama de amenazas
  en `2.2.5` **y** cierre de `2.3.2`), `[44]` (párrafo «Apoyo al analista en el SOC» de `2.3.2`) y
  `[45]` (junto con `[37]`). Cada sitio lleva su callout; las cinco entradas siguen en la tabla,
  **sin borrar ni renumerar**, marcadas como sin uso.

## Lo que sigue sin poder confirmarse

- **La página exacta** dentro de `[78]` (pp. 3-28) y dentro de `[8]` cap. 1: no hay texto paginado
  accesible en ninguno de los dos. **Se marca, no se inventa.**
- **La discrepancia del registro de Edinburgh** sobre `[78]`: fecha el capítulo en dic. 2008 y
  consigna «Yale University Press», que es un error de ese registro (la editorial es MIT Press,
  verificada en su catálogo y en la ACM DL).
- **Seis entradas quedan sin uso en el texto** (`[27]`, `[28]`, `[37]`, `[44]`, `[45]`, `[76]`).
  Es consecuencia buscada de las decisiones, pero **rompe la dirección inversa de T16** y conviene
  que Francisco lo sepa: borrarlas o no es decisión suya.
