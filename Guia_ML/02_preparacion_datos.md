# 02 — Preparación de los datos

> Los algoritmos no digieren texto ni categorías crudas, y sufren con clases muy
> desbalanceadas o con features inútiles. Este fichero cubre las tres cosas que se
> hacen antes de entrenar: **codificar/escalar**, **balancear** y **seleccionar
> características**. Todo esto es tu 2.1.3 ("limpieza y procesamiento") aplicado.

---

## 1. Preprocesamiento: de datos crudos a matriz numérica

### One-Hot Encoding
Tres columnas de NSL-KDD son **categóricas** (texto): `protocol_type` (tcp/udp/icmp),
`service` (http, ftp, smtp… decenas) y `flag` (estado de la conexión). Un modelo no
puede multiplicar "http". El One-Hot convierte cada categoría en una **columna 0/1**:

```
service = http   →   service_http=1, service_ftp=0, service_smtp=0, ...
```

- Por qué así y no un número (http=1, ftp=2…): eso inventaría un orden falso
  ("ftp > http") que el modelo interpretaría como magnitud. El One-Hot no impone orden.
- Precio: muchas columnas. De ahí que pasemos de 41 campos a 122 features.

> [!warning] La trampa del vocabulario (bug del "Paso 0", ya arreglado)
> Al principio el vocabulario de columnas se construía **solo con D1 (normal)**. Los
> servicios/flags que solo aparecen en ataques (D3) se descartaban → el modelo de
> firmas perdía justo las señales más discriminantes. **El fix:** vocabulario =
> unión ordenada de **D1+D3** (el train completo). Subió de 77 a 122 features
> (+45 dummies de ataque recuperados). Las categorías que solo salen en D2 (test) se
> dejan fuera **a propósito**: en producción tampoco las conocerías de antemano.

### Escalado (normalización)
Las features numéricas viven en rangos dispares (`duration` en segundos, `src_bytes`
en millones, una tasa entre 0 y 1). Algoritmos basados en distancia (KNN, One-Class
SVM) o en reconstrucción (autoencoder) se dejan dominar por la feature de rango más
grande. El escalado las lleva a un rango común.

- Se usa **MinMaxScaler** → todo a **[0, 1]**. Elegido porque OCSVM, KNN y el
  autoencoder van mejor en [0,1] (los árboles y bosques no lo necesitan, pero no les
  perjudica).
- **Detalle sin leakage:** el scaler se ajusta con el **train (D1+D3)** y se *aplica*
  a D2. Nunca se ajusta con D2. Por eso D2 escalado puede salirse un poco de [0,1]
  (algún valor de test mayor que el máximo visto en train): es esperable y correcto.

> [!note] LabelEncoder
> Es lo mismo pero para la **etiqueta** `y`: convierte `dos/probe/r2l/u2r` en
> 0/1/2/3 para que el modelo trabaje con números. No afecta a las features.

---

## 2. Desbalance de clases y balanceo

### El problema
D3 está brutalmente desbalanceado: `dos` ~45.900 muestras frente a **`u2r` 52**
(cifra exacta, en `Resultados/specialized_nsl_kdd_composicion_d3.csv`).
Un modelo que solo quiera acertar mucho aprende a decir siempre "dos" e ignorar u2r:
tendría un *accuracy* altísimo y sería **inútil** para lo que importa (detectar los
ataques raros, que suelen ser los más peligrosos).

> [!important] Por eso NO medimos con accuracy, sino con **f1_macro**
> La media *macro* da el mismo peso a cada clase, así que ignorar u2r se penaliza.
> Ver fichero 03. La métrica y el balanceo atacan el mismo problema por dos vías.

### Las dos herramientas para balancear

**a) `class_weight='balanced'`** — no toca los datos. Le dice al algoritmo que un
error en una clase rara "cuesta" más, en proporción inversa a su frecuencia. Así el
modelo presta atención a u2r. Lo tienen DecisionTree y RandomForest; **no** lo tienen
KNN ni HistGradientBoosting.

