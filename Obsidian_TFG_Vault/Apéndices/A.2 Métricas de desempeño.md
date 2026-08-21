---
titulo: "Apéndice A.2 — Métricas de desempeño"
numero: "A.2"
estado: redactada
---

# A.2 Métricas de desempeño

Este apéndice documenta **cómo se instancian en este sistema** las métricas empleadas en la evaluación del [[5.1 Resultados del modelo de detección de anomalías|capítulo 5]]: la convención de signo adoptada, la forma que toma la matriz de confusión en las dos etapas, el criterio de umbral del detector de anomalías y las cifras de FPR que se obtienen con él (A.2.1). A ello se añade un apartado de naturaleza distinta, **A.2.2**, que recoge las familias de métricas **ajenas a la clasificación** —regresión y *clustering*— que el marco teórico necesita definir pero que **ninguna tabla de resultados de este trabajo reporta**. **La definición formal de cada métrica y la justificación de su elección no están aquí, sino en [[2.1.5 Métricas de evaluación]]**, donde se desarrollan; las fórmulas que siguen se reproducen **solo como tabla de consulta rápida**, para no obligar al lector del capítulo 5 a volver al capítulo 2.

Salvo indicación contraria, se adopta la convención del sistema: **positivo = ataque (1)**, **negativo = normal (0)**.

## Matriz de confusión y conteos base

Para un problema binario, la matriz de confusión enfrenta la clase real (filas) con la predicha (columnas):

|  | Predicho: normal | Predicho: ataque |
|---|---|---|
| **Real: normal** | VN (verdadero negativo) | FP (falso positivo) |
| **Real: ataque** | FN (falso negativo) | VP (verdadero positivo) |

En el caso multiclase la matriz es de $k \times k$ (o $5 \times 6$ en el híbrido, al añadirse la columna `unknown`; véase [[5.3 Resultados del sistema híbrido]]), y los conteos VP/FP/FN se calculan por clase en esquema *uno-contra-el-resto*.

## Métricas derivadas (consulta rápida)

Las fórmulas siguientes se recogen sin desarrollo: su derivación, su lectura y el motivo por el que este trabajo prioriza unas sobre otras están en 2.1.5.2 y 2.1.5.3.

$$\text{Precision} = \frac{VP}{VP + FP}$$

$$\text{Recall (TPR, sensibilidad)} = \frac{VP}{VP + FN}$$

$$F_1 = 2 \cdot \frac{\text{Precision} \cdot \text{Recall}}{\text{Precision} + \text{Recall}}$$

$$\text{FPR (tasa de falsos positivos)} = \frac{FP}{FP + VN}$$

- **Precision** — proporción de las alarmas de ataque que son correctas.
- **Recall / TPR** — proporción de ataques reales que el sistema detecta.
- **F1** — media armónica de precision y recall; penaliza el desequilibrio entre ambas.
- **FPR** — proporción de tráfico normal marcado erróneamente como ataque. Métrica **clave en un NIDS**: un FPR alto satura al analista con falsas alarmas.

### Promedios en el caso multiclase

Con $k$ clases y una métrica $M_i$ por clase $i$ (precision, recall o F1):

$$M_{\text{macro}} = \frac{1}{k}\sum_{i=1}^{k} M_i \qquad M_{\text{weighted}} = \frac{1}{N}\sum_{i=1}^{k} n_i \, M_i$$

donde $n_i$ es el número de muestras reales de la clase $i$ y $N = \sum_i n_i$.

- **Macro** — promedio no ponderado; da el mismo peso a cada clase, por lo que **penaliza el mal desempeño en clases minoritarias** (r2l, u2r). Es la métrica de decisión del proyecto (`f1_macro`).
- **Weighted** — promedio ponderado por frecuencia; refleja el rendimiento global pero puede quedar dominado por las clases mayoritarias.

## Curvas y áreas bajo curva

Métricas independientes del umbral, calculadas a partir del *score* continuo del modelo:

