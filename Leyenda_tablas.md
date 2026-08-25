# Leyendas de las tablas

Pies para las **40 filas** listadas de `Proyecto_Fin_de_Grado-FJLM-2026.docx` (3 + 13 + 13 + 5 + 6),
que se corresponden con **37 pies reales** en el documento (ver la aritmética más abajo).
Cubre la tarea **T6**.

**Estado a hoy.** Las **37 tablas** del documento son **tablas reales de Word** con rejilla, y todas
llevan su pie «Tabla x.y». **Ninguna está volcada párrafo a párrafo ni en Markdown** (verificado en
el PDF `Proyecto_Fin_de_Grado-FJLM-2026.pdf`; este fichero venía afirmando lo contrario). Lo que
queda no es convertir ni insertar, sino **corregir los defectos** de la lista de abajo.

**Aritmética 40 → 37.** Las 40 filas de este fichero no son 40 pies en el `.docx`:

| Bloque | Filas listadas aquí | Pies reales en el `.docx` |
|---|---:|---:|
| Caps. 3 + 4 + 5 + 6 | 34 | 34 |
| Apéndice A | 6 | 3 (A.1, A.2, A.3) |
| **Total** | **40** | **37** |

La diferencia de 3 sale entera del Apéndice A: los cuatro bloques de características (básicas 1–9,
contenido 10–22, tiempo 23–31, host 32–41) **no son cuatro tablas, sino UNA tabla continua** partida
por subtítulos, cuya cabecera «# / Nombre / Tipo / Descripción» se repite en cada página; el pie
«Tabla A.1» al final las cubre las cuatro. 4 filas listadas → 1 pie real.

> Las páginas del PDF que se citen en este fichero son **páginas físicas**; la impresa es ≈ −13.

**Cómo se usa.** Cada entrada trae el ancla (búscala con Ctrl+F) y el texto de leyenda de
referencia. La numeración es correlativa por capítulo.

**El capítulo 2 no tiene ninguna tabla** — solo las siete ecuaciones. La numeración empieza en el 3.

---

## Defectos pendientes

Lista contrastada contra el PDF. Los que aparecían aquí y **ya están corregidos** se retiran: los
`**` de Markdown crudo en `6.3.`, `6.4.` y `6.5.`; el pie `Tabla 6.2.` fundido con la frase
siguiente (hoy «Dos huecos detectados…» arranca como epígrafe aparte); y el pegote «…sobre D2
completoFigura 5.11.». **0 ocurrencias en las 203 páginas.**

### Formato de los pies

- **Falta el espacio tras el punto** en **exactamente 4 pies**, y solo en esos: `Tabla 4.2.Dimensiones…`, `Tabla 4.5.Mini-experimento…`, `Tabla 5.4.F1…`, `Tabla 5.5.Efecto…`. Los otros 33 lo llevan bien.
- **Pie sin punto final**, únicos de su serie: **Figura 3.1** y **Tabla A.1**.

### Restos de Markdown

- **Tabla 5.8:** dos celdas conservan pipes crudos — «| 5 clases, criterio conservador (n = 22.544)» y «| f1_macro (unknown = error)». Es la **única** tabla afectada; los demás `|` del documento son la notación legítima `|r| > 0,95`.

### Saltos de página y maquetación

- **Tabla 5.11:** la tabla y su pie quedan partidos por un salto de página.
- **Figura 4.3:** la imagen y su pie quedan partidos por un salto de página.
- **Figura 5.11:** el párrafo de entrada («…sobre D2 completo») está **centrado**, heredando estilo de pie, y termina sin punto ni dos puntos.
- **No existe índice de figuras ni índice de tablas** en el documento.

### Decisiones pendientes de Francisco

