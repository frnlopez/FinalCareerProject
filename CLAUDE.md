# CLAUDE.md — TFG Kiko (H-NIDS con ML)

## Contexto del proyecto

Trabajo Fin de Grado sobre un **Sistema Híbrido de Detección de Intrusiones en Red (H-NIDS)** que combina detección por anomalías y detección por firmas usando Machine Learning sobre el dataset NSL-KDD.

---

## Estructura del repositorio

```
Working_Directory/            ← raíz del repositorio git (rama de trabajo: develop)
├── CLAUDE.md                 ← este archivo
├── README.md                 ← presentación del repo y de cada script
├── Proyecto_Fin_de_Grado-FJLM-2026.docx  ← memoria en Word (no versionada). El
│                             `TFG - Fran.docx` que había aquí es un NOMBRE MUERTO
├── Archivos dataset/         ← NSL-KDD crudo (no versionado)
├── Resultados/               ← métricas, figuras y sus CSV, versionados; modelos y splits, no
├── Implementacion/           ← código Python
│   ├── app/                  ← program · validacion · anomalias · firmas ·
│   │                           baseline · hibrido · cascada_invertida ·
│   │                           config · evaluacion
│   ├── Imp/                  ← entorno virtual Python 3.11 (no versionado)
│   ├── diagramas/
│   ├── PIPELINE.md           ← diagrama del pipeline de preprocesado
│   ├── .gitignore            ← plantilla Python; manda sobre el raíz aquí dentro
│   ├── requirements.txt
│   └── readme.md
└── Obsidian_TFG_Vault/       ← la memoria en Markdown (Obsidian)
    ├── 99 Investigación/     ← informes de apoyo documental. NO es memoria
    ├── assets/               ← las imágenes embebidas por las notas (ver abajo)
    ├── Bibliografía.md       ← referencias del TFG
    └── .obsidian/            ← config de Obsidian (no tocar)
```

---

## Implementacion/

### Entorno virtual

```powershell
# Crear (solo la primera vez)
"C:\Python311\python.exe" -m venv Imp

# Activar (PowerShell)
.\Imp\Scripts\Activate.ps1

# Instalar dependencias
pip install -r requirements.txt
```

### Scripts principales

