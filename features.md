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
  - **Aviso heredado de T1 (cerrada el 2026-08-08):** T4 **no puede escribir en las cuatro tablas
    principales** — choca contra el borrado por variante, la `CLAVE_UNICIDAD` sin `semilla` y el
    recuento fijo 4/4/1/1. Es coherente con esta ficha (la dispersión va a tabla nueva en `A.3`) y ya
    está escrito en `PIPELINE.md` y en el docstring de `comprobar_recuento()`.
  - **Dato de T1 para dimensionar la corrida:** el wall-clock dispersa hasta **4,8× entre corridas en
    máquina no dedicada** con calidad idéntica al bit (Autoencoder-54: 37,71 → 181,91 s). La
    estimación de ≈160 min es orientativa, y las columnas de tiempo de las 10 semillas **no** se
    pueden leer como propiedad del algoritmo sin declarar esa dispersión.
    → **Salvedad del 2026-08-09 (cierre de T22):** ese 4,8× debe leerse **«con el recuento de épocas
    idéntico»**. `n_iter_total_grid` quedó registrado y resultó **determinista** (162 a 54 · 128 a
    122), así que la dispersión es **carga de máquina, no épocas**. Consecuencia práctica para quien
    arranque T4: **no diseñar las 10 semillas para resolver la duda del número de épocas — ya está
    resuelta.**

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
    → **El número de T3 ya existe (cierre del 2026-08-10):** de las **9.711 filas normales de D2**, el
    clasificador de firmas condenaría **6.558 (67,53 %)** a 54 características y **3.329 (34,28 %)** a
    122. **Se cita como cota inferior de falsos positivos irrecuperables, NO como «el FPR de un
    sistema de firmas-primero»**: en el sistema publicado `unknown` es alarma (`hibrido.py:301`,
    decisión P-5), así que lo que cae bajo umbral no queda exonerado. Lectura, tabla y forma de
    citarlo en `Implementacion/PIPELINE.md`, sección «La cascada invertida (T3)».
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
    → **El par `68,7 s / 54,8 s` de esta ficha NO existe en ningún artefacto** (detectado el
    2026-08-08 al cerrar T1). **No usarlo.** La reformulación defendible está en **T20**; esta
    viñeta no se reescribe hasta que T20 se resuelva.

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
    → **Las cifras de T2 ya existen (cierre del 2026-08-10):** el drift KS son **dos mediciones
    separadas y no intercambiables** — (A) D1 vs D2 completo: **37/54** y **44/122** características
    con drift; (B) D1 vs las **9.711 normales de D2**: **25/54** y **31/122** (`src_bytes` 0,346 →
    0,091, `dst_bytes` 0,317 → 0,107). El `delta = (A) − (B)` **se publica como comparación, nunca
    como descomposición aditiva**: el KS es un supremo de diferencia de CDF y no es aditivo sobre una
    mezcla. La salvedad está impresa en los dos informes de validación; escribirla también aquí.
    → **Estrechamiento decidido por Francisco el 2026-08-11: T11 pasa a INTERPRETAR, no a publicar.**
    `4.2.1` es la **FUENTE NUMÉRICA** del KS y `5.1` la usa **por referencia, sin repetir cifras**.
    Las cifras de (A) y (B) y la salvedad del `delta` se publican **una sola vez, en `4.2.1`**; aquí se
    citan y se interpretan. Registrado como decisión en `resumen-de-decisiones.md`
    (§ Decisiones del 2026-08-11).

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
  Francisco **no tiene acceso institucional**. **Esta es la ficha ejecutable y el inventario completo
  vive solo aquí** (consolidado el 2026-08-09: la ficha de guardia «PDF sin acceso institucional»
  duplicaba el mismo listado y se ha reducido a su función propia, con puntero a T14).
  **Las siete verificaciones — 3 degradadas + 5 cerradas por escrito.** Criterio de cierre aplicado
  a las cinco últimas el 2026-08-06: **«no verificable sin acceso institucional; no sostiene ninguna
  afirmación del trabajo»**. Cerrarlas explícitamente vale más que dejarlas como deuda flotante.
  - Citadas **degradadas** (3):
    - `Yin et al. 2017` y `Khraisat et al. 2020`: se citan **sin cifra** (metadatos verificados).
    - `Kim et al. 2014`: se cita **por su resumen**, y `3.2.2` declara que la comparabilidad exacta de
      su métrica de desconocidos no se ha podido verificar.
  - **Cerradas por escrito** (5): Arp Fig. 1 · Shyaa et al. texto completo · MDPI *Algorithms*
    18(12):749 · columnas de tiempo de UNSW-NB15 · la CV de Shone et al.

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
  **Estado el 2026-08-09 — parcialmente cubierta, sigue abierta.**
  - **Ya cubierto:** el volcado a `resumen-de-decisiones.md` está hecho (§ Decisiones del 2026-08-06
    y § Decisiones del 2026-08-09, más sus dos entradas de bitácora): reapertura declarada del track
    de código con alcance y motivo, retirada de la regla de autoría en dos velocidades, criterio
    rector del lote, renuncia al p-valor, anclaje de `[6]` en `2.1.4` con sus tres descartes y las
    conclusiones de diseño de T18 y T22.
  - **Sigue pendiente:** (1) el bloque «Decisiones tomadas a partir de este informe» en **cada uno de
    los cuatro informes** de `Obsidian_TFG_Vault/99 Investigación/`, con qué se convirtió en decisión
    y qué se descartó; (2) la **deriva de documentación de `evaluacion.py`** en los cinco ficheros
    listados arriba, que no se ha tocado.
  - **Anotado el 2026-08-09 al cerrar T0 — es trabajo de T17, no de T0:** dos de esos cuatro informes
    siguen diciendo que `6.2` la redacta Francisco (`aprendizaje-continuo-nested-learning.md:25` y
    `clasificadores-tabulares-y-arquitecturas-hibridas.md:30`), cuando la decisión marco (b) la pasó a
    **borrador del `redactor-tfg` con revisión final de Francisco**. T0 no los tocó a propósito: se
    corrigen en la misma pasada que les ponga su bloque «Decisiones tomadas a partir de este informe».

- [ ] **PDF sin acceso institucional — reabrir si Francisco consigue acceso** · — · `researcher`
  Ficha de guardia abierta el 2026-08-06 junto a T14. **Su única función es esa: quedarse de guardia.**
  Si Francisco consigue acceso institucional, se reabren las verificaciones degradadas o cerradas por
  escrito y se revisa qué afirmaciones pueden dejar de ir con salvedad.
  **El inventario de las siete verificaciones (3 degradadas + 5 cerradas) está en T14**, que es la
  ficha ejecutable. Se retiró de aquí el 2026-08-09 por duplicado; no volver a copiarlo.

### Residuos de T1 — altas del 2026-08-08

> T1 se cerró en su objetivo (ver `## Cerradas`, `5f98d88`). Estas cinco fichas son lo que **quedó
> fuera** de ese cierre, anotado con el detalle necesario para retomarlo en frío.
>
> **Dato transversal que no debe perderse:** las corridas anteriores **están en git**
> (`077119e` guarda la del código `c7cf319`; `34bee30` la de `38fdd4b`), así que los
> `.esquema-anterior.bak` son **prescindibles** y **cualquier cita a una corrida vieja debe apuntar
> al commit, nunca al `.bak`**.

- [ ] **T19 · Cifras de tiempo del vault sin respaldo en ningún artefacto** · Informe · `redactor-tfg`
  Detectado dentro de T1 (2026-08-06 a 2026-08-08). **Ninguna de estas cifras sale de una corrida que exista:**
  la **columna Tiempo entera** de la tabla de `5.1 …anomalías.md:44-47` (5,04 · 28,34 · 16,42 ·
  40,56); la frase de `5.1:58` («5 s frente a los 40,6 s del Autoencoder»); la de
  `5.2 …firmas.md:59` («DecisionTree, el más rápido, 1,8 s»); y la tabla de
  `4.4 …anomalías.md:56-61`. Hay que **regenerarlas desde `Resultados/`**.
  **Advertencia dura, no opcional:** el wall-clock **dispersa hasta 4,8× entre corridas en máquina no
  dedicada** (Autoencoder-54: 37,71 → 181,91 s, con **calidad idéntica al bit**). Estas cifras **no
  deben citarse como propiedad del algoritmo** sin declarar la dispersión.
  **Refuerzo del 2026-08-09 (cierres de T18 y T22):** la horquilla 4,8× ya puede enunciarse **«con el
  recuento de épocas idéntico»** — `n_iter_total_grid` quedó registrado y resultó **determinista**. Y
  lo que debe sostener el capítulo es el **Hallazgo 7**: los segundos absolutos **no son reproducibles
  entre corridas**, pero **el reparto interno del bloque se mueve como mucho 4,5 pp y conserva el
  orden de las ocho filas**. Es una afirmación mucho más defendible que cualquier cifra en segundos.

