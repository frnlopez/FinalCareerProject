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
| `app/program.py` | `NSLKDDPreprocessor` | Carga el dataset, EDA, preprocesamiento y generación de splits D1/D2/D3 |
| `app/validacion.py` | `NSLKDDValidator` | Valida los datos procesados: integridad, distribuciones, drift, outliers |

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
- [x] Balanceo (4.3.4, SMOTE vs class_weight) y selección de características (4.3.5, 122→54) en `program.py`
- [x] Entrenamiento del modelo de anomalías (`anomalias.py`: IsolationForest, OneClassSVM, LocalOutlierFactor, Autoencoder-MLP; umbral p95)
- [x] Entrenamiento del modelo de firmas y extracción de reglas desde D3 (`firmas.py`: DecisionTree, RandomForest, KNN, HistGradientBoosting)
- [x] Baseline RF monolítico de control (`baseline.py`)
- [x] Sistema híbrido (cascada anomalía→firmas) y evaluación conjunta sobre D2 (`hibrido.py`)

> **Estado a 2026-07-16:** el track de CÓDIGO está COMPLETO (todos los scripts implementados, auditados y ejecutados en 54 y 122 features). El trabajo restante del TFG es la redacción de la memoria (track INFORME). Ver `next-steps.md` (roadmap vivo) y `resumen-de-decisiones.md`.

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
- La teoría en prosa de los capítulos 2.x, la 6.2 y la bibliografía final **las escribe
  Francisco**. Ningún agente las redacta; como mucho se propone el guion.

## Git

- Repositorio: `https://github.com/frnlopez/FinalCareerProject.git` — raíz en `Working_Directory/`.
- Se trabaja en **`develop`**. `main` se actualiza solo en hitos y solo si el usuario lo pide.
- Se versiona el **texto plano**: código, notas del vault, `metricas_*.csv`, figuras, reglas.
  Quedan fuera (ver `.gitignore`) el venv, los `.joblib`, los CSV procesados, el dataset crudo y
  los `.doc/.docx` — todo reproducible o descargable, y suman 1,1 GB.
- Un **commit por tarea cerrada**, mensaje en español con prefijo `codigo:` / `informe:` /
  `harness:`.

## Normas de trabajo

- **Lenguaje del proyecto:** Español (notas, comentarios, nombres de secciones).
- **Python:** versión 3.11. No usar f-strings con `=` (walrus) ni sintaxis 3.12+.
- **No commitear:** la carpeta `Imp/` (entorno virtual) ya está en `.gitignore`.
- **Notas Obsidian:** cuando el usuario pida crear o editar una nota, escribirla directamente en `Obsidian_TFG_Vault/` con Markdown estándar compatible con Obsidian (wikilinks `[[enlace]]`, callouts `> [!note]`, etc.).
- **No inventar rutas:** si se necesita una ruta al dataset o a los resultados, usar las hardcodeadas en los scripts o preguntar al usuario.
