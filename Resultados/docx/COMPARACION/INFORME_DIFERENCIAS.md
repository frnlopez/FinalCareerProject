# Diferencias entre el Word en limpio y la memoria actualizada

**Limpio:** `Proyecto_Fin_de_Grado-FJLM-2026.docx` (2.364 lineas convertidas) · **Actualizado:** volcado del vault del 2026-08-22 15:44, commit `fd089cc`-sucio (5.017 lineas)

Comparacion a nivel de CONTENIDO Y ARGUMENTO, no palabra por palabra. Ninguno de los dos documentos ha sido modificado.

## Leyenda

| | Gravedad | Significado |
|---|---|---|
| **C** | CONTRADICE | esta en el limpio, pero afirma algo distinto de lo actualizado |
| **B** | FALTA-BLOQUEANTE | sin esto, lo que ya esta en el limpio no se entiende o queda sin justificar |
| **R** | FALTA-RECOMENDABLE | complementa lo que ya hay |
| **P** | FALTA-PRESCINDIBLE | se puede omitir sin dano real |
| **D** | SOLO-EN-DOCX | esta en el limpio y el actualizado ya no lo tiene (puede ser borrado deliberado) |

Flags ortogonales: **[PROFESOR]** peticion trazable del profesor o de tu propia revision · **[CIFRA]** hay un numero en juego.

## Recuento

| C | B | R | P | D | TOTAL |
|---|---|---|---|---|---|
| 3 | 23 | 19 | 11 | 7 | 63 |

Con flag [PROFESOR]: **9** · con flag [CIFRA]: **7**

## Indice por gravedad

| # | Grav | Flags | Bloque | Diferencia |
|---|---|---|---|---|
| 1 | **C** | CIFRA | A | Motivación - la cifra que abre el párrafo está desactualizada y sin fuente verificable |
| 2 | **C** | CIFRA | E | 5.1 Resultados del modelo de detección de anomalías - el "ocho veces menor" del coste de IsolationForest está obsoleto |
| 3 | **C** | CIFRA | E | 5.1 Resultados del modelo de detección de anomalías - tabla de tiempos de un solo valor por algoritmo, ya sustituida por dos columnas |
| 4 | **B** |  | A | Modelo de amenaza - falta la justificación de por qué NO se hace un experimento adversario |
| 5 | **B** |  | A | Objetivo - los 9 objetivos específicos con criterio de cumplimiento no llegaron al limpio |
| 6 | **B** | CIFRA | A | Arquitectura del sistema - falta entera "Por qué una cascada, y en este orden" (3.2.2) |
| 7 | **B** |  | B | 2.1.5 - Falta el aparato de promediado multiclase (macro/ponderado) y la matriz multiclase |
| 8 | **B** |  | B | 2.1.6 - Ausencia total de "Metodologías y buenas prácticas" |
| 9 | **B** | PROFESOR | B | 2.1.3 - Confusión cross-validation / N-fold / desviación típica sin resolver |
| 10 | **B** |  | C | 2.2.3 — Falta la delimitación del término «híbrido» en cuatro sentidos |
| 11 | **B** |  | C | 2.3.3 — Falta prácticamente todo el desarrollo del modelo de amenaza (P10) salvo el enunciado mínimo |
| 12 | **B** | PROFESOR | C | 2.3 — El bloque de IA está reducido a un resumen mínimo frente al vault actual |
| 13 | **B** | PROFESOR | C | 2.3.1.3 — Falta la justificación de "por qué ML clásico y no Deep Learning" |
| 14 | **B** |  | D | 4.2.1 - Falta el aviso KDDTest-21 / la vacuna contra el «14» de Tavallaee |
| 15 | **B** | PROFESOR | D | 4.3.7 - Falta la declaración de que 3 decisiones del sistema se tomaron mirando D2 (data snooping) |
| 16 | **B** |  | E | 5.1 Resultados del modelo de detección de anomalías - falta la explicación del exceso de FPR como desplazamiento entre particiones (T2) |
| 17 | **B** |  | E | 5.1 y 5.2 - falta la declaración de que tres decisiones del sistema se calibraron mirando D2 (data snooping admitido) |
| 18 | **B** |  | E | 5.2 Resultados del modelo de detección basado en firmas - falta la subsección entera "Robustez frente a la semilla" (T4) |
| 19 | **B** |  | E | 5.4 Conclusiones del capítulo - falta entera la comparación con la literatura publicada (C1-C7, siete baselines, Hindy et al.) |
| 20 | **B** |  | E | 5.4 Conclusiones del capítulo - falta la proyección a prevalencia realista (falacia de la tasa base) |
| 21 | **B** | PROFESOR | E | 5.0 Protocolo de evaluación - la sección entera no llegó al limpio |
| 22 | **B** |  | F | 6.1 Conclusiones - falta el desglose de los 9 objetivos específicos en 4 bloques (A-D) |
| 23 | **B** |  | F | 6.1 Conclusiones - falta entera la sección "Límites de lo medible con NSL-KDD" (6.1.4) |
| 24 | **B** |  | F | 6.2 Líneas futuras - toda la sección está vacía en el limpio (solo el título) |
| 25 | **B** |  | F | Apéndices - falta entero `A.2 Métricas de desempeño` |
| 26 | **B** | PROFESOR | F | Apéndices - falta entero `A.3 Ficha del sistema` |
| 27 | **R** |  | A | Algoritmos candidatos (firmas) - falta "Por qué familias clásicas y no una arquitectura tabular profunda" |
| 28 | **R** |  | A | Conclusiones del capítulo 3 - falta la viñeta de divergencia declarada con ADAM |
| 29 | **R** |  | A | Introducción - falta la Sinopsis del capítulo 1 |
| 30 | **R** |  | A | Modelo de detección de anomalías - falta "El coste del paradigma" |
| 31 | **R** |  | B | 2.1.2 - Falta la aclaración de que el autoencoder es auto-supervisado en mecanismo pero one-class en régimen |
| 32 | **R** | PROFESOR | B | 2.1.1 - Falta la aclaración explícita de que la IA no se define aquí |
| 33 | **R** |  | C | 2.2.2 — Falta el recorrido histórico del IDS (Anderson 1980, Denning/IDES 1987, Snort 1999, análisis con estado) y la comparación IDS vs. IPS |
| 34 | **R** |  | C | 2.2.3 — Faltan los antecedentes históricos de la combinación anomalías+firmas y los tres trabajos comparables sobre NSL-KDD |
| 35 | **R** |  | C | 2.2.5 — Falta la tabla de gradación de visibilidad en red y la sección "Vigencia de una taxonomía de 1998" |
| 36 | **R** |  | C | 2.3.2.5 — Falta el panorama de datasets públicos para NIDS |
| 37 | **R** | CIFRA | C | 2.2.3 — Falta la sección de limitaciones transversales de los NIDS |
| 38 | **R** | PROFESOR | C | 2.3.2 — Falta el desarrollo de adversarial ML (evasión/envenenamiento) y "el modelo que no sabe decir no lo sé" |
| 39 | **R** | PROFESOR | C | 2.3.3 — Falta la explicabilidad como requisito no opcional en seguridad |
| 40 | **R** |  | D | 4.3.3 - Falta el reencuadre de la selección de características como poda del one-hot de `service` |
| 41 | **R** | CIFRA | D | 4.2.1 - Falta el detalle del reparto D2 por dos denominadores distintos (ataques vs D2 completo) |
| 42 | **R** |  | E | 5.2 Resultados del modelo de detección basado en firmas - falta el análisis de la inversión probe/r2l frente a la jerarquía predicha en 2.2.5.2 |
| 43 | **R** |  | E | 5.3 Resultados del sistema híbrido - falta la explicación en tres partes del 13,4 % de enrutado a "unknown" |
| 44 | **R** |  | E | 5.4 Conclusiones del capítulo - falta la sección sobre los límites de la latencia publicada |
| 45 | **R** |  | F | Apéndice A.1 (Columnas del dataset) - subtítulos con numeración A.1.1-A.1.5 ausentes |
| 46 | **P** |  | B | 2.1.4 - Falta mencionar SVM en la lista de algoritmos supervisados representativos |
| 47 | **P** |  | B | 2.1.4 - Faltan las citas bibliográficas de Isolation Forest y LOF |
| 48 | **P** |  | C | 2.2.1 — Falta la distinción explícita "seguridad informática frente a ciberseguridad" como relación de continencia |
| 49 | **P** |  | C | 2.3.2.1 — Falta el desarrollo de malware, anti-phishing/anti-spam y UEBA como casos de uso |
| 50 | **P** |  | C | 2.3.3 — Faltan privacidad/RGPD, marco regulatorio (AI Act/NIS2) y la tabla de síntesis de límites |
| 51 | **P** |  | D | 4.3.4 - Falta la limitación declarada de SMOTE sobre variables dummy (valores fraccionarios) |
| 52 | **P** |  | D | 4.4.3 - Falta la distinción entre AUC-ROC de validación (§4.4) y AUC-ROC de test (§5.1.2) |
| 53 | **P** | CIFRA | D | 4.3.1 - Falta el detalle KS con dos poblaciones distintas ((A) D1 vs D2 completo, (B) D1 vs D2 solo normales) |
| 54 | **P** |  | E | 5.2 Resultados del modelo de detección basado en firmas - precisión del soporte de u2r (37 en el subconjunto conocido vs 200 en D2 completo vs 52 en D3) |
| 55 | **P** |  | E | 5.4 Conclusiones del capítulo - falta la nota de que el eje de balanceo SMOTE-vs-class_weight se declara "no establecido" (T4) |
| 56 | **P** |  | F | Bibliografía - el limpio tiene 11 entradas frente a las ~78 numeradas del proyecto |
| 57 | **D** |  | A | Preliminares (portada, resumen ES/EN, agradecimientos, TDC) - vacío en ambos, no es una falta |
| 58 | **D** |  | B | 2.1.3 - El limpio conserva el desarrollo íntegro del ciclo de vida en cinco fases que el actualizado comprimió a remisiones |
| 59 | **D** |  | C | Ninguna diferencia SOLO-EN-DOCX detectada en este bloque |
| 60 | **D** |  | D | 4.5.3 - El limpio no tiene el análisis fino de por qué KNN e HistGradientBoosting coinciden o casi coinciden entre el mini-experimento de 4.3.4 y el GridSearchCV final |
| 61 | **D** |  | D | Firmas - El limpio omite correctamente hiperparámetros de detalle de las rejillas de búsqueda |
| 62 | **D** |  | F | 6.1 Conclusiones - el limpio detalla f1_macro 0.909→0.472 en "Validación de la tesis"; el actualizado lo remite a 5.3 |
| 63 | **D** |  | F | Apéndices - el limpio trae texto de plantilla de Word sin desarrollar al final del fichero |

---

# Detalle por bloque


---

# BLOQUE A — Preliminares + Cap.1 Introducción + Cap.3 Diseño

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


---

# BLOQUE B — Cap.2.1 Machine Learning

# Comparación — Capítulo 2, bloque 2.1 Machine Learning