| Archivo | Clase | Función |
|---|---|---|
| `app/program.py` | `NSLKDDPreprocessor` | Carga el dataset, EDA, preprocesamiento y generación de splits D1/D2/D3; expone `load_specialized_splits()`, que usan todos los scripts de modelos |
| `app/validacion.py` | `NSLKDDValidator` | Valida los splits D1/D2/D3 ya generados: integridad, distribuciones, drift y outliers. El drift son **dos** mediciones separadas y no intercambiables (T2): (A) D1 vs D2 completo y (B) D1 vs las 9.711 filas normales de D2. El informe publica `delta = (A) − (B)` como **comparación**, nunca como descomposición: el KS no es aditivo sobre una mezcla (`validacion.py`, cabecera de la sección 4) |
| `app/config.py` | — | Módulo de configuración central: rutas de salida, `base_path()` para elegir el set de 54 o 122 features, las convenciones de clase (0=normal, 1=ataque, `CATEGORIAS_ATAQUE`/`CATEGORIAS_MULTICLASE`) y la procedencia (`commit_actual()`). **La semilla ya no es «semilla 42» a secas:** 42 es `SEMILLA_POR_DEFECTO` y sigue siendo la de todo lo publicado, pero T4 añadió override por CLI (`fijar_semilla()`, `--semilla`), el barrido `SEMILLAS_BARRIDO = [1..10]` —que excluye la 42 a propósito— y el desvío de nombres de artefactos y tablas (`sufijo_semilla()`, `sufijo_artefactos()`, `nombre_tabla_semillas()`), con sufijo vacío cuando la semilla es 42 para no pisar lo publicado |
| `app/evaluacion.py` | — | Módulo común de métricas, figuras **y esquema de las tablas**. **Métricas:** `evaluar_binario`, `evaluar_multiclase`, `evaluar_0day_por_tipo` y `metricas_tiempo` (entrenamiento, latencia por flujo y flujos/s). **Figuras:** `plot_matriz_confusion` y `plot_roc_pr`. **Escritura:** `guardar_metricas` (CSV acumulado). **Y toda la maquinaria de esquema que trajo T1**, que esta fila omitía: `validar_esquema_minimo`, `cabecera_esperada`, `limpiar_variante_csv` (con `_respaldar_csv`), `comprobar_unicidad` y `comprobar_recuento`. Son la razón de que las tablas tengan recuento y unicidad verificables, así que no son un detalle interno: descríbelas al hablar del esquema |
| `app/anomalias.py` | `NSLKDDAnomalyTrainer` | Etapa 1: entrena sobre D1 y compara IsolationForest, OneClassSVM, LocalOutlierFactor y Autoencoder-MLP con score unificado y umbral percentil 95 sobre D1_val |
| `app/firmas.py` | `NSLKDDSignatureTrainer` | Etapa 2: clasificador multiclase de ataques conocidos sobre D3 (DecisionTree, RandomForest, KNN, HistGradientBoosting) con GridSearchCV `f1_macro`, balanceo intra-fold y extracción de reglas legibles. El eje de balanceo depende del algoritmo (`firmas.py:100-108`): SMOTE vs `class_weight` en DecisionTree y RandomForest; SMOTE vs nada en KNN e HistGradientBoosting, que no admiten `class_weight` en sklearn |
| `app/baseline.py` | `NSLKDDBaselineTrainer` | Baseline de control ajeno al híbrido: un único RandomForest monolítico de 5 clases entrenado sobre todo el train y evaluado en D2, con recall 0-day por tipo como métrica de contraste |
| `app/cascada_invertida.py` | `NSLKDDInvertedCascadeMeasurer` | Medición **contrafactual** de la cascada invertida (T3), fuera del sistema: pasa las 9.711 filas normales de D2 por el clasificador de firmas ya persistido y cuenta cuántas condenaría con confianza ≥ `UMBRAL_CONF` (leído de `hibrido_<set>.joblib`, nunca como literal). **Cero `fit`** y D2 solo se reporta (P-4). Tabla propia (`metricas_cascada_invertida.csv`, 5 filas por variante, recuento verificado por `_comprobar_tabla()`): no escribe en ninguna de las cuatro principales. **Su fila `__global__` es una COTA INFERIOR del FPR de un sistema de firmas-primero, no ese FPR** — `unknown` es alarma (P-5), así que lo que cae bajo umbral no queda exonerado |
| `app/hibrido.py` | `NSLKDDHybridEvaluator` | Sistema híbrido en cascada anomalías→firmas: carga los `.joblib` de ambas etapas sin re-entrenarlas y evalúa de extremo a extremo sobre D2 (incluida la clase `unknown`). Única excepción a "no re-entrena" (`hibrido.py:6-9` y el método `_calibrar_umbral_conf`, `hibrido.py:247`): para calibrar el umbral de confianza reconstruye el estimador de firmas desde su config guardada y lo reajusta una vez por fold vía `cross_val_predict`, obteniendo probabilidades out-of-fold sobre D3. La calibración no ve D2, así que no hay leakage |

