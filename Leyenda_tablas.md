# Defectos de tablas y figuras del `.docx`

Censo exhaustivo de las 48 tablas y verificación de figuras contra
`Proyecto_Fin_de_Grado-FJLM-2026.docx`. **Poda del 2026-08-25 (21:06)** hecha contra el volcado
fresco `Resultados/docx/REPASO_20260825-2106/` del binario **mtime 2026-08-25T21:06:08, 4.023.965 bytes**.
Se localiza siempre por el fragmento literal, nunca por número de página ni de línea.

Recuentos frescos del binario actual: **2.989 párrafos · 48 tablas · 37 pies de tabla** (34 «Tabla
`<dígito>`» + 3 «Tabla A.x») **· 23 pies de figura · 93 marcadores `[n]` · 109 párrafos de TOC**.

- **Lo resuelto se borra, no se archiva.** Este fichero no lleva censo de retiradas: el rastro vive
  en el commit `16fd538` y en `features.md`. Lo que aparece aquí abajo está **vivo**.
- **Frontera con `Las tareas de Kiko.md`:** todo lo que sea **defecto de tabla, de figura, de pie o
  de la prosa que los introduce** vive aquí. Lo que sea **prosa del cuerpo** vive allí. Cuando un
  defecto toca los dos lados, se escribe **una sola vez** y el otro fichero remite.
- **Dónde se arregla: `Word` salvo mención expresa.** Todo lo de este fichero es maquetación,
  estilo de pie, numeración o prosa introductoria de una tabla o figura, y eso se toca en el
  `.docx`. Las entradas que además (o en vez de eso) tocan la nota `.md` del vault llevan su
  etiqueta `vault` escrita en la propia entrada. Misma convención que en `Las tareas de Kiko.md`:
  `Word` = se arregla en el `.docx` · `vault` = se arregla en la nota `.md`.

> [!note] Lo que el censo confirma que está BIEN (no volver a revisar)
> - Numeración «Tabla x.y» **contigua y sin duplicados** en 3.1-3.3, 4.1-4.13, 5.1-5.13, 6.1-6.5 y A.1-A.3 (37, reverificado el 2026-08-25 21:06).
> - Numeración «Figura x.y» **contigua y sin duplicados** en 2.1-2.5, 3.1, 4.1-4.5 y 5.1-5.12 (23, reverificado el 2026-08-25 21:06).
> - Los **37 pies** van todos **debajo** de su tabla y **fuera** de ella.
> - Los **23 pies de figura** son párrafo propio, **sin excepciones** — el de la Figura 5.11 también lo es. Lo que sigue vivo en esa figura **no es el pie, sino la imagen**, que continúa incrustada en el párrafo de prosa: ver la viñeta «Figura 5.11: la imagen sigue dentro del párrafo de prosa», más abajo. **No buscar ahí un pie mal puesto: no lo hay.**
> - Cero tablas anidadas.
> - Cero filas vacías.
> - Cero columnas inconsistentes.
> - Cero restos de Markdown **dentro** de las celdas.
> - Las **8 tablas-contenedor de ecuaciones** no necesitan pie.
> - El pie «Tabla A.1. Características del dataset completo NSL-KDD.» **ya cierra con punto**.

## Defectos vivos

> [!info] Censo de esta lista, para que el número no vuelva a designar dos conjuntos
> Recuento hecho **contando las viñetas** tras la poda de duplicados del 2026-08-25:
> - **10 defectos vivos**, de los que **9 están verificados** contra el volcado del 21:06 y **1 va
>   marcado ⚠️ NO VERIFICADO** (los marcadores y campos `SEQ` de los pies: el volcado de texto no
>   extrae códigos de campo de Word, así que esa afirmación no es comprobable por esta vía).
> - **1 de esos 10 ha pasado a ser remisión pura** tras la corrección del 2026-08-26: «Dos palabras
>   pegadas en la prosa de la Tabla 6.3», cuya sede con fragmento y acción es la tarea **5.32** de
>   `Las tareas de Kiko.md`. Sigue contando como viñeta, pero **aquí no hay nada que ejecutar**.
> - **2 remisiones puras** en el bloque «Apéndice A» —el título duplicado del cuerpo y la entrada
>   repetida del TOC—, que **no son defectos de este fichero**: son prosa del cuerpo y son índice,
>   así que su sede única está en `Las tareas de Kiko.md` (**A6** y **T8**). Se conservan como una
>   línea de remisión para que nadie las vuelva a fichar aquí.
> - **3 menores + 1 remisión**, degradados a «si sobra tiempo»: bajo el encabezado «Menores, a
>   criterio de Francisco» hay **cuatro** viñetas, pero la cuarta («Redundancia D1/D2/D3 entre tres
>   tablas») es solo un puntero a la decisión de Francisco de más abajo, no un menor.
> - **2 decisiones pendientes de Francisco**, que no son defectos.
>
> **Ojo al leer el historial:** las cifras antiguas de este callout («17 originales», «18 viñetas
> vivas») designaban conjuntos distintos, porque la lista se ha rehecho y reagrupado varias veces.
> Cuenta las viñetas; no te fíes de ninguna cifra heredada.