> [!todo] 1 · Posición del pie de tabla
> Los **37 pies van debajo** de su tabla (verificado visualmente en 3.1, 4.2, 4.3, 4.4, 4.5, 5.1,
> 5.2, 5.3, 5.4, 5.5, 5.8, 5.9, 5.11 y A.1). Que la plantilla los exija **encima** es
> **NO VERIFICABLE desde el PDF**: hoy solo lo enuncia este fichero. **Lo decide Francisco.**

> [!todo] 2 · Numeración del Apéndice A
> El `.docx` tiene **tres pies reales**: «Tabla A.1. Características del dataset completo NSL-KDD»
> (que cubre los cuatro bloques de características), «Tabla A.2» y «Tabla A.3». Aquí abajo se
> listan seis entradas provisionales (A.1–A.6). Hay que **decidir el esquema** antes de tocar nada.
> **No lo resuelve un agente.**

> [!todo] 3 · Censo de la Figura 3.1
> «Figura 3.1. Flujo del proyecto» existe en el `.docx` y **sí entra** en el recuento de 23 pies,
> pero no está en el censo declarado del vault. Decidir si se incorpora.

> [!todo] 4 · Índices de figuras y de tablas
> El documento no los tiene. Decidir si se añaden.

---

## Figuras

**23 imágenes** en el `.docx` y **23 pies «Figura x.y»**. El censo cuadra así:

| Serie | Figuras |
|---|---:|
| 2.1–2.5 | 5 |
| 3.1 | 1 |
| 4.1–4.5 | 5 |
| 5.1–5.12 | 12 |
| **Total** | **23** |

La **Figura 3.1 entra en el recuento**: sin ella la suma daría 22. Otra cosa es que esté o no en el
censo declarado del vault, que es la decisión 3 de arriba.

Pendientes:

- **Figuras 4.6 y 4.7: no existen** en el documento, ni imagen ni referencia. Verificar si se perdieron o nunca se insertaron.
- **Figura 3.1:** pie sin punto final.
- **Figura 4.3:** imagen y pie partidos por un salto de página.
- **Figura 5.11:** párrafo de entrada centrado (hereda estilo de pie) y sin puntuación final.
- **Uniformidad:** en 5.1, 5.6, 5.11 y 5.12 el pie está en el mismo párrafo que la imagen; en el resto de la serie va aparte.
- **No hay índice de figuras.**

---

## Capítulo 3 · Diseño del sistema

| Nº | Ancla | Leyenda |
|---|---|---|
| **3.1** | «SUBCONJUNTO / CONTENIDO / PROPÓSITO» (§3.3.1) | **Tabla 3.1.** Subconjuntos especializados derivados del NSL-KDD: contenido de cada uno y etapa del sistema a la que sirve. |
| **3.2** | «ALGORITMO / NOCIÓN DE ANOMALÍA» (§3.4.2) | **Tabla 3.2.** Detectores de anomalías candidatos para la etapa 1, con la noción de anomalía que implementa cada uno y el motivo de su inclusión en la comparación. |
| **3.3** | «ALGORITMO / IDEA / MOTIVO DE SU INCLUSIÓN» (§3.5.2) | **Tabla 3.3.** Clasificadores supervisados candidatos para la etapa 2, con su principio de funcionamiento y el motivo de su inclusión. |

---

## Capítulo 4 · Implementación del sistema

