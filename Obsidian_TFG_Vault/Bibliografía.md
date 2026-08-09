---
titulo: "Bibliografía"
numero: "-"
estado: borrador
docx_ref: "Desarrollo (referencias)"
---

# Bibliografía

> [!info] Tabla de *staging* — auditada el 2026-08-09 (T15)
> Este fichero **no es la bibliografía final**: es la tabla de trabajo desde la que Francisco hará
> el pase mecánico a Zotero en formato IEEE. Cada entrada lleva su **cita completa**, su **DOI o
> URL estable** y su **nivel de fiabilidad** a la vista, para que no se cuele una fuente de nivel
> 2-3 sosteniendo una afirmación fuerte.
>
> **Niveles:** **1** revisado por pares con DOI · norma o estándar · organismo oficial ·
> documentación oficial · libro con ISBN de editorial reconocida — cita sin reservas.
> **2** preprint, tesis, informe técnico de empresa, *white paper* — admisible declarando la
> reserva. **3** blog, prensa, web sin autor ni fecha, copia no autorizada — **no sostiene nada**.
>
> Informe de la auditoría: [[Auditoría de Bibliografía]].
> **La numeración no se reordena**: los `[n]` están usados en las notas. `[9]` queda retirada y su
> número **no se reutiliza**.

| `[n]` | Cita completa | DOI / URL estable | Nivel | Dónde se usa |
|---|---|---|---|---|
| [1] | Instituto Nacional de Ciberseguridad (INCIBE), «INCIBE presenta su balance de ciberseguridad 2024 con más de 97.000 incidentes gestionados», nota de prensa, 20 de marzo de 2025. **Dato citado:** 97.348 incidentes gestionados en 2024, un 16,6 % más que en 2023; 65.808 (67,6 %) afectaron a la ciudadanía y 31.540 (32,4 %) a empresas; 7.470 intrusiones o intentos de acceso no autorizado; 42.136 casos de *malware*, de ellos 357 de *ransomware* | https://www.incibe.es/incibe/sala-de-prensa/incibe-presenta-su-balance-de-ciberseguridad-2024-con-mas-de-97000-incidentes | **1** | `1.1 Motivación` |
| [2] | J. P. Anderson, *Computer Security Threat Monitoring and Surveillance*. Fort Washington, PA: James P. Anderson Co. (Box 42, Fort Washington, PA 19034), contrato 79F296400, 26 de febrero de 1980 (revisado el 15 de abril de 1980) | http://csrc.nist.gov/publications/history/ande80.pdf | **2** | `1.2 Preliminares` |
| [3] | D. E. Denning, «An Intrusion-Detection Model», *IEEE Transactions on Software Engineering*, vol. SE-13, n.º 2, pp. 222-232, feb. 1987 | 10.1109/TSE.1987.232894 | **1** | `1.2 Preliminares` |
| [4] | C. Chio y D. Freeman, *Machine Learning and Security: Protecting Systems with Data and Algorithms*, 1.ª ed. Sebastopol, CA: O'Reilly Media, 2018, 383 pp. ISBN 978-1-4919-7990-7 | ISBN 978-1-4919-7990-7 (sin DOI; sitio oficial del libro: https://mlsec.net/) | **1** | `2.1.1 Introducción al ML` |
| [5] | A. Géron, *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow: Concepts, Tools, and Techniques to Build Intelligent Systems*, 2.ª ed. Sebastopol, CA: O'Reilly Media, 2019. ISBN 978-1-492-03264-9 | https://www.oreilly.com/library/view/hands-on-machine-learning/9781492032632/ | **1** | `2.1.1 Introducción al ML`, `2.1.3 Ciclo de vida de un proyecto ML` |
| [6] | I. Goodfellow, Y. Bengio y A. Courville, *Deep Learning*. Cambridge, MA: MIT Press, 2016. ISBN 978-0-262-03561-3 | https://www.deeplearningbook.org/ | **1** | `2.1.2 Tipos de ML` |
| [7] | K. P. Murphy, *Machine Learning: A Probabilistic Perspective*. Cambridge, MA: MIT Press, 2012. ISBN 978-0-262-01802-9 | https://dl.acm.org/doi/book/10.5555/2380985 | **1** | `2.1.2 Tipos de ML` |
| [8] | W. Stallings y L. Brown, *Computer Security: Principles and Practice*, 4.ª ed. Pearson, 2018. ISBN 978-0-13-479410-5 | https://www.pearson.com/en-us/subject-catalog/p/computer-security-principles-and-practice/P200000010333 | **1** | `2.2.1 Introducción a la ciberseguridad` (definición de *Computer Security* y conceptos añadidos) |
| ~~[9]~~ | **RETIRADA el 2026-08-09 — fundida en [8]** (baja autorizada por Francisco el 2026-08-06) | — | ~~3~~ | ver aviso |
| [10] | Centro Criptológico Nacional (CCN-CERT), *Guía de Seguridad de las TIC CCN-STIC-401: Glosario y Abreviaturas*, entrada «ciberseguridad» | https://www.ccn-cert.cni.es/publico/seriesCCN-STIC/series/400-Guias_Generales/401-glosario_abreviaturas/index.html?n=189.html | **1** | `2.2.1 Introducción a la ciberseguridad` |

