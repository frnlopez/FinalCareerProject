---
titulo: "¿Es aplicable el aprendizaje continuo y el Nested Learning de Google al H-NIDS sobre NSL-KDD?"
numero: "-"
estado: informe
docx_ref: "-"
---

# ¿Es aplicable el aprendizaje continuo y el *Nested Learning* de Google al H-NIDS sobre NSL-KDD?

- **Encargo:** documentar y verificar el veredicto ya cerrado por Francisco —*Nested Learning no
  es aplicable a este TFG porque los registros de NSL-KDD no tienen marca de tiempo y por tanto
  no hay no-estacionariedad que explotar*— y delimitar «qué podemos hacer y qué no» antes de
  redactar las líneas futuras (6.2). Cuatro preguntas: (1) qué propone NL; (2) por qué no se
  puede aplicar aquí, con razón técnica verificada contra el código; (3) qué sí es posible con
  NSL-KDD; (4) qué sería posible con otros datasets.
- **Fecha:** 2026-08-01
- **Alcance:**
  - **Entra:** el artículo de Nested Learning (Behrouz et al.) leído entero en sus partes
    relevantes; verificación en disco de cada afirmación sobre el código del proyecto; contraste
    acotado sobre (a) si NL se ha aplicado fuera de modelos de secuencia/LLM y (b) qué se usa hoy
    en NIDS frente a la deriva; y el diseño en papel de lo que sí sería importable.
  - **Queda fuera** (por encargo): barrido del estado del arte de *continual learning*,
    comparativa de arquitecturas de memoria, y todo lo relativo a TabNet, *benchmarks* o
    clasificadores tabulares —van en otros informes.
- **Alimenta a:** [[6.2 Líneas futuras]] (respaldo en `EL_FUTURO.md`).

> [!info] Corrección del 2026-08-18 — autoría de `6.2`
> Este informe se escribió el 2026-08-01, cuando `6.2 Líneas futuras` estaba reservada a Francisco;
> por eso el resto del texto habla de «material para que Francisco escriba 6.2». Esa reserva
> **caducó el 2026-08-06** con la **decisión marco (b)** del *grill* de los cuatro informes
> (`resumen-de-decisiones.md`, § Decisiones del 2026-08-06): `6.2` pasó a **borrador redactado por
> el `redactor-tfg` con revisión final de Francisco**. La nota se redactó así en la **Tanda 7**
> (T12, 2026-08-15) y **la revisión final de Francisco sigue pendiente**. Se conserva la redacción
> original del cuerpo como rastro histórico: donde dice «Francisco escribe 6.2», léase «el
> `redactor-tfg` redacta el borrador y Francisco lo revisa».

> [!warning] Este informe no es memoria
> Es insumo citable. No entra en [[00 Índice TFG]] y su prosa no se copia a un capítulo sin que
> lo decida Francisco.

## Respuesta corta

El veredicto **se confirma, y por una razón más fuerte que la enunciada**. No solo falta el eje
temporal: los propios autores de NL sitúan su aportación de optimizador en el caso de datos
**no i.i.d.** con elementos fuertemente dependientes (tokens de una secuencia), y declaran que el
descenso de gradiente clásico ya es adecuado para muestras i.i.d. —que es exactamente lo que son
los registros por flujo de NSL-KDD. A eso se suman dos bloqueos verificados en disco: siete de
los ocho modelos del sistema no se entrenan por gradiente, y el único que sí (`MLPRegressor`) no
expone en scikit-learn ningún punto donde sustituir el optimizador. Fabricar la no-estacionariedad
troceando D1 o D3 produce un **artefacto experimental**, no una medida de deriva. El cuello de
botella no es la librería: **es el dataset**, lo que fusiona esta línea futura con la de
generalización cruzada ya escrita en `EL_FUTURO.md:93-95`.

## Hallazgos

### 1. Qué propone Nested Learning como mecanismo de aprendizaje continuo

**Versión canónica localizada.** El PDF del perímetro (`abehrouz.github.io/files/NL.pdf`, hoy
redirigido a `alibehrouz.com/files/NL.pdf`) es la copia del autor, **nivel 2**. Existe versión
canónica: *Advances in Neural Information Processing Systems 38 (NeurIPS 2025)*, Main Conference
Track, y el propio PDF lo declara en su nota al pie de la p. 1 —«*A version of this work is
published at Neural Information Processing Systems (NeurIPS) 2025*». Con eso la fuente **sube a
nivel 1** y se cita por las actas. (Discrepancia menor de título entre copias: ver
`## Lo que no he podido confirmar`.)

**La tesis central.** NL representa un modelo de ML **y su procedimiento de entrenamiento** como
un conjunto de problemas de optimización *anidados, multinivel y/o paralelos*, cada uno con su
propio «flujo de contexto» (*context flow*) y su propia **frecuencia de actualización**. La
afirmación fuerte del artículo es que arquitectura y optimización «son fundamentalmente el mismo
concepto, pero en niveles distintos de un sistema, con contextos distintos (gradientes frente a
*tokens*)» (§1.2). Bajo esa lente, un Transformer no es «capas apiladas» sino capas lineales con
frecuencias de actualización distintas: la atención opera a frecuencia ∞ y los bloques MLP a
frecuencia 0 tras el pre-entrenamiento (§1.1 y Fig. 5, p. 30).

**Frecuencias y motivación neurofisiológica.** El diseño se inspira en las ondas cerebrales: el
cerebro no usa un reloj centralizado; las neuronas rápidas (gamma, 30-150 Hz) procesan
información sensorial y las lentas (delta/theta, 0.5-8 Hz) consolidan memoria (§1.1). En NL, cada
parámetro pertenece a un nivel con una frecuencia propia; los niveles altos se adaptan rápido al
contexto inmediato y los bajos integran información a largo plazo.

**Memoria asociativa como formalismo unificador.** Cada nivel se modela como una memoria que
comprime su flujo de contexto mapeando claves a valores. §5 reescribe con ese formalismo la
atención *softmax* (solución **no paramétrica** de una regresión ℓ₂ con estimadores
Nadaraya-Watson, ec. 62), la atención de ventana deslizante (ec. 63), la atención lineal / RNN con
regla hebbiana (ec. 64) y DeltaNet con regla delta (ec. 65).