> Orden de ejecución según las dependencias del código: `program.py` → `anomalias.py` /
> `firmas.py` (independientes entre sí) → `hibrido.py`, que consume los `.joblib` de ambas
> etapas. `validacion.py` es una **puerta de calidad**, no un eslabón del pipeline: lee los
> CSV que deja `program.py` y escribe su informe y sus figuras, pero ningún script de modelos
> lo importa ni consume su salida; se pasa tras `program.py` para confirmar que los splits
> están sanos. `baseline.py` va aparte **del híbrido**, no del preprocesado: es el control
> monolítico, pero depende igual del pipeline (`baseline.py:46` hace
> `from program import load_specialized_splits`). `cascada_invertida.py` va **al final de su
> variante**: necesita el `firma_*.joblib` de `firmas.py` y el `hibrido_*.joblib` de `hibrido.py`
> (de donde lee el umbral), y aborta si falta alguno; es una medición aparte, no un eslabón del
> sistema. `config.py` y `evaluacion.py` no se ejecutan
> (no tienen `__main__`): son librerías internas que importan los cuatro scripts de
> modelos —`anomalias.py`, `firmas.py`, `baseline.py` e `hibrido.py`— **más
> `cascada_invertida.py`**. **`program.py` no depende de ninguna de las dos.
> `validacion.py` sí importa `config.py` desde el 2026-08-11**, en origen **solo por la
> **procedencia**: usa `config.commit_actual()` para estampar `commit` y `fecha` en la cabecera
> de sus informes y en las columnas de sus CSV, en vez de
> duplicar el mecanismo por copia (decisión de Francisco registrada en
> `resumen-de-decisiones.md`, que extiende el alcance de Q2 de las rutas a la procedencia).
> **Esa frontera se ENSANCHÓ el 2026-08-16, y Francisco APROBÓ la extensión ese mismo día.** Al
> emitir el reparto de D3 por categoría, el código pasó a leer también **`config.CATEGORIAS_ATAQUE`**,
> que **no es procedencia**: la Q2 original cubría «rutas → procedencia» y nada más. Lo decidió un
> agente sobre la marcha, se marcó como pendiente y **Francisco lo aprobó al preguntárselo**
> (registrado en `resumen-de-decisiones.md`). **La dependencia cubre hoy TRES cosas: rutas,
> procedencia y el vocabulario de categorías.** Lo que **sigue sin cubrir**, y que ningún agente
> debe dar por extendido: cualquier lectura de `config.py` que **produzca o altere un recuento**.
> Los recuentos salen de `value_counts()` y `len()`.
> **`validacion.py` escribe hoy SEIS artefactos, no cuatro**: los dos `*_validation_report.txt`,
> los dos `*_vocabulario_onehot.csv` y los dos `*_composicion_d3.csv`.
> No importa `evaluacion.py`, y el import no tiene efectos ni ciclos: `config.py` solo define
> constantes y funciones —no llama a `ensure_dirs()` al importarse— y no importa nada del
> proyecto. El encabezado de `config.py` está actualizado en consecuencia. El pipeline de
> preprocesado está diagramado en `Implementacion/PIPELINE.md`, que además guarda el **runbook**
> de las tablas de métricas y la lectura de la cascada invertida.

### Dataset y rutas