| Nº | Ancla | Leyenda |
|---|---|---|
| **4.1** | «Librería / Versión / Función en el proyecto» (§4.1.3) | **Tabla 4.1.** Librerías de Python empleadas, con la versión fijada en `requirements.txt` y su función concreta dentro del pipeline. |
| **4.2** | «Subconjunto / Contenido / Instancias / Características» (§4.2.1) | **Tabla 4.2.** Dimensiones de los tres subconjuntos tras el preprocesamiento completo, verificadas por el informe de validación. |
| **4.3** | «Categoría / Descripción / Tipos agrupados» (§4.3.1) | **Tabla 4.3.** Agrupación de los 39 tipos de ataque específicos del NSL-KDD en las cuatro categorías canónicas, más la clase normal. |
| **4.4** | «Característica / Máximo en D2 (escalado)» (§4.3.2) | **Tabla 4.4.** Características de D2 que superan el intervalo [0, 1] tras aplicar el escalador ajustado solo sobre el entrenamiento: consecuencia esperada de la disciplina anti-fuga, no un fallo. |
| **4.5** | «Algoritmo / Balanceo / F1_macro(CV) / Desv. Típica» (§4.3.4) | **Tabla 4.5.** Mini-experimento de balanceo sobre el conjunto de 54 características: F1 macro en validación cruzada de 5 particiones sobre D3, por algoritmo y estrategia. |
| **4.6** | «Métrica (cascada AE→RF sobre D2)» (§4.3.5) | **Tabla 4.6.** Experimento H1: comparación del sistema híbrido completo sobre D2 con los conjuntos de 54 y 122 características. |
| **4.7** | «Split / Contenido / Tamaño / Función» (§4.3.6) | **Tabla 4.7.** División especializada del NSL-KDD en D1, D2 y D3, con su tamaño y su función experimental. |
| **4.8** | «Categoría / Instancias / % de D3» (§4.3.6) | **Tabla 4.8.** Distribución de D3 por categoría de ataque: el desbalance de ≈ 883:1 entre la clase mayoritaria y la minoritaria que condiciona toda la estrategia de evaluación. |
| **4.9** | «Transformación / Dónde se ajusta / Dónde solo se aplica» (§4.3.7) | **Tabla 4.9.** Auditoría anti-fuga: las cuatro transformaciones del pipeline que aprenden de los datos, con el conjunto sobre el que se ajusta cada una. Ninguna ve D2. |
| **4.10** | «Algoritmo / Espacio explorado / Configuraciones» (§4.4.2) | **Tabla 4.10.** Espacios de búsqueda de hiperparámetros de los cuatro detectores de anomalías, con el número de configuraciones evaluadas. |
| **4.11** | «Algoritmo / Configuración ganadora / AUC-ROC (validación)» (§4.4.3) | **Tabla 4.11.** Configuraciones ganadoras de la etapa 1 sobre el conjunto de 54 características, con su AUC-ROC de validación, el umbral fijado por percentil 95 y el coste de ajuste. |
| **4.12** | «Algoritmo / Espacio explorado / Combinaciones» (§4.5.2) | **Tabla 4.12.** Espacios de búsqueda de hiperparámetros de los cuatro clasificadores de firmas, con el número de combinaciones evaluadas por `GridSearchCV`. |
| **4.13** | «Algoritmo / Balanceo (4.3.4) / Configuración ganadora» (§4.5.3) | **Tabla 4.13.** Configuraciones ganadoras de la etapa 2 sobre el conjunto de 54 características, con el esquema de balanceo aplicado y su F1 macro en validación cruzada sobre D3. |

---

## Capítulo 5 · Evaluación