**Dónde vive exactamente la aportación: en ambos, y explícitamente en su unión.** Las tres
contribuciones de §1.2 se reparten así:

| Contribución | Dónde vive | Qué es |
|---|---|---|
| *Deep / Expressive Optimizers* (§4) | **Optimizador** | SGD-momentum, Adam y AdaGrad se demuestran memorias asociativas que comprimen gradientes; se descomponen en dos niveles de optimización anidados. De ahí salen **Delta Momentum** (ec. 48-49), **DMGD** (ec. 50), **Delta Gradient Descent (DGD)** (ec. 57) y el optimizador **M3** (*Multi-scale Momentum Muon*, Alg. 1, p. 29) |
| *Self-Modifying Titans* (§8.1) | **Arquitectura** | Modelo de secuencia que aprende su propio algoritmo de actualización y genera sus propios valores (ec. 83-88) |
| *Continuum Memory System* (CMS, §7) | **Arquitectura** | Sustituye los bloques MLP del Transformer por un espectro de bloques con frecuencias de actualización distintas; el bloque de nivel *s* se actualiza cada ⌈C⁽ˢ⁾/C⁽ˢ⁺¹⁾⌉ pasos |
| **HOPE** (§8.3) | Ambas | Titans auto-modificantes + CMS. Es el modelo con el que evalúan |

Es decir: **no se puede coger «solo el optimizador» ni «solo la arquitectura» y decir que se está
aplicando NL** —el propio marco sostiene que la separación entre ambos es la ilusión que da
título al artículo.

**Cómo ataca el olvido catastrófico.** Dos mecanismos distintos: (i) en el optimizador, §4.3
muestra que con β=0.9 los últimos 43 gradientes concentran el 99 % del momento, de modo que el
momento «olvida» el subespacio de gradientes de tareas anteriores y arrastra los pesos hacia
direcciones que dañan lo aprendido; Delta Momentum y M3 amplían esa memoria. (ii) en la
arquitectura, CMS retiene en los bloques de baja frecuencia lo que los de alta frecuencia
sobrescriben, y la transferencia entre niveles «hace circular» el conocimiento (§7.1, «*CMS Design
Helps with Continual Learning*»).

**Qué entiende NL por aprendizaje continuo.** «*Continual learning puede verse como un problema de
aprendizaje sobre una **secuencia de contextos o episodios entrantes**, donde niveles distintos se
encargan de comprimir su propio contexto y transferirlo a niveles superiores*» (§1.2). La
definición operativa **presupone una secuencia**: sin ella, el marco no tiene sobre qué anidar
frecuencias.

**Sobre qué datos lo evalúan (§9).** Modelado de lenguaje y razonamiento de sentido común;
comprensión de contexto largo (*needle-in-a-haystack*, BABILong); *recall* y memorización
in-context; reconocimiento de lenguaje; comparación de optimizadores; y aprendizaje continuo,
incluido **class-incremental learning** —que se evalúa **en dominio de texto**: CLINC, Banking y
DBpedia, con *backbones* Llama3-3B y Llama3-8B (Fig. 6, p. 33). **Ni un solo experimento sobre
datos tabulares.**

### 2. Por qué NO se puede aplicar aquí

Cuatro bloqueos encadenados, de lo conceptual a lo operativo. Todos verificados: los del código,
en disco con `fichero:línea`; los del artículo, contra el PDF.

#### 2.1 No hay eje temporal — y sin eje temporal no existe la «secuencia de contextos» que NL requiere

Las columnas del dataset están declaradas en `Implementacion/app/program.py:37-50`: 41
características más `attack` y `level`. **Ninguna es una marca de tiempo.** Las dos candidatas
aparentes no lo son:

- `duration` (`program.py:38`) es la **duración del flujo** —una magnitud escalar, no una posición
  en una línea de tiempo. Dos flujos con `duration=5` no guardan ninguna relación de orden entre sí.
- `level` (`program.py:49`) es el índice de dificultad de NSL-KDD, no un instante.

Y los splits tampoco introducen tiempo por la puerta de atrás: **D1 y D3 se construyen por puro
filtrado de etiqueta** —`train_df[train_df['attack'] == 'normal']` (`program.py:166`) y
`train_df[train_df['attack'] != 'normal']` (`program.py:195`)— y D2 es el fichero de test
completo. No hay ninguna partición inducida por un criterio temporal en todo el pipeline
(`program.py` no contiene ni `sort_values` por tiempo ni `train_test_split`: su único
`sort_values`, en la línea 501, ordena importancias de características).

Esto tiene una consecuencia que va más allá de NL y que está documentada en la literatura de
seguridad: sin marca de tiempo **no se puede siquiera construir un split temporal válido**.
TESSERACT (USENIX Security 2019) formaliza el «sesgo temporal» como una de las dos fuentes
sistemáticas de resultados inflados en clasificación de *malware*, y sus restricciones de diseño
experimental —igual que su métrica AUT— exigen ordenar cronológicamente los objetos. Un dataset
sin reloj no admite ese protocolo. Es la misma imposibilidad, enunciada desde el otro lado.

#### 2.2 El propio artículo sitúa su aportación en el caso NO i.i.d. — y aquí los datos son i.i.d.

Este es el argumento más fuerte y no estaba en el enunciado del veredicto. En §4.5, justificando
por qué hace falta ir más allá del descenso de gradiente, los autores escriben (p. 20):

> «*While this design can be effective for nested problems with independent elements, i.i.d.
> samples for training, it can be restrictive for context with highly dependent elements (e.g.,
> tokens in a sequence).*»

Y en §1.2 presentan DGD como una variante «*cuya actualización no solo depende de la entrada
actual, sino también del estado del peso, capturando así las dependencias entre muestras de datos
**sin la suposición i.i.d.***». En §8.2 el mecanismo se apoya directamente en que «*sabemos que los
tokens están altamente correlacionados*» (p. 32).

