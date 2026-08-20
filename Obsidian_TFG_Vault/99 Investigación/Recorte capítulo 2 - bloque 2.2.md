---
titulo: "Recorte del capítulo 2 — bloque 2.2 Ciberseguridad"
tipo: informe de análisis
fecha: 2026-08-20
alcance: "2.2.1 · 2.2.2 · 2.3.3 · 2.2.4 · 2.2.5"
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
# Recorte del capítulo 2 — bloque 2.2 Ciberseguridad

> [!important] Qué pidió el profesor y qué decide Francisco
> El profesor **no pidió recortar el capítulo 2**. Su indicación literal, recogida en
> `mis-apuntes-del-informe.md`, es: «El informe está bien en general, pero hay que mejorar bastante
> la redacción, simplificando las explicaciones de las soluciones analizadas sin dar todos los
> hiperparámetros **(por ejemplo, que aporta al lector saber si has usado como semilla el valor 42)**, quizás recortando algunos apartados (por ejemplo, los primeros apartados del
> Capítulo 3 no creo que sean necesarios y se podían unificar)». El apartado que señaló es del
> **capítulo 3**.
> Por tanto, en la tabla de veredictos la columna **(a)/(b)** distingue:
> - **(a) profesor** — el recorte responde a algo que él dijo. En este bloque **(a) aplica a un
>   único tipo de material**: el detalle técnico redundante en las descripciones de soluciones
>   analizadas («simplificando las explicaciones de las soluciones analizadas»), que en 2.2 aparece
>   en la descripción de los tres trabajos comparables de 2.2.4.5.
> - **(b) volumen** — el recorte lo decide **Francisco hoy**, por el criterio «quién lo usa»
>   aplicado a un capítulo 2 que pesa 35.361 palabras sobre 108.591 totales. **Casi todo este
>   informe es (b)**, y así debe defenderse: no se le atribuye al profesor.

---

## 1. Resumen ejecutivo

**Volumen actual, medido con `wc -w` sobre los cinco ficheros:**

| Nota | Palabras |
|---|---|
| 2.2.1 Introducción a la ciberseguridad | 1.358 |
| 2.2.2 Sistemas de detección de intrusiones | 2.635 |
| 2.2.3 Taxonomía de los IDS | 2.709 |
| 2.2.4 Detección por firmas frente a detección por anomalías | 2.909 |
| 2.2.5 Taxonomía de ataques y panorama de amenazas | 2.419 |
| **Total 2.2** | **12.030** |

**Dato previo que cambia la lectura de la cifra.** De esas 12.030 palabras, **1.586 son callouts de
gestión interna del proyecto** —los `[!warning] Verificación pendiente`, los `[!warning] … RETIRADA
el 2026-08-18` y las dos notas de decisión de 2.2.5.3—, medidos bloque a bloque:

| Nota | Palabras en callouts de gestión |
|---|---|
| 2.2.1 | 0 |
| 2.2.2 | 626 |
| 2.2.3 | 260 |
| 2.2.4 | 292 |
| 2.2.5 | 408 |
| **Total** | **1.586** |

Ese material **no va al `.docx`** en ningún escenario: no es prosa de la memoria, es bitácora. La
prosa real de 2.2 es por tanto **10.444 palabras**, y conviene descontarlo antes de discutir
recortes para no contarlo dos veces como «ahorro».

**Veredicto agregado.**

| | Palabras |
|---|---|
| 2.2 hoy (medido) | 12.030 |
| — de ellas, callouts de gestión (medido) | 1.586 |
| Prosa de memoria hoy (medido) | 10.444 |
| **Objetivo de redacción tras el recorte** (estimación de destino) | **≈ 7.300** |
| **Ahorro sobre la prosa de memoria** | **≈ 3.100 palabras (≈ 30 %)** |
| Ahorro sobre el total del fichero, contando la bitácora | ≈ 4.700 palabras (≈ 39 %) |

> [!warning] Qué está medido y qué no
> **Todas las cifras de «palabras hoy» de este informe están medidas con `wc -w`** sobre rangos
> delimitados por título. Las cifras de «objetivo» son **destinos de redacción**, no mediciones: no
> se puede contar prosa que aún no existe. Van marcadas siempre con `≈`. Ningún número de la columna
> «palabras» está estimado a ojo.

**Las tres piezas que NO se tocan** (verificado en disco, no asumido):

1. **2.2.4 es efectivamente la nota nuclear.** Tiene tres remisiones entrantes desde capítulos
   posteriores, y dos de ellas **por número de subapartado**: `3.2 Arquitectura del sistema` dice
   literalmente «El argumento **general** […] está desarrollado en 2.2.4 § 2.2.4.5 *De la
   complementariedad a la arquitectura híbrida*, y **aquí solo se instancia**»; `3.6 Conclusiones
   del capítulo` remite «sobre el fundamento expuesto en 2.2.4.5»; y `5.4 Conclusiones del
   capítulo` la enlaza en el apartado «Qué significa este FPR a prevalencia realista». Recortar
   2.2.4.5 dejaría a 3.2 y a 3.6 **sin el fundamento que declaran no repetir**.
2. **2.2.5 sostiene el espacio de salida del modelo.** `4.2 Base de datos utilizada` la enlaza por
   wikilink, y el punto ciego de `snmpgetattack` que enuncia 2.2.5.2 reaparece en `4.2`, `4.3`,
   `5.3`, `5.4` y `6.2` (hits contados con grep).
3. **2.2.4.3 «El falso positivo como coste operativo real» es el apartado con la remisión más
   fuerte de todo el bloque.** No es teoría suelta: `5.4` lo **instancia numéricamente** en «Qué
   significa este FPR a prevalencia realista» y su conclusión 2 cita las dos mismas fuentes que
   2.2.4.3, `[24]` (Axelsson) y `[25]` (NIST): «la conclusión clásica de la falacia de la tasa base
   es que el factor limitante de la detección de intrusiones es la tasa de falsos positivos, no la
   sensibilidad».

**El hallazgo que más recorte habilita.** Se buscó en los capítulos 3, 4, 5 y 6 la terminología
propia de cada apartado con `grep -rnwiE` (palabra completa). **Cero apariciones** de: `tríada`,
`CIA`, `HIDS`, `IPS`, `APT`, `ransomware`, `phishing`, `DDoS`, `MITRE`, `ATT&CK`, `Axelsson`,
`Snort`, `Denning`, `Anderson`, `Tombini`, `Khraisat`, `consola`, `preventiv*`, `correctiv*`. Es
decir: la tríada CIA, la contraposición HIDS/NIDS, la distinción IDS/IPS, la defensa en profundidad
y el panorama contemporáneo de amenazas **no los invoca por su nombre ningún capítulo posterior**.
Esa es la masa recortable, y toda ella es **(b)**.