| Nº | Ancla | Leyenda |
|---|---|---|
| **5.1** | «Detector / VN (tn) / FP / FN / VP (tp)» (§5.1.1) | **Tabla 5.1.** Recuentos de la matriz de confusión binaria de los cuatro detectores de anomalías sobre D2, con 54 características y umbral por percentil 95. |
| **5.2** | «Detector / AUC-ROC / AUC-PR / Precision» (§5.1.2) | **Tabla 5.2.** Métricas de los cuatro detectores de anomalías sobre D2 (positivo = ataque), con el coste separado en tiempo de ajuste y bloque completo. |
| **5.3** | «Algoritmo / Balanceo / f1_macro (CV, D3) / f1_macro (D2)» (§5.2.2) | **Tabla 5.3.** Clasificadores de firmas en validación cruzada sobre D3 frente a su rendimiento sobre los ataques de tipo conocido de D2. La brecha refleja el desplazamiento distribucional D3→D2. |
| **5.4** | «Algoritmo / F1 dos (n=5.741)» (§5.2.2) | **Tabla 5.4.** F1 por categoría de ataque sobre D2 de los cuatro clasificadores de firmas, con el soporte de cada clase. |
| **5.5** | «Algoritmo / F1_macro D2 (54) / F1_macro D2 (122)» (§5.2.3) | **Tabla 5.5.** Efecto del conjunto de características sobre la generalización D3→D2 de cada clasificador de firmas. |
| **5.6** | «Algoritmo / Media (n=10) / sd / Min / Max / Semilla 42» (§5.2.4) | **Tabla 5.6.** Dispersión del F1 macro sobre D2 de los dos mejores clasificadores a lo largo de diez semillas, frente al valor publicado con la semilla 42. |
| **5.7** | «Variante / Algoritmo / Métrica / Semilla 42 / Min (10)» (§5.2.4) | **Tabla 5.7.** Celdas cuyo valor con la semilla 42 cae fuera del intervalo [mín, máx] de las diez semillas del barrido. |
| **5.8** | «Alcance / Métrica / Valor» (§5.3) | **Tabla 5.8.** Rendimiento del sistema híbrido sobre D2 según el alcance de la evaluación, con el tamaño de la población en cada caso. |
| **5.9** | «UMBRAL_CONF / Recall macro OOF» (§5.3) | **Tabla 5.9.** Calibración del umbral de confianza sobre probabilidades out-of-fold de D3. Las columnas de D2 son informativas y no intervinieron en la elección. |
| **5.10** | «Tipo 0-day / n / Autoencoder» (§5.3) | **Tabla 5.10.** Recall de detección por tipo de ataque 0-day sobre los 17 tipos ausentes del entrenamiento, para los cuatro detectores. Cada uno se reporta junto a su FPR binario, porque los recalls no son comparables a distinto punto de operación. |
| **5.11** | «Métrica / Híbrido (AE → RF, 54)» (§5.3) | **Tabla 5.11.** Sistema híbrido frente al baseline de control (RandomForest monolítico de 5 clases) sobre D2, con 54 características. |
| **5.12** | «Clasificador [23] / Accuracy sobre KDDTest+» (§5.4) | **Tabla 5.12.** Baselines canónicos del artículo que creó el NSL-KDD, medidos sobre KDDTest+ completo, frente a la accuracy binaria de este sistema. Cifra de comparabilidad externa, no titular del trabajo. |
| **5.13** | «Prevalencia de ataque / Precisión proyectada / Lectura» (§5.4) | **Tabla 5.13.** Precisión del sistema proyectada a distintas prevalencias de ataque, a partir del recall y el FPR medidos sobre D2. |

---

## Capítulo 6 · Conclusiones

| Nº | Ancla | Leyenda |
|---|---|---|
| **6.1** | «# / Error metodológico / Estado en este trabajo» (§6.1.4) | **Tabla 6.1.** Balance del trabajo frente al catálogo de errores metodológicos en aprendizaje automático aplicado a seguridad, con la medida concreta adoptada en cada caso. |
| **6.2** | «Bloque / Naturaleza / Líneas» (§6.2) | **Tabla 6.2.** Agrupación de las líneas futuras en refinamientos ejecutables sobre NSL-KDD y ampliaciones que exigen salir del dataset. |
| **6.3** | «Tipo 0-day (n) / Autoencoder / IsolationForest» (§6.2.1) | **Tabla 6.3.** Complementariedad de los detectores por tipo de ataque: los dos tipos que el detector seleccionado falla por completo y que otros detectan. Motiva la línea del conjunto de detectores. |
| **6.4** | «Métrica / 54 características / 122 características / A quién favorece» (§6.2.4) | **Tabla 6.4.** Reparto del beneficio entre las dos etapas según el conjunto de características, que sostiene la opción B como línea futura. |
| **6.5** | «Peldaño / Qué es / Qué desbloquea» (§6.2.6) | **Tabla 6.5.** Los tres peldaños encadenados para pasar del flujo aislado a la secuencia con reloj, con lo que habilita cada uno. |

