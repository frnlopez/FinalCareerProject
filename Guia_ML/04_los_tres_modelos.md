# 04 — Los tres modelos: anomalías, firmas e híbrido

> Aquí se junta todo. Dos detectores que ven mundos distintos y una cascada que los
> combina. Y la pregunta que lo justifica todo: por qué esto y no "un Random Forest
> y ya", que es lo que hace todo el mundo con NSL-KDD.

---

## 1. Modelo de ANOMALÍAS (etapa 1) — `anomalias.py`

**Qué hace:** aprende cómo es el tráfico **normal** (se entrena solo con D1, sin
etiquetas) y marca como sospechoso todo lo que se desvía. No sabe *qué* ataque es;
solo dice **normal vs sospechoso**. Es no supervisado (fichero 01).

**Anomaly score:** cada algoritmo da una puntuación de "rareza". Se unifica el
criterio para poder comparar: **mayor score = más anómalo** (en sklearn suele ser al
revés, así que se niega el signo).

Los **4 algoritmos** que se comparan bajo el mismo protocolo:

| Algoritmo | Idea | Nota de implementación |
|---|---|---|
| **IsolationForest** | Aísla anomalías con particiones aleatorias; lo raro se aísla antes | rápido, sin problema con 67k |
| **One-Class SVM** | Dibuja una frontera alrededor de lo normal | O(n²): se entrena con submuestra de 20.000 de D1 |
| **LocalOutlierFactor** | Compara la densidad local de un punto con la de sus vecinos | `novelty=True` obligatorio para puntuar D2 |
| **Autoencoder** (`MLPRegressor`) | Red que aprende a reconstruir lo normal; un ataque se reconstruye mal → error alto = anomalía | sin TensorFlow/Keras; arquitectura tipo (64,32,64) |

**El umbral (decisión cerrada):** con la config ganadora, `umbral = percentil 95 del 
anomaly_score sobre D1_val` (el 20% de D1 reservado para validar). Se acepta ~5% de
falsas alarmas **por diseño**. El **mismo percentil para los 4** → comparación
homogénea. Nunca se mira D2 para esto.

> [!note] Resultado real observado (ejecución 2026-07-06)
> Mejor detector: **Autoencoder ≈ IsolationForest**; LOF el más flojo. El FPR real
> sobre D2 sale ~8-10%, no el ~5% de diseño: es por **drift** (el test tiene
> distribución algo distinta al train), no un bug. Se explica así en la memoria.

---

## 2. Modelo de FIRMAS (etapa 2) — `firmas.py`

**Qué hace:** dado un tráfico que ya se sabe atacante, decide **de qué tipo** es
(`dos/probe/r2l/u2r`). Es clasificación **supervisada multiclase**, entrenada con D3.
No conoce la clase "normal" (por eso necesita que la etapa 1 filtre primero).

Los **4 algoritmos** comparados (tu 2.1.4 los cubre):

| Algoritmo | Idea | Papel especial |
|---|---|---|
| **DecisionTree** | Reglas if/else legibles | base para **extraer firmas legibles** (`export_text`) |
| **RandomForest** | Muchos árboles votando (ensemble) | el "estándar" para NSL-KDD |
| **KNN** | Clasifica por los `k` vecinos más cercanos | sensible al escalado (ya resuelto) |
| **HistGradientBoosting** | Boosting: árboles que corrigen el error del anterior | rendimiento tipo XGBoost, sin dependencia nueva |

**Protocolo (fichero 03):** para cada algoritmo, mini-experimento de balanceo (SMOTE
vs class_weight/nada) → GridSearchCV con StratifiedKFold(5) y `f1_macro` → refit sobre
todo D3 → evaluación sobre las filas de ataque de D2 **de tipos conocidos** (los 0-day
se excluyen aquí; son trabajo de la etapa 1).

**Extracción de firmas (la parte "IDS clásico"):** del mejor DecisionTree se sacan
reglas legibles con `export_text`, tipo `si flag_S0 > 0.5 → dos`. Conectan el modelo
con la idea tradicional de firma de un IDS. Van a `firmas_reglas.txt` y a la sección 4.5.

---

## 3. Sistema HÍBRIDO — `hibrido.py`

**La cascada** (decisión cerrada):

```
1. Anomalías puntúa cada flujo de D2  →  score > umbral ?
      NO  → 'normal'
      SÍ  → sospechoso, pasa a la etapa 2
2. Firmas clasifica el sospechoso     →  categoría con mayor predict_proba
      si la confianza (proba máx) < UMBRAL_CONF  →  'unknown' (0-day)
```

