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
>
> **Refactorización integral autorizada por Francisco el 2026-08-13.** Excepción **puntual** al
> invariante de edición quirúrgica del `cronista`: se reorganizó y compactó el fichero entero para
> eliminar contradicciones acumuladas por capas. **No es precedente.** El histórico retirado vive en
> git, en el commit anterior a este ciclo (último commit: **`9d4c26d`**, con el estampado de ese hash
> en su ficha cerrada encima, sin commitear). **No existe `features-historico.md` y no se crea.**

Estados: `[ ]` pendiente · `[~]` en curso · `[!]` bloqueado
Fechas absolutas `AAAA-MM-DD`. Track: **Código** / **Informe**.

---

## PRÓXIMOS PASOS — próxima sesión

> Derivado del «Plan de cierre» de más abajo. **Orden de ejecución, no estado**: lo abierto sigue
> siendo lo que está en `## Abiertas`.

> **Dónde queda la sesión del 2026-08-13: la Fase 0 está EN CURSO.** De las decisiones, la **1 (rango
> de FPR)** y la **3 (automatizar el «13 de 98»)** están **resueltas**, y la **Tarea B queda APLICADA**
> (`c5ceca5`). **La Fase 4 ya NO está bloqueada por el andamiaje**: la prohibición derogada seguía viva
> en `leader.md` y se retiró el 2026-08-13 (`0fb5f2b`) — era la razón estructural de que las 8 notas
> del capítulo 2 llevaran semanas en guion. La Fase 4 se ejecutará en **tandas de 3-4 notas en
> paralelo**.
>
> **El `push` está PENDIENTE:** hay **8 commits en local sin subir** — `ea35ce3`, `dbba05e`, `ddade37`,
> `9d4c26d`, `0fb5f2b`, `6bfc779`, `c5ceca5` y el que cierre este registro. Falla por **autenticación
> desde el harness**, así que **lo tiene que lanzar Francisco**.

**Tanda 0 — decisiones de Francisco (cero cómputo, va primero).** Sin ellas, tres tandas posteriores
arrancan a medias. **La Tarea B ya no está aquí: aplicada el 2026-08-13** (`c5ceca5`). Quedan las
**seis** de la tabla del plan de cierre —eje de balanceo de `4.3.4`; ¿se regeneran los splits?;
permiso de escritura en `resumen-de-decisiones.md`; acceso institucional; alcance de los tres
`grill-me`; título del TFG— **más las dos altas nuevas del 2026-08-13**: la **granularidad del commit
bajo despacho en paralelo** (**a decidir ANTES de la Fase 4, no dentro**) y la **divergencia de
`resumen-de-decisiones.md:459`**, que solo tiene dos salidas: ficha o descarte expreso.

**Tanda 1 — barrido de correcciones de una línea. Dos ciclos EN PARALELO, uno por track** (ficheros
distintos, agentes distintos). Precondición: ninguna.
- **Código** (`ml-implementador` → `auditor-ml`): `warnings.filterwarnings('ignore')` en
  `program.py:12` y `validacion.py:57` (**no `validacion.py:21`, que es comentario**) + nota fechada
  en `resumen-de-decisiones.md:820-821`.
- **Informe** (`redactor-tfg`): `4.2:105`, el sello de `4.2:145`, **T20** (desbloquea T9) y, **en
  serie y solo `researcher`**, las tres correcciones de `Bibliografía.md:32`, `:86` y
  `Auditoría de Bibliografía.md:140` (T25).
- **Aplicar la Decisión 1 del FPR** en sus cuatro sitios (`4.2:120`, `A.2:69`, viñetas de T9 y T11)
  **en la misma pasada**: ya es instrucción vigente, no decisión pendiente.

**Tanda 2 — `A.3` y cierre de T4.** Precondición: nada; el «13 de 98» ya está automatizado
(`9d4c26d`). Crear **`A.3` (T7)** pegando `Resultados/dispersion_semillas.md` con sus tres
salvedades → con eso **queda servido T11** → y **T4 se puede cerrar**. `redactor-tfg`, en serie
respecto a T11.

---

## Abiertas

- [ ] **Diagrama y README de agentes describen la arquitectura anterior** · Código · `ml-implementador`
  Detectado el 2026-08-01. `Implementacion/diagramas/README.md:10` y
  `Implementacion/diagramas/03_orquestacion_agentes.mmd` documentan el ciclo «orquestador →
  implementador → auditor/ejecutor → redactor → cronista → `next-steps.md`», cuando hoy la
  entrada es el `leader` con carriles y tracks (`CLAUDE.md`, «Arquitectura de agentes») y
  `next-steps.md` está congelado: el roadmap vivo es `features.md`. Regenerar `.png` y `.svg` si
  se toca el `.mmd`. **La acepta o la retira Francisco.**

- [ ] **Preliminares: título, resumen y abstract** · Informe · `redactor-tfg`
  Se redactan **al final**, cuando el resto de capítulos esté cerrado.
  Notas: `00 Preliminares/Resumen.md` y `00 Preliminares/Abstract.md`.
  - **Ampliada el 2026-08-12** a partir de `mis-apuntes-del-informe.md:5` (el **resumen no está
    escrito** y Francisco pide propuesta; el **abstract** es ese mismo texto en inglés) y
    `mis-apuntes-del-informe.md:7` (**falta el título del proyecto**). Ese fichero es
    **incremental**: al ejecutar esta ficha hay que **releerlo entero** y no fiarse de lo anotado
    aquí, que es el estado del **2026-08-12**.
  - **El título es decisión de Francisco, no de un agente:** un agente puede **proponer
    candidatos**, no fijarlo.

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
  10 semillas × **5 scripts** (`cascada_invertida.py` entra también) × 2 sets de características.
  **Duración medida del barrido: 2026-08-12T22:09 → 2026-08-13T00:38, ≈2 h 29 min** — es la única
  cifra de duración citable.
  - **La parte de CÓMPUTO está CERRADA** (barrido corrido y agregado, ver `## Cerradas`, `9ad971b`).
    Lo que queda vivo de T4 es el **consumo del resultado en el informe**: la tabla de dispersión de
    `A.3` (**T7**) y los párrafos de `5.2`/`5.4` (**T11**). **T4 no se cierra hasta que esos dos
    consuman la banda.**
  - **Los titulares de 5.1-5.3 siguen siendo los de la semilla 42.** La dispersión (media, sd, mín,
    máx) entra como tabla nueva en `A.3` más un párrafo en `5.4`. **No se reescribe el capítulo.**
  - Cierra los ítems FT *number of runs*, *error bars* y *central tendency* de Pineau et al.
  - **Sin p-valor, con la renuncia declarada y su razón: 10 puntos sobre un único dataset no
    sostienen un contraste.** Declarar la renuncia **cumple** el ítem *statistics*; callarla no.
  - **Objetivo real, YA RESPONDIDO por el barrido:** dos decisiones cerradas descansaban en huecos de
    1-2 pp medidos con n=1 — RandomForest 0,822 vs HistGradientBoosting 0,804 (firmas) y Autoencoder
    vs IsolationForest (anomalías). **El primero solapa** —hay que decirlo y **no establecer el
    orden**— y **el segundo aguanta**. Detalle y forma de escribirlo, en la viñeta `5.2` de **T11**.
    Es un hallazgo para `5.4`, no un desastre.
  - **Aviso heredado de T1 (cerrada el 2026-08-08):** T4 **no puede escribir en las cuatro tablas
    principales** — choca contra el borrado por variante, la `CLAVE_UNICIDAD` sin `semilla` y su
    recuento fijo. Por eso la dispersión va a **tabla nueva** en `A.3`. Ya está escrito en
    `PIPELINE.md` y en el docstring de `comprobar_recuento()`.
  - **El lanzador del barrido exige CINCO recuentos por (variante, semilla): 4/4/1/1/5** — las 5
    filas de la cascada invertida entran también (`barrido_semillas.py:107-109`).
  - **Dispersión del wall-clock:** hasta **4,8× entre corridas en máquina no dedicada** con calidad
    idéntica al bit (Autoencoder-54: 37,71 → 181,91 s), y **con el recuento de épocas idéntico** —
    `n_iter_total_grid` es **determinista** (162 a 54 · 128 a 122), así que es **carga de máquina, no
    épocas**. Las columnas de tiempo de las 10 semillas **no** se leen como propiedad del algoritmo
    sin declarar esa dispersión.
  - **Estado del barrido verificado en disco:** corrido y **agregado** — **2.320 filas**, **20/20
    celdas** (10 semillas × 2 variantes), sello `df30cb2` único y limpio;
    `Resultados/dispersion_semillas.csv` y `.md`, **198 filas**, `sd` muestral `ddof=1`.
  - **El andamiaje de semilla (flag `--semilla N`, nueve tablas `*_semillas.csv`, lanzador reanudable
    y agregador) está cerrado y auditado**, con los **ocho hallazgos aplicados el 2026-08-12**: borrado
    de `.joblib` por semilla tras `hibrido.py` y `cascada_invertida.py`; `SEMILLAS_BARRIDO = [1..10]`
    en `config.py` (42 **fuera** a propósito); agregador nuevo `Implementacion/app/agregar_semillas.py`;
    `Resultados/figuras/*_semilla*` excluido en el `.gitignore` raíz; tabla «qué SÍ varía dentro de
    cada semilla» en `PIPELINE.md`; traza `Resultados/verificacion_semilla_joblib.txt` (**20/20
    `.joblib` publicados con `semilla = 42`**); salvaguarda simetrizada en
    `cascada_invertida._leer_umbral_conf`; y `--semilla` documentado en los cinco scripts, `README.md`
    y `GUIA_RESULTADOS.md`. Cifras medidas: `Resultados/modelos/` **481,33 MB**, el barrido **200
    modelos ≈ 4,8 GB**, **65,2 GB libres** en C: — el espacio **no** es blocker, y los `.joblib` del
    barrido se borran por semilla por higiene, no por falta de sitio.
  - **LÍMITE DEL DISEÑO, a declarar en `A.3` (T7) y en `5.4`/`5.2` (T11):** `program.py` **no está
    parametrizado** —su `random_state=42` es literal y no importa `config.py`—. Las 10 semillas miden
    dispersión **de los modelos sobre splits D1/D2/D3 y set de características FIJOS**: **no**
    incluyen variabilidad del preprocesado ni de la selección de características. Escribirlo así, no
    como «dispersión del sistema».
  - **El runbook del barrido está en `Implementacion/PIPELINE.md`, sección «Runbook del barrido de
    semillas»**, y es lo que hay que teclear para relanzar. Su **paso 2** exige que
    `Get-ChildItem -Recurse ..\Resultados -Filter *_semilla*` salga **VACÍO** antes de lanzar,
    **excluyendo `verificacion_semilla_joblib.txt`** —esa traza casa con el patrón, está versionada y
    es permanente—: cualquier corrida interrumpida repone residuos `*_semilla*` y la reanudación los
    tomaría como celdas ya hechas.
  - **🟡 La rama del agregador «1 semilla de 10» sigue sin ejercitarse en ejecución** — solo auditada
    su lógica; llegar a ella exige correr `anomalias.py` y `firmas.py` de una semilla entera. **Lo
    asume o lo cubre Francisco.**
  - **Historial de los tres pasos previos, los tres HECHOS y verificados** (2026-08-12/13):
    1. **Residuo `_semilla1` borrado** — 11 ficheros (6 figuras `*_54_semilla1*`, 4 `.joblib`
       `anomalia_*_54_semilla1` y `metricas_anomalias_semillas.csv`), con OK explícito de Francisco y
       **antes del commit `54d1349`**. Verificado en disco después: el único fichero de todo
       `Resultados/` que casa con `*_semilla*` es la traza `verificacion_semilla_joblib.txt`, y lo
       publicado quedó intacto (20 modelos, 39 figuras, 9 tablas).
    2. **Ensayo de humo rematado:** los tres puntos que faltaban **PASAN** — salvaguarda de mezcla de
       semillas (aborta con exit 1 y escritura cero), reanudación sin duplicar filas (10 corridas → 9
       con 1 saltada; tablas en 1 y 18 filas tras relanzar, no en 2 y 36) y el agregador aborta (por
       la guarda de tabla inexistente, `agregar_semillas.py:235`). En el mismo pase se escribió el
       **runbook del barrido**, que no existía, con puntero desde `README.md`.
    3. **Barrido lanzado y agregado**, con dictamen **APTO** de `auditor-ml` a la tercera pasada. Las
       cifras están en «Estado del barrido verificado en disco», arriba.
    - **Las cargas de `.joblib` ausente ya dan mensaje accionable** (`hibrido.py:200-219`,
      `cascada_invertida.py:198-213`): relanzan `RuntimeError` con ruta, script previo, variante con su
      flag y semilla, y **siguen abortando con exit ≠ 0 y escritura cero**.
    - **Dato de un solo punto, no concluyente pero del mismo signo:** a semilla 1, Autoencoder
      `f1` **0,8632** / `accuracy` **0,8520** frente a IsolationForest `f1` **0,8226** / `accuracy`
      **0,8157** — **mismo signo que el hueco publicado** con la 42, que en `accuracy` es
      **0,8605 vs 0,8257** y en `f1` **0,8716 vs 0,8341** (`Resultados/metricas_anomalias.csv`, set 54).
      El signo se sostiene en las dos métricas. **No sustituye al barrido.**
      → **Aviso de procedencia, y no es formalismo:** estas cuatro cifras de la semilla 1
      **no son verificables desde git por un tercero**. El CSV que las respaldaba
      (`metricas_anomalias_semillas.csv`) se borró como residuo y **nunca se commiteó**, así que no
      hay ninguna coincidencia de `0.8632|0.8520|0.8226|0.8157` en el repositorio. Sirven como
      indicio interno para decidir; **no valen como evidencia citable en la memoria**. Las de la 42 sí
      están en disco y versionadas.

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
  → **La tabla de dispersión de T4 YA EXISTE:** `Resultados/dispersion_semillas.md` es el artefacto a
    pegar (`.csv` al lado), **198 filas**, `sd` muestral `ddof=1`, con **sección propia del recuento
    «fuera de banda» de la semilla 42**. Cuatro cosas al pegarla:
    - **Rotular `alcance` y `tabla_origen`** — sin ellas «`54 | RandomForest`» nombra a la vez al
      clasificador de firmas y a la cascada invertida, que fue el bug corregido en el agregador.
    - **Declarar el alcance:** dispersión **de los modelos sobre splits y set de características
      FIJOS**, no «del sistema».
    - **El sello impreso en el artefacto es `commit_agregador = ddade37-sucio`, que es pre-commit.**
      **T7 cita el sello RE-ANCLADO al commit de este ciclo, y no se inventa el hash.** El artefacto
      **no se regenera**: lo estampa `config.commit_actual()` y no puede llevar el hash del commit que
      lo versiona. El re-anclaje tiene **ficha propia abierta**.
    - **Pegar las TRES SALVEDADES del «13 de 98»**, que **ya se puede citar** (automatizado en
      `9d4c26d`): (i) el 13 sale con los **extremos SIN redondear** y la **igualdad contando como
      dentro**, simétrico en ambos extremos —con mín/máx a 4 decimales salen **14**, porque `f1_u2r`
      de RandomForest en 122 tiene la 42 en **0,318182**, exactamente en el mínimo—; (ii) **10 de las
      98 celdas son umbrales**, no métricas sobre D2: descontarlos daría denominador **88**, y **una
      de las tres celdas de borde que deciden el recuento es un umbral**; (iii) **titular y banda NO
      salen del mismo commit** —semilla 42 de `1163c90` (94 celdas) y `274923d-sucio` (4, la cascada
      invertida), bandas de `df30cb2`—, así que parte de la distancia podría ser **deriva de código,
      no dispersión por semilla**: es **salvedad de procedencia, no invalidación**.
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
    122. **Se cita como COTA INFERIOR de falsos positivos irrecuperables, NO como «el FPR de un
    sistema de firmas-primero»**: en el sistema publicado `unknown` es alarma (decisión **P-5**,
    respaldada **por símbolo: `hibrido.py::_ensamblar_prediccion`**), así que lo que cae bajo umbral no
    queda exonerado. Lectura, tabla y forma de citarlo en `Implementacion/PIPELINE.md`, sección «La
    cascada invertida (T3)».
  - `3.2`/`3.6`: la divergencia declarada. En ADAM la etapa 2 etiqueta «falsa alarma» y **la filtra**;
    aquí se le prohíbe por diseño (H-5, P-5). Matiz: H-5 es correcta *dentro* de su premisa, pero su
    redacción actual puede leerse como si **toda** cascada anomalía→firmas tuviera esa propiedad, y
    no es así: la tienen las cascadas cuya etapa 2 carece de clase `normal`, que es una **elección**.
  - `3.3`: Mitchell et al. (el recall 0-day por tipo **es** evaluación desagregada, con nombre y
    precedente) + Scheirer et al. (`unknown` es formalmente *open-set recognition*, lo que justifica
    reportar la tasa de enrutado como métrica propia con su alcance — decisión H-6).
  - `3.4`: Sommer y Paxson, verbatim: entrenar solo con normal es obligado para aspirar a lo novedoso,
    y **cuesta** —«exige tener un modelo *perfecto* de normalidad»—. Es la explicación teórica del FPR
    del híbrido, que se cita **por variante: 10,2 % en 54 y 8,5 % en 122** (`metricas_hibrido.csv`,
    `bin_fpr`), **nunca como rango redondeado**. No es un defecto del autoencoder.
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
  - `4.2:72` · **el «~33 %» de DoS en D2 está mal referido** (anclado aquí el **2026-08-12**, salido de
    la auditoría del despacho de las dos fichas del `4.2`; **no abre ficha propia porque es
    preexistente y cae de lleno en el alcance de T10**). Ese ~33 % es sobre **D2 entero**, no sobre
    **sus ataques**: sobre los ataques de D2 el DoS es el **58,1 %**. Al redactar, decir **sobre qué
    denominador** se da cada porcentaje.
  - `4.3`: C5 sin fuga con las cuatro líneas verificadas (Kapoor y Narayanan; P3/P5 de Arp et al.) y
    el peso del one-hot: **84 de 122 características (69 %) vienen de la codificación**, 70 de ellas
    de `service` sola; de las 60 eliminadas por importancia, **58 son *dummies*** → la selección de
    4.3.5 es en la práctica un mecanismo de poda del one-hot de `service`.

