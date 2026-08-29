---
titulo: "Fuente primaria de las tres afirmaciones de 6.2 sin marcador de cita (TabArena, TESSERACT y Nested Learning)"
numero: "-"
estado: informe
docx_ref: "-"
---

# Fuente primaria de las tres afirmaciones de 6.2 sin marcador de cita

- **Encargo:** tres afirmaciones de la memoria atribuyen contenido a trabajos publicados concretos y
  no llevan marcador `[n]`; un tribunal simulado las marcó como fallo de verificabilidad.
  Identificar y verificar la fuente primaria de cada una, comprobar que la afirmación se sostiene en
  esa fuente, y dar de alta las tres entradas en `Bibliografía.md` con su «Localizador por uso».
- **Fecha:** 2026-08-28
- **Alcance:**
  - **Entra:** las tres afirmaciones literales de §6.2.1 y §6.2.6 (extracción
    `Resultados/docx/REPASO_20260828-1723/documento.txt`); la verificación de autores, título, sede,
    año e identificador de cada fuente; la comprobación de que el contenido atribuido está en el
    original; el alta de las tres entradas y la asignación de `[n]` de vault y de `.docx`.
  - **Queda fuera** (por encargo): las otras entradas huérfanas (`[9]`, `[65]`, `[70]` y las de
    librerías), cualquier edición de la memoria o de las notas del vault, y ampliar el estado del
    arte de ninguno de los tres temas.
- **Alimenta a:** [[6.2 Líneas futuras]] (§6.2.1 y §6.2.6). Insumo previo:
  [[aprendizaje-continuo-nested-learning]] y [[clasificadores-tabulares-y-arquitecturas-hibridas]].

> [!warning] Este informe no es memoria
> Es insumo citable. No entra en [[00 Índice TFG]] y su prosa no se copia a un capítulo sin que lo
> decida Francisco.

## Respuesta corta

Las tres fuentes están **identificadas y verificadas, las tres de nivel 1**, y dadas de alta como
`[111]` TabArena, `[112]` TESSERACT y `[113]` Nested Learning. Dos afirmaciones **se sostienen tal
como están escritas** —(B) TESSERACT y (C) Nested Learning, esta última con la fecha de corte
explícita que ya lleva—. La tercera, **(A) TabArena, se sostiene con matiz y hay que reescribirla**:
el original dice «algunos modelos **de aprendizaje profundo**» y la memoria dice «algunos modelos», y
la glosa del mecanismo que añade la memoria («la misma partición con la que se reporta») no es lo que
dice la fuente. Aviso aparte: **el siguiente número libre del `.docx` es el `[76]`, no el `[75]`** —el
`[75]` ya está ocupado por Moustafa y Slay—.

## Hallazgos

### 1. (A) TabArena — fuente verificada, afirmación con matiz

