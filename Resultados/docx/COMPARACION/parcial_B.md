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