## Avisos y reservas por entrada

> [!warning] [9] — retirada de la numeración, fundida en [8]
> Era `students.aiu.edu/.../j5V2a3_Computer_Security_Principles.pdf`: **copia no autorizada del
> mismo libro de Stallings que ya es [8]**, alojada en un dominio de terceros, sin garantía de
> integridad → **nivel 3**. Comprobado el 2026-08-09: el enlace **ya ni siquiera resuelve en
> abierto** (302 a `aiu.edu/securelogin.html`), así que tampoco era una URL estable.
> **Su número no se reutiliza** para no romper los `[n]` de las notas.
> **Acción pendiente, NO ejecutada por el researcher:** `2.2.1 Introducción a la
> ciberseguridad.md:32` sigue citando `[9]`; hay que **repuntarla a `[8]`**. Es una edición en una
> nota de la memoria y corresponde al `redactor-tfg` o a Francisco.

> [!warning] [8] — edición sin confirmar
> El libro se citaba **sin autor completo, sin año y sin editorial**. Completado con los
> metadatos verificados de la 4.ª edición (Pearson, 2018, ISBN 978-0-13-479410-5), que es la más
> difundida. **Existe una 5.ª edición: Pearson, 2023, ISBN impreso 978-0-13-809167-5**
> (e-book 978-0-13-809171-2). La definición citada en `2.2.1` (la de *computer security* tomada
> del NIST) aparece en el capítulo 1 de **todas** las ediciones, así que el texto no permite
> deducir cuál se usó, y la copia de [9] ya no es accesible para comprobarlo.
> **Francisco debe confirmar la edición que tiene delante antes del pase a Zotero.**
> Coautor añadido: **Lawrie Brown**, que faltaba.

> [!note] [2] — nivel 2, y qué sostiene exactamente
> Es un **informe técnico de empresa** (James P. Anderson Co.), no una publicación revisada por
> pares: **nivel 2**. Se cita como **fuente primaria histórica** y la copia enlazada la aloja el
> **NIST CSRC**, lo que da garantía de integridad. Portada verificada el 2026-08-09: título,
> contrato 79F296400, 26-02-1980 y revisión de 15-04-1980.
> **Reserva:** la frase de `1.2 Preliminares` «este informe se considera el punto de partida para
> los IDS» es una afirmación *sobre* el informe, que el propio informe no puede sostener.
> Necesita un aval de nivel 1 (una revisión del área). **Propuesta, no ejecutada.**

> [!note] [1] — sustituida (baja autorizada el 2026-08-06)
> Antes era `channelpartner.es` (**prensa sectorial, nivel 3**) sosteniendo una cifra de
> ciberataques. Sustituida por la **nota de prensa oficial de INCIBE** sobre el *Balance de
> ciberseguridad 2024* (nivel 1), con el dato exacto ya recogido en la tabla.
> **Reserva importante:** INCIBE da la **magnitud del fenómeno**, no los **nombres propios**
> (Santander, Telefónica, Iberdrola, UCM) que hoy aparecen en `1.1 Motivación:12`. Con esta
> fuente, la frase debe reformularse hacia la cifra agregada. **Propuesta, no ejecutada:** es
> edición de una nota de la memoria.

> [!note] [10] — organismo oficial, URL con protección anti-bot
> Nivel 1 por emisor (Centro Criptológico Nacional). El 2026-08-09 la URL devuelve **403/503 a
> cualquier acceso automático** (`ccn-cert.cni.es` filtra herramientas), igual que el espejo
> docente de la UPM. **No es un enlace roto**: es verificable a mano desde un navegador.
> **Sin verificar:** la **versión y la fecha** de la guía. Antes del pase a Zotero conviene citar
> la guía completa («CCN-STIC-401 Glosario y Abreviaturas», con su versión) en lugar del
> enlace profundo al término, que es frágil.

> [!warning] [6] — posible atribución equivocada, detectada de paso
> En `2.1.2 Tipos de ML.md:30` y `:64` se atribuyen a **Goodfellow et al.** dos listas
> (k-NN / regresión lineal / SVM / árboles / redes neuronales, y K-Means / DBSCAN / HCA /
> One-class SVM / Isolation Forest / PCA / Kernel PCA / LLE / t-SNE / Apriori / **Eclat**). Esas
> listas son las del **capítulo 1 de Géron [5]**; *Deep Learning* no trata Eclat, Apriori ni
> Isolation Forest. **Propuesta, no ejecutada:** repuntar esas dos citas a `[5]`. No es una baja
> de bibliografía, es una corrección de puntero en una nota de la memoria.
