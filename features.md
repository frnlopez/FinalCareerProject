# features — tareas del TFG

> **Registro operativo.** Aquí vive lo que está **abierto** ahora mismo y lo que se ha
> **cerrado**, con el commit que lo hace durable. Es lo primero que lee el `leader` en cada
> mensaje.
>
> - `next-steps.md` queda **congelado en cuanto a casillas**: su §1-§5 es historial y su §6 es
>   la especificación técnica de cada script, que sigue vigente como referencia **salvo §6.5
>   (`hibrido.py`), superada por el grill H-1…H-7 de `resumen-de-decisiones.md`** — no calibrar
>   `UMBRAL_CONF` con el método de §6.5. Ya no se marcan tareas allí.
> - `resumen-de-decisiones.md` sigue siendo el registro de **decisiones de diseño**.
> - Lo mantiene el agente `cronista`, disparado por el skill `cierre`. **Estar en Abiertas
>   significa estar abierto**: una tarea aceptada la borra el usuario, nadie más.

Estados: `[ ]` pendiente · `[~]` en curso · `[!]` bloqueado
Fechas absolutas `AAAA-MM-DD`. Track: **Código** / **Informe**.

---

## Abiertas

- [ ] **Auditar la bibliografía** · Informe · `researcher`
  10 entradas en `Bibliografía.md`, todas en uso. Detectado el 2026-08-01: `[9]` duplica `[8]`
  (mismo libro de Stallings) y es una copia alojada en un dominio de terceros; `[2]` (Anderson)
  y `[8]` (Stallings) están sin año ni editorial; `[1]` apoya una cifra de ciberataques en
  prensa sectorial. Completar datos de cita y marcar lo que no llegue a nivel 1-2. **Sin
  borrar nada**: las bajas las decide Francisco.
  → **La continúa T15** del lote 2026-08-06, con las bajas ya autorizadas por Francisco el
  2026-08-06.

- [ ] **`PIPELINE.md` desalineado con su propia figura** · Código · `ml-implementador`
  Detectado el 2026-08-01 al cerrar el diagrama `01_pipeline_completo.mmd`. El árbol de ficheros
  generados de `Implementacion/PIPELINE.md:24-46` no lista `_transformers.joblib`,
  `selected_features.txt` (que sí escribe `program.py:521`) ni la variante de prefijo
  `_sin_seleccion` (122 características). El texto y el `.svg` que él mismo incrusta dicen cosas
  distintas sobre los mismos ficheros. **La acepta o la retira Francisco.**

- [ ] **Diagrama y README de agentes describen la arquitectura anterior** · Código · `ml-implementador`
  Detectado el 2026-08-01. `Implementacion/diagramas/README.md:10` y
  `Implementacion/diagramas/03_orquestacion_agentes.mmd` documentan el ciclo «orquestador →
  implementador → auditor/ejecutor → redactor → cronista → `next-steps.md`», cuando hoy la
  entrada es el `leader` con carriles y tracks (`CLAUDE.md`, «Arquitectura de agentes») y
  `next-steps.md` está congelado: el roadmap vivo es `features.md`. Regenerar `.png` y `.svg` si
  se toca el `.mmd`. **La acepta o la retira Francisco.**

- [ ] **La línea de `4.2` en «lo escribe Francisco» quedó desfasada** · Informe · decide Francisco
  Detectado el 2026-08-01. `features.md:53` reserva a Francisco la prosa teórica de `4.2` completa
  (origen, las 41 características, por qué NSL-KDD), pero la decisión del 2026-07-21
  (`resumen-de-decisiones.md:430-438`) cedió «Origen» y «Las 41 características» a borrador de
  Claude y dejó solo el «por qué NSL-KDD» a revisión de Francisco — y ese borrador **ya existe** en
  `Obsidian_TFG_Vault\04 Implementación del sistema\4.2 Base de datos utilizada.md:8`. Tal como está
  la línea, se puede reescribir desde cero algo ya redactado. **No la toca ningún agente: esa línea
  define lo que escribe Francisco. La acepta o la retira Francisco.**
  → **Queda resuelta por T0** (retirada de la regla «lo escribe Francisco» en las 12 ubicaciones) y
  por **T10** (el contenido de `4.2` pasa a ficha propia del lote 2026-08-06).

- [ ] **Resumen y Abstract** · Informe · `redactor-tfg`
  Se redactan **al final**, cuando el resto de capítulos esté cerrado.
  Notas: `00 Preliminares/Resumen.md` y `00 Preliminares/Abstract.md`.

### Lote 2026-08-06 — los 4 informes del `researcher` convertidos en tareas

> Alta de las 18 fichas T0-T17 acordadas con Francisco en el `grill-me` de 13 preguntas cerrado el
> **2026-08-06**, a partir de los cuatro informes de `Obsidian_TFG_Vault/99 Investigación/`.
> **Criterio rector:** nada que no refine el proyecto o no ayude al lector a ver que con NSL-KDD se
> hizo todo lo posible; las imposibilidades se **declaran con su razón técnica**, no se omiten ni se
> sustituyen por sucedáneos sintéticos. Y el dataset tiene argumento positivo propio (Goldschmidt y
> Chudá: solo el 23 % de los datasets NIDS trae partición train/test predefinida, 16 % desde 2020, y
> su ausencia es «*prone to biased evaluations and selective reporting*»; NSL-KDD sí la trae y este
> TFG la respeta), y ese argumento va **antes** de cualquier límite.
>
> **Decisión marco (a) — se REABRE el track de código**, cerrado el 2026-07-16, de forma
> **declarada** y con el alcance exacto de la spec: Nivel 1 (esquema de métricas, no mueve ningún
> número publicado) + Nivel 2 acotado (10 semillas, los titulares siguen siendo semilla 42) + dos
> mediciones baratas. Todo pasa por `auditor-ml`. Nada más.
>
> **Decisión marco (b) — se retira la regla «lo escribe Francisco», en dos velocidades:** `2.x`
> retirada completa (`redactor-tfg` redacta la prosa desde los guiones existentes); `6.2` pasa a
> **borrador de agente con revisión final de Francisco** (es el sitio natural del material de NL, y
> bloqueada dejaba a medias un entregable del encargo); **la bibliografía final en Zotero/IEEE sigue
> siendo de Francisco** (trabajo mecánico en su máquina).