Los scripts tienen rutas hardcodeadas a (verificado en disco y en `program.py`, 2026-07-16):
- **Dataset:** `C:\Users\francisco.lopez\KIKO_TFG\Working_Directory\Archivos dataset\KDDTrain+.txt` y `KDDTest+.txt`
- **Salida:** `C:\Users\francisco.lopez\KIKO_TFG\Working_Directory\Resultados\` (las figuras en `Resultados\figuras\`)

Dataset descargable de: https://github.com/Jehuty4949/NSL_KDD

### Splits generados por program.py

| Split | Contenido | Uso |
|---|---|---|
| D1 | Solo tráfico normal | Entrenamiento del modelo de anomalías |
| D2 | Set de test completo | Evaluación realista |
| D3 | Solo ataques conocidos | Extracción de reglas/firmas |

### Categorías de ataque (39 tipos de ataque → 5 categorías)

`normal`, `dos`, `probe`, `r2l`, `u2r`

> El `LabelEncoder` del pipeline maneja **40 etiquetas**: `normal` + 39 tipos de ataque (verificado en `specialized_nsl_kdd_mappings_and_info.txt`, "Total de ataques específicos: 40" incluye `normal`). Estos 39 tipos se agrupan en las 4 categorías de ataque (+`normal`). La cifra "51" que se citaba antes era errónea.

### Estado actual del código

- [x] Carga y EDA del dataset NSL-KDD
- [x] Preprocesamiento (One-Hot Encoding, MinMaxScaler/StandardScaler, LabelEncoder)
- [x] Validación de datos procesados
- [x] Selección de características (4.3.5, 122→54) en `program.py` (`select_features()`); mini-experimento de balanceo (4.3.4, SMOTE vs class_weight/nada, decidido por algoritmo) en `firmas.py`
- [x] Entrenamiento del modelo de anomalías (`anomalias.py`: IsolationForest, OneClassSVM, LocalOutlierFactor, Autoencoder-MLP; umbral p95)
- [x] Entrenamiento del modelo de firmas y extracción de reglas desde D3 (`firmas.py`: DecisionTree, RandomForest, KNN, HistGradientBoosting)
- [x] Baseline RF monolítico de control (`baseline.py`)
- [x] Sistema híbrido (cascada anomalía→firmas) y evaluación conjunta sobre D2 (`hibrido.py`)
- [x] KS de D1 contra los normales de D2 (T2, en `validacion.py`) y medición de la cascada invertida (T3, `cascada_invertida.py`) — las dos del lote de reapertura del 2026-08-06

> **Estado a 2026-07-16:** el track de CÓDIGO estaba COMPLETO (todos los scripts implementados, auditados y ejecutados en 54 y 122 features) y el trabajo restante era la redacción (track INFORME).
>
> **Reabierto el 2026-08-06** de forma declarada y acotada (decisión marco (a)): esquema de métricas (T1), dispersión entre semillas (T4) y dos mediciones baratas (T2, T3). Todo pasa por una revisión adversaria separada. El alcance abierto vive en `features.md`, no aquí.

**Reparto de roles entre ficheros de seguimiento (desde el 2026-08-01):** el registro operativo vivo (tareas abiertas y cerradas) es `features.md`; `next-steps.md` está congelado en cuanto a casillas (§1-§5 historial y bitácora, §6 vigente como especificación técnica de cada script, salvo §6.5 (`hibrido.py`), superada por el grill H-1…H-7 de `resumen-de-decisiones.md`) y las decisiones de diseño están en `resumen-de-decisiones.md`.

### Dependencias principales

```
numpy, pandas, scikit-learn, imbalanced-learn, matplotlib, seaborn, scipy, joblib, pillow
```
> Versiones exactas fijadas (*pinning*) en `Implementacion/requirements.txt`.

---

## Obsidian_TFG_Vault/

Aquí se escriben y gestionan las **notas del TFG en Markdown**. Obsidian las lee directamente.

- Puedo crear, editar y organizar archivos `.md` en esta carpeta a petición del usuario.
- La carpeta `.obsidian/` contiene la configuración del vault; no modificarla salvo que se pida explícitamente.
- Los archivos de esta carpeta son documentación/notas, no código ejecutable.

---

## Proyecto_Fin_de_Grado-FJLM-2026.docx

Memoria **final y oficial** del TFG en formato Word, ubicada en este repo
(`Working_Directory/Proyecto_Fin_de_Grado-FJLM-2026.docx`). **Se llamaba `TFG - Fran.docx`; ese
nombre está MUERTO desde el 2026-08-26** — el fichero viejo sigue en disco (mtime 2026-06-11) pero
ya no es la memoria: no lo leas ni lo cites. Conviven además un `.doc` gemelo y
`Plantilla-para-volcado.docx`, que tampoco son la memoria.

**Se extrae, no se lee en crudo.** Las extracciones viven en `Resultados/docx/REPASO_<fecha>/`.
**Antes de comparar nada contra él, verifica el `mtime` del `.docx` contra el `_PROCEDENCIA.txt` de
la última extracción**: el documento cambia entre mensajes y una extracción de hace unas horas ya
miente. Si existe un `~$Proyecto_Fin_de_Grado-FJLM-2026.docx`, **está abierto en Word y cualquier
re-extracción es inválida**: hay que pedir a Francisco que lo cierre.

No se edita desde aquí; se referencia para contexto cuando el usuario necesita alinear notas o código con el contenido del informe. Las notas de `Obsidian_TFG_Vault/` son la fuente que se vuelca a este documento.

---

## Git

- Repositorio: `https://github.com/frnlopez/FinalCareerProject.git` — raíz en `Working_Directory/`.
- Se trabaja en **`develop`**. `main` se actualiza solo en hitos y solo si el usuario lo pide.
- Se versiona el **texto plano**: código, notas del vault, figuras, reglas y **los CSV citables**
  —`metricas_*.csv`, `dispersion_semillas.csv`, **`comparaciones_pareadas.csv`**,
  `*_vocabulario_onehot.csv` y `*_composicion_d3.csv`—. (`comparaciones_pareadas.csv` lo emite
  `agregar_semillas.py` junto a `dispersion_semillas.csv`/`.md` y faltaba en esta lista hasta el
  2026-08-17, aunque ya estaba versionado: la enumeración se contradecía con sus cuatro hermanos.)
  Quedan fuera (ver `.gitignore`) el venv, los `.joblib`, **los CSV de los splits**, el dataset
  crudo y los `.doc/.docx` — todo reproducible o descargable, y suman 1,1 GB.
  **Y, desde el 2026-08-29, todo el material de trabajo interno**: `.claude/`,
  `resumen-de-decisiones.md`, `features.md`, `next-steps.md`, `how-to-work.md`,
  `mis-apuntes-del-informe.md`, `EL_FUTURO.md`, `andamiaje-interno.md` y los `sesion-2026-07-*.md`.
  Siguen **vivos en disco** y siguen siendo la referencia de trabajo: lo unico que cambia es que
  no se publican, porque el enlace al repositorio va en la memoria. **El historico NO se reescribio**:
  quien mire `git log` los seguira viendo en los commits anteriores. Fue una decision consciente
  de Francisco para no alterar los SHA con la entrega encima.
  **«Los CSV no se versionan» es FALSO y lo decía este fichero hasta el 2026-08-16.** La regla real
  del `.gitignore` es por patrón, no por extensión: solo excluye `Resultados/*_processed_*.csv` y
  `Resultados/*_original_*.csv`, que son los splits —regenerables y pesados—. **Todo lo demás en
  `Resultados/` se versiona**, y hay 20+ CSV dentro. Si dudas, `git ls-files 'Resultados/*.csv'`.
