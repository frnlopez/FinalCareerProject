---
titulo: "Apéndice A.2 — Métricas de desempeño"
numero: "A.2"
estado: borrador
---

# A.2 Métricas de desempeño

Este apéndice recoge las **definiciones formales** de las métricas empleadas en la evaluación del [[5.1 Resultados del modelo de detección de anomalías|capítulo 5]]. La interpretación conceptual de cada una se trata en [[2.1.5 Métricas de evaluación]]; aquí se listan únicamente como fórmulas de referencia.

Salvo indicación contraria, se adopta la convención del sistema: **positivo = ataque (1)**, **negativo = normal (0)**.

## Matriz de confusión y conteos base

Para un problema binario, la matriz de confusión enfrenta la clase real (filas) con la predicha (columnas):

|  | Predicho: normal | Predicho: ataque |
|---|---|---|
| **Real: normal** | VN (verdadero negativo) | FP (falso positivo) |
| **Real: ataque** | FN (falso negativo) | VP (verdadero positivo) |

En el caso multiclase la matriz es de $k \times k$ (o $5 \times 6$ en el híbrido, al añadirse la columna `unknown`; véase [[5.3 Resultados del sistema híbrido]]), y los conteos VP/FP/FN se calculan por clase en esquema *uno-contra-el-resto*.

## Métricas derivadas

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

- **AUC-ROC** — área bajo la curva ROC, que enfrenta TPR frente a FPR al barrer todos los umbrales de decisión. Un valor de 1 indica separación perfecta; 0,5 equivale al azar.
- **AUC-PR** — área bajo la curva *Precision-Recall*. Más informativa que la ROC cuando **la clase positiva es minoritaria o el conjunto está desbalanceado**, situación habitual en la detección de intrusiones.

## A.2.1 Métricas del modelo de anomalías

El detector de anomalías es un modelo **one-class**: se entrena solo con tráfico normal (D1) y no dispone de etiquetas de ataque durante el ajuste. Sus métricas presentan dos particularidades:

- **Score de anomalía.** Cada muestra recibe un valor continuo (mayor = más anómala), unificado entre los cuatro algoritmos para poder compararlos en igualdad de condiciones (véase [[3.4 Modelo de detección de anomalías]]). La decisión binaria surge de comparar ese *score* con un umbral: $\;\text{predicción} = \text{ataque} \iff \text{score} > \text{umbral}$.

- **Umbral por percentil.** El umbral se fija en el **percentil 95 del score sobre el conjunto de validación de D1** (solo tráfico normal), lo que corresponde a un **FPR nominal del 5 %**:

$$\text{umbral} = P_{95}\big(\text{score}(D1_{\text{val}})\big)$$

  El mismo criterio (p95) se aplica a los cuatro algoritmos. El umbral **nunca se ajusta mirando el conjunto de test D2** (salvaguarda anti-*leakage*).

- **FPR nominal frente a FPR real.** El 5 % es el FPR *esperado* bajo la hipótesis de que el tráfico normal de test se distribuye como el de entrenamiento. En la práctica, el **desplazamiento de distribución (*drift*) entre D1 y D2** eleva el FPR real observado (≈ 8–10 %; véase [[5.1 Resultados del modelo de detección de anomalías]]). Esta diferencia no es un error de implementación, sino una consecuencia medida del *drift* del dataset, y debe interpretarse como tal.