Los registros de NSL-KDD son vectores de características por flujo, sin orden, y en este proyecto
se procesan como muestras intercambiables. **Por el propio criterio de los autores, este es el caso
en el que el descenso de gradiente estándar ya es el algoritmo adecuado** y la aportación de NL no
tiene de qué agarrarse. Aplicarlo aquí no es «difícil»: es usar una herramienta contra el supuesto
que la motiva.

#### 2.3 Siete de los ocho modelos del sistema no se entrenan por gradiente

La maquinaria de NL —niveles de optimización, momento como memoria entrenable, precondicionadores,
frecuencias de actualización— presupone un modelo entrenado por descenso de gradiente. En este
sistema eso deja fuera a casi todo:

| Etapa | Modelos | ¿Gradiente? | Verificado en |
|---|---|---|---|
| 1 (anomalías) | IsolationForest, OneClassSVM, LocalOutlierFactor | **No** | `anomalias.py:41-43` |
| 1 (anomalías) | Autoencoder = `MLPRegressor` | **Sí** | `anomalias.py:44`, `anomalias.py:179` |
| 2 (firmas) | DecisionTree, RandomForest, KNN, HistGradientBoosting | **No** | `firmas.py:45-47`, `firmas.py:66` |
| Control | RandomForest monolítico (`baseline.py`) | **No** | — |

El **único punto de anclaje posible en todo el H-NIDS es el autoencoder de la etapa 1**, y ni
siquiera es un autoencoder «de verdad»: es un `MLPRegressor` que reconstruye su entrada
(`model.fit(X_fit, X_fit)`, `anomalias.py:198-199`) y cuyo *score* de anomalía es el MSE de
reconstrucción (`anomalias.py:216-218`). La cabecera del script prohíbe explícitamente el
alternativo: «*Autoencoder implementado como MLPRegressor (fit(X, X)); PROHIBIDO TF/Keras*»
(`anomalias.py:12`).

#### 2.4 Y en ese único anclaje, scikit-learn no expone el optimizador

Aunque se aceptara trabajar solo con el autoencoder, `MLPRegressor` no ofrece dónde enchufar nada
de NL:

- **El optimizador es una cadena, no un objeto.** El parámetro `solver` toma uno de
  `{'lbfgs', 'sgd', 'adam'}` y por defecto `'adam'`
  (`Imp/Lib/site-packages/sklearn/neural_network/_multilayer_perceptron.py:1682`). No hay forma de
  pasar un DGD, un Delta Momentum o un M3: **la aportación de optimizador de NL no tiene punto de
  entrada.**
- **El entrenamiento incremental existe, pero choca con la configuración actual.**
  `MLPRegressor.partial_fit` está definido en `_multilayer_perceptron.py:1776` —el mecanismo por
  ráfagas es real y no exige dependencias nuevas—, pero el modelo se construye con
  `early_stopping=True` (`anomalias.py:178-184`, línea 181) y sklearn **rechaza esa combinación de
  forma explícita**: «*partial_fit does not support early_stopping=True*»
  (`_multilayer_perceptron.py:638-640`). Pasar a ráfagas obliga a **retirar el criterio de parada
  actual** —que es justamente el que permite parar sin mirar D2 (`anomalias.py:178`)— y a inventar
  otro. Eso ya no es un cambio cosmético: toca el protocolo.
  > Detalle menor verificado: el guardián de `partial_fit` en `MLPRegressor`
  > (`_multilayer_perceptron.py:1774`, `@available_if(lambda est: est._check_solver)`) no invoca
  > el comprobador, a diferencia del de `MLPClassifier` (línea 1293, con paréntesis). Es
  > irrelevante en la práctica porque el *solver* por defecto es `'adam'`, que sí es estocástico
  > (`_multilayer_perceptron.py:851-857`).
- **La arquitectura de NL no admite entradas tabulares.** Titans auto-modificantes, CMS y HOPE
  operan sobre secuencias: proyectan el *input* en claves, valores y consultas (§8.1, ec. 76-79) y
  se entrenan por *chunks* de una secuencia de longitud L (§8.2, ec. 90). Un vector de 54
  características de un flujo aislado es una secuencia de longitud 1: el aparato entero degenera.

#### 2.5 Dictamen: fabricar la no-estacionariedad produce un artefacto, no una medida de deriva

El enunciado del veredicto planteaba dos formas de fabricar la deriva ausente. Dictamen razonado:

**(a) Trocear `D1_train` al azar → ráfagas i.i.d.** Confirmado: no hay nada que medir. D1 es
íntegramente tráfico normal (`program.py:166`) y un troceo aleatorio produce muestras de la misma
distribución. Sin cambio de distribución entre ráfagas no hay olvido catastrófico, y la curva de
rendimiento sale plana. El experimento no fracasaría: **es que no mide nada**.

**(b) Estratificar D1 por `protocol_type` / `service` → *covariate shift* sintético.** Aquí sí
habría cambio de distribución medible entre ráfagas, pero es un cambio **inducido por el
experimentador sobre una columna que el propio modelo recibe como característica**. Responde a
«¿olvida el autoencoder el tráfico UDP si lo entreno primero solo con TCP?». Es un estudio de
sensibilidad legítimo y honesto **si se etiqueta como tal**; no es evidencia de que el sistema
resista la deriva real del tráfico. Presentarlo como «análisis de deriva de concepto» sería un
artefacto.

**(c) Trocear D3 por categoría → protocolo *class-incremental*.** Es el caso más interesante,
porque **el propio artículo de NL usa ese protocolo** (Fig. 6, p. 33). Tres objeciones, en orden
de peso:

1. Mide **olvido catastrófico de un clasificador entrenado por tareas**, no deriva temporal del
   tráfico. Son fenómenos distintos y no se deben confundir en la memoria.
2. **El orden de las clases lo elige el experimentador.** El resultado depende de una decisión
   arbitraria (¿dos→probe→r2l→u2r? ¿al revés?) que ninguna propiedad del dataset justifica. La
   deriva real es interesante precisamente porque el orden **no** lo controla nadie.