**Veredicto del bloque:** el limpio corresponde a un estado de 2.1 anterior a la reestructuración
en subapartados numerados (2.1.1.1…, 2.1.6…) que trae el actualizado, y sobre todo anterior a la
sección **2.1.6 Metodologías y buenas prácticas**, que en el limpio **no existe en absoluto** — ni
como sección propia ni troceada en otra parte del capítulo 2. Es la ausencia más grave del bloque:
2.1.6 es, según el propio informe de recorte (`Recorte capítulo 2 - bloque 2.1.md`), la nota que
recibe las 8 remisiones entrantes desde los capítulos 3-6, y el recorte deliberado de esa nota fue
mínimo (CRISP-DM se comprimió; validación cruzada, fuga de información y reproducibilidad se
dejaron **sin recortar**). El resto del bloque (2.1.1-2.1.5) sí está presente en el limpio en
sustancia, con contenido equivalente aunque con distinta redacción y sin la subdivisión numerada;
las ausencias ahí son en su mayoría el recorte deliberado por volumen ya documentado, y no se
listan como falta. Dos de los cuatro puntos que el profesor comentó sobre 2.1 siguen sin resolverse
en el limpio.

---

## [B] 2.1.6 - Ausencia total de "Metodologías y buenas prácticas"

**Que pasa:** La sección 2.1.6 entera —CRISP-DM, separación train/validación/test y la "línea roja
del test", el perímetro anti-fuga, la declaración de las tres decisiones tomadas mirando D2,
validación cruzada estratificada, búsqueda de hiperparámetros, fuga de información (*data
leakage*), por qué el accuracy miente bajo desbalance, reproducibilidad (semilla 42 y barrido de
semillas) y la sobreestimación de la CV frente al test (dataset shift, clases nunca vistas,
*semantic gap*)— no aparece en ningún punto del capítulo 2 del limpio. Se ha verificado por
búsqueda de términos («CRISP-DM», «línea roja», «data snooping», «semantic gap», «perímetro
anti-fuga») en todo el documento: cero apariciones fuera de los capítulos 4-5, donde el limpio sí
explica varias de estas ideas pero de forma puntual y aplicada (p. ej. la fuga de información se
menciona al hilo de SMOTE en 4.3.4, y la reproducibilidad al hilo de las librerías), nunca como
marco teórico general.

**Por qué importa:** Es la sección que el resto de la memoria consume de verdad. En el actualizado
recibe remisiones explícitas desde 3.2, 3.3 (×2), 3.6, 4.1, 4.3 (×2) y 6.1. Si esas remisiones
llegan a pasarse al limpio sin que exista el destino, quedan colgando; y aunque no se pasen, el
lector del capítulo 2 se queda sin el fundamento teórico de conceptos que el capítulo 4 y el 5 dan
por sabidos: qué es la "línea roja del test", por qué `f1_macro` y no accuracy, qué es la fuga de
información en sus tres formas típicas, por qué se declara honestamente que tres decisiones de
diseño se tomaron mirando D2. Es la diferencia de mayor alcance de todo el bloque.

**Donde encaja en el limpio:** Justo después de la sección de Métricas de evaluación de modelos y
antes de "## Ciberseguridad" — es decir, al final de todo el bloque de Machine Learning, junto a la
frase "La curva PR, al no involucrar los verdaderos negativos... se considera más informativa bajo
desequilibrio fuerte de clases."

**Material:** Sección completa `### Metodologías y buenas prácticas` en el actualizado (línea 115
del extracto, "Las secciones anteriores han presentado qué es el aprendizaje automático..."), con
sus ocho subapartados 2.1.6.1-2.1.6.8. Es larga (~2.800 palabras tras el recorte que el propio
Francisco ya decidió aplicarle); si se quiere priorizar, los subapartados que el informe de recorte
marca "SE QUEDA sin recorte" —2.1.6.3 (validación cruzada), 2.1.6.5 (fuga de información) y 2.1.6.7
(reproducibilidad)— son los de mayor consumo por el resto de la memoria.

---

## [B][PROFESOR] 2.1.3 - Confusión cross-validation / N-fold / desviación típica sin resolver

**Que pasa:** El profesor preguntó explícitamente en `mis-apuntes-del-informe.md` («En el 2.1.3, en
la etapa 3, hablo de cross-validation, N-FOLD y desviación. Son 3 cosas distintas?»). El limpio
sigue sin resolver esa ambigüedad: en "Selección del tipo de modelo" solo dice "se compara por
validación cruzada" y luego habla de "media" y "desviación típica" sin aclarar que *cross-validation*
y *N-fold* (o *K-fold*) son el mismo procedimiento y que la desviación típica es un estadístico
distinto, no un tercer procedimiento.

**Por qué importa:** Es uno de los cuatro puntos concretos que el profesor señaló sobre este bloque
y sigue abierto en el limpio.

**Donde encaja en el limpio:** En "Selección del tipo de modelo", junto a la frase "La decisión no
se toma con un único número: se contrastan la media de la métrica elegida entre particiones, su
desviación típica...".

**Material:** El *callout* "Tres términos que no son sinónimos" de 2.1.6.3 en el actualizado:
"Validación cruzada de K particiones (K-fold, o N-fold): son el mismo procedimiento, con distinta
letra para el número de bloques... Desviación típica: es otra cosa, un estadístico de dispersión."

---

## [B] 2.1.5 - Falta el aparato de promediado multiclase (macro/ponderado) y la matriz multiclase

**Que pasa:** El limpio define matriz de confusión solo en su forma binaria (VP/VN/FP/FN) y las
métricas derivadas (precisión, recall, FPR, accuracy, F1) también en binario. No hay ninguna mención
a que en un problema multiclase la matriz pasa a ser k×k, ni a los esquemas de promediado macro y
ponderado, ni a por qué `f1_macro` es la métrica elegida en este trabajo (más allá de mencionarse de
pasada en secciones posteriores del propio limpio, en capítulos 4-5, sin remisión a una definición
teórica en el capítulo 2).

**Por qué importa:** El clasificador de firmas es multiclase y el criterio de selección de todo el
protocolo experimental es `f1_macro`, término que aparece decenas de veces en los capítulos 4 y 5
del propio limpio sin que el capítulo 2 lo defina. Sin esta pieza, el lector no tiene forma de saber
por qué macro y no accuracy, ni qué significa exactamente "macro" frente a "ponderado" cuando el
limpio ya usa ambos en las tablas de resultados.

**Donde encaja en el limpio:** En "Métricas de evaluación de modelos", inmediatamente después de la
definición de F1 y antes del párrafo "Las métricas anteriores evalúan un clasificador en un único
umbral de decisión...".

**Material:** 2.1.5.1 (párrafo del caso multiclase, matriz k×k con esquema uno-contra-el-resto) y
2.1.5.3 "Promediado multiclase: macro y ponderado" del actualizado, con las dos fórmulas
$M_{macro}=\frac{1}{k}\sum M_i$ y $M_{weighted}=\frac{1}{N}\sum n_i M_i$, y el argumento de que
weighted "disimula el fallo en las pequeñas" mientras macro no deja "que una clase mayoritaria tape
a una minoritaria".

---

## [R][PROFESOR] 2.1.1 - Falta la aclaración explícita de que la IA no se define aquí

**Que pasa:** El profesor comentó que en 2.1.1 se introduce la IA pero "ese no es el punto en el que
hay que definirla, sino más adelante". El limpio sigue mencionando la IA en la introducción ("El ML
se enmarca dentro de la IA...") sin ninguna aclaración de que la definición formal se reserva para
más adelante.

**Por qué importa:** Responde directamente a una observación del profesor; sin la aclaración, un
lector (o el propio tribunal) puede interpretar que 2.1.1 pretende definir la IA y encontrarla
incompleta.

**Donde encaja en el limpio:** Justo después de la Figura 1.1 y su pie, tras la frase "el DL es a
su vez un subconjunto estricto del ML".

**Material:** Frase añadida en el actualizado, 2.1.1.1: "La jerarquía completa —qué es la IA, en qué
se diferencia del ML y en qué punto exacto se sitúa el sistema desarrollado— se desarrolla en 2.3.1,
que fija el vocabulario para el resto del documento, y no aquí."

---

## [R] 2.1.2 - Falta la aclaración de que el autoencoder es auto-supervisado en mecanismo pero one-class en régimen

**Que pasa:** El limpio no distingue entre el mecanismo de entrenamiento del autoencoder (que es
auto-supervisado: la señal de entrenamiento es la propia entrada) y el régimen de supervisión
efectivo que este trabajo usa para clasificarlo (semisupervisado one-class, porque solo ve tráfico
normal). El párrafo final de "Tipos de ML" en el limpio justifica el one-class pero no menciona el
matiz auto-supervisado ni resuelve la posible objeción de que scikit-learn documenta estos
algoritmos como "no supervisados".

**Por qué importa:** Es una precisión terminológica menor pero que anticipa una pregunta previsible
de un tribunal ("¿scikit-learn no los llama no supervisados?").

**Donde encaja en el limpio:** Al final de "Tipos de ML", tras el párrafo que empieza "Por
consecuencia, se trata de un aprendizaje semisupervisado de una sola clase (one-class)...".

**Material:** *Callout* "Relación con el autoencoder de este trabajo" en 2.1.2.5 del actualizado:
"...este trabajo lo clasifica y lo evalúa como parte de un régimen semisupervisado (one-class),
porque lo que importa a efectos de detección de anomalías no es cómo se genera la señal de
entrenamiento internamente, sino qué población de datos ve el modelo".

---

## [P] 2.1.4 - Falta mencionar SVM en la lista de algoritmos supervisados representativos

