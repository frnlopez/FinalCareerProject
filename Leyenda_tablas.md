# Defectos de tablas y figuras del `.docx`

Censo exhaustivo de las 48 tablas y verificación de figuras el 2026-08-25 contra
`Proyecto_Fin_de_Grado-FJLM-2026.docx` (mtime 2026-08-25 07:05:43, 4.021.871 bytes).
Se localiza siempre por el fragmento literal, nunca por número de página ni de línea.

> [!note] Lo que el censo confirma que está BIEN (no volver a revisar)
> - Numeración «Tabla x.y» **contigua y sin duplicados** en 3.1-3.3, 4.1-4.13, 5.1-5.13, 6.1-6.5 y A.1-A.3.
> - Los **37 pies** van todos **debajo** de su tabla y **fuera** de ella.
> - Cero tablas anidadas.
> - Cero filas vacías.
> - Cero columnas inconsistentes.
> - Cero restos de Markdown **dentro** de las celdas.
> - Las **8 tablas-contenedor de ecuaciones** no necesitan pie.

## Defectos vivos

### Referencias cruzadas y numeración

- **Ninguna de las 37 tablas se llama por su número desde la prosa** · Cero apariciones de «Tabla 3.1»…«Tabla A.3» en párrafos de cuerpo. Lo que hay son referencias deícticas sin número («la tabla siguiente», «la tabla anterior»), que son justo la sede donde insertar la llamada. SEDES de ejemplo: Ctrl+F «La tabla siguiente recoge las métricas completas de los cuatro detectores», «La lectura conjunta de las cuatro matrices se resume en la tabla siguiente:», «La tabla siguiente compara los cuatro algoritmos en validación cruzada». ACCIÓN: sustituir cada deíctico por la llamada numerada («La Tabla 5.2 recoge…»).

  | Tabla | Localiza por (última frase del párrafo previo) | Nota |
  |---|---|---|
  | 3.1 | «…y el test se reserva íntegro para evaluar:» | |
  | 3.2 | «…todos implementables en scikit-learn[]:» | ojo, esa frase tiene además una cita vacía `[]` |
  | 3.3 | «Se comparan cuatro clasificadores supervisados, todos de la librería ya mencionada anteriormente, scikit-learn.» | |
  | 4.1 | «La tabla siguiente recoge las librerías directas y papel en el pipeline.» | |
  | 4.2 | «…quedan con las dimensiones siguientes (verificadas por el reporte de validación, integridad APROBADA):» | |
  | 4.3 | «…agrupa cada tipo en una de las cinco categorías canónicas de la literatura de NSL-KDD:» | |
  | 4.4 | «…tras el escalado 4 características de D2 quedan fuera del intervalo [0, 1]:» | |
  | 4.5 | «Los resultados sobre el set primario de 54 características son:» | |
  | 4.6 | «…sobre ambas variantes y comparar recall 0-day por tipo y f1_macro.» | |
  | 4.7 | «…el pipeline genera tres divisiones especializadas a partir de los conjuntos oficiales de NSL-KDD:» | |
  | 4.8 | «D3 está extremadamente desbalanceado. Su distribución por categorías es:» | |
  | 4.9 | «Las cuatro transformaciones del pipeline que aprenden algo de los datos son estas, y ninguna ve D2 en su ajuste:» | |
  | 4.10 | «…comparación amplia de algoritmos con búsquedas contenidas, no optimización exhaustiva de uno solo):» | |
  | 4.11 | «Resultado de la selección por AUC-ROC de validación sobre el set de 54 características:» | |
  | 4.12 | — | **no hay prosa previa**: la tabla arranca pegada al título «Algoritmos y espacios de búsqueda». Hay que escribir una frase introductoria |
  | 4.13 | «…el modelo final de cada algoritmo se re-ajusta sobre todo D3 con su mejor configuración):» | |
  | 5.1 | «La lectura conjunta de las cuatro matrices se resume en la tabla siguiente:» | |
  | 5.2 | «La tabla siguiente recoge las métricas completas de los cuatro detectores sobre D2…» | |
  | 5.3 | «La tabla siguiente compara los cuatro algoritmos en validación cruzada (StratifiedKFold(5) sobre D3) y sobre D2:» | |
  | 5.4 | «El desglose por categoría (F1 sobre D2, con el soporte de cada clase) muestra dónde se decide realmente la comparación:» | |
  | 5.5 | «La comparación entre las variantes de 54 y 122 características aporta el hallazgo más relevante de la sección:» | |
  | 5.6 | «…de los dos mejores algoritmos en la variante de 54 características se solapan ampliamente:» | |
  | 5.7 | «De esas 13, 5 proceden de la tabla de firmas:» | |
  | 5.8 | «Las métricas por alcance de la cascada son:» | |
  | 5.9 | «Las columnas de D2 de la tabla siguiente son puramente informativas (análisis de sensibilidad); en ningún caso intervinieron en la elección.» | |
  | 5.10 | «…porque cada detector alarma con distinta frecuencia sobre tráfico normal.» | |
  | 5.11 | «…y evaluado sobre D2 completo.» | |
  | 5.12 | «Superan el filtro los siete baselines canónicos del artículo que creó el dataset [23]…» | |
  | 5.13 | «…y una prevalencia de ataque *p* que se hace variar:» | ojo, esa frase tiene Markdown residual |
  | 6.1 | «…no que el error quede eliminado.» | |
  | 6.2 | «Las líneas se agrupan en dos bloques:» | |
  | 6.3 | «…muestra que ningún detectordomina a los demás en todos los tipos, y que sus puntos ciegos no coinciden:» | ojo, «detectordomina» va pegado |
  | 6.4 | «Pero la medición en las dos variantes muestra que el óptimo no es el mismo para cada etapa:» | |
  | 6.5 | «…es, sobre este dataset, inejecutable, y conviene decir por qué antes de proponerla.» | |
  | A.1 | — | no hay prosa previa; el título «Características básicas (1–9)» va directo a la tabla |
  | A.2 | — | **no hay prosa previa**: pegada al título «Codificación de categorías». Hay que escribir una frase introductoria |
  | A.3 | «…únicos detectables por la etapa de anomalías (véase [[5.3 Resultados del sistema híbrido]]).» | ojo, wikilink sin convertir |