---

## 2. Tabla apartado por apartado

Leyenda de veredictos: **QUEDA** · **COMPRIME** (a un párrafo) · **SALE** (del cuerpo).

### 2.2.1 Introducción a la ciberseguridad — 1.358 palabras medidas

| Apartado | Palabras | Quién lo usa | Veredicto | Destino | (a)/(b) |
|---|---|---|---|---|---|
| Preámbulo de la nota | 130 | — | COMPRIME | fundido con 2.2.1.2 | (b) |
| 2.2.1.1 Seguridad informática frente a ciberseguridad | 319 | Nadie en 3-6 | COMPRIME | una frase en el preámbulo | (b) |
| 2.2.1.2 La tríada CIA | 466 | `3.1` fila «Activo protegido» (mapea `dos`→disponibilidad y `probe`/`r2l`/`u2r`→confidencialidad e integridad); `2.2.5.1` ficha DoS | COMPRIME | un párrafo de ≈120 palabras | (b) |
| 2.2.1.3 Objetivos adicionales: autenticidad y responsabilidad | 213 | **Nadie** | SALE | solo exposición | (b) |
| 2.2.1.4 Recorrido del bloque de ciberseguridad | 230 | **Nadie** | SALE | **se borra** (no apéndice, no exposición) | (b) |

**Objetivo de la nota: ≈ 250 palabras** (hoy 1.358).

### 2.2.2 Sistemas de detección de intrusiones — 2.635 palabras medidas

| Apartado | Palabras | Quién lo usa | Veredicto | Destino | (a)/(b) |
|---|---|---|---|---|---|
| 2.2.2.1 Definición y propósito | 529 (de ellas 244 en callouts de gestión) | Encuadre de todo el trabajo: «alerta, no decisión ejecutada» es lo que sostiene el alcance declarado en `5.0` y `6.1` | QUEDA comprimido | ≈250 palabras; la tabla Entrada/Salida se disuelve en el texto | (b) |
| 2.2.2.2 Origen y evolución del concepto | 742 (188 la parte Anderson/Denning; 554 el resto y sus tres callouts) | `2.2.4.2` necesita a Denning `[3]`. **Anderson, Denning y Snort tienen cero hits en 3-6.** Además el linaje IDES/Snort **ya está contado en `1.2 Preliminares`** | COMPRIME | un párrafo de ≈150 palabras con `[2]`, `[3]`, `[26]`; el resto, solo exposición | (b) |
| 2.2.2.3 IDS frente a IPS | 285 | Solo para declarar «este TFG es detección, no prevención». Cero hits de `IPS` en 3-6 | COMPRIME | ≈90 palabras: dos frases + el `[!important] Alcance de este trabajo`, que se conserva | (b) |
| 2.2.2.4 Componentes funcionales de un NIDS | 468 (220 la lista de 5 bloques; 248 la tabla de correspondencia y el pie de la Figura 2.5) | **Sostiene la lectura de todo el capítulo 5**: «las métricas obtenidas evalúan el motor de análisis». Es el enunciado que `5.4` instancia en «Qué NO mide la latencia publicada» | QUEDA | la lista a ≈110; **la tabla de correspondencia y la Figura 2.5, íntegras** | (b) |
| 2.2.2.5 El IDS dentro de la defensa en profundidad | 558 (149 el callout de retirada de `[28]`) | **Nadie.** Cero hits de `defensa en profundidad`, `preventiv*`, `correctiv*`. Su cita `[28]` ya se retiró por irreconstruible | COMPRIME | un párrafo de ≈100 palabras («el H-NIDS es una capa detectiva, no un sustituto de las preventivas»); el resto, solo exposición | (b) |

**Objetivo de la nota: ≈ 1.000 palabras** (hoy 2.635, de las que 626 son bitácora).

### 2.2.3 Taxonomía de los IDS — 2.709 palabras medidas

| Apartado | Palabras | Quién lo usa | Veredicto | Destino | (a)/(b) |
|---|---|---|---|---|---|
| Preámbulo (los cuatro ejes ortogonales) | 229 | Prepara 2.2.3.5 | COMPRIME | ≈150 | (b) |
| 2.2.3.1 Por fuente de datos: HIDS y NIDS | 483 | Solo la conclusión «el sistema es un NIDS porque NSL-KDD son conexiones», que además **ya está en `4.2`** («Las 41 características y sus tres grupos»). Cero hits de `HIDS` en 3-6 | COMPRIME | un párrafo de ≈130; **la tabla de 6 filas HIDS/NIDS sale**: solo exposición | (b) |
| 2.2.3.2 → las tres casillas (firmas/anomalías/híbridos) | 229 | Es el eje que estructura el trabajo | QUEDA | ≈150 | (b) |
| 2.2.3.2 → «El problema del término *híbrido*» | 517 | **`5.3` lo necesita**: «cuando en 5.3 se contrasten resultados con la literatura, se indicará en qué sentido usa cada trabajo el término». La definición operativa del sentido (a) la invocan `3.2` y `2.2.4.5` | QUEDA | ≈380: se recorta el desarrollo de la crítica a Khraisat et al. (2019) —«despachan los sistemas híbridos en un único párrafo»— a dos frases | (b) |
| 2.2.3.2 → «Antecedentes de la combinación anomalías + firmas» | 264 | **Verificado: `3.2` cita `[33]` Tombini en la fila «Cobertura» de su tabla de razones, y `[32]` ADAM en el callout «Divergencia con ADAM»** | QUEDA íntegro | — | — |
| 2.2.3.3 Por modo de despliegue y por momento del análisis | 299 | **`3.1` es la única remisión entrante a esta nota**: «El sistema se evalúa en diferido sobre un corpus cerrado ([[2.2.3 Taxonomía de los IDS]])» | QUEDA comprimido | ≈140 | (b) |
| 2.2.3.4 Limitaciones transversales de los NIDS | 534 | **Parcial.** Cifrado, volumen/velocidad y evasión `[34]`: cero hits en 3-6 (`3.1` construye su propio modelo de adversario y se apoya en Arp et al., no en `[34]`). Sí se usan: la viñeta de falsas alarmas (puerta a 2.2.4) y `[21]` Sommer y Paxson, citado en `3.4` | COMPRIME | un párrafo de ≈150 con esas dos viñetas; cifrado, volumen y evasión → solo exposición | (b) |
| 2.2.3.5 Encaje del sistema desarrollado | 163 | Es la ficha de cuatro casillas que `3.1` y `3.2` instancian | QUEDA íntegro | — | — |

**Objetivo de la nota: ≈ 1.530 palabras** (hoy 2.709, de las que 260 son bitácora).