- [ ] **T11 · Capítulo 5** · Informe · `redactor-tfg`
  - `5.2` · **dispersión de T4, YA MEDIDA: los intervalos RF/HGB SÍ se solapan, así que hay que
    escribir que el orden NO queda establecido.** `f1_macro` RF-54 **[0,7779–0,8205]** vs HGB-54
    **[0,7680–0,8327]**, y el **máximo de HGB supera la media de RF**; como observación **pareada**,
    RF gana en **8 de 10** semillas. Tres cosas más que este capítulo tiene que absorber:
    (a) **el titular publicado de firmas (54-RF `f1_macro` 0,8223) es el punto más favorable de once
    corridas** —por encima del **máximo** de las diez semillas (**0,8205**), media **0,8035**—, así
    que **la banda va junto al titular**, y en **122** el mismo modelo cae **al otro lado**; (b) el
    hueco **Autoencoder vs IsolationForest SÍ aguanta** (bandas **disjuntas** en `f1`, AE **10 de
    10**), pero el contraste publicado **0,8605 vs 0,8257** son *accuracies* y `accuracy` **no está en
    la lista cerrada de `ESPECIFICACION` para anomalías**: **no figura en la tabla de dispersión**,
    cítese por `f1`; (c) **la semilla 42 cae fuera de la banda en 13 de 98 celdas** — recuento
    **automatizado** (`9d4c26d`), que **sale del artefacto** y **se puede citar**, con las **tres
    salvedades detalladas en T7**, que van escritas al lado y no omitidas.
    Y **la decisión de balanceo de `4.3.4` no es constante entre semillas** (`class_weight` gana en
    **17 de 40** celdas de DecisionTree/RandomForest, estando cerrada con **n=1**): tiene **ficha
    propia** en «Residuos del cómputo de T4» y **la decide Francisco**. **T11 no la resuelve: la
    consume** cuando Francisco decida.
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
    de FPR y el real es **10,2 % en 54 y 8,5 % en 122** (`metricas_hibrido.csv`, `bin_fpr`); el exceso
    tiene explicación medible **sin necesidad de reloj**.
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
  Acompaña cada cierre del lote. **Parcialmente cubierta:** el volcado a `resumen-de-decisiones.md`
  está hecho (§ Decisiones del 2026-08-06 y del 2026-08-09, más sus dos entradas de bitácora) —
  reapertura declarada del track de código con alcance y motivo, retirada de la regla de autoría en
  dos velocidades, criterio rector del lote, renuncia al p-valor, anclaje de `[6]` en `2.1.4` con sus
  tres descartes, y las conclusiones de diseño de T18 y T22.
  **Sigue pendiente, y es lo que mantiene la ficha abierta:**
  1. El bloque «Decisiones tomadas a partir de este informe» en **cada uno de los cuatro informes** de
     `Obsidian_TFG_Vault/99 Investigación/`, con qué se convirtió en decisión y qué se descartó. En la
     misma pasada se corrige que **dos de ellos siguen diciendo que `6.2` la redacta Francisco**
     (`aprendizaje-continuo-nested-learning.md:25` y
     `clasificadores-tabulares-y-arquitecturas-hibridas.md:30`), cuando la decisión marco (b) la pasó
     a **borrador del `redactor-tfg` con revisión final de Francisco**.
  2. La **deriva de documentación de `evaluacion.py`**: su contrato cambió con T1 y sigue descrito en
     la forma anterior en `CLAUDE.md:63`, `next-steps.md:621`,
     `resumen-de-decisiones.md:319,343` y `Guia_ML\03_validacion_y_metricas.md:153`.

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
  dedicada** (Autoencoder-54: 37,71 → 181,91 s, con **calidad idéntica al bit**) y **con el recuento de
  épocas idéntico** —`n_iter_total_grid` es determinista—. Estas cifras **no deben citarse como
  propiedad del algoritmo** sin declarar la dispersión.
  **Lo que debe sostener el capítulo es el Hallazgo 7:** los segundos absolutos **no son reproducibles
  entre corridas**, pero **el reparto interno del bloque se mueve como mucho 4,5 pp y conserva el orden
  de las ocho filas**. Es una afirmación mucho más defendible que cualquier cifra en segundos.

- [ ] **T20 · Reformular el argumento de T9 («HistGB tarda más que RF»)** · Informe · `redactor-tfg`
  El par **`68,7 / 54,8`** de la viñeta `3.5` de **T9** y del informe tabular **no existe en ningún
  artefacto**: no se usa.
  **Lo medido:** son **8 de 10 pares** intra-corrida en el mismo sentido, con los **dos contraejemplos
  ambos en la variante de 54** (2 de cada 5 corridas invierten ese par), así que **no hay horquilla que
  citar** y la afirmación **solo es sólida en la variante de 122**. Sigue siendo **coste de
  entrenamiento**, y **en inferencia a 54 características el orden se invierte**: HistGB **0,0032
  ms/flujo** frente a RF **0,0072**. Y sigue **sin ganar `f1_macro`** (0,804 vs 0,822).
  **La dirección aguanta y la prosa del vault no se toca**; lo que era falso es la formulación.
  **La formulación correcta y anclada está en `PIPELINE.md:493-498`** —el bloque que empieza «**Lo
  citable, y ni una palabra más**»—, y es la que debe usarse.

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
  - **T25 está desbloqueada:** la prosa de `2.1.4` —incluido el bloque de redes neuronales que abre
    **T24**— la redacta el `redactor-tfg`; `2.1.4` **no** queda exceptuada de la retirada de la regla
    de autoría (decisión de Francisco del 2026-08-09).
  - **Pendiente para el `researcher`, en ciclo propio:** actualizar la columna «Dónde se usa» de
    `Bibliografía.md:32`, retirar el aviso de `Bibliografía.md:86` si ya no procede, y corregir el
    error de `Obsidian_TFG_Vault/99 Investigación/Auditoría de Bibliografía.md:140`, que afirma que
    «`[6]` se usa bien en otros sitios y se queda» — **es falso**.

### Migración de `next-steps.md` §3.2 — altas del 2026-08-11

> Las dos fichas siguientes salen de la **migración de la deuda técnica de `next-steps.md` §3.2**,
> hecha el **2026-08-11**: eran casillas `☐` dentro de un fichero congelado, donde nadie las miraba.
> **§3.2 y §3.3 quedan como historial**, sin reescribir ni una casilla; el estado vivo de lo que siga
> abierto es **este**.
>
> De las **cinco** fichas migradas, **tres están cerradas** (ver `## Cerradas`): las de
> `validacion.py`, completadas sobre el código WIP de `d9225be` **sin reescribir sus ~231 líneas** y
> **re-corridas en las dos variantes** (`EXITCODE=0`, `Integridad: APROBADA`, 16 artefactos
> regenerados el 2026-08-11 19:28). También se cerraron las **constantes duplicadas** —Francisco
> decidió ejecutarlo, no aceptarlo como deuda—: son ahora de **módulo** en `program.py:36-37` y
> `validacion.py` las importa. **Quedan las dos fichas de abajo.**

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

### Residuos del despacho de `4.2` — altas del 2026-08-12

> Salen del cierre **en una sola pasada de `redactor-tfg`** de las dos fichas de
> `Obsidian_TFG_Vault\04 Implementación del sistema\4.2 Base de datos utilizada.md` (la «mediana» de
> `:107` y el KS (B) de `:110`), con dictamen **APTO CON CAMBIOS** de `auditor-ml`: sin leakage, sin
> cifras caducadas, sin hash inventado y sin invadir T10. **Ninguno de estos residuos es 🔴.** La
> cuarta observación de esa auditoría —el «~33 %» de DoS de `4.2:72`, que está sobre D2 entero y no
> sobre sus ataques (**58,1 %**)— **no abre ficha: es preexistente y queda anclada dentro de T10**.

