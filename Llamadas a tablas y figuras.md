# Llamadas por número a tablas y figuras

Este fichero cierra las tareas **T6** (37 tablas) y **T7** (14 figuras) de `Las tareas de Kiko.md`,
cuya sede de defecto está en `Leyenda_tablas.md`, sección «Referencias cruzadas y numeración».

Contiene **51 frases**: 37 de tabla y 14 de figura.

La sede de inserción **no está aquí a propósito**: Francisco localiza cada tabla o figura por su
nombre. Para el fragmento literal del párrafo previo a cada una, remitir a las dos tablas de sedes
que ya existen en `Leyenda_tablas.md`.

El criterio de inserción es **sustituir el deíctico sin número** («la tabla siguiente», «la tabla
anterior») por la llamada numerada de abajo, no añadir una frase suelta encima de la existente.

Las figuras 2.1-2.5 y 5.1-5.4 **no están en esta lista** porque ya se llaman por número desde la
prosa.

Generado contra el volcado `Resultados/docx/REPASO_20260825-2106/` (binario mtime
2026-08-25T21:06:08).

## Capítulo 3

### Tablas

**Tabla 3.1** — Los subconjuntos D1, D2 y D3 derivados del NSL-KDD, junto con el contenido y la etapa a la que sirve cada uno, se resumen en la Tabla 3.1.
**Tabla 3.2** — La Tabla 3.2 compara los cuatro candidatos evaluados para la etapa de anomalías —Isolation Forest, OneClassSVM, LocalOutlierFactor y un Autoencoder— según la noción de anomalía que implementan.
**Tabla 3.3** — Los cuatro clasificadores supervisados candidatos para la etapa de firmas —DecisionTree, RandomForest, KNN e HistGradientBoosting— se contrastan en la Tabla 3.3 según su principio de funcionamiento.

### Figuras

**Figura 3.1** — El flujo completo del proyecto, desde el dataset hasta el sistema híbrido evaluado, se ilustra en la Figura 3.1.

## Capítulo 4

### Tablas

**Tabla 4.1** — Como se detalla en la Tabla 4.1, cada librería de Python usada se fija con su versión en `requirements.txt` y su función en el pipeline.
**Tabla 4.2** — La Tabla 4.2 recoge las dimensiones de D1, D2 y D3 tras el preprocesamiento, verificadas por el informe de validación.
**Tabla 4.3** — La Tabla 4.3 muestra cómo los 39 tipos de ataque específicos del NSL-KDD se agrupan en las cuatro categorías canónicas más la clase normal.
**Tabla 4.4** — La Tabla 4.4 enumera las características de D2 que superan el intervalo [0, 1] tras el escalado ajustado solo con el entrenamiento, consecuencia esperada de la disciplina anti-fuga.
**Tabla 4.5** — La Tabla 4.5 compara, por algoritmo y estrategia de balanceo, el F1 macro en validación cruzada de 5 particiones sobre D3 con 54 características.
**Tabla 4.6** — El experimento H1 de la Tabla 4.6 contrasta el rendimiento del sistema híbrido completo sobre D2 usando 54 frente a 122 características.
**Tabla 4.7** — La Tabla 4.7 detalla el tamaño y la función experimental de cada uno de los subconjuntos D1, D2 y D3 de la división especializada del NSL-KDD.
**Tabla 4.8** — La Tabla 4.8 recoge la distribución de D3 por categoría de ataque, con un desbalance de ≈ 883:1 entre la clase mayoritaria y la minoritaria.
**Tabla 4.9** — La Tabla 4.9 detalla la auditoría anti-fuga, enumerando las cuatro transformaciones del pipeline que aprenden de los datos sin que ninguna vea D2.
**Tabla 4.10** — La Tabla 4.10 presenta los espacios de búsqueda de hiperparámetros de los cuatro detectores de anomalías, con el número de configuraciones evaluadas en cada caso.
**Tabla 4.11** — La Tabla 4.11 reúne las configuraciones ganadoras de la etapa 1 sobre 54 características, con su AUC-ROC de validación y el umbral por percentil 95.
**Tabla 4.12** — La Tabla 4.12 muestra los espacios de búsqueda de hiperparámetros de los cuatro clasificadores de firmas y las combinaciones evaluadas por `GridSearchCV`.
**Tabla 4.13** — La Tabla 4.13 sintetiza las configuraciones ganadoras de la etapa 2, con su esquema de balanceo y el F1 macro obtenido en validación cruzada sobre D3.

### Figuras

**Figura 4.1** — La Figura 4.1 ofrece un panel de nueve gráficos del análisis exploratorio, con el reparto de clases y la cobertura de ataques entre D1, D2 y D3.
**Figura 4.2** — La Figura 4.2 evidencia la pureza de D1 y D3 y el desbalance entre categorías de ataque dentro de D3, según lo generado por `validacion.py`.
**Figura 4.3** — La Figura 4.3 superpone los histogramas de las doce características más discriminantes entre D1 y D3, revelando su distinto poder de separación.
**Figura 4.4** — La Figura 4.4 mide con el test de Kolmogorov-Smirnov el desplazamiento entre D1 y D2 sobre las 54 características, marcando las que superan la significación.
**Figura 4.5** — La Figura 4.5 acota, al top 15, la proporción de valores atípicos por IQR en D1, D2 y D3 entre las características más afectadas.