### 2.2.4 Detección por firmas frente a detección por anomalías — 2.909 palabras medidas

| Apartado | Palabras | Quién lo usa | Veredicto | Destino | (a)/(b) |
|---|---|---|---|---|---|
| Preámbulo | 161 | — | QUEDA | — | — |
| 2.2.4.1 Detección por firmas | 478 | `3.5`, `4.5` (reglas legibles vía `export_text`, `firmas_reglas_54.txt`); `[25]` reaparece en `5.4` | QUEDA | ≈400: el ejemplo de Snort se queda **solo con la regla**, sin glosarla línea a línea | (b) |
| 2.2.4.2 Detección por anomalías | 561 (138 en callout de gestión) | `3.4`, `4.4`, `5.1`. El callout del percentil 95 y del «5 % de falsas alarmas por diseño» es el que `5.1` y `5.4` dan por sabido | QUEDA | ≈500 | (b) |
| 2.2.4.3 El falso positivo como coste operativo real | 375 | **`5.4` «Qué significa este FPR a prevalencia realista» + su conclusión 2, con `[24]` y `[25]`; y `6.1` (prevalencia, pitfall P9)** | **QUEDA ÍNTEGRO** | — | — |
| 2.2.4.4 Comparación de ambos paradigmas | 220 | Es la bisagra: «un paradigma responde a *¿es esto sospechoso?* y el otro a *¿qué es esto?*», que es literalmente el reparto de etapas de `3.2` | **QUEDA ÍNTEGRO** | — | — |
| 2.2.4.5 → justificación del orden de la cascada (4 puntos) | 374 | **`3.2.2` y `3.6` lo citan por número y declaran no repetirlo** | **QUEDA ÍNTEGRO** | — | — |
| 2.2.4.5 → los tres trabajos comparables (Ji · Kim · Khraisat) | 675 (de ellas 154 en dos callouts de verificación) | **Kim, Lee y Kim `[69]` es obligatorio**: `3.2` dice «Su descripción arquitectónica, su cita y la salvedad de verificación que la acompaña están en 2.2.4 § 2.2.4.5, y **no se reproducen aquí**». **Ji `[68]` y Khraisat `[70]` no tienen ninguna remisión desde 3-6** | COMPRIME parcialmente | ≈475: Kim íntegro; Ji y Khraisat a dos frases cada uno, sin describir su arquitectura interna | **(a)** — «simplificando las explicaciones de las soluciones analizadas» |
| 2.2.4.5 → callout «Encaje con el resto de la memoria» | 74 | Enuncia la pregunta de investigación; `5.3` la responde | QUEDA íntegro | — | — |

**Objetivo de la nota: ≈ 2.680 palabras** (hoy 2.909, de las que 292 son bitácora). **Es la nota que
menos se toca, y a propósito.**

### 2.2.5 Taxonomía de ataques y panorama de amenazas — 2.419 palabras medidas

| Apartado | Palabras | Quién lo usa | Veredicto | Destino | (a)/(b) |
|---|---|---|---|---|---|
| Preámbulo | 165 | — | QUEDA | — | — |
| 2.2.5.1 → intro DARPA/KDD, 39 tipos → 40 etiquetas → 5 clases | 174 | `4.2`, `4.3`, `A.1` | QUEDA íntegro | — | — |
| 2.2.5.1 → las cuatro fichas (DoS, Probe, R2L, U2R) + callout «Conexión con el problema del TFG» | 698 | **Son las clases del problema**: `4.3` (tabla de categorías), `5.1`-`5.3`, `6.1` («clases minoritarias `u2r` y `r2l`») | QUEDA | ≈580: se recortan las **enumeraciones exhaustivas de tipos** de cada ficha, que duplican `A.1` y `4.2`; se conservan uno o dos ejemplos por categoría y la «huella en el tráfico» completa | (b) |
| 2.2.5.2 Gradación de visibilidad en red | 364 | **`4.2` la enlaza por wikilink**; el punto 2 (`snmpgetattack`, punto ciego estructural) reaparece en `4.2`, `4.3`, `5.3`, `5.4` y `6.2`; el punto 1 (jerarquía DoS→Probe→R2L→U2R como predicción *a priori*) es el marco con que `6.1` lee sus resultados por clase | **QUEDA ÍNTEGRO** | — | — |
| 2.2.5.3 Panorama actual de amenazas | 502 (de ellas 311 en tres callouts de gestión) | **Nadie.** Cero hits de `ransomware`, `APT`, `phishing`, `DDoS` en 3-6. Su cita `[37]` ya se retiró por irreconstruible y el apartado declara él mismo que no cuantifica nada | COMPRIME | un párrafo de ≈120 palabras que solo da pie a 2.2.5.4; el desarrollo de los cuatro bloques → **solo exposición** | (b) |
| 2.2.5.4 Vigencia de una taxonomía de 1998 | 539 (97 en callout de gestión) | Es la defensa de la elección de dataset. **Pero su tabla «A favor / En contra» duplica «Por qué se eligió NSL-KDD» de `4.2`**, que desarrolla cinco razones más la contrapartida | QUEDA comprimido | ≈350: se conserva «lo que caduca son los tipos, no las categorías» con `[38]` (kill chain / ATT&CK) y la segunda razón con `[22]` `[23]`; **la tabla A favor/En contra se retira y la sede única pasa a ser `4.2`** | (b) |

**Objetivo de la nota: ≈ 1.885 palabras** (hoy 2.419, de las que 408 son bitácora).

### Recuento de destino

| Nota | Hoy (medido) | Objetivo (≈) |
|---|---|---|
| 2.2.1 | 1.358 | 250 |
| 2.2.2 | 2.635 | 1.000 |
| 2.2.3 | 2.709 | 1.530 |
| 2.2.4 | 2.909 | 2.680 |
| 2.2.5 | 2.419 | 1.885 |
| **Total** | **12.030** | **≈ 7.345** |

Ahorro sobre el fichero completo: **≈ 4.685 palabras**. Descontando las 1.586 de bitácora que no
iban al `.docx` de todos modos, el ahorro **real sobre la prosa de la memoria** es de **≈ 3.100
palabras (≈ 30 % de 2.2)**.

---

## 3. Justificación por apartado

### 3.1 Por qué 2.2.1 se queda en un cuarto de su tamaño

La nota es un capítulo de manual de seguridad: define seguridad informática frente a ciberseguridad,
desglosa la tríada CIA en sus seis subconceptos, añade autenticidad y responsabilidad, y cierra con
un índice del propio bloque 2.2. Ninguna de esas piezas se vuelve a usar.