- [ ] **T0 · Retirar la regla «lo escribe Francisco» en sus 12 ubicaciones** · — · hilo principal
  Es andamiaje, así que lo hace el hilo principal (excepción única al enrutado de `CLAUDE.md`).
  Aplicar las dos velocidades de la decisión marco (b). Ubicaciones (12): `CLAUDE.md` («Reglas duras
  del andamiaje»), `features.md:57-65`, `.claude/agents/redactor-tfg.md`, y el callout «Redacción a
  cargo de Francisco» en 9 notas: `2.1.6`, `2.2.1`, `2.2.2`, `2.2.3`, `2.2.4`, `2.2.5`, `2.3.1`,
  `2.3.2`, `2.3.3`.

- [~] **T1 · Nivel 1: esquema de métricas** · Código · `ml-implementador` → `auditor-ml`
  > **Estado 2026-08-06: CÓDIGO IMPLEMENTADO Y APTO**, tres pasadas de `auditor-ml`
  > (APTO CON CAMBIOS 12 puntos → corrección → APTO CON CAMBIOS 5 puntos → corrección → APTO).
  > Verificado en las tres: sin fuga, semilla 42 intacta, calibración OOF de `hibrido.py` sin tocar,
  > CSV publicados sin editar a mano. Ficheros tocados:
  > `Implementacion\app\{config,evaluacion,anomalias,firmas,baseline,hibrido}.py`,
  > `Implementacion\PIPELINE.md`, `.gitignore` raíz. **NO COMMITEADO.**
  >
  > **Falta para cerrarla:** regenerar las 8 tablas de `Resultados\`, que siguen con el esquema
  > anterior. Runbook de 8 invocaciones escrito en `PIPELINE.md` (4 scripts × 2 variantes, `hibrido`
  > al final, ≈16 min). Los CSV viejos se apartan como `.esquema-anterior.bak`, no se borran.
  > **Correrlo entero de una vez:** el estado intermedio es committeable y dejaría tablas a medias.
  >
  > **Decisiones de diseño tomadas dentro de T1 → van a T17:** (1) el problema de la columna homónima
  > era **más amplio** que el `accuracy_D2` de la ficha — `f1_macro_cv` 0,9094 convivía con
  > `f1_macro` 0,4721 (**44 pp**) y `auc_val` 0,9918 con `roc_auc` 0,9229, todas leídas igual;
  > corregido. (2) `alcance` es campo único más convención de prefijos/sufijos, con
  > `ALCANCE_SELECCION`, `ALCANCE_HIBRIDO_CONOCIDA`, `ALCANCE_HIBRIDO_CALIBRACION`,
  > `ALCANCE_OOF_D3`, `ALCANCE_D2_REPORTE`. (3) Las **cuatro tablas auxiliares** también llevan
  > procedencia (la ficha no lo pedía). (4) `commit` = hash corto con tres valores posibles
  > (`-sucio` acotado a `git status --porcelain -- Implementacion`, y `-suciedad_desconocida`);
  > `5.0`/`A.3` van a citar esa columna. (5) En el híbrido, `tiempo_entrenamiento_s` = calibración OOF
  > sobre D3, **cero ajuste de la cascada** — frase para `5.0`/`A.3` en la ficha del `redactor-tfg`.
  > (6) `metricas_hibrido.csv` gana `algoritmo` (`"<detector>-><firma>"`); ninguna de las 5 citas del
  > vault se rompe. (7) `baseline.py` añade `bin_tn/bin_fp/bin_fn/bin_tp`.
  >
  > **Aviso para quien implemente T4:** no puede escribir en las cuatro tablas principales — choca
  > contra el borrado por variante, la `CLAVE_UNICIDAD` sin `semilla` y el recuento fijo 4/4/1/1. Es
  > coherente con la ficha (la dispersión va a tabla nueva en `A.3`) y ya está escrito en
  > `PIPELINE.md` y en el docstring de `comprobar_recuento()`.

  **Ningún resultado publicado cambia (semilla 42): solo cambia el esquema de columnas.**
  - `bin_accuracy` en la fila de `metricas_baseline.csv`. Hoy falta y **es la cifra que la literatura
    usa para comparar** (0,8605 del híbrido frente a los baselines canónicos de Tavallaee et al.).
  - **Campo `alcance` por fila** en las cuatro tablas. Motivo verificado en disco y **peor de lo que
    decía el informe**: `accuracy_D2` existe con el mismo nombre en `metricas_firmas.csv` (0,9683,
    4 clases sobre conocidos de D2) y en `metricas_baseline.csv` (0,7395, 5 clases sobre D2 entero).
    Columna homónima, dos alcances. Cierra C3 y C6.
  - Columnas `semilla` y `commit` (procedencia por fila; hoy la semilla vive en `config.py` y no
    viaja con el dato).
  - **Conjunto mínimo obligatorio de columnas** común a las cuatro tablas, declarado.
  - `_limpiar_variante_csv` (hoy repetido 4 veces) sube a `evaluacion.py` con la **clave de unicidad
    declarada** (variante × algoritmo × alcance).
  - **Separar el tiempo de inferencia** del de entrenamiento y reportar **latencia por flujo y
    flujos/segundo**. Es la mitad viable de P9 (*Lab-Only Evaluation*).

- [ ] **T2 · KS de D1 contra los normales de D2** · Código · `ml-implementador` → `auditor-ml`
  `validacion.py:394-431` ya calcula KS D1→D2 y reporta **37 de 54 características con drift** (top:
  `src_bytes` 0,346, `dst_bytes` 0,317). **Ese 37 no sirve para explicar el FPR**: compara D1 (todo
  normal) con D2 completo (43 % normal + 57 % ataques), así que buena parte del drift es la presencia
  de ataques. Añadir el KS de D1 contra **las 9.711 filas normales de D2**, separado del actual y
  **sin sustituirlo**.

- [ ] **T3 · Medición de la cascada invertida** · Código · `ml-implementador` → `auditor-ml`
  Cargar `firma_RandomForest_54.joblib` (y el de 122), pasarle las **9.711 filas normales de D2** y
  contar cuántas recibirían etiqueta de ataque con confianza sobre `UMBRAL_CONF`. Convierte en número
  la afirmación hoy no medida de `3.2.2` («si las firmas fueran primero, condenarían tráfico legítimo
  en masa»).
  **Marca para el `auditor-ml`: solo hay inferencia sobre modelos ya persistidos, y D2 solo se
  reporta — no ajusta ni calibra nada. No toca la línea roja H-4/P-4.**

- [ ] **T4 · Nivel 2: 10 semillas** · Código · `ml-implementador` → `auditor-ml` → `ejecutor-experimentos`
  10 semillas × 4 scripts × 2 sets de características, **≈160 min de cómputo desatendido** (un pase
  completo son ≈16 min: anomalías 90 s + 280 s, firmas 177 s + 307 s, baseline 25 s + 34 s, híbrido
  27 s + 16 s).
  - **Los titulares de 5.1-5.3 siguen siendo los de la semilla 42.** La dispersión (media, sd, mín,
    máx) entra como tabla nueva en `A.3` más un párrafo en `5.4`. **No se reescribe el capítulo.**
  - Cierra los ítems FT *number of runs*, *error bars* y *central tendency* de Pineau et al.
  - **Sin p-valor, con la renuncia declarada y su razón: 10 puntos sobre un único dataset no
    sostienen un contraste.** Declarar la renuncia **cumple** el ítem *statistics*; callarla no.
  - **Objetivo real:** dos decisiones cerradas descansan en huecos de 1-2 pp medidos con n=1 —
    RandomForest 0,822 vs HistGradientBoosting 0,804 (firmas) y Autoencoder 0,8605 vs
    IsolationForest 0,8257 (anomalías). Si los intervalos se solapan, **decirlo y no establecer el
    orden**. Eso es un hallazgo para `5.4`, no un desastre.

- [ ] **T5 · `5.0 Protocolo de evaluación`** · Informe · `redactor-tfg`
  Nota nueva, antes de `5.1`. Recoge junto lo que hoy está disperso en Q4, Q6, H-1…H-7 y P-1…P-5 de
  `resumen-de-decisiones.md` (documento interno que no va a la memoria) y le pone cita de nivel 1:
  particiones y su función, lo congelado entre variantes, métricas obligatorias, prohibiciones
  explícitas, y el vocabulario de Pineau et al. (*reproducible* / *replicable* / *robust* /
  *generalisable*) usado con precisión.
  - **Los C1-C7 aparecen aquí reflexivamente**, con la frase que les da sentido: *el mismo filtro que
    se exige a las cifras ajenas hay que pasarlo uno mismo*. Y **se cuenta el arreglo**: C3 y C6 no
    se cumplían, el caso concreto de la columna homónima, y qué hubo que cambiar. Contar la
    corrección —y no solo exhibir siete verdes— es lo que separa la autocrítica de la
    autocomplacencia.
  - Auditoría C1-C7 verificada contra disco: **C1** D2 = 22.544 exactas · **C2** D1/D3 declarados ·
    **C3** fallaba, lo arregla T1 · **C4** `bin_fpr` en las 4 tablas (P-2) · **C5 cumple, verificado
    línea a línea**: one-hot alineado sobre la unión D1+D3 descartando categorías exclusivas de D2
    (`program.py:292-298`), escalador ajustado solo sobre D1+D3 (`:316`), `LabelEncoder` sobre el
    diccionario estático `attack_mapping` (`:321-328`), RF de selección solo con train (`:500`) ·
    **C6** fallaba, lo arregla T1 · **C7** los 17 tipos nativos.

- [ ] **T6 · Apartado «Límites de lo medible con NSL-KDD» dentro de `6.1`** · Informe · `redactor-tfg`
  En el **cuerpo, no en apéndice**: los apéndices no se leen y el argumento solo funciona si se ve.
  Cada límite con su razón técnica, su cita, y **lo que sí se hizo en su lugar**. Inventario:
  - Sin marca de tiempo → no hay deriva temporal ni aprendizaje continuo (ver T12).
  - Sin despliegue real → **P9** de Arp et al., cubierto en sus dos mitades viables (T1 y T11).
  - Sin adversario adaptativo → **P10**, cubierto por escrito (T9).
  - Una sola semilla → resuelto por T4; lo que quede, declarado.
  - Umbralizar un clasificador cerrado no acota el riesgo de espacio abierto → Scheirer et al.
    explica el 13,4 % (T11).
  - Los 0-day de NSL-KDD son ataques ausentes del train, **no amenazas actuales** → Khraisat et al.
    2019 («los datasets KDD/DARPA ya no representan los *zero-day* contemporáneos»).
  - **Resultado a escribir:** de los diez pitfalls de Arp et al., ocho cubiertos y dos cubiertos
    hasta donde el dataset permite, con la razón técnica escrita. No «P9 y P10 no aplican a un TFG».

- [ ] **T7 · `A.3 Ficha del sistema`** · Informe · `redactor-tfg`
  Apéndice nuevo, plantilla de *model card* de Mitchell et al. 2019. Volcado seco: particiones,
  semilla, configuraciones ganadoras, alcance de cada métrica, tabla de dispersión de T4, e
  **infraestructura de cómputo**: i7-12700H, 34 GB RAM, Windows 11 Pro 10.0.26200, Python 3.11,
  21 dependencias fijadas (`scikit-learn==1.7.1`).
  - **Checklist de Pineau: los 11 ítems FT, NO los 17.** Los otros seis van de liberación de código y
    presupuesto de cómputo y no aplican; rellenarlos es paja que diluye los que importan. Decir
    explícitamente que son el subconjunto FT del checklist de 17.

- [ ] **T8 · Cita en el punto de la decisión — capítulo 2** · Informe · `redactor-tfg`
  - `2.2.3`/`2.2.4`: **los 4 sentidos de «híbrido»** y cuál usa el TFG. En la literatura NSL-KDD
    «híbrido» designa con la misma frecuencia (a) anomalías + firmas —el de este TFG—, (b) selección
    de características + clasificador, (c) *clustering* + clasificador, (d) dos clasificadores
    supervisados en *ensemble*. Sin acotarlo aquí, toda comparación posterior es ruido. Añadir que la
    revisión más citada (Khraisat et al. 2019) **no taxonomiza lo híbrido**: lo despacha en un
    párrafo y con un ejemplo que combina dos supervisados. Más los 5 patrones y el linaje ADAM 2001 /
    Tombini 2004.
  - `2.1.5`/`2.1.6`: P7/P8 de Arp et al.; Chow 1970 (regla de rechazo óptima **sobre las posteriores
    verdaderas**, y `predict_proba` de un RF no lo es); vocabulario de Pineau.
  - `2.3.3`: P9 y P10, y el marco del modelo de amenaza.

- [ ] **T9 · Cita en el punto de la decisión — capítulo 3** · Informe · `redactor-tfg`
  - `3.1`: **modelo de amenaza explícito** = aplicar P10. Atacante no adaptativo, sin conocimiento
    del modelo, que no intenta evadirlo; opera sobre flujos ya extraídos, no sobre paquetes; sin
    envenenamiento del entrenamiento. **Y la razón citada de por qué no hay experimento adversario:**
    muchas características de NSL-KDD son derivadas y agregadas (`count`, `srv_count`, tráfico-host,
    contenido); perturbarlas libremente produce vectores que ningún atacante real puede generar —un
    ataque en espacio de características sin correspondencia en el espacio del problema, que es otro
    de los errores que Arp et al. documentan. **Intentar P10 a fondo con este dataset incumpliría
    otro pitfall del mismo artículo.** Eso es un resultado, no una excusa.
  - `3.2.2`: por qué anomalías primero. Tres patas: diseño (la etapa 2 no conoce `normal`), cobertura
    (Tombini et al. 2004), y el *semantic gap* de Sommer y Paxson 2010 —la etapa 2 no existe para
    detectar sino para **traducir** «esto es anómalo» en «esto es un `dos`»—. Más **Kim et al. 2014
    como antagonista directo** (mismo dataset, orden inverso) y el precio declarado: FPR 0,102 frente
    al 0,027 del baseline monolítico. Más **el número de T3**.
  - `3.2`/`3.6`: la divergencia declarada. En ADAM la etapa 2 etiqueta «falsa alarma» y **la filtra**;
    aquí se le prohíbe por diseño (H-5, P-5). Matiz: H-5 es correcta *dentro* de su premisa, pero su
    redacción actual puede leerse como si **toda** cascada anomalía→firmas tuviera esa propiedad, y
    no es así: la tienen las cascadas cuya etapa 2 carece de clase `normal`, que es una **elección**.
  - `3.3`: Mitchell et al. (el recall 0-day por tipo **es** evaluación desagregada, con nombre y
    precedente) + Scheirer et al. (`unknown` es formalmente *open-set recognition*, lo que justifica
    reportar la tasa de enrutado como métrica propia con su alcance — decisión H-6).
  - `3.4`: Sommer y Paxson, verbatim: entrenar solo con normal es obligado para aspirar a lo novedoso,
    y **cuesta** —«exige tener un modelo *perfecto* de normalidad»—. Es la explicación teórica del
    FPR del 8-10 %: no es un defecto del autoencoder.
  - `3.5`: **por qué RandomForest y no una arquitectura profunda.** Los 5 criterios de McElfresh et
    al. cruzados con los números de D3 (58.630 filas, razón 1.086 muestras/característica,
    distribuciones con colas larguísimas, 60 de 122 características descartadas por importancia)
    apuntan todos al cuadrante de los árboles; más Grinsztajn et al. y Shwartz-Ziv y Armon. La
    familia tabular profunda se nombra **una vez y en positivo** (TabNet, FT-Transformer, TabPFN),
    nunca como «lo descartamos», que invita a «¿y por qué no lo probaste?». Dos apoyos duros: el
    contraste interno (HistGradientBoosting 0,804 frente a RandomForest 0,822, y tarda más: 68,7 s
    frente a 54,8 s — si el GBDT de la propia sklearn no despega, el argumento se sostiene solo) y
    **TabPFN v2 de *Nature* admite 10.000 muestras y D3 tiene 58.630**. Usar la formulación C.1 del
    informe tabular.

- [ ] **T10 · Capítulo 4** · Informe · `redactor-tfg`
  - `4.2`: definición correcta de las tres particiones (KDDTrain+ 125.973 · KDDTest+ 22.544 ·
    KDDTest-21 11.850) y **vacuna contra el error que circula por la literatura**: KDDTest-21 **no**
    es «el subconjunto con 21 tipos de ataque», es el de dificultad alta —`#successfulPrediction` ∈
    [0,21] sobre **21 máquinas aprendidas (7 algoritmos × 3 entrenamientos)**, excluyendo los
    registros que todas acertaron—. Comprobado que ese error **no está hoy en ningún fichero del
    repo**: se vacuna, no se corrige. Escribir que **D2 es KDDTest+ completo**, requisito de entrada a
    toda comparación externa. Y el matiz de los baselines canónicos: se entrenaron con **el primer
    20 % de KDDTrain+**.
  - `4.2` · **el 17**: unificar «~17» → «17» (aparece con virgulilla en `EL_FUTURO.md:20`,
    `resumen-de-decisiones.md:65,143`, `baseline.py:12`, `firmas.py:157`, `Guia_ML` ×3,
    `next-steps.md` ×3, `2.1.6:55`) y añadir la nota de procedencia: **17 contados sobre
    `metricas_hibrido_0day.csv`; la cifra 14 de Tavallaee et al. se refiere a KDD'99, no a
    NSL-KDD**. El 17 se justifica **por medición en disco, nunca por cita**.
  - `4.2` · **por qué NSL-KDD**, con Goldschmidt y Chudá (el argumento positivo del criterio rector).
  - `4.3`: C5 sin fuga con las cuatro líneas verificadas (Kapoor y Narayanan; P3/P5 de Arp et al.) y
    el peso del one-hot: **84 de 122 características (69 %) vienen de la codificación**, 70 de ellas
    de `service` sola; de las 60 eliminadas por importancia, **58 son *dummies*** → la selección de
    4.3.5 es en la práctica un mecanismo de poda del one-hot de `service`.