## Capítulo 5

### Tablas

**Tabla 5.1** — Los recuentos de la matriz de confusión binaria de los cuatro detectores de anomalías sobre D2 se detallan en la Tabla 5.1.
**Tabla 5.2** — La Tabla 5.2 recoge las métricas de los cuatro detectores de anomalías sobre D2, separando el coste en ajuste y bloque completo.
**Tabla 5.3** — La Tabla 5.3 contrasta el rendimiento en validación cruzada sobre D3 con el obtenido sobre los ataques conocidos de D2.
**Tabla 5.4** — El F1 por categoría de ataque de los cuatro clasificadores de firmas sobre D2, con su soporte, figura en la Tabla 5.4.
**Tabla 5.5** — La Tabla 5.5 muestra el efecto del conjunto de características sobre la generalización D3→D2 de cada clasificador de firmas.
**Tabla 5.6** — La dispersión del F1 macro sobre D2 de los dos mejores clasificadores a lo largo de diez semillas, frente al valor con la semilla 42, se recoge en la Tabla 5.6.
**Tabla 5.7** — La Tabla 5.7 señala las celdas cuyo valor con la semilla 42 queda fuera del intervalo [mín, máx] del barrido de semillas.
**Tabla 5.8** — El rendimiento del sistema híbrido sobre D2 varía según el alcance de la evaluación considerado, como muestra la Tabla 5.8.
**Tabla 5.9** — La Tabla 5.9 recoge la calibración del umbral de confianza sobre probabilidades out-of-fold de D3, con las columnas de D2 a título meramente informativo.
**Tabla 5.10** — La Tabla 5.10 detalla, para los 17 tipos de ataque 0-day, el recall de cada detector junto a su FPR binario, ya que cada uno opera en su propio punto de operación.
**Tabla 5.11** — La Tabla 5.11 contrasta el sistema híbrido con el baseline monolítico de control sobre D2, en el conjunto de 54 características.
**Tabla 5.12** — La Tabla 5.12 sitúa la accuracy binaria del sistema frente a los baselines canónicos del artículo original de NSL-KDD, como referencia de comparabilidad externa.
**Tabla 5.13** — La Tabla 5.13 proyecta la precisión del sistema a distintas prevalencias de ataque a partir del recall y el FPR observados en D2.

### Figuras

**Figura 5.5** — Las curvas ROC de los cuatro detectores de anomalías sobre D2 se representan en la Figura 5.5.
**Figura 5.6** — Las curvas precisión-recall de los cuatro detectores de anomalías sobre D2 se muestran en la Figura 5.6.
**Figura 5.7** — La Figura 5.7 presenta la matriz de confusión multiclase de DecisionTree sobre los flujos de tipo conocido de D2.
**Figura 5.8** — La matriz de confusión multiclase de RandomForest sobre la misma población se representa en la Figura 5.8.
**Figura 5.9** — La Figura 5.9 muestra la matriz de confusión multiclase de KNN sobre la misma población de ataques conocidos.
**Figura 5.10** — La matriz de confusión multiclase de HistGradientBoosting sobre esa población se recoge en la Figura 5.10.
**Figura 5.11** — La Figura 5.11 muestra la matriz de confusión del sistema híbrido sobre D2 completo, con la columna unknown para lo anómalo sin firma atribuida.
**Figura 5.12** — La Figura 5.12 presenta la matriz de confusión del baseline de control (RandomForest monolítico de 5 clases) sobre D2, con 54 características.

## Capítulo 6

### Tablas

**Tabla 6.1** — El balance entre los errores metodológicos habituales en ML aplicado a seguridad y la medida adoptada frente a cada uno se resume en la Tabla 6.1.
**Tabla 6.2** — Las líneas futuras se agrupan, según exijan o no salir de NSL-KDD, en la Tabla 6.2.
**Tabla 6.3** — La Tabla 6.3 recoge la complementariedad entre detectores: los dos tipos de ataque que el detector seleccionado falla por completo y que otros sí detectan.
**Tabla 6.4** — El reparto del beneficio entre las dos etapas según el conjunto de características, que sostiene la opción B como línea futura, se muestra en la Tabla 6.4.
**Tabla 6.5** — Los tres peldaños encadenados para pasar del flujo aislado a la secuencia con reloj se detallan en la Tabla 6.5.

## Apéndice A

### Tablas

**Tabla A.1** — Las características del dataset completo NSL-KDD se listan en la Tabla A.1 del apéndice.
**Tabla A.2** — La codificación numérica de las cinco categorías asignada por el LabelEncoder del pipeline se recoge en la Tabla A.2 del apéndice.
**Tabla A.3** — Los 40 tipos de etiqueta agrupados por categoría, con los 17 tipos exclusivos del test marcados como escenario 0-day, se listan en la Tabla A.3 del apéndice.