- [ ] **Las figuras de validación de `assets\` van por detrás de `Resultados\figuras\`** (🟠) · Informe · `redactor-tfg`
  Dos mitades del **mismo** trabajo —copiar de `Resultados\figuras\` a `Obsidian_TFG_Vault\assets\` y
  embeber—, por eso van en **una sola ficha**:
  1. `Obsidian_TFG_Vault\assets\validacion_drift_ks.png` es de una **corrida anterior** (sus rótulos
     no llevan el «(A)») mientras el callout de la nota la da por **vigente**. **Las cifras coinciden,
     así que no invalida nada de lo escrito**; hay que **re-copiarla** desde `Resultados\figuras\`.
  2. **Las figuras de (B) existen en `Resultados\figuras\` pero NO están en `assets\`**, así que la
     pasada del 2026-08-12 **no pudo embeberlas** y dejó un **`> [!todo]` vivo** en la nota. Ese
     `[!todo]` se retira **al copiarlas y embeberlas**, no antes.
  - **Va ANTES de T10**, por el mismo motivo que iban sus dos fichas madre: si T10 vuelca `4.2` tal
    cual, publica una figura que no corresponde a la medición que el texto describe.

- [ ] **Dos imprecisiones de una línea en `4.2` que la auditoría dejó señaladas** (🟡) · Informe · `redactor-tfg`
  Las dos son **texto**, en la misma nota, y **no exigen re-correr nada**:
  1. **`4.2:120` · el rango de FPR — DECISIÓN 1 APROBADA por Francisco el 2026-08-13. Es INSTRUCCIÓN
     VIGENTE, ya no está bloqueada por ninguna decisión.**
     - **Se retira «8,5-16 %»**: era de **otra tabla y otra columna** —`metricas_anomalias.csv`,
       columna `fpr`, los cuatro detectores de anomalías **sueltos**, con el extremo alto puesto por
       **LocalOutlierFactor (16,6 %), que fue DESCARTADO**—.
     - **Se retira también el rango redondeado «8-10 %»**, que redondea **10,17 a la baja** y deja el
       valor real fuera. Lo citable es **la cifra por variante: 10,2 % en 54 y 8,5 % en 122**
       (`Resultados/metricas_hibrido.csv`, columna `bin_fpr`).
     - Si además se cita la **banda entre semillas**, es **4,9-10,7 %** y va **rotulada como otra
       cosa**, no fundida con las anteriores.
     - **Cuatro sitios, y los cuatro en la MISMA pasada:** `4.2:120`; `A.2:69` —que además **remite a
       `5.1`**, así que el apéndice se contradice con su propia referencia—; y las viñetas `3.4` de
       **T9** y del KS de **T11** de este fichero, **ya aplicadas aquí**.
     - **Texto vivo que arrastra el rango y que esta ficha de track Informe NO absorbe:**
       `Resultados\GUIA_RESULTADOS.md:219` y los comentarios de
       `Implementacion\app\validacion.py:548,620` — esto último es **código y exige `auditor-ml`**, por
       su propia vía.
     - **Congelado o registro histórico, NO se toca** (son foto de su fecha):
       `next-steps.md:178,370,451`, `resumen-de-decisiones.md:346,580`, `EL_FUTURO.md:96`,
       `sesion-2026-07-06.md:66`, `Guia_ML\04_los_tres_modelos.md:35` y los tres informes de
       `Obsidian_TFG_Vault\99 Investigación\`, que **no es memoria**.
  2. **`4.2:105`** — acota el **ranking** a la variante de **54** cuando es **idéntico en ambas**.
     Basta con retirar la acotación.

### Residuos del clúster de `PIPELINE.md` — altas del 2026-08-12

> Salen del cierre **en una sola pasada** de las **cinco fichas de `PIPELINE.md`** (ver
> `## Cerradas`), con dictamen **APTO CON CAMBIOS** de `auditor-ml`, todo aplicado. **Documentación
> pura: ningún script de `app/` tocado, ninguna corrida, ninguna cifra publicada movida.** **Ninguno
> de estos residuos es 🔴.**
>
> **Anclas vigentes de `PIPELINE.md` tras ese cierre, contadas en disco el 2026-08-12** (el fichero
> creció ~40 líneas): tabla canónica del sello en **`:994`** (encabezado) + **`:1001-1005`** (valores);
> glosa del `-sucio` en **`:186-190`**, colgando de su primera aparición en **`:184`**; las tres filas
> de la tabla de corridas en **`:369-371`**; y el bloque citable de **T20** en **`:493-498`**.

- [ ] **`resumen-de-decisiones.md:820-821` sigue afirmando en presente que el aviso de re-anclaje se mantiene** (🟠) · Código · `ml-implementador`
  Es el **punto 5 de la auditoría, el único que quedó sin aplicar**: el `ml-implementador` se declaró
  **sin permiso para escribir en ese fichero** en esa pasada. La entrada del `2026-08-11` (procedencia,
  residuo 5) dice «**El aviso de re-anclaje de `PIPELINE.md` se mantiene igualmente**», y **ya no se
  mantiene**: el re-anclaje está hecho y el commit es `9af842c`.
  - **Cómo se arregla, y solo así: nota fechada que la supera, sin reescribir el texto histórico** —
    es la convención que el propio fichero ya usa en **`:805-808`**.
  - **No basta con la entrada del `2026-08-12` (`:824-834`)**, que dice haber añadido «arriba, dentro
    de la entrada de procedencia» una nota fechada: la nota que existe está en **`:657-664`**, en otra
    sección, y **no cubre `:820-821`**.
  - **Es la enésima recaída del defecto reincidente del proyecto** (afirmar en presente algo que ya no
    respalda el estado del repo), esta vez en su forma de **texto que no se actualizó**.

- [ ] **El vault sigue diciendo «pendiente de re-anclaje» del sello `fc1c6b4-sucio`** (🟡) · Informe · `redactor-tfg`
  `Obsidian_TFG_Vault\04 Implementación del sistema\4.2 Base de datos utilizada.md:145` conserva el
  callout de procedencia con «**pendiente de re-anclaje al commit de cierre**». Es la **cuarta copia
  viva** del aviso: las otras tres (`PIPELINE.md`, `GUIA_RESULTADOS.md`, `resumen-de-decisiones.md`)
  se re-anclaron el 2026-08-12, pero esta es **track Informe** y **no se tocó en aquel ciclo**, que
  era track Código.
  - **El sello se cita tal cual, `fc1c6b4-sucio` — eso NO se cambia**, porque es lo que está impreso
    dentro del artefacto. Lo que hay que añadir es **su commit de cierre, `9af842c`**, y retirar el
    «pendiente».
  - **Va ANTES de T10**, como sus dos fichas hermanas de esta nota: si T10 vuelca `4.2` tal cual, la
    memoria publica un «pendiente» que ya no lo está.

### Apuntes de relectura de la memoria — alta del 2026-08-12

- [ ] **`1.4`: qué conceptos de IA entran de verdad en el capítulo 2, y resúmenes de capítulo demasiado escuetos** · Informe · `redactor-tfg`
  Sale de la **relectura de la memoria completa** que está haciendo Francisco. **Fuente viva:
  `mis-apuntes-del-informe.md`**, en la raíz del repo. Ese fichero es **incremental**: Francisco lo
  sigue ampliando conforme relee, así que **al ejecutar esta ficha hay que releerlo entero** y
  trabajar sobre lo que diga ese día — **no fiarse de lo copiado aquí**, que es solo el estado del
  **2026-08-12**.
  - **ORDEN — se ejecuta LA ÚLTIMA:** después de **todas** las fichas abiertas hoy en este fichero.
    Lo pidió Francisco el **2026-08-12**.
  1. **`1.4` dice que el capítulo 2 introduce los conceptos en tres bloques, uno de ellos de IA** —
     y la pregunta de Francisco es **qué conceptos de IA se están incluyendo realmente, si es que
     hay alguno**. O el capítulo 2 cumple lo que `1.4` promete, o hay que ajustar una de las dos
     partes.
  2. **El resumen de cada capítulo en `1.4` es excesivamente escueto.**
  - **DELIMITACIÓN DURA — no absorbe ni sustituye a `T24` ni a `T25`.** `T24` (`2.1.4 Algoritmos de
    ML` sin bloque de redes neuronales) y `T25` (anclaje de `[6]` Goodfellow en ese mismo bloque)
    son **una nota concreta y un hueco concreto**. Esta ficha es otra cosa: pregunta si el
    **capítulo 2 en su conjunto cumple lo que `1.4` promete** sobre el bloque de IA, y **añade el
    punto de los resúmenes escuetos, que no está en ninguna ficha**.
  - **ALCANCE NO CERRADO:** cuando le llegue el turno hará falta un **`grill-me` con Francisco**.
    «Qué conceptos de IA entran en el capítulo 2» es una **decisión de contenido** y **no la puede
    tomar un agente**.

- [ ] **`2.1` · coherencia y densidad del guion teórico** · Informe · `redactor-tfg`
  Sale de la misma relectura. **Fuente viva: `mis-apuntes-del-informe.md`**, en la raíz del repo.
  Ese fichero es **incremental**: Francisco lo sigue ampliando conforme relee, así que **al
  ejecutar esta ficha hay que releerlo entero** y trabajar sobre lo que diga ese día — **no fiarse
  de lo anotado aquí**, que es solo el estado del **2026-08-12**.
  1. `mis-apuntes-del-informe.md:13` — `2.1.1` introduce la IA en un punto que Francisco considera
     equivocado: la definición debe ir **más adelante**, aunque la comparación IA/ML sí aporta
     perspectiva ahí.
  2. `mis-apuntes-del-informe.md:16` — la figura de `1.4` menciona el **aprendizaje continuo** y no
     está definido en ningún sitio; Francisco propone definirlo. **Punto de contacto con `T12`**
     (`6.2 Líneas futuras`), que es donde vive el material de aprendizaje continuo: **no duplicar**,
     decidir qué se define en `2.x` y qué se queda en `6.2`.
  3. `mis-apuntes-del-informe.md:18` y `:22` — en `2.1.3`, etapa 3, se citan juntos
     *cross-validation*, N-fold y desviación estándar; Francisco pregunta si son **tres cosas
     distintas** y si la frase de validación cruzada es un punto propio de la enumeración o va
     dentro de «Medir y comparar su rendimiento».
  4. `mis-apuntes-del-informe.md:20` — la lista larga que sigue son, presumiblemente, las
     **métricas de selección de modelo**; hay que confirmarlo y darle **encabezado propio** si lo es.
  5. `mis-apuntes-del-informe.md:26` — **asimetría de formato**: lo importante del algoritmo va en
     enumeración separada por párrafos y las propiedades que lo hacen bueno, no.
  6. `mis-apuntes-del-informe.md:28` — Francisco pregunta si el apartado incluye **demasiada
     información**. Es una **decisión de densidad, no de estilo**: converge con la ficha de la
     revisión del profesor (justo debajo), que pide simplificar. **Ejecutarlas con el mismo
     criterio.**
  - `mis-apuntes-del-informe.md:24` — **NO es trabajo de agente.** Francisco lo apunta como **tarea
    suya**: cómo maquetar las fórmulas de probabilidad dentro de la definición de la regresión
    logística. Queda anotado aquí **solo para no perderlo**.
  - **ALCANCE NO CERRADO:** «cuánta teoría sobra» y «dónde se define la IA» son **decisiones de
    contenido**; hará falta un **`grill-me` con Francisco** antes de ejecutar.

- [ ] **Revisión del profesor: simplificar, unificar y desduplicar del capítulo 3 en adelante** · Informe · `redactor-tfg`
  **El material que el profesor pide quitar del cuerpo se MUEVE al apéndice `A.3 Ficha del
  sistema` (`T7`), NO se elimina.** `T7` es exactamente la *model card* donde viven semilla,
  hiperparámetros y configuraciones ganadoras; borrar esos datos rompería `T7` y la
  **reproducibilidad declarada** del trabajo.
  **Fuente viva: `mis-apuntes-del-informe.md`**, en la raíz del repo. Ese fichero es
  **incremental**: Francisco lo sigue ampliando conforme relee, así que **al ejecutar esta ficha
  hay que releerlo entero** y trabajar sobre lo que diga ese día — **no fiarse de lo anotado
  aquí**, que es solo el estado del **2026-08-12**.
  - `mis-apuntes-del-informe.md:30` y `:32` — **cita textual del profesor** tras su primer revisado
    del informe completo: mejorar la redacción, **simplificar las explicaciones de las soluciones
    analizadas sin dar todos los hiperparámetros** (su propio ejemplo: la semilla 42), y
    **recortar/unificar apartados** — señala explícitamente **los primeros apartados del
    capítulo 3**.
  - `mis-apuntes-del-informe.md:34` — encargo de Francisco: **interpretar** esas palabras, **no
    rehacer el informe**; identificar qué apartados conviene **recortar o unificar** y hacer un
    **repaso de duplicación en todo el informe**, incluidos los puntos definidos últimamente.
    Francisco confirma haber notado que **en el capítulo 3 se repiten muchas veces los mismos
    datos**.
  - **Alcance: del capítulo 3 en adelante** (es la parte redactada por agente).
  - **ALCANCE NO CERRADO:** qué se unifica y qué se recorta necesita un **`grill-me` con
    Francisco** antes de tocar ninguna nota.

### Residuos del cómputo de T4 — altas del 2026-08-13

> Salen del **cierre de sesión del 2026-08-13**, al verificar el registro contra disco tras cerrar la
> parte de cómputo de T4 (`9ad971b`). **Fichar no es resolver: aquí no se ha tocado ni una línea de
> código.** Nacieron **cuatro**: tres estaban **enterradas dentro de la fila `9ad971b` de
> `## Cerradas`** o **dentro de T11**, donde nadie las mira, y la cuarta **no estaba en ninguna
> parte**. Por la regla de este fichero —**estar en Abiertas significa estar abierto**—, hoy eran
> invisibles para quien retome el proyecto.
>
> **Estado al cerrar la sesión del 2026-08-13: de las cuatro, tres ya están cerradas** —el
> re-anclaje del sello (`ea35ce3`), la automatización del «13 de 98» (`9d4c26d`) y la Tarea B del
> bullet Q6 (`c5ceca5`)—, **y aquí abajo queda solo una**, que es decisión de Francisco. El
> encabezado dice «cuatro» porque describe el lote de altas, no lo que queda pendiente.

- [ ] **La decisión de balanceo de `4.3.4` no es constante entre semillas** · Código · **PENDIENTE DE DECISIÓN DE FRANCISCO**
  `class_weight` gana en **17 de 40** celdas de DecisionTree/RandomForest a lo largo de las 10
  semillas, y la decisión de `4.3.4` se cerró con **n=1** (semilla 42). Medido en el barrido del
  2026-08-12/13 (ver la fila `9ad971b` de `## Cerradas`).
  - **Por qué sale a ficha propia:** hasta hoy **vivía solo dentro de `T11`**, marcada «lo decide
    Francisco» pero **delegada a una ficha de track Informe, que no puede resolverla**. Una decisión
    de diseño no se resuelve desde el capítulo que la cita.
  - **Es una decisión de DISEÑO, no de redacción.** El agente puede **presentar el recuento y las
    opciones**; **fijar el eje de balanceo es de Francisco**. Según lo que decida, toca `4.3.4`
    (rehacer la decisión con n=10) o `5.4` (declararla no constante y dejarla como está).
  - **Nada que ejecutar hasta que Francisco decida:** si se reabriera el eje de balanceo habría que
    pasar por `auditor-ml` y **movería cifras publicadas**, así que **no se toca `firmas.py`** por
    iniciativa de nadie.
  - **Puntero cruzado:** la viñeta de `5.2` de **T11** remite aquí; **T11 no la resuelve**.