- **Catorce figuras tampoco se llaman por número desde la prosa** · SEDE: 3.1, 4.1, 4.2, 4.3, 4.4, 4.5, 5.5, 5.6, 5.7, 5.8, 5.9, 5.10, 5.11 y 5.12. Cero apariciones de «Figura N.M» fuera del propio pie. Sí la llevan la 2.1, la 2.5 y las 5.1–5.4.

  | Figura | Localiza por (última frase del párrafo que la introduce) | Qué añadir |
  |---|---|---|
  | 3.1 | «…lo asigna a una categoría de ataque conocida o lo marca como desconocido.» | añadir al final: «La Figura 3.1 resume este flujo.» |
  | 4.1 | «…la cobertura de tipos entre train y test:» | «…entre train y test (Figura 4.1):» |
  | 4.2 | «…que confirma visualmente la pureza de D1/D3 y el desbalance de D3.» | añadir «(Figura 4.2)» antes del punto |
  | 4.3 | «…más discriminantes (verde = normal, rojo = ataque):» | «…(verde = normal, rojo = ataque) (Figura 4.3):» |
  | 4.4 | «…entre D1 y D2, característica a característica:» | «…característica a característica, como recoge la Figura 4.4:» |
  | 4.5 | «…por característica y subconjunto:» | «…por característica y subconjunto (Figura 4.5):» |
  | 5.5 y 5.6 | «…con independencia del umbral concreto:» | «…del umbral concreto (Figura 5.5 y Figura 5.6):» — un solo párrafo introduce las dos |
  | 5.7 a 5.10 | «…sobre los 9.083 flujos de tipos conocidos de D2 son las siguientes:» | «…son las siguientes (Figuras 5.7 a 5.10):» — un solo párrafo introduce las cuatro |
  | 5.11 | «…sobre D2 completo» | al separar la imagen, cerrar con «…sobre D2 completo, que recoge la Figura 5.11:» |
  | 5.12 | «…puede leerse en las matrices de confusión.)» | añadir después: «La Figura 5.12 muestra la del baseline.» |

