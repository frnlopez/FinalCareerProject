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