- [ ] **T11 · Capítulo 5** · Informe · `redactor-tfg`
  - `5.2`: dispersión de T4 y, si los intervalos RF/HGB se solapan, decir que el orden no queda
    establecido.
  - `5.3`: **el 13,4 % de enrutado a `unknown` explicado, no disculpado.** Scheirer et al.
    (umbralizar un clasificador de conjunto cerrado no acota el riesgo de espacio abierto), Bendale y
    Boult (OpenMax supera explícitamente al umbralizado de la salida probabilística, que es el
    mecanismo de `UMBRAL_CONF`), Chow (la regla de rechazo es óptima sobre las posteriores
    verdaderas). Pasa de «esto nos ha salido regular» a «esto es lo que la teoría predice y lo hemos
    cuantificado».
  - `5.4` · **comparación externa reducida, cuatro párrafos y ninguna tabla grande de *accuracies***:
    (1) los criterios C1-C7; (2) la tabla pequeña de supervivientes —los 7 baselines canónicos de
    Tavallaee et al. frente al `bin_accuracy` 0,8605 del híbrido, que está **por encima del mejor**
    (NBTree 82,02 %), en la misma partición y la misma tarea— **con sus dos reservas declaradas**: la
    granularidad de etiqueta de los canónicos no está declarada en el artículo (ni la referencia
    canónica cumple C3 limpiamente) y su presupuesto de datos fue el 20 % de KDDTrain+; (3) el
    descarte y su magnitud, **apoyado en el dato citable de Goldschmidt y Chudá** (NSL-KDD aparece
    3 veces en la investigación NIDS de primer nivel 2020-2023), **no** en el ≈87 % del conteo
    propio, que es una muestra acotada de búsqueda web y así debe declararse; (4) el hueco: no se ha
    encontrado trabajo verificable que reporte recall por tipo sobre los 17 tipos ausentes con FPR
    declarado — formulado como «no lo he encontrado en la literatura revisada», no como «nadie lo
    hace».
  - `5.4` · **Hindy et al. 2020 se cita por el método, no por el número.** Su 89-99 % incumple C7 (su
    «0-day» es toda clase de ataque; agrupan ataques de KDDTrain+ y KDDTest+; barren umbral sin fijar
    punto de operación, FPR ≈15-21 % frente al 0,1017 de este proyecto). Lo comparable y valioso es
    la forma: precedente de nivel 1 de que el desglose por clase es la manera correcta de reportar un
    detector de 0-day, y de que un AE supera a un OCSVM en esa tarea — que es lo que mide
    `metricas_anomalias.csv` (AE `roc_auc` 0,9288 vs OCSVM 0,8360 en 54).
  - `5.4` · **proyección a prevalencia realista** (mitad viable de P9, cero código): D2 tiene 43 % de
    tráfico normal y el tráfico real ronda el 99 %; con `bin_recall` 0,8318 y `bin_fpr` 0,1017 se
    proyecta la precisión a prevalencia realista. El resultado va a ser incómodo, **y ese es el
    punto**: enseña que un FPR del 10 % es un problema operativo, no un decimal. Es NIST SP 800-94 y
    la falacia de la tasa base de Axelsson (ya en el guion de `2.2.4`).
  - `5.1` o `5.4` · **el desplazamiento D1→D2 medido y atribuido** con el KS de T2. Nombrarlo con
    precisión: **desplazamiento entre particiones, no deriva temporal** — sin esa precisión la
    afirmación se cae en cuanto alguien pregunte por la marca de tiempo. El umbral p95 promete ≈5 %
    de FPR y el real es 8-10 %; el exceso tiene explicación medible **sin necesidad de reloj**.