- Un **commit por tarea cerrada, o un commit por tanda paralela** nombrando en el cuerpo las
  fichas que cierra; mensaje en español con prefijo `codigo:` / `informe:` / `harness:`.
  **Por qué la tanda cuenta como unidad** (decisión de Francisco del 2026-08-14, Decisión 7 de la
  Fase 0): bajo despacho en paralelo los 3-4 agentes de una tanda terminan sobre **el mismo estado
  del árbol**, así que trocear su cierre en 3-4 commits sería granularidad **ficticia** — no habría
  estados intermedios recuperables y `git log` prometería una trazabilidad que no existe.
- **`Implementacion/` NO tiene repositorio git propio y no debe recrearse**: el repo anidado que
  había ahí se absorbió en el repo padre (commit `fb920b8`, 2026-08-01), así que su contenido se
  versiona como el resto del árbol. Nada de `git init` dentro de `Implementacion/`.
- `Implementacion/.gitignore` es la plantilla Python de GitHub (heredada de aquel repo) **más dos
  líneas locales**: `Imp/` —redundante con el `Implementacion/Imp/` del raíz— y
  `virtualEnvPRECLAIMS/`. Convive con el `.gitignore` de la raíz: ambos se aplican.
- **Precedencia:** el de la raíz aplica a todo el árbol, pero **en caso de conflicto manda
  `Implementacion/.gitignore` dentro de `Implementacion/`** — en git, el `.gitignore` de nivel
  inferior anula al superior dentro de su subárbol. Importa porque ese fichero anidado ignora
  `*.log`, `lib/`, `build/`, `dist/`, `docs/_build/`, `.env` y bastantes más: una re-inclusión
  `!…` escrita en el `.gitignore` raíz **no** rescataría un artefacto que caiga dentro de
  `Implementacion/`. Si hay que versionar algo así, la excepción se escribe en el anidado.

