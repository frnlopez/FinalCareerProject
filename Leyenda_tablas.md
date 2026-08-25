# Defectos de tablas y figuras del `.docx`

Recuento y sedes verificados el 2026-08-25 contra `Proyecto_Fin_de_Grado-FJLM-2026.docx`
(mtime 2026-08-25 07:05:43, 4.021.871 bytes). De los 17 defectos originales, **11 quedaron
resueltos y 6 siguen vivos**. Se localiza siempre por el fragmento literal.

## Defectos vivos

- **Apéndice A: siguen siendo cuatro tablas y solo una leyenda** · SEDE: Ctrl+F «Características de tráfico basadas en tiempo (23–31)». Francisco indicó haber dejado una sola tabla, pero **en el binario siguen cuatro**:
  - «Características básicas (1–9)» — 9 filas de datos
  - «Características de contenido (10–22)» — 13 filas
  - «Características de tráfico basadas en tiempo (23–31)» — 9 filas
  - «Características de tráfico basadas en host (32–41)» — 10 filas

  La única leyenda, «Tabla A.1. Características del dataset completo NSL-KDD.», va tras la cuarta tabla y no cubre a las tres anteriores. ACCIÓN: o fusionar de verdad las cuatro en una sola tabla continua (que es lo decidido), o dar pie propio a cada una. Observación menor: los cuatro encabezados usan hoy el estilo `Título 8`, pero el índice los lista como «A.1.1…A.1.4».

- **Figura 5.11: la imagen sigue dentro del párrafo de prosa** · SEDE: Ctrl+F «sobre D2 completo». El pegote «completoFigura 5.11» ya está corregido y el pie ya es párrafo propio, pero el párrafo de prosa que termina en «…sobre D2 completo» conserva la imagen incrustada y además no tiene punto final. ACCIÓN: sacar la imagen a párrafo propio y cerrar la prosa con dos puntos.

- **Catorce figuras no se llaman por número desde la prosa** · SEDE: 3.1, 4.1, 4.2, 4.3, 4.4, 4.5, 5.5, 5.6, 5.7, 5.8, 5.9, 5.10, 5.11 y 5.12. Para las catorce hay cero apariciones de «Figura N.M» fuera del propio pie. Sí la llevan la 2.1, la 2.5 y las 5.1–5.4.

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

- **Tres llamadas de figura entre corchetes** · SEDE: Ctrl+F «a mano [Figura 2.2]», «el que corrige [Figura 2.3]», «previamente entrenado [Figura 2.4]». Sí se ve mal, y el motivo concreto es el tercer caso: conviven en la misma frase el corchete de figura y el bibliográfico («…previamente entrenado [Figura 2.4]. [5]»), mismo delimitador para dos cosas distintas. Redacciones propuestas:
  - «…para corregirlas a mano, como muestra la Figura 2.2.»
  - «…el propio entrenamiento del algoritmo es el que corrige (Figura 2.3).»
  - «…a partir del algoritmo previamente entrenado, según se representa en la Figura 2.4 [5].»

- **Los 60 pies del documento están en estilo Normal** · Recuento verificado: 60 pies (23 «Figura x.y» + 37 «Tabla x.y»/«Tabla A.x»), los 60 en estilo Normal. `FiguraTablaEcuacin` lo usan exactamente 17 párrafos y son solo las ecuaciones. La objeción de Francisco es correcta en el fondo: `FiguraTablaEcuacin` agranda la letra y no sirve como estilo de pie. Lo que hace falta **no** es aplicar ese estilo, sino **usar un estilo de pie propio** (tipo `Descripción`/`Caption` de Word, cuerpo menor que el texto). CONSECUENCIA: sin ningún estilo de pie no se puede generar índice de figuras ni de tablas.

- **No existen índice de figuras ni índice de tablas, ni numeración automática** · Cero apariciones de «Índice de figuras» / «Índice de tablas»; **cero campos `SEQ`**: todos los «Figura 5.1» y «Tabla 4.2» son texto tecleado a mano, que es la causa de que hubiera cuatro pies sin espacio tras el punto. Hay un único `TOC`, el de contenidos. ACCIÓN: pendiente de decisión de Francisco. Recomendación: añadirlos y pasar la numeración a campos `SEQ`, porque es la única corrección de la lista que además previene defectos futuros.

## Decisiones pendientes de Francisco

- **Apéndice A:** fusionar las cuatro tablas en una sola tabla continua con un único pie A.1, o dar pie propio a cada una de las cuatro.
- **Índices de figuras y de tablas:** decidir si se añaden. Si se añaden, requiere antes definir y aplicar un estilo de pie (los 60 pies están hoy en Normal).