3. Es incompatible con la etapa 2 tal como está: DecisionTree, RandomForest, KNN e
   HistGradientBoosting (`firmas.py:66`) no admiten entrenamiento por tareas sucesivas. Habría que
   **sustituir el modelo de la etapa 2**, no solo el protocolo, y con ello se pierde la extracción
   de reglas legibles que da sentido a esa etapa.

**Regla que resume el dictamen:** para que un experimento mida deriva, la partición tiene que venir
de un eje que el experimentador **no** controla —el tiempo. Cualquier partición inducida por una
columna del propio dataset es un diseño factorial disfrazado. Con NSL-KDD solo se puede hacer lo
segundo.

#### 2.6 Distinción crítica: un bucle de `partial_fit` NO es Nested Learning

Dictamen explícito, porque es el error de etiquetado más fácil de cometer en 6.2 y el más fácil de
pinchar en una defensa:

| | Bucle de `partial_fit` | Nested Learning |
|---|---|---|
| Niveles de optimización | **Uno** | Dos o más, anidados |
| Frecuencias de actualización | **Una** | Un espectro (§7, CMS) |
| Objetivo interno por nivel | No existe | Cada nivel tiene el suyo (ec. 40, 80-81) |
| Momento / optimizador | Estado interno fijo de Adam | **Memoria asociativa entrenable** (§4) |
| Qué es | Aprendizaje incremental clásico: SGD por minilotes con estado persistente | Un paradigma que reescribe la relación entre arquitectura y optimizador |

Entrenar el autoencoder por ráfagas con `partial_fit` es **aprendizaje incremental clásico**, una
técnica anterior a NL en décadas. Llamarlo «Nested Learning» en la memoria sería inexacto. Y como
la aportación de NL vive también en el optimizador, y `MLPRegressor` no permite sustituirlo
(§2.4), **la parte de NL que quedaría fuera es precisamente la que lo hace NL**.

### 3. Qué SÍ es posible con NSL-KDD pese a esa limitación

Cuatro cosas, ordenadas por relación coste/valor para la memoria.

**3.1 Documentar la imposibilidad con su razón técnica — valor alto, coste nulo.** Es contenido de
6.2 de pleno derecho, y probablemente el más diferenciador de esta línea: la mayoría de trabajos
sobre NSL-KDD proponen «aplicar aprendizaje continuo» como línea futura sin comprobar que el
dataset lo permita. Decir *por qué* no se puede, con la columna que falta y la cita del artículo
que sitúa su aportación en el caso no i.i.d., es una afirmación verificable y poco común.

**3.2 Cuantificar la deriva D1→D2 que YA está medida — valor alto, coste bajo, y no necesita
reloj.** Es la vía más rentable. El sistema ya exhibe una discrepancia distribucional documentada:
el umbral se fija en el percentil 95 sobre D1_val (`anomalias.py:89`, `anomalias.py:259-261`), lo
que debería dar ≈5 % de FPR, pero el FPR real de la etapa 1 sobre D2 es **8-10 %**
(`resumen-de-decisiones.md:345-349`; recogido también en `EL_FUTURO.md:96-97`). Ese exceso es una
medida directa de que los «normales» de D2 no vienen de la misma distribución que los de D1 —un
*dataset shift* real, no fabricado. Cuantificarlo por característica y atribuir el exceso de FPR es
un análisis honesto, con datos ya en disco, y **sin necesidad de marca de tiempo**: no es deriva
*temporal*, es desplazamiento entre particiones, y así debe nombrarse.

**3.3 Aprendizaje incremental por ráfagas como estudio de viabilidad operativa — valor medio, coste
medio.** Mecánicamente posible sin dependencias nuevas: `partial_fit` existe
(`_multilayer_perceptron.py:1776`), D1 ya se parte 80/20 en `D1_train`/`D1_val`
(`anomalias.py:139`) y trocear `D1_train` respeta la disciplina de particiones —D1_val sigue
calibrando el p95 y D2 sigue intocable, luego no hay *leakage*. Lo que mide **no** es olvido
catastrófico (§2.5a) sino otra cosa, legítima y bien delimitada: *¿converge el autoencoder
entrenado por ráfagas a la misma AUC-ROC que el entrenado de una vez, y a qué coste?* Es una
pregunta de despliegue —un NIDS real se actualiza sin re-entrenar de cero— y se responde con el
protocolo actual. Requisito ineludible: retirar `early_stopping=True` y sustituirlo por un criterio
de parada que tampoco mire D2 (§2.4).

**3.4 Estudio *class-incremental* sobre D3 — valor bajo aquí, coste alto.** Posible, pero exige
cambiar el modelo de la etapa 2 y arrastra las tres objeciones de §2.5c. Solo tiene sentido si se
declara como «estudio de olvido catastrófico bajo un orden de clases arbitrario», nunca como
análisis de deriva.

**3.5 Lo que NO es posible, y no debe afirmarse en la memoria.** Cualquier enunciado del tipo «el
sistema se adapta a amenazas nuevas *a lo largo del tiempo*», «resiste la deriva de concepto» o
«aprende continuamente en despliegue» es indemostrable con NSL-KDD. Con este dataset se puede medir
generalización a ataques no vistos (que es lo que ya hace el recall 0-day), pero **no** evolución
temporal.

### 4. Qué sería posible con otros datasets

**4.1 CIC-IDS2017 sí tiene reloj.** Verificado en la ficha oficial del Canadian Institute for
Cybersecurity: los flujos se etiquetan «*based on the time stamp, source and destination IPs,
source and destination ports, protocols and attack*», con más de 80 características extraídas con
CICFlowMeter, y la captura cubre **cinco días laborables consecutivos** —lunes 3 a viernes 7 de
julio de 2017, de 9:00 a 17:00—, con el lunes de tráfico exclusivamente benigno y ataques de martes
a viernes. Eso habilita de golpe: split temporal real (entrenar con los primeros días, evaluar con
los últimos), curva de degradación día a día, y el protocolo de TESSERACT completo (restricciones
de espacio y tiempo, y la métrica AUT de robustez esperada en despliegue).