- [ ] **T12 · `6.2 Líneas futuras`, borrador desde `EL_FUTURO.md`** · Informe · `redactor-tfg`
  El aprendizaje continuo aparece **fusionado en tres peldaños encadenados**, nunca como línea
  independiente: (1) migrar a un dataset con reloj —CIC-IDS2017 tiene marca de tiempo verificada,
  cinco días laborables consecutivos—; (2) análisis de deriva temporal con protocolo TESSERACT;
  (3) representación de secuencia (sesión o *host* como secuencia de flujos), que conecta con algo ya
  demostrado con datos propios: `snmpgetattack` (n=178) lo fallan los cuatro detectores en ambos sets
  porque apenas perturba las características **por flujo**. NL solo se menciona en el peldaño 3, como
  lo que lo volvería aplicable en sentido literal.
  - **Prohibición de redacción 1:** no llamar «Nested Learning» a un bucle de `partial_fit` — es
    aprendizaje incremental clásico, anterior a NL en décadas, y la parte de NL que quedaría fuera es
    precisamente la que lo hace NL.
  - **Prohibición de redacción 2:** no presentar un troceo de D1 o D3 como análisis de deriva —
    sería un artefacto: la partición la elegiría el experimentador.
  - Formulación de respaldo para el veredicto de NL: la del §E del informe de NL, **íntegra**.