- [ ] **T20 · Reformular el argumento de T9 («HistGB tarda más que RF»)** · Informe · `redactor-tfg`
  El par **`68,7 / 54,8`** de la viñeta `3.5` de **T9** y del informe tabular **no existe en ningún
  artefacto**.
  **Corregida el 2026-08-09 al cerrar T18: la formulación que traía esta ficha era falsa.** No son
  4 de 4 pares ni 7 de 8, sino **8 de 10 pares** intra-corrida en el mismo sentido, y los **dos
  contraejemplos están ambos en la variante de 54** (2 de cada 5 corridas invierten ese par). Por eso
  **se retira la horquilla «1,31×-4,40×»**: se queda sin cota inferior. La afirmación **solo es sólida
  en la variante de 122**. Sigue siendo **coste de entrenamiento**, y **en inferencia a 54
  características el orden se invierte**: HistGB **0,0032 ms/flujo** frente a RF **0,0072** (los
  `0,0035 / 0,0069` que citaba esta ficha son de otra corrida). Y sigue **sin ganar `f1_macro`**
  (0,804 vs 0,822).
  **La dirección aguanta y la prosa del vault no se toca**; lo que era falso es la formulación
  recomendada aquí. **La formulación correcta y anclada está en `PIPELINE.md:252-256`**, y es la que
  debe usarse.

- [ ] **T21 · Declarar la mitad de P9 que T1 no cubre** · Informe · `redactor-tfg`
  `latencia_ms_por_flujo` mide **solo `predict`/`score`** sobre características ya calculadas y en
  memoria. El **coste real de despliegue** —captura, ensamblado de flujo, extracción de las 41
  características— **no está medido**. Citar «4,4 millones de flujos/s» como capacidad operativa sin
  esa salvedad **sería el propio pitfall P9** (*Lab-Only Evaluation*) que se dice estar cubriendo.
  Encaja en `5.4` y en el inventario de límites de **T6**.

### Residuos de T15 y T18 — altas del 2026-08-09

> T15 (auditoría de `Bibliografía.md`) y T18 (rediseño de `alcance_tiempo_s`) se cerraron el
> 2026-08-09 (ver `## Cerradas`). Estas tres fichas son lo que **quedó fuera** de esos cierres.

- [ ] **T23 · Correcciones del texto que la auditoría de bibliografía dejó sin autorizar** · Informe · `redactor-tfg`
  Salen del informe `Obsidian_TFG_Vault/99 Investigación/Auditoría de Bibliografía.md` (T15). Son las
  correcciones de texto que **no estaban autorizadas** en aquel encargo y por tanto no se aplicaron.
  **Fuera de esta ficha, ya ejecutadas:** reformular `1.1:12` al dato agregado de INCIBE, repuntar
  `2.1.2:30,64` de `[6]` a `[5]`, y `2.2.1:32` de `[9]` a `[8]`.

- [ ] **T24 · `2.1.4 Algoritmos de ML` no tiene bloque de redes neuronales** · Informe · `redactor-tfg`
  Hueco del marco teórico detectado por el `redactor-tfg` el 2026-08-09, **independiente de la
  bibliografía**: el apartado enumera algoritmos de ML sin ningún bloque de redes neuronales, cuando
  la etapa 1 del sistema es un Autoencoder-MLP.

- [ ] **T25 · `[6]` (Goodfellow) se ha quedado sin cita en el texto** · — · `researcher`
  Choca con la **regla dura de T16** («ninguna entrada sin cita en el texto»): tras repuntar
  `2.1.2:30,64` a `[5]`, `[6]` no la cita nadie. Además, la columna «Dónde se usa» de
  `Bibliografía.md:32` está **desactualizada** y el aviso de `:86` puede que ya no proceda. **Solo el
  `researcher` toca ese fichero.**
  **Decisión de Francisco del 2026-08-09: `[6]` NO se retira — se ancla en `2.1.4 Algoritmos de ML`**,
  abriendo allí el bloque de redes neuronales que falta. Esto **enlaza T25 con T24**.
  - Descartados `2.1.5`/`2.1.6`: son métricas y metodología, **no arquitecturas**.
  - Descartado presentar el autoencoder como **red profunda** para colgarle la cita: la memoria
    afirma lo contrario en `3.1:28`, `3.4:28` y `2.3.1:24`, y crearía una **contradicción entre
    capítulos**.
  - El anclaje legítimo es el **error de reconstrucción**, que el proyecto usa en `3.4.2` y `4.4`:
    Goodfellow se cita como referencia canónica **del concepto**, **sin afirmar que el modelo del TFG
    sea profundo**.
  - ~~**Restricción dura:** `2.1.4` es teoría del capítulo 2.x y la prosa la escribe Francisco.~~
    → **RETIRADA el 2026-08-09 al cerrar T0.** Era la misma pregunta que T0, no una regla
      independiente, y **Francisco la decidió en el sentido de no exceptuar**: `2.1.4` entra en la
      retirada completa de `2.x` que ordenaba la decisión marco (b). Exceptuar una sola nota habría
      reintroducido a mano la regla recién retirada del capítulo entero.
      **Consecuencia: T25 queda desbloqueada** y la prosa de `2.1.4` —incluido el bloque de redes
      neuronales que abre **T24**— la redacta el `redactor-tfg`. El anclaje de `[6]` ya no espera a
      nadie.
  - **Pendiente para el `researcher`, en ciclo propio:** actualizar la columna «Dónde se usa» de
    `Bibliografía.md:32`, retirar el aviso de `Bibliografía.md:86` si ya no procede, y corregir el
    error de `Obsidian_TFG_Vault/99 Investigación/Auditoría de Bibliografía.md:140`, que afirma que
    «`[6]` se usa bien en otros sitios y se queda» — **es falso**.

### Migración de `next-steps.md` §3.2 — altas del 2026-08-11

> Las cinco fichas siguientes salen de la **migración de la deuda técnica de `next-steps.md` §3.2**,
> hecha el **2026-08-11**: eran casillas `☐` dentro de un fichero congelado, donde nadie las miraba.
> **§3.2 y §3.3 quedan como historial**, con cabecera propia y **sin reescribir ni una casilla**; el
> estado vivo de lo que siga abierto es **este**.
>
> **Las líneas citadas son las POSTERIORES a esa cabecera de migración**, que añadió 5 líneas a §3.2:
> `:267` era `:262` · `:271` era `:266` · `:282`/`:283`/`:284` eran `:277`/`:278`/`:279`.
>
> **[HISTORIAL — SUPERADO EL 2026-08-11, NO CITAR COMO VIGENTE] Lo que fue el «DESAJUSTE VIVO» de
> las salidas de `validacion.py`.** El texto de abajo se conserva **sin reescribir**, pero **su
> contenido ya es falso**: dice que `validacion.py` está «incompleto y sin re-correr» y que los
> informes de `Resultados/` son de la corrida `274923d`-sucio del 2026-08-10 (20:24 y 20:45).
> **Verificado en disco el 2026-08-11:** los dos `*_validation_report.txt` llevan sello
> **`fc1c6b4-sucio`** y fecha **`2026-08-11T20:53:27`** (54) / **`20:53:46`** (122) en su propia
> cabecera (`:4-5`). **La refutación completa, con lo que sí queda abierto, está ~27 líneas más
> abajo, en la nota «ACTUALIZACIÓN 2026-08-11 — … QUEDA RESUELTO».** Quien haya llegado aquí por
> `grep` debe leer esa nota antes de actuar.
>
> `Implementacion/app/validacion.py` está **commiteado como WIP en `d9225be`** (`+231 −21`, 6 hunks,
> 1144 líneas; el registro de aquella sesión salió en `9734f4b`), **incompleto y sin re-correr**.
>
> **COMMITEADO NO ES TERMINADO — es la distinción que gobierna este grupo.** Las **tres fichas `[~]`**
> de abajo (`:282`, `:283`, `:284`) **siguen abiertas**, y **ya no por falta de commit —lo tienen—**
> sino por dos motivos nuevos: (i) el fichero **quedó incompleto** —`_save_report()` **no escribe**
> `zero_day_df`, y el parámetro `onehot` de `:991` **nunca se lee** (parámetro muerto)—; y (ii) **no se
> ha re-corrido**, así que **no se sabe si el fix de orden destapa un desajuste D2/D3 real**. De ahí las
> **dos lecturas erróneas que hay que evitar, y van en direcciones opuestas**: **ni** dar el trabajo por
> perdido y **reimplementar las ~231 líneas** —están en `d9225be`—, **ni** cerrar las fichas invocando
> «lo hecho es lo que tiene commit», porque aquí el commit **no** acredita que la tarea esté hecha.
>
> **El commit no regenera nada en disco.** Los **2 informes de validación y las 12 figuras** que hay en
> `Resultados/` **siguen siendo** de la corrida **`274923d`-sucio**: los dos `*_validation_report.txt`
> son del **2026-08-10** (20:24 y 20:45), **previos** a esas ediciones, y **no contienen ni el delta
> 77→122 ni la lista de 0-day**. **No corresponden al código que hay hoy en el fichero, y nadie debe
> citarlas como producto suyo.** El fichero **no quedó roto: quedó incompleto** (`ast.parse` OK) — un
> implementador se cortó a media ejecución. **No hay nada que revertir.**
>
> **Deuda nueva detectada en la misma inspección, sin ficha propia** (se cierra con `:282` y `:283`):
> (i) los comentarios de `validacion.py:82-83` y `:338-339` **afirman un comportamiento que no
> existe** («se persisten en el informe», «para que `_save_report()` lo persista»); (ii)
> `COLUMNAS_CATEGORICAS` y `COLUMNAS_NO_CARACTERISTICA` (`:90-91`) son **constantes de clase
> duplicadas por copia** de `program.py:53` y `program.py:281-283`, acoplamiento que el propio
> comentario `:87-89` reconoce.
>
> **ACTUALIZACIÓN 2026-08-11 — el desajuste vivo de arriba QUEDA RESUELTO; no citarlo más como
> vigente.** Las **tres fichas `[~]`** (`:282`, `:283`, `:284`) están **cerradas** (ver
> `## Cerradas`): `validacion.py` se completó sobre el código de `d9225be` —sin reescribir sus
> ~231 líneas— y se **re-corrió en las dos variantes** (`EXITCODE=0`, `Integridad: APROBADA`), con
> **16 artefactos regenerados** en `Resultados/` el 2026-08-11 19:28. Los dos
> `*_validation_report.txt` del 2026-08-10 **ya no son los que hay en disco**, así que la
> advertencia «no corresponden al código de hoy» **ha dejado de aplicar**. De esta migración
> **siguen abiertas solo dos** de las cinco fichas (rutas absolutas y `warnings.filterwarnings`),
> más la ficha nueva de las constantes duplicadas que se abre justo debajo.
>
> **Corrección al paréntesis «(se cierra con `:282` y `:283`)» de la deuda nueva:** de sus dos
> mitades solo se cerró la primera —los comentarios de `:82-83` y `:338-339` **ya son verdad**—.
> **Las constantes duplicadas de `:90-91` NO se cerraron:** el encargo **prohibía tocarlas**.
> Pasan a **ficha propia abajo**, pendiente de decisión de Francisco.
>
> **ACTUALIZACIÓN 2026-08-11 (segundo ciclo) — esa ficha propia ya está CERRADA** (ver
> `## Cerradas`): Francisco decidió **ejecutarla, no aceptarla como deuda**. Las constantes son ahora
> de **módulo** en `program.py:36-37` y `validacion.py` las **importa**; las líneas se desplazaron de
> `:90-91` a **`:100-101`**, así que **no citar más `:90-91`**.