### Residuos de la automatización del «13 de 98» — altas del 2026-08-13

> Salen del ciclo que **cerró** la ficha 🟠 del recuento manual (Decisión 3 de la Fase 0 del plan de
> cierre, aprobada por Francisco el **2026-08-13**; ver `## Cerradas`). **Fichar no es resolver:
> ninguna de las dos se ha tocado.** **Ninguna lleva commit ni fecha de cierre.**

- [ ] **La salvedad de procedencia de `dispersion_semillas.md` enumera los dos commits pero no
  imprime los recuentos 94/4** (🟡) · Código · `ml-implementador`
  El `.md` declara que el titular y la banda **no salen del mismo commit** —la semilla 42 viene de
  `1163c90` y de `274923d-sucio` (la cascada invertida), y las bandas de `df30cb2`—, pero **no dice
  cuántas celdas aporta cada uno**: son **94 y 4**. El **CSV sí lo da celda a celda**, así que el
  dato existe y solo falta emitirlo agregado. Importa porque **T7 pega ese `.md` en `A.3`** y un
  lector no puede dimensionar la salvedad sin los recuentos.

- [ ] **El sello `ddade37-sucio` de los artefactos regenerados queda pendiente de re-anclaje en
  prosa** · Código · `ml-implementador`
  `Resultados/dispersion_semillas.csv` y `.md` se regeneraron con `commit_agregador = ddade37-sucio`,
  que es **pre-commit**: hay que re-anclarlo en prosa (`PIPELINE.md`, `GUIA_RESULTADOS.md`) al commit
  de este ciclo **cuando exista**. **No inventar el hash.**
  - **Sería el CUARTO re-anclaje del proyecto** y va **con la misma forma que los tres anteriores**
    (`fc1c6b4-sucio → 9af842c`, `00c3c3e-sucio → 54d1349`, `df30cb2-sucio → 9ad971b`): **el sello
    impreso DENTRO del artefacto NO se toca** —lo estampa `config.commit_actual()` y no puede llevar
    el hash del commit que lo versiona, porque ese commit tiene que existir después—.
  - **Consecuencia para `T7`: cita el sello RE-ANCLADO, no el impreso.** Y ojo: el re-anclaje
    anterior (`df30cb2-sucio → 9ad971b`, commit `ea35ce3`) **queda superado por este** para los dos
    artefactos de dispersión, que ya no son los de `9ad971b`.

### Huecos del informe detectados contra disco — altas del 2026-08-13

> Salen del **pase de verificación contra disco del 2026-08-13**, hecho al preparar el plan de cierre
> que Francisco aprobó ese mismo día. **Fichar no es resolver: aquí no se ha redactado ni una línea de
> la memoria.** La primera es **el mayor bloque de trabajo pendiente del TFG y hoy era invisible en
> este fichero**; las otras tres son residuos menores sin ficha. **Ninguna lleva commit ni fecha de
> cierre: no se ha cerrado nada.**
>
> **Recuento real del vault hoy, medido en disco: 44 notas — 31 redactadas, 8 en guion, 3 vacías**
> (`Resumen` 120 B, `Abstract` 123 B, `6.2 Líneas futuras` 688 B).

- [ ] **La prosa de las 8 notas en guion del capítulo 2 no la encarga ninguna ficha** · Informe · `redactor-tfg`
  Las **8 notas están en GUION PURO** —bullets bajo un epígrafe «Guion propuesto», **cero prosa
  redactada**— y **todas llevan `estado: pendiente`** en el frontmatter, línea 4:
  `2.1.6 Metodologías y buenas prácticas` (7502 B), `2.2.2 Sistemas de detección de intrusiones`
  (3728 B), `2.2.3 Taxonomía de los IDS` (3415 B), `2.2.4 Detección por firmas frente a anomalías`
  (4801 B), `2.2.5 Taxonomía de ataques y panorama` (4402 B), `2.3.1 IA, ML y Deep Learning`
  (4414 B), `2.3.2 La IA en ciberseguridad` (4905 B), `2.3.3 Límites y consideraciones éticas`
  (5220 B).
  - **POR QUÉ ES UN HUECO REAL, y no una ficha duplicada:** **T8** solo encarga *insertar citas en el
    punto de la decisión* en `2.1.5`, `2.1.6`, `2.2.3`, `2.2.4` y `2.3.3` — **no la prosa**. La ficha
    **`2.1 · coherencia y densidad del guion teórico`** cubre el bloque `2.1`. Resultado: **la prosa
    de `2.2.2`, `2.2.5`, `2.3.1` y `2.3.2` no la tiene asignada nadie**, y la de las otras cuatro
    solo está cubierta **de refilón**, por una ficha que va a insertar citas dentro de un texto que
    todavía no existe.
  - **AUTORIZACIÓN YA EXISTENTE — no hace falta decisión nueva de Francisco.** La **decisión marco
    (b) del 2026-08-06** retiró la regla «la teoría la escribe Francisco» para **todo el capítulo 2,
    `2.1.4` incluida**, y la tabla de autoría vigente de este mismo fichero lo confirma: «Todo
    `02 Marco Teórico` … `redactor-tfg`, condición: **ninguna**».
  - **EJECUCIÓN RECOMENDADA: redactar la prosa E INSERTAR LAS CITAS DE T8 EN LA MISMA PASADA**, nota
    por nota. Hacer dos pases sobre las mismas ocho notas es trabajo duplicado.
  - **Estimación: es la fase más larga del plan de cierre, cuatro o cinco sesiones.** Le corresponde
    la **Fase 4**.