### Referencias cruzadas y numeración

- **Ninguna de las 37 tablas se llama por su número desde la prosa** · Cero apariciones de «Tabla 3.1»…«Tabla A.3» en párrafos de cuerpo. Lo que hay son referencias deícticas sin número («la tabla siguiente», «la tabla anterior»), que son justo la sede donde insertar la llamada. SEDES de ejemplo: Ctrl+F «La tabla siguiente recoge las métricas completas de los cuatro detectores», «La lectura conjunta de las cuatro matrices se resume en la tabla siguiente:», «La tabla siguiente compara los cuatro algoritmos en validación cruzada». ACCIÓN: sustituir cada deíctico por la llamada numerada («La Tabla 5.2 recoge…»). **No se recorta por caro**: sin llamada por número no hay referencia cruzada desde el texto. Es la sede única de la tarea **T6** de `Las tareas de Kiko.md`.

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
  | 4.12 | — | **no hay prosa previa**: la tabla arranca pegada a un título «Algoritmos y espacios de búsqueda». ⚠️ Hay **dos** títulos con ese texto exacto en el cuerpo (§4.4.2 y §4.5.2), más sus dos entradas de índice: son **4 coincidencias** de Ctrl+F. El que toca es el **segundo del cuerpo**, el de §4.5.2, el que precede a la Tabla 4.12. Hay que escribir una frase introductoria |
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
  | 5.12 | «Superan el filtro los siete baselines canónicos del artículo que creó el dataset [44]…» | el marcador es hoy `[44]`, no `[23]`: lo cambió una de las reescrituras X1–X30, ya cumplidas en el binario del 21:06 (ver el callout del bloque 🔴 PRIORITARIO de `Las tareas de Kiko.md`) |
  | 5.13 | «…y una prevalencia de ataque *p* que se hace variar:» | ojo, esa frase tiene Markdown residual (ver «Markdown residual») |
  | 6.1 | «…no que el error quede eliminado.» | |
  | 6.2 | «Las líneas se agrupan en dos bloques:» | |
  | 6.3 | «…muestra que ningún detectordomina a los demás en todos los tipos, y que sus puntos ciegos no coinciden:» | ojo, «detectordomina» va pegado: ver la viñeta «Dos palabras pegadas en la prosa de la Tabla 6.3» de este fichero, que remite a la barrida única de la tarea **5.32** de `Las tareas de Kiko.md` |
  | 6.4 | «Pero la medición en las dos variantes muestra que el óptimo no es el mismo para cada etapa:» | |
  | 6.5 | «…es, sobre este dataset, inejecutable, y conviene decir por qué antes de proponerla.» | |
  | A.1 | — | no hay prosa previa; el título «Características básicas (1–9)» va directo a la tabla |
  | A.2 | — | **no hay prosa previa**: pegada al título «Codificación de categorías». Hay que escribir una frase introductoria |
  | A.3 | «…únicos detectables por la etapa de anomalías (véase [[5.3 Resultados del sistema híbrido]]).» | ojo, wikilink sin convertir: lo cubre **T5** de `Las tareas de Kiko.md` |

