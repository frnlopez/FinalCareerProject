# Bloque A — Preliminares + Capítulo 1 (Introducción) + Capítulo 3 (Diseño del sistema)

**Veredicto del bloque:** el capítulo 1 en el limpio es una versión temprana y notablemente más pobre
que la actualizada: falta la Sinopsis entera, el Objetivo pasa de 9 objetivos específicos con
criterio de cumplimiento a 6 viñetas sueltas sin criterio, y la cifra de la Motivación está
desactualizada (dato viejo sin fuente frente al dato INCIBE 2024 con cita). El capítulo 3 es donde
más pesa la diferencia: el limpio conserva la tabla de requisitos y el modelo de amenaza (dimensiones
del adversario), pero **le faltan íntegras dos secciones que el propio índice anuncia** —"Por qué una
cascada, y en este orden" (3.2.2) y "De dónde sale la capacidad de detectar lo desconocido" (3.2.3)—,
que son las que sostienen con datos (medición contrafactual, FPR comparado) la decisión arquitectónica
central del trabajo. También falta la justificación de por qué no se corre un experimento adversario.
Preliminares (portada, resumen, TDC) está intencionadamente en blanco (plantilla), acorde con las
notas de Francisco, y no se reporta como falta.

---

### [B] Objetivo - los 9 objetivos específicos con criterio de cumplimiento no llegaron al limpio
**Que pasa:** El limpio conserva el objetivo general y una lista de 6 viñetas sin numerar ni criterio.
La versión actualizada desagrega el objetivo general en **9 objetivos específicos**, cada uno con un
**criterio de cumplimiento verificable** y su remisión al capítulo/sección donde se satisface, además
de una tabla de las dos etapas (paradigma / datos / función) y un párrafo de "Alcance" que declara
explícitamente que el sistema es offline sobre NSL-KDD, sin despliegue en red real.
**Por qué importa:** Los criterios de cumplimiento son lo que permite verificar objetivo por objetivo
sin apelar al juicio del autor — es la respuesta directa a la nota de Francisco de que el resumen de
cada bloque «es excesivamente escueto» y pide «una propuesta más completa» (`mis-apuntes-del-informe.md`).
**Donde encaja en el limpio:** sección "Objetivo", justo después de "***Objetivos específicos***" y
sus seis guiones actuales.
**Material:** actualizado, sección "## Objetivo" → "### Objetivo general" (tabla de las dos etapas y
párrafo "Alcance") y "### Objetivos específicos" (los 9 puntos numerados con "*Criterio:*").

---

### [B][CIFRA] Arquitectura del sistema - falta entera "Por qué una cascada, y en este orden" (3.2.2)
**Que pasa:** El índice del limpio anuncia 3.2.2 "Por qué una cascada, y en este orden" y 3.2.3 "De
dónde sale la capacidad de detectar lo desconocido", pero el cuerpo salta de "Las dos etapas"
directamente a "Metodología de funcionamiento del sistema": las dos secciones no están escritas.
La actualizada sí las tiene, con: (1) la tabla de tres razones (Diseño / Cobertura / *Semantic gap*)
para poner las anomalías delante; (2) el contraste con el "antagonista directo" (firmas-primero sobre
el mismo dataset); (3) la **medición contrafactual de la cascada invertida** —6.558 filas normales
condenadas (67,53 %) en la variante de 54 características y 3.329 (34,28 %) en la de 122—, con la
advertencia de que es una cota inferior, no un FPR; (4) el coste del orden elegido, declarado: FPR del
híbrido 10,2 %/8,5 % (54/122 características) frente a 2,7 %/2,6 % del baseline monolítico; y (5) la
divergencia deliberada con ADAM (que sí puede exonerar tráfico, aquí prohibido por diseño H-5/P-5).
**Por qué importa:** Es el argumento con datos que sostiene la decisión de diseño central del trabajo
(por qué anomalías→firmas y no al revés); sin él, la arquitectura queda afirmada pero no justificada
con evidencia, y las cifras de FPR del capítulo 5 aparecen sin el contraste que las hace legibles.
**Donde encaja en el limpio:** entre "### Las dos etapas" y "## Metodología de funcionamiento del
sistema" (el índice ya reserva el hueco con "3.2.2" y "3.2.3").
**Material:** actualizado, "### Por qué una cascada, y en este orden" y "### De dónde sale la capacidad
de detectar lo desconocido", bajo "## Arquitectura del sistema".