**b) SMOTE (Synthetic Minority Over-sampling Technique)** — sí toca los datos.
Genera muestras **sintéticas** de la clase minoritaria: coge una muestra de u2r, mira
sus `k` vecinos más cercanos de la misma clase, y crea puntos nuevos **interpolando**
entre ellos (no copia: inventa puntos intermedios). Así u2r deja de tener 52 muestras
y pasa a estar equilibrada con el resto.

- Parámetro `k_neighbors` (aquí 5): cuántos vecinos usa para interpolar. Con u2r tan
  pequeña hay que vigilarlo; si una clase tiene menos de `k+1` muestras, SMOTE falla y
  hay que bajar a 3.

> [!warning] SMOTE SOLO dentro de cada fold del CV — nunca antes
> Si generas sintéticos **antes** de partir en train/validación, algunos sintéticos
> derivados del train acaban en la validación → el modelo se evalúa en parte sobre
> datos que "conoce" → CV **optimista** (leakage). Solución en el código: SMOTE va
> dentro de un `ImbPipeline`, de modo que `cross_val_score` lo aplica **dentro de
> cada fold**, solo al train de ese fold. (Ver `firmas.py::_envolver_balanceo`.)

> [!note] Limitación de SMOTE aquí (a citar en la memoria 4.3.4)
> Muchas de nuestras 122/54 features son dummies 0/1 del One-Hot. SMOTE interpola y
> produce valores intermedios (p. ej. 0,37) sobre columnas que solo deberían ser 0 ó
> 1. Funciona, pero es una limitación conceptual que hay que mencionar.

### El mini-experimento de balanceo (sección 4.3.4)
No decidimos a ojo. `firmas.py` compara, por algoritmo, **SMOTE vs class_weight**
(en DT/RF) o **SMOTE vs nada** (en KNN/HistGB, que no tienen class_weight), midiendo
`f1_macro` en CV. El ganador de cada algoritmo se usa para el entrenamiento final. Esa
tabla ES el contenido de la sección 4.3.4 de la memoria.

---

## 3. Selección de características

### El problema y la idea
Tras el One-Hot hay 122 features. Muchas aportan poco: columnas casi constantes, o
pares que dicen lo mismo (correlacionadas). Menos features = modelo más simple, más
rápido y menos propenso a sobreajustar. En tu 2.1.3 aparece como paso "opcional"; aquí
lo hacemos y lo justificamos.

### Cómo se hace (dos pasos, en `program.py::select_features`)
1. **Filtro barato:** eliminar features con **varianza ≈ 0** (una columna que casi
   siempre vale lo mismo no distingue nada) y, de cada par con **correlación > 0,95**,
   conservar una sola (la otra es redundante).
2. **Importancias de Random Forest:** se entrena un RandomForest sobre D1+D3 con las 5
   clases y se ordenan las features por su `feature_importances_`. Se conservan las que
   acumulan el **99,9%** de la importancia total → quedan **54 features**.

> [!warning] Trampa de la varianza (auditoría, ya resuelta)
> La varianza hay que calcularla sobre **D1+D3**, no solo sobre D1. Si se calcula solo
> con D1 (normal), los dummies que solo aparecen en ataques parecen "constantes" y se
> borrarían — deshaciendo el fix del Paso 0 en silencio. El código ya lo hace sobre D1+D3.

### El riesgo abierto (H1) y por qué el set de features está "en el aire"
La selección es **supervisada** (usa importancias RF con las etiquetas de 5 clases).
Está optimizada para separar normal-vs-ataque, que es justo lo que necesita **firmas**.
Pero el detector de **anomalías** es no supervisado y solo ve normal: una feature casi
constante en tráfico normal —que la selección podría tirar— puede ser la **única
señal de un 0-day**.

> [!important] Decisión Q1/C: no fijar el set a ciegas
> Por eso los scripts cargan el set de features **por parámetro** (54 por defecto, 122
> con `--sin-seleccion`). Un **experimento con datos** (54 vs 122, midiendo *recall
> 0-day por tipo* además de F1) decidirá qué usa cada modelo. Resultado probable:
> firmas con 54, anomalías quizá con 122. Se resuelve cuando existan los baselines.

---

**Siguiente:** `03_validacion_y_metricas.md` — cómo se ajustan los hiperparámetros
sin hacer trampas y cómo se mide de verdad si un modelo es bueno.