- **Catorce figuras tampoco se llaman por número desde la prosa** · SEDE: 3.1, 4.1, 4.2, 4.3, 4.4, 4.5, 5.5, 5.6, 5.7, 5.8, 5.9, 5.10, 5.11 y 5.12. Cero apariciones de «Figura N.M» fuera del propio pie. Sí la llevan la 2.1 (dos veces), la 2.5 y el bloque 5.1–5.4. Es la sede única de la tarea **T7** de `Las tareas de Kiko.md`. Mismo criterio que con las tablas: **no se recorta por caro**.

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
  | 5.11 | «las cinco categorías más la columna unknown), sobre D2 completo» ⚠️ **usar este fragmento, no «sobre D2 completo» a secas**: el corto da **4 coincidencias** (una de ellas la prosa de la Tabla 5.11, que es otro párrafo y otra tarea); el largo da **1** | al separar la imagen, cerrar con «…sobre D2 completo, que recoge la Figura 5.11:» |
  | 5.12 | «…puede leerse en las matrices de confusión.)» | añadir después: «La Figura 5.12 muestra la del baseline.» |

- ⚠️ NO VERIFICADO (el volcado de texto no extrae marcadores de Word ni códigos de campo) · **Ningún pie de tabla tiene marcador ni campo `SEQ`** · Los 37 pies son texto literal tecleado a mano; solo uno tiene `bookmarkStart`, y es una marca del índice de contenidos, no de referencia cruzada. Ninguno de los 40+ campos `REF` del documento apunta a una tabla: todos apuntan a epígrafes. CONSECUENCIA: no se puede generar índice de tablas ni renumerar automáticamente, y cualquier inserción o borrado de tabla obliga a renumerar a mano. Hay que comprobarlo con el `.docx` abierto antes de darlo por bueno.

- **Los 60 pies del documento están en estilo Normal** · 23 pies «Figura x.y» + 37 «Tabla x.y»/«Tabla A.x», los 60 en Normal (`estilos_usados.txt` no registra ni un uso del estilo `Descripción`). `FiguraTablaEcuacin` lo usan 17 párrafos y son solo las ecuaciones. La objeción de Francisco es correcta en el fondo: ese estilo agranda la letra y no sirve como pie. Dato del censo: **el estilo `Descripción` (Caption) ya existe en `styles.xml` del documento** y no lo usa nadie. ACCIÓN: aplicar `Descripción` a los 60 pies. **Es requisito previo** de la decisión de los índices (ver «Decisiones pendientes de Francisco», más abajo). `Word`

### Apéndice A

- **La leyenda única no se lee como leyenda de las cuatro tablas** · SEDE: Ctrl+F «Tabla A.1. Características del dataset completo NSL-KDD.». La decisión de Francisco de **no fusionar** las cuatro tablas se respeta y no se vuelve a plantear: quedan partidas, con una sola leyenda al final de la cuarta. El problema real, verificado: entre la primera tabla y la leyenda hay **cuatro tablas y tres títulos de nivel `Título 8`** intercalados («Características de contenido (10–22)», «…basadas en tiempo (23–31)», «…basadas en host (32–41)»); en la maquetación final esa leyenda cae justo debajo del bloque «host (32–41)», y un lector la leerá como pie de esa subtabla, no del conjunto. Las tres anteriores quedan sin nada. ACCIÓN: no fusionar, sino **hacer explícito el alcance en la propia redacción de la leyenda**. Redacción propuesta:

  > Tabla A.1. Características del dataset completo NSL-KDD, desglosadas en los cuatro bloques anteriores: básicas (1–9), de contenido (10–22), de tráfico basadas en tiempo (23–31) y de tráfico basadas en host (32–41).

  Como refuerzo barato, conviene que la prosa introductoria del apéndice («Cada registro del dataset describe una conexión TCP/IP resumida en 41 atributos…») anuncie que la Tabla A.1 se presenta partida en cuatro bloques. `Word` + `vault` (la redacción de la leyenda y la frase del apéndice existen también en la nota del vault).

  > [!note] Esto NO es la disyuntiva de numeración
  > Aquí se decide **el alcance de la leyenda del pie A.1**: qué tiene que decir su texto para que se
  > lea como leyenda de los cuatro bloques. **Cuántos pies hay y cómo se numeran** (A.1–A.4 con pie
  > propio, desplazando los actuales A.2 y A.3) es otra cosa, y su sede única es la tarea **A5** de
  > `Las tareas de Kiko.md`. Si Francisco decide numerar los cuatro bloques por separado, esta
  > redacción ampliada deja de hacer falta.

- **Título duplicado al abrir el Apéndice A** → **remisión, no defecto de este fichero.** Es prosa
  del cuerpo (dos encabezados consecutivos), así que su **sede única con SEDE y ACCIÓN es la tarea
  A6** de `Las tareas de Kiko.md`. Aquí solo se anota para que nadie la refiche: afecta al Apéndice
  A, pero no a ninguna tabla, figura ni pie.