- **Ningún pie de tabla tiene marcador ni campo `SEQ`** · Los 37 pies son texto literal tecleado a mano; solo uno tiene `bookmarkStart`, y es una marca del índice de contenidos, no de referencia cruzada. Ninguno de los 40+ campos `REF` del documento apunta a una tabla: todos apuntan a epígrafes. CONSECUENCIA: no se puede generar índice de tablas ni renumerar automáticamente, y cualquier inserción o borrado de tabla obliga a renumerar a mano.

- **No existen índice de figuras ni índice de tablas** · El único campo `TOC` del documento es el del índice de contenidos. ACCIÓN: pendiente de decisión de Francisco. Recomendación: añadirlos y pasar la numeración a campos `SEQ`, porque es la única corrección de la lista que además previene defectos futuros.

- **Los 60 pies del documento están en estilo Normal** · 23 pies «Figura x.y» + 37 «Tabla x.y»/«Tabla A.x», los 60 en Normal. `FiguraTablaEcuacin` lo usan 17 párrafos y son solo las ecuaciones. La objeción de Francisco es correcta en el fondo: ese estilo agranda la letra y no sirve como pie. Dato nuevo del censo: **el estilo `Descripción` (Caption) ya existe en `styles.xml` del documento** y no lo usa nadie. ACCIÓN: aplicar `Descripción` a los 60 pies. Es requisito previo para los índices.

### Apéndice A

- **La leyenda única no se lee como leyenda de las cuatro tablas** · SEDE: Ctrl+F «Tabla A.1. Características del dataset completo NSL-KDD.». La decisión de Francisco de **no fusionar** las cuatro tablas se respeta y no se vuelve a plantear: quedan partidas, con una sola leyenda al final de la cuarta. El problema real, verificado: entre la primera tabla y la leyenda hay **cuatro tablas y tres títulos de nivel `Título 8`** intercalados; en la maquetación final esa leyenda cae justo debajo del bloque «host (32–41)», y un lector la leerá como pie de esa subtabla, no del conjunto. Las tres anteriores quedan sin nada. ACCIÓN: no fusionar, sino **hacer explícito el alcance en la propia redacción de la leyenda**. Redacción propuesta:

  > Tabla A.1. Características del dataset completo NSL-KDD, desglosadas en los cuatro bloques anteriores: básicas (1–9), de contenido (10–22), de tráfico basadas en tiempo (23–31) y de tráfico basadas en host (32–41).

  Como refuerzo barato, conviene que la prosa introductoria del apéndice («Cada registro del dataset describe una conexión TCP/IP resumida en 41 atributos…») anuncie que la Tabla A.1 se presenta partida en cuatro bloques.

- **Título duplicado al abrir el Apéndice A** · SEDE: Ctrl+F «Columnas del dataset NSL-KDD» — aparece dos veces seguidas, en dos párrafos consecutivos con estilos `Título 6` y `Título 7`. ACCIÓN: borrar uno de los dos.

### Erratas de texto en pies y prosa de tablas