- **AUC-ROC** — área bajo la curva ROC, que enfrenta TPR frente a FPR al barrer todos los umbrales de decisión.
- **AUC-PR** — área bajo la curva *Precision-Recall*.

La lectura de ambas áreas y el criterio para preferir una u otra están en [[2.1.5 Métricas de evaluación]] § 2.1.5.5.

## A.2.1 Métricas del modelo de anomalías

El detector de anomalías es un modelo **one-class**: se entrena solo con tráfico normal (D1) y no dispone de etiquetas de ataque durante el ajuste. Sus métricas presentan dos particularidades:

- **Score de anomalía.** Cada muestra recibe un valor continuo (mayor = más anómala), unificado entre los cuatro algoritmos para poder compararlos en igualdad de condiciones (véase [[3.4 Modelo de detección de anomalías]]). La decisión binaria surge de comparar ese *score* con un umbral: $\;\text{predicción} = \text{ataque} \iff \text{score} > \text{umbral}$.

- **Umbral por percentil.** El umbral se fija en el **percentil 95 del score sobre el conjunto de validación de D1** (solo tráfico normal), lo que corresponde a un **FPR nominal del 5 %**:

$$\text{umbral} = P_{95}\big(\text{score}(D1_{\text{val}})\big)$$

  El mismo criterio (p95) se aplica a los cuatro algoritmos. El umbral **nunca se ajusta mirando el conjunto de test D2** (salvaguarda anti-*leakage*).

- **FPR nominal frente a FPR real.** El 5 % es el FPR *esperado* bajo la hipótesis de que el tráfico normal de test se distribuye como el de entrenamiento. En la práctica, el **desplazamiento de distribución (*drift*) entre D1 y D2** eleva el FPR real observado: **10,2 % en la variante de 54 características y 8,5 % en la de 122**. Ambas cifras proceden del artefacto `Resultados\metricas_hibrido.csv`, columna `bin_fpr`, una fila por variante. Se citan **por separado, nunca fundidas en un rango redondeado**; el desglose por detector individual **de la variante de 54 características** está en [[5.1 Resultados del modelo de detección de anomalías]] —esa nota no publica el desglose de la variante de 122, que debe consultarse en el artefacto. Esta diferencia no es un error de implementación, sino una consecuencia medida del *drift* del dataset, y debe interpretarse como tal.

> [!note] Por qué el FPR del sistema es el FPR de esta etapa
> Que este apartado —dedicado al **detector de anomalías**— cite `metricas_hibrido.csv` no es un descuido. La columna `bin_fpr` de la tabla del sistema y la columna `fpr` de `Resultados\metricas_anomalias.csv` (filas del Autoencoder) contienen **exactamente los mismos valores** (0,10174 y 0,084852), y coinciden **por construcción, no por casualidad**: en una cascada anomalías→firmas, un falso positivo binario del sistema solo puede originarse en la etapa 1, porque una muestra normal que la etapa 1 declara normal **nunca llega** al clasificador de firmas y no puede ser reclasificada como ataque. La etapa 2 no puede crear ni corregir falsos positivos binarios. Esta identidad está documentada en la columna `alcance` de `metricas_hibrido.csv`.

> [!warning] Alcance de la remisión a `5.3`
> [[5.3 Resultados del sistema híbrido]] publica **únicamente la variante de 54 características**. La cifra de la variante de 122 **no aparece allí**, y el «8,5 %» que sí figura en esa nota corresponde a la columna «OneClassSVM (FPR 8,5 %)», es decir, a **otro detector y en la variante de 54**. Para la cifra de 122, la fuente es el artefacto citado arriba.

---

## A.2.2 Métricas ajenas a la clasificación, no reportadas por este trabajo

Las familias que siguen **no aparecen en ninguna tabla `metricas_*.csv` del capítulo 5**: se recogen aquí, y no en el cuerpo, por completitud del marco de aprendizaje automático expuesto en [[2.1.2 Tipos de ML]]. El cuerpo de [[2.1.5 Métricas de evaluación]] § 2.1.5.6 se limita a mencionarlas y remite a este apartado. Ninguna decisión del sistema depende de ellas.