**4.2 UNSW-NB15: el tiempo es recuperable, aunque no por la vía cómoda.** La ficha oficial de UNSW
documenta 49 características más etiqueta, generadas con Argus y Bro-IDS sobre **100 GB de pcap
crudo**, con particiones publicadas de 175 341 / 82 332 registros. El pcap crudo garantiza que la
información temporal existe en origen; lo que **no** he podido verificar es que las CSV publicadas
expongan las columnas de tiempo (ver `## Lo que no he podido confirmar`).

**4.3 Con eje temporal, el aparato que la literatura NIDS ya usa.** La revisión sistemática de
Shyaa et al. (*Engineering Applications of Artificial Intelligence*, vol. 137, art. 109143, 2024)
cubre 2019-2024 y describe el repertorio vigente: detección de deriva de concepto, algoritmos
adaptativos, monitorización continua y reentrenamiento, articulados en un marco *drift-aware*. Su
conclusión más útil aquí es que **la literatura de deriva de concepto aplicada a ciberseguridad es
escasa**, y que la deriva de concepto y la dinámica de características se estudian por separado en
lugar de conjuntamente. Es decir: con un dataset con reloj, el hueco existe y es atacable con
técnicas ya establecidas —sin necesidad de NL.

**4.4 ¿Y qué aportaría Nested Learning que eso no aporte ya? A día de hoy, nada demostrado en este
dominio.** Dos búsquedas dirigidas no han encontrado **ninguna** aplicación de NL a datos
tabulares, a detección de anomalías tabular ni a NIDS (ver reserva metodológica en
`## Lo que no he podido confirmar`). La ventaja de NL está demostrada donde el artículo la
demuestra: secuencias largas de *tokens* con *backbones* de miles de millones de parámetros. Frente
a «detectar deriva y reentrenar», que es barato y funciona, NL no tiene evidencia a favor en
tráfico de red.

Lo que sí sería **conceptualmente** trasladable, y merece decirse en 6.2 porque conecta con algo ya
escrito: NL se vuelve aplicable en su sentido literal solo si se cambian **a la vez** dos cosas, no
una:

1. **El dataset** → uno con marca de tiempo (eje temporal, §4.1).
2. **La representación** → modelar la sesión o el *host* como una **secuencia de flujos**, en lugar
   de flujos aislados. Y esto es exactamente el límite que `EL_FUTURO.md:98-103` ya identificó con
   datos: `snmpgetattack` (n=178) lo fallan los cuatro detectores en ambos sets de características
   porque apenas perturba las características **por flujo**; harían falta características de
   secuencia o temporales.

Con secuencias de flujos y reloj, un modelo con memoria multifrecuencia deja de ser un extraño en
el problema. Sin las dos cosas, no.

## Lo que no he podido confirmar

- **Que las CSV publicadas de UNSW-NB15 incluyan columnas de tiempo (`Stime` / `Ltime`).** La ficha
  oficial de UNSW no enumera las 49 características y remite a `UNSW-NB15_features.csv`. Los únicos
  sitios donde he visto los nombres son copias de terceros en GitHub y Kaggle y fragmentos de
  buscador —**nivel 3, no sostiene nada**. Lo verificado y citable es que existen 100 GB de pcap
  crudo, de donde el tiempo es recuperable.
- **Texto completo de la revisión de Shyaa et al. (2024).** Elsevier devuelve 403 tanto a `WebFetch`
  como con navegador. El DOI **resuelve** (302 hacia `linkinghub.elsevier.com`, pii
  S0952197624013010) y los metadatos y el resumen están verificados vía la API de OpenAlex, que
  refleja el registro de Crossref. **Todo lo que afirmo de esa fuente sale del resumen, no del
  cuerpo del artículo.** No he intentado sortear el muro de pago.
- **Ninguna aplicación de Nested Learning a datos tabulares, a detección de anomalías tabular o a
  NIDS.** Dos búsquedas dirigidas, sin resultados. Reserva metodológica honesta: **ausencia de
  evidencia no es evidencia de ausencia**, y el artículo es de diciembre de 2025 —ocho meses de
  recorrido a fecha de este informe. La afirmación defendible es «no consta ninguna aplicación
  publicada a agosto de 2026», no «no se puede».
- **Discrepancia de título entre copias del artículo.** La copia del autor titula «*Nested
  Learning: The Illusion of Deep Learning **Architecture***» (singular); las actas de NeurIPS y
  arXiv, «*…Architectures*» (plural). Para la cita hay que usar la forma de las actas.
- **Evidencia que contradiga el veredicto del usuario: no he encontrado ninguna.** Una sola reserva
  explícita, que dejo señalada sin reescribir la tesis: el artículo **sí** evalúa
  *class-incremental learning*, un protocolo de aprendizaje continuo que **no exige marca de
  tiempo** (Fig. 6, p. 33). Eso no valida «aplicar NL a este TFG» —sigue en pie todo §2.3, §2.4 y
  §2.6—, pero matiza el enunciado «sin timestamp no hay ningún protocolo de continual learning
  posible»: lo hay, es sintético, y su dictamen está en §2.5c.

## Fuentes

