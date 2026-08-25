# Defectos de tablas y figuras del `.docx`

Recuento y sedes verificados el 2026-08-25 contra `Proyecto_Fin_de_Grado-FJLM-2026.docx`
(mtime 2026-08-25 05:07), volcado en `Resultados\docx\REPASO_20260825\`.
Localiza siempre por el fragmento literal; el `p<NNNN>` es solo pista auxiliar.

## Defectos vivos

- **Tabla 5.3 anidada dentro de otra tabla, con su pie dentro de la celda** · SEDE: Ctrl+F «Tabla 5.3. Clasificadores de firmas en validación cruzada sobre D3» (p1705; la envoltura empieza en p1679). ACCIÓN: deshacer la tabla exterior, dejar solo la tabla de datos `Algoritmo / Balanceo / f1_macro (CV, D3) / f1_macro (D2) / Accuracy (D2)` y sacar el pie a un párrafo propio debajo de ella.
- **Tres tablas del Apéndice A sin pie** · SEDE: Ctrl+F «Características básicas (1–9)» (p2654, 10 filas), «A.1.2 Características de contenido (10–22)» (p2695, 14 filas) y «A.1.3 Características de tráfico basadas en tiempo (23–31)» (p2752, 10 filas). ACCIÓN: insertar debajo de cada tabla su pie; el único pie que hoy existe en el bloque, «Tabla A.1. Características del dataset completo NSL-KDD», va tras la cuarta tabla (host, 32–41) y pretende cubrir las cuatro. Leyendas propuestas, supeditadas a la decisión 2:
  - Básicas (1–9): «Características básicas (1–9): atributos de la propia conexión TCP/IP, extraíbles de sus cabeceras.»
  - Contenido (10–22): «Características de contenido (10–22): atributos obtenidos inspeccionando la carga útil, orientados a los ataques r2l y u2r.»
  - Tiempo (23–31): «Características de tráfico basadas en tiempo (23–31): estadísticas sobre la ventana de las conexiones de los dos últimos segundos.»
  - Host (32–41): «Características de tráfico basadas en host (32–41): estadísticas sobre la ventana de las 100 conexiones anteriores al mismo destino.»
- **Pie sin espacio tras el punto — Tabla 4.2** · SEDE: Ctrl+F «Tabla 4.2.Dimensiones de los tres subconjuntos» (p0976). ACCIÓN: insertar un espacio tras el punto.
- **Pie sin espacio tras el punto — Tabla 4.5** · SEDE: Ctrl+F «Tabla 4.5.Mini-experimento de balanceo» (p1166). ACCIÓN: insertar un espacio tras el punto.
- **Pie sin espacio tras el punto — Tabla 5.4** · SEDE: Ctrl+F «Tabla 5.4.F1 por categoría de ataque» (p1764). ACCIÓN: insertar un espacio tras el punto.
- **Pie sin espacio tras el punto — Tabla 5.5** · SEDE: Ctrl+F «Tabla 5.5.Efecto del conjunto de características» (p1797). ACCIÓN: insertar un espacio tras el punto.
- **Tabla A.1 sin punto final** · SEDE: Ctrl+F «Tabla A.1. Características del dataset completo NSL-KDD» (p2841). ACCIÓN: añadir el punto final; su alcance queda resuelto con la decisión 2.
- **Figura 3.1 sin punto final** · SEDE: Ctrl+F «Figura 3.1. Flujo del proyecto» (p0707). ACCIÓN: añadir el punto final.
- **Dos celdas de la Tabla 5.8 empiezan por pipe de Markdown** · SEDE: Ctrl+F «| 5 clases, criterio conservador (n = 22.544)» y «| f1_macro (unknown = error)» (p1949 y p1950). ACCIÓN: borrar el `|` inicial y el espacio siguiente. Los demás `|` del documento son la notación legítima `|r| > 0,95`.
- **Pie de figura en el mismo párrafo que la imagen — Figura 5.1** · SEDE: Ctrl+F «Figura 5.1. Matriz de confusión binaria (normal frente a ataque) de IsolationForest» (p1537). ACCIÓN: separar el pie en párrafo propio.
- **Pie de figura en el mismo párrafo que la imagen — Figura 5.6** · SEDE: Ctrl+F «Figura 5.6. Curvas precisión-recall de los cuatro detectores» (p1644). ACCIÓN: separar el pie en párrafo propio.
- **Pie de la Figura 5.11 pegado a la prosa y a la imagen, sin puntuación intermedia** · SEDE: Ctrl+F «sobre D2 completoFigura 5.11. Matriz de confusión del sistema híbrido sobre D2 completo» (p1936). ACCIÓN: cerrar la prosa con dos puntos y separar el pie en párrafo propio. Es la razón de que el documento tenga 23 imágenes y solo 22 pies detectables como tales.
- **Pie de figura en el mismo párrafo que la imagen — Figura 5.12** · SEDE: Ctrl+F «Figura 5.12. Matriz de confusión del baseline de control» (p2173). ACCIÓN: separar el pie en párrafo propio.
- **Catorce figuras no se llaman por número desde la prosa** · SEDE: 3.1, 4.1, 4.2, 4.3, 4.4, 4.5, 5.5, 5.6, 5.7, 5.8, 5.9, 5.10, 5.11 y 5.12 (catorce). Sí llevan llamada la 2.1 (Ctrl+F «se ilustra en la Figura 2.1», p0308), la 2.5 (Ctrl+F «representada en la Figura 2.5», p0513) y las 5.1, 5.2, 5.3 y 5.4 (Ctrl+F «Las cuatro figuras siguientes (Figura 5.1, 5.2, 5.3 y 5.4)», p1536); las 2.2, 2.3 y 2.4 la llevan entre corchetes, defecto tratado en la viñeta siguiente. ACCIÓN: añadir en el párrafo que introduce cada una una llamada del tipo «…como muestra la Figura 4.1».
- **Tres llamadas de figura entre corchetes, confundibles con una cita `[n]`** · SEDE: Ctrl+F «a mano [Figura 2.2]», «el que corrige [Figura 2.3]», «previamente entrenado [Figura 2.4]». ACCIÓN: sustituir por «la Figura 2.2», «la Figura 2.3» y «la Figura 2.4».
- **Los 59 pies del documento no usan el estilo de pie de la plantilla** · SEDE: los 34 pies «Tabla x.y», los 3 pies «Tabla A.x» (Ctrl+F «Tabla A.1. Características del dataset completo NSL-KDD», «Tabla A.2. Codificación numérica», «Tabla A.3. Los 40 tipos de etiqueta») y los 22 pies «Figura x.y»; todos figuran en estilo Normal (`-` en el volcado). El estilo `FiguraTablaEcuacin` lo usan 17 párrafos y son **exclusivamente las ecuaciones** (p0426–p0458, `(1)`…`(7)`, y p2294–p2295, el `(1)` de §5.4). CONSECUENCIA: ningún índice de figuras ni de tablas puede generarse automáticamente —Word los construye a partir de ese estilo o de campos SEQ— y la maquetación de los pies no es homogénea con la plantilla. ACCIÓN: aplicar el estilo `FiguraTablaEcuacin` a los 59 párrafos de pie, **después** de separar los cuatro pies hoy pegados al párrafo de la imagen (Figuras 5.1, 5.6, 5.11 y 5.12, listadas arriba).
- **No existen índice de figuras ni índice de tablas** · SEDE: cero apariciones de «Índice de figuras» y «Índice de tablas» en el documento; el único índice es el de contenido. ACCIÓN: pendiente de la decisión 4.

## Corregidos desde la versión anterior

- La **Tabla 5.3 ya no está vacía**: contiene los cuatro clasificadores con sus cifras (lo que queda es el anidamiento, listado arriba). Ya **no hay ninguna imagen VML** en §6.2.6 —el documento tiene 0 VML y 23 DrawingML—, así que decaen tanto «una imagen sin pie» como la propuesta de `Figura 6.1`. **No hay imagen huérfana**: las 23 tienen pie, y el hueco aparente de la `Figura 5.11` es el pie pegado a la prosa. Los pies **A.1, A.2 y A.3 sí existen** en el Apéndice A.

## Decisiones pendientes de Francisco

- **Posición del pie de tabla:** hoy todos van debajo salvo el de la Tabla 5.3, que está dentro. ¿Se mantienen debajo o la plantilla los exige encima?
- **Numeración del Apéndice A:** cuatro bloques con pie propio (A.1–A.4, desplazando los actuales A.2 y A.3 a A.5 y A.6) o una sola tabla continua con un único pie A.1.
- **Censo de la Figura 3.1:** existe en el `.docx` pero no en el censo declarado del vault. Decidir si se incorpora.
- **Índices de figuras y de tablas:** el documento no los tiene. Decidir si se añaden. Si se añaden, requiere antes aplicar el estilo `FiguraTablaEcuacin` a los 59 pies, hoy en estilo Normal (defecto listado arriba), porque Word genera estos índices a partir de ese estilo o de campos SEQ.