- [ ] **Rutas absolutas hardcodeadas en `program.py` y `validacion.py`** (🟠) · Código · `ml-implementador`
  Origen: `next-steps.md:267` (§3.2). Poco portable y poco reproducible.
  **ABIERTA. No se toca en este lote:** toca `program.py`, y eso obliga a **decidir antes si se
  regeneran los splits**. Esa decisión es de Francisco.

- [ ] **`warnings.filterwarnings('ignore')` global** (🟡) · Código · `ml-implementador`
  Origen: `next-steps.md:271` (§3.2). Oculta avisos útiles durante la experimentación.
  **ABIERTA. Verificado vivo el 2026-08-11** en `program.py:12` y **`validacion.py:57`**.
  - **TRAMPA — no citar más `validacion.py:21`.** Esa línea (que esta ficha apuntaba antes, y antes
    aún `:12`) **es hoy un COMENTARIO**, parte del bloque `:19-25` que documenta los efectos de
    `import program` y que **menciona** `warnings.filterwarnings('ignore')` citando
    `program.py:12`. Quien vaya a `:21` a «borrar la línea» **borra la documentación y deja el
    `filterwarnings` vivo**. La llamada real es `validacion.py:57`, después de
    `import program` (`:33`) e `import config` (`:55`).

### Residuos del cierre de `validacion.py` — altas del 2026-08-11

> Las tres fichas `[~]` de `validacion.py` (`:282`, `:283`, `:284`) se cerraron el **2026-08-11** con
> dictamen **APTO CON CAMBIOS** de `auditor-ml` (ver `## Cerradas`). Estas fichas son lo que
> **quedó fuera** de ese cierre. **Ninguna es 🔴.**
>
> **Actualización 2026-08-11 (segundo ciclo):** de las seis originales, la del **rótulo media/mediana**
> está **cerrada** (ver `## Cerradas`), así que **quedan cinco**. La que hoy tiene consecuencia sobre
> la memoria es el residuo nuevo del vault (`4.2:107`) que se abre más abajo.
>
> **ACTUALIZACIÓN 2026-08-11 (tercer ciclo) — esas cinco están CERRADAS** (ver `## Cerradas`), en un
> **ciclo agrupado** junto a las dos que dejó el segundo ciclo (el alias de las constantes y el
> comentario del orden de import): **siete residuos, una sola corrida, ninguna cifra publicada
> alterada**. Esta cabecera queda como **historial**; no quedan fichas abiertas debajo de ella.

### Residuos del cierre de media/mediana y constantes — altas del 2026-08-11 (segundo ciclo)

> Salen del cierre de las dos fichas de arriba (rótulo media/mediana y constantes duplicadas), con
> dictamen **APTO CON CAMBIOS** de `auditor-ml` y **ninguna cifra publicada alterada**. **Ninguno es
> 🔴.** Los dos primeros son 🟠 y **no tenían ficha propia**; los dos últimos son de una línea y **no
> exigen re-correr nada**.

- [ ] **El vault sigue diciendo «mediana» donde el artefacto ya dice «media»** (🟠) · Informe · `redactor-tfg`
  `Obsidian_TFG_Vault\04 Implementación del sistema\4.2 Base de datos utilizada.md:107` afirma «**La
  mediana de outliers en D1 es del 4,78 %**». Es el **único** sitio del vault afectado y
  **correctamente no se tocó** en el cierre del rótulo (es track Informe), pero ahora **contradice
  explícitamente al artefacto de origen**, que ya rotula «media entre características».
  - **Nadie lo tenía fichado:** la ficha del rótulo solo nombraba `GUIA_RESULTADOS.md` y
    `PIPELINE.md`, y la ficha del `4.2` tiene tres puntos y **ninguno es este**.
  - **Va ANTES de T10.** Si T10 vuelca `4.2` tal cual, el TFG **publica un estadístico que nadie ha
    calculado** — exactamente el defecto que el cierre del rótulo venía a eliminar.
  - **PUNTERO CRUZADO (añadido el 2026-08-11):** la otra ficha de esta misma nota es
    **«`4.2`: añadir la medición (B) del KS, arreglar la frase del FPR y el callout de
    trazabilidad»** (sección «Altas del grill del 2026-08-11»), y su **punto 3 toca `:110`** — a
    **tres líneas** de la «mediana» de `:107` que corrige esta ficha. **Mismo agente
    (`redactor-tfg`), mismo párrafo, ambas antes de T10: conviene despacharlas en la MISMA pasada.**
    Ejecutar una sola deja la nota internamente inconsistente y fuerza una segunda visita al mismo
    sitio.

> **ACTUALIZACIÓN 2026-08-11 (tercer ciclo):** de los tres residuos de esta sección, los **dos de
> `validacion.py`** (el alias de las constantes y el comentario falso del orden de import) están
> **cerrados** dentro del ciclo agrupado de los siete (ver `## Cerradas`). **Sigue abierta solo la
> primera**, la del vault — es track Informe y va **antes de T10**. Confirmado el 2026-08-11: **el
> error sigue vivo en la nota.**

### Residuo del ciclo de los siete — alta del 2026-08-11 (tercer ciclo)

> Sale del cierre agrupado de los siete residuos de `validacion.py`. **No es 🔴** y **no se cerró a
> propósito**: no puede cerrarse hasta que exista el commit.

- [ ] **Re-anclar el sello `fc1c6b4-sucio` de los cuatro artefactos de validación** (🟡) · Código · `ml-implementador`
  Los dos `*_validation_report.txt` y los dos `*_vocabulario_onehot.csv` salieron sellados
  **`fc1c6b4-sucio`** (fecha por invocación: 54 → `20:53:27` · 122 → `20:53:46`) porque la corrida se
  hizo con el árbol sucio. El aviso de «**pendiente de re-anclaje**» está **conservado y replicado** en
  `Implementacion/PIPELINE.md`, `Resultados/GUIA_RESULTADOS.md` y `resumen-de-decisiones.md`, **sin
  ningún hash inventado** — y así debe quedarse hasta que se resuelva.
  - **Se resuelve cuando exista el commit de cierre**, de una de dos formas: re-correr `validacion.py`
    en las dos variantes con el árbol limpio (**ninguna cifra debe moverse**; si alguna se mueve, es un
    hallazgo) o re-anclar el texto de los tres documentos al hash real.
  - **Los anclajes concretos de la vía «re-anclar el texto», verificados en disco el 2026-08-11**
    (la ficha nombraba los tres documentos pero **no enumeraba las líneas**):
    **`Implementacion/PIPELINE.md:161, 171, 189, 331`** y
    **`Resultados/GUIA_RESULTADOS.md:101, 122, 255, 478-481`**. Más el sitio del sello en
    `resumen-de-decisiones.md`, que va con su propia nota fechada.
    - **`PIPELINE.md:331` SE AUTO-INSTRUYE a re-anclarse** —la fila `fc1c6b4-sucio` de la tabla de
      corridas dice literalmente «hay que **re-anclar el hash en el commit de cierre** de este
      ciclo, en esta fila y en el recuadro de trazabilidad de arriba»—, y esta ficha **no lo
      sabía**: son **dos** sitios, la fila y el recuadro (`:161`/`:171`).
    - **`PIPELINE.md:189` es un anclaje FRÁGIL:** cita `fichero:línea` de un **artefacto
      regenerable** (`Resultados/specialized_nsl_kdd_validation_report.txt:4-5`, la cabecera
      `Commit del código:` / `Fecha de la corrida:`). Hoy es correcto —verificado byte a byte—, pero
      **cualquier re-corrida que cambie el número de líneas de cabecera lo desplaza en silencio**.
      Al re-anclar, comprobar también ese `:4-5`, o citar el campo por su nombre en vez de por su
      línea.
  - **Convención de los tres valores del sello** (`<hash>` · `-sucio` · `-suciedad_desconocida`):
    tabla canónica en `PIPELINE.md:952-963`.
  - **PUNTERO CRUZADO (añadido el 2026-08-11):** la tabla de corridas que hay que retocar aquí
    (`PIPELINE.md:329-331`) arrastra además **dos filas caducadas**, fichadas justo debajo en
    «Incoherencias de `PIPELINE.md`…» (ficha 2). **Quien abra esa tabla para re-anclar el
    `fc1c6b4-sucio` de `:331` debería arreglar las tres cosas en la misma pasada.**