| # | Fuente | Nivel | Fecha | Cita completa | URL / DOI |
|---|---|---|---|---|---|
| 1 | Nested Learning: The Illusion of Deep Learning Architectures (**versión canónica**) | **1** | 2025-12 | A. Behrouz, M. Razaviyayn, P. Zhong y V. Mirrokni, «Nested Learning: The Illusion of Deep Learning Architectures», en *Advances in Neural Information Processing Systems 38 (NeurIPS 2025)*, Main Conference Track, 2025 | https://proceedings.neurips.cc/paper_files/paper/2025/hash/4309616aaed8e848009bc4a7ef73b493-Abstract-Conference.html |
| 2 | Ídem, preprint en arXiv (usado para verificar identificadores) | 2 | 2025-12-31 | arXiv:2512.24695 [cs.LG]. Campo *comments*: «Published at Neural Information Processing Systems (NeurIPS) 2025» | doi:10.48550/arXiv.2512.24695 |
| 3 | Ídem, copia del autor (**el PDF del perímetro**; es de donde he leído el texto) | 2 | 2025 | Copia en dominio personal del autor. Redirección 301 desde `abehrouz.github.io`. Declara en p. 1 la publicación en NeurIPS 2025 → **usar la entrada nº 1 para citar** | https://alibehrouz.com/files/NL.pdf |
| 4 | TESSERACT: Eliminating Experimental Bias in Malware Classification across Space and Time | **1** | 2019-08 | F. Pendlebury, F. Pierazzi, R. Jordaney, J. Kinder y L. Cavallaro, en *Proceedings of the 28th USENIX Security Symposium*, Santa Clara, CA, 14-16 ago. 2019, USENIX, pp. 729-746. ISBN 978-1-939133-06-9 | https://www.usenix.org/conference/usenixsecurity19/presentation/pendlebury |
| 5 | Evolving cybersecurity frontiers: A comprehensive survey on concept drift and feature dynamics aware machine and deep learning in intrusion detection systems | **1** | 2024-08-22 | M. A. Shyaa, N. F. Ibrahim, Z. Zainol, R. Abdullah, M. Anbar y L. Alzubaidi, *Engineering Applications of Artificial Intelligence*, vol. 137, art. 109143, 2024. **Solo resumen y metadatos: texto completo tras muro de pago** | doi:10.1016/j.engappai.2024.109143 |
| 6 | Intrusion Detection Evaluation Dataset (CIC-IDS2017) — ficha oficial | **1** | consultada 2026-08-01 | Canadian Institute for Cybersecurity, University of New Brunswick. Artículo asociado: I. Sharafaldin, A. H. Lashkari y A. A. Ghorbani, «Toward Generating a New Intrusion Detection Dataset and Intrusion Traffic Characterization», *4th Int. Conf. on Information Systems Security and Privacy (ICISSP)*, Portugal, ene. 2018 | https://www.unb.ca/cic/datasets/ids-2017.html |
| 7 | The UNSW-NB15 Dataset — ficha oficial | **1** | consultada 2026-08-01 | UNSW Canberra Cyber Range Lab. Artículo asociado: N. Moustafa y J. Slay, «UNSW-NB15: a comprehensive data set for network intrusion detection systems», *Military Communications and Information Systems Conference (MilCIS)*, IEEE, 2015 | https://research.unsw.edu.au/projects/unsw-nb15-dataset |
| 8 | «Introducing Nested Learning: A new ML paradigm for continual learning» (blog corporativo de Google Research) | **3** | 2025 | Localizado durante la búsqueda. **Blog de empresa: no sostiene ninguna afirmación de este informe.** Se lista solo para dejar constancia de que existe la versión divulgativa | https://research.google/blog/introducing-nested-learning-a-new-ml-paradigm-for-continual-learning/ |

**Evidencia interna (no son fuentes externas; verificada en disco el 2026-08-01):**
`Implementacion/app/program.py:37-50, 166, 195` · `Implementacion/app/anomalias.py:5-7, 12, 41-45,
89, 139, 178-184, 198-199, 216-218, 259-261` · `Implementacion/app/firmas.py:45-47, 66` ·
`Implementacion/app/hibrido.py:6-9, 154-155` · `Implementacion/app/config.py:16` ·
`Implementacion/requirements.txt:15` ·
`Implementacion/Imp/Lib/site-packages/sklearn/neural_network/_multilayer_perceptron.py:638-640,
851-857, 1682, 1774, 1776` · `resumen-de-decisiones.md:345-349` · `EL_FUTURO.md:93-95, 96-97,
98-103`.

## Cambios en Bibliografía.md

**Ninguno.** Por decisión del *leader*: hay una auditoría de `Bibliografía.md` abierta
(`features.md:22-27`) y añadir entradas ahora la contaminaría. Las fuentes de este informe quedan
completas y clasificadas en la tabla `## Fuentes`; el trasvase se hará al cerrar esa auditoría. Las
candidatas a entrada nueva, si Francisco decide citarlas en la memoria, son las nº 1, 4, 5, 6 y 7.

## Implicaciones para el proyecto

> [!warning] Propongo, no decido
> Nada de esta sección crea tarea, toca código ni reabre el track de código —cerrado el
> 2026-07-16. Es material para que Francisco escriba 6.2 y decida.

### A. Qué NO se contradice de `resumen-de-decisiones.md`

Ninguna decisión cerrada queda desmentida por esta investigación. Al contrario: dos de ellas son
justamente lo que un salto a NL rompería, y conviene tenerlo a la vista.

- **Decisión 2** («comparar 4 algoritmos… Autoencoder vía `MLPRegressor`, sin TF/Keras») y
  **decisión 6** («umbral p95 sobre el 20 % de D1 reservado, **igual para los 4**») sostienen el
  protocolo de comparación homogéneo de `anomalias.py:5-7`. Ese «igual para los 4» es lo primero
  que se cae si uno de los cuatro pasa a entrenarse con otra librería y otro criterio de parada.
- **H-2** (detector por defecto = Autoencoder, seleccionable por `--detector`) hace que el
  autoencoder sea el detector que va a 5.3. Tocarlo mueve los resultados publicados de 5.1 y 5.3, no
  solo los de un experimento aislado.

### B. Diseño en papel del único experimento defendible (E-INC)

De las cuatro vías de §3, la única que combina «aporta algo» + «no rompe nada estructural» es la
**3.3**. La dejo aterrizada; la 3.2 se comenta aparte porque no es un experimento nuevo sino un
análisis.

