---
titulo: "¿Cómo resuelven otros autores los H-NIDS que combinan anomalías y firmas, y dónde encaja la cascada de este TFG?"
numero: "-"
estado: informe
docx_ref: "-"
---

# ¿Cómo resuelven otros autores los H-NIDS que combinan anomalías y firmas, y dónde encaja la cascada de este TFG?

- **Encargo:** contrastar la arquitectura de este TFG con la literatura publicada de H-NIDS.
  Cinco frentes: (1) taxonomía real de arquitecturas híbridas; (2) el **orden** de las etapas y
  su justificación; (3) cómo trata cada trabajo lo **desconocido**; (4) qué reportan y qué callan,
  en particular cuántos miden algo parecido al **recall 0-day**; (5) dónde coincide y dónde diverge
  la cascada de este proyecto respecto de cada patrón.
- **Fecha:** 2026-08-02
- **Alcance:**
  - **Entra:** arquitecturas de combinación anomalía + firmas (serie en ambos órdenes, paralelo con
    fusión, meta-clasificador, jerárquico, y los patrones que no encajan en esos); el mecanismo de
    clase `unknown` y su tratamiento formal (*open-set recognition*); la práctica de evaluación
    sobre ataques ausentes del entrenamiento.
  - **Queda fuera** (por encargo, van en informes hermanos): alternativas de modelado tabular
    (TabNet, GBDT, autosupervisión, codificación de categóricas) →
    `clasificadores-tabulares-y-arquitecturas-hibridas.md`; tabla de cifras del TFG frente a lo
    publicado sobre NSL-KDD y protocolo de *benchmark* → `benchmark-comparativo-nsl-kdd.md`. Aquí
    las métricas solo aparecen para **caracterizar un diseño**, nunca para comparar rendimiento.
- **Alimenta a:** [[2.2.4 Detección por firmas frente a detección por anomalías]],
  [[2.2.3 Taxonomía de los IDS]] y, sobre todo, [[3.2 Arquitectura del sistema]] (y por extensión
  [[03 Diseño del sistema/3.4 Modelo de detección de anomalías|3.4]] y [[3.5 Modelo de detección basado en firmas]]).

> [!warning] Esto NO es material de líneas futuras
> A diferencia de los otros informes de este lote, este es **respaldo bibliográfico de una
> arquitectura que ya está construida, ejecutada y evaluada** (track de código cerrado el
> 2026-07-16). Sirve para justificar en los capítulos 2 y 3 por qué la cascada anomalía→firmas es
> una decisión defendible y con linaje, y para declarar honestamente en qué se aparta del patrón
> publicado. **No es un catálogo de mejoras pendientes.** Lo poco que sí es propuesta va marcado
> como tal en `## Implicaciones para el proyecto`.

> [!warning] Esto tampoco es memoria
> Es insumo citable. No entra en [[00 Índice TFG]] y su prosa no se copia a un capítulo sin que lo
> decida Francisco.

## Respuesta corta

La literatura tiene **cinco patrones** bien identificables, y la cascada **anomalía→firmas** de
este TFG no es una rareza: es el patrón más **antiguo y conceptualmente más explícito**, fundado en
ADAM (2001) y en Tombini *et al.* (2004), que ya definían exactamente las tres salidas de este
proyecto —conocido / falsa alarma / **desconocido**—. No es, en cambio, el patrón dominante hoy:
en los trabajos recientes el orden inverso (firmas→anomalías) gana terreno por un argumento de
coste y de tasa de falsos positivos, y hay una tercera familia (paralelo con fusión) que evita
elegir. Dos divergencias del TFG merecen declararse en la memoria y **no son cosméticas**: (i) en
ADAM y en Tombini la etapa 2 **puede devolver un sospechoso a "falsa alarma"**, y este proyecto se
lo prohíbe por diseño (H-5/P-5), de donde sale que su binaria coincida con la etapa 1 y que el FPR
se quede en el 8-10 % de la etapa 1; (ii) el `unknown` por umbral sobre `predict_proba` es el
mecanismo más débil de los publicados —Scheirer *et al.* (2013) demuestran que umbralizar un
clasificador de conjunto cerrado **no acota el riesgo de espacio abierto**—, lo que explica
teóricamente el 13,4 % de enrutado a `unknown` medido en `hibrido.py`. Por último: **casi nadie
mide lo que este TFG mide.** La evaluación en protocolo cerrado sigue siendo la norma, y el recall
por tipo sobre ataques ausentes del entrenamiento solo aparece de forma sistemática en la rama de
*open-set* posterior a 2017.

## Hallazgos

### 1. Sí hay taxonomía, pero no la traen los *surveys* más citados