La comprobación es dura: `tríada`, `CIA`, `autenticidad`, `accountability`, `privacidad` no aparecen
como palabra completa en ningún fichero de los capítulos 3, 4, 5 y 6. El **único** uso real del
vocabulario CIA en toda la memoria posterior es una celda de tabla de `3.1 Requisitos del sistema`:
«**Activo protegido** | La red monitorizada: disponibilidad de sus servicios (`dos`),
confidencialidad e integridad de los equipos accesibles desde ella (`probe`, `r2l`, `u2r`)». Para
sostener esa celda basta con haber dicho, una vez, qué significan las tres palabras. No hace falta
el desglose «confidencialidad de los datos frente a privacidad», ni «integridad de los datos frente
a integridad del sistema».

**2.2.1.3 sale por completo.** Autenticidad y responsabilidad no las usa nada ni nadie: son un
apéndice conceptual del manual de Stallings que entró aquí por completitud. Su destino es **solo
exposición**, no apéndice: un apéndice del TFG debe contener material que el lector necesite
*consultar* —columnas del dataset, definiciones formales de métricas—, y dos definiciones de manual
disponibles en cualquier libro de texto no lo son. Meterlas en el apéndice sería mover el volumen,
no reducirlo.

**2.2.1.4 se borra.** Es un índice de las cuatro notas siguientes, redundante con el índice de la
memoria y con los preámbulos de cada nota, que ya se remiten entre sí. No tiene destino: no hay nada
que preservar.

### 3.2 Por qué 2.2.2 pierde dos tercios

Se conserva **el esqueleto de encuadre** y se retira **la historia**.

Lo que se conserva es lo que otros capítulos dan por dicho:

- La definición de IDS como «monitoriza, analiza y **emite una alerta**, no ejecuta la respuesta».
  Es el enunciado que hace legítimo que el capítulo 5 no reporte ninguna métrica de bloqueo.
- **2.2.2.4 completo en su parte útil**: la tabla que reparte los cinco bloques funcionales en
  «núcleo del trabajo / parcial / fuera de alcance», y su frase de cierre —«las métricas obtenidas
  evalúan **el motor de análisis**, y trasladarlas sin más a un despliegue completo supondría
  atribuir al sistema un rendimiento que depende también de bloques que aquí no se han
  implementado»—. `5.4` la instancia literalmente en «Qué NO mide la latencia publicada». La
  **Figura 2.5** se queda: es la única figura del bloque 2.2 y es exactamente el diagrama que marca
  esa frontera.

Lo que se comprime:

- **2.2.2.2, la línea temporal.** Es el bloque más caro de la nota (742 palabras, de las que 554 son
  el tramo posterior a Denning más tres callouts de gestión) y el que menos rinde. `Anderson`,
  `Denning` y `Snort` no aparecen en 3-6. Peor: el linaje ya se cuenta en `1.2 Preliminares` —«A
  esas dos familias —la detección por anomalías heredada de IDES y la detección por firmas
  popularizada por Snort—»—, de modo que 2.2.2.2 es en buena medida una segunda narración del mismo
  material. Lo único que hay que preservar es que `[3]` Denning quede citada, porque 2.2.4.2 se
  apoya en ella para la formulación original de la detección por anomalías. Un párrafo con `[2]`,
  `[3]` y `[26]` lo cubre.
- **2.2.2.3 IDS/IPS.** Su función real es una declaración de alcance, y esa declaración ya la hace
  el callout `[!important] Alcance de este trabajo`, que se conserva. La tabla de cuatro filas y el
  párrafo sobre desplegar primero en modo detección son contexto de manual: fuera.
- **2.2.2.5 defensa en profundidad.** Cero hits de su terminología en 3-6, y su cita `[28]` ya se
  retiró como irreconstruible, de modo que el enunciado del principio **ya está sin aval** en la
  nota. Lo que se salva es la conclusión de encuadre —el H-NIDS es una capa detectiva, y su
  aportación se mide por lo que hace visible, no por lo que impide—, que es la que da sentido a la
  pregunta de investigación. El reparto preventivo/detectivo/correctivo y las ubicaciones del sensor
  van a **solo exposición**.

### 3.3 Por qué 2.2.3 se queda a la mitad, y qué es intocable dentro de ella

Esta nota es mitad taxonomía de manual, mitad aportación propia. El recorte separa las dos.

**Lo de manual, fuera o comprimido.** 2.2.3.1 dedica 483 palabras a contraponer HIDS y NIDS, con una
tabla de seis filas, para concluir algo que se resuelve en una frase: NSL-KDD describe conexiones,
así que el sistema solo puede ser un NIDS. Y esa conclusión **ya está también en `4.2`**, en «Las 41
características y sus tres grupos». La tabla va a **solo exposición**: es didáctica, pero no la
consulta nadie. Igual con 2.2.3.4: de sus cinco limitaciones, tres (cifrado, volumen/velocidad,
evasión `[34]`) no las recoge ningún capítulo posterior. `3.1 Requisitos del sistema` sí trata al
adversario, pero construye su propio modelo de amenaza y se apoya en Arp et al., no en `[34]`. Se
conservan las dos que sí tienen continuidad: falsas alarmas —puerta de entrada a 2.2.4.3— y los
límites del ML aplicado a la detección `[21]`, que `3.4` cita.

**Lo propio, intocable.** Dos piezas:

1. **«El problema del término *híbrido*»** con sus cuatro sentidos (a)-(d) y la definición operativa
   del sentido (a). No es material de manual: es la delimitación que hace que las comparaciones del
   capítulo 5 signifiquen algo, y la propia nota lo dice —«cuando en `5.3` se contrasten resultados
   con la literatura, se indicará en qué sentido usa cada trabajo el término»—. `3.2` y `3.6`
   escriben «híbrido» dando por hecho que está definido aquí. Lo único recortable es el desarrollo
   de la crítica a la revisión de Khraisat et al. (2019), que hoy ocupa un párrafo entero para
   argumentar que ellos dedican un párrafo al tema; dos frases bastan.
2. **«Antecedentes de la combinación anomalías + firmas»**, ADAM `[32]` y Tombini `[33]`. Aquí la
   verificación fue decisiva y **contradice la intuición de que un apartado histórico es
   recortable**: `3.2 Arquitectura del sistema` cita `[33]` en la fila «Cobertura» de su tabla de
   razones —«argumento con el que ya se justificaba la combinación en serie anomalías→firmas en la
   literatura clásica [33]»— y `[32]` en el callout «Divergencia con ADAM», que es uno de los
   argumentos de diseño más finos del capítulo 3. Recortar este apartado dejaría **dos citas de
   `3.2` sin sede**. Queda íntegro.

**2.2.3.3 y 2.2.3.5 se quedan** porque son las dos únicas piezas con remisión entrante directa:
`3.1` enlaza la nota precisamente por el «corpus cerrado, evaluado en diferido», y la ficha de
cuatro casillas de 2.2.3.5 es lo que `3.1` y `3.2` instancian.