| | |
|---|---|
| **Nombre propuesto** | E-INC — autoencoder incremental por ráfagas |
| **Pregunta** | ¿Converge el autoencoder entrenado por ráfagas sucesivas a la misma AUC-ROC y al mismo umbral p95 que el entrenado de una sola vez, y con qué coste en tiempo? |
| **Qué NO pregunta** | Nada sobre deriva ni sobre olvido catastrófico (§2.5a). Debe decirse en el enunciado del experimento, no en una nota al pie |
| **Etapa** | Etapa 1 (anomalías), y **solo** el algoritmo `Autoencoder` |
| **Fichero** | `Implementacion/app/anomalias.py`. Los otros tres detectores no se tocan |
| **Dato de entrada** | `X_D1_train` (`anomalias.py:139`), troceado en ráfagas |
| **Qué se conserva intacto** | `D1_val` sigue fijando el umbral p95 (`anomalias.py:89`, `259-261`); D2 sigue intocable; el *score* unificado sigue siendo el MSE de reconstrucción (`anomalias.py:216-218`); la semilla sigue siendo 42 (`config.py:16`) |
| **Por qué no hay *leakage*** | El troceo ocurre **dentro** de `D1_train`, que ya está separado de `D1_val` desde `anomalias.py:139`. Ni el troceo ni el criterio de parada ven D2 |
| **Comparador** | El autoencoder actual, ya entrenado y persistido. La comparación es contra una fila que ya existe en `metricas_anomalias.csv` |

**Prerrequisitos, en orden y todos bloqueantes:**

1. **Sustituir el criterio de parada.** `early_stopping=True` (`anomalias.py:181`) es incompatible
   con el entrenamiento incremental (`_multilayer_perceptron.py:638-640`). Hace falta un criterio
   nuevo que **no** mire D2. La opción conservadora es un número fijo de pasadas por ráfaga, fijado
   *a priori*; cualquier criterio adaptativo hay que justificarlo contra la decisión 6.
2. **Decidir el número y el tamaño de ráfaga *antes* de mirar resultados**, y dejarlo escrito. Si se
   ajusta el troceo hasta que el resultado sea bonito, el experimento no vale nada.
3. **Reejecutar la selección de hiperparámetros o congelarla.** `_seleccionar_config`
   (`anomalias.py:224-242`) elige la configuración por AUC-ROC sobre D1_val + muestra de D3. Con
   entrenamiento incremental esa selección cambia de significado; lo limpio es **congelar la
   configuración ganadora actual** y comparar batch contra incremental con la misma arquitectura.
4. **Idempotencia del CSV.** Cualquier variante nueva tiene que encajar en el mecanismo
   `_limpiar_variante_csv` (`anomalias.py:296-318`) o se acumulan filas duplicadas.

**Coste estimado:** bajo en dependencias (**cero** nuevas: `partial_fit` está en el sklearn ya
fijado, `scikit-learn==1.7.1`, `requirements.txt:15`), medio en tiempo de diseño (los cuatro
prerrequisitos son decisiones de protocolo, no líneas de código) y bajo en cómputo (solo el
autoencoder, solo D1). **Veredicto de viabilidad: viable, pero de valor limitado para la tesis del
TFG.** Responde a una pregunta de despliegue, no a la pregunta de investigación del trabajo. Si hay
que elegir una sola línea futura, no es esta.

### C. Lo que se rompería al salir de scikit-learn a PyTorch (por si se plantea)

Confirmado punto por punto. Es la razón por la que esto es línea futura y no experimento:

1. **El protocolo de comparación homogéneo entre los cuatro detectores** (`anomalias.py:5-7`:
   «mismo split, misma semilla 42, mismo umbral percentil 95, mismas métricas»). Con un autoencoder
   en otra librería, «bajo protocolo idéntico» deja de ser cierto y la tabla de 5.1 pierde su
   garantía.
2. **La persistencia.** `hibrido.py` carga los `.joblib` de ambas etapas sin reentrenar
   (`hibrido.py:6-9`, `154-155`). Un modelo PyTorch no entra por ahí sin una capa de carga
   distinta, y eso rompe la propiedad que hace auditable el híbrido: que 5.3 usa exactamente los
   mismos modelos que 5.1 y 5.2.
3. **El `requirements.txt` fijado** (21 dependencias, `requirements.txt:1-21`). Añadir PyTorch
   multiplica el tamaño del entorno y rompe la reproducibilidad ya verificada.
4. **La prohibición explícita** de `anomalias.py:12` («PROHIBIDO TF/Keras») —escrita contra Keras,
   pero cuyo espíritu es el mismo: una sola librería de modelado.
5. **Reabre el track de código**, cerrado el 2026-07-16, y con él la obligación de pasar por
   `auditor-ml` y de reejecutar 5.1 y 5.3 en las dos variantes de características.

### D. La conclusión más valiosa, y dónde encaja en `EL_FUTURO.md`

**Confirmada: el cuello de botella no es la librería, es el dataset.** Y de ahí sale la
recomendación de redacción más importante de este informe: **no escribir «aprendizaje continuo»
como línea futura independiente**. No lo es. Es una línea **dependiente**, y su prerrequisito ya
está escrito en `EL_FUTURO.md:93-95` («Generalización cruzada de dataset: entrenar en NSL-KDD y
evaluar en otro (CIC-IDS2017 / UNSW-NB15)»).

Propuesta de fusión para 6.2, en un solo bloque con tres peldaños encadenados —cada uno
prerrequisito del siguiente:

| Peldaño | Qué es | Estado en `EL_FUTURO.md` | Qué desbloquea |
|---|---|---|---|
| **1. Migrar a un dataset con reloj** | CIC-IDS2017 (marca de tiempo por flujo verificada) o UNSW-NB15 (pcap crudo) | `EL_FUTURO.md:93-95`, ya escrito, «coste alto (re-mapeo de features)» | Todo lo demás |
| **2. Análisis de deriva temporal** | Split cronológico, curva de degradación, protocolo TESSERACT | `EL_FUTURO.md:96-97` lo apunta ya, pero **como deriva D1→D2**, que es desplazamiento entre particiones, no deriva temporal | Justifica por primera vez hablar de adaptación |
| **3. Representación de secuencia** | Sesión o *host* como secuencia de flujos, en lugar de flujos aislados | `EL_FUTURO.md:98-103`, respaldado con datos (`snmpgetattack` lo fallan los 4 detectores por límite de las características por flujo) | Es lo único que haría de Nested Learning una opción literal, y no una metáfora |

Dos matices de redacción que conviene no perder:

