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
