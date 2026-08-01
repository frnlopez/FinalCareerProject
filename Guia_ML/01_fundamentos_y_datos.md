# 01 — Fundamentos y datos

> De qué va el aprendizaje automático, la diferencia entre supervisado y no
> supervisado (la decisión más importante de todo el diseño), y por qué partimos
> el dataset en tres trozos D1/D2/D3.

---

## 1. Qué es "entrenar un modelo de ML"

Un modelo de ML no se programa con reglas escritas a mano. Se le dan **datos** y
un **algoritmo de aprendizaje** ajusta sus parámetros internos hasta que el modelo
reproduce bien un patrón. "Entrenar" = ese proceso de ajuste.

- Cada muestra es un vector de **features** (características) `x`. En NSL-KDD, cada
  fila es una conexión de red descrita por 41 campos originales (duración, bytes,
  flags, tasas de error…) que tras el preprocesado se vuelven 122 → 54 columnas.
- Lo que se quiere predecir es la **etiqueta** `y`. Aquí: si la conexión es
  `normal` o de qué categoría de ataque (`dos`, `probe`, `r2l`, `u2r`).

> [!note] Terminología de tu informe (2.1.2)
> Tus notas ya lo dicen: las entradas `x` son "características, atributos o
> covariables"; cuando `y` es categórica la tarea es de **clasificación**, cuando
> es un número real es **regresión**. Todo este TFG es clasificación.

---

## 2. Supervisado vs no supervisado (la decisión de fondo)

Esta distinción, que en tu nota 2.1.2 es teoría, aquí **define la arquitectura entera**.

### Aprendizaje supervisado
Aprende de pares `(x, y)` **etiquetados**. Se le muestran ejemplos con la respuesta
correcta y aprende a reproducirla. Necesita datos etiquetados de todas las clases
que quieras reconocer.

- Ejemplos (tu 2.1.4): Decision Trees, Random Forests, k-NN, regresión logística, SVM.
- **En este TFG:** el **modelo de firmas** es supervisado. Se entrena con D3, donde
  cada ataque viene con su categoría. Solo sabe reconocer lo que ha visto etiquetado.

### Aprendizaje no supervisado
Solo ve las entradas `x`, **sin etiquetas**. Busca "patrones interesantes" o cosas
que se salen de lo normal. No hay una respuesta correcta contra la que comparar
durante el entrenamiento.

- Ejemplos (tu 2.1.2): clustering (k-means), y **detección de anomalías**
  (Isolation Forest, One-Class SVM).
- **En este TFG:** el **modelo de anomalías** es no supervisado. Se entrena SOLO con
  tráfico normal (D1) y aprende "cómo es lo normal". Cualquier cosa que se desvíe la
  marca como sospechosa, **aunque nunca haya visto ese ataque**.

> [!important] Por qué esta división es la clave del TFG
> Un ataque nuevo (0-day) no está etiquetado en ningún sitio: por definición nadie
> lo ha visto. Un modelo **supervisado** no puede reconocer una clase que nunca vio.
> Uno **no supervisado** sí puede detectarlo como "esto no es normal". Por eso el
> sistema combina los dos: firmas para lo conocido (preciso), anomalías para lo
> desconocido (cobertura). Esto se desarrolla en el fichero 04.

---

## 3. Por qué se separan train y test

Si mides el modelo con los mismos datos con los que aprendió, mides su memoria, no
su capacidad de generalizar. Por eso se reserva un **conjunto de test** que el
modelo **no ve** durante el entrenamiento ni el ajuste. El rendimiento sobre el
test estima el **error de generalización** (tu 2.1.3, paso 5).

> [!warning] Regla de oro del proyecto: D2 es INTOCABLE
> D2 (el test) no se usa NUNCA para entrenar, ni para elegir hiperparámetros, ni
> para fijar umbrales, ni para decidir el balanceo. Todo eso se hace con datos de
> train (D1/D3) vía validación. Tocar D2 antes de la evaluación final es **leakage**
> (fuga de información) e invalida los resultados. Está escrito así en el código
> (`firmas.py`: "D2 es INTOCABLE").

---

## 4. Los tres splits: D1, D2, D3

En lugar del clásico train/test, este TFG parte el dato en **tres** porque hay dos
modelos que necesitan ver cosas distintas.

| Split | Qué contiene | Etiquetado | Para qué |
|---|---|---|---|
| **D1** | solo tráfico **normal** (~67.343) | — (se usa sin etiqueta) | entrenar anomalías (aprender "lo normal") |
| **D3** | solo **ataques conocidos** (~58.630) | sí, por categoría | entrenar firmas (aprender a clasificar ataques) |
| **D2** | **test completo**: normal + ataque (~22.544) | sí (solo para evaluar) | evaluar todo al final |

**Por qué separar D1 y D3 y no entrenar un solo modelo con todo junto:**
- El detector de anomalías **debe** ver solo lo normal, o "aprendería" que los
  ataques también son normales y no los detectaría.
- El clasificador de firmas se entrena solo con ataques porque su trabajo es decir
  *qué tipo* de ataque es, no *si* es ataque (de eso se encarga la etapa de anomalías).

> [!note] Detalle importante para el argumento 0-day
> Los ~17 tipos de ataque que aparecen en D2 pero **no** en el train (D3) son los
> "0-day" del experimento. El modelo de firmas es incapaz de clasificarlos (nunca
> los vio); su detección recae en la etapa de anomalías. Medir cuántos de esos se
> detectan es el resultado central del TFG (fichero 04).

---

## 5. Cómo se cargan en el código

`program.py` genera los CSV y expone un helper:

```python
from program import load_specialized_splits
splits = load_specialized_splits(base_path)   # dict con 'D1','D2','D3'
X_D3 = splits["D3"]["X"]                        # features
y_D3 = splits["D3"]["y_category"]              # categoría (dos/probe/r2l/u2r)
```

El `base_path` decide si cargas la variante de **54 features** (por defecto) o la de
**122** (`--sin-seleccion`). Que sea un parámetro y no algo hardcodeado es la
decisión **Q1/C**: qué set de features usar lo decidirá un experimento con datos,
no una corazonada (fichero 02).

---

**Siguiente:** `02_preparacion_datos.md` — cómo se transforman los datos crudos en
algo que los algoritmos puedan digerir, y cómo se maneja el desbalance.