- **El TOC repite el mismo rótulo en dos niveles** → **remisión, no defecto de este fichero.** Un
  índice de contenidos no es tabla, figura ni pie: su **sede única con la evidencia de
  `indice_toc.txt` y la acción es la tarea T8** de `Las tareas de Kiko.md`, que además la liga a
  A6. Aquí solo se anota para que nadie la refiche.

### Erratas de texto en pies y prosa de tablas

- **Markdown residual: una sola barrida de Ctrl+F** · Cuatro pares de backticks en tres párrafos, más una cursiva Markdown. Se hacen **de una vez**, porque en Word es el mismo gesto de edición: quitar el delimitador y aplicar el formato real (fuente monoespaciada o cursiva). ACCIÓN por sede:
  - **Pie de la Tabla 4.1** · Ctrl+F «con la versión fijada en `requirements.txt`» → quitar los backticks y dar monoespaciada, o dejar el texto llano.
  - **Pie de la Tabla 4.12** · Ctrl+F «evaluadas por `GridSearchCV`» → ídem.
  - **Prosa posterior a la Tabla 5.13** · Ctrl+F «Las tres columnas se derivan solo de `bin_recall` y `bin_fpr` medidos» → dos pares en la misma frase; ídem.
  - **Prosa que introduce la Tabla 5.13** · Ctrl+F «y una prevalencia de ataque *p* que se hace variar» → **cursiva Markdown `*p*`**: sustituir los asteriscos por cursiva de Word. Es la tarea **5.17** de `Las tareas de Kiko.md`, que remite aquí y no se duplica allí.

  > [!note] Barrido completo, para no volver a buscar
  > Contados en el volcado del 21:06: **4 pares de backticks vivos en 3 párrafos** (`documento.txt`
  > líneas de los pies p0914 y p1414, y el párrafo p2333) y **una sola cursiva `*p*`** (p2309).
  > `tablas.txt` no tiene ninguno: **dentro de las celdas no queda Markdown**. Los «tres pares
  > nuevos, fuera del alcance de 5.17» que se sospechaban tras la poda anterior **no existen como
  > hallazgo aparte**: son los que ya recogen las sub-viñetas de arriba, porque el párrafo original
  > de 5.17 (p2309, «La proyección es aritmética elemental…») ya perdió los suyos y solo conserva
  > el `*p*`.

- **Dos palabras pegadas en la prosa de la Tabla 6.3** → **remisión, no ficha de este fichero.** Falta el espacio entre dos palabras en la prosa que introduce la Tabla 6.3. **Sus dos sedes, con fragmento de Ctrl+F y acción, están en la tarea 5.32** de `Las tareas de Kiko.md`, que las hace de una sola pasada junto con las otras tres palabras pegadas del cuerpo. Aquí solo se anota para que nadie las refiche.

- **Cita bibliográfica vacía** · Ctrl+F «todos implementables en scikit-learn[]». ACCIÓN: poner la cita que falte o quitar los corchetes. Es la frase que además introduce la Tabla 3.2, así que se aprovecha el mismo paso que la llamada numerada.

- **Tres llamadas de figura entre corchetes, y un `[5]` que queda huérfano** · SEDE: Ctrl+F «a mano [Figura 2.2]», «el que corrige [Figura 2.3]», «previamente entrenado [Figura 2.4]». Motivo: en el tercer caso conviven en la misma frase el corchete de figura y el bibliográfico, con el agravante verificado de que **el marcador queda suelto detrás del punto**, como si fuera una frase propia: el párrafo termina literalmente «…a partir del algoritmo previamente entrenado [Figura 2.4]. [5]». Mismo delimitador para dos cosas distintas, y una referencia que no se lee ligada a nada. Redacciones propuestas:
  - «…para corregirlas a mano, como muestra la Figura 2.2.»
  - «…el propio entrenamiento del algoritmo es el que corrige (Figura 2.3).»
  - «…a partir del algoritmo previamente entrenado, según se representa en la Figura 2.4 [5].» ← esta reescritura **resuelve a la vez** el corchete y el `[5]` huérfano. `[5]` es Géron y está dentro del tramo congelado `[1]`–`[11]`: **el número no se toca**, solo se reubica dentro de la frase.

