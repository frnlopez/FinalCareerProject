# 03 — Validación y métricas

> Dos preguntas que este fichero responde: (1) ¿cómo ajustamos el modelo sin
> engañarnos a nosotros mismos? (validación cruzada, GridSearch); (2) ¿cómo sabemos
> si un modelo es bueno de verdad? (matriz de confusión, precision/recall/F1,
> ROC/PR). Ancla tu 2.1.3 (entrenamiento) y 2.1.5 (métricas).

---

## 1. El enemigo: overfitting

- **Overfitting (sobreajuste):** el modelo memoriza el train, incluido su ruido, y
  falla con datos nuevos. Da 99% en train y se hunde en test.
- **Underfitting (subajuste):** el modelo es demasiado simple y ni siquiera capta el
  patrón del train.

El objetivo es **generalizar**: acertar en datos que no ha visto. Todo lo que sigue
(validación cruzada, reservar D2, elegir bien las métricas) existe para no confundir
"memorizar" con "aprender".

---

## 2. Parámetros vs hiperparámetros

- **Parámetros:** los aprende el modelo solo durante el entrenamiento (p. ej. dónde
  corta cada nodo de un árbol).
- **Hiperparámetros:** los fijas **tú antes** de entrenar y condicionan cómo aprende
  (profundidad máxima del árbol, nº de árboles del bosque, `k` de KNN…).

Elegir buenos hiperparámetros es parte del trabajo. Pero no se pueden elegir mirando
el test (sería leakage) ni el propio train (elegirías lo que sobreajusta). Se eligen
con **validación cruzada**.

---

## 3. Validación cruzada (cross-validation)

### Qué es
En lugar de un único corte train/validación, se parte el train en **K trozos (folds)**.
Se entrena K veces: cada vez, K−1 folds entrenan y el fold restante valida. Se
promedian los K resultados. Así la estimación no depende de la suerte de un corte
concreto, y **cada muestra sirve tanto de entrenamiento como de validación** (en
rondas distintas). Tu 2.1.3 ya lo menciona: "validación cruzada N-fold calculando la
media y la desviación estándar".

### StratifiedKFold (el que usamos, K=5)
Un K-fold normal podría dejar un fold sin ninguna muestra de u2r (solo hay 52, según
`Resultados/specialized_nsl_kdd_composicion_d3.csv`). El
**estratificado** mantiene en cada fold la **misma proporción de clases** que el total.
Imprescindible con desbalance. En el código: `StratifiedKFold(5, shuffle=True,
random_state=42)`, el mismo objeto para los 4 algoritmos → comparación justa.

> [!note] Encaja con SMOTE (fichero 02)
> Al ir SMOTE dentro del `ImbPipeline`, la CV lo aplica **dentro de cada fold**, solo
> al train de ese fold. El fold de validación queda limpio de sintéticos. Sin leakage.

---

## 4. GridSearchCV: elegir hiperparámetros con método

**GridSearchCV** prueba **todas las combinaciones** de una rejilla (grid) de
hiperparámetros, evaluando cada una con validación cruzada, y se queda con la mejor.
Luego reentrena el modelo con esa combinación sobre todo el train (`refit`).

Ejemplo real (`firmas.py`, RandomForest):
```python
GRIDS["RandomForest"] = {"n_estimators": [100, 300], "max_depth": [10, None]}
# GridSearchCV prueba las 4 combinaciones, cada una con StratifiedKFold(5),
# puntúa con f1_macro y se queda con la mejor.
```

- Los grids son **pequeños a propósito** (3-4 valores por hiperparámetro): el TFG
  compara 4 algoritmos, no exprime uno; grids gigantes tardarían horas y no cambiarían
  la conclusión. Las tablas de grids van a la memoria (4.4/4.5).
- `scoring='f1_macro'` (ver §6). `random_state=42` en todo → reproducible.

> [!note] En anomalías no hay etiquetas → no hay GridSearchCV clásico
> El detector de anomalías se entrena sin `y`. Para elegir sus hiperparámetros se
> construye un set de validación etiquetado con D1_val (normal) + una muestra de D3
> (ataques *conocidos*, nunca D2) y se elige por AUC-ROC. Detalle en el fichero 04.

---

## 5. Reproducibilidad: `random_state=42`

Muchos pasos tienen azar (barajar folds, arrancar un bosque, interpolar en SMOTE). Si
no fijas la semilla, cada ejecución da números ligeramente distintos y no puedes
comparar experimentos ni defender un resultado. **Regla del proyecto:** `random_state=42`
en absolutamente todo (folds, SMOTE, modelos, GridSearch). Está centralizado en
`config.RANDOM_STATE`.

---

## 6. Métricas de clasificación

### Matriz de confusión
Tabla: filas = clase **real**, columnas = clase **predicha** (tu 2.1.5). La diagonal
son aciertos; todo lo de fuera, errores, y te dice **qué** confunde con **qué**. Para
el problema binario normal/ataque es 2×2:

|  | Predicho normal | Predicho ataque |
|---|---|---|
| **Real normal** | TN (verdadero negativo) | FP (falsa alarma) |
| **Real ataque** | FN (ataque no visto) | TP (ataque detectado) |

### Precision, Recall, F1
- **Precision** = TP / (TP + FP): de lo que marco como ataque, ¿cuánto es ataque real?
  Baja precision = muchas falsas alarmas.