- [ ] **T13 · `EL_FUTURO.md` — tres entradas nuevas y una anotación** · Informe · `redactor-tfg`
  - **★ Vector de error de reconstrucción por característica como entrada extra de la etapa 2.** La
    única idea del lote que **podría ayudar al recall 0-day conservando reglas legibles** (cada
    componente lleva el nombre de una característica real: `if err_num_shells alto → u2r` sigue
    siendo una firma). Cero dependencias nuevas. No estaba en `EL_FUTURO.md`.
  - **Aviso de TabArena sobre sobreajuste al conjunto de validación en los *ensembles***, pegado a la
    línea nº 1 (ensemble de detectores de la etapa 1): si los miembros se eligen mirando `D1_val` o
    los pliegues OOF de D3, la ganancia no se reproduce en D2. Protege la línea, no la debilita.
  - **El bucle de generación automática de firmas de Hwang et al. 2007** como respuesta publicada a
    «¿y qué hago con un `unknown`?» — hoy el TFG termina en la etiqueta.
  - **Anotación (no reapertura):** el *target encoding* es estructuralmente incompatible con la
    opción A, porque la etapa 1 no tiene destino sobre el que ajustarlo (D1 es una sola clase). No
    desmiente Q1/C —se tomó sobre one-hot y sigue siendo correcta— pero es **una razón nueva a favor
    de la opción B**.