- [ ] **`03 Desarrollo\` está vacía en disco y solo falta borrar la carpeta** (🟡) · Informe · `redactor-tfg`
  `00 Índice TFG.md:101-102` la marca «pendiente de borrado físico», y **además su texto afirma que
  «contiene solo avisos de migración», lo que YA ES FALSO**: en disco **no hay ni un `.md`**. Son dos
  cosas: borrar la carpeta y corregir esa frase del índice.

- [ ] **`00 Índice TFG.md:104` declara un recuento que no cuadra con el disco** (🟡) · Informe · `redactor-tfg`
  Dice «**de 43 notas**» con un desglose (5+6 borrador, 9 teoría, 10 pendiente de volcado, 10
  esqueleto, 2 pendiente) que **hoy no corresponde**: son **44 notas, 31 redactadas, 8 en guion, 3
  vacías**. Cuadrarlo al final, cuando la Fase 4 haya movido el reparto redactadas/guion.

- [ ] **`4.2 Base de datos utilizada.md` arrastra 6 marcadores `[CITA:` sin resolver** (🟡) · Informe · `redactor-tfg`
  Líneas **8, 18, 22, 24 (tres veces), 36 y 45**. **Alimentan a T16 y a la bibliografía de Zotero:
  es dependencia de la Fase 7, no trabajo suelto** — resolverlos antes de T16 y no después.

### Altas del cierre de sesión del 2026-08-13

> Salen del **cierre de sesión del 2026-08-13**, tras la corrección de `leader.md` y la política de
> despacho en paralelo (`0fb5f2b`). **Fichar no es resolver: ninguna de las tres se ha tocado.**
> **Ninguna lleva commit ni fecha de cierre.** Las dos últimas son **de Francisco**: un agente puede
> presentar las opciones, no fijarlas.

- [ ] **Reconciliar el contador de citas: convertir `[CITA: …]` a `[n]` y dar de alta en
  `Bibliografía.md`** (🟠) · Informe · **solo `researcher`**
  El **paralelismo aprobado el 2026-08-13** convierte esto en **deuda garantizada**: con tandas de 3-4
  notas el volumen de marcadores se multiplica, y `4.2` ya arrastra **6** por sí sola.
  - **No es solo convertir, es RECONCILIAR: la numeración ya está dañada.** `[6]` (Goodfellow) quedó
    **huérfano** por T25. Un pase que solo tradujese marcadores dejaría el hueco dentro.
  - **T16 NO lo cubre.** T16 es el **volcado de fuentes** bajo la regla «ninguna entrada sin cita en el
    texto», que es **la dirección contraria**: va del listado al texto, no del texto al listado.
  - **Va al FINAL DE CADA FASE de redacción, no una sola vez al final del plan** — si se acumula,
    reaparece el solapamiento silencioso de `[n]` que el protocolo de citas existe para evitar.
  - Lo ejecuta **solo el `researcher`**, único que escribe `Bibliografía.md`, y **en serie**.

- [ ] **Granularidad del commit bajo despacho en paralelo** · — · **PENDIENTE DE DECISIÓN DE FRANCISCO**
  Una tanda cierra **3-4 fichas de golpe** y eso **choca con la regla vigente «un commit por tarea
  cerrada»** (`CLAUDE.md`, sección `## Git`).
  - Las dos únicas salidas: **un commit por TANDA**, nombrando las fichas que cierra, o **3-4 commits
    sobre el mismo estado del árbol** —que es lo que saldría hoy por defecto—.
  - **Hay que decidirlo ANTES de la Fase 4, no dentro.** Recomendación del hilo principal: **un commit
    por tanda**.

- [ ] **`resumen-de-decisiones.md:459` · la divergencia «a corregir por Francisco al redactar»** ·
  Informe · **PENDIENTE DE DECISIÓN DE FRANCISCO**
  Decisión **aplazada dos veces** (2026-08-09 y 2026-08-11) que hasta hoy **vivía solo dentro de la
  fila cerrada `d6dae35` de `## Cerradas`**: no era una ficha, así que **no la veía nadie**. Se le da
  ficha propia por la regla de este fichero: **estar en Abiertas significa estar abierto**.
  - Es una **divergencia terminológica concreta** en `2.2.4` («detectores no supervisados»), **no** la
    autoría de un capítulo: **roza la regla retirada por T0, pero no es la misma cosa**.
  - **Dos salidas y no hay tercera: aceptarla como ficha con alcance, o descartarla expresamente.**
  - **Plantearla al REPARTIR trabajo, no al cerrar sesión** — plantearla al cerrar es exactamente lo
    que la ha aplazado dos veces.

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

> **Estado del lote, consolidado el 2026-08-13.** Cerradas: `T0`; `T1` (`5f98d88`, 8 tablas sobre el
> esquema nuevo, con residuos `T18`-`T22`); `T2` y `T3` (`b1f1df2`, las **dos mediciones baratas**,
> ambas APTO); `T15` (con residuos `T23`-`T25`); `T18` y `T22` (`8fdc421`). Del track de código
> reabierto el 2026-08-06 **solo queda `T4`**, y solo por el **consumo** de su banda en `A.3` (**T7**)
> y en `5.2`/`5.4` (**T11**). **`T9` y `T11` siguen abiertas:** T2 y T3 no las cierran, solo las
> alimentan —el número de la cascada invertida va a `3.2.2` (T9) y el KS separado a `5.1`/`5.4`
> (T11)—, y sus cifras quedan anotadas dentro de cada ficha con su salvedad de uso.

### Autoría de la redacción — estado vigente desde T0 (2026-08-09)

Antes había aquí una lista de secciones vedadas a los agentes. Solo **una** sobrevive como redacción.

**Lo que sigue siendo de Francisco:**

- **La bibliografía final con Zotero en formato IEEE.** Trabajo mecánico en su máquina, fuera del
  vault. No confundir con `Bibliografía.md`, que es del `researcher`.
- Y, fuera de la redacción: **el título del TFG**, **las decisiones de diseño y de alcance** y la
  **revisión final de `6.2`**.

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

## Plan de cierre — aprobado por Francisco el 2026-08-13

> **AVISO: esto es un ORDEN DE EJECUCIÓN, no un estado.** Las **fichas de `## Abiertas` siguen siendo
> la única fuente de verdad de lo que está abierto**; esta sección solo dice **en qué orden
> atacarlas**. Aquí no se cierra nada, no se acepta nada y no se borra nada: leer una ficha nombrada
> en una fase **no** significa que esté hecha ni empezada.
>
> **Objetivo declarado por Francisco el 2026-08-13:** cerrar todas las tareas pendientes para poder
> **dar él una última vuelta al informe y cerrarlo**.
>
> **Decidido el 2026-08-13: NO se elimina ningún fichero del proyecto.** `Guia_ML`,
> `resumen-de-decisiones.md`, `99 Investigación/`, `PIPELINE.md` y `GUIA_RESULTADOS.md` **se
> CONSERVAN** — son la trazabilidad de las decisiones y la procedencia de los artefactos, y borrarlos
> ahorraría bytes a cambio de perder justificación citable. **Los agentes tampoco se colapsan.**

### Las decisiones que solo puede tomar Francisco

Son **el cuello de botella real del plan, no el volumen de trabajo**. Ninguna la puede tomar un
agente; cada una deja bloqueado lo de la columna derecha. **Quedan ocho**: de las ocho originales se
decidieron dos, y el cierre del **2026-08-13** dio de alta otras dos —**granularidad del commit bajo
despacho en paralelo** (que hay que decidir **antes** de la Fase 4, no dentro) y la **divergencia
huérfana de `resumen-de-decisiones.md:459`**, aplazada ya dos veces—, ambas con ficha propia en
`## Abiertas`, que es la fuente de verdad. Las dos decididas: dos de las ocho originales
se decidieron el **2026-08-13** — el **rango de FPR** (hoy instrucción vigente: cifra por variante,
10,2 % en 54 y 8,5 % en 122) y **automatizar el «13 de 98»** (hecho en `9d4c26d`; la prohibición de
citarlo está levantada).

| # | Decisión | Qué bloquea |
|---|---|---|
| 1 | **Eje de balanceo de `4.3.4`**: rehacer la decisión con n=10, o declararla no constante | El cierre de **T11** |
| 2 | **¿Se regeneran los splits?** | La ficha de las **rutas absolutas hardcodeadas** |
| 3 | **Permiso de escritura en `resumen-de-decisiones.md` para el `ml-implementador`** | Dos fichas de corrección |
| 4 | **¿Consigue acceso institucional?** | **T14** y la ficha de guardia del PDF |
| 5 | **Alcance de los tres `grill-me`** (`2.1`, revisión del profesor, `1.4`) | No son despachables sin él |
| 6 | **El título del TFG** | **Preliminares**. Un agente **propone candidatos**, no lo fija |

### Las siete fases, en orden

- **Fase 0 — Decisiones. EN CURSO.** Las **ocho** de la tabla de arriba (las seis que quedaban más
  las dos altas del cierre del 2026-08-13: granularidad del commit en paralelo y la divergencia de
  `resumen-de-decisiones.md:459`). **Cero cómputo.** Va primera porque **cuatro fases posteriores
  arrancan a medias sin esto**.
  **La Tarea B ya NO forma parte de esta fase: se aplicó el 2026-08-13 en `c5ceca5`** (bullet Q6 de
  `resumen-de-decisiones.md`). Si algún texto la sigue pidiendo, está desfasado.
- **Fase 1 — Barrido de correcciones de una línea.** **DOS ciclos, uno por track**, porque el agente
  difiere.
  - **Código:** `warnings.filterwarnings('ignore')` en **`program.py:12`** y **`validacion.py:57`**
    —**ojo: NO `validacion.py:21`, que es comentario**— y la **nota fechada de
    `resumen-de-decisiones.md:820-821`**.
  - **Informe:** **`4.2:105`**, el **rango de FPR en sus cuatro sitios** (`4.2:120`, `A.2:69` y las dos
    viñetas de este fichero, **en la misma pasada**), el **sello de `4.2:145`**, **T20** (desbloquea
    **T9**) y las **tres correcciones de una línea de T25** en `Bibliografía.md:32`, `:86` y
    `Auditoría de Bibliografía.md:140`, **que solo toca el `researcher`, y en serie**.
  - **Minutos de trabajo, cierra seis fichas.** Por eso va tan arriba.
- **Fase 2 — Cerrar T4.** **Crear `A.3` (T7)** pegando la tabla de `Resultados/dispersion_semillas.md`
  con sus **tres salvedades** y el sello re-anclado → **queda servido T11** → **con eso T4 se puede
  cerrar**. El «13 de 98» ya está automatizado (`9d4c26d`), así que esta fase no espera a nada. **T7 va
  ANTES de la revisión del profesor** porque el material que se recorte del cuerpo **se MUEVE a `A.3`,
  no se elimina**.
- **Fase 3 — Deuda de datos del informe.** **Figuras de `assets\`** (va **antes de T10** y **retira un
  `[!todo]` vivo en `4.2:117`**), **T19**, **T21**.
- **Fase 4 — Capítulo 2.** La **ficha nueva de la prosa de las 8 notas en guion** (alta del
  2026-08-13), con **T8 y T24 integrados en la misma pasada por nota**. **La fase más larga del
  plan.**
- **Fase 5 — Capítulos 3 a 6.** **T5** (crea `5.0`, que **NO existe en disco**), **T10**, **T11**,
  **T9**, **T6**, **T13**, **T12**.
- **Fase 6 — Los tres `grill-me`.** `2.1`, revisión del profesor, y **la ficha `1.4` la ÚLTIMA de
  todas**, como pidió Francisco el **2026-08-12**.
- **Fase 7 — Cierre.** **T16** (obligatoriamente **después de T8-T13**, por su regla dura «ninguna
  entrada sin cita en el texto»), **T17**, **Preliminares con el título**, **borrar `03 Desarrollo\`**
  y **cuadrar el recuento del índice**. **La bibliografía final Zotero/IEEE es de Francisco**, no
  entra en ninguna fase.
- **Fuera de fases, a aceptar o retirar por Francisco:** el **diagrama de agentes desactualizado** y
  las **rutas hardcodeadas**.

### Política de paralelismo — regla nueva del 2026-08-13

**El criterio es el FICHERO, no el tema: dos redactores a la vez solo si escriben ficheros distintos.**

- **La Fase 4 (capítulo 2) se ejecuta en tandas de 3-4 notas en paralelo, no nota a nota.** Son 8 notas
  en guion, con **T8 y T24 integrados en la misma pasada por nota**. Es la fase más larga del plan y la
  que más se acorta con esto.
- **La Fase 5 admite paralelismo por nota**, respetando las ordenaciones duras de abajo.
- **NUNCA en paralelo:** dos agentes sobre la **misma nota**; `Bibliografía.md`; `features.md`; la
  **asignación de números de cita `[n]`**; y el pase de **`auditor-ml`**, que va **después**, no a la vez.
- **Protocolo de citas bajo paralelismo:** un redactor en paralelo **no asigna nunca un `[n]` nuevo** —
  son un contador global, y hoy `[4]`, `[5]`, `[7]`, `[8]` y `[10]` ya están en uso en las notas de
  `2.1` y `2.2`, así que cuatro redactores simultáneos empezarían los cuatro en `[11]` y se solaparían
  en silencio. Se escribe **`[CITA: autor o tema]`**, convención que el proyecto ya usa (`4.2` arrastra
  6 marcadores). **La conversión a `[n]` y el alta en `Bibliografía.md` es un pase posterior y EN SERIE
  del `researcher`.**
- **La prohibición de que el `redactor-tfg` escriba la teoría `2.x` y el borrador de `6.2` está
  RETIRADA del andamiaje** (corregido en `leader.md` el **2026-08-13**): era lo que bloqueaba la Fase 4
  entera. **Sigue siendo de Francisco:** la bibliografía Zotero/IEEE, el título del TFG, las decisiones
  de diseño y alcance, y la **revisión final de `6.2`**.

### Ordenaciones duras heredadas que el plan respeta

Se dejan listadas para que **nadie las rompa** al reordenar:

- **T16 después de T8-T13.**
- **Figuras de `assets\` y el sello `4.2:145` antes de T10.**
- **T20 antes de T9.**
- **La ficha `1.4`, la última de todas.**
- **El recorte del profesor va a `A.3`**, así que **T7 antes**.
- **«13 de 98» automatizado antes de que T7 y T11 lo citen** — **satisfecha** en `9d4c26d`.

### Estimación y límite declarado

**Entre diez y catorce sesiones**, **dominadas por la Fase 4** — menos con la política de paralelismo.

**El límite, dicho sin rodeos: NO se pueden cerrar «todas» las fichas por parte de agentes.** **Seis
son estructuralmente de Francisco** — bibliografía Zotero/IEEE, título del TFG, eje de balanceo,
alcance de los tres `grill-me`, acceso institucional y regeneración de los splits. **Si esas se quedan
quietas, el plan se atasca en la Fase 0, no en la Fase 4.**

---

## Cerradas

| Fecha | Track | Tarea | Commit |
|---|---|---|---|
| 2026-08-13 | Código | **Tarea B APLICADA · corregido el alcance del balanceo en el bullet Q6 de `resumen-de-decisiones.md`.** Cierra la ficha 🟠 abierta el 2026-08-13 (`resumen-de-decisiones.md:120`). El texto decía «*se corre solo sobre el set 54*» y era **falso contra disco**: `firmas.py:559` llama a `_experimento_balanceo()` **sin condicional de variante**, `Resultados/metricas_balanceo.csv` trae **16 filas = 8 por variante** (`54` y `122_sin_seleccion`) y `config.ALCANCE_BALANCEO` (`config.py:463-468`) es **agnóstico a la variante**. De paso se precisó el eje, que la fórmula corta dejaba impreciso: **SMOTE vs `class_weight` solo vale para DecisionTree y RandomForest; KNN e HistGradientBoosting comparan SMOTE contra NADA**, porque sklearn no les admite `class_weight` (`firmas.py:91-96`). El «4 algoritmos» sí era correcto. **CORRIGE UNA DESCRIPCIÓN, NO REABRE Q6:** sigue vigente que el balanceo **no se cruza** con el grid ni con el eje de selección (`firmas.py:249-255`). La edición la aplicó el **hilo principal con Francisco delante** —ningún agente escribe en ese fichero—, sobre el texto que el `ml-implementador` había redactado y verificado. Cero código, cero corridas, ninguna cifra publicada movida | `c5ceca5` |
| 2026-08-13 | Código | **Refactorización integral de `features.md`, 1.349 → 1.087 líneas**, con **excepción autorizada por Francisco** al invariante «se edita quirúrgicamente, nunca se reorganiza entero». **No es precedente** y el estado previo íntegro queda recuperable en `9d4c26d`. **10 fichas palimpsesto compactadas**, **5 cabeceras vacías retiradas** y `## Cerradas` compactada **conservando fecha, track, hash y evidencia**. **Verificación mecánica contra la versión anterior, que es lo que hace citable esta fila: 39 fichas abiertas antes y después, 50 filas cerradas antes y después, 173.360 → 133.230 bytes; y de los 39 hashes citados solo desaparece `9734f4b`**, que estaba en un párrafo que describía `validacion.py` como WIP incompleto y sin re-correr —estado superado— y cuyo hash principal `d9225be` sobrevive. Trabajo sin ficha propia (carril Intervención) | `6bfc779` |
| 2026-08-13 | Código | **Retirada de `leader.md` la prohibición DEROGADA de despachar `redactor-tfg` para la teoría `2.x` y el borrador de `6.2`.** Estaba derogada desde el **2026-08-06** (decisión marco (b)) y ya retirada de `CLAUDE.md` y de `redactor-tfg.md`, **pero no de `leader.md`; y como el leader es quien despacha, ganaba la regla vieja: ésa era la razón ESTRUCTURAL de que las 8 notas del capítulo 2 llevaran semanas en guion sin que nadie tuviera permiso de escribirlas.** En el mismo commit, la **política de despacho en paralelo** (decisión de Francisco del 2026-08-13): la unidad es el **FICHERO, no el tema**; nunca en paralelo dos agentes sobre la misma nota, `Bibliografía.md`, `features.md`, la asignación de `[n]` ni el pase de `auditor-ml`; **varios `auditor-ml` sí van en paralelo**, que son de solo lectura. **Protocolo de citas:** nadie inventa un `[n]` nuevo —contador global, hoy `[4]`, `[5]`, `[7]`, `[8]` y `[10]` en uso—, se escribe `[CITA: tema]` y la conversión es un pase posterior **en serie** del `researcher`; escrito en **`CLAUDE.md`**, que es lo que se inyecta a todos los agentes, y no solo en `leader.md`. Dos ítems nuevos en `auditor-ml.md` que no existían en `.claude/`: **ningún número de la memoria sale de un cálculo a mano** y **las nueve tablas publicadas son intocables, verificado por md5 antes y después**. `grill-me/SKILL.md` reescrito. **No se tocaron las 313 entradas de `permissions.allow`**, y merece quedar escrito por qué: un `deny` sobre `git commit`/`push` **rompería el skill `cierre`**, que es la vía sancionada; la barrera real es la lista `tools:` de cada agente, y solo `ml-implementador` y `ejecutor-experimentos` tienen Bash/PowerShell. Ficheros: `.claude/agents/leader.md`, `.claude/agents/redactor-tfg.md`, `.claude/agents/auditor-ml.md`, `.claude/skills/grill-me/SKILL.md`, `CLAUDE.md` | `0fb5f2b` |
| 2026-08-13 | Código | **El titular «13 de 98» ya SALE DEL ARTEFACTO: automatizado el recuento «fuera de banda» de la semilla 42.** Cuatro columnas nuevas en `agregar_semillas.py` —`valor_semilla_42`, `dentro_banda_42`, `distancia_fuera_banda_42`, `commit_semilla_42`—, **sección propia en el `.md`** y recuento por stdout. **El número manual RESISTE: 13 de 98, con 0 celdas sin casar**, así que **queda LEVANTADA la prohibición de citarlo**. Artefacto regenerado dos veces; **las nueve `metricas_*.csv` publicadas quedan con md5 IDÉNTICO antes y después** y **cero entrenamiento**. Dictamen de `auditor-ml`: **APTO CON CAMBIOS**, los cinco hallazgos altos aplicados y reverificados. **Las tres salvedades que se van con el `.md` y que T7 tiene que pegar en `A.3` están escritas en T7.** No cierra **T4** (falta el consumo de la banda) ni la **Tarea B**. Deja dos residuos con ficha propia: los recuentos **94/4** sin imprimir y el sello **`ddade37-sucio`** pendiente de re-anclaje. Ficheros: `Implementacion/app/agregar_semillas.py`, `Implementacion/PIPELINE.md`, `Resultados/GUIA_RESULTADOS.md`, `README.md`, `Resultados/dispersion_semillas.csv` y `.md` | `9d4c26d` |
| 2026-08-13 | Código | **Re-anclado en prosa el sello `commit_agregador = df30cb2-sucio` → `9ad971b`** en `Implementacion/PIPELINE.md` y `Resultados/GUIA_RESULTADOS.md` (tabla de corridas **y** prosa). **Tercer re-anclaje del proyecto**, tras `fc1c6b4-sucio → 9af842c` (`97e679b`) y `00c3c3e-sucio → 54d1349` (`ad62665`), y **con la misma forma**: **el sello impreso DENTRO del artefacto NO se toca** —lo estampa `config.commit_actual()` y no puede llevar el hash del commit que lo versiona, que tiene que existir después—. **Cero cómputo, cero artefactos regenerados, ninguna cifra publicada movida.** Acotados dos recuentos sin moverlos: **2.320 filas** en las nueve `metricas_*_semillas.csv` y **232 = 222 + 10** en las nueve publicadas. Dictamen de `auditor-ml`: **APTO CON CAMBIOS**, aplicado en la segunda pasada. **Superado para los dos artefactos de dispersión por su regeneración posterior** (`ddade37-sucio`, ficha propia abierta) | `ea35ce3` |
| 2026-08-13 | Código | **La parte de CÓMPUTO de T4 — barrido de 10 semillas CORRIDO y agregado. NO cierra T4**, que sigue abierta por el **consumo** del resultado (`A.3`/**T7** y `5.2`/`5.4`/**T11**). Trabajo sin ficha propia (carril Intervención dentro de T4). Corrió el **2026-08-12T22:09 → 2026-08-13T00:38**, **≈2 h 29 min**: **2.320 filas**, **20/20 celdas** (10 semillas × 2 variantes, `54` y `122_sin_seleccion`), sello **`df30cb2` único y limpio**. **Aislamiento intacto**, que es lo que el andamiaje existe para garantizar: nueve tablas publicadas, 20 `.joblib` y 39 figuras **sin tocar**, cero residuos `_semilla` en `Resultados/modelos/`, los **100 logs** de `Resultados/logs_barrido/` terminan en `COMPLETADO` sin tracebacks, y la propagación de `--semilla` verificada como **real y no cosmética**. **Agregador ejecutado** → `Resultados/dispersion_semillas.csv` y `.md`, **198 filas** (98 de calidad + 100 de dispersión de máquina), `sd` muestral `ddof=1`. **Bug corregido en el agregador, reincidencia del defecto que cerró T1:** `_tabla_md` no emitía `alcance` ni `tabla_origen`, así que rotulaba **`54 \| RandomForest`** tanto para el clasificador de firmas como para la cascada invertida; corregido y agregador re-ejecutado. **Tres pasadas de auditoría, la 2.ª NO APTO; veredicto final APTO.** **Los resultados, que es para lo que existía T4, están escritos en T11 y en T4**: el hueco RF vs HGB **no sobrevive** (orden no establecido), el hueco AE vs IsolationForest **sí aguanta**, el titular de firmas es el punto más favorable de once corridas, la 42 cae fuera de banda en **13 de 98** celdas, y la decisión de balanceo de `4.3.4` **no es constante** entre semillas. **Alcance de lo medido, a escribir así y no de otra manera:** dispersión **de los modelos sobre splits y set de características FIJOS** (`program.py` no está parametrizado), **no «dispersión del sistema»**. Ficheros: `Implementacion/app/agregar_semillas.py`, `Implementacion/PIPELINE.md`, `Resultados/GUIA_RESULTADOS.md`, `README.md` y `Resultados/verificacion_semilla_joblib.txt` (modificados); `Resultados/dispersion_semillas.csv` y `.md` y los **nueve `Resultados/metricas_*_semillas.csv`** (nuevos) | `9ad971b` |
| 2026-08-12 | Código | **El `.joblib` ausente ya da mensaje accionable en vez de traceback crudo — más tres correcciones del runbook del barrido.** Trabajo sin ficha propia (carril Intervención dentro de T4); Francisco lo mandó arreglar antes de lanzar. **Cero cambios de lógica, umbrales, métricas o escritura de tablas; ningún número publicado se mueve.** `app/hibrido.py:200-219` (`_cargar_joblib`) y `app/cascada_invertida.py:198-213` (`_cargar_joblib_firma`, **simetrizado con `_leer_umbral_conf`**) envuelven el `joblib.load` y relanzan `RuntimeError ... from None` con ruta, script previo, variante con su flag y semilla; **siguen abortando con exit ≠ 0 y escritura cero**. El caso «joblib **AUSENTE**» caía por debajo de las salvaguardas auditadas, que solo cubrían «joblib de **OTRA** semilla presente». **La cita falsa que merece quedar escrita:** `cascada_invertida.py:314` citaba `hibrido.py:301` como respaldo de **P-5**, y esa línea es **la regla τ**, otra decisión; reanclada **por símbolo** (`hibrido.py::_ensamblar_prediccion`). **Tres correcciones en el runbook de `PIPELINE.md`, las tres por afirmar en absoluto algo que el código no sostiene:** **paso 0 nuevo** —árbol limpio bajo `Implementacion/` antes de lanzar, porque `config.commit_actual()` sellaría `-sucio` y las 2.320 filas nacerían con un sello no recuperable desde git—; **salvedad al «abortan»** —la tabla de los cuatro detectores es la excepción: omite el detector con aviso y deja `metricas_hibrido_0day*` en **54 filas en vez de 72**—; y el **nombre de función equivocado**: la que gobierna los nombres de artefacto es **`config.sufijo_semilla()`** (`config.py:203-213`), que **con la 42 devuelve cadena vacía** —lo que hace verdadera la garantía de T4—, no `config.sufijo_de_semilla()`, que toma argumento y devuelve `"_semilla42"` (la usa el borrado del barrido). Verificado **ejecutando** las dos funciones. **Tres pasadas de `auditor-ml`, veredicto final APTO.** Cifras medidas que sustituyen a las que arrastraba T4: **65,2 GB libres** en C: y **2.320 filas** verificadas por dos vías | `91f2ed7` |
| 2026-08-12 | Código | **Re-anclaje del sello `00c3c3e-sucio` → `54d1349` y saneamiento del texto de T4.** Trabajo sin ficha propia (carril Intervención dentro de T4). Ficheros: `Implementacion/PIPELINE.md`, `features.md`. **Cero código de modelos, cero corridas, cero cifras publicadas movidas**; la aritmética 232 filas / 9 ficheros no cambia. **El sello impreso DENTRO de `Resultados/verificacion_semilla_joblib.txt` no se editó** —es salida de `config.commit_actual()`, misma razón que en `97e679b`—, con fila nueva en la tabla de corridas; verificado que `git diff 54d1349 -- Resultados/verificacion_semilla_joblib.txt` sale **vacío** y que `54d1349` es el único commit que ha tocado el fichero. Dictamen de `auditor-ml`: **APTO CON CAMBIOS, ningún 🔴**, los siete hallazgos aplicados. **El 🟠 que merece quedar escrito: el paso 2 del runbook exigía un VACÍO IMPOSIBLE** — `Get-ChildItem -Recurse ..\Resultados -Filter *_semilla*` casa con esa traza, que está versionada y es **permanente**, así que enseñaba al operador a ignorar la única comprobación que evita que la reanudación dé una celda por hecha. Ahora la excluye explícitamente, con el motivo al lado, **verificado ejecutándolo: sale vacío**. Los otros dos 🟠: el sello `00c3c3e-sucio` **nombra DOS corridas** (la verificación `--solo-verificar` con cero `fit` y el ensayo de humo a semilla 1, que sí hizo cuatro `fit`), declarado en la tabla; y `--solo-verificar` **reescribe la traza siempre** (`barrido_semillas.py:149-150`), así que en cuanto alguien siga el runbook las citas del sello dejan de describir el disco — añadido el aviso y cómo re-anclarlas. De los cuatro 🟡: el par **0,8605 / 0,8257 son *accuracies*** y se añadieron los `f1` reales **0,8716** y **0,8341** (`Resultados/metricas_anomalias.csv`, set 54), y **las cuatro cifras de la semilla 1 quedan marcadas como NO VERIFICABLES desde git** —su CSV se borró como residuo y nunca se commiteó: cero coincidencias de `0.8632\|0.8520\|0.8226\|0.8157` en el repo—, así que valen como indicio interno, **no como evidencia citable en la memoria** | `ad62665` |
| 2026-08-12 | Código | **Remate del ensayo de humo del barrido + RUNBOOK del barrido.** Trabajo sin ficha propia (carril Intervención dentro de T4); el andamiaje que esto remata se commiteó antes en `54d1349`. **Cero código de modelos tocado, cero cifras publicadas movidas.** Ficheros: `Implementacion/PIPELINE.md` (+152), `README.md` (+4), `resumen-de-decisiones.md` (+9). **Los tres puntos que quedaban PASAN, dos con reserva:** (1) la **salvaguarda de mezcla de semillas** aborta con exit 1 y escritura cero, pero con **traceback crudo** —arreglado luego en `91f2ed7`—; (2) la **reanudación no duplica filas**, probada por vía barata (10 corridas → 9 con 1 saltada; tablas en 1 y 18 filas tras relanzar, no en 2 y 36); (3) el **agregador aborta** con exit 1, mensaje claro y sin escritura parcial, pero por la guarda de **tabla inexistente** (`agregar_semillas.py:235`), **no** por la de «1 semilla de 10», que sigue sin ejercitarse. **Residuo del ensayo creado y borrado, verificado:** cuatro ficheros, y `Resultados/` queda idéntico al estado inicial (**107 ficheros, 20 `.joblib`, 39 figuras, 9 tablas publicadas**). Merece quedar escrito porque las `metricas_*_semillas.csv` **sí se versionan**: de haberse quedado, se colaban en el commit. **El runbook era el hueco de «dejarlo listo»: no existía uno autosuficiente** — faltaban el comando completo, el recuento total esperado de cada una de las nueve tablas y la comprobación **de CIERRE** de que la semilla 42 no se movió (la única existente era *preflight*, o sea antes y no después). Sección nueva «Runbook del barrido de semillas» en `Implementacion/PIPELINE.md`: seis pasos copiables, prerrequisitos redactados **como comprobaciones y no como afirmaciones sobre el disco**, tabla de los nueve totales con su derivación declarada, y qué teclear tras un corte. Puntero desde `README.md`. Dictamen de `auditor-ml`: **APTO CON CAMBIOS**, un 🟠 y cuatro 🟡, todos aplicados. **El 🟠: el runbook decía CUATRO recuentos y el lanzador exige CINCO** (las 5 filas de la cascada invertida, `barrido_semillas.py:107-109`), contradiciendo en silencio a la ficha contigua. El quinto hallazgo fue a `resumen-de-decisiones.md` con **nota fechada, sin reescribir el texto histórico**: D5 se declaraba cerrada con solo la tasa de la cascada y el agregador agrega **también `n_condenadas`** | `419f4c7` |
| 2026-08-12 | Código | **Andamiaje COMPLETO del barrido de semillas para T4 — los OCHO hallazgos aplicados, lanzador reanudable y agregador.** Trabajo sin ficha propia (carril Intervención dentro de T4). Contenido: `SEMILLAS_BARRIDO = [1..10]` en `config.py`; el agregador nuevo `Implementacion/app/agregar_semillas.py`; el lanzador **reanudable** `Implementacion/app/barrido_semillas.py`; `Resultados/figuras/*_semilla*` excluido en el `.gitignore` raíz; la traza `Resultados/verificacion_semilla_joblib.txt` (**20/20 `.joblib` publicados con `semilla = 42`**, verificado en disco); y la tabla «qué SÍ varía dentro de cada semilla» en `PIPELINE.md`, verificada línea a línea contra el código por el auditor. **DOS pasadas de `auditor-ml`, ambas APTO CON CAMBIOS, las once aplicadas.** El hallazgo más serio merece quedar escrito porque es el tipo de fallo que este proyecto ya ha sufrido: **`config.ALCANCE_BALANCEO` llevaba el literal «semilla 42» y lo escribía en la columna `alcance`**, así que el barrido habría producido **160 filas versionadas con una afirmación FALSA dentro del propio dato**, imposible de corregir sin re-correr. En la segunda pasada: `commit` → `commit_agregador`, `decisiones_no_constantes` como columna del CSV, el modo real de la traza parametrizado y una frase sin respaldo retirada. Cifras medidas: `Resultados/modelos` **481,33 MB** y el barrido **200 modelos ≈ 4,8 GB**, con lo que el 🟠 del espacio dejó de ser blocker. **El ensayo de humo quedó a medias** (el `ejecutor-experimentos` cayó con un 529 Overloaded tras `anomalias.py --semilla 1`) y dejó en disco **11 ficheros `_semilla1`** con `commit = 00c3c3e-sucio` **sin abrir ninguna de las nueve tablas publicadas**, que es lo que el andamiaje existe para garantizar; se **borraron el mismo 2026-08-12**, con OK de Francisco y antes de este commit. **La comprobación NO queda superada por ese borrado:** el paso 2 del runbook sigue exigiendo que `Get-ChildItem -Recurse ..\Resultados -Filter *_semilla*` salga **VACÍO** antes de lanzar, **con la exclusión de `verificacion_semilla_joblib.txt`** añadida en `ad62665` —esa traza casa con el patrón, está versionada y es permanente—, porque cualquier corrida interrumpida repone residuos | `54d1349` |
| 2026-08-12 | Código | **Andamiaje de semilla para T4 — el flag `--semilla N` y las nueve tablas `*_semillas.csv`**, con cómputo CERO. Trabajo sin ficha propia (carril Intervención dentro de T4). **Vía elegida:** flag CLI que llama a `config.fijar_semilla(N)` **antes de instanciar**; los consumidores ya leían `config.RANDOM_STATE` **por atributo**, así que mutar la global propaga **sin cambiar ninguna firma**. **Tres decisiones de diseño cerradas:** (1) **una tabla `*_semillas.csv` por cada tabla existente (9), no una común** — obligado, porque `guardar_metricas()` **aborta** si el conjunto de columnas difiere entre filas del mismo CSV, y una tabla común exigía **rediseñar T1**, que estaba prohibido; (2) **con semilla 42 el sufijo es cadena vacía**, así que una corrida por defecto es idéntica a la actual, y con semilla ≠ 42 **no se abre ninguna de las nueve tablas publicadas**; (3) **se incluyó `cascada_invertida.py`** —el encargo decía cuatro scripts, **son cinco**—: sin el flag, correrla bajo otra semilla **habría escrito en su tabla publicada**. **Límite del diseño:** `program.py` **no** está parametrizado, así que las 10 semillas miden dispersión **de los modelos sobre splits y set de características FIJOS**. Ficheros: `Implementacion/app/config.py`, `evaluacion.py`, `anomalias.py`, `firmas.py`, `baseline.py`, `hibrido.py`, `cascada_invertida.py` e `Implementacion/PIPELINE.md`. Dictamen de `auditor-ml`: **APTO CON CAMBIOS, ningún 🔴** — verificó que el **peor modo de fallo** (10 corridas con semilla 42 → dispersión cero, falso tranquilizador) **no puede darse**: no hay ni un `from config import RANDOM_STATE`, los ~15 usos son por atributo dentro de funciones y `fijar_semilla()` se llama en los **cinco `__main__`**. Sin leakage nuevo, sin rediseño de T1, y `config.py` **sigue sin imports del proyecto** (de lo que depende `validacion.py`) | `e611068` |
| 2026-08-12 | Código | **`PIPELINE.md` ya no está desalineado con su propia figura** (ficha abierta el 2026-08-01, «la acepta o la retira Francisco»). El árbol de ficheros generados lista ya **`transformers.joblib`** (`:53`) y **`selected_features.txt`** (`:30`), **distingue lo que existe por duplicado —uno por variante, `_transformers.joblib` incluido— de lo que no**, y **declara su alcance** (`:71-72`). **Corrección verificada en disco que la propia ficha traía mal:** `selected_features.txt` lo escribe **`program.py:531-535`**, no `:521`, y **no lleva prefijo de variante** — es la única excepción a la regla del prefijo. **Documentación pura:** ningún script de `app/` tocado, ninguna corrida, ninguna cifra publicada movida. Sale en el **clúster de cinco fichas de `PIPELINE.md`**; dictamen común en la fila de abajo | `97e679b` |
| 2026-08-12 | Código | **Re-anclado el sello `fc1c6b4-sucio` a su commit de cierre, `9af842c`** — la ficha que **no podía cerrarse hasta que el commit existiera**, y ya existe. Re-anclado en los **tres** documentos: `Implementacion/PIPELINE.md`, `Resultados/GUIA_RESULTADOS.md` y `resumen-de-decisiones.md`. **El implementador se dejó el tercero en la primera pasada y se completó en una segunda.** **El sello impreso DENTRO de los artefactos no se tocó** —sigue diciendo `fc1c6b4-sucio`— **y se dice por qué**: es una salida generada, no un texto editable; quien la edite a mano rompe la correspondencia con lo que imprimió `config.commit_actual()`. Corregido de paso el **anclaje frágil** `..._validation_report.txt:4-5`, que pasa a citarse **por el nombre del campo**. **Re-anclaje textual: cero corridas, cero artefactos regenerados, cero cifras alteradas.** **Residuos: `resumen-de-decisiones.md:820-821`** (punto 5 de la auditoría, sin permiso de escritura en aquella pasada) **y la copia viva del vault** (`4.2:145`, track Informe) — **dos fichas nuevas en `## Abiertas`**. **Dictamen de `auditor-ml` del clúster: APTO CON CAMBIOS, todo aplicado.** Encontró un **🟠 real**: `GUIA_RESULTADOS.md` afirmaba que las líneas de procedencia «no están en los ficheros que hay en disco» cuando **sí están** desde la corrida de las 20:53, **contradiciendo a su propia §3.2** — es la **variante INVERSA del defecto reincidente del proyecto**: no afirmar en presente lo que la corrida no respalda, sino **negar en presente lo que la corrida sí respalda**. Más **tres 🟡** de texto caducado, aplicados | `97e679b` |
| 2026-08-12 | Código | **`PIPELINE.md` ya no se contradice dentro del mismo recuadro de trazabilidad.** Retirada la frase falsa «**su commit de cierre todavía no existe**» —el commit existe y es `9af842c`—, que chocaba con la mitad verdadera del mismo recuadro («están commiteados»). **Y no era una, eran tres:** se retiraron además **dos recaídas gemelas del mismo recuadro**. Verificado en disco el 2026-08-12: **cero apariciones** de «todavía no existe» en `Implementacion/PIPELINE.md`. Era **texto vigente y engañoso, no historial** —no llevaba nota fechada que lo superase—, y por eso se **corrige**, no se anota. Sale en el clúster de cinco; dictamen en la fila de arriba | `97e679b` |
| 2026-08-12 | Código | **Las tres filas de la tabla de corridas de `PIPELINE.md` quedan ancladas a su commit.** Ya no dicen «*aún en el árbol de trabajo*»: **`1163c90` → `8fdc421`** (cierre de **T18**), **`274923d-sucio` → `b1f1df2`** (cierre de **T3**) y **`fc1c6b4-sucio` → `9af842c`** (cierre del ciclo de los siete residuos). Las dos primeras eran el 🟡 «caducadas» y la tercera es el re-anclaje: **las tres en la misma pasada**, como ordenaban sus punteros cruzados. Importa porque un tercero que leyera la columna concluía que **las cifras publicadas de T18 y de T3 no se pueden recuperar de git**, cuando sí se pueden. Las filas viven hoy en **`PIPELINE.md:369-371`**. Sale en el clúster de cinco | `97e679b` |
| 2026-08-12 | Código | **Glosa del sufijo `-sucio` escrita en la primera aparición de los dos ficheros.** Una línea en `Implementacion/PIPELINE.md` (glosa **`:186-190`**, colgando de la primera aparición **`:184`**) y en `Resultados/GUIA_RESULTADOS.md` (**`:104-106`**, bajo la fila `commit`/`fecha` de **`:102`**), describiendo la convención y **remitiendo a la tabla canónica**, que queda **INTACTA y no se duplica** —hoy en `PIPELINE.md:994` (encabezado) + `:1001-1005` (los tres valores)—. El hueco era **de orden de lectura**: el `-sucio` ya estaba documentado en `config.py`, `evaluacion.py` y esa tabla, pero a **≈800 líneas** de su primera aparición, y **sin ninguna explicación** en `GUIA_RESULTADOS.md`. **Queda fuera el vault**, donde el `-sucio` sigue sin glosarse: se cubre con la ficha nueva de `4.2:145`. Sale en el clúster de cinco | `97e679b` |
| 2026-08-12 | Informe | **`4.2` · la medición (B) del KS, la frase del FPR y el callout de trazabilidad.** Despachada en la **misma pasada** que la fila de abajo, como ordenaba el puntero cruzado de ambas: **un solo fichero tocado**, `Obsidian_TFG_Vault\04 Implementación del sistema\4.2 Base de datos utilizada.md`. La medición **(B)** entra **junto a (A)**, con tabla: **37/54 · 44/122** frente a **25/54 · 31/122**, y `src_bytes` **0,346 → 0,091**, `dst_bytes` **0,317 → 0,107**. La salvedad del `delta = (A) − (B)` queda **impresa como COMPARACIÓN y no como descomposición aditiva** —el KS es un supremo de diferencia de CDF y no es aditivo sobre una mezcla—. La frase del FPR queda **reanclada a (B)**, que es la que la sostiene: (A) compara contra un D2 que es 57 % ataques y los falsos positivos los generan las filas **normales**. Y el callout de trazabilidad cita **las dos variantes** con sus fechas (**20:53:27** / **20:53:46**) y el sello **`fc1c6b4-sucio` tal cual, sin inventar hash** — su re-anclaje tiene **ficha propia abierta**. Dictamen de `auditor-ml`: **APTO CON CAMBIOS** — sin leakage, sin cifras caducadas y **sin invadir T10, que sigue intacta**. **Residuos que deja:** las figuras de `assets\` (la de (A) es de una corrida anterior y las de (B) no están copiadas, con un `> [!todo]` vivo en la nota) y dos imprecisiones 🟡 de una línea (`:120` y `:105`) — **dos fichas nuevas en `## Abiertas`**; más el «~33 %» de DoS de `:72`, **anclado dentro de T10** | `7c0659f` |
| 2026-08-12 | Informe | **El vault ya no dice «mediana» donde el artefacto dice «media».** `4.2 Base de datos utilizada.md:107` afirmaba «la **mediana** de outliers en D1 es del 4,78 %» y era el **único** sitio del vault afectado tras el cierre del rótulo del 2026-08-11 (`84e3c8f`). Rótulo corregido a **media entre características**, con **4,78 %** (54) y **2,44 %** (122), **verificados contra los dos `*_validation_report.txt`** — no copiados de la ficha. Cerrada **antes de T10**, que era la condición: si T10 hubiera volcado `4.2` tal cual, el TFG publica un estadístico que **nadie ha calculado**. Sale en la misma pasada y bajo el mismo dictamen que la fila de arriba | `7c0659f` |
| 2026-08-11 | Código | **`commit` + `fecha` en el CSV de vocabulario y en la cabecera de los dos informes de validación** — la ficha que gobierna el **ciclo agrupado de los siete residuos** de `validacion.py`. Cerrada por la **opción A que aprobó Francisco**: `validacion.py` **importa `config.py`** (`:55`) y estampa `config.commit_actual()` (`:111`) en los **cuatro artefactos**. **Cruza una frontera que se documentaba como inexistente** —`program.py` y `validacion.py` no dependían de `config.py`—: registrado en `resumen-de-decisiones.md` que la decisión **CONSUME Q2 y EXTIENDE su alcance de rutas a procedencia**, y **explícitamente NO como permiso literal**, porque Q2 hablaba de rutas y `commit_actual()` no es una ruta. **`program.py` NO pasa a depender de `config.py`**; actualizadas en consecuencia la frase de independencia de `CLAUDE.md`, la cabecera de `config.py` y `PIPELINE.md`. Sello: **`fc1c6b4-sucio`**, fecha por invocación (54 → `20:53:27` · 122 → `20:53:46`), **pendiente de re-anclaje** al commit de cierre — **ficha propia abierta**, sin ningún hash inventado. **Hechos del ciclo, comunes a las siete filas:** **dos pasadas de `auditor-ml`, ambas APTO CON CAMBIOS, ambas aplicadas** —la primera con **seis afirmaciones falsas**, documentación escrita **en presente antes** de la corrida—. **Una sola corrida y ninguna cifra publicada se mueve:** diff de `Resultados/` contra `fc1c6b4` caracterizado, **cero diferencias fuera de las cuatro clases esperadas**; intactos `Integridad: APROBADA`, D1 67.343 / D2 22.544 / D3 58.630 / 9.711 normales (43,1 %), drift (A) 37 y 44 · (B) 25 y 31, outliers 4,78 % y 2,44 % con el rótulo «media entre características», **los 17 tipos 0-day byte a byte** (total 3.750, 16,63 %) y el one-hot 77→122 con desglose `service` +44 / `flag` +1 / `protocol_type` +0. Zanjado además: las **12 figuras son byte-idénticas** a HEAD (generación determinista), los **splits NO se regeneraron** (mtime del 2026-07-05) y **ningún `metricas_*.csv`** se tocó. **Dato que merece quedar escrito:** el defecto de afirmar en presente algo que la corrida no respalda **reapareció en un sitio nuevo en cada vuelta**, y se trató bien: **nota fechada que la supera, sin reescribir el texto histórico** | `9af842c` |
| 2026-08-11 | Código | **`PIPELINE.md` y `GUIA_RESULTADOS.md` al día — y el recuadro que MENTÍA ya no miente.** Era el 🟠 del grupo: `PIPELINE.md:141-146` atribuía los informes y las 12 figuras que hay en disco a la corrida `274923d`-sucio del **2026-08-10** «todos con marca de tiempo de esa re-corrida» y remataba «**hay que creerse este recuadro**» (`:152`) — pedía crédito explícito que no merecía. Reatribuido a la corrida del **2026-08-11** y puestos al día `Implementacion/PIPELINE.md:43-45,103-108,139-153` y `Resultados/GUIA_RESULTADOS.md:16,§3.2`, que además **ya listan el artefacto nuevo** `*_vocabulario_onehot.csv`. La tabla canónica del sello `commit` vive hoy en **`PIPELINE.md:994`** (encabezado) **+ `:1001-1005`** (los tres valores), **verificado en disco el 2026-08-12**. **La referencia se ha desplazado dos veces y esta fila deja la traza**: era `:879-888`, pasó a `:952-963` al cerrar este ciclo (2026-08-11) y el clúster de cinco fichas de `PIPELINE.md` del **2026-08-12** volvió a moverla ~40 líneas hasta `:994` + `:1001-1005`. Sale en el ciclo agrupado de los siete; dictamen y verificaciones, en la fila de arriba | `9af842c` |
| 2026-08-11 | Código | **El 77 del delta 77→122 ya se publica rotulado como RECONSTRUCCIÓN.** No es el vocabulario que el pipeline usó en su día: se **recuenta** desde los CSV `_original_*`, así que sin rótulo cualquiera podía leerlo como cifra registrada por `program.py`. El token `RECONSTRUIDO` va ahora **en consola y en el informe** (`validacion.py:977` y `:1230`), en las dos variantes. Cambio de rótulo, **no de cálculo**: el 77, el 122 y el 45 siguen **recontándose, cero literales**. Sale en el ciclo agrupado de los siete | `9af842c` |
| 2026-08-11 | Código | **Los recuentos del CSV de vocabulario one-hot ya son enteros.** `38.0 / 77.0 / 122.0 / 45.0` pasan a `38 / 77 / 122 / 45` en la fila `__total__` de los dos `*_vocabulario_onehot.csv`. Son recuentos: publicarlos como flotantes invitaba a leerlos como promedios. Sale en el ciclo agrupado de los siete | `9af842c` |
| 2026-08-11 | Código | **El encabezado «Recomendaciones:» ya no se imprime vacío.** Ahora solo se escribe **si hay alguna** (`validacion.py:1102`, `:1122`), con la condición documentada en el propio código. Efecto verificado en disco: la variante de **54 pierde el encabezado** —no tenía recomendaciones que dar— y es una de las cuatro clases de diferencia esperadas del diff. Un encabezado vacío en un artefacto publicado invitaba a pensar que se había perdido algo. Sale en el ciclo agrupado de los siete | `9af842c` |
| 2026-08-11 | Código | **Las constantes importadas de `program.py` ya son copia, no alias.** `validacion.py` envuelve en `list(...)` (`:156-157`, **antes `:100-101`: no citar más esas líneas**) `COLUMNAS_CATEGORICAS` y `COLUMNAS_NO_CARACTERISTICA`, igual que hace `program.py:65` con la canónica de `program.py:36-37`. Era **inerte hoy** —todos los usos son de lectura— pero una **mutación futura habría contaminado el one-hot real sin dejar rastro**. Arreglo de una línea, **sin re-correr nada obligado**. Sale en el ciclo agrupado de los siete | `9af842c` |
| 2026-08-11 | Código | **El comentario de la cabecera de `validacion.py` ya no miente, y el orden de import queda DECLARADO como requisito.** Decía que `program.py` no tiene efectos al importarse, cuando sí los tiene (`program.py:12`, `:16-23`, `:26-27`: `warnings.filterwarnings`, reconfiguración de `stdout`, `plt.style.use('default')` y `sns.set_palette`). Reescrito (`validacion.py:13-33`) enumerando los cuatro efectos y declarando la **consecuencia load-bearing**: el `import program` (`:33`) **debe quedar por encima** del bloque `plt.style.use` / `sns.set_palette` / `plt.rcParams`; movido por debajo, el `plt.style.use('default')` de `program.py` **borraría `figure.figsize`** y las 12 figuras cambiarían de tamaño **en silencio**. Documentado además que `import config` (`:55`), a diferencia de aquél, **no tiene efectos al importarse** —`ensure_dirs()` y `setup_utf8()` existen pero no se llaman a nivel de módulo—, así que su posición **no** es load-bearing. Sale en el ciclo agrupado de los siete | `9af842c` |
| 2026-08-11 | Código | **El 4,78 % / 2,44 % de outliers de D1 ya se publica como MEDIA, no como «mediana».** Se cambió el **nombre, no el cálculo**: `.mean()` sigue donde estaba (`validacion.py:978`, era `:968`) y **las cifras 4,78 % y 2,44 % siguen siendo válidas**. El rótulo del informe pasa a **«Outliers D1 (media entre características)»**, y corregidos `Resultados/GUIA_RESULTADOS.md` (`:117`, `:276-281`, `:379-381`, `:394`) e `Implementacion/PIPELINE.md:54-55`. **La verificación que importaba:** el auditor comprobó que **no se corrigió ninguna mediana legítima** por error — `cascada_invertida.py:296`, `PIPELINE.md:832,864-865,746` y `conf_mediana_argmax` **siguen intactas**. Re-corrido en las dos variantes (19:51-19:52): `git diff 6ae4554 -- Resultados/` da **una única línea cambiada por informe**, la del rótulo, y los dos `*_vocabulario_onehot.csv` **byte-idénticos**; todo lo demás igual —17 tipos 0-day, 3.750 (16,63 %), delta 77→122, KS (A: 37/54 y 44/122 · B: 25/54 y 31/122), conteos, `Integridad: APROBADA`—. Dictamen de `auditor-ml`: **APTO CON CAMBIOS**, ningún hallazgo 🔴, **ninguna cifra publicada cambia**. **Residuo que dejó:** el vault (`4.2:107`) seguía diciendo «mediana» — **cerrado en `7c0659f`** | `84e3c8f` |
| 2026-08-11 | Código | **`COLUMNAS_CATEGORICAS` y `COLUMNAS_NO_CARACTERISTICA` dejan de estar duplicadas por copia.** **Ejecutada, no aceptada como deuda** — decisión explícita de Francisco sobre la ficha que quedó pendiente de su criterio. Son ahora **constantes de módulo** en `program.py:36-37`, y `validacion.py` las **importa** (hoy en `validacion.py:156-157`, tras el arreglo del alias). **Camino elegido: `import program`** —fuente canónica, que es quien hace el one-hot— en vez de subirlas a `config.py`, que **sí habría violado** la restricción de `CLAUDE.md`: `program.py` y `validacion.py` no dependen de `config.py`. **La verificación que importaba:** el **orden** de la lista **no puede alterar ningún artefacto**, porque `program.py:310-311` fija `train_cols = sorted(set(D1) | set(D3))` y `:316` reindexa las tres matrices con esa lista — el orden final es **alfabético e independiente del one-hot**. Solo importa la **pertenencia**, corroborada por los CSV (38 numéricas + 39/84 dummies = 77/122) y por el contraste independiente del `.joblib`. **Sin import circular**, `argparse` bajo `__main__`, **cero `fit`**, y **los splits en disco NO se regeneraron porque no hacía falta**. Re-corrido con la ficha del rótulo (19:51-19:52), mismo diff de una línea por informe. Dictamen de `auditor-ml`: **APTO CON CAMBIOS**, ningún hallazgo 🔴. **Residuos que dejó, los dos ya cerrados:** el alias (compartía objeto lista) y el comentario falso del orden de import | `84e3c8f` |
| 2026-08-11 | Código | **`validacion.py:282` · La lista nominal de los 17 tipos 0-day ya se persiste en el informe.** Cerrada completando el WIP de `d9225be` **sin reescribir sus ~231 líneas**: el cambio queda confinado a `_save_report()` (`:1080-1142`). `_save_report()` ya escribe la lista nominal completa —**tipo, categoría, instancias, total y % de D2**— con **tres ramas de degradación**, así que los 0-day dejan de quedarse solo en consola, que era la deuda. **El 17 sigue siendo emergente, no una lista a mano** (`:340`), y el auditor verificó que **los 17 tipos coinciden uno a uno con `metricas_hibrido_0day.csv`**. Re-corrida en las **dos variantes**: `EXITCODE=0`, `Integridad: APROBADA`, **16 artefactos regenerados** en `Resultados/` (2026-08-11 19:28), **ningún `metricas_*.csv` y ningún `.joblib` tocados**. Con esto **queda desbloqueada la ficha del `4.2`**, que cita el informe que esta re-corrida regenera. Dictamen de `auditor-ml`: **APTO CON CAMBIOS** — los cambios salen como residuos, ninguno 🔴. Commit previo del WIP: `d9225be` | `6ae4554` |
| 2026-08-11 | Código | **`validacion.py:283` · El delta 77→122 del fix one-hot ya vive en un artefacto regenerable.** El parámetro `onehot` de `:991` **deja de ser *dead parameter***: ahora se lee y se escribe el delta **con desglose por columna categórica**, y nace el artefacto **`Resultados/specialized_nsl_kdd_vocabulario_onehot.csv`** (más su gemelo `_sin_seleccion_`), vía el helper nuevo y contiguo `_guardar_csv_vocabulario_onehot()` (`:1144-1201`). Las **~148 líneas** de `medir_vocabulario_onehot()` **no se reescribieron**. **Resultado que hay que leer bien: el delta sale 77→122 en las DOS variantes**, no 77→54 en la de 54 — **correcto por construcción y verificado en código**: el one-hot ocurre en `program.py:283`, `select_features()` se invoca **después** (`:1148-1150`) y los CSV `_original_*` se escriben **pre-one-hot** (`:650-652`). Queda **declarado en los dos informes**. **Cero literales**: el 17, el 77, el 122 y el 45 se **recuentan** (verificado por el auditor). Dictamen de `auditor-ml`: **APTO CON CAMBIOS**. Commit previo del WIP: `d9225be` | `6ae4554` |
| 2026-08-11 | Código | **`validacion.py:284` · Comparación de columnas D2/D3 por orden, re-corrida — y la incógnita se resuelve EN NEGATIVO.** Era la mitad que faltaba: el fix estaba en `d9225be` pero **nadie lo había corrido**, así que no se sabía si destapaba un desajuste real. **Ya se sabe: NO destapó ningún desajuste D2/D3.** Los CSV que deja `program.py` **ya estaban alineados posicionalmente en ambas variantes**; la comparación por conjunto **no ocultaba nada**. Es un **resultado, no un no-hallazgo**: la rama de diagnóstico «mismo conjunto, distinto orden» queda como red de seguridad, no como parche de un bug vivo. Verificado además por el auditor en la misma pasada: **cero `fit`**, salvedad del KS **impresa en ambos informes**, KS **coincidente con lo publicado** —(A) **37/54** y **44/122** · (B) **25/54** y **31/122**— y **alcance respetado**. Dictamen de `auditor-ml`: **APTO CON CAMBIOS**. Commit previo del WIP: `d9225be` | `6ae4554` |
| 2026-08-10 | Código | **T3 · Medición de la cascada invertida.** Script nuevo `Implementacion/app/cascada_invertida.py` (clase `NSLKDDInvertedCascadeMeasurer`): medición **contrafactual y fuera del sistema** que pasa las **9.711 filas normales de D2** por el clasificador de firmas **ya persistido** (`firma_RandomForest_<set>.joblib`) y cuenta cuántas condenaría con confianza ≥ `UMBRAL_CONF`. **Cero `fit`**, solo inferencia; y el umbral se lee de `hibrido_<set>.joblib::umbral_conf_elegido`, **nunca como literal** — si falta el descriptor, **aborta**. Resultados: variante **54 → 6.558 condenadas (67,53 %)**; variante **122 → 3.329 (34,28 %)**. Salida en `Resultados/metricas_cascada_invertida.csv` (**10 filas**, tabla propia: no toca ninguna de las cuatro principales) y dos figuras. **Matiz conceptual que impuso la auditoría y que manda al citar:** la fila `__global__` es una **cota inferior de falsos positivos irrecuperables**, **no** «el FPR de un sistema de firmas-primero» — en el sistema publicado `unknown` es alarma (decisión **P-5**, respaldada por símbolo: `hibrido.py::_ensamblar_prediccion`), así que lo que cae bajo umbral **no queda exonerado**. La lectura y los números viven en `Implementacion/PIPELINE.md`, sección «La cascada invertida (T3)». **No cierra `T9`**: solo la alimenta (viñeta `3.2.2`), y allí queda anotada la cifra con su salvedad. Dictamen de `auditor-ml`: **APTO** | `b1f1df2` |
| 2026-08-10 | Código | **T2 · KS de D1 contra los normales de D2.** Añadido en `Implementacion/app/validacion.py` **sin sustituir** el KS existente: ahora son **dos mediciones separadas y no intercambiables** — **(A)** D1 vs D2 completo: **37/54** y **44/122** características con drift; **(B)** D1 vs las **9.711 normales de D2**: **25/54** y **31/122**. `src_bytes` cae de **0,346 a 0,091** y `dst_bytes` de **0,317 a 0,107**. El `delta = (A) − (B)` se publica como **comparación, nunca como descomposición aditiva** —el KS es un supremo de diferencia de CDF y no es aditivo sobre una mezcla—, y la salvedad quedó **impresa en los dos informes de validación**. **Efecto colateral no previsto:** `validacion.py` **nunca se había corrido en la variante 122**; ahora sí, con informe nuevo (`Resultados/specialized_nsl_kdd_sin_seleccion_validation_report.txt`) y **6 figuras nuevas**. De paso aparecieron **dos cifras inventadas preexistentes** en `Resultados/GUIA_RESULTADOS.md` («34 features», «85 % de drift»), **con destino explícito a §4.2.1 y §5.1**: corregidas a **37** y **68,5 %** contra el artefacto real. Invariantes verificadas **cuatro veces** por `auditor-ml`: cero `fit`, cero recalibración, **D2 solo se reporta** (H-4/P-4 intactas); los **8 `metricas_*.csv` previos sin reescribir** (222 filas, `semilla = 42`, `commit = 1163c90`), y `CLAVE_UNICIDAD`, `_limpiar_variante_csv`, `comprobar_recuento()` y `COLUMNAS_MINIMAS` **sin tocar** — no hubo que re-correr el runbook. **No cierra `T11`**: solo la alimenta (`5.1`/`5.4`), donde quedan anotadas las cifras y la salvedad del `delta`. Dictamen de `auditor-ml`: **APTO** | `b1f1df2` |
| 2026-08-09 | — | **T0 · Retirada de la regla «lo escribe Francisco».** Aplicadas las dos velocidades de la decisión marco (b) del lote 2026-08-06, en **15 ficheros (+96 −92)**: `CLAUDE.md`, `features.md`, `.claude/agents/redactor-tfg.md`, el callout de las **8 notas** del capítulo 2, `resumen-de-decisiones.md:560`, el MOC `00 Índice TFG.md` (5 sitios) y la nota `2.2.1:52`. La ficha **subestimaba el alcance**, así que hubo que barrer **por contenido y no por la lista**: varias ubicaciones no llevaban el callout literal sino la misma regla escrita de otra forma («la redacción corresponde a Francisco», «✍ teoría (Francisco)»). **Decisión de Francisco tomada al cerrar: `2.1.4` NO queda exceptuada** — entra en la retirada completa de `2.x`, porque exceptuar una sola nota reintroduciría a mano la regla recién retirada del capítulo entero; **con eso T25 queda desbloqueada, y con ella T24**. **Deliberadamente sin tocar:** `next-steps.md:382,387,421`, congelado e historial del 2026-07-15; reescribirlo falsearía lo que se decidió entonces. **No es deuda pendiente.** **Residuo sin ficha, señalado y no tocado, PENDIENTE DE DECISIÓN DE FRANCISCO desde el 2026-08-09 y aplazado el 2026-08-11:** `resumen-de-decisiones.md:459` dice «queda como divergencia a corregir por Francisco al redactar» — roza la regla retirada pero **no es la misma cosa** (habla de una divergencia terminológica concreta en `2.2.4`, «detectores no supervisados», no de la autoría de un capítulo). Solo tiene **dos salidas: ficha propia en `## Abiertas` o descarte expreso**, y **plantearlo ANTES de repartir trabajo**, no al cerrar sesión, que es lo que lo ha aplazado dos veces. Las **2 notas de `99 Investigación/`** que dicen que `6.2` la redacta Francisco son trabajo de **T17**. **Fuera del alcance de T0 pero corregido en el mismo ciclo, con aprobación de Francisco:** `how-to-work.md:32` decía «no te fíes de la prosa de `next-steps.md`/bitácora» cuando desde el 2026-08-01 el registro operativo vivo es `features.md` | `d6dae35` |
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