### 3.4 Por qué 2.2.4 apenas se toca

Es la nota nuclear y la verificación lo confirma sin ambigüedad. Tiene la mayor densidad de
remisiones entrantes de todo 2.2, y dos de ellas son **remisiones por número de subapartado con
declaración explícita de no repetición**, que es la forma más fuerte de dependencia que puede tener
una nota: si el destino desaparece, el origen queda cojo y nadie lo nota al leer el origen.

- `3.2 Arquitectura del sistema`, § «Por qué una cascada, y en este orden»: «El argumento
  **general** […] está desarrollado en 2.2.4 § 2.2.4.5 […] y **aquí solo se instancia**: este
  apartado no vuelve a demostrar por qué las anomalías van delante».
- `3.2`, § «El antagonista directo»: «Su descripción arquitectónica, su cita y la salvedad de
  verificación que la acompaña están en 2.2.4 § 2.2.4.5, y **no se reproducen aquí**».
- `3.6 Conclusiones del capítulo`: «sobre el fundamento expuesto en 2.2.4.5».
- `5.4 Conclusiones del capítulo`: enlaza 2.2.4 desde «Qué significa este FPR a prevalencia
  realista», y reutiliza sus dos fuentes, `[24]` y `[25]`.

Consecuencias directas: los cuatro puntos que justifican el orden de la cascada **no se tocan**; la
tabla comparativa de 2.2.4.4 **no se toca** (es de donde sale el reparto «¿es esto sospechoso?» /
«¿qué es esto?» que estructura `3.2`); y 2.2.4.3 **no se toca**, porque `5.4` lo convierte en
aritmética.

**El único recorte de 2.2.4, y el único (a) de todo el informe.** El bloque de los tres trabajos
comparables ocupa 675 palabras. De los tres, **solo Kim, Lee y Kim `[69]` tiene remisión entrante**
—`3.2` la declara expresamente—, así que se queda con su arquitectura descrita y su callout de
verificación. Ji et al. `[68]` y Khraisat et al. `[70]` no los reclama nadie desde 3-6, y hoy se
describen con su arquitectura interna al detalle: las tres etapas de Ji, el C5.0 más *one-class* SVM
apilados por meta-clasificador de Khraisat. **Esto es exactamente «las explicaciones de las
soluciones analizadas» que el profesor pidió simplificar**, y por eso este recorte —y solo este— se
marca **(a)**. Dos frases por trabajo: qué comparte con este TFG y en qué se aparta. El párrafo de
cierre que sitúa los tres frente al TFG se conserva, porque es lo que convierte la enumeración en
argumento.

### 3.5 Por qué 2.2.5 pierde su tercio menos anclado

La nota tiene dos mitades de valor muy distinto.

**La mitad que se queda.** Las cuatro fichas de categoría y la gradación de visibilidad **son la
definición formal del espacio de salida del modelo**, como dice su propio callout. `4.3` tabula las
categorías, `5.1`-`5.3` reportan por categoría, `6.1` explica los fallos de `u2r` y `r2l` con
exactamente el argumento de 2.2.5.2 —dependen de características de contenido, no de estadísticas de
flujo—, y el punto ciego de `snmpgetattack` reaparece en cinco notas distintas. El único recorte
admisible dentro de esta mitad son las **enumeraciones exhaustivas de tipos** de cada ficha, que
duplican `A.1 Columnas del dataset NSL-KDD` y `4.2`: uno o dos ejemplos por categoría bastan para
que la ficha se entienda, y el catálogo completo ya tiene sede.

**La mitad que sale.** 2.2.5.3 «Panorama actual de amenazas» es el apartado más huérfano de todo el
bloque 2.2. Ninguno de sus cuatro bloques —ransomware, APT, DDoS, phishing— aparece en 3-6 con
palabra completa. Su cita `[37]` se retiró como irreconstruible, y el propio apartado ya lleva dos
callouts declarando que no cuantifica nada y que no tiene fuente. Es decir: es una descripción
cualitativa, sin aval, sin cifras y sin consumidor. Su única función estructural es dar pie a
2.2.5.4, y eso se hace en un párrafo. Destino: **solo exposición**, no apéndice — un apéndice sin
fuente citable no es un apéndice, es un texto suelto, y llevar allí material sin aval reproduce el
problema en otro sitio.

**2.2.5.4 se queda pero adelgaza, y por una razón de sede única.** Su tabla «A favor / En contra
(asumido)» de cuatro filas dice lo mismo que «Por qué se eligió NSL-KDD» de `4.2`, que lo desarrolla
en cinco razones con su contrapartida. Dos sedes para el mismo argumento es exactamente el problema
que ya documentan `Datos repetidos en el capítulo 3.md` y `Datos repetidos en los capítulos 4-6.md`.
La sede natural del *por qué este dataset* es `4.2`, donde está el dataset; lo que 2.2.5.4 aporta y
`4.2` no es el argumento conceptual —**los tipos caducan, las categorías no**, con el contraste
frente a la *cyber kill chain* y MITRE ATT&CK `[38]`—, y eso se conserva.

---

## 4. Destinos: qué va al apéndice y qué no

El criterio que se ha aplicado, y que conviene poder enunciar ante el tribunal: **al apéndice va lo
que el lector necesita consultar; a exposición va lo que el lector necesitaría aprender**. Un
apéndice de material didáctico no reduce la memoria, solo la desplaza.

