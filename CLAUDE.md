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
    ├── 99 Investigación/     ← informes del researcher. NO es memoria
    ├── assets/               ← las imágenes embebidas por las notas (ver abajo)
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
> **Reabierto el 2026-08-06** de forma declarada y acotada (decisión marco (a)): esquema de métricas (T1), dispersión entre semillas (T4) y dos mediciones baratas (T2, T3). Todo pasa por `auditor-ml`. El alcance abierto vive en `features.md`, no aquí.

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
- **Track Código no se cierra sin `auditor-ml`.** Y **el que escribe no puede ser el que audita**:
  la revisión es un pase separado, con instrucción adversaria explícita.
- **Despacho en paralelo (desde el 2026-08-13).** El track Informe es el grueso de lo que queda y
  se acelera despachando varias notas a la vez. **La unidad es el FICHERO, no el tema**: dos
  agentes trabajan a la vez solo si escriben ficheros distintos. Las 8 notas en guion del capítulo
  2 son el caso claro (tandas de 3-4). **Nunca en paralelo:** dos agentes sobre la misma nota,
  `Bibliografía.md`, `features.md`, `00 Índice TFG.md`, la asignación de números `[n]`, ni el pase
  de `auditor-ml` (va después, no a la vez). **Varios `auditor-ml` sí pueden ir en paralelo**: son
  de solo lectura. Un cierre por **tanda**, no por nota: una sola pasada de `cronista`.
- **Protocolo de citas — vale para CUALQUIER agente que escriba en el vault.** Los marcadores `[n]`
  son un **contador global** que apunta a `Bibliografía.md`. **Contado en disco el 2026-08-24, tras las 32 altas
  del mapeo de la bibliografía del `.docx`: se han emitido 110 números, de los que 102 son ENTRADAS VIVAS
  y OCHO están QUEMADAS —`[9]`,
  `[27]`, `[28]`, `[37]`, `[40]`, `[44]`, `[45]` y `[76]`—.** Quemada significa **retirada SIN RENUMERAR**
  (`[9]` lo fue en `396e283`; las otras siete, al retirarse las entradas que ya no citaba ningún
  marcador vivo — `[40]` Krizhevsky, la última, en R1 el 2026-08-20): el número **no vuelve al contador jamás**. **El primer número disponible es el
  `[111]`.** Ojo con `[76]`: está quemada, pero **`[78]` Storkey sí está viva** — nació al desdoblarla. **Este rango se cuenta, no se recuerda**
  (`grep -oE '^\| *\[[0-9]+\]' Bibliografía.md`): estuvo desfasado en `leader.md` diciendo `[11]`
  cuando ya iba por el `[57]`, y ese es justo el fichero que despacha.
  Importa porque `[2]` (Anderson 1980) y `[3]` (Denning 1987) son las que más se citan al redactar
  el capítulo 2: **se MAPEAN, no se dan de alta**.
  **Nadie inventa un `[n]` nuevo**: se escribe `[CITA: autor o tema]`, convención
  que el proyecto ya usa. Si dos agentes en paralelo asignaran números, los dos
  empezarían en el mismo y el solape no lo ve nadie al leer. La conversión de `[CITA: …]` a `[n]` y
  el alta en `Bibliografía.md` es un pase **posterior y en serie**, del `researcher`. Un `[n]` que
  ya estaba en la nota **se respeta**: no se renumera ni se borra.