**Fuente primaria.** N. Erickson, L. Purucker, A. Tschalzev, D. Holzmüller, P. Mutalik Desai,
D. Salinas y F. Hutter, «TabArena: A Living Benchmark for Machine Learning on Tabular Data»,
*NeurIPS 2025*, Datasets and Benchmarks Track, *spotlight*. Autores, título y sede verificados contra
el registro de arXiv ([arXiv:2506.16791](https://arxiv.org/abs/2506.16791), v4 de 3 nov. 2025, campo
*comments*: «Accepted (spotlight) at NeurIPS 2025 Datasets and Benchmarks Track») — nivel 1.

**Lo que dice el original, literal (resumen):**

> «*Finally, we show that ensembles across models advance the state-of-the-art in tabular machine
> learning. We observe that some **deep learning** models are overrepresented in cross-model
> ensembles due to validation set overfitting, and we encourage model developers to address this
> issue.*»

**Y en el cuerpo**, §3.2 «Holistic Benchmarking of Peak Performance with TabArena», apartado
«Ensembles Across Models and Individual Contributions»:

> «*Notably, models with the highest performance on the leaderboard are not necessarily the ones with
> the highest weights, likely because the ensemble construction favors models overfitting the
> validation data, such as ModernNCA and RealMLP as seen in Section A.6.*»

**Veredicto: se sostiene CON MATIZ.** El fenómeno —sobrerrepresentación de modelos en los conjuntos
entre modelos por sobreajuste al conjunto de validación— **está documentado en TabArena, y de forma
casi literal**. Pero hay dos desajustes de alcance:

1. **El original lo restringe a modelos de aprendizaje profundo**, y nombra a los dos culpables
   (ModernNCA y RealMLP, ambos redes neuronales). La memoria escribe «algunos modelos», sin el
   calificativo. Esa generalización **no está respaldada**: TabArena no observa el fenómeno en los
   *gradient-boosted trees* ni en los modelos fundacionales.
2. **La glosa del mecanismo que añade la memoria no es la de la fuente.** La memoria explica «si los
   miembros se escogen mirando la misma partición con la que se reporta, entra el que mejor se ajusta
   a esa partición, no el que mejor generaliza». En TabArena el sobreajuste es al **conjunto de
   validación con el que se construye el conjunto**, que **no** es la partición sobre la que se
   reporta el resultado del *leaderboard*. La intuición va en la dirección correcta, pero **la frase
   atribuye a la fuente un enunciado que la fuente no hace**.

**Reescritura propuesta** (la decide Francisco; este informe no toca la memoria):

> «El benchmark TabArena documenta que algunos modelos de aprendizaje profundo aparecen
> sobrerrepresentados en los conjuntos entre modelos porque sobreajustan el conjunto de validación
> con el que se construye el conjunto: entra el que mejor se ajusta a esa partición, no el que mejor
> generaliza.»

> [!note] No es un hallazgo nuevo del vault
> La cita textual correcta ya estaba recogida en [[clasificadores-tabulares-y-arquitecturas-hibridas]]
> («*some deep learning models are overrepresented in cross-model ensembles due to validation set
> overfitting*»). El «de aprendizaje profundo» se perdió al pasar de ese informe a la prosa de
> `6.2.1`. Es un fallo de trasvase, no de investigación.

### 2. (B) TESSERACT — fuente verificada, afirmación sostenida

**Fuente primaria.** La pista de partida del encargo **se confirma en los cinco campos**, verificada
contra el **BibTeX oficial de USENIX** (entrada 235493), que además aporta páginas e ISBN que la
pista no traía:

| Campo | Pista del encargo | Verificado |
|---|---|---|
| Autores | Pendlebury, Pierazzi, Jordaney, Kinder, Cavallaro | ✅ idénticos y en ese orden |
| Título | «TESSERACT: Eliminating Experimental Bias in Malware Classification across Space and Time» | ✅ literal |
| Sede | USENIX Security Symposium | ✅ 28th USENIX Security Symposium (USENIX Security 19), Santa Clara, CA |
| Año | 2019 | ✅ ago. 2019 |
| Extra | — | **pp. 729-746**, ISBN 978-1-939133-06-9, USENIX Association |

Afiliaciones (de la ficha de USENIX): Pendlebury, Pierazzi y Jordaney en *King's College London &
Royal Holloway, University of London*; Kinder en *Bundeswehr University Munich*.

**Que la métrica AUT se define en ESE artículo: confirmado.** Es la pregunta explícita del encargo y
la respuesta es sí. El resumen ya anuncia «*a new metric that summarizes the expected robustness of a
classifier in a real-world setting*», y en la **versión extendida** —que declara «*This article
extends our work published at USENIX Security Symposium 2019*»— la métrica se define con nombre
propio en **§4.2 «Time-aware Performance Metrics», ecuación 4**: **AUT (*Area Under Time*)**,
construida por la regla del trapecio como las métricas tipo AUC y acotada en [0, 1]. La restricción
de diseño que la memoria menciona es **C1 *Temporal training consistency*** (**§4.1 «Evaluation
Constraints»**): todos los objetos del entrenamiento deben ser estrictamente anteriores en el tiempo
a los del test. **No es de otro artículo.**

**Veredicto: se sostiene.** Los cuatro elementos que la memoria atribuye están en la fuente: (i) el
sesgo temporal como fuente **sistemática** de resultados inflados —el artículo identifica dos,
temporal y espacial—; (ii) las **restricciones de diseño experimental**; (iii) entre ellas, que el
entrenamiento **preceda cronológicamente** a la evaluación (C1); y (iv) una **métrica de robustez
esperada en despliegue**, AUT. La redacción de la memoria es fiel, incluido el matiz de decir «una de
las fuentes sistemáticas» y no «la».

> [!note] Salvedad de dominio, no de contenido
> TESSERACT formaliza el sesgo sobre **clasificación de *malware***; la memoria escribe «clasificación
> de amenazas», que es un término más ancho. No lo marco como matiz porque el propio artículo se
> presenta como marco metodológico general para clasificación en seguridad, y porque los mismos
> autores lo extienden así en `[18]` Arp *et al.*, ya citada en la memoria.

### 3. (C) Nested Learning — fuente verificada, las dos afirmaciones sostenidas

**Fuente primaria.** A. Behrouz, M. Razaviyayn, P. Zhong y V. Mirrokni, «Nested Learning: The
Illusion of Deep Learning Architectures», *NeurIPS 2025*, Main Conference Track. Verificada por tres
vías concordantes: las **actas de NeurIPS**, **OpenReview** (`nbMeRvNb7A`) y **arXiv:2512.24695**
(31 dic. 2025; *comments*: «A version of this work is published at Neural Information Processing
Systems (NeurIPS) 2025»). **Se cita por las actas** — la copia del autor (`alibehrouz.com/files/NL.pdf`)
es nivel 2 y además titula «…Architecture» en singular.

**Los tres mecanismos, uno a uno:**

| Mecanismo que atribuye la memoria | ¿Está en la fuente? | Dónde |
|---|---|---|
| **Varios niveles anidados** | ✅ Sí, es la tesis central | Resumen («*a set of nested, multi-level, and/or parallel optimization problems, each of which with its own context flow*») y §1.2 |
| **Un espectro de frecuencias** (de actualización) | ✅ Sí | §1.1 (el Transformer como capas lineales con frecuencias de actualización distintas; motivación en las ondas cerebrales) y §7, *Continuum Memory System*: el bloque de nivel *s* se actualiza cada ⌈C⁽ˢ⁾/C⁽ˢ⁺¹⁾⌉ pasos |
| **Un optimizador que es él mismo una memoria entrenable** | ✅ Sí, es la contribución (1) | Resumen («*known gradient-based optimizers, such as Adam, SGD with Momentum, etc., are in fact associative memory modules that aim to compress the gradients' information*») y §4 |

**Que la validación experimental se limita a modelos de lenguaje: confirmado.** §9 evalúa modelado de
lenguaje y razonamiento de sentido común, comprensión de contexto largo (*needle-in-a-haystack*,
BABILong), *recall* y memorización in-context, reconocimiento de lenguaje, comparación de
optimizadores y aprendizaje continuo. El bloque de *class-incremental learning* se hace **en dominio
de texto** (CLINC, Banking y DBpedia, con *backbones* Llama3-3B y Llama3-8B, Fig. 6). **Ni un solo
experimento sobre datos tabulares.** El resumen del artículo no menciona ni datos tabulares ni
detección de intrusiones.

**Que no consta aplicación a datos tabulares ni a detección de intrusiones: confirmado, con la
reserva metodológica que la propia frase de la memoria ya incorpora.** No he encontrado ninguna
aplicación publicada, igual que las dos búsquedas dirigidas del informe del 2026-08-01. La memoria
está redactada con la salvaguarda correcta —«**no consta a fecha de este trabajo**»—, que es
exactamente la formulación defendible: ausencia de evidencia, no evidencia de ausencia. Si dijera «no
se ha aplicado» o «no es aplicable», habría que corregirla; no lo dice.

**Veredicto: se sostienen los dos párrafos.** Sin matiz. Y son literalmente la formulación que el
informe del 2026-08-01 dejó respaldada en su §E, así que el trasvase a la memoria fue fiel.

### 4. Aviso de numeración del `.docx` — el siguiente libre es el `[76]`

El encargo dice que en el `.docx` el siguiente número libre es el `[75]`. **No lo es.** Verificado en
[[Bibliografia del docx - numeracion y anclas]]: el `.docx` necesita **75 números**, «los 11
congelados más 64 obras, de `[12]` a `[75]`», y el **`[75]` está ocupado por Moustafa y Slay
(UNSW-NB15, MilCIS 2015)**, ancla del dataset en `6.2 Líneas futuras`. Ese mismo informe fija la
regla: las obras nuevas reciben número **por detrás del `[75]`**, sin intercalar. Por tanto:

| Afirmación | `[n]` de vault | `[n]` del `.docx` |
|---|---|---|
| (A) TabArena | **[111]** | **[76]** |
| (B) TESSERACT | **[112]** | **[77]** |
| (C) Nested Learning | **[113]** | **[78]** |

Contador de vault contado en disco el 2026-08-28: **110 números emitidos**, el `[110]` el último, y
las ocho quemadas (`[9]`, `[27]`, `[28]`, `[37]`, `[40]`, `[44]`, `[45]`, `[76]`) sin reutilizar. El
primer libre era, en efecto, el `[111]`.

> [!warning] Ojo con el falso amigo
> El **`[76]` del vault está QUEMADO**, pero el **`[76]` del `.docx` es libre y es el que va a
> TabArena**. Son dos contadores distintos y aquí se cruzan en el mismo número.

## Lo que no he podido confirmar

- **La numeración de secciones y la página exacta de TESSERACT en la versión de USENIX 2019.** El
  texto completo devuelve **403 a todo acceso automático**: `WebFetch` sobre
  `usenix.org/system/files/sec19-pendlebury.pdf` y sobre la ficha de la ponencia, y el PDF del
  repositorio institucional de KCL no expone capa de texto legible. Los localizadores que doy
  (**§4.1** para C1, **§4.2** para AUT) están verificados sobre la **versión extendida**
  (arXiv:2402.01359v2), que declara extender el artículo de 2019. **No se ha inventado ninguna
  página** y no he intentado sortear ningún muro de pago ni iniciar sesión.
- **La paginación de Nested Learning en las actas de NeurIPS.** Los localizadores por sección (§1.1,
  §1.2, §4, §7, §9) se establecieron sobre la copia del autor, que **no comparte paginación con las
  actas**. Marcado como no establecido en la entrada.
- **Que la afirmación (A) no aparezca además en otra sección del cuerpo de TabArena.** He localizado
  su enunciado en el resumen y en §3.2, y el propio §3.2 remite a un apéndice (§A.6) que no he
  leído. Puede haber un desarrollo más fino allí; lo que afirmo se apoya en las dos sedes que sí he
  leído.
- **Fecha de corte de la afirmación (C).** «No consta ninguna aplicación a datos tabulares ni a
  detección de intrusiones» es una comprobación **a 2026-08-28** sobre un artículo de diciembre de
  2025. La frase de la memoria ya lleva la salvaguarda temporal, así que no hay nada que corregir,
  pero **la comprobación caduca** y conviene repetirla antes de la defensa.

## Fuentes

| # | Fuente | Nivel | Fecha | Cita completa | URL / DOI |
|---|---|---|---|---|---|
| 1 | TabArena: A Living Benchmark for Machine Learning on Tabular Data | **1** | 2025 (v1 20 jun. 2025; v4 3 nov. 2025) | N. Erickson, L. Purucker, A. Tschalzev, D. Holzmüller, P. Mutalik Desai, D. Salinas y F. Hutter, en *Advances in Neural Information Processing Systems 38 (NeurIPS 2025)*, Datasets and Benchmarks Track (*spotlight*), 2025 | https://arxiv.org/abs/2506.16791 · 10.48550/arXiv.2506.16791 · https://tabarena.ai |
| 2 | Ídem, versión HTML de arXiv (de donde sale la cita del cuerpo, §3.2) | 2 | 2025-11-03 | Versión v4. Usada para localizar la afirmación fuera del resumen | https://arxiv.org/html/2506.16791v4 |
| 3 | TESSERACT: Eliminating Experimental Bias in Malware Classification across Space and Time | **1** | 2019-08 | F. Pendlebury, F. Pierazzi, R. Jordaney, J. Kinder y L. Cavallaro, en *Proc. 28th USENIX Security Symposium*, Santa Clara, CA, ago. 2019, USENIX Association, pp. 729-746. ISBN 978-1-939133-06-9. **Metadatos del BibTeX oficial de USENIX, entrada 235493** | https://www.usenix.org/conference/usenixsecurity19/presentation/pendlebury |
| 4 | Ídem, preprint en arXiv (usado para verificar resumen, autores y sesgos) | 2 | 2018-07 | arXiv:1807.07838. Campo *comments*: publicado en USENIX Security 2019 | https://arxiv.org/abs/1807.07838 |
| 5 | Ídem, **versión extendida** (de donde salen los localizadores §4.1 y §4.2) | 2 | 2024-02 | arXiv:2402.01359v2. Declara «*This article extends our work published at USENIX Security Symposium 2019*». **Es obra distinta: no sustituye a la nº 3 para citar** | https://arxiv.org/html/2402.01359v2 |
| 6 | Nested Learning: The Illusion of Deep Learning Architectures | **1** | 2025-12 | A. Behrouz, M. Razaviyayn, P. Zhong y V. Mirrokni, en *Advances in Neural Information Processing Systems 38 (NeurIPS 2025)*, Main Conference Track, 2025 | https://proceedings.neurips.cc/paper_files/paper/2025/hash/4309616aaed8e848009bc4a7ef73b493-Abstract-Conference.html · https://openreview.net/forum?id=nbMeRvNb7A |
| 7 | Ídem, preprint en arXiv (verificación de identificadores y resumen) | 2 | 2025-12-31 | arXiv:2512.24695 [cs.LG]. *Comments*: «A version of this work is published at NeurIPS 2025» | 10.48550/arXiv.2512.24695 |

**Evidencia interna del vault** (no son fuentes externas; leída el 2026-08-28):
`Obsidian_TFG_Vault/99 Investigación/aprendizaje-continuo-nested-learning.md` (§1, §4.1 y §E, de
donde salen los localizadores por sección de Nested Learning, verificados allí contra el PDF el
2026-08-01) · `…/clasificadores-tabulares-y-arquitecturas-hibridas.md` (la cita textual de TabArena) ·
`…/Bibliografia del docx - numeracion y anclas.md` (§ numeración: `[1]`-`[75]` ocupados y la regla de
no intercalar) · `Resultados/docx/REPASO_20260828-1723/documento.txt` (el texto literal de las tres
afirmaciones).

**Herramientas:** `WebFetch` en todo salvo un punto. **Playwright usado en `www.usenix.org`**, y solo
porque `WebFetch` devolvió **403** tanto en la ficha de la ponencia como en el PDF; el navegador sí
sirvió el HTML y de ahí salen las páginas, el ISBN y las afiliaciones (BibTeX oficial). Navegador
cerrado al terminar. No se inició sesión en ningún sitio.

## Cambios en Bibliografía.md

| `[n]` | Qué he hecho |
|---|---|
| [111] | **Añadida** — TabArena, nivel 1. Con «Localizador por uso» establecido (§3.2 y resumen) y **aviso de que la frase de la memoria generaliza la del original**, con reescritura propuesta |
| [112] | **Añadida** — TESSERACT, nivel 1. Metadatos completos del BibTeX de USENIX (pp. 729-746, ISBN). Localizador **parcial**: §4.1 y §4.2 verificados en la versión extendida; **numeración y página de la versión de 2019 marcadas como NO establecidas** |
| [113] | **Añadida** — Nested Learning, nivel 1. Localizador por sección (§1.1, §1.2, §4, §7, §9 y Fig. 6); **paginación de actas marcada como NO establecida**. Anotada la discrepancia de título singular/plural entre copias |

**Tres entradas, ninguna existente tocada.** No he borrado, renumerado ni sustituido nada, y **no he
tocado `[9]`, `[65]`, `[70]` ni las entradas de librerías**, que están fuera de este encargo. El
aviso de `[111]` se ha añadido en `## Avisos y reservas por entrada`, no dentro de la fila.

## Implicaciones para el proyecto

> [!warning] Propongo, no decido
> Nada de esta sección edita la memoria ni crea tarea. Los marcadores `[76]`, `[77]` y `[78]` del
> `.docx` **los escribe Francisco en Word**; este informe solo dice cuáles son y dónde van.

1. **Los tres marcadores que hay que poner en el `.docx`.** `[76]` al final de la frase de TabArena en
   §6.2.1; `[77]` al final de la frase de TESSERACT en §6.2.6; `[78]` en los dos párrafos de Nested
   Learning de §6.2.6 —**el segundo párrafo también lo necesita**, porque atribuye los tres
   mecanismos—. **A pelo, sin localizador**: `[76]`, no `[76, §3.2]`. La derogación del 2026-08-24
   sigue vigente.
2. **Hay que reescribir la frase de TabArena de §6.2.1**, con la propuesta de la §1 de este informe.
   Es la única de las tres que no se sostiene tal cual, y el arreglo es de dos palabras más un
   cambio de glosa. Dejarla como está sería atribuir a TabArena un enunciado más ancho que el suyo,
   que es exactamente el tipo de fallo que el tribunal simulado busca.
3. **Ninguna decisión de `resumen-de-decisiones.md` queda desmentida.** Al contrario: (B) y (C)
   confirman el veredicto ya cerrado sobre Nested Learning («no aplicable, y con cuatro razones
   citables») y el criterio rector del lote del 2026-08-06 —declarar las imposibilidades con su razón
   técnica—. (A) refuerza la línea futura ★ nº 1 de `EL_FUTURO.md`, el *ensemble* de detectores de la
   etapa 1, añadiéndole una **advertencia de diseño**: si algún día se construye ese conjunto, los
   miembros no se eligen mirando la partición con la que se reportará el resultado.
4. **Queda pendiente, fuera de este encargo:** repetir la comprobación de (C) —«no consta aplicación
   a datos tabulares»— antes de la defensa, porque es una afirmación con fecha de caducidad, y
   resolver las otras cuatro entradas huérfanas.