| Material retirado | Palabras hoy | Destino | Por qué ese destino |
|---|---|---|---|
| 2.2.1.1 distinción seguridad informática / ciberseguridad | 319 | Solo exposición | Definición de manual, sin ningún consumidor. No hay nada que consultar |
| 2.2.1.2 desgloses de la tríada (datos/privacidad, datos/sistema) | ≈340 de las 466 | Solo exposición | Ídem. Lo consultable de la tríada son los tres nombres, que se quedan en el cuerpo |
| 2.2.1.3 autenticidad y responsabilidad | 213 | Solo exposición | Cero uso. Al apéndice iría a envejecer |
| 2.2.1.4 recorrido del bloque | 230 | **Se borra** | Índice redundante con el índice de la memoria. No se preserva |
| 2.2.2.2 línea temporal completa (tramo posterior a Denning) | 554 | Solo exposición | Historia, no referencia. Además ya narrada en `1.2 Preliminares` |
| 2.2.2.3 tabla IDS/IPS y modo de despliegue progresivo | ≈195 de las 285 | Solo exposición | Contexto operativo; el trabajo no despliega nada en línea |
| 2.2.2.5 preventivo/detectivo/correctivo y ubicaciones del sensor | ≈450 de las 558 | Solo exposición | Su cita ya está retirada: llevarlo al apéndice sería consolidar material sin aval |
| 2.2.3.1 tabla comparativa HIDS/NIDS (6 filas) | ≈350 de las 483 | Solo exposición | Buena tabla docente, cero consumidores. **Único candidato discutible a apéndice** de todo el bloque: si Francisco quiere un `A.4 Taxonomía de los IDS`, esta tabla es lo único que lo justificaría |
| 2.2.3.2 desarrollo de la crítica a Khraisat et al. (2019) | ≈140 de las 517 | Solo exposición | Argumento *ad fontem* sobre una revisión; la conclusión se conserva en dos frases |
| 2.2.3.4 cifrado, volumen/velocidad y evasión `[34]` | ≈380 de las 534 | Solo exposición | Limitaciones reales pero no medidas ni discutidas en 5-6 |
| 2.2.4.5 arquitectura interna de Ji `[68]` y Khraisat `[70]` | ≈200 de las 675 | Solo exposición | **(a)**: es literalmente el detalle de soluciones analizadas que el profesor pidió simplificar |
| 2.2.5.1 catálogos exhaustivos de tipos por categoría | ≈120 de las 698 | **Ya está en `A.1` y `4.2`** | No hay destino nuevo: es una deduplicación, la sede ya existe |
| 2.2.5.3 los cuatro bloques del panorama de amenazas | ≈380 de las 502 | Solo exposición | Sin fuente citable. Un apéndice sin aval traslada el problema, no lo resuelve |
| 2.2.5.4 tabla «A favor / En contra» | ≈190 de las 539 | **Sede única en `4.2`** | Deduplicación, no retirada: el argumento se conserva donde está desarrollado |

> [!note] Un solo apéndice nuevo sería defendible, y probablemente no hace falta
> De las catorce piezas retiradas, **solo una** tiene forma de material de consulta: la tabla
> comparativa HIDS/NIDS de 2.2.3.1. El resto es prosa didáctica. La recomendación es **no crear
> apéndice nuevo** para el bloque 2.2 y llevarlo todo a exposición: crear un `A.4` para una sola
> tabla de seis filas añade estructura sin reducir volumen, y el TFG ya tiene tres apéndices con
> función clara (`A.1` columnas, `A.2` métricas, `A.3` ficha del sistema).

---

## 5. Material retirado, orientado a la DEFENSA ORAL

Lo que sale del cuerpo no se pierde: se convierte en munición para preguntas previsibles. Cada
bloque va con la pregunta que responde y con lo que hay que llevar preparado.

### 5.1 «¿Qué es exactamente la ciberseguridad y en qué se diferencia de la seguridad informática?»
**Retirado de:** 2.2.1.1 (319 palabras).
**Qué llevar:** seguridad informática = proteger **un** sistema automatizado (hardware, software,
firmware, datos, telecomunicaciones) preservando confidencialidad, integridad y disponibilidad
`[8, cap. 1]`. Ciberseguridad = el mismo objetivo trasladado al **ciberespacio** interconectado, con
tres líneas de actuación: detectar intrusiones y hacerles frente; detectar, reaccionar y recuperarse
de incidentes; y preservar la tríada `[10]`. La relación es de **continencia, no de sustitución**.
**Por qué importa para el TFG:** la dimensión de interconexión es la que hace que el objeto del
trabajo sea un NIDS y no un HIDS. Es la respuesta de una frase si preguntan por qué el marco se
titula «ciberseguridad».

### 5.2 «Usted habla de falsos positivos, pero ¿qué objetivo de seguridad protege realmente su sistema?»
**Retirado de:** 2.2.1.2 (desgloses) y 2.2.1.3 (213 palabras).
**Qué llevar:** el desglose completo —confidencialidad de los datos frente a privacidad; integridad
de los datos frente a integridad del sistema— y el ejemplo que lo hace tangible: una modificación no
autorizada de un fichero de configuración compromete la **integridad de los datos** aunque el
sistema siga funcionando, mientras que un DoS puede dejar intacto cada dato y comprometer la
**integridad del sistema** al impedirle cumplir su función. Más autenticidad («¿es quien dice ser?»)
y responsabilidad («¿a quién se atribuye cada acción?»), con el enganche fuerte: **sin registro
trazable, una alerta pierde buena parte de su utilidad para el analista**, que es la justificación
operativa última de un IDS.
**Por qué importa:** conecta con la celda «Activo protegido» de `3.1` y permite responder por
categoría —`dos` ataca disponibilidad, `probe`/`r2l`/`u2r` atacan confidencialidad e integridad—.

### 5.3 «¿Desde cuándo existe esto? ¿Su trabajo es original o reinventa algo de los años ochenta?»
**Retirado de:** 2.2.2.2 (554 palabras del tramo posterior a Denning) y sus callouts.
**Qué llevar:** la línea temporal completa en cuatro hitos. 1980, Anderson, *Computer Security
Threat Monitoring and Surveillance*: los registros de auditoría, hasta entonces material contable,
pueden explotarse para vigilar amenazas `[2]`. 1987, Denning, IDES: primer marco formal, perfil
estadístico del comportamiento normal de cada sujeto y alarma ante desviación significativa `[3]` —
antecedente directo de la etapa 1 de este trabajo—. Años 90: primeros prototipos y el problema de
**cómo compararlos**, que es lo que produce DARPA 1998-1999, KDD Cup 99 y, por depuración, NSL-KDD.
1999, Snort de Roesch en LISA'99 `[26]`: motor ligero contra reglas legibles, la tradición de las
firmas; después Suricata y Zeek/Bro.
**La respuesta a la pregunta:** el trabajo no reinventa ninguna de las dos tradiciones, las
**encadena** — y la etapa de firmas se diferencia de Snort en que **las reglas no las escribe un
analista, se aprenden de los datos** y se extraen legibles del árbol (`firmas_reglas_54.txt`).
**Cautela que hay que llevar sabida:** `[26]` avala Snort, **no** Suricata ni Zeek —Suricata es de
2009— y la memoria deja esa parte sin aval explícito a propósito. Si el tribunal aprieta en la
atribución, ese es el punto.