- [ ] **T14 · Cerrar las verificaciones pendientes** · — · `researcher`
  Francisco **no tiene acceso institucional**.
  - `Yin et al. 2017` y `Khraisat et al. 2020`: se citan **sin cifra** (metadatos verificados).
  - `Kim et al. 2014`: se cita **por su resumen**, y `3.2.2` declara que la comparabilidad exacta de
    su métrica de desconocidos no se ha podido verificar.
  - Las otras cinco (Arp Fig. 1, Shyaa et al. texto completo, MDPI *Algorithms* 18(12):749, columnas
    de tiempo de UNSW-NB15, la CV de Shone et al.) se **cierran por escrito** como «no verificable
    sin acceso institucional; no sostiene ninguna afirmación del trabajo». Cerrarlas explícitamente
    vale más que dejarlas como deuda flotante.

- [ ] **T15 · B1: cerrar la auditoría de `Bibliografía.md`** · — · `researcher`
  Tarea abierta desde el 2026-08-01 (ver la ficha «Auditar la bibliografía» más arriba, que esta
  continúa). Completar `[2]` (Anderson) y `[8]` (Stallings) con año y editorial; **fundir `[9]` en
  `[8]`** (copia del mismo libro en dominio de terceros) y retirarla de la numeración;
  **sustituir `[1]`** (prensa sectorial sosteniendo una cifra de ciberataques) por fuente de nivel
  1-2: ENISA *Threat Landscape*, INCIBE o CCN-CERT, todas públicas y sin muro. **Bajas autorizadas
  por Francisco el 2026-08-06.** Cambio de formato: `Bibliografía.md` pasa a **tabla de staging** con
  cita completa, DOI y **nivel de fiabilidad por entrada** — el pase final en Zotero/IEEE se vuelve
  mecánico y el nivel a la vista impide colar sin darse cuenta una fuente de nivel 2-3 sosteniendo
  una afirmación fuerte.