**Que pasa:** La lista de algoritmos supervisados representativos del limpio ("k-NN, la regresión
logística y lineal, los árboles de decisión y las redes neuronales") no incluye las máquinas de
vectores soporte (SVM), que sí aparece en la lista equivalente del actualizado.

**Por qué importa:** Detalle menor de completitud de una enumeración; SVM no forma parte del sistema
implementado (solo aparece en su variante one-class, ya cubierta en otra sección).

**Donde encaja en el limpio:** En "Algoritmos de ML", tras "Algunos de los algoritmos de aprendizaje
supervisado más representativos son...".

**Material:** "...k-vecinos más próximos (k-NN), la regresión lineal y logística, las máquinas de
vectores soporte (SVM), los árboles de decisión y los bosques aleatorios, y las redes neuronales" —
2.1.4.1 del actualizado.

---

## [P] 2.1.4 - Faltan las citas bibliográficas de Isolation Forest y LOF

**Que pasa:** En el limpio, los párrafos de Isolation Forest y Local Outlier Factor no llevan
marcador de cita; en el actualizado sí: Isolation Forest cita `[73]` (Liu, Ting y Zhou 2008, tras
reasignación desde Molnar) y LOF cita `[75]`.

**Por qué importa:** Rigor bibliográfico menor; no cambia ningún argumento del texto.

**Donde encaja en el limpio:** En los párrafos "Isolation Forest" y "Local Outlier Factor" dentro de
"Algoritmos de ML".

**Material:** Añadir `[73]` tras la descripción de Isolation Forest y `[75]` tras la de LOF, según
2.1.4.2 del actualizado.

---

## [D] 2.1.3 - El limpio conserva el desarrollo íntegro del ciclo de vida en cinco fases que el actualizado comprimió a remisiones

**Que pasa:** El limpio mantiene "Etapas del Ciclo de vida de un proyecto de ML" con las cinco fases
desarrolladas en prosa (comprensión, limpieza, selección de modelo, entrenamiento, evaluación). El
actualizado comprimió esa misma sección a un esqueleto de fases con remisiones a 2.1.6, según el
recorte deliberado documentado en `Recorte capítulo 2 - bloque 2.1.md` (partida D-7): la nota se
identificó como la de menor anclaje del bloque y su relleno concreto vive en 4.2-4.5.

**Por qué importa:** No es una pérdida de contenido si se pasa al limpio la versión comprimida —el
argumento es el mismo, solo más breve—, pero se marca como SOLO-EN-DOCX porque, mientras 2.1.6 no
exista en el limpio (ver la entrada [B] de arriba), las remisiones de la versión comprimida
("su rigor está en 2.1.6") apuntarían a nada. No es una contradicción de contenido, es una
consecuencia de la ausencia ya señalada.

**Donde encaja en el limpio:** Toda la sección "Etapas del Ciclo de vida de un proyecto de ML".

**Material:** No aplica traer material nuevo — es una nota de coherencia: si se recorta esta sección
al pasar a limpio, hacerlo después de resolver la ausencia de 2.1.6, no antes.


---

# BLOQUE C — Cap.2.2 Ciberseguridad + 2.3 IA

# Comparación bloque 2.2 Ciberseguridad + 2.3 Inteligencia Artificial (agente C)

## Veredicto del bloque

El limpio conserva el **esqueleto** de 2.2 (introducción, IDS, taxonomía, firmas-vs-anomalías,
taxonomía de ataques) casi completo en su prosa original de hace semanas, pero **no ha incorporado
ninguna de las ampliaciones estructurales** que el vault tiene hoy: la subdivisión numerada
(2.2.x.y), la delimitación del término «híbrido» en cuatro sentidos, los antecedentes y trabajos
comparables, IDS-vs-IPS, las limitaciones transversales y la vigencia de la taxonomía de 1998. El
bloque 2.3 es el más grave: en el limpio ocupa **~90 líneas y tres subtítulos casi vacíos**; en el
actualizado son **tres notas completas (2.3.1/2.3.2/2.3.3) con ocho apartados numerados solo en
2.3.3**. Dado que el profesor preguntó explícitamente «¿qué conceptos de IA estoy incluyendo en el
informe? ¿Ninguno?» (`mis-apuntes-del-informe.md:9`), el estado actual del limpio en 2.3 confirma
literalmente su objeción: la respuesta hoy es, en la práctica, «casi ninguno». Importante: el
informe `Recorte capítulo 2 - bloque 2.3.md` deja constancia de que **la mayoría de los recortes
planificados para 2.3 NO se ejecutaron** (§6 del informe, tabla P1-P9): el material sigue vivo en
el vault, así que estas ausencias no son un recorte intencionado ya aplicado, son trabajo pendiente
de volcar.

---

## [B][PROFESOR] 2.3 — El bloque de IA está reducido a un resumen mínimo frente al vault actual

**Qué pasa:** El limpio tiene "## Inteligencia Artificial" con solo dos subtítulos con contenido real
("IA, ML y DL" reducida a 2 párrafos de conclusión sin argumentación, y "La IA en Ciberseguridad"
con una lista de 4 casos de uso sin desarrollar y el razonamiento del 0-day) más "Límites y
consideraciones éticas" con solo el marco Arp et al. y P9/P10 enunciados muy brevemente. Faltan
completas las secciones 2.3.1.2 (reglas escritas a mano vs. aprendidas), 2.3.1.3 (por qué ML clásico
y no DL, con sus tres argumentos y el criterio de la herramienta mínima), el desarrollo íntegro de
2.3.2.1 (malware, anti-phishing, UEBA), 2.3.2.4 (adversarial ML: evasión y envenenamiento, y "el
modelo que no sabe decir no lo sé"), 2.3.2.5 (panorama de datasets), y de 2.3.3 casi todo excepto la
mención de P9/P10: falta 2.3.3.1 (coste de falsos positivos), 2.3.3.3 completo (modelo de amenaza,
la sección más citada del bloque según el informe de recorte), 2.3.3.4 (explicabilidad), 2.3.3.5
(privacidad/RGPD), 2.3.3.6 (obsolescencia y sesgo), 2.3.3.7 (AI Act/NIS2), 2.3.3.8 (síntesis).
**Por qué importa:** Es la respuesta directa y trazable a la pregunta del profesor. Sin este
material, el capítulo 2 no demuestra ningún aparato conceptual de IA propio: apenas sitúa el sistema
como "aprendizaje automático, no deep learning" sin justificarlo, y no toca en absoluto ni la
explicabilidad, ni el modelo de amenaza, ni el marco regulatorio, que son piezas que capítulos
posteriores (3.1, 5.x, 6.1, A.3 según las remisiones del propio vault) dan por asumidas.
**Dónde encaja en el limpio:** bajo `## Inteligencia Artificial`, entre `### IA, ML y DL` y
`### Límites y consideraciones éticas` (líneas 806-890 del limpio).
**Material:** todo el bloque `## Inteligencia Artificial` del actualizado (líneas 1153-1537),
especialmente 2.3.1.2/2.3.1.3, 2.3.2.1/2.3.2.4/2.3.2.5 y 2.3.3.1/2.3.3.3 a 2.3.3.8.

## [B][PROFESOR] 2.3.1.3 — Falta la justificación de "por qué ML clásico y no Deep Learning"

**Qué pasa:** El limpio afirma que el sistema "es aprendizaje automático" y que el autoencoder "no
constituye una red profunda", pero no da ninguna razón. El actualizado sostiene esa afirmación con
tres argumentos independientes: naturaleza tabular de los datos (con las citas [41] Grinsztajn et
al. y [42] el estudio comparativo de árboles vs. redes), el requisito de interpretabilidad de la
etapa de firmas, y el coste computacional/reproducibilidad; y cierra con los cuatro hechos concretos
que sostienen que el autoencoder no es "profundo" (escala, implementación con MLPRegressor, papel de
escalar único, régimen semisupervisado).
**Por qué importa:** Es precisamente el tipo de argumentación de IA que el profesor echa en falta:
sin ella, la frase "no es deep learning" queda como afirmación sin respaldo, exactamente lo que el
resto del proyecto evita hacer en cualquier otro terreno.
**Dónde encaja en el limpio:** justo después de "Dicho criterio se sitúa en el anillo intermedio...
no constituye una red profunda" (línea 812).
**Material:** actualizado, sección "2.3.1.3 Por qué este trabajo usa ML clásico y no aprendizaje
profundo" (líneas 1203-1236), con sus tres apartados (1)(2)(3) y "El único componente neuronal".

## [B] 2.2.3 — Falta la delimitación del término «híbrido» en cuatro sentidos

**Qué pasa:** El limpio dice solo "Sistemas híbridos: combinan ambos mecanismos... buscando que las
carencias de uno queden cubiertas por el otro" (línea 712), sin más. El actualizado dedica un
apartado completo ("El problema del término «híbrido»") a mostrar que la literatura sobre NSL-KDD
usa "híbrido" con al menos cuatro sentidos incompatibles (combinación de paradigmas, de pipeline, de
clustering+clasificador, de ensemble), fija que este trabajo usa exclusivamente el sentido (a), y
respalda con el caso de Khraisat et al. (2019), que tampoco lo taxonomiza bien.
**Por qué importa:** Es la definición operativa que sostiene todo el argumento de "sistema híbrido"
del trabajo; sin ella, cualquier comparación con trabajos previos que también se llamen "híbridos"
queda sin fundamento, y es justamente el tipo de rigor terminológico que el resto de la memoria
exige (paralelo directo al criterio usado para "IA" en 2.3.1).
**Dónde encaja en el limpio:** dentro de "### Taxonomía de los IDS", tras "Sistemas híbridos:
combinan ambos mecanismos..." (línea 712).
**Material:** actualizado, "2.2.3.2 Por método de detección: firmas, anomalías e híbridos", apartado
"El problema del término «híbrido»" y "Definición operativa adoptada en este trabajo" (líneas
904-921).

## [R] 2.2.3 — Faltan los antecedentes históricos de la combinación anomalías+firmas y los tres trabajos comparables sobre NSL-KDD

**Qué pasa:** El actualizado añade ADAM (2001) y Tombini et al. (2004) como antecedentes de la
casilla híbrida, y sitúa el trabajo frente a tres estudios sobre NSL-KDD que usan el mismo orden
(Ji et al.), el orden inverso (Kim, Lee y Kim) o una topología distinta (Khraisat et al., stacking).
El limpio solo menciona en una frase que "existen trabajos que la adoptan, la invierten y la
reformulan" sin identificarlos (línea 758).
**Por qué importa:** Da al TFG un anclaje bibliográfico concreto que justifica por qué se eligió el
orden anomalías→firmas frente a las alternativas documentadas, en vez de una afirmación genérica.
**Dónde encaja en el limpio:** al final de "### Detección por firmas frente a detección por
anomalías", tras el párrafo que termina "...permite precisar en qué se apoya y en qué se aparta"
(línea 758).
**Material:** actualizado, "Antecedentes de la combinación anomalías + firmas" y los tres párrafos
"Mismo orden.../Orden inverso.../Topología distinta..." (líneas 923-930 y 1068-1074).

## [R] 2.2.2 — Falta el recorrido histórico del IDS (Anderson 1980, Denning/IDES 1987, Snort 1999, análisis con estado) y la comparación IDS vs. IPS

**Qué pasa:** El limpio menciona a Denning y Snort solo de pasada, en una frase (línea 674), sin
fechas ni la línea temporal completa (Anderson 1980, IDES de Denning 1987, los datasets
DARPA/KDD Cup, Snort/Suricata/Zeek, y el análisis con estado de los 2000). Tampoco existe en el
limpio la comparación IDS-vs-IPS (tabla con papel/posición/respuesta/coste de un fallo).
**Por qué importa:** Ancla el linaje conceptual de las dos etapas del sistema (anomalías→Denning,
firmas→Snort) con fechas y citas trazables ([2] Anderson, [3] Denning), que `CLAUDE.md` señala como
de las más citadas del capítulo 2; y la distinción IDS/IPS delimita explícitamente que este trabajo
no hace ninguna afirmación sobre bloqueo ni tiempo real.
**Dónde encaja en el limpio:** dentro de "### Sistemas de detección de intrusiones", tras el párrafo
que empieza "En este trabajo, la etapa de anomalías hereda de Denning..." (línea 674).
**Material:** actualizado, "2.2.2.2 Origen y evolución del concepto" (líneas 799-814) y "2.2.2.3 IDS
frente a IPS" (líneas 816-831).

## [R][CIFRA] 2.2.3 — Falta la sección de limitaciones transversales de los NIDS

**Qué pasa:** El actualizado añade un apartado completo sobre cinco/seis limitaciones que afectan a
cualquier IDS de red con independencia de su casilla taxonómica: cifrado del tráfico, volumen y
velocidad, evasión, falsas alarmas y los límites de Sommer y Paxson sobre ML en detección de
intrusiones, más el límite de representación (caso `snmpgetattack`). Nada de esto está en el limpio.
**Por qué importa:** Contextualiza por qué el enfoque de metadatos/estadísticas de flujo (que es
exactamente lo que usa NSL-KDD) sigue siendo válido pese al cifrado generalizado, y anticipa el
límite de representación que se retoma en el capítulo 5/6.
**Dónde encaja en el limpio:** dentro de "### Taxonomía de los IDS", tras el cuarto eje (momento del
análisis), antes de "### Detección por firmas frente a detección por anomalías" (línea 724-726).
**Material:** actualizado, "2.2.3.4 Limitaciones transversales de los NIDS" (líneas 949-964).

## [R] 2.2.5 — Falta la tabla de gradación de visibilidad en red y la sección "Vigencia de una taxonomía de 1998"

**Qué pasa:** El limpio termina la taxonomía de ataques con la correspondencia DoS/Probe/R2L/U2R con
el espacio de salida del sistema (línea 798), pero no incluye la tabla de gradación de visibilidad
(DoS/Probe alta, R2L baja, U2R muy baja) ni la sección que justifica por qué usar una taxonomía de
1998 sigue siendo defendible (lo que caduca son los tipos, no las categorías; McHugh y
Tavallaee et al.).
**Por qué importa:** La gradación de visibilidad es la predicción a priori de dificultad que el
capítulo 5 contrasta empíricamente (según el actualizado); sin ella en el limpio, esa comprobación
del capítulo 5 (si existe en el .docx) carece de hipótesis previa declarada. La sección de vigencia
responde a la objeción obvia "el dataset es de 1998" antes de que se plantee.
**Dónde encaja en el limpio:** justo después de la "Correspondencia con el espacio de salida del
sistema" que cierra la sección de taxonomía de ataques (línea 798), antes de "## Inteligencia
Artificial".
**Material:** actualizado, "2.2.5.2 Gradación de visibilidad en red" (líneas 1115-1131) y "2.2.5.3
Vigencia de una taxonomía de 1998" (líneas 1133-1150).

## [R][PROFESOR] 2.3.2 — Falta el desarrollo de adversarial ML (evasión/envenenamiento) y "el modelo que no sabe decir no lo sé"

**Qué pasa:** El limpio no menciona en absoluto el vector de evasión ni el de envenenamiento contra
el propio modelo, ni la fragilidad de un clasificador cerrado que asigna con confianza alta un
ataque desconocido a la categoría conocida más parecida (open-set recognition).
**Por qué importa:** Es la sección que conecta con el resultado empírico del capítulo 5 (los 0-day
que la etapa de anomalías detecta pero la de firmas mal-clasifica en vez de decir "unknown"), citada
como fundamento en 6.1/6.2 según el actualizado. Es de las piezas de IA más sustanciosas del bloque
2.3 y responde directamente a la pregunta del profesor.
**Dónde encaja en el limpio:** dentro de "## Inteligencia Artificial", tras el razonamiento del
0-day de tres pasos (línea 838), antes de "### Límites y consideraciones éticas".
**Material:** actualizado, "2.3.2.4 Adversarial machine learning: atacar al modelo mismo" (líneas
1307-1336), incluido "El modelo que no sabe decir «no lo sé»".

## [R] 2.3.2.5 — Falta el panorama de datasets públicos para NIDS

**Qué pasa:** El limpio no compara NSL-KDD con otros datasets del área. El actualizado incluye una
tabla con DARPA 1998/99, KDD Cup 99, NSL-KDD, UNSW-NB15 y CIC-IDS2017/2018, su origen y su
limitación reconocida, y cierra explicando por qué la validación cruzada entre datasets excede el
alcance de esta entrega.
**Por qué importa:** Sitúa la elección de NSL-KDD frente al panorama completo, no solo frente a su
propio linaje DARPA→KDD Cup→NSL-KDD, y es la única sede donde se explican UNSW-NB15 y CIC-IDS2017/18,
que 6.2 Líneas futuras (según el actualizado) usa por nombre como propuesta de trabajo futuro.
**Dónde encaja en el limpio:** al final de "## Inteligencia Artificial" o junto a la taxonomía de
ataques de 2.2.5, antes del cierre del capítulo.
**Material:** actualizado, "2.3.2.5 Datasets públicos para la investigación en NIDS" (líneas
1340-1358).

## [B] 2.3.3 — Falta prácticamente todo el desarrollo del modelo de amenaza (P10) salvo el enunciado mínimo

**Qué pasa:** El limpio sí incluye el marco Arp et al. y una versión resumida de P9 y P10 (líneas
846-889), pero le falta la tabla completa de las seis dimensiones de un modelo de amenaza (activo
protegido, objetivo, conocimiento, capacidad, momento, adaptatividad) con sus "valores típicos", y
el apartado sobre espacio de características vs. espacio del problema (perturbaciones no
realizables) que cierra 2.3.3.3 en el actualizado.
**Por qué importa:** Según el informe de recorte del vault, es "el apartado más citado de todo 2.3":
lo referencian por título 3.1 §3.1.5, 6.1 y A.3. Si el limpio no llega a tener esa base, cualquier
capítulo posterior que remita a "el modelo de amenaza fijado en 2.3.3" (si el .docx llega a esos
capítulos) carece de destino.
**Dónde encaja en el limpio:** dentro de "El modelo de amenaza como requisito metodológico (P10)"
(línea 862), tras la lista de seis dimensiones ya presente pero sin la columna de "valores típicos".
**Material:** actualizado, "2.3.3.3 El modelo de amenaza como requisito metodológico (P10)" completo,
incluida la tabla de dimensiones y "Un límite teórico añadido: espacio de características y espacio
del problema" (líneas 1411-1444).

## [R][PROFESOR] 2.3.3 — Falta la explicabilidad como requisito no opcional en seguridad

**Qué pasa:** El limpio no dedica ninguna sección a la explicabilidad. El actualizado desarrolla tres
razones operativas (triaje, justificación ante terceros, depuración), una tabla
interpretable-por-construcción vs. explicación post-hoc (SHAP/LIME), y sitúa la etapa de firmas del
sistema en la primera fila de esa tabla.
**Por qué importa:** Es un concepto de IA propio y aplicado directamente al sistema (la extracción de
reglas legibles del árbol de decisión), justo el tipo de contenido que el profesor buscaba y no
encontró.
**Dónde encaja en el limpio:** dentro de "### Límites y consideraciones éticas", después de P10
(línea 889).
**Material:** actualizado, "2.3.3.4 Explicabilidad: por qué en seguridad no es opcional" (líneas
1448-1466).

## [P] 2.3.3 — Faltan privacidad/RGPD, marco regulatorio (AI Act/NIS2) y la tabla de síntesis de límites

**Qué pasa:** No están en el limpio los apartados sobre privacidad del tráfico y RGPD, el marco
regulatorio europeo (RGPD/AI Act/NIS2) con su tabla de relevancia para un NIDS con ML, ni la tabla
de síntesis de los siete límites del bloque.
**Por qué importa:** Complementan el marco ético/legal pero son, de los ausentes en 2.3, los que
menos consumidores tienen dentro del propio vault (según el informe de recorte, el callout de "no se
determina la categoría de riesgo" y la tabla RGPD/AI Act/NIS2 no las cita nadie más). Se pueden
omitir sin romper remisiones de otros capítulos, a diferencia del modelo de amenaza o la
explicabilidad.
**Dónde encaja en el limpio:** al final de "### Límites y consideraciones éticas" (tras línea 889).
**Material:** actualizado, "2.3.3.5 Privacidad del tráfico de red", "2.3.3.7 Marco regulatorio y
supervisión humana" y "2.3.3.8 Síntesis" (líneas 1469-1535).

## [P] 2.3.2.1 — Falta el desarrollo de malware, anti-phishing/anti-spam y UEBA como casos de uso

**Qué pasa:** El limpio lista los cuatro casos de uso defensivos como viñetas sin desarrollar
(línea 824-830). El actualizado añade un párrafo por caso: análisis de malware (estático vs.
dinámico), anti-phishing/anti-spam (filtros bayesianos, cita [43]) y UEBA (vínculo explícito con
Denning).
**Por qué importa:** Es contenido de IA aplicada legítimo, pero el propio informe de recorte del
vault lo marca como candidato a comprimir por falta de consumidores en el resto de la memoria
(`malware`, `phishing`, `UEBA` no aparecen fuera del capítulo 2). Prescindible sin daño real.
**Dónde encaja en el limpio:** tras la lista de viñetas de casos de uso (línea 830).
**Material:** actualizado, "2.3.2.1 Casos de uso defensivos", párrafos "Análisis de malware",
"Anti-phishing y anti-spam" y "UEBA" (líneas 1279-1284).

## [P] 2.2.1 — Falta la distinción explícita "seguridad informática frente a ciberseguridad" como relación de continencia

**Qué pasa:** El limpio ya tiene las definiciones de seguridad informática y ciberseguridad casi
literales, pero no incluye el párrafo que explicita la relación entre ambas como "continencia y no
sustitución": la ciberseguridad incorpora la tríada CIA y le añade la dimensión de interconexión.
**Por qué importa:** Es una precisión de vocabulario, no un dato nuevo; el limpio ya transmite la
idea central sin ella, así que su ausencia no rompe nada aguas abajo.
**Dónde encaja en el limpio:** entre la definición de ciberseguridad (línea 634) y "Esta definición
nos introduce a tres objetivos clave..." (línea 636).
**Material:** actualizado, "2.2.1.1 Seguridad informática frente a ciberseguridad", último párrafo
("La relación entre ambos términos es, por tanto, de continencia...", líneas 740).

## [D] Ninguna diferencia SOLO-EN-DOCX detectada en este bloque

**Qué pasa:** No se ha localizado en 2.2/2.3 del limpio ningún contenido, cifra o tesis que ya no
esté en el actualizado (ni contradicho ni retirado). El texto del limpio es, allí donde existe, un
subconjunto casi literal del actualizado (mismas definiciones de CIA, misma taxonomía de ataques,
mismo razonamiento del orden de la cascada), no una versión con material propio perdido.
**Por qué importa:** Confirma que el trabajo pendiente en este bloque es de **incorporación**, no de
reconciliación de contradicciones: no hay que decidir qué versión es la correcta, solo volcar lo que
falta.
**Dónde encaja en el limpio:** n/a.
**Material:** n/a.


---

# BLOQUE D — Cap.4 Implementación

# Bloque D — Capítulo 4, Implementación del sistema

**Veredicto del bloque:** el limpio conserva bien el esqueleto y la mayoría de cifras duras del
capítulo (splits, vocabulario one-hot, tabla de balanceo, tabla H1, reglas del árbol), y de hecho
recorta correctamente varios hiperparámetros de detalle en línea con la petición del profesor —eso
es aceptable y no se reporta como falta—. Pero le faltan tres piezas estructurales que el
actualizado añadió tras un endurecimiento metodológico serio: (1) el aviso KDDTest-21 / el «14» de
Tavallaee (evita un error de comparabilidad grave si alguien lo lee), (2) el reencuadre de la
selección de características como poda del one-hot de `service` con su propia tabla de desglose, y
(3) la declaración explícita de que **tres decisiones se tomaron mirando D2** (data snooping),
incluida la propia elección 54 vs 122. Esta última es la ausencia más grave del bloque porque el
limpio presenta el experimento H1 con el mismo tono "neutral" que el actualizado ya corrigió.
No se ha detectado ninguna contradicción numérica ([C]) entre ambos textos: las cifras que aparecen
en los dos coinciden.

---

### [B][PROFESOR] 4.3.7 - Falta la declaración de que 3 decisiones del sistema se tomaron mirando D2 (data snooping)
**Que pasa:** El actualizado añade un apartado nuevo, "Preprocesado sin fuga de datos" (§4.3.7), que
tras verificar que el preprocesado no fuga (tabla de las 4 transformaciones y dónde se ajustan),
declara explícitamente que **tres decisiones sí se tomaron mirando D2**: el algoritmo ganador de la
etapa de anomalías, el algoritmo ganador de firmas, y el propio set de características (54 vs 122,
experimento H1 de §4.3.5). Las llama por su nombre "*data snooping*" y remite a las limitaciones de
6.1. El limpio no tiene nada de esto: presenta el experimento H1 (que sí conserva, con su tabla
completa) como si fuera una comparación neutral, sin la advertencia de que la propia elección se
basó en métricas de test.
**Por qué importa:** Es una autocrítica metodológica que el propio informe actualizado considera
importante — enlazada desde 2.1.6, 3.3, 4.3.7, 4.6, 5.0, 5.1, 5.2, 5.4, 6.1 y el Apéndice A.3. Sin
ella, el capítulo 4 del limpio presenta el pipeline como más limpio de fuga de lo que realmente es,
y contradice en espíritu (aunque no en cifra) lo que dice 6.1 si esa sección sí ha llegado con la
limitación declarada.
**Donde encaja en el limpio:** en la sección "Selección de características", justo después de la
tabla del experimento H1 y del párrafo "Veredicto: se adopta el set de 54 características...".
También cabría como apartado nuevo antes de "División del conjunto de datos".
**Material:** actualizado, sección "Preprocesado sin fuga de datos" (§4.3.7) y el párrafo "Esta
elección se tomó sobre D2" en §4.3.5: *"Tres decisiones del sistema se tomaron mirando D2: el
detector de la etapa 1, el clasificador de la etapa 2 y el set de características (54 frente a
122). Las tres son selección de modelo sobre el conjunto de test, es decir data snooping, y por
tanto las métricas publicadas son optimistas respecto a lo que daría un test verdaderamente
ciego."*

---

### [B] 4.2.1 - Falta el aviso KDDTest-21 / la vacuna contra el «14» de Tavallaee
**Que pasa:** El actualizado añade dos avisos nuevos en "Base de datos utilizada": (a) que NSL-KDD
distribuye tres ficheros (KDDTrain+, KDDTest+, KDDTest-21), que KDDTest-21 NO es "el subconjunto con
21 tipos de ataque" sino el de dificultad alta (filtrado por 21 clasificadores), y que este trabajo
usa KDDTest+ completo (D2) y no KDDTest-21 por ser condición necesaria de comparabilidad; (b) que la
cifra de "14 tipos de ataque solo en test" que circula en la literatura (Tavallaee) es de KDD'99, no
de NSL-KDD, y no debe usarse para "corregir" el 17 que usa este trabajo. El limpio no tiene ninguno
de los dos.
**Por qué importa:** Sin el aviso (a), un lector familiarizado con NSL-KDD podría pensar erróneamente
que el trabajo debería haber usado KDDTest-21, o confundir las poblaciones de evaluación. Sin (b),
un lector que conozca la cifra "14" de la literatura podría pensar que el "17" del informe es un
error. Ambos son vacunas contra errores de lectura externa, señaladas explícitamente como tales por
el propio actualizado.
**Donde encaja en el limpio:** en "Base de datos utilizada", tras el párrafo que cita a Tavallaee
2009 y McHugh 2000, antes de pasar a "Cada conexión se describe mediante 41 características...".
**Material:** actualizado, subsecciones "Las tres particiones oficiales" y "Vacuna contra un error
que circula en la literatura" (tabla KDDTrain+/KDDTest+/KDDTest-21), y "Vacuna: el «14» de Tavallaee
et al. es de KDD'99, no de NSL-KDD" (tabla comparativa 14 vs 17).

---

### [R] 4.3.3 - Falta el reencuadre de la selección de características como poda del one-hot de `service`
**Que pasa:** El actualizado añade dos apartados analíticos que el limpio no tiene: "El peso real del
one-hot en el espacio de características" (84 de 122 columnas son dummies, el 68,9 % del espacio no
existe en el fichero original, y `service` concentra el 83,3 % de esas dummies y el 57,4 % del total)
y "Qué se poda realmente: la selección es un recorte del one-hot de `service`" (de las 60
características eliminadas por importancia, 58 son dummies, 55 de `service`; sin tocar `service` el
espacio habría bajado de 122 a 109, no a 54). El limpio conserva la mecánica de la selección (varianza,
correlación, ranking) pero sin esta relectura.
**Por qué importa:** Cambia la interpretación de qué hace realmente la selección de características:
no es una reducción genérica, es casi exclusivamente una poda de la variable `service`. Esto también
explica mejor el propio experimento H1 (por qué firmas mejora y anomalías empeora ligeramente con 54
features), argumento que el actualizado conecta explícitamente ("Efecto de esta poda sobre las dos
etapas") y que el limpio no tiene.
**Donde encaja en el limpio:** en "Selección de características", entre el resumen "122 → 54
características (−1 varianza, −7 correlación, −60 importancia)" y el bloque de código de
`select_features`.
**Material:** actualizado, tabla de "protocol_type/service/flag: Categorías en D1 / D1∪D3 / Recuperadas
por el fix / % del total de dummies" y tabla de "Bloque: Numéricas / protocol_type_* / service_* /
flag_*: Antes(122) / Después(54) / Variación".

---

### [R][CIFRA] 4.2.1 - Falta el detalle del reparto D2 por dos denominadores distintos (ataques vs D2 completo)
**Que pasa:** El actualizado desglosa el "el test no replica el reparto del entrenamiento" con una
tabla que da el % de cada categoría sobre dos denominadores distintos: sobre los ataques de D2
(12.833) y sobre D2 completo (22.544). Con el primero, DoS pasa de 78,3 % en D3 a 58,1 % en D2 (el
comparable); con el segundo, a 33,1 % (no comparable con D3). El limpio solo da la cifra "en D2 baja
a ~33 %", que corresponde al denominador de D2 completo, sin aclarar que ese no es el denominador
comparable con el 78,3 % de D3.
**Por qué importa:** Es una fuente de confusión de cifras: el limpio compara 78,3 % (D3, solo
ataques) con ~33 % (D2 completo, con normales) como si fueran directamente comparables, cuando el
actualizado deja claro que el comparable correcto es 58,1 %. Un lector atento notaría la
inconsistencia de denominadores.
**Donde encaja en el limpio:** en el punto "El test no replica el reparto del entrenamiento", justo
donde dice "en D2 baja a ~33 %".
**Material:** actualizado, tabla "Categoría | Registros en D2 | % sobre los ataques de D2 (12.833) |
% sobre D2 completo (22.544)" — DoS: 7.458 / 58,1 % / 33,1 %.

---

### [P] 4.4.3 - Falta la distinción entre AUC-ROC de validación (§4.4) y AUC-ROC de test (§5.1.2)
**Que pasa:** El actualizado añade un apartado ("El AUC-ROC de validación no es el de §5.1.2") que
compara explícitamente 0,9918 (IsolationForest en validación) frente a 0,923 (mismo algoritmo sobre
D2 en 5.1), aclarando que son magnitudes distintas sobre poblaciones distintas y que la primera solo
sirve para ordenar configuraciones dentro de un algoritmo, no como estimación de desempeño. El limpio
no tiene esta comparación cruzada.
**Por qué importa:** Sin la aclaración, un lector podría comparar directamente el 0,9918 de la tabla
de "Configuraciones ganadoras" (4.4) con las cifras del capítulo 5 y pensar que hay una caída de
rendimiento no explicada.
**Donde encaja en el limpio:** en "Configuraciones ganadoras" del apartado de anomalías, tras la
tabla de configuraciones ganadoras.
**Material:** actualizado, apartado "El AUC-ROC de validación no es el de § 5.1.2", tabla con columna
"Aquí (4.4)" vs "En §5.1.2".

---

### [P] 4.3.4 - Falta la limitación declarada de SMOTE sobre variables dummy (valores fraccionarios)
**Que pasa:** El actualizado añade un apartado "Limitación asumida de SMOTE sobre variables one-hot":
SMOTE interpola linealmente, lo que puede producir valores fraccionarios en columnas dummy binarias
(p. ej. flag_S0 = 0,4); se declara como limitación asumida en vez de ocultarse, y se menciona SMOTE-NC
como alternativa fuera de alcance. El limpio no menciona este matiz.
**Por qué importa:** Es una limitación técnica menor pero honesta, del tipo que el proyecto valora
declarar explícitamente en vez de callar; su ausencia no rompe nada del limpio pero es la clase de
detalle que refuerza el rigor metodológico del capítulo.
**Donde encaja en el limpio:** en "Equilibrio y balanceo de muestras", tras la tabla de resultados del
mini-experimento de balanceo.
**Material:** corto y autocontenido — del actualizado: *"SMOTE genera muestras sintéticas
interpolando linealmente entre vecinos [...] las muestras sintéticas pueden tomar valores
fraccionarios en variables que en los datos reales solo valen 0 o 1 (p. ej. flag_S0 = 0,4). Los
clasificadores de árboles lo toleran bien [...], pero es una impureza del espacio de entrada que se
declara como limitación en lugar de ocultarse."*

---

### [P][CIFRA] 4.3.1 - Falta el detalle KS con dos poblaciones distintas ((A) D1 vs D2 completo, (B) D1 vs D2 solo normales)
**Que pasa:** El limpio solo reporta la medición (A) (37 de 54 características con drift). El
actualizado añade una segunda medición, (B) — D1 frente a las 9.711 filas normales de D2 —, con su
propia tabla (25 de 54, ≈46 %), aclara que ambas mediciones "no son intercambiables" y que el delta
(A)−(B) es una comparación, no una descomposición aditiva del drift (el estadístico KS no es aditivo
sobre una mezcla). Esto es un endurecimiento metodológico explícito documentado también en
`resumen-de-decisiones.md`/CLAUDE.md del proyecto (T2).
**Por qué importa:** Sin (B), el limpio no puede sostener con propiedad la explicación del FPR real
del detector sobre D2 (~8-10 %) frente al de diseño (~5 %): el actualizado señala que es justamente
(B), no (A), la medición que puede sostener esa atribución. El limpio conserva la frase sobre el FPR
pero pierde la base metodológica que la justifica con rigor.
**Donde encaja en el limpio:** en "Desplazamiento de distribución entre entrenamiento y test (drift)",
justo después de la cifra "37 de las 54 características (≈69 %) presentan drift".
**Material:** actualizado, apartado "Desplazamiento de distribución..." con la tabla (A)/(B) y el
aviso "`delta = (A) − (B)` es una comparación, no una descomposición".

---

### [D] Firmas - El limpio omite correctamente hiperparámetros de detalle de las rejillas de búsqueda
**Que pasa:** El limpio conserva la tabla completa de espacios de búsqueda con todos los valores
concretos (`max_depth ∈ {5,10,20,None}`, etc.) para anomalías y firmas. El actualizado, en cambio, en
la sección de firmas **resume en prosa** los ejes explorados sin dar los valores concretos de la
rejilla, remitiendo al apéndice A.3 (§A.3.3) para el detalle, y hace lo mismo con las configuraciones
ganadoras de firmas (remitidas también a A.3). Es decir: en este punto es el LIMPIO el que da MÁS
detalle de hiperparámetros que el actualizado.
**Por qué importa:** No es una falta del limpio — es justo lo contrario de lo que pidió el profesor
("no dar todos los hiperparámetros"). Se reporta como [D] únicamente para que Francisco decida si
quiere alinear el limpio con el nuevo criterio de resumir y remitir al apéndice, tal como ya hizo el
actualizado.
**Donde encaja en el limpio:** secciones "Algoritmos y espacios de búsqueda" y "Configuraciones
ganadoras" de "Entrenamiento del modelo de detección basado en firmas".
**Material:** actualizado, mismas secciones, ya reescritas en prosa resumida con remisión a A.3.

---

### [D] 4.5.3 - El limpio no tiene el análisis fino de por qué KNN e HistGradientBoosting coinciden o casi coinciden entre el mini-experimento de 4.3.4 y el GridSearchCV final
**Que pasa:** El actualizado añade un párrafo que explica que para KNN el f1_macro de CV es
*exactamente* el mismo número en 4.3.4 y en la tabla final (0,945349) porque la config. ganadora
coincide con los valores por defecto; y que para HistGradientBoosting la diferencia (0,969377 vs
0,969391) es un artefacto de redondeo sin significado práctico pese a que las configuraciones
técnicamente difieren (max_iter 100 vs 300). El limpio solo dice que "los valores... difieren
marginalmente... porque los dos ejes se exploraron por separado", sin el detalle de qué casos
coinciden exactamente y por qué.
**Por qué importa:** Es una precisión menor, del tipo que evita que un lector atento se pregunte por
qué dos números casi idénticos corresponden a configuraciones distintas. No bloquea la comprensión
del limpio actual.
**Donde encaja en el limpio:** en "Configuraciones ganadoras" de la etapa de firmas, tras la tabla de
configuraciones ganadoras.
**Material:** actualizado, párrafo que empieza "Los valores de f1_macro en CV no son uniformemente
distintos...".


---

# BLOQUE E — Cap.5 Evaluación

# Parcial E — Capítulo 5, Evaluación

## Veredicto del bloque
El limpio conserva casi intacto el esqueleto narrativo de 5.1/5.2/5.3/5.4 (mismas tablas de métricas, mismos hallazgos 0-day, misma comparación con el baseline), pero le falta TODO el aparato metodológico que T1-T4 añadieron este mes: el apartado "5.0 Protocolo de evaluación" no existe como tal en el limpio (solo hay un resumen de una frase en 3.3.4, mucho más pobre), la subsección de robustez frente a la semilla (T4, dispersión entre 10 semillas) no aparece en absoluto, la explicación del exceso de FPR como *dataset shift* (T2) tampoco, y todo el bloque final de 5.4 sobre la comparación con la literatura (rejilla C1-C7, tabla de 7 baselines canónicos, Hindy et al., falacia de la tasa base, límites de la latencia) está ausente del capítulo 5 del limpio. El hallazgo de mayor gravedad es una contradicción de cifra concreta: el propio texto del limpio dice que IsolationForest cuesta "ocho veces menos" que el Autoencoder; el actualizado, con el esquema de tiempos ya corregido por T1, dice "catorce veces" (o "nueve veces" según la columna). Es un capítulo de cifras, y aquí la desactualización es sustancial, no cosmética.

---

### [C][CIFRA] 5.1 Resultados del modelo de detección de anomalías - el "ocho veces menor" del coste de IsolationForest está obsoleto
**Que pasa:** El limpio afirma que IsolationForest tiene "un coste de entrenamiento ocho veces menor" que el Autoencoder, con una tabla de tiempos de una sola columna ("Tiempo (s)": IF 5,04; OCSVM 28,34; LOF 16,42; AE 40,56). El actualizado divide el tiempo en dos columnas —`tiempo_entrenamiento_s` (solo los `fit`) y `tiempo_s` (bloque completo)— y con esos valores corregidos (IF 3,51/5,27; AE 48,93/49,20) el factor pasa a ser "aproximadamente catorce veces menor" sobre entrenamiento puro, o "≈×9,3" sobre el bloque completo.
**Por que importa:** Es una cifra citada literalmente en la sección "Resultados finales", que el lector puede repetir tal cual en la memoria final; el factor "ocho veces" ya no es el que sostienen los datos actuales, y además el esquema T1 (columna `alcance_tiempo_s`) explica por qué había que declarar cuál de las dos magnitudes se está citando.
**Donde encaja en el limpio:** Sección "Resultados finales" del capítulo 5, frase "IsolationForest queda muy cerca (F1 = 0.834, AUC-ROC 0.923) y constituye una alternativa razonable con un coste de entrenamiento ocho veces menor".
**Material:** Actualizado, § Resultados finales de 5.1: "IsolationForest queda muy cerca ... y constituye una alternativa razonable con un coste de entrenamiento aproximadamente catorce veces menor (3,51 s frente a 48,93 s, columna tiempo_entrenamiento_s)"; y la tabla de métricas de § 5.1.2 con las columnas "Entrenamiento (s)" / "Bloque completo (s)".

### [C][CIFRA] 5.1 Resultados del modelo de detección de anomalías - tabla de tiempos de un solo valor por algoritmo, ya sustituida por dos columnas
**Que pasa:** La tabla de métricas de desempeño del limpio tiene una única columna "Tiempo (s)" con un valor por algoritmo (p.ej. Autoencoder = 40,56). El actualizado reporta esos mismos algoritmos con dos columnas distintas y valores distintos (Autoencoder: entrenamiento 48,93 / bloque completo 49,20; OneClassSVM: 10,69 / 25,58; LOF: 13,29 / 20,16), acompañadas de una nota que explica qué mide cada una y por qué mezclarlas es un error (esquema T1, columna `alcance_tiempo_s`).
**Por que importa:** Ninguno de los cuatro valores de la tabla del limpio coincide con ninguna de las dos columnas del actualizado; presentar un "Tiempo (s)" ambiguo es justo el defecto de esquema que T1 corrigió (columnas con el mismo nombre midiendo magnitudes distintas), y volcarlo al Word tal cual reintroduce el problema que el proyecto ya solucionó.
**Donde encaja en el limpio:** Tabla de "Métricas de desempeño" en 5.1, columna "Tiempo (s)".
**Material:** Actualizado § 5.1.2, tabla con columnas "Entrenamiento (s)" y "Bloque completo (s)", más el párrafo "Qué mide cada columna de tiempo, y hasta dónde vale" inmediatamente debajo.

### [B][PROFESOR] 5.0 Protocolo de evaluación - la sección entera no llegó al limpio
**Que pasa:** El actualizado abre el capítulo 5 con "## Protocolo de evaluación" (unas 230 líneas): tabla de particiones D1/D2/D3 con función exclusiva de cada una, tabla de "qué queda congelado entre variantes", las cuatro métricas obligatorias, las cuatro prohibiciones explícitas (incluida la distinción P5 vs P-5), el vocabulario de reproducibilidad de NeurIPS, y la rejilla propia de 7 criterios C1-C7 con la auditoría del propio trabajo contra ella (incluido el episodio de la corrección T1: la columna `accuracy_D2` que significaba dos cosas distintas en dos tablas). El limpio no tiene nada de esto bajo ese título; lo único parecido es un párrafo de una frase en "3.3.4 Protocolo de evaluación común" (capítulo 3), mucho más genérico y sin ninguna de las tablas ni la auditoría C1-C7.
**Por que importa:** Sin este apartado, toda cifra del capítulo 5 del limpio queda sin las reglas que la hacen defendible: qué partición interviene, qué prohibiciones vinculantes rigen, y por qué el propio trabajo se audita contra los mismos siete criterios que aplica a la literatura ajena. Es, además, el material más nuevo (T1) y el que Francisco pidió expresamente situar antes de las cifras.
**Donde encaja en el limpio:** Justo al principio del capítulo "# Evaluación", antes de "## Resultados del modelo de detección de anomalías" — el limpio salta directamente a los resultados.
**Material:** Actualizado, sección completa "## Protocolo de evaluación" (líneas 4-237 de la extracción de este bloque), con sus seis subsecciones: "Las particiones y la función de cada una", "Qué queda congelado entre las dos variantes", "Métricas obligatorias", "Prohibiciones explícitas", "Vocabulario de reproducibilidad" y "El mismo filtro, aplicado a uno mismo".

### [B] 5.2 Resultados del modelo de detección basado en firmas - falta la subsección entera "Robustez frente a la semilla" (T4)
**Que pasa:** El actualizado añade tras la comparación 54-vs-122 una subsección completa de cuatro apartados (5.2.4.1-5.2.4.4) sobre el barrido de diez semillas: el solapamiento de intervalos RandomForest/HistGradientBoosting, la comparación pareada (RF gana en 8 de 10), el hecho de que el titular publicado (0,8223) es el punto más favorable de las once corridas, las 13 celdas del proyecto que caen fuera de su banda de dispersión, y la inestabilidad del eje SMOTE-vs-class_weight entre semillas (mientras que SMOTE-vs-nada sí está establecido, 40 de 40). Nada de esto aparece en el limpio.
**Por que importa:** Es la aportación central de T4 y cambia cómo debe leerse la cifra estrella de la etapa de firmas (0.822): en el actualizado se declara que hay que citarla junto a su banda [0,7779-0,8205] y su media 0,8035, y que el orden entre RandomForest y HistGradientBoosting solo está establecido en la comparación pareada, no en absoluto. Publicar 0.822 sin este matiz es presentar el punto más favorable de once corridas como si fuera LA cifra.
**Donde encaja en el limpio:** Al final de "Resultados del modelo de detección basado en firmas", justo después del párrafo que cierra con "la decisión Q1/C a favor del conjunto de 54 características".
**Material:** Actualizado, sección "### Robustez frente a la semilla" completa (§ 5.2.4.1 a 5.2.4.4), y su cierre "El barrido no descubre que la decisión de 4.3.4 estuviera mal: confirma que ese eje nunca estuvo establecido".

### [B] 5.4 Conclusiones del capítulo - falta entera la comparación con la literatura publicada (C1-C7, siete baselines, Hindy et al.)
**Que pasa:** El actualizado cierra el capítulo con una sección larga "### El sistema frente a la literatura publicada sobre NSL-KDD": aplica la rejilla C1-C7 (ya definida en 5.0) a la literatura revisada, publica la tabla de los siete baselines canónicos del artículo que creó el dataset (NBTree 82,02 %, ..., SVM 69,53 %) frente al 86,05 % del sistema propio, explica que el porcentaje del descarte propio no se cita como dato (solo la cifra externa de una revisión sistemática, [74]), y discute en detalle el único precedente comparable (Hindy et al. [77], descartado por incumplir C7 en tres motivos). Nada de esta comparación con la literatura aparece en el capítulo 5 del limpio.
**Por que importa:** Es la única sección del capítulo que sitúa el sistema frente al estado del arte publicado sobre NSL-KDD con un criterio de admisión explícito, en vez de afirmar superioridad sin más. Sin ella, el capítulo 5 del limpio no tiene ningún punto de comparación externo.
**Donde encaja en el limpio:** Después de "Los caveats que acompañan a la tesis", antes de que termine "## Conclusiones del capítulo" (justo antes del salto a "# Conclusiones").
**Material:** Actualizado, "### El sistema frente a la literatura publicada sobre NSL-KDD" completa, con sus subapartados "Los criterios de admisión", "Lo que sobrevive al filtro" (tabla de 7 baselines), "La magnitud del descarte" y "Hindy et al.: el precedente que se cita por el método, no por el número".

### [B] 5.4 Conclusiones del capítulo - falta la proyección a prevalencia realista (falacia de la tasa base)
**Que pasa:** El actualizado incluye "### Qué significa este FPR a prevalencia realista": proyecta el recall (0,8318) y el FPR (0,1017) medidos a distintas prevalencias de ataque realistas (10 %, 5 %, 1 %, 0,1 %) con la fórmula de precisión condicionada, mostrando que a prevalencia del 1 % más de 9 de cada 10 alarmas serían falsas. Concluye que el FPR del 10 % "no es un decimal, es un problema operativo" y que reducirlo es prioridad de mejora antes que ganar recall. El limpio no tiene esta proyección.
**Por que importa:** Es el matiz más incómodo y más honesto del capítulo: pone en contexto operativo la cifra estrella del sistema, algo que el capítulo 2 (falacia de la tasa base) anuncia en teoría y que aquí se aplica con números concretos al propio sistema. Omitirlo deja las cifras de 5.3 leyéndose como si fueran directamente trasladables a un despliegue real.
**Donde encaja en el limpio:** Tras la comparación con el baseline monolítico, dentro de "## Conclusiones del capítulo", antes o después de "Los caveats que acompañan a la tesis".
**Material:** Actualizado, "### Qué significa este FPR a prevalencia realista", con su tabla de prevalencias y la fórmula de precisión proyectada.

### [B] 5.1 Resultados del modelo de detección de anomalías - falta la explicación del exceso de FPR como desplazamiento entre particiones (T2)
**Que pasa:** El actualizado añade "### El desplazamiento entre particiones explica el exceso de falsos positivos": distingue explícitamente *dataset shift* (medible, es lo que hay en NSL-KDD) de *concept drift* (no medible, no hay marca de tiempo), explica que la medición (B) del KS de 4.2 —D1 frente a los normales de D2— es la única que puede sostener la explicación del exceso de FPR, aclara que `delta = (A) - (B)` es una comparación y no una descomposición aditiva, y publica la tabla de exceso por variante (54: FPR diseño ≈5 % → medido 10,2 %; 122: ≈5 % → 8,5 %). El limpio no explica en ningún punto por qué el FPR real duplica al nominal del percentil 95.
**Por que importa:** Sin esta sección, el lector del limpio ve un umbral "percentil 95" prometiendo 5 % de falsos positivos y luego una tabla con FPR del 8,5-16 % sin que se explique la discrepancia; es exactamente el tipo de objeción de protocolo que el propio 5.0 dice que hay que responder antes de enseñar los números.
**Donde encaja en el limpio:** Entre "Métricas de desempeño" y "Resultados finales" de la sección de anomalías, donde el limpio menciona el umbral percentil 95 sin volver sobre el exceso observado.
**Material:** Actualizado, "### El desplazamiento entre particiones explica el exceso de falsos positivos" completa, incluida la tabla "El exceso, por variante".

### [B] 5.1 y 5.2 - falta la declaración de que tres decisiones del sistema se calibraron mirando D2 (data snooping admitido)
**Que pasa:** El actualizado declara explícitamente, en 5.1 ("La elección del detector ganador sí usó métricas de D2") y en 5.2 ("La elección del clasificador ganador sí usó métricas de D2"), que la elección del Autoencoder, la de RandomForest y la del set de 54 vs 122 características son selección de modelo hecha sobre el conjunto de test, y que las cifras del ganador deben leerse como "optimistas por selección". El limpio presenta ambas elecciones (H-2, H-3) sin ese matiz, como si fueran decisiones limpias de fuga.
**Por que importa:** Es una autocrítica metodológica explícita del propio trabajo (parte del espíritu de la rejilla C1-C7): omitirla hace que el limpio parezca más limpio metodológicamente de lo que el propio proyecto se declara.
**Donde encaja en el limpio:** Al final de "Resultados finales" en 5.1 (tras la frase sobre el equilibrio recall/FPR) y al final de "Comparación de los resultados de cada algoritmo" en 5.2.
**Material:** Actualizado § 5.1 "La elección del detector ganador sí usó métricas de D2" y § 5.2 "La elección del clasificador ganador sí usó métricas de D2".

### [R] 5.3 Resultados del sistema híbrido - falta la explicación en tres partes del 13,4 % de enrutado a "unknown"
**Que pasa:** El limpio menciona el 13,4 % de 0-day enrutados a unknown y da una frase de contexto sobre sobre-confianza del clasificador. El actualizado desarrolla tres afirmaciones separadas con respaldo bibliográfico: (1) el 13,4 % mide calidad del etiquetado, no detección (por P-5 los 0-day no enrutados a unknown siguen alarmados); (2) el mecanismo es un umbral sobre un clasificador de conjunto cerrado, con límite teórico demostrado (Scheirer et al. [61]); (3) OpenMax [49] se propone en la literatura justo como superación de este mecanismo, situándolo como comparador a batir, no como error propio.
**Por que importa:** Da al hallazgo un respaldo bibliográfico concreto que hoy falta en el limpio, y aclara una posible mala lectura (que el 13,4 % fuera una tasa de fallo del sistema, cuando no lo es).
**Donde encaja en el limpio:** Dentro de "Calibración del umbral de confianza", tras la frase "El RandomForest, entrenado solo con los tipos de D3, resulta sobre-confiado ante datos fuera de su distribución".
**Material:** Actualizado § 5.3 "El enrutado a unknown: el 13,4 %, explicado", puntos 1-3.

### [R] 5.4 Conclusiones del capítulo - falta la sección sobre los límites de la latencia publicada
**Que pasa:** El actualizado añade "### Qué NO mide la latencia publicada": aclara que `latencia_ms_por_flujo` y `flujos_por_segundo` solo miden el `predict`/`score` sobre características ya calculadas, no captura ni extracción; da la cifra de techo de inferencia (≈4.196.350 flujos/s en semilla 42, hasta 4.656.277 en el barrido de 10 semillas) y advierte de una inconsistencia interna de redondeo entre columnas (desvío del 8,2 % / 12,6 % según variante). El limpio no tiene esta salvedad.
**Por que importa:** Evita que un lector cite la cifra de flujos/s como capacidad operativa real del sistema.
**Donde encaja en el limpio:** Al final de "## Conclusiones del capítulo", cerca de donde se discuten los caveats de la tesis.
**Material:** Actualizado, "### Qué NO mide la latencia publicada" completa.

### [R] 5.2 Resultados del modelo de detección basado en firmas - falta el análisis de la inversión probe/r2l frente a la jerarquía predicha en 2.2.5.2
**Que pasa:** El actualizado añade "#### Contraste con la jerarquía de dificultad predicha": contrasta el orden de detectabilidad predicho en 2.2.5.2 (`dos > probe > r2l > u2r`) con lo observado, mostrando que el orden se invierte en el tramo intermedio (`r2l` supera a `probe` en 3 de 4 modelos) y explica por qué (precisión alta pero recall más bajo en r2l; recall casi perfecto pero precisión contaminada en probe). El limpio no discute esta inversión.
**Por que importa:** Es un hallazgo metodológico propio (la predicción teórica del capítulo 2 se confirma solo parcialmente) que conecta explícitamente dos capítulos y que el limpio deja sin cerrar.
**Donde encaja en el limpio:** Tras el desglose por categoría de la tabla F1 por clase en "Métricas de desempeño" de la sección de firmas.
**Material:** Actualizado § 5.2 "#### Contraste con la jerarquía de dificultad predicha", con la tabla de precisión/recall de `probe`.

### [P] 5.2 Resultados del modelo de detección basado en firmas - precisión del soporte de u2r (37 en el subconjunto conocido vs 200 en D2 completo vs 52 en D3)
**Que pasa:** El limpio dice que u2r tiene "37 muestras" en D2 sin más precisión. El actualizado aclara que 37 es el soporte solo entre los ataques de tipo conocido evaluados (9.083), que en D2 completo u2r tiene 200 muestras, y que en D3 (entrenamiento) son 52.
**Por que importa:** Complementa la cifra existente sin contradecirla; evita que un lector confunda "37" con el total de u2r en el test.
**Donde encaja en el limpio:** Junto a la frase "u2r es el punto débil universal: con solo 37 muestras en D2".
**Material:** Actualizado § 5.2, nota "(200 en D2 completo, según §4.2; 52 en D3, recuento exacto de Resultados/specialized_nsl_kdd_composicion_d3.csv)".

### [P] 5.4 Conclusiones del capítulo - falta la nota de que el eje de balanceo SMOTE-vs-class_weight se declara "no establecido" (T4)
**Que pasa:** El actualizado añade en el cierre del capítulo la frase "### Una decisión de preprocesado que se declara no establecida", remitiendo a 5.2.4.4: la elección de SMOTE vs class_weight en DecisionTree/RandomForest no es estable entre semillas, mientras SMOTE vs nada sí lo es. El limpio, al no tener 5.2.4, tampoco tiene este resumen de cierre.
**Por que importa:** Es prescindible como entrada independiente porque su contenido ya se cubre en el hallazgo [B] de "Robustez frente a la semilla"; se anota aparte solo porque aparece también como frase de cierre explícita en 5.4.
**Donde encaja en el limpio:** Dentro de "## Conclusiones del capítulo", cerca de "Hallazgos que trascienden la comparación 54 vs 122".
**Material:** Actualizado § 5.4 "### Una decisión de preprocesado que se declara no establecida".


---

# BLOQUE F — Cap.6 Conclusiones + Apéndices

# Bloque F — Capítulo 6 (Conclusiones y Líneas futuras) + Apéndices

## Veredicto del bloque

El limpio se corta a mitad del capítulo 6: `6.1 Conclusiones` está pasada a limpio en una versión
**vieja** (anterior a la reapertura T2-T4 y a la reestructuración por los 9 objetivos de `1.3`), y
`6.2 Líneas futuras` es solo el título, sin una sola línea de contenido. **No hay ningún apéndice
real en el limpio**: lo que sigue al título "Líneas futuras" es un único bloque —el antiguo
`A.1 Columnas del dataset NSL-KDD`— seguido de una `Bibliografía` de 11 entradas y de texto de
plantilla de Word sin desarrollar ("Nombre del apéndice A", "Este texto está escrito en estilo
Normal..."). Los apéndices `A.2 Métricas de desempeño` y, sobre todo, `A.3 Ficha del sistema` —que
en el actualizado suman varios miles de palabras cada uno— **no han llegado al limpio en absoluto**.
Se diagnostica agrupado por apéndice/sección, no entrada a entrada, tal como pide el encargo.
`6.1`, `6.2` y `A.3` están modificadas sin commitear en el vault: el volcado de hoy ya las recoge.

---

## [B] 6.1 Conclusiones - falta el desglose de los 9 objetivos específicos en 4 bloques (A-D)
**Qué pasa:** el limpio conserva la versión antigua de "Grado de cumplimiento de los objetivos": 4
bullets sueltos (investigar métodos, revisar/preprocesar, entrenar/validar, estudiar resultados).
El actualizado la sustituyó por una correspondencia explícita **uno a uno** con los 9 objetivos
enunciados en `1.3 Objetivo`, agrupados en cuatro bloques temáticos (A: fundamentos teóricos —obj.
1—; B: dataset/preprocesado/validación —obj. 2-3—; C: entrenamiento e integración de la cascada
—obj. 4-6—, con la salvedad metodológica del objetivo 4 sobre H-2; D: contraste, medición 0-day y
análisis crítico —obj. 7-9—).
**Por qué importa:** si `1.3 Objetivo` ya enumera 9 objetivos (verificar en el propio limpio, que sí
llegó actualizado según el volcado de esa sección), el capítulo de conclusiones del limpio queda
descolgado: no cierra el círculo objetivo-por-objetivo que el resto de la memoria sí prometía.
**Dónde encaja en el limpio:** sección `## Conclusiones`, inmediatamente bajo el encabezado
"### Grado de cumplimiento de los objetivos", sustituyendo los 4 bullets actuales ("- Investigar los
dos métodos...", etc.).
**Material:** actualizado, `# Conclusiones` → `## Conclusiones` → "Sobre los **nueve objetivos
específicos** enunciados en 1.3 Objetivo, la valoración se agrupa en cuatro bloques temáticos..."
hasta el final de "Bloque D — contraste, medición de lo desconocido y análisis crítico".

## [B] 6.1 Conclusiones - falta entera la sección "Límites de lo medible con NSL-KDD" (6.1.4)
**Qué pasa:** el actualizado añade una subsección completa, distinta de "Limitaciones", que separa
límites *del sistema* de límites *del banco de pruebas NSL-KDD*: seis límites numerados (sin marca
de tiempo, sin despliegue real -P9-, sin adversario adaptativo -P10-, una sola semilla, el
clasificador cerrado no acota riesgo de espacio abierto, los 0-day del NSL-KDD no son amenazas
actuales) y una tabla de balance final contra los diez errores metodológicos de Arp et al.
(P1-P10), con "cubierto"/"cubierto hasta donde el dataset permite" para cada uno. Es contenido
sustancial (varios miles de palabras) que el limpio no tiene en ninguna forma, ni resumida.
**Por qué importa:** es la sección que sostiene metodológicamente por qué el trabajo no promete lo
que el NSL-KDD no puede medir (deriva temporal, adversario adaptativo, prevalencia real); sin ella
las "Limitaciones" que sí están en el limpio quedan sin el marco que las justifica y sin conectar
con `2.3.3` y `3.1.5`.
**Dónde encaja en el limpio:** justo después de "### Limitaciones" y antes de la sección
"## Líneas futuras", como nueva subsección "### Límites de lo medible con NSL-KDD".
**Material:** actualizado, sección "### Límites de lo medible con NSL-KDD" completa, con
subapartados "#### 6.1.4.1 Los seis límites, uno a uno" y "#### 6.1.4.2 Balance frente al catálogo
de errores metodológicos" (tabla P1-P10).

## [B] 6.2 Líneas futuras - toda la sección está vacía en el limpio (solo el título)
**Qué pasa:** en el limpio, "## Líneas futuras" no tiene ni una frase debajo; pasa directo al primer
apéndice. En el actualizado es una sección desarrollada de ~2.500-3.000 palabras, organizada en dos
bloques: **A. Refinamientos sobre el sistema actual** (6.2.1 ensemble de detectores de anomalías,
6.2.2 reconocimiento de conjunto abierto/open-set, 6.2.3 vector de error de reconstrucción por
característica como entrada de la etapa 2, 6.2.4 conjuntos de características distintos por etapa,
6.2.5 generación automática de firmas a partir de `unknown`) y **B. Ampliación del alcance
experimental** (6.2.6 migración a un dataset con marca de tiempo y representación de secuencia, en
tres peldaños, con la nota sobre por qué el aprendizaje incremental por ráfagas NO es *Nested
Learning*). Cada línea trae observación motivadora, propuesta concreta y qué habría que medir para
que cuente como mejora.
**Por qué importa:** es un entregable completo del capítulo de conclusiones, ya cerrado y
redactado; dejarlo en blanco en el limpio no es un recorte, es simplemente no haberlo pasado.
**Dónde encaja en el limpio:** bajo "## Líneas futuras", sustituyendo el vacío actual.
**Material:** actualizado, desde "## Líneas futuras" ("El criterio de admisión de esta sección es
deliberadamente restrictivo...") hasta el final de la sección "### Enlaces" (justo antes de
"::: {custom-style=\"Apéndice\"} Apéndices").

## [B][PROFESOR] Apéndices - falta entero `A.3 Ficha del sistema`
**Qué pasa:** el limpio no tiene ningún rastro de `A.3`. En el actualizado es el apéndice más
extenso del trabajo: una *model card* (A.3.1-A.3.9: detalles del modelo, particiones de datos,
configuraciones seleccionadas por semilla 42, alcance de cada métrica, infraestructura de cómputo,
resultados con dispersión entre semillas, límite de reproducibilidad de rutas *hardcodeadas*, las
tres decisiones tomadas mirando D2, y otros límites del alcance evaluado) más un anexo teórico
(A.3.10: algoritmos que el sistema NO usa —regresión logística, k-means/jerárquico, redes
neuronales—; A.3.11: desarrollo metodológico en extensión de CRISP-DM, la partición train/test, la
validación cruzada y el coste de GridSearchCV).
**Por qué importa:** `A.3` es donde fue a parar el material que el profesor pidió sacar del cuerpo
de la memoria (ficha T7 en `features.md`: "RESTRICCIÓN DURA (T7): lo que salga del cuerpo se MUEVE
a A.3, NO se elimina"). El propio `6.1 Conclusiones` del actualizado remite explícitamente a
`A.3 §A.3.7` para el volcado tabulado de las tres decisiones de *data snooping*. Sin `A.3`, esas
remisiones del cuerpo (ya presentes en el `6.1` actualizado, y candidatas a entrar en el limpio) no
tienen destino: no es un apéndice cosmético, es la contraparte de recortes ya aplicados en el
cuerpo.
**Dónde encaja en el limpio:** como tercer apéndice, después de un futuro `A.2 Métricas de
desempeño`, con el título "Ficha del sistema" en el mismo estilo "Título 2 de Apéndice" que usan
`A.1` y `A.2`.
**Material:** archivo `memoria_completa_20260822-154416_fd089cc-sucio.md`, desde
"::: {custom-style=\"Título 2 de Apéndice\"} Ficha del sistema" hasta el final del fichero (línea
~4240 hasta 5017); también disponible como nota independiente en
`Obsidian_TFG_Vault/Apéndices/A.3 Ficha del sistema.md`.

## [B] Apéndices - falta entero `A.2 Métricas de desempeño`
**Qué pasa:** el limpio salta de "Métricas de desempeño" (solo el título suelto, sin desarrollar,
justo antes de la Bibliografía) al final del fichero. El actualizado desarrolla ese apéndice
completo: convención de signo, matriz de confusión y conteos base, fórmulas de precision/recall/F1/
FPR "de consulta rápida", promedios macro vs. weighted, curvas ROC/PR, y dos subsecciones propias:
`A.2.1 Métricas del modelo de anomalías` (por qué el FPR del sistema es el FPR de la etapa 1,
umbral por percentil 95, FPR nominal 5 % frente al real medido: **10,2 % en 54 características y
8,5 % en 122**) y `A.2.2 Métricas ajenas a la clasificación, no reportadas por este trabajo` (MAE/
RMSE y coeficiente de silueta, por completitud del marco teórico).
**Por qué importa:** sin A.2.1 no hay dónde documentar la relación exacta entre `bin_fpr` del
híbrido y `fpr` del Autoencoder en `metricas_anomalias.csv`, que el actualizado usa para justificar
por qué "el FPR del sistema ES el FPR de la etapa de anomalías" — una afirmación que aparece citada
desde otras partes de la memoria.
**Dónde encaja en el limpio:** el limpio ya tiene el título "####### Métricas de desempeño" suelto
justo antes de la Bibliografía; ahí debe entrar todo el contenido.
**Material:** actualizado, desde "::: {custom-style=\"Título 2 de Apéndice\"} Métricas de
desempeño" hasta justo antes de "::: {custom-style=\"Título 2 de Apéndice\"} Ficha del sistema".

## [R] Apéndice A.1 (Columnas del dataset) - subtítulos con numeración A.1.1-A.1.5 ausentes
**Qué pasa:** el contenido de tablas de A.1 SÍ está en el limpio (las 41 características y las
etiquetas coinciden en sustancia), pero el limpio no usa la numeración `A.1.1`-`A.1.5` que trae el
actualizado en sus subtítulos ("A.1.1 Características básicas", ..., "A.1.5 Etiquetas: tipos de
ataque y categorías"); en el limpio son subtítulos sin numerar.
**Por qué importa:** es menor porque el contenido ya está, pero la numeración es la que después usan
las referencias cruzadas de otras secciones (p. ej. A.3 remite a "A.1" en general, y si se numeran
subapartados en otros sitios conviene que A.1 también los lleve, por consistencia con A.2/A.3).
**Dónde encaja en el limpio:** en cada uno de los cuatro subtítulos de tabla dentro del apéndice
"Columnas del dataset NSL-KDD".
**Material:** actualizado, títulos "A.1.1 Características básicas (1–9)" a "A.1.5 Etiquetas: tipos
de ataque y categorías".

## [P] Bibliografía - el limpio tiene 11 entradas frente a las ~78 numeradas del proyecto
**Qué pasa:** la Bibliografía que aparece intercalada en el limpio (entre el apéndice A.1 y el resto
de plantilla) trae solo 11 referencias en formato antiguo (sin `[n]` consistente con
`Bibliografía.md`). El vault vivo tiene 78 números emitidos (70 vivos + 8 quemados).
**Por qué importa:** se marca como prescindible en este bloque porque, según `CLAUDE.md`, "la
bibliografía final en Zotero/IEEE sigue siendo de Francisco" y es trabajo mecánico fuera del vault;
no es una diferencia de contenido del capítulo 6/apéndices que corresponda resolver por un agente.
Se deja constancia solo para que no se pierda de vista al pasar a limpio el documento entero.
**Dónde encaja en el limpio:** sección "Bibliografía" tras el apéndice A.1.
**Material:** `Obsidian_TFG_Vault/Bibliografía.md`, tabla completa de referencias `[1]`-`[78]`.

## [D] 6.1 Conclusiones - el limpio detalla f1_macro 0.909→0.472 en "Validación de la tesis"; el actualizado lo remite a 5.3
**Qué pasa:** el limpio, en el párrafo de "Validación de la tesis del híbrido", cita explícitamente
el desplome de f1_macro del baseline (0.909 en CV → 0.472 en test) dentro del propio 6.1. El
actualizado retiró esas cifras de 6.1 y las dejó solo en 5.3 ("La comparación completa —tabla de
métricas, matrices de confusión y análisis de la forma del error— está en 5.3 y no se reproduce
aquí"). Las cifras siguen vivas y son las mismas (`metricas_baseline.csv`), no hay contradicción de
valor.
**Por qué importa:** no es una pérdida de contenido, es una reorganización deliberada para no
duplicar cifras entre capítulos; se marca [D] porque, si se pasa el 6.1 actualizado tal cual, el
párrafo del limpio con esas cifras debe sustituirse (no fusionarse) por la versión resumida.
**Dónde encaja en el limpio:** párrafo "La hipótesis central del trabajo..." dentro de "### Grado de
cumplimiento..." → "### Validación de la tesis del híbrido".
**Material:** actualizado, párrafo que empieza "La hipótesis central del trabajo —que un enfoque
híbrido..." en `## Conclusiones` → `### Validación de la tesis del híbrido`.

## [D] Apéndices - el limpio trae texto de plantilla de Word sin desarrollar al final del fichero
**Qué pasa:** tras la Bibliografía, el limpio conserva literalmente instrucciones de plantilla
("Nombre del apéndice A", "Este texto está escrito en estilo Normal...", "Para introducir una
Figura/Tabla en un apéndice, debe proceder igual que...") con una figura y tabla de ejemplo vacías.
El actualizado no tiene nada de esto: los apéndices reales (A.1, A.2, A.3) sustituyen por completo
ese contenido de plantilla.
**Por qué importa:** confirma que el corte del limpio ocurrió literalmente a mitad de trabajo sobre
la plantilla de apéndices de Word, antes de rellenarla con A.2 y A.3; es la prueba física de que
falta pasar el bloque completo, no un detalle a limpiar.
**Dónde encaja en el limpio:** al final del fichero, tras la tabla de ejemplo "Tabla en Apéndice
A.1. Ejemplo de pie de tabla en apéndice."
**Material:** N/A — este contenido de plantilla debe eliminarse al pasar A.2 y A.3 a limpio, no
completarse.