## Normas de trabajo

- **Lenguaje del proyecto:** Español (notas, comentarios, nombres de secciones).
- **Python:** versión 3.11. No usar f-strings con `=` (walrus) ni sintaxis 3.12+.
- **No commitear:** la carpeta `Imp/` (entorno virtual) ya está en `.gitignore`.
- **Notas Obsidian:** cuando el usuario pida crear o editar una nota, escribirla directamente en `Obsidian_TFG_Vault/` con Markdown estándar compatible con Obsidian (wikilinks `[[enlace]]`, callouts `> [!note]`, etc.).
- **Imágenes del vault — `Obsidian_TFG_Vault/assets/`.** Ahí viven **todos** los ficheros que las notas
  embeben con `![[nombre.png]]`; no hay imágenes en ninguna otra carpeta del vault. **Censo verificado el
  2026-08-18:** **36 ficheros en la carpeta**, **24 nombres distintos embebidos** en **24 embebidos** de
  **6 notas** (el desfase 27 vs 24 que hubo hasta la Tanda 28 eran figuras repetidas: 4.8/4.9 duplicaban
  4.1/4.2 y 5.11/5.12 eran el mismo `.png`; **retiradas el 2026-08-18**, hoy no hay ningún duplicado), y **12 ficheros huérfanos**
  que no embebe nadie. **Ningún embebido roto:** los 24 existen en disco. Las figuras las genera el código
  en `Resultados/figuras/` y se copian aquí a mano, así que **`assets/` no se regenera solo**: si una
  figura se rehace, hay que volver a copiarla. **Los 24 embebidos llevan pie numerado** con el criterio
  `Figura <capítulo>.<orden>`, en series **contiguas y sin duplicados**: `2.1`–`2.5`, `4.1`–`4.7` y
  `5.1`–`5.12` (el `2.1`–`2.4` que decía este fichero **ya era falso antes** de la Tanda 28) y **se llaman por número desde la
  prosa**, que es lo que les da referencia cruzada al volcarlas al `.docx`.
- **Referenciar por TÍTULO, nunca por `fichero:línea`.** Al remitir a una sede dentro de una nota,
  un script o un fichero de seguimiento, se cita el **título de la sección, el encabezado o un
  fragmento literal del texto**, no el número de línea. Los números de línea **caducan en cuanto
  alguien edita el fichero por encima**, y este proyecto ya ha mandado agentes a corregir líneas
  que habían dejado de existir: el 2026-08-18 se contaron **doce ocurrencias en una sola sesión**,
  ocho de ellas por esta causa —incluida la vez que el desfase mordió al propio bloque que lo
  denunciaba, cuyas referencias nacieron desplazadas **+456 líneas** al insertarse él mismo al
  inicio de `## Abiertas`—. Un `fichero:línea` solo es admisible como **pista auxiliar junto al
  título**, nunca como única referencia, y quien lo lea **debe localizar el destino por contenido
  antes de editarlo**.
- **No inventar rutas:** si se necesita una ruta al dataset o a los resultados, usar las hardcodeadas en los scripts o preguntar al usuario.