- [ ] **T16 · B2: volcado de fuentes, DESPUÉS de la redacción** · — · `researcher`
  **Va después de la redacción (T8-T13): no se arranca antes.** Regla dura: **ninguna entrada sin
  cita en el texto.** Los cuatro informes aportan ≈40 fuentes con datos completos y nivel asignado;
  se filtran por el mapa de T8-T12. Estimación: entran 25-30. Volcar ahora produciría una
  bibliografía inflada con entradas que no aparecen citadas en ningún sitio — lo contrario del rigor
  que busca todo este lote.

- [ ] **T17 · Volcar las decisiones del grill a `resumen-de-decisiones.md`** · — · `cronista` + `redactor-tfg`
  Volcar **todas** las decisiones de este grill, incluida la **reapertura declarada del track de
  código** (con su motivo) y la **retirada de la regla de autoría** en dos velocidades. Y anotar en
  **cada uno de los cuatro informes** de `Obsidian_TFG_Vault/99 Investigación/` un bloque «Decisiones
  tomadas a partir de este informe» que diga **qué se convirtió en decisión y qué se descartó**, para
  no tener que reconstruirlo dentro de tres meses. Acompaña cada cierre del lote.
  **Añadido el 2026-08-06 tras T1 — deriva de documentación detectada y NO corregida:** el contrato
  de `evaluacion.py` cambió con T1 y siguen describiendo la forma anterior `CLAUDE.md:63`,
  `next-steps.md:621`, `resumen-de-decisiones.md:319,343` y `Guia_ML\03_validacion_y_metricas.md:153`.
  Ponerlos al día es parte de T17.

- [ ] **PDF sin acceso institucional — reabrir si Francisco consigue acceso** · — · `researcher`
  Ficha de guardia abierta el 2026-08-06 junto a T14. Criterio de cierre aplicado hoy a las cinco
  últimas: **«no verificable sin acceso institucional; no sostiene ninguna afirmación del trabajo».**
  Las siete verificaciones:
  - Citadas **degradadas** (3): `Yin et al. 2017` y `Khraisat et al. 2020` → **sin cifra** (metadatos
    verificados); `Kim et al. 2014` → **por su resumen**, con `3.2.2` declarando que la
    comparabilidad exacta de su métrica de desconocidos no se ha podido verificar.
  - **Cerradas por escrito** (5): Arp Fig. 1 · Shyaa et al. texto completo · MDPI *Algorithms*
    18(12):749 · columnas de tiempo de UNSW-NB15 · la CV de Shone et al.

### Descartado — no reabrir

> Descartes **cerrados en el `grill-me` del 2026-08-06**. No son tareas pendientes ni pospuestas:
> están decididos. **Reabrir cualquiera de ellos exige decisión expresa de Francisco.**

| Descartado | Razón |
|---|---|
| **E-INC** (autoencoder incremental por ráfagas) | Viable, pero responde a una pregunta de despliegue, no a la del TFG. Complejidad innecesaria |
| **Cascada invertida completa** | No se puede invertir esta cascada, solo construir otro sistema: la etapa 2 no tiene clase `normal` (`firmas.py:5`, `153-154`). Exigiría reentrenar a 5 clases y mover 4.5, 5.2 y la comparabilidad de H1. Y Kim et al. tampoco solo invierte el orden. Sustituido por la medición T3 |
| **Experimento adversario** para P10 | Incumpliría otro pitfall del propio Arp et al. (espacio de características sin correspondencia en el espacio del problema). Sustituido por el modelo de amenaza escrito |
| **Sustituir las 54 características por el latente de 32 del AE** | El latente está entrenado solo con D1 para reconstruir lo que **no** es ataque; `root_shell`, `num_shells`, `su_attempted` son ≈0 en D1 por construcción, así que el cuello de botella no tiene incentivo para reservarles dirección — y `u2r` ya es el eslabón débil (f1 0,452, 37 muestras). Además destruye las reglas legibles y `MLPRegressor` no expone `transform()` |
| **Stacking como solución al `unknown`** | No puede aprender la clase que importa: de `unknown` no hay ni un ejemplo en el entrenamiento (D3 son solo ataques conocidos). Es un problema de conjunto abierto y el stacking supervisado no es la herramienta. Rebajar la expectativa de `EL_FUTURO.md:66-68` |
| **TabNet / FT-Transformer / SAINT / NODE / TabM / TabPFN** | PyTorch, ruptura de la persistencia `.joblib` y del protocolo homogéneo, sin respaldo para este régimen. TabPFN v2 ni admite D3 (58.630 > 10.000) |
| **Aprendizaje semisupervisado** | La premisa no existe: no hay datos sin etiquetar. Cada fila de NSL-KDD trae `attack` y `level` |
| **p-valor sobre las 10 semillas** | 10 puntos sobre un único dataset. Se declara la renuncia con su razón |
| **Tabla grande de *accuracies* de la literatura en `5.4`** | Con 87 % de descarte en la muestra y NSL-KDD casi ausente de los venues de primer nivel, sería una colección de cifras indefendibles una por una. El descarte **es** el hallazgo |
| **Nota propia para «híbrido», cascada invertida o TabNet** | Son párrafos dentro de notas que ya existen. Sacarlos a nota propia es la complejidad que el criterio rector prohíbe |

### Secuencia del lote 2026-08-06

`T0` → `T1`-`T4` (código, cada uno con `auditor-ml`; `T4` lo corre `ejecutor-experimentos`) →
`T2`/`T3` alimentan `T9`/`T11` → `T5`-`T13` (redacción) → `T15` en paralelo desde el principio →
`T16` al final → `T17` acompaña cada cierre.