### Incoherencias de `PIPELINE.md` — altas del pase de cuadre del 2026-08-11

> Detectadas por el `cronista` en el pase de cuadre de cierre de sesión del **2026-08-11**, fuera del
> alcance que traía ese encargo, y **dadas de alta por decisión del `leader`** para que no se pierdan.
> **Las dos son track Código, tocan DOCUMENTACIÓN y no comportamiento: ninguna exige re-correr nada.**
> Anclas verificadas en disco antes de escribirlas. **Fichar no es resolver: aquí no se arregló nada.**

- [ ] **`PIPELINE.md:180` se contradice con `:171` dentro del MISMO recuadro** (🟠) · Código · `ml-implementador`
  El recuadro de trazabilidad de `Implementacion/PIPELINE.md` afirma las dos cosas a la vez: `:169-171`
  dice que «el ciclo de residuos ya está aplicado y re-corrido, pero **su commit de cierre todavía no
  existe**», y `:179-181` dice que los artefactos «son además **artefactos versionados**: **están
  commiteados** y `validacion.py` no ha cambiado desde el commit que los versiona».
  - **Es OTRA RECAÍDA del mismo defecto** que la fila `9af842c` de `## Cerradas` deja documentado como
    dato que merecía quedar escrito: **afirmar en presente algo que la corrida aún no respaldaba**.
    Reapareció, una vez más, en un sitio nuevo.
  - **Cuál de las dos ha quedado falsa hoy: `:171`.** El commit de cierre **ya existe** — es
    **`9af842c`**—, así que `:180` es la mitad verdadera y la frase «todavía no existe» es la que hay
    que corregir. Es **texto vigente y engañoso, no historial**: no lleva ninguna nota fechada que lo
    supere.
  - **Relación con la ficha del re-anclaje:** `:171` es uno de los cuatro anclajes que esa ficha
    enumera, así que las dos se tocan — pero **no son la misma cosa**: allí se sustituye un hash,
    aquí se retira una afirmación falsa.

- [ ] **`PIPELINE.md:329` y `:330` están caducadas: dos corridas «aún en el árbol» que ya tienen commit** (🟡) · Código · `ml-implementador`
  En la tabla de corridas de `Implementacion/PIPELINE.md`, la columna «versionados» dice:
  - `:329` — fila `1163c90`: «*(aún en el árbol de trabajo, **pendiente del commit de cierre de
    T18**)*», cuando `features.md` registra **T18 cerrada en `8fdc421`** (ver `## Cerradas`).
  - `:330` — fila `274923d-sucio`: «*(aún en el árbol de trabajo)*», cuando esa corrida es la de la
    cascada invertida (**T3**), **cerrada en `b1f1df2`**.
  - **Agravante — es la MISMA tabla** en la que vive la fila `fc1c6b4-sucio` (`:331`) que la ficha
    **«Re-anclar el sello `fc1c6b4-sucio`…»** (justo arriba, en «Residuo del ciclo de los siete»)
    manda re-anclar. **Quien abra la tabla para eso debería arreglar las tres filas en la misma
    pasada**; puntero cruzado puesto también en esa ficha.
  - **No es 🔴 pero engaña sobre reproducibilidad:** un tercero que lea `:329-330` concluye que las
    cifras publicadas de T18 y de T3 no se pueden recuperar de git, cuando sí se pueden.

### Altas del grill del 2026-08-11 — dos specs pendientes

> Salen del `grill-me` cerrado con Francisco el **2026-08-11**; ninguna de las dos estaba en disco
> antes de esa fecha. Ambas son **carril Intervención** y de **lectura estrecha**: **no absorben ni
> sustituyen ninguna ficha existente.**

- [ ] **`4.2`: añadir la medición (B) del KS, arreglar la frase del FPR y el callout de trazabilidad** · Informe · `redactor-tfg`
  Sobre `Obsidian_TFG_Vault/04 Implementación del sistema/4.2 Base de datos utilizada.md`. Tres puntos
  y nada más. **T10 sigue intacta: esto no la sustituye ni la absorbe.**
  1. Añadir la medición **(B)** junto a la **(A)**, con tabla: **(A)** D1 vs D2 completo = **37/54** y
     **44/122**; **(B)** D1 vs las **9.711 normales de D2** = **25/54** y **31/122** (`src_bytes`
     0,346 → 0,091; `dst_bytes` 0,317 → 0,107). **Con la salvedad impresa:** el `delta = (A) − (B)` es
     **COMPARACIÓN, nunca descomposición aditiva** — el KS es un supremo de diferencia de CDF y **no es
     aditivo sobre una mezcla**.
  2. **Reescribir la frase del FPR de `:99`**, que hoy usa **(A)** para sostener algo que **solo (B)
     sostiene**: (A) compara D1 contra un D2 que es **57 % ataques**, y los falsos positivos los
     generan las filas **normales**.
  3. **Corregir el callout de trazabilidad de `:110`**, que afirma que los estadísticos se calculan
     «sobre los splits ya procesados (54 características)» cuando **ya existe el informe de la variante
     122**.
  - **PUNTERO CRUZADO (añadido el 2026-08-11):** el `:110` del punto 3 está a **tres líneas** del
    `:107` de la ficha **«El vault sigue diciendo "mediana" donde el artefacto ya dice "media"»**
    (sección «Residuos del cierre de media/mediana y constantes»), que corrige el 4,78 % de outliers
    en esa misma nota. **Mismo agente (`redactor-tfg`), mismo párrafo, ambas antes de T10:
    despacharlas en la MISMA pasada.** Ejecutar una sola deja la nota internamente inconsistente.
  - **ORDEN IMPUESTO (dependencia dura):** las **tres correcciones de `validacion.py` van ANTES** que
    esta ficha — las del grupo «Migración de `next-steps.md` §3.2»: `:282` (los 17 tipos 0-day), `:283`
    (el delta 77→122) y `:284` (la comparación por orden). **Motivo:** esta nota **cita el informe y
    las figuras que la re-corrida regenera**, y los que hay hoy en disco son de la corrida
    `274923d`-sucio (ver el desajuste vivo anotado en la cabecera de ese grupo).
    → **DEPENDENCIA SATISFECHA el 2026-08-11:** las tres están **cerradas** y `validacion.py` se
    re-corrió en ambas variantes, con **16 artefactos regenerados** en `Resultados/` (19:28). **Esta
    ficha queda desbloqueada** y debe citar los informes y figuras de **esa** corrida, no los del
    2026-08-10. **Corrección del 2026-08-11 (ciclo de los siete residuos) — lo que decía aquí ya es
    falso:** el `*_vocabulario_onehot.csv` y las cabeceras de los dos `*_validation_report.txt` **sí
    llevan ya `commit` y `fecha`** (`config.commit_actual()`), así que la trazabilidad **no** hay que
    anclarla a mano. **Dos precisiones para citar bien:** (i) los artefactos vigentes son los de la
    corrida del **2026-08-11 20:53:27** (54) y **20:53:46** (122), **no los de las 19:28**; (ii) su
    sello es **`fc1c6b4-sucio`** y está **pendiente de re-anclaje** al commit de cierre (ficha propia
    en este mismo fichero). Se cita ese sello tal cual; **no se inventa hash.**
  - **Fuente numérica:** por la decisión del 2026-08-11, las cifras del KS se publican **una sola vez,
    aquí en `4.2.1`**; `5.1` las usa **por referencia** y **T11 interpreta, no publica**.