- La deriva de `EL_FUTURO.md:96-97` **ya es medible hoy** y sin reloj: el FPR real de 8-10 % frente
  al 5 % que promete el p95 (`resumen-de-decisiones.md:345-349`) es el dato. Pero hay que nombrarlo
  con precisión —**desplazamiento entre D1 y los normales de D2**, no deriva temporal— o la
  afirmación se cae en cuanto alguien pregunte por la marca de tiempo. Esta es, con diferencia, la
  línea de mejor relación coste/valor de todo el informe: dato ya en disco, análisis acotado,
  afirmación defendible.
- El peldaño 3 conecta con algo que el TFG ya demostró con datos propios: que hay familias de
  ataque intrínsecamente indetectables con características por flujo. Eso convierte «modelar
  secuencias» en una conclusión **derivada de los propios resultados**, no en una idea importada de
  un artículo de Google.

### E. Veredicto final sobre Nested Learning en 6.2

**No aplicable, y con cuatro razones citables en lugar de una.** Si Francisco quiere mencionar NL en
las líneas futuras, la formulación que este informe respalda es: *el paradigma de Nested Learning
(Behrouz et al., NeurIPS 2025) sitúa su aportación en el aprendizaje sobre secuencias de contextos
con muestras no i.i.d., y su validación experimental se limita a modelos de lenguaje; no consta a
fecha de este trabajo ninguna aplicación a datos tabulares ni a detección de intrusiones. Su
adopción en un H-NIDS exigiría, antes que cualquier decisión de librería, un dataset con marca de
tiempo y una representación de secuencia —dos cambios que este trabajo identifica como líneas
futuras por derecho propio.*

Lo que **no** debería escribirse en 6.2: «aplicar Nested Learning al modelo de anomalías», ni
llamar «Nested Learning» a un bucle de `partial_fit` (§2.6), ni presentar un troceo de D1 o D3 como
análisis de deriva (§2.5).

## Decisiones tomadas a partir de este informe

> [!note] Añadido el 2026-08-18 (ficha **T17, punto 1**)
> Bloque de cierre retrospectivo. Recoge **solo** lo que está respaldado en
> `resumen-de-decisiones.md` o en `features.md`; nada se infiere del propio informe.

Este informe entró, junto con otros tres, en el `grill-me` de 13 preguntas del **2026-08-06**, que
los convirtió en las fichas **T0-T17** de `features.md` y cuyas conclusiones se registraron el
**2026-08-09** en `resumen-de-decisiones.md` (§ Decisiones del 2026-08-06).

### A. Lo que se convirtió en decisión

| Decisión | Qué dice | Dónde está registrada |
|---|---|---|
| **Criterio rector del lote** — «refinar el proyecto o enseñar el límite; nunca sucedáneos» | Las imposibilidades **se declaran con su razón técnica**; no se omiten ni se sustituyen por sucedáneos sintéticos. Es exactamente lo que propone §3.1 de este informe y lo que descarta §2.5 | `resumen-de-decisiones.md`, § Decisiones del 2026-08-06 |
| **Decisión marco (b)** — retirada de la regla «lo escribe Francisco», en dos velocidades | `2.x` sin restricción para el `redactor-tfg`; **`6.2 Líneas futuras` pasa a borrador de agente con revisión final de Francisco**, por ser «el sitio natural del material de *Nested Learning*»; la bibliografía Zotero/IEEE sigue siendo de Francisco | `resumen-de-decisiones.md`, § Decisiones del 2026-08-06 y bitácora `2026-08-06` |
| **El material de aprendizaje continuo se redacta en `6.2`** | Ejecutado en **T12** (Tanda 7, 2026-08-15): `6.2 Líneas futuras` pasa de *placeholder* a documento entero, redactado desde `EL_FUTURO.md`. **La revisión de Francisco sigue pendiente** | `features.md`, nota de cierre de T12 |

### B. Lo que se descartó

| Descartado | Razón registrada |
|---|---|
| **E-INC** — autoencoder incremental por ráfagas (§3.3 y § B de este informe) | «Viable, pero responde a una pregunta de despliegue, no a la del TFG. Complejidad innecesaria». Coincide con el propio veredicto de viabilidad de § B | `features.md`, tabla «Descartado — no reabrir» |
| **Aprendizaje semisupervisado** | «La premisa no existe: no hay datos sin etiquetar. Cada fila de NSL-KDD trae `attack` y `level`» | `features.md`, misma tabla |
| **Salir de scikit-learn a PyTorch** (§ C) | Los descartes de arquitecturas PyTorch del lote se cierran por «ruptura de la persistencia `.joblib` y del protocolo homogéneo» — el mismo motivo que enumera § C. El descarte está fichado sobre los clasificadores tabulares, no sobre el autoencoder | `features.md`, misma tabla (fila TabNet / FT-Transformer / SAINT / NODE / TabM / TabPFN) |

> [!todo] Sin respaldo documental localizado — no se afirma
> No he encontrado en `resumen-de-decisiones.md` ni en `features.md` una decisión explícita sobre
> dos propuestas de este informe, así que **no las registro como decididas**:
> 1. La **fusión de «aprendizaje continuo» con la línea de generalización cruzada** en un único
>    bloque de tres peldaños (§ D). Falta comprobar contra el texto vigente de
>    `6.2 Líneas futuras` si T12 la adoptó, y anotarlo aquí.
> 2. El **análisis del desplazamiento D1→D2** como línea de mejor coste/valor (§3.2). El dato del
>    FPR está en `resumen-de-decisiones.md`, pero no consta decisión de convertirlo en análisis.
> 3. **Dónde se define «aprendizaje continuo»: `2.x` o `6.2`.** Es un **punto de contacto
>    declarado** entre los apuntes de Francisco (la figura de `1.4` menciona el término sin
>    definirlo) y T12, **sin decisión registrada**: la ficha correspondiente sigue **abierta** en
>    `features.md` (ficha de `mis-apuntes-del-informe.md`, punto 2), donde solo consta que
>    Francisco *propone* definirlo y que queda por **decidir** qué se define en `2.x` y qué se
>    queda en `6.2`, evitando duplicarlo.

**Sin efecto sobre `Bibliografía.md`:** la sección `## Cambios en Bibliografía.md` sigue vigente —
este bloque **no da de alta ninguna entrada ni asigna ningún número**.