- **Markdown residual (backticks) en dos pies de tabla** · Ctrl+F «con la versión fijada en `requirements.txt`» (pie de la Tabla 4.1) y «evaluadas por `GridSearchCV`» (pie de la Tabla 4.12). ACCIÓN: quitar los backticks y dar formato de fuente monoespaciada, o dejar el texto llano.
- **Markdown residual en la prosa que introduce la Tabla 5.13** · Ctrl+F «y una prevalencia de ataque *p* que se hace variar». Lleva backticks alrededor de `bin_recall` y `bin_fpr` y cursiva Markdown `*p*`. Misma errata, sin backticks, en Ctrl+F «Las tres columnas se derivan solo de `bin_recall`».
- **Wikilinks de Obsidian sin convertir en 12 párrafos de prosa** · Ctrl+F «[[5.3 Resultados del sistema híbrido]]», «[[6.2 Líneas futuras]]», «[[4.5 Entrenamiento del modelo de detección basado en firmas|4.5]]». ACCIÓN: sustituir por la referencia normal al apartado.
- **Wikilink roto, con el texto del enlace corrompido** · Ctrl+F «[[5.1 Resultados del modelo de detección de anomalías el capítulo 5]]». El propio texto del enlace está mal formado.
- **Cita bibliográfica vacía** · Ctrl+F «todos implementables en scikit-learn[]». ACCIÓN: poner la cita que falte o quitar los corchetes.
- **Dos palabras pegadas en la prosa de la Tabla 6.3** · Ctrl+F «ningún detectordomina a los demás» y «está en 0,160frente al». ACCIÓN: separar.
- **Espacio sobrante al final del pie de la Tabla 5.11** · Ctrl+F «Tabla 5.11. Sistema híbrido frente al baseline de control». Es el único pie con espacio en blanco tras el punto final.
- **Tres llamadas de figura entre corchetes** · SEDE: Ctrl+F «a mano [Figura 2.2]», «el que corrige [Figura 2.3]», «previamente entrenado [Figura 2.4]». Motivo: en el tercer caso conviven en la misma frase el corchete de figura y el bibliográfico («…previamente entrenado [Figura 2.4]. [5]»), mismo delimitador para dos cosas distintas. Redacciones propuestas:
  - «…para corregirlas a mano, como muestra la Figura 2.2.»
  - «…el propio entrenamiento del algoritmo es el que corrige (Figura 2.3).»
  - «…a partir del algoritmo previamente entrenado, según se representa en la Figura 2.4 [5].»
- **Figura 5.11: la imagen sigue dentro del párrafo de prosa** · SEDE: Ctrl+F «sobre D2 completo». El pegote «completoFigura 5.11» ya está corregido y el pie ya es párrafo propio, pero el párrafo de prosa que termina en «…sobre D2 completo» conserva la imagen incrustada y no tiene punto final. ACCIÓN: sacar la imagen a párrafo propio y cerrar la prosa con dos puntos.

### Menores, a criterio de Francisco

- **Numeración de ecuaciones duplicada: «(1)» aparece dos veces** · Ctrl+F «La proyección es aritmética elemental sobre dos cifras ya publicadas». La ecuación de la proyección de precisión del capítulo 5 se numera «(1)», igual que la definición de Precisión del capítulo 2. ACCIÓN: renumerar la del capítulo 5 como «(8)», o adoptar numeración por capítulo.
- **Cabecera con celda vacía en la Tabla 6.1** · Ctrl+F «Error metodológico». La columna de códigos P1–P10 no tiene rótulo. ACCIÓN: poner un rótulo o dejarlo si es deliberado.
- **Tres tablas describen el mismo reparto D1/D2/D3** · Tabla 3.1 (`SUBCONJUNTO | CONTENIDO | PROPÓSITO`), Tabla 4.2 (`Subconjunto | Contenido | Instancias | Características`) y Tabla 4.7 (`Split | Contenido | Tamaño | Función`). Ctrl+F «Tabla 4.7. División especializada del NSL-KDD en D1, D2 y D3». No es un error, es redundancia: valorar si 3.1 y 4.7 se fusionan o si una de las dos se remite a la otra.

## Decisiones pendientes de Francisco

- **Índices de figuras y de tablas:** decidir si se añaden. Requiere antes aplicar el estilo `Descripción` a los 60 pies y, para renumeración automática, pasar a campos `SEQ`.
- **Redundancia entre las Tablas 3.1, 4.2 y 4.7:** decidir si se fusionan o se dejan.
