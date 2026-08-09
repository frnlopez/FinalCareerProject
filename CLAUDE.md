# CLAUDE.md — TFG Kiko (H-NIDS con ML)

## Contexto del proyecto

Trabajo Fin de Grado sobre un **Sistema Híbrido de Detección de Intrusiones en Red (H-NIDS)** que combina detección por anomalías y detección por firmas usando Machine Learning sobre el dataset NSL-KDD.

---

## Estructura del repositorio

```
Working_Directory/            ← raíz del repositorio git (rama de trabajo: develop)
├── CLAUDE.md                 ← este archivo
├── README.md                 ← presentación del repo y de cada script
├── features.md               ← tareas abiertas y cerradas. LO PRIMERO que se lee
├── next-steps.md             ← CONGELADO en casillas. §1-§5 historial · §6 specs
├── resumen-de-decisiones.md  ← decisiones de diseño cerradas
├── EL_FUTURO.md              ← líneas futuras respaldadas con datos
├── .mcp.json                 ← MCP de Playwright (solo lo usa el researcher)
├── .claude/                  ← arquitectura de agentes (ver sección propia)
├── TFG - Fran.docx           ← memoria en Word (no versionada)
├── Archivos dataset/         ← NSL-KDD crudo (no versionado)
├── Resultados/               ← métricas y figuras versionadas; modelos y CSV, no
├── Implementacion/           ← código Python
│   ├── app/                  ← program · validacion · anomalias · firmas ·
│   │                           baseline · hibrido · config · evaluacion
│   ├── Imp/                  ← entorno virtual Python 3.11 (no versionado)
│   ├── diagramas/
│   ├── PIPELINE.md           ← diagrama del pipeline de preprocesado
│   ├── .gitignore            ← plantilla Python; manda sobre el raíz aquí dentro
│   ├── requirements.txt
│   └── readme.md
└── Obsidian_TFG_Vault/       ← la memoria en Markdown (Obsidian)
    ├── 99 Investigación/     ← informes del researcher. NO es memoria
    ├── Bibliografía.md       ← lo escribe SOLO el researcher
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
| `app/validacion.py` | `NSLKDDValidator` | Valida los splits D1/D2/D3 ya generados: integridad, distribuciones, drift y outliers |
| `app/config.py` | — | Módulo de configuración central: semilla 42, rutas de salida, `base_path()` para elegir el set de 54 o 122 features y las convenciones de clase (0=normal, 1=ataque, orden de categorías) |
| `app/evaluacion.py` | — | Módulo común de métricas y figuras: `evaluar_binario`, `evaluar_multiclase`, `evaluar_0day_por_tipo`, matrices de confusión, curvas ROC/PR y `guardar_metricas` (CSV acumulado) |
| `app/anomalias.py` | `NSLKDDAnomalyTrainer` | Etapa 1: entrena sobre D1 y compara IsolationForest, OneClassSVM, LocalOutlierFactor y Autoencoder-MLP con score unificado y umbral percentil 95 sobre D1_val |
| `app/firmas.py` | `NSLKDDSignatureTrainer` | Etapa 2: clasificador multiclase de ataques conocidos sobre D3 (DecisionTree, RandomForest, KNN, HistGradientBoosting) con GridSearchCV `f1_macro`, balanceo intra-fold y extracción de reglas legibles. El eje de balanceo depende del algoritmo (`firmas.py:91-96`): SMOTE vs `class_weight` en DecisionTree y RandomForest; SMOTE vs nada en KNN e HistGradientBoosting, que no admiten `class_weight` en sklearn |
| `app/baseline.py` | `NSLKDDBaselineTrainer` | Baseline de control ajeno al híbrido: un único RandomForest monolítico de 5 clases entrenado sobre todo el train y evaluado en D2, con recall 0-day por tipo como métrica de contraste |
| `app/hibrido.py` | `NSLKDDHybridEvaluator` | Sistema híbrido en cascada anomalías→firmas: carga los `.joblib` de ambas etapas sin re-entrenarlas y evalúa de extremo a extremo sobre D2 (incluida la clase `unknown`). Única excepción a "no re-entrena" (`hibrido.py:6-9`, `184-192`): para calibrar el umbral de confianza reconstruye el estimador de firmas desde su config guardada y lo reajusta una vez por fold vía `cross_val_predict`, obteniendo probabilidades out-of-fold sobre D3. La calibración no ve D2, así que no hay leakage |

> Orden de ejecución según las dependencias del código: `program.py` → `anomalias.py` /
> `firmas.py` (independientes entre sí) → `hibrido.py`, que consume los `.joblib` de ambas
> etapas. `validacion.py` es una **puerta de calidad**, no un eslabón del pipeline: lee los
> CSV que deja `program.py` y escribe su informe y sus figuras, pero ningún script de modelos
> lo importa ni consume su salida; se pasa tras `program.py` para confirmar que los splits
> están sanos. `baseline.py` va aparte **del híbrido**, no del preprocesado: es el control
> monolítico, pero depende igual del pipeline (`baseline.py:46` hace
> `from program import load_specialized_splits`). `config.py` y `evaluacion.py` no se ejecutan
> (no tienen `__main__`): son librerías internas que importan **solo los cuatro scripts de
> modelos** —`anomalias.py`, `firmas.py`, `baseline.py` e `hibrido.py`—; `program.py` y
> `validacion.py` NO dependen de ellas, como dice `config.py:9-10`. El pipeline de preprocesado
> está diagramado en `Implementacion/PIPELINE.md`.

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

> **Estado a 2026-07-16:** el track de CÓDIGO está COMPLETO (todos los scripts implementados, auditados y ejecutados en 54 y 122 features). El trabajo restante del TFG es la redacción de la memoria (track INFORME).

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

## TFG - Fran.docx

Memoria **final y oficial** del TFG en formato Word, ubicada en este repo (`Working_Directory/TFG - Fran.docx`). No se edita desde aquí; se referencia para contexto cuando el usuario necesita alinear notas o código con el contenido del informe. Las notas de `Obsidian_TFG_Vault/` son la fuente que se vuelca a este documento.

---

## Arquitectura de agentes

Cada mensaje del usuario pasa por el hook `UserPromptSubmit` (`.claude/hooks/leader-gate.sh`),
que inyecta la regla de enrutado y el `git status` del repo. **El hilo principal no responde: delega
en el agente `leader`**, que clasifica en un **carril** y un **track** y despacha.

| Carril | Qué es | Interroga | Ficha | Cierre |
|---|---|---|---|---|
| **Consulta** | Pregunta sobre estado, resultados o una decisión | No | No | No |
| **Intervención** | Cambio pequeño y entendido | No | No | Sí |
| **Tarea** | Alcance nuevo que hay que definir | Sí (`grill-me`) | Sí | Sí |
| **Investigación** | El usuario pide investigar algo que no está en disco | Sí, salvo encargo ya cerrado | No | No |

| Track | Agente |
|---|---|
| **Código** | `ml-implementador` → `auditor-ml` (obligatorio); `ejecutor-experimentos` para correr |
| **Informe** | `redactor-tfg` |
| **Ninguno** | `researcher` (investigar y verificar fuentes) · `cronista` (mantener `features.md`) |

Excepción única al enrutado: **configurar el propio andamiaje** (`settings.json`, hooks,
`.claude/agents/`, skills, `.mcp.json`) lo atiende el hilo principal directamente.

**Reglas duras del andamiaje:**

- **Ningún subagente habla con el usuario.** No tienen canal: devuelven `done -> <ficheros>` o
  `blocked -> <descripción>`. Lo que requiera preguntar vuelve al hilo principal.
- **Ningún agente ejecuta `git` de escritura.** El `add`/`commit`/`push` lo hace el skill
  `cierre`, en hilo principal y **preguntando siempre**. El `git status` de lectura lo ejecuta
  el hook, no un agente.
- **El `researcher` solo se despacha si el usuario lo pide explícitamente**, y con el encargo
  cerrado: pregunta concreta, qué entra y qué queda fuera.
- **Track Código no se cierra sin `auditor-ml`.**
- **No hay máquina de estados**: lo abierto es lo que está en `features.md`; lo hecho es lo que
  tiene commit.
- **Autoría de la redacción** (decisión marco (b) del lote 2026-08-06, aplicada en T0 el
  2026-08-09; sustituye a la regla anterior «la teoría en prosa la escribe Francisco»):
  - **Capítulos 2.x — sin restricción.** El `redactor-tfg` redacta la prosa a partir de los
    guiones que ya están en las notas. Aplica a **todo** el capítulo 2, `2.1.4` incluida: no hay
    ninguna sección exceptuada.
  - **`6.2 Líneas futuras` — borrador de agente con revisión final de Francisco.** Es el sitio
    natural del material de líneas futuras; bloqueada dejaba a medias un entregable del encargo.
    Material de respaldo en `EL_FUTURO.md`.
  - **`4.2` (prosa teórica del dataset) — ya cedida antes**, por la decisión del 2026-07-21
    (`resumen-de-decisiones.md:430-438`): «Origen» y «Las 41 características» las redacta el
    agente —el borrador **ya existe** en la nota—; solo el «por qué NSL-KDD» queda a revisión de
    Francisco. El contenido lo cierra **T10**.
  - **La bibliografía final en Zotero/IEEE sigue siendo de Francisco.** Es trabajo mecánico en
    su máquina. `Bibliografía.md` dentro del vault es del `researcher`, que es otra cosa.

## Git

- Repositorio: `https://github.com/frnlopez/FinalCareerProject.git` — raíz en `Working_Directory/`.
- Se trabaja en **`develop`**. `main` se actualiza solo en hitos y solo si el usuario lo pide.
- Se versiona el **texto plano**: código, notas del vault, `metricas_*.csv`, figuras, reglas.
  Quedan fuera (ver `.gitignore`) el venv, los `.joblib`, los CSV procesados, el dataset crudo y
  los `.doc/.docx` — todo reproducible o descargable, y suman 1,1 GB.
- Un **commit por tarea cerrada**, mensaje en español con prefijo `codigo:` / `informe:` /
  `harness:`.
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
- **No inventar rutas:** si se necesita una ruta al dataset o a los resultados, usar las hardcodeadas en los scripts o preguntar al usuario.