El primer hallazgo es negativo y conviene decirlo en la memoria: **la revisión de IDS más citada de
los últimos años no taxonomiza las arquitecturas híbridas**. Khraisat *et al.* (2019), en
*Cybersecurity*, organiza todo el campo en SIDS (por firmas) y AIDS (por anomalías), dedica tablas
a métricas, datasets y técnicas de evasión —y despacha lo híbrido en **un solo párrafo** bajo el
epígrafe «*Hybrid based techniques*», con una única obra de ejemplo (Farid *et al.*, 2010; Naive
Bayes + árbol de decisión, 99,63 % sobre KDD'99). Ni tipos, ni orden, ni diagrama. Peor aún para
nuestro propósito: **ese ejemplo combina dos clasificadores supervisados**, no una etapa de
anomalías con una de firmas, de modo que ilustra la dilución terminológica más que la arquitectura.
([Khraisat *et al.*, 2019](https://doi.org/10.1186/s42400-019-0038-7), leído íntegro) — nivel 1

> [!note] Dilución del término «híbrido»
> Merece un párrafo en 2.2.3/2.2.4. En la literatura NSL-KDD, «IDS híbrido» designa con la misma
> frecuencia (a) anomalías + firmas —el sentido de este TFG—, (b) selección de características +
> clasificador, (c) *clustering* + clasificador y (d) dos clasificadores supervisados en *ensemble*.
> Cuando el TFG diga «híbrido» tiene que **acotar cuál de los cuatro sentidos usa**, o la
> comparación con lo publicado se vuelve ruido.

La taxonomía explícita más útil que he localizado no está en un *survey*, sino en la sección de
trabajo relacionado de Macko *et al.* (2023), que ordena la literatura en **cuatro tipos** y asigna
citas concretas a cada uno. Es un **preprint de arXiv sin publicación posterior localizada →
nivel 2**, así que lo uso como **andamio de organización**, no como autoridad: cada tipo va
respaldado abajo por su fuente primaria de nivel 1, verificada una a una.
([Macko *et al.*, 2023](https://arxiv.org/abs/2310.06656)) — nivel 2

Los propios autores añaden una observación que conviene citar tal cual porque es exactamente la
justificación de un trabajo como este: pese a que el uso de sistemas híbridos es «*bastante
intuitivo y se cree en general que mejora el rendimiento de un NIDS*», **faltan análisis rigurosos
que confirmen esa creencia**.

### 2. Los cinco patrones (cuatro de la taxonomía + uno que no encaja)

#### Patrón A — Serie con **anomalías primero** (anomalía → firmas)

La etapa de anomalías decide sospechoso/normal; la de firmas solo ve lo sospechoso y lo cualifica.
Es la arquitectura de este TFG.

- **ADAM** (Barbará *et al.*, 2001) es el ancestro directo y el hallazgo más valioso del informe.
  Su funcionamiento es literalmente el de `hibrido.py`: primero construye un repositorio de
  *itemsets* frecuentes «normales» minando datos **libres de ataque**; después, en línea, compara
  los *itemsets* de la ventana actual contra ese perfil y **descarta lo que se considera normal**;
  con el resto, «*ADAM usa un clasificador previamente entrenado para clasificar las conexiones
  sospechosas como un tipo conocido de ataque, un tipo desconocido o una falsa alarma*».
  ([Barbará *et al.*, 2001](https://doi.org/10.1145/604264.604268), texto completo) — nivel 1
- **Tombini *et al.* (2004)** formalizan la combinación en serie sobre tráfico HTTP y, sobre todo,
  la nombran: proponen «*un componente de anomalías drástico con un componente de firmas
  sensible*», y su aportación es que la serie **separa los eventos en tres clases** —*normal*,
  *intrusive* y *unqualified*— dando «mejor cualificación de los resultados de detección» con menos
  falsas alarmas y menos eventos sin cualificar.
  ([Tombini *et al.*, 2004](https://doi.org/10.1109/CSAC.2004.4), solo resumen) — nivel 1
- **Ji *et al.* (2016)**, sobre **NSL-KDD**, encadena tres etapas: extraer patrones del tráfico para
  derivar reglas que identifican anomalías → modelo predictivo que categoriza el **tipo** de ataque
  → visualización interactiva para validar. Es la misma secuencia lógica que la cascada del TFG,
  con reglas en lugar de un detector *one-class*.
  ([Ji *et al.*, 2016](https://doi.org/10.1016/j.jnca.2015.12.004), solo resumen) — nivel 1
- **Khan *et al.* (2019), TSDL** se cita habitualmente en esta familia, pero **no pertenece a ella
  en sentido estricto y conviene no confundirlo**: su etapa 1 es un clasificador **supervisado**
  binario normal/anómalo cuya *probability score* se inyecta como **una característica más** en la
  etapa 2 multiclase. No hay filtro: todo el tráfico atraviesa las dos etapas, y ninguna se entrena
  solo con tráfico normal.
  ([Khan *et al.*, 2019](https://doi.org/10.1109/ACCESS.2019.2899721), solo resumen) — nivel 1

#### Patrón B — Serie con **firmas primero** (firmas → anomalías)

El detector de firmas caza lo conocido y solo el residuo llega al detector de anomalías.

- **Zhang, Zulkernine y Haque (2008)**: Random Forest construye automáticamente los patrones de
  intrusión (misuse) y, en la parte de anomalías, un mecanismo de **detección de *outliers*** del
  propio RF busca lo novedoso; el sistema híbrido «mejora el rendimiento combinando las ventajas de
  ambas». ([Zhang *et al.*, 2008](https://doi.org/10.1109/TSMCC.2008.923876), solo resumen) — nivel 1
- **Elbasiony *et al.* (2013)**: RF para firmas, *k-means* ponderado para anomalías, con un método
  propio para elegir los clústeres anómalos **inyectando ataques conocidos** en los datos inciertos.
  ([Elbasiony *et al.*, 2013](https://doi.org/10.1016/j.asej.2013.01.003), solo resumen) — nivel 1
- **Kim, Lee y Kim (2014)** es, con diferencia, **el antagonista más directo de este TFG**: mismo
  dataset (**NSL-KDD**) y orden inverso. Su modelo de firmas (C4.5) **descompone el conjunto de
  entrenamiento normal en subconjuntos** y sobre cada uno construye un **one-class SVM**; la
  detección de anomalías queda así «informada» por el conocimiento de los ataques conocidos.
  Reportan mejor detección **tanto de ataques conocidos como desconocidos** y una reducción de
  tiempos al ~50 %/60 %.
  ([Kim *et al.*, 2014](https://doi.org/10.1016/j.eswa.2013.08.066), solo resumen) — nivel 1
- **Bangui, Ge y Buhnova (2022)**, en VANET: Random Forest + detección posterior basada en
  *coresets*. ([Bangui *et al.*, 2022](https://doi.org/10.1007/s00607-021-01001-0), solo resumen) — nivel 1
- **Macko *et al.* (2023)** adoptan este orden y lo justifican explícitamente (ver §3).

#### Patrón C — Paralelo con módulo de fusión

Los dos detectores ven **todo** el tráfico y un tercer componente concilia sus veredictos.

- **Depren *et al.* (2005)** es el ejemplar canónico: módulo de anomalías (SOM entrenado sobre
  comportamiento normal), módulo de firmas (árbol J.48) y un **sistema de soporte a la decisión
  basado en reglas** que interpreta las salidas de ambos. Sobre KDD Cup 99.
  ([Depren *et al.*, 2005](https://doi.org/10.1016/j.eswa.2005.05.002), solo resumen) — nivel 1

La diferencia estructural con la cascada es que aquí **el detector de anomalías nunca deja de ver
tráfico normal**, así que su tasa de falsos positivos entra íntegra en el sistema y el módulo de
fusión existe precisamente para amortiguarla.

#### Patrón D — Meta-clasificador sobre las salidas de ambos (*stacking*)

Variante «aprendida» del patrón C: en lugar de reglas escritas a mano, un modelo combina las
salidas.

- **Khraisat *et al.* (2020)** apilan (*stacking ensemble*) un árbol **C5.0** como SIDS y un
  **one-class SVM** como AIDS, con el objetivo declarado de identificar «tanto las intrusiones bien
  conocidas como los ataques *zero-day*», evaluado sobre **NSL-KDD** y ADFA.
  ([Khraisat *et al.*, 2020](https://doi.org/10.3390/electronics9010173), solo resumen) — nivel 1

Es el trabajo publicado **más cercano al TFG en piezas** (firmas supervisadas + detector *one-class*
+ NSL-KDD + objetivo 0-day) y el **más lejano en topología**: donde este proyecto pone una puerta
dura, ellos ponen un combinador entrenado. Corresponde a la línea «fusión por meta-clasificador»
que `EL_FUTURO.md:66-68` ya tenía apuntada; **la literatura la respalda, no la inventa este
informe**.

#### Patrón E — Jerárquico / multinivel

Más de dos etapas, con detectores que se coordinan entre niveles.

- **Guo *et al.* (2016)**: **dos** componentes de anomalías y **uno** de firmas en jerarquía de dos
  niveles. La etapa 1 es un detector de anomalías de baja complejidad computacional; su salida
  **participa en la construcción** de los dos detectores del nivel 2 (basados en k-NN), que existen
  para «reducir los falsos positivos y los falsos negativos generados por el componente de la
  etapa 1». Evaluado sobre KDD'99 y el *benchmark* de la Universidad de Kioto.
  ([Guo *et al.*, 2016](https://doi.org/10.1016/j.neucom.2016.06.021), solo resumen) — nivel 1

#### Patrón F — El que no encaja: **realimentación con generación automática de firmas**

No es serie, ni paralelo, ni jerarquía: es un **bucle**.

- **Hwang, Cai, Chen y Qin (2007)**, en IEEE TDSC: el detector de anomalías mina episodios de
  tráfico anómalo, y un **esquema de generación de firmas ponderadas** extrae firmas de esas
  anomalías y **las inserta en la base de datos de SNORT**. El sistema aprende firmas nuevas de lo
  que la etapa de anomalías descubre. Reportan 60 % de detección frente al 30 % de SNORT y el 22 %
  de Bro con <3 % de falsas alarmas, y que las firmas generadas por el módulo de anomalías
  **mejoran a SNORT en un 33 %**.
  ([Hwang *et al.*, 2007](https://doi.org/10.1109/TDSC.2007.9), solo resumen) — nivel 1

Es la respuesta que la literatura da a una pregunta que el TFG deja abierta: **qué hacer con un
`unknown` una vez detectado**. Aquí el `unknown` no es un final de línea, sino la entrada de un
proceso que fabrica la firma que faltaba.

- Una variante moderna del mismo espíritu: **Uddin *et al.* (2024)** proponen un IDS de **dos
  niveles dirigido por clasificación one-class** —nivel 1 separa normal de ataque, nivel 2 decide
  si el ataque es conocido o desconocido— y **reentrenan agrupando los ataques no vistos**.
  ([Uddin *et al.*, 2024](https://arxiv.org/abs/2403.13010), solo resumen) — **nivel 2, preprint**

### 3. El orden: quién pone qué primero, y con qué argumento

El encargo pregunta si anomalía→firmas es dominante o minoritario. La respuesta honesta tiene tres
partes.

**(a) Ninguna fuente que haya localizado cuenta cuántos trabajos usan cada orden.** No hay
porcentajes citables. Lo que sí es citable es que ambos órdenes son familias establecidas con
literatura de nivel 1 propia (§2), y que la única taxonomía explícita que he encontrado los lista
como tipos 1 y 2 con un número similar de referencias (cinco y cuatro respectivamente, en Macko
*et al.*, 2023).

**(b) Los argumentos son distintos y no son intercambiables.** Esto sí es material de 3.2.2:

| Orden | Argumento de sus autores | Qué gana | Qué paga |
|---|---|---|---|
| **Anomalías → firmas** | La etapa 1 es «drástica» y la 2 «sensible»: la de firmas **cualifica** lo que la de anomalías señala, separando *normal* / *intrusive* / *unqualified* (Tombini *et al.*, 2004); en ADAM, además, **filtra las falsas alarmas** para no molestar al analista (Barbará *et al.*, 2001) | Cobertura de lo desconocido y una etiqueta accionable para el operador | La etapa 1 ve **todo** el tráfico: su FPR es el FPR del sistema, salvo que la etapa 2 pueda vetarla |
| **Firmas → anomalías** | «Los ataques conocidos se detectan de forma relativamente fiable; al mismo tiempo, el detector de anomalías puede ser **menos sensible** a las desviaciones, reduciendo la tasa de falsos positivos» (Macko *et al.*, 2023) | FPR más bajo y menos carga sobre el componente caro | Lo desconocido llega **filtrado y sesgado**: solo se examina el residuo que las firmas no reclamaron |

**(c) Hay un argumento a favor del orden de este TFG que la literatura sostiene y que 3.2.2 aún no
usa.** Sommer y Paxson (2010) formulan el problema del **«semantic gap»**: el fallo operativo
característico de la detección por anomalías no es no detectar, sino no producir un informe
**accionable**; «*el objetivo de desplegar un sistema de detección de intrusiones **es** encontrar
ataques, y un detector que no permite salvar esa brecha difícilmente cumplirá las expectativas
operativas*». Poner las firmas **detrás** del detector de anomalías es, en esos términos, una
respuesta directa al *semantic gap*: la etapa 2 no está ahí para detectar, sino para **traducir**
«esto es anómalo» en «esto es un `dos`» o «esto es algo que no reconozco».
([Sommer y Paxson, 2010](https://doi.org/10.1109/SP.2010.25), texto completo) — nivel 1

El mismo trabajo respalda, casi palabra por palabra, la elección de entrenar la etapa 1 **solo con
D1**: «*para la detección de anomalías que aspira a encontrar ataques novedosos, por definición uno
no puede entrenar con los ataques de interés, sino solo con tráfico normal, y por tanto se dispone
de una única categoría contra la que comparar*». Y advierte del precio, que este TFG paga y mide:
eso «*exige tener un modelo **perfecto** de normalidad para cualquier decisión fiable*», mientras
que un problema de clasificación con varias alternativas «*bastaría con un modelo lo bastante
nítido para separar las clases*». Es la explicación teórica del FPR del 8-10 % de la etapa 1 y de
la caída `conocida f1_macro` 0,822 → 0,748 al entrar en la cascada, ya registradas en
`resumen-de-decisiones.md`.

### 4. Cómo tratan lo desconocido: tres niveles de formalización

Los trabajos revisados se reparten en tres escalones muy desiguales.

**Escalón 1 — No lo abordan.** Es la mayoría. Depren (2005), Ji (2016), Khan (2019) o Guo (2016)
reportan exactitud, tasa de detección y FPR sobre las clases del dataset. Lo «desconocido» aparece
en la motivación —«los IDS por firmas no detectan *zero-day*»— y desaparece en la evaluación. Es
también la posición del *survey* de referencia: Khraisat *et al.* (2019) sostienen que AIDS «puede
detectar ataques *zero-day*» **como propiedad cualitativa de la técnica**, no como magnitud medida.

**Escalón 2 — Clase `unknown` por defecto / por baja confianza.** Es exactamente el mecanismo de
este TFG, y tiene 25 años. ADAM lo argumenta mejor que ningún trabajo posterior que haya leído:

> «*Nótese que ningún conjunto de entrenamiento puede preparar a un clasificador para un ataque
> desconocido (puesto que no puede haber ejemplos de tal evento). […] Podemos incluir esa provisión
> usando un artificio presente en algunos clasificadores: la inclusión de una etiqueta "por
> defecto" mediante la cual el clasificador expresa su **incapacidad de reconocer** la clase del
> evento como una de las conocidas. Adoptamos el enfoque de que cualquier evento marcado por el
> software de reglas de asociación que el clasificador no pueda clasificar como ataque conocido ni
> como evento normal (falsa alarma) debe considerarse, **conservadoramente**, un ataque
> desconocido.*» (Barbará *et al.*, 2001)

La «clase *unqualified*» de Tombini *et al.* (2004) es la misma idea con otro nombre. El fundamento
estadístico de todo el escalón es todavía anterior: **Chow (1970)** derivó la regla de rechazo
óptima y la relación entre probabilidad de error y probabilidad de rechazo. La letra pequeña de
Chow es la que importa aquí: la regla es óptima **sobre las probabilidades a posteriori
verdaderas**, y `predict_proba` de un RandomForest no lo es.
([Chow, 1970](https://doi.org/10.1109/TIT.1970.1054406)) — nivel 1

**Escalón 3 — *Open-set recognition* formal.** Es la única rama que ataca de frente el problema que
este TFG midió (el 86 % de 0-day cazados que reciben etiqueta conocida con confianza alta), y su
diagnóstico es que **el escalón 2 es estructuralmente insuficiente**:

- **Scheirer *et al.* (2013)** formalizan el reconocimiento de conjunto abierto como un problema de
  optimización con restricciones e introducen la noción de **riesgo de espacio abierto** (*open
  space risk*). El punto: un clasificador de conjunto cerrado no acota ese riesgo, por bien que se
  elija el umbral. ([Scheirer *et al.*, 2013](https://doi.org/10.1109/TPAMI.2012.256)) — nivel 1
- **Bendale y Boult (2016)** introducen **OpenMax**, una capa que estima la probabilidad de que la
  entrada pertenezca a una clase desconocida, y demuestran que **supera al umbralizado de SoftMax**
  aportando riesgo de espacio abierto acotado. Que su comparador explícito sea «umbralizar la
  salida probabilística» es lo que hace que esta cita apunte directamente al `UMBRAL_CONF` de
  `hibrido.py`. ([Bendale y Boult, 2016](https://doi.org/10.1109/CVPR.2016.173)) — nivel 1
- **Cruz *et al.* (2017)** llevan el marco al dominio: sobre KDDCUP'99 y con granularidad **por
  tipo de ataque** (`sendmail`, `snmp guess`…) comparan SVM con núcleo RBF frente a **W-SVM**, con
  garantía teórica de acotar el riesgo de espacio abierto. La ventaja del W-SVM **crece a medida
  que sube el coste de equivocarse con una instancia desconocida** —el escenario del TFG—.
  ([Cruz *et al.*, 2017](https://doi.org/10.1109/THS.2017.7943467); contenido leído en
  [arXiv:1703.02244](https://arxiv.org/abs/1703.02244)) — nivel 1 (registro) / nivel 2 (texto leído)
- **Fang y Xie (2025)** son el estado reciente: InfoGAN + **OpenMax** con teoría de valores extremos
  (Weibull) para estimar la activación de la clase desconocida, sustituyendo SoftMax en la salida.
  Interesa además su variante **O-S**, que es una **cascada de dos decisiones**: OpenMax detecta lo
  desconocido y luego SoftMax refina las clases conocidas para reducir falsas alarmas. Reportan
  >70 % de *recall* sobre tráfico desconocido con OpenMax.
  ([Fang y Xie, 2025](https://doi.org/10.1038/s41598-025-01084-1), texto completo vía PMC) — nivel 1

> [!note] Lo que este escalón le dice al TFG
> No es «hay un método mejor» (eso ya estaba en `EL_FUTURO.md:60-65`). Es que **existe una
> explicación teórica publicada del número concreto que el proyecto midió**: el 13,4 % de enrutado
> a `unknown` no es un defecto de calibración de `UMBRAL_CONF`, es el comportamiento esperado de
> umbralizar un clasificador de conjunto cerrado. Eso convierte un resultado incómodo de 5.3 en un
> resultado **explicado y citable**.

### 5. Qué reportan y qué callan

**El diagnóstico general es de nivel 1 y es duro.** Cruz *et al.* (2017) abren su artículo
constatando que «*la mayoría de las evaluaciones de sistemas de detección de intrusiones se han
realizado en un protocolo de conjunto cerrado, en el que solo se consideran las clases vistas
durante el entrenamiento*». Ahmad *et al.* (2023), en una revisión sistemática dedicada
exclusivamente a la detección de *zero-day*, concluyen que las soluciones recientes «*se apoyan en
repositorios de firmas, datasets obsoletos o no consideran los ataques zero-day*», y que detectar
un ataque completamente nuevo **sigue siendo un problema abierto**.
([Ahmad *et al.*, 2023](https://doi.org/10.1007/s10462-023-10437-z), solo resumen) — nivel 1

**Mi propio recuento, con su reserva.** Sobre los **catorce** trabajos de arquitectura que he
verificado uno a uno en este informe (§2 y §4), y **sin que esto sea una revisión sistemática ni
una muestra aleatoria** —los elegí siguiendo la taxonomía de Macko *et al.* y las referencias de
*open-set*, lo que sesga la muestra **a favor** de quien mide lo desconocido—:

| Qué hacen con los ataques ausentes del entrenamiento | Trabajos |
|---|---|
| **Lo miden explícitamente** con un protocolo diseñado para ello | Cruz 2017 (protocolo *open-set*), Macko 2023 (*novelty test*: omitir una clase del entrenamiento), Fang y Xie 2025 (*recall* de la clase desconocida), Uddin 2024 (preprint) |
| **Tienen mecanismo** para lo desconocido, pero la evaluación no aísla una métrica sobre ataques no vistos | ADAM 2001, Tombini 2004, Khraisat 2020 |
| **Lo enuncian como capacidad** y reportan métricas agregadas sobre el dataset completo | Depren 2005, Hwang 2007, Zhang 2008, Elbasiony 2013, Guo 2016, Ji 2016, Khan 2019, Bangui 2022 |

Kim *et al.* (2014) es el caso ambiguo y lo dejo señalado: su resumen afirma mejor detección «tanto
de ataques conocidos como desconocidos» sobre NSL-KDD, pero **no he podido leer el texto completo**
para determinar si eso es una métrica sobre los tipos ausentes del train o una lectura genérica de
la tasa de detección (ver `## Lo que no he podido confirmar`).

Aun con el sesgo a favor, **más de la mitad de la muestra no aísla ninguna métrica sobre ataques no
vistos**. La conclusión defendible en la memoria es cualitativa, no porcentual: *medir el recall por
tipo sobre los ataques ausentes del entrenamiento es minoritario en la literatura de H-NIDS, y donde
aparece de forma sistemática es en la rama de open-set recognition posterior a 2017*.

**Dos observaciones metodológicas de nivel 1 para acompañarla:**

- Arp *et al.* (2022) revisaron **treinta artículos** de conferencias de seguridad de primer nivel
  de la última década y encontraron que los sesgos de diseño, implementación y evaluación que
  inflan resultados están **generalizados**. Es la cita adecuada para justificar por qué este TFG
  reporta el FPR junto al recall 0-day (decisión P-2) en lugar de vender el recall aislado.
  ([Arp *et al.*, 2022](https://arxiv.org/abs/2010.09470), resumen y metadatos) — nivel 1
- Khraisat *et al.* (2019) añaden el reparo sobre el propio banco de pruebas: como los datasets
  KDD/DARPA «*ya no representan los ataques zero-day contemporáneos*», evaluar sobre ellos «*no
  ofrece una evaluación real y podría dar lugar a afirmaciones inexactas*». Es un límite que la
  memoria debe reconocer al presentar el recall 0-day: los 0-day de NSL-KDD son **ataques ausentes
  del entrenamiento**, no amenazas actuales.

### 6. Dónde coincide y dónde diverge este TFG, patrón por patrón

Este es el contraste que pedía el encargo. Vocabulario del proyecto.

| Eje | Lo que hace la literatura | Lo que hace este TFG | Veredicto |
|---|---|---|---|
| **Topología** | Cinco patrones (A-F, §2). El A (anomalía→firmas) tiene linaje desde 2001 | Patrón A puro: cascada con puerta dura | **Coincide.** No es exótico: es el patrón fundacional |
| **Naturaleza de la etapa 1** | Muy variable: *one-class* real (Khraisat 2020, OC-SVM), reglas (ADAM, Ji), SOM (Depren), o **binario supervisado** disfrazado de anomalía (Khan 2019) | Detector semisupervisado (*one-class*) entrenado **solo con D1**, 4 algoritmos bajo protocolo idéntico | **Coincide con la rama estricta y se separa de la laxa.** El «entrenado solo con normal» de Sommer y Paxson describe la etapa 1 del TFG, no la de Khan 2019 |
| **Naturaleza de la etapa 2** | Suele ser un clasificador que incluye la clase «normal» o «falsa alarma» | Clasificador de 4 clases de ataque entrenado **solo con D3**, sin clase `normal` | **Diverge.** Ver la fila siguiente: es la divergencia con más consecuencias |
| **¿Puede la etapa 2 vetar a la etapa 1?** | **Sí** en el patrón A canónico: ADAM etiqueta explícitamente «falsa alarma» y **la filtra** antes del analista; Tombini describe el papel del componente de firmas como reducir falsas alarmas | **No, por diseño** (H-5, P-5): la etapa 2 no tiene clase `normal`, así que nunca devuelve un sospechoso a normal | **Diverge.** Consecuencia directa: la binaria del híbrido **es** la de la etapa 1 y el FPR se queda en 0,102 (54). En ADAM y Tombini, la etapa 2 **sí** baja el FPR del sistema |
| **Orden** | Ambos órdenes tienen literatura de nivel 1. El inverso (firmas→anomalías) es el que más ha crecido, y su motivo declarado es **bajar el FPR** | Anomalía→firmas, justificado en 3.2.2 porque la etapa 2 no conoce «normal» | **Coincide, con un argumento propio distinto del de la literatura.** El argumento de 3.2.2 es de **consistencia interna del diseño**; el de la literatura es de **cobertura y accionabilidad** (Tombini, Sommer y Paxson). Ambos valen y conviene sumarlos |
| **Antagonista directo** | Kim *et al.* (2014): mismo dataset (NSL-KDD), orden inverso, misuse C4.5 → múltiples OC-SVM sobre subconjuntos del normal | Cascada inversa | **Diverge frontalmente.** Es la comparación que un tribunal puede pedir: *«¿por qué no al revés, como Kim?»*. La respuesta del TFG está en 3.2.2 y se puede reforzar con Sommer y Paxson |
| **Mecanismo de `unknown`** | Escalón 2 (etiqueta por defecto: ADAM, Tombini) o escalón 3 (*open-set* con EVT: OpenMax, W-SVM) | Escalón 2: umbral `UMBRAL_CONF` sobre `predict_proba` | **Coincide con el escalón clásico; queda por debajo del estado del arte**, y hay teoría publicada que predice exactamente ese déficit (Scheirer 2013, Bendale y Boult 2016) |
| **Calibración del umbral** | Rara vez se explicita. Chow (1970) da la teoría; los trabajos de *open-set* calibran con EVT sobre las activaciones | `UMBRAL_CONF` calibrado **out-of-fold sobre D3**, con regla de presupuesto τ=2 pp y D2 solo para reportar (Q4, H-4, P-4) | **Aventaja a casi toda la muestra.** No he encontrado en la muestra ningún H-IDS que describa con este detalle su protocolo anti-*leakage* para el umbral de rechazo. Es un punto fuerte del TFG, no una carencia |
| **Protocolo 0-day** | Cuando se mide, se **fabrica**: omitir una clase del entrenamiento (Macko 2023) o construir splits *open-set* (Cruz 2017) | Se usan los **17 tipos nativos** de KDDTest+ ausentes del train, con recall **por tipo** | **Aventaja al protocolo artificial.** El split no lo elige el experimentador: viene con el dataset. Es más difícil de acusar de diseño a medida |
| **Baseline de contraste** | Los híbridos suelen compararse contra **sus propias etapas** aisladas | Además de eso, un **RF monolítico de 5 clases** (`baseline.py`), el patrón dominante de la literatura NSL-KDD | **Aventaja.** Arp *et al.* (2022) señalan el *baseline* inapropiado como uno de los sesgos generalizados; tener el baseline que el tribunal espera es defensa directa |
| **Qué hacer con un `unknown`** | Hwang *et al.* (2007) cierran el bucle: generan la firma y la insertan en SNORT | Termina en la etiqueta `unknown` | **Diverge.** El TFG no cierra el bucle, y es correcto que no lo haga (fuera de alcance), pero conviene **nombrarlo** en 3.6/6.1 como límite consciente |

## Lo que no he podido confirmar

- **Qué orden es dominante, en cifras.** No he encontrado **ninguna** fuente que cuente cuántos
  H-NIDS publicados usan anomalía→firmas frente a firmas→anomalías. La única revisión sistemática
  con recuentos que localicé (Seiba *et al.*, SPCSJ) cuenta prácticas de preprocesado —61 % sin
  selección de características, 35 % que tratan el desbalanceo— **no arquitecturas**, y además es
  **nivel 3** por el perfil de la publicación. Lo afirmable es que **ambos órdenes son familias
  establecidas**; cualquier «es el patrón dominante» sin fuente sería invención.
- **Cómo mide exactamente Kim *et al.* (2014) la detección de ataques desconocidos.** Su resumen la
  afirma sobre NSL-KDD, pero el texto completo está tras muro de pago en Elsevier (403 a `WebFetch`).
  **No he intentado sortearlo.** Sin el cuerpo del artículo no puedo decir si es un recall sobre los
  tipos ausentes del train —comparable al del TFG— o una lectura agregada. **Es la verificación
  pendiente de mayor valor de este informe**, porque Kim es el antagonista directo.
- **La topología real de Khraisat *et al.* (2020).** MDPI devuelve 403 tanto a `WebFetch` como con
  navegador. Su título dice «*stacking ensemble*» (patrón D), Macko *et al.* lo clasifican como
  paralelo (patrón C), y con solo el resumen no puedo dirimirlo. Todo lo que afirmo de esa fuente
  sale del resumen y de sus metadatos verificados.
- **Texto completo de la mayoría de las fuentes primarias.** De las catorce obras de arquitectura,
  solo he leído íntegras **tres** (ADAM, Sommer y Paxson, Macko *et al.*) y una vía PMC (Fang y Xie).
  Del resto dispongo de resumen y metadatos verificados —suficiente para caracterizar la
  arquitectura y para citar, insuficiente para afirmar detalles de implementación—. Está marcado
  caso por caso en la tabla de fuentes con «solo resumen».
- **Que el patrón A canónico *siempre* permita a la etapa 2 vetar a la etapa 1.** Lo he verificado
  en ADAM (texto completo, la clase «falsa alarma» se filtra explícitamente) y está enunciado en el
  resumen de Tombini. **No lo he verificado en Ji (2016) ni en de Assis (2014)**, así que la
  afirmación de §6 se limita a los dos trabajos donde consta.
- **de Assis *et al.* (2014).** Aparece en la taxonomía de Macko *et al.* como patrón A y **no lo he
  verificado de forma independiente**; no sostiene ninguna afirmación de este informe.
- **Páginas exactas de Arp *et al.* (2022) y de Bendale y Boult (2016).** USENIX devolvió 403 y
  colab.ws no las lista. Prefiero omitirlas a inventarlas.
- **Contradicciones con decisiones cerradas del proyecto: ninguna encontrada.** Con un matiz que
  detallo en `## Implicaciones`: la literatura muestra que la premisa de **H-5** («en una cascada
  pura, la binaria del híbrido coincide con la de la etapa 1») es correcta **para el diseño
  elegido**, pero no describe la cascada anomalía→firmas canónica, donde la etapa 2 sí modifica la
  decisión binaria.

## Fuentes

| # | Fuente | Nivel | Fecha | Cita completa | URL / DOI |
|---|---|---|---|---|---|
| 1 | ADAM: A Testbed for Exploring the Use of Data Mining in Intrusion Detection (**texto completo leído**, sitio oficial de la revista) | **1** | 2001-12 | D. Barbará, J. Couto, S. Jajodia y N. Wu, «ADAM: a testbed for exploring the use of data mining in intrusion detection», *ACM SIGMOD Record*, vol. 30, n.º 4, pp. 15-24, dic. 2001 | doi:10.1145/604264.604268 |
| 2 | A serial combination of anomaly and misuse IDSes applied to HTTP traffic (**solo resumen**, sitio oficial de ACSAC) | **1** | 2004-12 | E. Tombini, H. Debar, L. Mé y M. Ducassé, en *20th Annual Computer Security Applications Conference (ACSAC)*, IEEE, 2004, pp. 428-437 | doi:10.1109/CSAC.2004.4 |
| 3 | An intelligent intrusion detection system (IDS) for anomaly and misuse detection in computer networks (**solo resumen**) | **1** | 2005-11 | O. Depren, M. Topallar, E. Anarim y M. K. Ciliz, *Expert Systems with Applications*, vol. 29, n.º 4, pp. 713-722, 2005 | doi:10.1016/j.eswa.2005.05.002 |
| 4 | Hybrid Intrusion Detection with Weighted Signature Generation over Anomalous Internet Episodes (**solo resumen**) | **1** | 2007-01 | K. Hwang, M. Cai, Y. Chen y M. Qin, *IEEE Transactions on Dependable and Secure Computing*, vol. 4, n.º 1, pp. 41-55, 2007 | doi:10.1109/TDSC.2007.9 |
| 5 | Random-Forests-Based Network Intrusion Detection Systems (**solo resumen**, vía OpenAlex) | **1** | 2008-09 | J. Zhang, M. Zulkernine y A. Haque, *IEEE Transactions on Systems, Man, and Cybernetics, Part C (Applications and Reviews)*, vol. 38, n.º 5, pp. 649-659, 2008 | doi:10.1109/TSMCC.2008.923876 |
| 6 | Outside the Closed World: On Using Machine Learning for Network Intrusion Detection (**texto completo leído**, copia de los autores en ICSI, *green OA*) | **1** | 2010-05 | R. Sommer y V. Paxson, en *2010 IEEE Symposium on Security and Privacy*, pp. 305-316 | doi:10.1109/SP.2010.25 |
| 7 | A hybrid network intrusion detection framework based on random forests and weighted k-means (**solo resumen**) | **1** | 2013-12 | R. M. Elbasiony, E. A. Sallam, T. E. Eltobely y M. M. Fahmy, *Ain Shams Engineering Journal*, vol. 4, n.º 4, pp. 753-762, 2013 | doi:10.1016/j.asej.2013.01.003 |
| 8 | Toward Open Set Recognition (**solo resumen**) | **1** | 2013-07 | W. J. Scheirer, A. de Rezende Rocha, A. Sapkota y T. E. Boult, *IEEE Transactions on Pattern Analysis and Machine Intelligence*, vol. 35, n.º 7, pp. 1757-1772, 2013 | doi:10.1109/TPAMI.2012.256 |
| 9 | A novel hybrid intrusion detection method integrating anomaly detection with misuse detection (**solo resumen**; texto completo tras muro de pago) | **1** | 2014-03 | G. Kim, S. Lee y S. Kim, *Expert Systems with Applications*, vol. 41, n.º 4, pp. 1690-1700, 2014 | doi:10.1016/j.eswa.2013.08.066 |
| 10 | Towards Open Set Deep Networks (OpenMax) (**solo resumen**) | **1** | 2016-06 | A. Bendale y T. E. Boult, en *2016 IEEE Conference on Computer Vision and Pattern Recognition (CVPR)*, 2016 | doi:10.1109/CVPR.2016.173 |
| 11 | A two-level hybrid approach for intrusion detection (**solo resumen**) | **1** | 2016-11 | C. Guo, Y. Ping, N. Liu y S. Luo, *Neurocomputing*, vol. 214, pp. 391-400, 2016 | doi:10.1016/j.neucom.2016.06.021 |
| 12 | A multi-level intrusion detection method for abnormal network behaviors (**solo resumen**) | **1** | 2016-02 | S.-Y. Ji, B.-K. Jeong, S. Choi y D. H. Jeong, *Journal of Network and Computer Applications*, vol. 62, pp. 9-17, 2016 | doi:10.1016/j.jnca.2015.12.004 |
| 13 | Open Set Intrusion Recognition for Fine-Grained Attack Categorization (**registro verificado**; contenido leído en el preprint) | **1** (registro) / 2 (texto) | 2017 | S. Cruz, C. Coleman, E. M. Rudd y T. E. Boult, en *2017 IEEE International Symposium on Technologies for Homeland Security (HST)*, IEEE, 2017. Preprint: arXiv:1703.02244 | doi:10.1109/THS.2017.7943467 |
| 14 | Hybrid Network Intrusion Detection Systems: A Decade's Perspective (**solo ficha del editor**) | **1** | 2017 | A. K. Dalai y S. K. Jena, en *Proc. Int. Conf. on Signal, Networks, Computing, and Systems*, Lecture Notes in Electrical Engineering, vol. 395, Springer, Nueva Delhi, 2017 | doi:10.1007/978-81-322-3592-7_35 |
| 15 | TSDL: A Two-Stage Deep Learning Model for Efficient Network Intrusion Detection (**solo resumen**) | **1** | 2019 | F. A. Khan, A. Gumaei, A. Derhab y A. Hussain, *IEEE Access*, vol. 7, pp. 30373-30385, 2019 | doi:10.1109/ACCESS.2019.2899721 |
| 16 | Survey of intrusion detection systems: techniques, datasets and challenges (**texto completo leído**, vía navegador) | **1** | 2019-07 | A. Khraisat, I. Gondal, P. Vamplew y J. Kamruzzaman, *Cybersecurity*, vol. 2, art. 20, 2019 | doi:10.1186/s42400-019-0038-7 |
| 17 | Hybrid Intrusion Detection System Based on the Stacking Ensemble of C5 Decision Tree Classifier and One Class Support Vector Machine (**solo resumen**; MDPI devuelve 403) | **1** | 2020-01 | A. Khraisat, I. Gondal, P. Vamplew, J. Kamruzzaman y A. Alazab, *Electronics*, vol. 9, n.º 1, art. 173, 2020 | doi:10.3390/electronics9010173 |
| 18 | A hybrid machine learning model for intrusion detection in VANET (**solo resumen**) | **1** | 2022-03 | H. Bangui, M. Ge y B. Buhnova, *Computing*, vol. 104, n.º 3, pp. 503-531, 2022 | doi:10.1007/s00607-021-01001-0 |
| 19 | Dos and Don'ts of Machine Learning in Computer Security (**solo resumen y metadatos**; USENIX devuelve 403) | **1** | 2022-08 | D. Arp, E. Quiring, F. Pendlebury, A. Warnecke, F. Pierazzi, C. Wressnegger, L. Cavallaro y K. Rieck, en *31st USENIX Security Symposium*, USENIX Association, 2022 | https://www.usenix.org/conference/usenixsecurity22/presentation/arp · preprint arXiv:2010.09470 |
| 20 | Zero-day attack detection: a systematic literature review (**solo resumen**) | **1** | 2023-02 | R. Ahmad, I. Alsmadi, W. Alhamdani y L. Tawalbeh, *Artificial Intelligence Review*, vol. 56, pp. 10733-10811, 2023 | doi:10.1007/s10462-023-10437-z |
| 21 | Assessing the Impact of a Supervised Classification Filter on Flow-based Hybrid Network Anomaly Detection (**texto completo leído** vía ar5iv). **Preprint sin publicación posterior localizada** | **2** | 2023-10-10 | D. Macko, P. Goldschmidt, P. Pištek y D. Chudá, arXiv:2310.06656 [cs.AI], 2023. **Usado solo como andamio de taxonomía; cada tipo se respalda con su fuente primaria de nivel 1** | doi:10.48550/arXiv.2310.06656 |
| 22 | A Dual-Tier Adaptive One-Class Classification IDS for Emerging Cyberthreats (**solo resumen**) | **2** | 2024-03-17 | Md. A. Uddin, S. Aryal, M. R. Bouadjenek, M. Al-Hawawreh y Md. A. Talukder, arXiv:2403.13010, 2024 | doi:10.48550/arXiv.2403.13010 |
| 23 | Unknown intrusion traffic detection method based on unsupervised learning and open-set recognition (**texto completo leído** vía PMC) | **1** | 2025-05 | J. Fang y C. Xie, *Scientific Reports*, vol. 15, art. 17001, 2025 | doi:10.1038/s41598-025-01084-1 |
| 24 | On optimum recognition error and reject tradeoff (**solo resumen**) | **1** | 1970-01 | C. K. Chow, *IEEE Transactions on Information Theory*, vol. 16, n.º 1, pp. 41-46, 1970 | doi:10.1109/TIT.1970.1054406 |
| 25 | HYBRID NETWORK INTRUSION DETECTION SYSTEMS: A SYSTEMATIC REVIEW | **3** | 2023 | A. Seiba, G. Abdul-Salaam, Y. Missah y M. H. Anisi, *Scientific and Practical Cyber Security Journal*, ISSN 2587-4667. **No sostiene ninguna afirmación de este informe**: se lista solo para dejar constancia de que la única revisión con recuentos que encontré no cuenta arquitecturas | https://journal.scsa.ge/papers/hybrid-network-intrusion-detection-systems-a-systematic-review/ |

**Evidencia interna** (no son fuentes externas; leída en disco el 2026-08-02):
`resumen-de-decisiones.md` (decisión 7 del 2026-07-02; H-1…H-7 del 2026-07-14; P-1…P-5; decisión
del 2026-07-15 y su fe de erratas del 2026-07-16) · `EL_FUTURO.md:45-68, 91-103` ·
`Obsidian_TFG_Vault/03 Diseño del sistema/3.2 Arquitectura del sistema.md` · `CLAUDE.md` ·
`features.md:20-27`.

**Nota metodológica sobre herramientas.** `WebFetch` fue la herramienta por defecto. Playwright se
usó **solo** tras fallo documentado de `WebFetch`, en dos dominios: `link.springer.com` (303 hacia
`idp.springer.com`, dos intentos) para leer Khraisat *et al.* 2019, con éxito; y `www.mdpi.com`
(403) para Khraisat *et al.* 2020, **sin** éxito —el 403 se repitió con navegador—. No se inició
sesión en ningún sitio ni se intentó sortear ningún muro de pago. Varios PDF que `WebFetch` no supo
parsear se leyeron con la herramienta de lectura de PDF sobre el fichero descargado (ADAM, Sommer y
Paxson).

## Cambios en Bibliografía.md

**Ninguno.** Por encargo explícito del *leader*: `Bibliografía.md` está bajo auditoría abierta
(`features.md:22-27`) y no se toca en este ciclo. Las fuentes quedan completas y clasificadas en la
tabla `## Fuentes`. Candidatas a entrada nueva si Francisco decide citarlas en los capítulos 2 y 3:
las nº 1, 2, 3, 5, 6, 8, 9, 10, 13, 16, 19 y 24.

## Implicaciones para el proyecto

> [!warning] Propongo, no decido
> Nada de esta sección crea tarea, toca código ni reabre el track de código —cerrado el 2026-07-16.
> Es material para que Francisco redacte los capítulos 2 y 3 y decida.

### A. Lo que este informe **respalda** de lo ya decidido (uso directo en 3.2)

Cuatro decisiones cerradas ganan cita externa y no hay que retocarlas:

1. **Decisión 7 (cascada anomalía→firmas).** Deja de ser una elección de ingeniería del autor para
   ser la **arquitectura fundacional** del campo: ADAM (2001) y Tombini *et al.* (2004). Sugerencia
   de redacción para 3.2.2: abrir el apartado situando la decisión en esa tradición **antes** de
   dar el argumento propio.
2. **Etapa 1 entrenada solo con D1.** Sommer y Paxson (2010) enuncian el requisito y su precio con
   una precisión que 3.4 puede citar literalmente. Además **explica** el FPR del 8-10 %: no es un
   defecto del autoencoder, es el coste estructural de tener «una única categoría contra la que
   comparar».
3. **Etapa 2 como traductora, no como detectora.** El *semantic gap* de Sommer y Paxson es el
   nombre publicado de lo que hace la etapa 2 en 3.2.3. Es probablemente **el mejor argumento
   disponible** para responder a «¿para qué la segunda etapa, si la binaria no cambia?» (H-5): la
   segunda etapa no existe para mejorar la binaria, existe para cerrar la brecha semántica.
4. **Protocolo 0-day y baseline monolítico.** Que Cruz *et al.* (2017) constaten que el protocolo
   cerrado es la norma, y que Arp *et al.* (2022) señalen el *baseline* inapropiado como sesgo
   generalizado, convierten dos decisiones del TFG (recall por tipo sobre los 17 tipos nativos;
   `baseline.py`) en **aciertos metodológicos citables**, no en trabajo extra.

### B. La divergencia que hay que **declarar**, no corregir

La cascada canónica del patrón A permite a la etapa 2 devolver un sospechoso a «falsa alarma»
—ADAM la filtra explícitamente— y ahí es donde esos sistemas recuperan precisión. **Este TFG se lo
prohíbe por diseño** (H-5, P-5: la etapa 2 no tiene clase `normal`).

- **No contradice ninguna decisión cerrada.** H-5 es correcta *dentro* de su premisa. Pero su
  redacción actual («en una cascada **pura** anomalía→firmas la respuesta es trivial») puede leerse
  como si **toda** cascada anomalía→firmas tuviera esa propiedad, y la literatura dice que no: la
  tienen las cascadas cuya etapa 2 carece de clase «normal», que es una **elección**, no una
  necesidad del patrón.
- **Propuesta de redacción (no de código):** en 3.2.2 o en 3.6, una frase que reconozca que la
  variante canónica usa la etapa 2 como filtro de falsos positivos y que este trabajo renuncia a
  ello a cambio de una etapa 2 especializada exclusivamente en categorizar. Convierte una
  vulnerabilidad de defensa —«su híbrido no mejora la binaria»— en una decisión declarada con su
  contrapartida.
- **Relación con `EL_FUTURO.md`:** es pariente cercano, pero **no idéntico**, de la línea «fusión
  por meta-clasificador» de `EL_FUTURO.md:66-68`. Aquella propone sustituir la cascada por un
  *stacking*; esta sería conservar la cascada y dotar a la etapa 2 de una clase `normal`. Si
  Francisco quiere anotarla, encaja en `EL_FUTURO.md §2`. **No la añado yo.**

### C. El hallazgo de mayor valor inmediato: el 13,4 % tiene explicación publicada

`resumen-de-decisiones.md` registra que solo el 13,4 % de los 0-day cazados por la etapa 1 acaban
en `unknown`, y `EL_FUTURO.md:60-65` ya lo apunta como línea futura de *open-set recognition*. Lo
que este informe añade **no es la línea futura** —ya estaba— sino su **fundamento teórico**:

- Scheirer *et al.* (2013): umbralizar un clasificador de conjunto cerrado **no acota el riesgo de
  espacio abierto**.
- Bendale y Boult (2016): OpenMax **supera explícitamente al umbralizado de la salida
  probabilística**, que es el mecanismo de `UMBRAL_CONF`.
- Chow (1970): la regla de rechazo es óptima **sobre las posteriores verdaderas**, y `predict_proba`
  de un RandomForest no lo es.

**Uso propuesto:** en 5.3 y/o 6.1, presentar el 13,4 % no como una anomalía del experimento sino
como **la manifestación medida de un límite conocido del método**. Cambia el tono de «esto nos ha
salido regular» a «esto es lo que la teoría predice, y lo hemos cuantificado en nuestro sistema».

### D. La pregunta que un tribunal puede hacer, y su respuesta

*«¿Por qué anomalías primero? Kim et al. (2014), sobre este mismo dataset, lo hace al revés.»*

La respuesta que sostiene este informe tiene tres patas, ninguna inventada:

1. **De diseño (ya en 3.2.2):** la etapa 2 se entrena solo con D3 y no conoce la clase `normal`; si
   fuera primera, condenaría tráfico legítimo en masa.
2. **De cobertura (Tombini 2004):** con las firmas delante, lo desconocido solo se examina en el
   residuo que las firmas no reclamaron; con las anomalías delante, todo el tráfico pasa por el
   único componente capaz de ver lo que nunca ha visto.
3. **De honestidad (el precio):** el orden inverso se elige en la literatura **para bajar el FPR**
   (Macko *et al.*, 2023), y este TFG paga ese precio —FPR 0,102 frente al 0,027 del baseline
   monolítico— y **lo reporta junto al recall 0-day** por decisión P-2. Reconocerlo antes de que lo
   pregunten es más fuerte que defenderlo.

### E. Lo que este informe **no** propone (a fecha de redacción, 2026-08-02)

Para que nadie lo lea como catálogo de mejoras: no propongo cambiar el orden de la cascada, ni
implementar OpenMax, ni dar clase `normal` a la etapa 2, ni cerrar el bucle de generación de firmas
al estilo de Hwang *et al.* (2007). El sistema está construido, ejecutado y evaluado. Lo único que
propongo es **cómo contarlo** en los capítulos 2 y 3, y **con qué citas**.

---

## Decisiones tomadas a partir de este informe

> [!note] Bloque añadido a posteriori (ficha **T17**, punto 1)
> Las secciones anteriores son del **2026-08-02** y están redactadas en modo «propongo, no decido».
> Este bloque cierra el ciclo: recoge **qué se convirtió efectivamente en decisión** y **qué se
> descartó** en el `grill-me` del **2026-08-06** y en los cierres posteriores. Fuentes de verdad:
> `resumen-de-decisiones.md` (§ Decisiones del 2026-08-06 y del 2026-08-09) y `features.md`
> (lote T0-T17 y su tabla «Descartado — no reabrir»). **No se añade aquí ninguna decisión que no
> conste en esos dos ficheros.**

### 1. Lo que se convirtió en decisión

| Qué salió de este informe | En qué decisión cuajó | Dónde consta |
|---|---|---|
| El contraste con el patrón B (firmas→anomalías) y con Kim *et al.* (2014) como antagonista directo | **Medición contrafactual de la cascada invertida (ficha T3)**, una de las «dos mediciones baratas» de la **decisión marco (a)** del 2026-08-06, que reabre el track de código de forma declarada y acotada | `resumen-de-decisiones.md`, § Decisiones del 2026-08-06; `features.md` (lote T0-T17) |
| Esa medición, ya ejecutada | `Implementacion/app/cascada_invertida.py`: **cero `fit`**, sobre modelos ya persistidos, con tabla propia (`metricas_cascada_invertida.csv`). Cerrada el **2026-08-10** con dictamen `auditor-ml` **APTO** | `features.md` (T3, cerrada en `b1f1df2`); `Implementacion/PIPELINE.md`, § «La cascada invertida (T3)» |
| La pregunta «¿por qué no al revés, como Kim?» (§6 y §D) | **Tres patas para `3.2.2`**: diseño (la etapa 2 no conoce `normal`), cobertura (Tombini *et al.*, 2004) y *semantic gap* (Sommer y Paxson, 2010), **más el precio declarado** (FPR del híbrido frente al del baseline monolítico) y **el número de T3** | `features.md`, ficha **T9** (capítulo 3) |
| La divergencia del §B (en ADAM la etapa 2 filtra «falsa alarma»; aquí se le prohíbe por diseño) | **Se declara, no se corrige**: matiz sobre **H-5** —correcta *dentro* de su premisa, pero no describe *toda* cascada anomalía→firmas— destinado a `3.2`/`3.6` | `features.md`, ficha **T9** |
| El escalón 3 (*open-set recognition*) como explicación teórica del enrutado a `unknown` | **Se usa como fundamento teórico de un resultado medido**, no como propuesta de método: `unknown` es formalmente *open-set*, lo que justifica reportar la tasa de enrutado como métrica propia (decisión **H-6**) | `features.md`, ficha **T9** (`3.3`) |
| Arp *et al.* (2022) sobre sesgos de evaluación y *baseline* inapropiado | Refuerzo de la **decisión P-2** (reportar el FPR junto al recall 0-day) y del **modelo de amenaza explícito** de `3.1` (**P10**) | `features.md`, ficha **T9** (`3.1`) |
| El marco general de los cuatro informes del lote | **Criterio rector**: refinar el proyecto o **enseñar el límite**, nunca sucedáneos; las imposibilidades se declaran con su razón técnica | `resumen-de-decisiones.md`, § Decisiones del 2026-08-06 |

**Cómo se cita el número de T3, sin excepción.** De las **9.711 filas normales de D2**, el
clasificador de firmas condenaría **6.558 (67,53 %)** a 54 características y **3.329 (34,28 %)** a
122. Es una **cota inferior de falsos positivos irrecuperables**, **no** «el FPR de un sistema de
firmas-primero»: en el sistema publicado `unknown` **es alarma** (decisión **P-5**), así que lo que
cae bajo umbral no queda exonerado. La forma exacta de citarlo está en `PIPELINE.md`.

### 2. Lo que se descartó

| Descartado | Razón registrada |
|---|---|
| **Invertir de verdad la cascada** (construir el sistema firmas→anomalías completo) | No es invertir, es **construir otro sistema**: la etapa 2 no tiene clase `normal` (`firmas.py`), así que exigiría reentrenarla a 5 clases y mover `4.5`, `5.2` y la comparabilidad de H1. Y Kim *et al.* tampoco se limita a invertir el orden. **Sustituido por la medición T3** |
| **Dar clase `normal` a la etapa 2** para que pueda vetar a la etapa 1, como en ADAM | Queda como **divergencia declarada** en la memoria, no como cambio. Es pariente —no idéntico— de la línea «fusión por meta-clasificador» de `EL_FUTURO.md`, que tampoco se implementa |
| **Stacking como solución al `unknown`** (patrón D, Khraisat *et al.* 2020) | No puede aprender la clase que importa: de `unknown` **no hay ni un ejemplo** en el entrenamiento (D3 son solo ataques conocidos). Es un problema de conjunto abierto y el *stacking* supervisado no es la herramienta |
| **Implementar OpenMax / W-SVM** a partir del escalón 3 | El track de código se reabrió **acotado** a T1-T4: nada más entra. El material de *open-set* queda como explicación teórica y como línea futura |
| **Cerrar el bucle de generación de firmas** (patrón F, Hwang *et al.* 2007) | Fuera de alcance; se **nombra como límite consciente** en la memoria en lugar de implementarse |
| **Nota propia para «híbrido» o para la cascada invertida** | Son **párrafos dentro de notas que ya existen**. Sacarlos a nota propia es la complejidad que el criterio rector prohíbe |
| **Experimento adversario** para P10 | Incumpliría otro *pitfall* del propio Arp *et al.*: ataque en el espacio de características sin correspondencia en el espacio del problema. **Sustituido por el modelo de amenaza escrito**. Ojo con la atribución: la distinción *feature space* / *problem space* es de **Pierazzi *et al.***, no de Arp *et al.* |

### 3. Lo que quedó pendiente, y no es decisión

- **Kim *et al.* (2014)** sigue citado **solo por su resumen** (muro de pago en Elsevier, sin acceso
  institucional). Es la verificación **de mayor valor** de este informe, por ser el antagonista
  directo de `3.2.2`, y está de guardia en `features.md` (fichas **T14** y «PDF sin acceso
  institucional»). Toda nota de la memoria que lo cite **nace con el callout de verificación
  pendiente**.
- **Khraisat *et al.* (2020)** se cita **sin cifra**, solo con metadatos verificados: su topología
  real (patrón C o D) no se pudo dirimir.

> [!todo] Sin respaldo documental que citar aquí
> Este informe **no** figura como origen de ninguna decisión registrada sobre `2.2.3`/`2.2.4` (la
> *dilución del término «híbrido»* del §1 sigue siendo propuesta, no decisión) ni sobre `6.2`. Si
> alguna de esas dos se cerró en algún sitio, no consta en `resumen-de-decisiones.md` ni en
> `features.md` a fecha de esta pasada, y **no se inventa aquí**.

> [!note] Corrección de autoría, en la misma pasada
> La **decisión marco (b)** del 2026-08-06 retiró la regla «la teoría en prosa la escribe Francisco»:
> el capítulo `2.x` lo redacta el `redactor-tfg` sin excepción (`2.1.4` incluida, confirmado al
> cerrar **T0** el 2026-08-09) y `6.2 Líneas futuras` pasa a **borrador de agente con revisión final
> de Francisco**. **Este informe no contenía esa afirmación desfasada** —sí la contienen dos de sus
> hermanos, que se corrigen en sus propios ficheros—, de modo que aquí no hay nada que rectificar.