**Por qué cascada y no los dos en paralelo:** el modelo de firmas solo vio ataques;
si le dieras tráfico normal, lo forzaría a etiquetarlo como algún ataque (no conoce
"normal"). La etapa de anomalías filtra primero lo normal, así firmas solo ve lo que
ya es sospechoso.

**El `UMBRAL_CONF` y los 0-day:** si un sospechoso no encaja con confianza en ninguna
categoría conocida, se marca **`unknown`** = posible ataque nuevo. Ese umbral se
calibra con probabilidades **out-of-fold** de la CV de firmas (`cross_val_predict`),
**no** con D2 (leakage) ni con un holdout (se perderían las ~52 muestras de u2r).
Decisión Q4.

---

## 4. El argumento 0-day (el corazón del TFG)

Un **0-day** es un ataque de un tipo nunca visto en el entrenamiento. D2 contiene
**~17 tipos** que no están en D3. La métrica clave: de esos tipos, ¿qué fracción marca
la **etapa 1 (anomalías)** como sospechosa? Eso lo calcula
`evaluacion.evaluar_0day_por_tipo(...)` → recall 0-day por tipo.

- Firmas **no puede** con ellos (nunca los vio → los mapearía a una clase conocida o
  fallaría). Solo anomalías tiene una oportunidad, porque solo necesita ver que "esto
  no es normal".
- Que el sistema detecte 0-days es **la aportación** del diseño híbrido frente a un
  clasificador supervisado clásico.

---

## 5. Por qué no "solo un Random Forest" (la pregunta del profesor)

El comentario "todo el mundo acaba en un Random Forest para este dataset" mezcla dos
cosas distintas. Conviene separarlas:

1. **RF como clasificador de firmas** → **ya lo tenemos** (§2 de este fichero). Es uno
   de los 4 algoritmos comparados, y además es el motor de la selección de
   características (fichero 02).
2. **RF monolítico** = un único RF supervisado sobre TODO el train (normal + 4
   ataques), evaluado sobre todo el test. Eso es "lo que hace todo el mundo" y da ~99%
   en la literatura. **Ese no lo tenemos como arquitectura, a propósito** — porque la
   tesis del TFG es el sistema híbrido, no un clasificador único.

**Pero** un RF monolítico sí tiene sentido como **baseline de comparación**, y no
tenerlo es un hueco real:

> [!important] Por qué conviene añadir el RF monolítico como control
> - Es el número que el tribunal tiene en la cabeza ("todos sacan 99%"). Sin medirlo,
>   no puedes responder: *¿para qué el híbrido si un RF de 20 líneas da 99%?*
> - La respuesta es el 0-day: un RF supervisado **no puede** detectar los ~17 tipos que
>   nunca vio etiquetados; la etapa de anomalías sí. Ese contraste **es** la
>   justificación del híbrido.
> - Coste trivial: RF ya está implementado. Es entrenarlo sobre el train completo y
>   evaluarlo sobre D2 completo (incluidos 0-day), con el mismo `evaluacion.py`.
> - Va al capítulo 5 como línea base, no como quinta arquitectura. Su debilidad
>   esperada en 0-day es la evidencia más fuerte a favor de la cascada.

Es decir: RF no es un rival a descartar, es el **experimento de control** que hace
defendible todo el trabajo. (Esta decisión está pendiente de tu aprobación para
meterla en el roadmap y en `resumen-de-decisiones.md`.)

---

## 6. Estado actual y qué falta

| Componente | Estado |
|---|---|
| Preprocesamiento + splits + selección (54/122) | hecho, validado |
| `evaluacion.py` + `config.py` | hecho, verificado |
| `anomalias.py` (4 algoritmos) | hecho y **ejecutado** (54 y 122) |
| `firmas.py` (4 algoritmos) | implementado y auditado APTO · **falta ejecutar** |
| `hibrido.py` (cascada) | por implementar |
| Experimento 54 vs 122 (recall 0-day) | por hacer (cierra Q1/C) |
| Baseline RF monolítico | propuesto, pendiente de decisión |

**Siguiente paso del roadmap:** ejecutar `firmas.py` (54 → 122). Pero antes conviene
cerrar si añadimos el baseline RF monolítico, porque cambia lo que se ejecuta.