### 5.4 «¿Por qué un IDS y no un IPS? ¿No sería más útil bloquear?»
**Retirado de:** 2.2.2.3 (≈195 palabras) y 2.2.2.5 (≈450).
**Qué llevar:** la diferencia no está en cómo detectan, sino en **dónde se colocan y qué hacen con
lo detectado**. El IDS es pasivo, fuera del camino del tráfico (*tap* o *port mirroring*), y su
salida es una alerta; el IPS está en línea y descarta, corta o bloquea. La fila decisiva es el
**coste de un fallo**: en un IDS un falso positivo es ruido en la consola; en un IPS **corta tráfico
legítimo**, y un fallo del propio equipo puede interrumpir el enlace `[25]`. De ahí la práctica
habitual de desplegar el motor primero en modo detección y habilitar el bloqueo solo sobre las
reglas cuya fiabilidad se ha comprobado.
**Cómo cerrar la respuesta con los datos propios:** este sistema tiene un FPR medido del 10,2 % en
54 características (`metricas_hibrido.csv`, `bin_fpr`). **Ese motor no se pone en línea.** La
pregunta se contesta con la propia cifra del capítulo 5, y refuerza que la prioridad de mejora
declarada en `5.4` sea reducir el FPR antes que ganar recall.
**Y el encuadre defensivo:** el H-NIDS es un control **detectivo** dentro de una defensa en capas —
preventivos (cortafuegos, segmentación, control de accesos, cifrado), detectivos y correctivos
(respuesta, contención, recuperación)—. No sustituye a ninguno. Su cometido es **acortar el tiempo
entre que algo atraviesa las barreras preventivas y que alguien se entera**. Sobre ubicación: el
perímetro observa lo que entra y sale; el interior de la red detecta el **movimiento lateral** de
quien ya está dentro y cuyo tráfico nunca cruza el perímetro.
**Cautela:** el enunciado del principio de defensa en profundidad **no tiene cita utilizable** en
esta memoria (`[28]` es irreconstruible y la afirmación se retiró). Enunciarlo oralmente como
doctrina consolidada es correcto; no se le puede colgar una referencia.

### 5.5 «¿Por qué un NIDS y no un HIDS, si dice que U2R es casi invisible en red?»
**Retirado de:** 2.2.3.1 (≈350 palabras, la tabla).
**Qué llevar — es la pregunta más probable del bloque, porque el propio trabajo la invita:** la
respuesta honesta es que **no es una preferencia de diseño, es una consecuencia de los datos**.
NSL-KDD describe conexiones de red y no contiene ningún evento de host —ni logs, ni integridad de
ficheros, ni trazas de llamadas al sistema—, y un dataset de conexiones solo puede entrenar
detección de red. Y a continuación, la tabla completa por si el tribunal quiere el contraste: HIDS ve
un equipo con detalle interno, NIDS ve todo el segmento; el cifrado extremo a extremo apenas afecta
al HIDS (ve los datos ya descifrados) y golpea al NIDS; el punto ciego del HIDS son los equipos sin
agente, el del NIDS la actividad puramente local; y si el equipo cae, el agente HIDS y sus logs son
manipulables mientras que el sensor de red es independiente del objetivo.
**El remate que conviene dar:** son **complementarios, no rivales**, y la invisibilidad de U2R en red
que documenta 2.2.5.2 es precisamente el argumento de por qué una defensa real desplegaría los dos.
Reconocerlo es más fuerte que defender que el NIDS basta.

### 5.6 «Su sistema no ve tráfico cifrado. ¿No queda obsoleto con TLS generalizado?»
**Retirado de:** 2.2.3.4 (≈380 palabras).
**Qué llevar — y este bloque conviene no perderlo, porque la respuesta favorece al trabajo:** con
TLS generalizado, la inspección de *payload* pierde alcance y el sensor ve un flujo opaco. Pero las
características de NSL-KDD son **metadatos y estadísticas de flujo** —duración, bytes por sentido,
banderas, contadores de conexiones al mismo servicio—, que **siguen siendo observables sobre tráfico
cifrado porque no dependen del contenido**. El enfoque adoptado es, en ese sentido, el que envejece
mejor.
Complementos para la misma pregunta: **volumen y velocidad** (muestreo y flujos agregados reducen
carga a costa de resolución, y un ataque de baja intensidad puede desaparecer en el agregado);
**evasión** (fragmentación y solapamiento que explotan diferencias de reensamblado entre sensor y
destino, ofuscación, canal lento por debajo de cualquier umbral, `[34]`); y la advertencia
metodológica de fondo de Sommer y Paxson `[21]`: la detección de intrusiones es un dominio
especialmente hostil para el ML por la variabilidad del tráfico normal, el coste asimétrico de los
errores y la dificultad de obtener datos etiquetados representativos.
**Enlace con lo medido:** la evasión queda **fuera del alcance declarado** por el modelo de adversario
de `3.1` —capacidad limitada a emitir tráfico, acción solo en inferencia, comportamiento estático—,
así que la respuesta correcta no es defender que el sistema resiste evasión, sino que **no se ha
medido y el trabajo lo declara**.

### 5.7 «¿Qué es un IDS híbrido? Porque hay muchos papers que dicen serlo.»
**Retirado de:** ≈140 palabras de 2.2.3.2 (el desarrollo de la crítica a la revisión de 2019). El
núcleo de los cuatro sentidos **se queda en el cuerpo**.
**Qué llevar de más:** que la ambigüedad no es de trabajos aislados sino del área. **La revisión más
citada del campo tampoco taxonomiza lo híbrido**: organiza todo en SIDS y AIDS con gran detalle
—técnicas, familias de algoritmos, datasets, métricas, evasión— y despacha los sistemas híbridos en
**un único párrafo**, bajo «*Hybrid based techniques*», con **una sola obra de ejemplo**, Farid et
al. (2010), que combina Naive Bayes con un árbol de decisión sobre KDD'99. Sin tipos, sin criterio de
orden entre etapas, sin diagrama. Y ese único ejemplo son **dos clasificadores supervisados**, es
decir el sentido (d) y no el (a) `[31]`.
**Por qué es munición y no relleno:** justifica que este TFG **haya tenido que fijar por su cuenta la
definición operativa** de la casilla híbrida. Si el tribunal pregunta «¿por qué se inventa usted una
definición?», la respuesta es que la literatura de referencia no la da.