### A.2.2.1 Métricas de regresión: MAE y RMSE

Aunque este trabajo aborda un problema de clasificación, dos métricas de regresión son parte del vocabulario común del aprendizaje automático y conviene fijarlas. Ambas miden la distancia entre el valor predicho $\hat{y}_i$ y el valor real $y_i$ sobre un conjunto de $n$ ejemplos.

**Error absoluto medio** (MAE, *Mean Absolute Error*): el promedio del valor absoluto de cada error.

$$\text{MAE} = \frac{1}{n}\sum_{i=1}^{n} |y_i - \hat{y}_i|$$

**Raíz del error cuadrático medio** (RMSE, *Root Mean Square Error*): la raíz cuadrada del promedio de los errores al cuadrado.

$$\text{RMSE} = \sqrt{\frac{1}{n}\sum_{i=1}^{n} (y_i - \hat{y}_i)^2}$$

La diferencia entre ambas no es solo de fórmula: al elevar al cuadrado antes de promediar, el RMSE **penaliza más los errores grandes** que los pequeños, mientras que el MAE trata cualquier error con peso proporcional a su magnitud, sin amplificarlo. Un único error muy grande —un caso atípico mal predicho— eleva el RMSE de forma desproporcionada respecto a su efecto en el MAE. La elección entre ambas depende de si el problema considera los errores grandes desproporcionadamente más costosos (RMSE) o si todos los errores deben pesar según su magnitud sin más (MAE) [5, cap. 2].

> [!note] Un matiz propio de este sistema
> El error de reconstrucción del autoencoder de la etapa 1 es formalmente un error de regresión, pero **no se reporta como métrica de regresión**: se usa como *score* de anomalía y se evalúa con las métricas de clasificación de A.2.1, tras compararlo con el umbral por percentil 95.

### A.2.2.2 Métricas de *clustering*: coeficiente de silueta

Cuando el algoritmo no dispone de etiquetas reales contra las que comparar —el caso del aprendizaje no supervisado por agrupamiento— las métricas anteriores no son aplicables, porque todas ellas necesitan conocer la clase verdadera de cada muestra. El **coeficiente de silueta** (*silhouette score*) evalúa en su lugar la calidad interna de la partición en grupos, sin requerir etiquetas.

Para una instancia dada, sea $a$ la distancia media a las demás instancias de su propio clúster (cohesión interna) y $b$ la distancia media a las instancias del clúster más cercano distinto del propio (separación respecto al vecino más próximo). El coeficiente de silueta de esa instancia es:

$$s = \frac{b - a}{\max(a, b)}$$

El valor resultante está acotado en $[-1, 1]$: cercano a $+1$ indica que la instancia está bien situada dentro de su clúster y lejos de los demás; cercano a $0$, que está en el límite entre dos clústeres; cercano a $-1$, que probablemente se asignó al clúster equivocado. El **coeficiente de silueta medio** de todas las instancias del conjunto resume la calidad global de la partición [5, cap. 9].

**Por qué esta métrica figura en la memoria.** El sistema implementado no emplea *clustering* en su arquitectura final —las dos etapas del H-NIDS son un detector de anomalías semisupervisado (*one-class*) y un clasificador de firmas supervisado, no un algoritmo de agrupamiento—. El coeficiente de silueta se incluye por completitud del marco teórico de ML expuesto en [[2.1.2 Tipos de ML]], no porque el capítulo 5 lo reporte. Los algoritmos de agrupamiento a los que se aplicaría —k-means y el agrupamiento jerárquico— se describen, por la misma razón y con el mismo criterio, en [[A.3 Ficha del sistema]] § A.3.10.

---

## Notas relacionadas

[[2.1.5 Métricas de evaluación]] · [[A.3 Ficha del sistema]] ·
[[5.1 Resultados del modelo de detección de anomalías]] · [[5.3 Resultados del sistema híbrido]]