---

### [B] Modelo de amenaza - falta la justificación de por qué NO se hace un experimento adversario
**Que pasa:** El limpio conserva la tabla de las seis dimensiones del adversario (activo protegido,
objetivo, conocimiento, capacidad, momento, adaptatividad) pero no incluye el desarrollo posterior: el
subapartado "Por qué no se realiza un experimento adversario", con tres razones encadenadas y
verificables sobre el propio NSL-KDD (no hay tráfico vivo contra el que adaptarse, no hay canal de
realimentación, la representación no admite una perturbación realizable), la cita del pitfall P10 de
Arp et al. [18], y el párrafo "Alcance de esta exclusión" que declara el límite en 6.1 y lo enlaza con
6.2 Líneas futuras.
**Por qué importa:** Sin esto, la ausencia de evaluación adversaria en el trabajo queda sin defender —
un lector puede leerla como una carencia no declarada en vez de una decisión metodológica razonada, y
el límite 3 de "6.1 Conclusiones" pierde el desarrollo del que depende.
**Donde encaja en el limpio:** justo después de la tabla de "Modelo de amenaza", antes de "##
Arquitectura del sistema".
**Material:** actualizado, "#### 3.1.5.2 Por qué no se realiza un experimento adversario" (bajo "###
Modelo de amenaza").

---

### [R] Conclusiones del capítulo 3 - falta la viñeta de divergencia declarada con ADAM
**Que pasa:** La lista de decisiones de diseño del cierre del capítulo, en el limpio, tiene 4 viñetas;
la actualizada tiene 5, con una viñeta adicional que declara la divergencia con ADAM (la etapa 2 no
puede exonerar tráfico, solo cualificar la alarma o etiquetarla `unknown`).
**Por qué importa:** Complementa la sección "3.2.2" que falta (ver entrada de arriba); si esa sección
se traslada, esta viñeta debería viajar con ella para que el cierre del capítulo la recoja.
**Donde encaja en el limpio:** en "## Conclusiones del capítulo", tras la primera viñeta sobre la
arquitectura híbrida en cascada.
**Material:** actualizado, "## Conclusiones del capítulo", segunda viñeta ("Una divergencia declarada
con el antecedente más próximo...").

---

### [R] Modelo de detección de anomalías - falta "El coste del paradigma"
**Que pasa:** El limpio cierra la sección de anomalías en "Papel en la cascada". La actualizada añade
un apartado "El coste del paradigma", que explica —citando a Sommer y Paxson [21]— por qué modelar solo
la normalidad exige "un modelo *perfecto* de normalidad" y encadena esa idea con el FPR observado en el
sistema (10,2 % / 8,5 % según variante).
**Por qué importa:** Es la contrapartida honesta de la virtud del planteamiento *one-class*: declara el
precio del diseño antes de que aparezca como sorpresa en los resultados del capítulo 5.
**Donde encaja en el limpio:** al final de "## Modelo de detección de anomalías", tras "### Papel en la
cascada".
**Material:** actualizado, "### El coste del paradigma", bajo "## Modelo de detección de anomalías".

---

### [R] Algoritmos candidatos (firmas) - falta "Por qué familias clásicas y no una arquitectura tabular profunda"
**Que pasa:** El limpio compara los cuatro algoritmos candidatos de la etapa de firmas con una tabla
breve y nada más. La actualizada añade un subapartado extenso que justifica no usar arquitecturas
tabulares profundas: literatura empírica (McElfresh et al. [42], tabla de 5 criterios que favorecen
árboles/boosting sobre D3), el contraste pareado RandomForest vs HistGradientBoosting (8 de 10
semillas en `f1_macro`, con la salvedad de que las bandas se solapan), el coste computacional
(entrenamiento vs inferencia, con el orden invertido según variante) y el límite objetivo de TabPFN
(10.000 muestras vs las 58.630 de D3).
**Por qué importa:** Es la respuesta anticipada a la pregunta obvia («¿por qué no una red neuronal
tabular moderna?»); sin ella, la elección de algoritmos clásicos parece una simplificación no
argumentada.
**Donde encaja en el limpio:** dentro de "### Algoritmos candidatos" (Modelo de detección basado en
firmas), tras la tabla de los cuatro algoritmos.
**Material:** actualizado, "#### Por qué familias clásicas y no una arquitectura tabular profunda",
bajo "### Algoritmos candidatos" de "## Modelo de detección basado en firmas".

---

### [C][CIFRA] Motivación - la cifra que abre el párrafo está desactualizada y sin fuente verificable
**Que pasa:** El limpio ilustra la vulnerabilidad de instituciones españolas nombrando cuatro casos
concretos (Santander, Telefónica, Iberdrola, Universidad Complutense) sin cifra ni fecha. La
actualizada sustituye ese ejemplo por un dato oficial y trazable: en 2024 el INCIBE gestionó **97.348
incidentes de ciberseguridad, un 16,6 % más que el año anterior [1]**.
**Por qué importa:** No es solo una reformulación de estilo: el limpio afirma un hecho concreto (los
cuatro nombres) que la versión actual ya no sostiene como argumento — lo sustituyó por una cifra
oficial y citada. Publicar la versión antigua sin la cifra sería presentar un argumento más débil y sin
respaldo verificable donde ya existe uno mejor.
**Donde encaja en el limpio:** segundo párrafo de "## Motivación" ("La posibilidad de sufrir estos
problemas no se limita a grandes corporaciones...").
**Material:** actualizado, "## Motivación", párrafo 2: "La magnitud del fenómeno en España queda
reflejada en los datos oficiales: durante 2024, el Instituto Nacional de Ciberseguridad (INCIBE)
gestionó 97.348 incidentes de ciberseguridad, un 16,6 % más que el año anterior [1]."

---

### [R] Introducción - falta la Sinopsis del capítulo 1
**Que pasa:** La actualizada abre el capítulo 1 con un apartado "## Sinopsis" que resume en cinco
párrafos el contenido del capítulo (motivación, preliminares, objetivo con sus 5 bloques temáticos y
estructura). El limpio no tiene esta sección; empieza directamente en "## Motivación".
**Por qué importa:** Es exactamente el tipo de resumen de apertura que Francisco pidió reforzar
("ese resumen de cada capítulo es excesivamente escueto. Ofrecer una propuesta más completa",
`mis-apuntes-del-informe.md`); cada capítulo de la actualizada arranca con su Sinopsis y el limpio, en
este bloque, se queda sin la del capítulo 1.
**Donde encaja en el limpio:** inmediatamente después del título "# Introducción" y antes de
"## Motivación".
**Material:** actualizado, "## Sinopsis" bajo "# Introducción" (párrafo inicial: "Este primer capítulo
sitúa el proyecto en su contexto...").

---

### [D] Preliminares (portada, resumen ES/EN, agradecimientos, TDC) - vacío en ambos, no es una falta
**Que pasa:** La portada, el resumen en español/inglés, los agradecimientos y la tabla de contenido
del limpio siguen siendo la plantilla sin rellenar ("El resumen debe ser una breve descripción...",
"Palabras y frases claves que describen..."). No hay equivalente en el volcado del vault porque esos
campos no son notas de la memoria: los rellena Francisco directamente en Word.
**Por qué importa:** Se deja constancia de que esto NO es una ausencia respecto al vault — es contenido
pendiente que el propio Francisco señaló como abierto ("RESUMEN del informe no escrito. Ofrecer
propuesta. [...] Título del proyecto también falta.", `mis-apuntes-del-informe.md`) y que no tiene
fuente en Markdown.
**Donde encaja en el limpio:** portada y páginas de resumen, antes de "# Contenido".
**Material:** no aplica — no hay contraparte en el vault; es trabajo directo de Francisco en Word.