- **Recall** (TPR, sensibilidad) = TP / (TP + FN): de los ataques reales, ¿cuántos
  detecto? Bajo recall = se me escapan ataques. **En un IDS, el recall suele importar
  más** (un ataque no detectado es peor que una falsa alarma).
- **F1** = media armónica de precision y recall. Resume ambas en un número; es baja si
  cualquiera de las dos lo es.

> [!important] macro vs weighted (por qué macro con u2r)
> - **macro:** promedia la métrica de cada clase dándoles **el mismo peso**. Si u2r va
>   fatal, la macro baja aunque u2r sean 52 muestras entre 58.000.
> - **weighted:** pondera por el tamaño de cada clase. u2r casi no influye.
> Usamos **f1_macro** para no premiar el ignorar las clases raras. Un accuracy alto
> con desbalance **miente**: predecir siempre "dos" acierta el ~78% y no sirve de nada.

### FPR (tasa de falsos positivos)
FPR = FP / (FP + TN): qué fracción del tráfico **normal** marco por error como ataque.
Es la "tasa de falsas alarmas". Un NIDS con FPR alto satura al analista y se ignora.

### ROC, PR y AUC (para scores continuos)
Los detectores de anomalías no dan un sí/no, dan un **score** continuo. Según dónde
pongas el **umbral**, cambian recall y FPR. Las curvas recorren *todos* los umbrales:
- **ROC:** TPR (recall) frente a FPR. **AUC-ROC** = área bajo la curva; 1,0 perfecto,
  0,5 azar.
- **PR (Precision-Recall):** precision frente a recall; más informativa con clases
  desbalanceadas.
- Ventaja: **AUC es independiente del umbral** → compara detectores de forma limpia,
  antes de comprometerte con un punto de corte.

En el código: `evaluacion.plot_roc_pr(...)` superpone las curvas de los 4 detectores
en una figura (la figura estrella de 5.1) y devuelve sus AUCs.

### El umbral (threshold)
Convierte el score continuo en decisión. Dónde ponerlo es una **decisión de diseño**,
no un resultado. En anomalías se fija en el **percentil 95 del score sobre D1_val**
(solo normal) → se acepta ~5% de falsas alarmas por diseño. **Nunca** se ajusta
mirando D2. (Detalle en el fichero 04.)

---

## 7. Dónde vive esto en el código

`evaluacion.py` centraliza todo para que **todos los modelos midan igual**. Lo importan cinco
scripts: `anomalias.py`, `firmas.py`, `baseline.py`, `hibrido.py` y `cascada_invertida.py`.

- `evaluar_binario(y_true, y_pred, y_score=None)` → precision/recall/F1 de la clase ataque,
  accuracy, FPR y la matriz 2×2 desglosada (`tn`, `fp`, `fn`, `tp`); con `y_score`, además
  AUC-ROC y AUC-PR. Si en `y_true` no hay ningún flujo normal, el **FPR sale `NaN`, no 0,0**:
  sin negativos la tasa de falsas alarmas no está definida, y un 0,0 fingiría el mejor
  resultado posible.
- `evaluar_multiclase(y_true, y_pred, labels=None)` → por clase (precision/recall/F1/soporte)
  + macro/weighted + accuracy + matriz de confusión + `classification_report`.
- `evaluar_0day_por_tipo(...)` → recall de cada tipo 0-day, más una clave `__global__` con el
  recall agregado (fichero 04).
- `plot_matriz_confusion(...)`, `plot_roc_pr(...)` → figuras 300 dpi a `Resultados/figuras/`.
- `metricas_tiempo(t_entrenamiento_s, t_inferencia_s, n_inferencia)` → las cinco columnas de
  tiempo. La latencia y el caudal son derivadas del mismo par, así que **o se publican las dos
  o ninguna**: un tiempo no medible deja celda vacía, nunca 0,0.
- `guardar_metricas(fila, csv)` → acumula una fila por experimento; ese CSV es la tabla
  comparativa del capítulo de Resultados.

> [!important] Lo que cambió con T1 (esquema de métricas) — nota del 2026-08-18
> `guardar_metricas()` ya no es un simple *append*. Antes de escribir:
> 1. **Inyecta la procedencia** de la fila: `semilla`, `commit` (hash corto del repo) y `fecha`.
>    Así el número viaja con la corrida que lo produjo, en vez de vivir solo en `config.py`.
> 2. **Valida un conjunto mínimo de columnas y aborta si falta alguna.** En las cuatro tablas
>    principales (`metricas_anomalias/firmas/baseline/hibrido.csv`) exige `algoritmo`,
>    `alcance`, `set_features`, `sin_seleccion`, `n_features`, `semilla`, `commit`, `fecha` y
>    `alcance_tiempo_s`; en las auxiliares, las mismas menos `algoritmo` y `alcance_tiempo_s`.
> 3. **Aborta si la cabecera del fichero y las claves de la fila no coinciden**, en lugar de
>    escribir columnas desalineadas en silencio.
>
> La columna clave para leer las tablas es **`alcance`**: dice *qué clases* y *sobre qué
> partición* se calcula cada fila. Sin ella, dos columnas con el mismo nombre en tablas
> distintas (`recall`, `tiempo_s`) no significan lo mismo y no se pueden comparar. El módulo
> comprueba además la unicidad de las filas (`comprobar_unicidad`) y su recuento
> (`comprobar_recuento`), para que la tabla publicada sea citable sin revisarla a ojo.

---

**Siguiente:** `04_los_tres_modelos.md` — cómo se aplica todo lo anterior en los dos
modelos y cómo se combinan en el sistema híbrido.