### 5.8 «¿Su arquitectura es novedosa?» / «¿Por qué en ese orden y no al contrario?»
**No retirado —** 2.2.4.5 se conserva íntegro en su justificación, y Kim et al. `[69]` también. Lo
retirado son ≈200 palabras: la arquitectura interna de Ji et al. `[68]` y de Khraisat et al. `[70]`.
**Qué llevar de lo retirado:** Ji et al., sobre NSL-KDD, tres etapas —extraer patrones del tráfico
para derivar reglas que señalan anomalías, un modelo predictivo que categoriza el tipo de ataque, y
una capa de visualización para validar—; mismo orden lógico que este TFG, distinta primera etapa
(reglas minadas frente a detector *one-class* sobre D1). Khraisat et al., sobre NSL-KDD y ADFA, C5.0
como componente de firmas y *one-class* SVM como componente de anomalías **apilados por un
meta-clasificador** (*stacking*), no en cascada: mismo sentido (a) de híbrido, topología opuesta —
donde aquí hay una puerta dura y secuencial, ellos dejan que un modelo aprendido pondere ambas
señales sobre todo el tráfico.
**La respuesta corta a «¿es novedosa?»:** no, y el trabajo no lo pretende. La cascada anomalías→firmas
tiene precedente desde ADAM (2001) y Tombini et al. (2004). **Lo que aporta este TFG es su
instanciación con modelos de aprendizaje automático y su evaluación sobre un reparto que preserva
ataques no vistos en entrenamiento.**
**Y la respuesta al orden, que sí es propia y está medida:** el orden inverso —firmas primero— tiene
un coste contable. Pasar las 9.711 filas normales de D2 por el clasificador de firmas ya entrenado
condena **6.558 (67,53 %)** en la variante de 54 características y **3.329 (34,28 %)** en la de 122
(`metricas_cascada_invertida.csv`, fila `__global__`). **Y hay que decirlo con la cautela correcta:
eso es una cota inferior de los falsos positivos irrecuperables, no «el FPR de un sistema de
firmas-primero»**, porque en este trabajo `unknown` es alarma (decisión P-5) y lo que cae bajo
umbral no queda exonerado.
**Cautela sobre las fuentes:** Kim et al. y Khraisat et al. se citan **por su resumen** —texto
completo tras muro de pago, sin acceso institucional— y la memoria lo declara. No atribuirles
ninguna cifra en la defensa.

### 5.9 «¿Un dataset de 1998? ¿Y las amenazas de hoy — ransomware, APT?»
**Retirado de:** 2.2.5.3 (≈380 palabras). **Es el bloque retirado más probable de ser preguntado, y
el que conviene llevar mejor preparado, porque su ausencia del cuerpo es justo lo que el tribunal
puede leer como punto ciego.**
**Qué llevar:** los cuatro vectores dominantes de la última década. **Ransomware**: cifrado extorsivo
con exfiltración previa y amenaza de publicación (*doble extorsión*), y el paso de campañas
indiscriminadas a operaciones dirigidas contra organizaciones con alta dependencia operativa de sus
sistemas. **APT**: campañas de larga duración con recursos y objetivo definidos, cuyo rasgo
distintivo es la **permanencia sigilosa** durante meses; su detección depende de identificar
movimiento lateral y comportamiento anómalo de bajo perfil, **no** de bloquear un único evento.
**DDoS de gran escala** apoyado en IoT comprometido, con capacidad agregada varios órdenes de
magnitud por encima de los ataques de finales de los noventa. **Phishing e ingeniería social**, aún
el vector de entrada inicial más frecuente, por explotar al usuario en lugar de a la tecnología.
**Cómo convertirlo en argumento a favor:** la APT es el caso que **más favorece** al diseño de este
trabajo — se detecta por comportamiento anómalo de bajo perfil, que es exactamente lo que hace la
etapa 1, y no por firma de un evento único. Y el DDoS moderno sigue siendo, categorialmente, `dos`.
**Cautela dura, y no se puede olvidar:** **no dar ninguna cifra**. La fuente en que se apoyaba este
apartado (`[37]`, un informe anual de organismo público) nunca se pudo identificar y la atribución se
retiró por decisión expresa. Todo esto se sostiene oralmente como caracterización cualitativa; **una
magnitud publicada citada de memoria en la defensa sería exactamente el error que la memoria evitó
por escrito**.

### 5.10 «Entonces, ¿su taxonomía sigue valiendo?»
**Parcialmente retirado:** la tabla «A favor / En contra» de 2.2.5.4 se retira del cuerpo, pero
**sigue en la memoria**, en `4.2 Base de datos utilizada`. El argumento conceptual se conserva en
2.2.5.4.
**Qué llevar:** dos razones que hay que separar con cuidado, porque mezclarlas debilita la respuesta.
**(1) Lo que caduca son los tipos, no las categorías.** `smurf` es inviable desde que los routers
dejaron de reenviar tráfico dirigido a broadcast; `teardrop` y `land` son fallos de pilas TCP/IP
corregidos hace décadas. Pero las **cuatro conductas** siguen describiendo las fases de una intrusión
moderna, y la correspondencia con los marcos de uso corriente es explícita: *Reconnaissance* ↔ Probe,
*Initial Access* ↔ R2L, *Privilege Escalation* ↔ U2R, *Impact* ↔ DoS, tanto en la *cyber kill chain*
como en MITRE ATT&CK `[38]`. **(2) La limitación es de representatividad, no de validez
conceptual.** Las críticas clásicas —los sesgos de la simulación DARPA señalados por McHugh, los
registros duplicados que motivaron NSL-KDD en Tavallaee et al.— apuntan a la **distribución** del
tráfico y a la fiabilidad de las **métricas absolutas**, `[22]` `[23]`, **no** a que la clasificación
en cuatro conductas sea incorrecta.
**Cautela:** la atribución concreta a McHugh (2000) no se ha podido contrastar sobre texto completo;
si hay que sostenerla en la defensa, atribuirla a Tavallaee et al. (2009), que resume esas críticas y
sí es accesible.

---

## 6. Avisos para quien ejecute el recorte

1. **No tocar 2.2.4.3, 2.2.4.4, la justificación de 2.2.4.5, 2.2.3.5, 2.2.5.2 ni el apartado
   «Antecedentes de la combinación anomalías + firmas» de 2.2.3.2.** Cada uno tiene al menos una
   remisión entrante verificada, y tres de ellas están redactadas en la forma «esto está allí y aquí
   no se repite», que no avisa al romperse.
2. **Dos deduplicaciones de este informe afectan a ficheros fuera de 2.2 y no debe hacerlas quien
   recorte 2.2**: la tabla «A favor / En contra» de 2.2.5.4 se retira **a condición** de que `4.2`
   conserve «Por qué se eligió NSL-KDD»; y el argumento de la gradación de visibilidad reaparece en
   `4.2` («Esta correspondencia entre grupo de características y tipo de ataque detectable no es
   anecdótica»), donde la sede única debe ser 2.2.5.2, no lo contrario.
3. **Las 1.586 palabras de callouts de gestión no son objeto de este recorte.** Salen al volcar al
   `.docx`, y varias de ellas registran decisiones de Francisco del 2026-08-18 que deben sobrevivir
   en el vault mientras las verificaciones sigan pendientes. No borrarlas para «ganar palabras».
4. **La Figura 2.5 (`fig-nids-bloques.png`) se queda.** Es la única figura de todo el bloque 2.2 y su
   pie está numerado en la serie contigua `2.1`–`2.5`: retirarla rompería la numeración del capítulo.