- **Localizador de página — DEROGADO PARA EL `.docx` el 2026-08-24. No lo reintroduzcas.**
  La decisión del 2026-08-15 admitía localizador en el marcador (`[8, p. 45]`, `[5, cap. 1]`) y lo
  hacía **obligatorio** en los 9 libros largos. **Francisco la derogó el 2026-08-24**, con estas
  palabras: «Quita los capítulos, deja las referencias a pelo `[12]`, `[13]`, `[14]`». Registrada en
  `resumen-de-decisiones.md`.
  - **El marcador que va al `.docx` se escribe A PELO: `[39]`, nunca `[39, cap. 1]`.** Ningún agente
    vuelve a añadir localizador a un marcador, ni en el vault ni en los ficheros de trabajo. Los 28
    que había se retiraron ese mismo día.
  - **Lo que NO se derogó: el registro de la obra.** `Bibliografía.md` conserva su columna
    «Localizador por uso», que sigue escribiendo **solo el `researcher`**. Saber de qué libro o
    página salió una afirmación sigue siendo obligatorio; lo que ya no se hace es **estamparlo en
    el marcador**.
  - **Y sigue en pie que la página no se inventa:** donde no se pueda establecer con honestidad, se
    MARCA. Misma disciplina que con las 47 citas reconstruidas.
  - Ojo con el falso amigo, que no es un localizador y **sí se conserva**: los `pp. 222-232` que
    aparecen en algunas entradas son **el rango del artículo en su revista**, metadato de la
    referencia.
  - Los 9 libros largos siguen siendo los mismos como **obras**, para el registro:
    `[4]` Chio, `[5]` Géron, `[6]` Goodfellow, `[7]` Murphy, `[8]` Stallings (**5.ª ed. 2023**,
    fijada el 2026-08-18), `[12]` Hastie, `[39]` Russell y Norvig, `[54]` Molnar y `[78]` Storkey.
    Lo que cambia es que **ya no arrastran localizador al marcador**.
  - **Sobre `[54]` Molnar:** la edición **ya está fijada** — la declaración de «edición sin fijar» que
    había aquí es FALSA desde el 2026-08-18 y se retira; no la reintroduzcas. Lo que se decía de que
    «bloqueaba localizadores del capítulo 2» dejó de aplicar en dos pasos: primero al reasignar el
    Isolation Forest a `[73]` Liu, Ting y Zhou (2008) el 2026-08-16, y después **por la derogación
    del 2026-08-24, que retiró los localizadores del marcador**. Sigue pendiente su uso en `2.3.3`.
  - ~~`[6]` Goodfellow está huérfana~~ **— RESUELTO el 2026-08-16 (`296de24`). T24 la ancló:
    la cita `2.1.4.3`.** (Nació como `[6, cap. 6]`; tras la derogación del 2026-08-24 el marcador va
    a pelo, `[6]`.) El dato se contaba como vivo desde
    el 2026-08-15; **verificar antes de repetirlo** — `Bibliografía.md` la seguía marcando huérfana
    en tres sitios cuando ya no lo era. **Esas tres declaraciones falsas se retiraron del propio
    `Bibliografía.md` en la Tanda 13** (`:63`, `:75`, `:199`), con sus 7 ocurrencias verificadas.
  - **`Bibliografía.md` gana una columna «Localizador por uso»**, que escribe **solo el `researcher`**.
  - **Donde la página no se pueda establecer con honestidad, se MARCA — no se inventa.** Misma
    disciplina que con las 47 citas reconstruidas.
- **Auditar una tanda paralela es auditar la COHERENCIA ENTRE sus notas**, no cada nota por
  separado: dos notas que no chocan en disco sí pueden definir el mismo concepto dos veces o citar
  una cifra de dos maneras. Ese fallo solo se ve mirándolas juntas.
- **No hay máquina de estados**: lo abierto es lo que está en `features.md`; lo hecho es lo que
  tiene commit.
- **Autoría de la redacción** (decisión marco (b) del lote 2026-08-06, aplicada en T0 el
  2026-08-09; sustituye a la regla anterior «la teoría en prosa la escribe Francisco»).
  **Aviso del 2026-08-13:** `leader.md` seguía llevando la prohibición derogada, y como es el
  agente que despacha, ganaba la regla vieja — **esa fue la razón estructural de que las 8 notas
  del capítulo 2 llevaran semanas en guion sin que nadie tuviera permiso de escribirlas**.
  Corregido. No reintroducir la prohibición en ningún fichero:
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
- Se versiona el **texto plano**: código, notas del vault, figuras, reglas y **los CSV citables**
  —`metricas_*.csv`, `dispersion_semillas.csv`, **`comparaciones_pareadas.csv`**,
  `*_vocabulario_onehot.csv` y `*_composicion_d3.csv`—. (`comparaciones_pareadas.csv` lo emite
  `agregar_semillas.py` junto a `dispersion_semillas.csv`/`.md` y faltaba en esta lista hasta el
  2026-08-17, aunque ya estaba versionado: la enumeración se contradecía con sus cuatro hermanos.)
  Quedan fuera (ver `.gitignore`) el venv, los `.joblib`, **los CSV de los splits**, el dataset
  crudo y los `.doc/.docx` — todo reproducible o descargable, y suman 1,1 GB.
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