- **Figura 5.11: la imagen sigue dentro del párrafo de prosa** · SEDE: Ctrl+F **«las cinco categorías más la columna unknown), sobre D2 completo»** — **1 sola coincidencia**. ⚠️ **No buscar «sobre D2 completo» a secas: da 4 coincidencias**, y una de ellas («…y evaluado sobre D2 completo.») es la prosa que introduce la **Tabla** 5.11, que es otro párrafo y otro defecto. El pegote «completoFigura 5.11» ya está corregido y el pie ya es párrafo propio, pero ese párrafo de prosa conserva la imagen incrustada y no tiene punto final. ACCIÓN: sacar la imagen a párrafo propio y cerrar la prosa con dos puntos. Se hace **junto con** la llamada numerada de la Figura 5.11 (tabla de figuras, más arriba), que es el mismo párrafo y el mismo gesto: **las dos las cubre la tarea T7** de `Las tareas de Kiko.md`, no T6. `Word`

### Menores, a criterio de Francisco

Cosméticos. **Si sobra tiempo**: ninguno afecta al contenido ni a la trazabilidad.

- **Numeración de ecuaciones duplicada: «(1)» aparece dos veces** · Ctrl+F «La proyección es aritmética elemental sobre dos cifras ya publicadas». La ecuación de la proyección de precisión del capítulo 5 se numera «(1)», igual que la definición de Precisión del capítulo 2; las dos con estilo `FiguraTablaEcuacin`. ACCIÓN: renumerar la del capítulo 5 como «(8)», o adoptar numeración por capítulo. Es la sede única de la tarea **5.19** de `Las tareas de Kiko.md`, que remite aquí.
- **Cabecera con celda vacía en la Tabla 6.1** · Ctrl+F «Error metodológico». La columna de códigos P1–P10 no tiene rótulo (`tablas.txt`, TABLA 38, celda `[f1,c1]` vacía). ACCIÓN: poner un rótulo o dejarlo si es deliberado.
- **Espacio sobrante al final del pie de la Tabla 5.11** · Ctrl+F «Tabla 5.11. Sistema híbrido frente al baseline de control». Es el único de los 37 pies con espacio en blanco tras el punto final. Degradado a menor: no se ve al imprimir. **No confundir con la tarea 5.28** de `Las tareas de Kiko.md`, que es otra cosa —mantener esa tabla y su pie en la misma página— y sigue viva allí.
- **Redundancia D1/D2/D3 entre tres tablas** → no se decide aquí: la sede única es «Redundancia entre las Tablas 3.1, 4.2 y 4.7» en «Decisiones pendientes de Francisco», más abajo.

## Decisiones pendientes de Francisco

No son defectos: son elecciones que nadie puede tomar por él.

- **Índices de figuras y de tablas: decidir si se añaden.** Hoy **no existe ninguno de los dos**: el único campo `TOC` del documento es el del índice de contenidos, y sus 109 párrafos son todos `TDC1`/`TDC2`/`TDC3` (cero rótulos «Índice de tablas» o «Índice de figuras»). Precondiciones si se añaden: (1) aplicar el estilo `Descripción` a los 60 pies, y (2) para que la renumeración sea automática, pasar los números de los pies a campos `SEQ`, que hoy no tiene ninguno. Recomendación: hacerlo, porque es la única corrección de este fichero que además **previene defectos futuros** — mientras los números sean texto tecleado, insertar o borrar una tabla obliga a renumerar a mano. Es la misma decisión que la tarea **T10** de `Las tareas de Kiko.md`, que remite aquí.
- **Redundancia entre las Tablas 3.1, 4.2 y 4.7: decidir si se fusionan o se dejan.** Las tres describen el mismo reparto D1/D2/D3 con columnas distintas: Tabla 3.1 (`SUBCONJUNTO | CONTENIDO | PROPÓSITO`), Tabla 4.2 (`Subconjunto | Contenido | Instancias | Características`) y Tabla 4.7 (`Split | Contenido | Tamaño | Función`). Ctrl+F «Tabla 4.7. División especializada del NSL-KDD en D1, D2 y D3». No es un error, es redundancia: valorar si 3.1 y 4.7 se fusionan o si una de las dos remite a la otra (la 4.2 aporta dimensiones, que las otras dos no dan). Es el **candidato a recorte nº 5** de `Las tareas de Kiko.md`, que remite aquí y no repite el contenido.