> **En este ciclo solo se arrancan `T0` y `T1`.** El resto queda dado de alta y en espera. En
> particular **`T4` espera a que `T1` esté auditado**, porque corre sobre el esquema nuevo de CSV.

> **T0 va a reescribir la sección de abajo** (retirada de la regla «lo escribe Francisco» en dos
> velocidades). Hasta que T0 se cierre, la sección sigue vigente tal como está.

### Fuera de la lista operativa — lo escribe Francisco

No se despachan a ningún agente. El `leader` no debe crear tareas para esto.

- Teoría en prosa de `02 Marco Teórico` (2.1.6, bloque 2.2 Ciberseguridad, bloque 2.3 IA).
  Los guiones de temas ya están propuestos en las 9 notas (2026-07-15).
- Prosa teórica de `4.2` (origen del dataset NSL-KDD, las 41 características, por qué NSL-KDD).
- `6.2 Líneas futuras` — material de respaldo en `EL_FUTURO.md`.
- Bibliografía final con Zotero en formato IEEE.

---

## Cerradas

| Fecha | Track | Tarea | Commit |
|---|---|---|---|
| 2026-08-01 | Código | Fin del «roadmap vivo»: `next-steps.md` ya no se anuncia como tal en ningún fichero. La frase de reparto sale del callout «Estado a 2026-07-16» de `CLAUDE.md:115-117` a párrafo propio fechado el 2026-08-01 (datar el congelado tres semanas antes era falso), mismo arreglo en `resumen-de-decisiones.md:4` + inciso de fecha sobre la casilla del 2026-07-21 (`:440-443`, registro original íntegro) + entrada de bitácora nueva (`:533-542`), y «Roadmap» → congelado en `README.md:26-28` y `Guia_ML\README.md:7-9`. El auditor corrige además el fondo: «§6 vigente como especificación técnica» era falso sin matiz — `next-steps.md:591-597` declara §6.5 (`hibrido.py`) superada por el grill H-1…H-7, y sin la salvedad un implementador podía calibrar `UMBRAL_CONF` con el método viejo y saltarse una decisión anti-leakage cerrada; la salvedad va en los cuatro ficheros. Dos pasadas de `auditor-ml` (la primera APTO CON CAMBIOS, 4 puntos aplicados), árbol ASCII de `README.md` intacto | `b5aec20` |
| 2026-08-01 | Código | Diagrama `01_pipeline_completo.mmd` al día: 15 correcciones verificadas contra `fichero:línea` — capa de modelos ya no es «no implementado», «51 ataques» → 40 etiquetas, la alineación one-hot es la **unión D1+D3** (y no «schema de D1», que documentaba el bug cerrado el 2026-07-05), alta del paso `select_features()` 122→54 y de las 4 aristas del protocolo anti-leakage (calibración OOF de `UMBRAL_CONF` con D3, D2 no ajusta nada). `.png` y `.svg` regenerados con `mermaid-cli` 11.16.0 `-s 3`; segunda auditoría sin rojos ni naranjas. Incluye `diagramas/README.md` y, en `CLAUDE.md`, la atribución del balanceo 4.3.4 a `firmas.py` (por algoritmo), no a `program.py` | `d88dada` |
| 2026-08-01 | Código | `CLAUDE.md` al día tras la absorción de `Implementacion/`: tabla de scripts de 2 a 8 (6 clases reales + `config.py` y `evaluacion.py` como módulos-librería), orden de ejecución y dependencias entre scripts, y en `## Git` que `Implementacion/` ya no lleva `.git` propio y la precedencia de su `.gitignore` anidado | `e3548ca` |
| 2026-08-01 | Código | Absorción del repo git anidado `Implementacion/`: retirado el gitlink huérfano y versionados los 22 ficheros de código (8 scripts de `app/`, 10 diagramas, `requirements.txt`, `PIPELINE.md`, `readme.md`, `.gitignore`) | `fb920b8` |
| 2026-08-01 | — | Arquitectura de agentes: `leader`, `researcher`, hook de entrada, skill `cierre`, `features.md`, git y README | `791a698` |
| 2026-07-16 | Informe | Apéndice A.2 — fórmulas de las métricas (borrador) | — |
| 2026-07-16 | Informe | 4.1 Tecnologías utilizadas (borrador) | — |
| 2026-07-16 | Informe | 6.1 Conclusiones (borrador) | — |
| 2026-07-16 | Informe | Apéndice A.1 + 4.2.1 — columnas del dataset, EDA y validación (borrador) | — |
| 2026-07-16 | Informe | Cap. 3 Diseño completo, 3.1–3.6 (borrador) | — |
| 2026-07-16 | Informe | Volcado de resultados a caps. 4 y 5 — dos auditorías adversarias, ambas aplicadas | — |
| 2026-07-16 | Código | Experimento H1: cierra Q1/C → **54 características (opción A)** | — |
| 2026-07-15 | Informe | Reestructuración del vault: 43 notas, MOC renumerado, 0 wikilinks rotos | — |
| ≤2026-07-16 | Código | `program.py` · `validacion.py` · `anomalias.py` · `firmas.py` · `baseline.py` · `hibrido.py` — implementados, auditados y ejecutados en 54 y 122 características | — |

> Las tareas anteriores al 2026-08-01 se cerraron sin git: el repositorio se creó ese día. El
> detalle de cada una está en la bitácora de `next-steps.md §5`.