---

## Apéndice A · Columnas del dataset NSL-KDD

> [!warning] Numeración sin cerrar
> En el `.docx` este apéndice tiene **tres pies reales**: A.1, A.2 y A.3. Las cuatro entradas de
> características (A.1–A.4 de la lista de abajo) **no son cuatro tablas**: son **una sola tabla
> continua** partida por subtítulos, con la cabecera «# / Nombre / Tipo / Descripción» repetida en
> cada página, y el pie «Tabla A.1. Características del dataset completo NSL-KDD» al final las
> cubre las cuatro. Por eso **no les falta pie**: lo tienen compartido. Los textos de leyenda de
> abajo siguen siendo válidos como descripción de cada bloque; **el esquema de numeración lo decide
> Francisco** (decisión 2).

| Nº (provisional) | Ancla | Estado en el `.docx` | Leyenda |
|---|---|---|---|
| **A.1** | «Características básicas (1–9)» | bloque de la tabla continua **Tabla A.1** | **Tabla A.1.** Características básicas (1–9): atributos de la propia conexión TCP/IP, extraíbles de sus cabeceras. |
| **A.2** | «Características de contenido (10–22)» | bloque de la misma **Tabla A.1** | **Tabla A.2.** Características de contenido (10–22): atributos obtenidos inspeccionando la carga útil, orientados a los ataques r2l y u2r. |
| **A.3** | «Características de tráfico basadas en tiempo (23–31)» | bloque de la misma **Tabla A.1** | **Tabla A.3.** Características de tráfico basadas en tiempo (23–31): estadísticas sobre la ventana de las conexiones de los dos últimos segundos. |
| **A.4** | «Características de tráfico basadas en host (32–41)» | bloque de la misma **Tabla A.1** | **Tabla A.4.** Características de tráfico basadas en host (32–41): estadísticas sobre la ventana de las 100 conexiones anteriores al mismo destino. |
| **A.5** | «Código / Categoría» | pie propio, **«Tabla A.2»** | **Tabla A.5.** Codificación numérica de las cinco categorías por el `LabelEncoder` del pipeline. |
| **A.6** | «Categoría / Tipos de ataque» | pie propio, **«Tabla A.3»** | **Tabla A.6.** Los 40 tipos de etiqueta agrupados por categoría. Se marcan con ★ los 17 tipos presentes solo en el conjunto de test, que constituyen el escenario 0-day. |

Defecto propio del apéndice: el pie **Tabla A.1** no lleva punto final.

---

## Resumen

| Capítulo | Tablas listadas | Estado |
|---|---:|---|
| 1 Introducción | 0 | — |
| 2 Marco Teórico | 0 | solo ecuaciones (1)–(7) |
| 3 Diseño | 3 | 3 pies · tablas reales de Word |
| 4 Implementación | 13 | 13 pies · falta espacio tras el punto en 4.2 y 4.5 |
| 5 Evaluación | 13 | 13 pies · falta espacio en 5.4 y 5.5; pipes crudos en 5.8; 5.11 partida por salto de página |
| 6 Conclusiones | 5 | 5 pies · **sin defectos** (los de 6.2–6.5 ya están corregidos) |
| Apéndice A | 6 | **3 pies**: A.1 cubre los 4 bloques de características (una tabla continua); A.1 sin punto final; numeración por decidir |
| **Total** | **40 filas listadas** | **37 pies reales en el `.docx`** |

**Consecuencia para la tarea T6:** la conversión y la inserción están hechas, y no queda ninguna
tabla en Markdown ni volcada párrafo a párrafo. Lo que queda es el repaso de formato de la lista de
defectos (4 espacios, 2 puntos finales, los pipes de 5.8, tres saltos de maquetación) y las **cuatro
decisiones pendientes de Francisco**: posición del pie, numeración del Apéndice A, censo de la
Figura 3.1 e índices de figuras y tablas.