- [ ] **Glosa del sufijo `-sucio` en la primera aparición de `PIPELINE.md` y `GUIA_RESULTADOS.md`** · Código · `ml-implementador`
  **Una línea** en la **primera aparición** de `Implementacion/PIPELINE.md` (**`:158`**) y de
  `Resultados/GUIA_RESULTADOS.md` (**`:101`**), describiendo la **convención** y **remitiendo a la
  tabla canónica de `PIPELINE.md:952-963`**, que queda **INTACTA y no se duplica**. **Referencia
  reapuntada el 2026-08-11:** era `:879-888` y se desplazó con el ciclo de los siete residuos; el
  bloque es hoy el encabezado `### El sello commit…` (`:952`) más su tabla de tres valores
  (`:959-963`).
  - **Las dos anclas de la primera aparición, RE-VERIFICADAS EN DISCO el 2026-08-11.** Esta ficha
    decía `PIPELINE.md:140` y `GUIA_RESULTADOS.md:350`, y **las dos eran falsas**: la primera
    aparición de `-sucio` está en **`PIPELINE.md:158`** («la corrida de **T2** (`274923d-sucio`…»)
    y en **`GUIA_RESULTADOS.md:101`** (fila `commit`, `fecha` de la tabla del CSV de vocabulario).
    **`GUIA_RESULTADOS.md:350` está 249 líneas por debajo y habla de otra cosa** — las figuras del
    KS de drift (A), «no una segunda medición de drift (A) sobre el set del TFG». **Ojo: el
    desplazamiento es de SIGNO CONTRARIO** al que esta ficha ya había corregido para la tabla
    canónica (`:879-888` → `:952`), así que su propio aviso de reapuntado **no cubría este caso**:
    aquí las líneas subieron, no bajaron.
  - **Contexto verificado el 2026-08-11:** el `-sucio` ya está documentado en `config.py:489-511`,
    `evaluacion.py:69-75` y esa tabla. **El hueco es solo de orden de lectura**: **≈794 líneas** de
    distancia dentro de `PIPELINE.md` (`:158` → `:952`; la cifra «740» que decía esta ficha salía de
    las anclas viejas), y ninguna explicación en `GUIA_RESULTADOS.md`. **No aparece en el vault.**
  - **Estado: ABIERTA, la glosa de una línea NO está escrita** — verificado por lectura de las dos
    primeras apariciones. **Retirado el argumento «ninguno de los dos ficheros aparece modificado en
    el árbol»**: era la evidencia de «no empezada» y **hoy no evidencia nada**, porque este ciclo ya
    commiteó ambos ficheros (`9af842c`, `84e3c8f`). El estado se comprueba leyendo `:158` y `:101`,
    no el `git status`.

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

> **Actualización 2026-08-08:** `T1` **cerrada** (`5f98d88`, 8 tablas publicadas sobre el esquema
> nuevo, cuatro pasadas de `auditor-ml`), así que **`T4` queda desbloqueada**. De T1 salen cinco
> residuos, dados de alta como `T18`-`T22`. `T18` **también exige una corrida del runbook**: si se va
> a correr `T4`, conviene decidir antes el orden para no repetir cómputo.

> **Actualización 2026-08-09:** `T18` y `T22` **cerradas** — su corrida del runbook es `1163c90`—, así
> que ese condicionante desaparece: **`T4` (10 semillas) es la siguiente tarea de código**, ya sin
> bloqueo previo. De los residuos de T1 siguen abiertos `T19`, `T20` y `T21`, los tres de track
> Informe. `T15` cerrada también, con tres residuos nuevos: `T23`-`T25`.

> **Actualización 2026-08-10:** `T2` y `T3` **cerradas**, ambas con dictamen APTO de `auditor-ml` (ver
> `## Cerradas`). Con ellas quedan hechas las **dos mediciones baratas** del lote, y del track de
> código reabierto **solo queda `T4` (10 semillas)**. **`T9` y `T11` siguen ABIERTAS**: T2 y T3 no las
> cierran, solo las alimentan —el número de la cascada invertida va a `3.2.2` (T9) y el KS separado a
> `5.1`/`5.4` (T11)—, y las cifras quedan anotadas dentro de cada ficha con su salvedad de uso.

> **Sección reescrita por T0 el 2026-08-09**, al aplicar la retirada de la regla «lo escribe
> Francisco» en sus dos velocidades. Lo que sigue es el estado vigente; la lista anterior —que
> reservaba a Francisco todo el capítulo 2, la prosa de `4.2` y `6.2`— **ya no está en vigor**.

### Autoría de la redacción — estado vigente desde T0 (2026-08-09)

Antes había aquí una lista de secciones vedadas a los agentes. Solo **una** sobrevive.

**Lo que sigue siendo de Francisco, y solo eso:**

- **La bibliografía final con Zotero en formato IEEE.** Trabajo mecánico en su máquina, fuera del
  vault. No confundir con `Bibliografía.md`, que es del `researcher`.

**Lo que pasó a los agentes:**

| Sección | Quién redacta | Condición |
|---|---|---|
| Todo `02 Marco Teórico` — 2.1.6, **`2.1.4`**, bloque 2.2, bloque 2.3 | `redactor-tfg` | Ninguna. Parte de los guiones ya propuestos en las 8 notas (2026-07-15) |
| `4.2` — origen del dataset, las 41 características | `redactor-tfg` | El borrador **ya existe** en la nota (decisión del 2026-07-21). El «por qué NSL-KDD» lo revisa Francisco. Contenido: **T10** |
| `6.2 Líneas futuras` | `redactor-tfg` | Revisión final de Francisco. Respaldo en `EL_FUTURO.md` |

> **`2.1.4` no queda exceptuada.** Era la pregunta que T0 y T25 compartían y **la decidió Francisco
> el 2026-08-09**: exceptuar una sola nota reintroduciría a mano la regla que la decisión marco (b)
> acababa de retirar del capítulo entero. Con esto **T25 queda desbloqueada**, y con ella **T24**.

> **Recuento:** la lista anterior decía «las 9 notas». Son **8** — `2.2.1` nunca llevó el callout de
> autoría, como ya corrigió la ficha de T0.

---

## Cerradas

| Fecha | Track | Tarea | Commit |
|---|---|---|---|
| 2026-08-11 | Código | **`commit` + `fecha` en el CSV de vocabulario y en la cabecera de los dos informes de validación** — la ficha que gobierna el **ciclo agrupado de los siete residuos** de `validacion.py`. Cerrada por la **opción A que aprobó Francisco**: `validacion.py` **importa `config.py`** (`:55`) y estampa `config.commit_actual()` (`:111`) en los **cuatro artefactos**. **Cruza una frontera que se documentaba como inexistente** —`program.py` y `validacion.py` no dependían de `config.py`—: registrado en `resumen-de-decisiones.md` que la decisión **CONSUME Q2 y EXTIENDE su alcance de rutas a procedencia**, y **explícitamente NO como permiso literal**, porque Q2 hablaba de rutas y `commit_actual()` no es una ruta. **`program.py` NO pasa a depender de `config.py`**; actualizadas en consecuencia la frase de independencia de `CLAUDE.md`, la cabecera de `config.py` y `PIPELINE.md`. Sello: **`fc1c6b4-sucio`**, fecha por invocación (54 → `20:53:27` · 122 → `20:53:46`), **pendiente de re-anclaje** al commit de cierre — **ficha propia abierta**, sin ningún hash inventado. **Hechos del ciclo, comunes a las siete filas:** **dos pasadas de `auditor-ml`, ambas APTO CON CAMBIOS, ambas aplicadas** —la primera con **seis afirmaciones falsas** (documentación escrita **en presente antes** de la corrida), la segunda, estrecha, con **cuatro correcciones**—; **no se despachó tercera vuelta**, y la razón queda declarada: eran correcciones textuales verificables por lectura directa (un ancla, una fila de tabla, dos reformulaciones y una cláusula de bitácora) y el auditor ya había validado **dos veces** la sustancia (frontera `config.py` sin efectos ni ciclos, `program.py` intacto, cero `fit`, cero cifras alteradas, matiz de Q2 correcto). **Una sola corrida y ninguna cifra publicada se mueve:** diff de `Resultados/` contra `fc1c6b4` caracterizado, **cero diferencias fuera de las cuatro clases esperadas**; intactos `Integridad: APROBADA`, D1 67.343 / D2 22.544 / D3 58.630 / 9.711 normales (43,1 %), drift (A) 37 y 44 · (B) 25 y 31, outliers 4,78 % y 2,44 % con el rótulo «media entre características», **los 17 tipos 0-day byte a byte** (mscan 996 … worm 2; total 3.750, 16,63 %) y el one-hot 77→122 con desglose `service` +44 / `flag` +1 / `protocol_type` +0. Zanjado además: las **12 figuras son byte-idénticas** a HEAD (generación determinista), los **splits NO se regeneraron** (`*_original_*`, `*_processed_*` y ambos `_transformers.joblib` conservan mtime del 2026-07-05) y **ningún `metricas_*.csv`** se tocó. **Dato que merece quedar escrito:** el mismo defecto —afirmar en presente algo que la corrida no respalda— **reapareció en un sitio nuevo en cada vuelta**; la segunda aparición viva estaba en `resumen-de-decisiones.md:765-769` y se trató bien: **nota fechada que la supera, sin reescribir el texto histórico** | `9af842c` |
| 2026-08-11 | Código | **`PIPELINE.md` y `GUIA_RESULTADOS.md` al día — y el recuadro que MENTÍA ya no miente.** Era el 🟠 del grupo: `PIPELINE.md:141-146` atribuía los informes y las 12 figuras que hay en disco a la corrida `274923d`-sucio del **2026-08-10** «todos con marca de tiempo de esa re-corrida» y remataba «**hay que creerse este recuadro**» (`:152`) — pedía crédito explícito que no merecía. Reatribuido a la corrida del **2026-08-11** y puestos al día `Implementacion/PIPELINE.md:43-45,103-108,139-153` y `Resultados/GUIA_RESULTADOS.md:16,§3.2`, que además **ya listan el artefacto nuevo** `*_vocabulario_onehot.csv`. La tabla canónica del sello `commit` queda en `PIPELINE.md:952-963` (**la referencia se desplazó**: era `:879-888`). Sale en el ciclo agrupado de los siete; dictamen y verificaciones, en la fila de arriba | `9af842c` |
| 2026-08-11 | Código | **El 77 del delta 77→122 ya se publica rotulado como RECONSTRUCCIÓN.** No es el vocabulario que el pipeline usó en su día: se **recuenta** desde los CSV `_original_*`, así que sin rótulo cualquiera podía leerlo como cifra registrada por `program.py`. El token `RECONSTRUIDO` va ahora **en consola y en el informe** (`validacion.py:977` y `:1230`), en las dos variantes. Cambio de rótulo, **no de cálculo**: el 77, el 122 y el 45 siguen **recontándose, cero literales**. Sale en el ciclo agrupado de los siete | `9af842c` |
| 2026-08-11 | Código | **Los recuentos del CSV de vocabulario one-hot ya son enteros.** `38.0 / 77.0 / 122.0 / 45.0` pasan a `38 / 77 / 122 / 45` en la fila `__total__` de los dos `*_vocabulario_onehot.csv`. Son recuentos: publicarlos como flotantes invitaba a leerlos como promedios. Sale en el ciclo agrupado de los siete | `9af842c` |
| 2026-08-11 | Código | **El encabezado «Recomendaciones:» ya no se imprime vacío.** Ahora solo se escribe **si hay alguna** (`validacion.py:1102`, `:1122`), con la condición documentada en el propio código. Efecto verificado en disco: la variante de **54 pierde el encabezado** —no tenía recomendaciones que dar— y es una de las cuatro clases de diferencia esperadas del diff. Un encabezado vacío en un artefacto publicado invitaba a pensar que se había perdido algo. Sale en el ciclo agrupado de los siete | `9af842c` |
| 2026-08-11 | Código | **Las constantes importadas de `program.py` ya son copia, no alias.** `validacion.py` envuelve en `list(...)` (`:156-157`, **antes `:100-101`: no citar más esas líneas**) `COLUMNAS_CATEGORICAS` y `COLUMNAS_NO_CARACTERISTICA`, igual que hace `program.py:65` con la canónica de `program.py:36-37`. Era **inerte hoy** —todos los usos son de lectura— pero una **mutación futura habría contaminado el one-hot real sin dejar rastro**. Arreglo de una línea, **sin re-correr nada obligado**. Sale en el ciclo agrupado de los siete | `9af842c` |
| 2026-08-11 | Código | **El comentario de la cabecera de `validacion.py` ya no miente, y el orden de import queda DECLARADO como requisito.** Decía que `program.py` no tiene efectos al importarse, cuando sí los tiene (`program.py:12`, `:16-23`, `:26-27`: `warnings.filterwarnings`, reconfiguración de `stdout`, `plt.style.use('default')` y `sns.set_palette`). Reescrito (`validacion.py:13-33`) enumerando los cuatro efectos y declarando la **consecuencia load-bearing**: el `import program` (`:33`) **debe quedar por encima** del bloque `plt.style.use` / `sns.set_palette` / `plt.rcParams`; movido por debajo, el `plt.style.use('default')` de `program.py` **borraría `figure.figsize`** y las 12 figuras cambiarían de tamaño **en silencio**. Documentado además que `import config` (`:55`), a diferencia de aquél, **no tiene efectos al importarse** —`ensure_dirs()` y `setup_utf8()` existen pero no se llaman a nivel de módulo—, así que su posición **no** es load-bearing. Sale en el ciclo agrupado de los siete | `9af842c` |
| 2026-08-11 | Código | **El 4,78 % / 2,44 % de outliers de D1 ya se publica como MEDIA, no como «mediana».** Se cambió el **nombre, no el cálculo**: `.mean()` sigue donde estaba (`validacion.py:978`, era `:968`) y **las cifras 4,78 % y 2,44 % siguen siendo válidas**. El rótulo del informe pasa a **«Outliers D1 (media entre características)»**, y corregidos `Resultados/GUIA_RESULTADOS.md` (`:117`, `:276-281`, `:379-381`, `:394`) e `Implementacion/PIPELINE.md:54-55`. **La verificación que importaba:** el auditor comprobó que **no se corrigió ninguna mediana legítima** por error — `cascada_invertida.py:296`, `PIPELINE.md:832,864-865,746` y `conf_mediana_argmax` **siguen intactas**. Re-corrido en las dos variantes (19:51-19:52): `git diff 6ae4554 -- Resultados/` da **una única línea cambiada por informe**, la del rótulo, y los dos `*_vocabulario_onehot.csv` **byte-idénticos**; todo lo demás igual —17 tipos 0-day, 3.750 (16,63 %), delta 77→122, KS (A: 37/54 y 44/122 · B: 25/54 y 31/122), conteos, `Integridad: APROBADA`—. Dictamen de `auditor-ml`: **APTO CON CAMBIOS**, ningún hallazgo 🔴, **ninguna cifra publicada cambia**. **Residuo que deja: el vault (`4.2:107`) sigue diciendo «mediana»** — ficha nueva 🟠 en `## Abiertas`, **antes de T10** | `84e3c8f` |
| 2026-08-11 | Código | **`COLUMNAS_CATEGORICAS` y `COLUMNAS_NO_CARACTERISTICA` dejan de estar duplicadas por copia.** **Ejecutada, no aceptada como deuda** — decisión explícita de Francisco sobre la ficha que quedó pendiente de su criterio. Son ahora **constantes de módulo** en `program.py:36-37`, y `validacion.py` las **importa** (`:100-101`, antes `:90-91`). **Camino elegido: `import program`** —fuente canónica, que es quien hace el one-hot— en vez de subirlas a `config.py`, que **sí habría violado** la restricción de `CLAUDE.md`: `program.py` y `validacion.py` no dependen de `config.py`. **La verificación que importaba:** el **orden** de la lista **no puede alterar ningún artefacto**, porque `program.py:310-311` fija `train_cols = sorted(set(D1) | set(D3))` y `:316` reindexa las tres matrices con esa lista — el orden final es **alfabético e independiente del one-hot**. Solo importa la **pertenencia**, corroborada por los CSV (38 numéricas + 39/84 dummies = 77/122) y por el contraste independiente del `.joblib`. **Sin import circular**, `argparse` bajo `__main__`, **cero `fit`**, y **los splits en disco NO se regeneraron porque no hacía falta**. Re-corrido con la ficha del rótulo (19:51-19:52), mismo diff de una línea por informe. Dictamen de `auditor-ml`: **APTO CON CAMBIOS**, ningún hallazgo 🔴. **Residuos que deja:** el alias de `:100-101` (comparte objeto lista) y el comentario falso de `:16-18` — dos fichas 🟡 nuevas en `## Abiertas` | `84e3c8f` |
| 2026-08-11 | Código | **`validacion.py:282` · La lista nominal de los 17 tipos 0-day ya se persiste en el informe.** Cerrada completando el WIP de `d9225be` **sin reescribir sus ~231 líneas**: el cambio queda confinado a `_save_report()` (`:1080-1142`). `_save_report()` ya escribe la lista nominal completa —**tipo, categoría, instancias, total y % de D2**— con **tres ramas de degradación**, así que los 0-day dejan de quedarse solo en consola, que era la deuda. **El 17 sigue siendo emergente, no una lista a mano** (`:340`), y el auditor verificó que **los 17 tipos coinciden uno a uno con `metricas_hibrido_0day.csv`**. Re-corrida en las **dos variantes**: `EXITCODE=0`, `Integridad: APROBADA`, **16 artefactos regenerados** en `Resultados/` (2026-08-11 19:28), **ningún `metricas_*.csv` y ningún `.joblib` tocados**. Con esto **queda desbloqueada la ficha del `4.2`**, que cita el informe que esta re-corrida regenera. Dictamen de `auditor-ml`: **APTO CON CAMBIOS** — los cambios salen como residuos, ninguno 🔴. Commit previo del WIP: `d9225be` | `6ae4554` |
| 2026-08-11 | Código | **`validacion.py:283` · El delta 77→122 del fix one-hot ya vive en un artefacto regenerable.** El parámetro `onehot` de `:991` **deja de ser *dead parameter***: ahora se lee y se escribe el delta **con desglose por columna categórica**, y nace el artefacto **`Resultados/specialized_nsl_kdd_vocabulario_onehot.csv`** (más su gemelo `_sin_seleccion_`), vía el helper nuevo y contiguo `_guardar_csv_vocabulario_onehot()` (`:1144-1201`). Las **~148 líneas** de `medir_vocabulario_onehot()` **no se reescribieron**. **Resultado que hay que leer bien: el delta sale 77→122 en las DOS variantes**, no 77→54 en la de 54 — **correcto por construcción y verificado en código**: el one-hot ocurre en `program.py:283`, `select_features()` se invoca **después** (`:1148-1150`) y los CSV `_original_*` se escriben **pre-one-hot** (`:650-652`). Queda **declarado en los dos informes**. **Cero literales**: el 17, el 77, el 122 y el 45 se **recuentan** (verificado por el auditor). Dictamen de `auditor-ml`: **APTO CON CAMBIOS**. Commit previo del WIP: `d9225be` | `6ae4554` |
| 2026-08-11 | Código | **`validacion.py:284` · Comparación de columnas D2/D3 por orden, re-corrida — y la incógnita se resuelve EN NEGATIVO.** Era la mitad que faltaba: el fix estaba en `d9225be` pero **nadie lo había corrido**, así que no se sabía si destapaba un desajuste real. **Ya se sabe: NO destapó ningún desajuste D2/D3.** Los CSV que deja `program.py` **ya estaban alineados posicionalmente en ambas variantes**; la comparación por conjunto **no ocultaba nada**. Es un **resultado, no un no-hallazgo**: la rama de diagnóstico «mismo conjunto, distinto orden» queda como red de seguridad, no como parche de un bug vivo. Verificado además por el auditor en la misma pasada: **cero `fit`**, salvedad del KS **impresa en ambos informes**, KS **coincidente con lo publicado** —(A) **37/54** y **44/122** · (B) **25/54** y **31/122**— y **alcance respetado**. Dictamen de `auditor-ml`: **APTO CON CAMBIOS**. Commit previo del WIP: `d9225be` | `6ae4554` |
| 2026-08-10 | Código | **T3 · Medición de la cascada invertida.** Script nuevo `Implementacion/app/cascada_invertida.py` (clase `NSLKDDInvertedCascadeMeasurer`): medición **contrafactual y fuera del sistema** que pasa las **9.711 filas normales de D2** por el clasificador de firmas **ya persistido** (`firma_RandomForest_<set>.joblib`) y cuenta cuántas condenaría con confianza ≥ `UMBRAL_CONF`. **Cero `fit`**, solo inferencia; y el umbral se lee de `hibrido_<set>.joblib::umbral_conf_elegido`, **nunca como literal** — si falta el descriptor, **aborta**. Resultados: variante **54 → 6.558 condenadas (67,53 %)**; variante **122 → 3.329 (34,28 %)**. Salida en `Resultados/metricas_cascada_invertida.csv` (**10 filas**, tabla propia: no toca ninguna de las cuatro principales) y dos figuras. **Matiz conceptual que impuso la auditoría y que manda al citar:** la fila `__global__` es una **cota inferior de falsos positivos irrecuperables**, **no** «el FPR de un sistema de firmas-primero» — en el sistema publicado `unknown` es alarma (`hibrido.py:301`, decisión P-5), así que lo que cae bajo umbral **no queda exonerado**. La lectura y los números viven en `Implementacion/PIPELINE.md`, sección «La cascada invertida (T3)». **No cierra `T9`**: solo la alimenta (viñeta `3.2.2`), y allí queda anotada la cifra con su salvedad. Dictamen de `auditor-ml`: **APTO** | `b1f1df2` |
| 2026-08-10 | Código | **T2 · KS de D1 contra los normales de D2.** Añadido en `Implementacion/app/validacion.py` **sin sustituir** el KS existente: ahora son **dos mediciones separadas y no intercambiables** — **(A)** D1 vs D2 completo: **37/54** y **44/122** características con drift; **(B)** D1 vs las **9.711 normales de D2**: **25/54** y **31/122**. `src_bytes` cae de **0,346 a 0,091** y `dst_bytes` de **0,317 a 0,107**. El `delta = (A) − (B)` se publica como **comparación, nunca como descomposición aditiva** —el KS es un supremo de diferencia de CDF y no es aditivo sobre una mezcla—, y la salvedad quedó **impresa en los dos informes de validación**. **Efecto colateral no previsto:** `validacion.py` **nunca se había corrido en la variante 122**; ahora sí, con informe nuevo (`Resultados/specialized_nsl_kdd_sin_seleccion_validation_report.txt`) y **6 figuras nuevas**. De paso aparecieron **dos cifras inventadas preexistentes** en `Resultados/GUIA_RESULTADOS.md` («34 features», «85 % de drift»), **con destino explícito a §4.2.1 y §5.1**: corregidas a **37** y **68,5 %** contra el artefacto real. Invariantes verificadas **cuatro veces** por `auditor-ml`: cero `fit`, cero recalibración, **D2 solo se reporta** (H-4/P-4 intactas); los **8 `metricas_*.csv` previos sin reescribir** (222 filas, `semilla = 42`, `commit = 1163c90`), y `CLAVE_UNICIDAD`, `_limpiar_variante_csv`, `comprobar_recuento()` y `COLUMNAS_MINIMAS` **sin tocar** — no hubo que re-correr el runbook. **No cierra `T11`**: solo la alimenta (`5.1`/`5.4`), donde quedan anotadas las cifras y la salvedad del `delta`. Dictamen de `auditor-ml`: **APTO** | `b1f1df2` |
| 2026-08-09 | — | **T0 · Retirada de la regla «lo escribe Francisco».** Aplicadas las dos velocidades de la decisión marco (b) del lote 2026-08-06. **Decisión de Francisco tomada al cerrar: `2.1.4` NO queda exceptuada** — entra en la retirada completa de `2.x`, porque exceptuar una sola nota reintroduciría a mano la regla que la decisión marco acababa de retirar del capítulo entero; **con eso T25 queda desbloqueada, y con ella T24** (el bloque de redes neuronales de `2.1.4` donde se ancla `[6]`). **Recuento real: 15 ficheros tocados (+96 −92), no las 11 ubicaciones que declaraba la ficha.** La ficha **subestimaba el alcance** y por eso hubo que barrer **por contenido, no por la lista**: las ubicaciones que faltaban no llevaban el callout literal, sino la misma regla escrita de otra forma («la redacción corresponde a Francisco», «✍ teoría (Francisco)», «en investigación por Francisco»). Una de ellas es `Obsidian_TFG_Vault/02 Marco Teórico/2.2 Ciberseguridad/2.2.1 Introducción a la ciberseguridad.md:52`: no lleva el callout «Redacción a cargo de Francisco» —eso la ficha lo había corregido bien—, pero dentro del callout de subestructura del 2026-07-15 decía «Cada una contiene un `## Guion propuesto`; la redacción corresponde a Francisco», que es la misma regla escrita de otra forma; corregida. Las otras once: (1) `CLAUDE.md`, donde la viñeta de «Reglas duras del andamiaje» pasa a bloque **«Autoría de la redacción»** con las tres velocidades — `2.x` sin restricción (`2.1.4` incluida), `6.2` borrador de agente con revisión de Francisco, `4.2` ya cedido por la decisión del 2026-07-21, y la bibliografía final en Zotero/IEEE que **sigue siendo de Francisco**; (2) este mismo fichero, cuya sección «Fuera de la lista operativa — lo escribe Francisco» se reescribe como **«Autoría de la redacción — estado vigente desde T0 (2026-08-09)»** con tabla de quién redacta qué —solo sobrevive la bibliografía de Zotero—; (3) `.claude/agents/redactor-tfg.md`, donde «Qué NO tocar» pierde el párrafo que le prohibía redactar teoría y se antepone «Autoría: qué redactas y con qué condición» — **cambio de alcance relevante: se elimina además el párrafo «Los primeros apartados del informe son investigación… Eres encargado de documentar EXCLUSIVAMENTE los resultados del código»**, porque era la misma prohibición en prosa; (4-11) el callout de las **8 notas** (`2.1.6`, `2.2.2`, `2.2.3`, `2.2.4`, `2.2.5`, `2.3.1`, `2.3.2`, `2.3.3`), que pasa de `> [!todo] Redacción a cargo de Francisco` a `> [!info] Redacción a cargo del redactor-tfg` conservando cada coletilla propia (la de `2.2.4` sobre ser la sección-motivación de la tesis, la de `2.1.6` sobre el anclaje a Guia_ML 02-03). **Dos ubicaciones más, aparecidas después de la verificación inicial:** (12) `resumen-de-decisiones.md:560`, cuya «Salvedad abierta» seguía diciendo que el choque T0/T25 sobre `2.1.4` estaba sin resolver — reescrita como **resuelta**, con la decisión de no exceptuar; (13) `Obsidian_TFG_Vault/00 Índice TFG.md`, el **MOC vivo del vault**, en **5 sitios**: el callout «Punto actual» (`:8`), la leyenda `✍ teoría (Francisco)` (`:15`), las **8 líneas de notas** del capítulo 2 (`:44-58`), la línea de `4.2` (`:72`) y la de `6.2` (`:88`) — todas reapuntadas al `redactor-tfg`. **Deliberadamente sin tocar:** `next-steps.md:382,387,421`, que está congelado y es **historial del 2026-07-15**; reescribirlo falsearía lo que se decidió entonces. **No es deuda pendiente.** **Residuo nuevo, sin ficha, señalado y no tocado:** `resumen-de-decisiones.md:459` dice «queda como divergencia a corregir por Francisco al redactar» — roza la regla retirada pero **no es la misma cosa** (habla de corregir una divergencia terminológica concreta en `2.2.4`, «detectores no supervisados», no de la autoría de un capítulo); **si merece ficha propia, lo decide Francisco.** **ANOTACIÓN DE ESTADO DEL 2026-08-11 (no es una ficha: sigue sin abrirse como tarea) — DECISIÓN APLAZADA, Y YA VAN DOS VECES.** Se le planteó a Francisco en la sesión del **2026-08-11** y **la aplazó expresamente al cerrar**, sin decidir ni ficha ni descarte. Por tanto **arrastra desde el 2026-08-09** —la sesión en que se detectó y se dejó a su criterio— y **va camino de su tercera sesión sin resolver**. La decisión **sigue siendo suya** y solo tiene **dos salidas: ficha propia en `## Abiertas` o descarte expreso** (que iría a la tabla «Descartado — no reabrir»). **Lo que NO es una salida es seguir como anotación al margen dentro de una fila cerrada**, que es exactamente donde lleva dos sesiones. **Para la próxima sesión: plantearlo ANTES de repartir trabajo**, no al cerrar — aplazarlo es lo que ha pasado las dos veces. Y las **2 notas de `Obsidian_TFG_Vault/99 Investigación/`** que dicen que `6.2` la redacta Francisco (`aprendizaje-continuo-nested-learning.md:25` y `clasificadores-tabulares-y-arquitecturas-hibridas.md:30`) **no son de T0**: quedan anotadas como trabajo de **T17**, que es quien pasa por los cuatro informes. **Fuera del alcance de T0 pero corregido en el mismo ciclo, con aprobación de Francisco:** `how-to-work.md:32` decía «no te fíes de la prosa de `next-steps.md`/bitácora» cuando desde el 2026-08-01 el registro operativo vivo es `features.md`; reescrito para nombrar los dos ficheros con su papel actual (lo detectó el `cronista` en el cierre anterior) | `d6dae35` |
| 2026-08-09 | Informe | **La línea de `4.2` en «lo escribe Francisco» quedó desfasada** (ficha abierta el 2026-08-01, marcada «la acepta o la retira Francisco»). Se retira de `## Abiertas` por absorción: **T0 la resolvió** y no le quedaba contenido propio. La prosa de `4.2` la redacta el `redactor-tfg` —el borrador de «Origen» y «Las 41 características» ya existía en la nota desde la decisión del 2026-07-21— y Francisco solo **revisa** el «por qué NSL-KDD». Su contenido restante lo cubre **T10**, que sigue abierta | `d6dae35` |
| 2026-08-09 | — | **Andamiaje · `how-to-work.md` §6 «How to» pasa a exigir recomendación de paso siguiente.** Dos viñetas nuevas (`:30-31`), justo debajo de «Pideme aprobación para cada step a ejecutar», a petición explícita de Francisco: (1) **nunca cerrar una respuesta con un menú de decisiones abiertas** para que elija a ciegas — se propone **un** paso concreto y se justifica por qué ese y no los otros candidatos; la aprobación por step **sigue siendo obligatoria**, recomendar no es ejecutar; (2) criterio de ordenación por defecto de esa recomendación: **qué desbloquea más por minuto de máquina** — lo barato que destraba varias fichas va antes que lo caro que no destraba nada. Intervención sin ficha previa en `## Abiertas`: un solo fichero tocado, +2 líneas | `e1be742` |
| 2026-08-09 | Código | **T18 · Rediseño de qué se publica en `alcance_tiempo_s`.** Los **cuatro defectos** que dejaron `0595a15` en `[PENDIENTE, NO APTO]` quedan resueltos, y con ellos el bucle de fondo: el CSV publica solo lo **estable** (qué tramos entran, cuáles no y el aviso de P9) y **todos los números viven en `PIPELINE.md`**, anclados a commits de git, editables sin re-correr. Las dos frases empíricas prohibidas —«las desviaciones observadas caben dentro de la dispersión entre corridas» y «un tramo de coste casi FIJO que no escala con el modelo»— estaban en **8/8 y 8/8 filas** y ahora salen **0/8 y 0/8**. Corrida final `1163c90`: **222 filas**, `commit` limpio, `semilla = 42`, **deriva de calidad cero** contra nueve anclas externas y sin fuga de datos. `PIPELINE.md` re-anclado a `1163c90` con todas las cifras reproducibles desde los CSV. **Efecto sobre otras fichas:** re-ancla **T20** (era falsa: 8 de 10 pares, no 4 de 4, y horquilla retirada) y refuerza **T19** (Hallazgo 7). Dictamen de `auditor-ml`: APTO. Commits previos: `ac496cb`, `1163c90` | `8fdc421` |
| 2026-08-09 | Código | **T22 · `n_iter_` del Autoencoder.** Cerrada **con la conclusión invertida respecto a lo que la ficha traía**: `n_iter_total_grid` queda registrado por fila y resulta **determinista** — **162** a 54 características y **128** a 122, idénticos en las dos corridas que lo registran (una de ellas no reproducible desde git). Con las épocas congeladas, el wall-clock del Autoencoder se mueve **1,29× y 3,63×** entre corridas: esa variación es **carga de máquina, no épocas**, que era justo lo que la ficha no podía decidir. El cociente s/época **no separa nada** al tener denominador fijo. Y el eje **54-vs-122 es indecidible con este diseño** sin medidas repetidas: eso es un **resultado**, no una tarea pendiente. Dictamen de `auditor-ml`: APTO. Sale con T18 (`ac496cb`, `1163c90`) | `8fdc421` |
| 2026-08-09 | Informe | **Auditar la bibliografía** (ficha abierta el 2026-08-01). Se retira de `## Abiertas` por absorción: **T15 la cubrió por completo** —cita completa y nivel declarado en las 10 entradas, `[9]` retirada, `[1]` sustituida, `[2]` y `[8]` completados con año y editorial— y no le quedaba contenido propio. Se resolvió en `396e283`; no genera trabajo nuevo más allá de los residuos **T23**-**T25** que ya dejó T15 | `396e283` |
| 2026-08-09 | — | **T15 · B1: auditoría de `Bibliografía.md` cerrada.** Las **10 entradas** con cita completa y **nivel declarado** (8 de nivel 1; `[2]` Anderson 1980 queda en **nivel 2** y no hay forma de subirlo). `[9]` **retirada sin renumerar** (copia no autorizada del mismo Stallings de `[8]`, y hoy además exige login); `[1]` **sustituida** por la nota de prensa oficial de INCIBE (**97.348 incidentes en 2024, +16,6 %**), y `[2]` y `[8]` completados con año y editorial. Formato migrado a **tabla de staging**. **0 entradas añadidas**: el volcado de las ≈40 fuentes es **T16** y va después de la redacción. Informe en `Obsidian_TFG_Vault/99 Investigación/Auditoría de Bibliografía.md`. Residuos dados de alta: **T23**, **T24**, **T25** | `396e283` |
| 2026-08-08 | Código | **T1 · Nivel 1: esquema de métricas.** Cerrada en su objetivo, con residuos anotados (`T18`-`T22`). Las **8 tablas regeneradas**, tres corridas del runbook completo; las publicadas son las de `5f98d88`, producidas por el código `5516b60`: `commit` limpio y `semilla = 42` en las **216 filas**, recuentos 8/8/2/2 y 16/36/144/6, **cero deriva en métricas de calidad**, sin leakage y sin valores imposibles. Esquema nuevo: `bin_accuracy` en `metricas_baseline.csv`, campo **`alcance` por fila** en las cuatro tablas (cierra C3 y C6 — `accuracy_D2` era columna homónima con dos alcances: 0,9683 en firmas, 0,7395 en baseline), columnas `semilla` y `commit`, conjunto mínimo obligatorio de columnas, `_limpiar_variante_csv` subido a `evaluacion.py` con `CLAVE_UNICIDAD` declarada (variante × algoritmo × alcance), y **tiempo de inferencia separado del de entrenamiento** con latencia por flujo y flujos/s. Además, no previsto en la ficha: **todos los cronómetros pasados de `time.time()` a `perf_counter`** (`time.time()` tiene ≈15,6 ms de resolución en Windows y publicaba `latencia_ms_por_flujo = 0.0` con caudal vacío en DecisionTree); **guarda única** para latencia, caudal y FPR — un valor no medible da **celda vacía, nunca `0.0`**; y `tiempo_s`, que significaba **tres cosas distintas según la tabla** sin que el dato lo dijera, ahora declara su `alcance_tiempo_s` por fila. **Hallazgo mayor:** el residual `tiempo_s − entrenamiento − inferencia` llegaba al **49 % en OneClassSVM-54** y estaba sin declarar; la etiqueta lo llamaba «figuras», que son décimas de segundo. Medido y cerrado con dos columnas nuevas en `metricas_anomalias.csv` (`tiempo_score_seleccion_s`, `tiempo_score_umbral_s`): el grueso es **el scoring repetido dentro de la selección de hiperparámetros** —el script pasa por el scorer 5-7× más filas eligiendo config que evaluando— y en OCSVM-54 ese tramo **iguala al propio ajuste**; no entraba en `tiempo_entrenamiento_s` porque no es `fit`. Declarado que **`latencia_ms_por_flujo` mide solo `predict`/`score`** sobre características ya calculadas y en memoria, sin captura ni extracción de features: sin esa frase, citar el caudal como capacidad operativa sería la *Lab-Only Evaluation* que denuncia P9 (la mitad que falta → `T21`). **Corrección de lo que esta ficha afirmaba mientras estuvo abierta:** era **falso** que «ningún resultado publicado cambia: solo cambia el esquema de columnas» — no cambia **ninguna métrica de calidad** (semilla 42, modelos y calibración OOF intactos), pero **las columnas de tiempo sí cambian de valor**, por el paso a `perf_counter` y por la varianza de máquina, y cambia el `alcance` de las 16 filas de `metricas_balanceo.csv`. Decisiones de diseño internas → `T17`. **Cuatro pasadas de `auditor-ml`**; dictamen sobre las tablas publicadas: T1 puede cerrarse en track Código. Commits: `077119e`, `38fdd4b`, `34bee30`, `5516b60`, `5f98d88` | `5f98d88` |
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
