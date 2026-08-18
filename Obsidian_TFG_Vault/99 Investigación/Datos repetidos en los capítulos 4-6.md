---
titulo: "Datos repetidos en los capítulos 4, 5 y 6 — diagnóstico previo al recorte"
tipo: informe de investigación interna
fecha: 2026-08-18
estado: cerrado
alcance: diagnóstico. NO aplica cambios en ninguna nota de la memoria
encargo: Tanda B del Grupo IV, pieza 2 (análisis)
---

# Datos repetidos en los capítulos 4-6

> [!warning] Este informe no es memoria
> Vive en `99 Investigación/` como insumo de la tarea de recorte de los capítulos 4-6. **No se
> enlaza desde `00 Índice TFG.md`** y su prosa no se vuelca a ningún capítulo. Ninguna cifra
> publicada se ha movido ni reescrito al elaborarlo: donde se detecta una discrepancia, se
> **reporta** (§5) y no se corrige.

**Encargo.** La Decisión 4 del `grill-me` del Grupo IV (`resumen-de-decisiones.md`, sección
«Decisiones del 2026-08-18 — `grill-me` del Grupo IV») ordena que los capítulos 4-6 lleven un
**barrido nuevo que produzca su propio informe con decisiones ANTES de tocar ninguna nota**: «no se
improvisan recortes sobre 52k palabras sin verificar». Este documento es ese informe. Sigue el
formato y el nivel de rigor de [[Datos repetidos en el capítulo 3]], que es su hermano para el
capítulo 3.

**Criterios heredados, que aquí solo se aplican y no se rediscuten.**

| Criterio | Enunciado | Sede |
|---|---|---|
| **T7** | Lo que salga del cuerpo **se MUEVE a `A.3 Ficha del sistema`, nunca se borra** | Decisión 4 |
| **Hiperparámetros y semilla** | Los valores concretos van a `A.3`; en el cuerpo, **qué se buscó y por qué**, con remisión | Decisión 5 |
| **Excepciones que se quedan** | El umbral **p95**, el **99,9 %** de importancia acumulada y **la semilla 42 en `5.2`** — ahí el número **es** el argumento | Decisión 5 |
| **Referencia por título** | Toda sede se cita por **título de sección o fragmento literal**, nunca por `fichero:línea` | `CLAUDE.md`, Normas de trabajo |

---

## 0. Verificación: qué se ha leído y con qué alcance

De la fiabilidad de este cuadro depende que se pueda confiar en las afirmaciones del tipo «única
sede donde aparece».

| Nivel de lectura | Notas |
|---|---|
| **Leídas íntegras** | `4.1`, `4.2`, `4.3`, `4.4`, `4.5`, `4.6`, `5.0`, `5.1`, `5.2`, `5.3`, `5.4`, `6.1`, `6.2` |
| **Leídas por búsqueda dirigida** (solo los pasajes citados y su contexto inmediato) | `A.3` (§A.3.3 Configuraciones seleccionadas, §A.3.4 Alcance de cada métrica, §A.3.6 bloque de máquina), `A.2` (índice de apartados) |
| **No abiertas** | Todo el capítulo 2, todo el capítulo 3, el capítulo 1, `A.1`, `Bibliografía.md` |

**Las trece notas de los capítulos 4-6 se han leído enteras.** Todas las citas literales de §1 se han
localizado en el fichero indicado.

> [!warning] Consecuencia: las afirmaciones de exclusividad son acotadas
> Un «única sede» de este informe significa **«única sede entre las notas leídas»**. Los capítulos 2
> y 3 **no se han abierto** en este barrido —el capítulo 3 lo está ejecutando otro agente en
> paralelo—, de modo que **cualquier solape adicional con el capítulo 2 queda fuera de este
> informe**. Esa fue exactamente la causa de tres fallos del informe del capítulo 3 (S4, S2 y S7).
> Antes de ejecutar un borrado apoyado en «no está en ningún otro sitio», conviene un `grep` sobre
> el vault completo.

---

## 1. Solapes verificados contra disco

Leyenda de **Sedes**: número de emplazamientos **distintos** en los que la afirmación aparece
**desarrollada**, no simples menciones de paso ni wikilinks. Un emplazamiento es **un pasaje**, no
un fichero: dos apartados de la misma nota cuentan dos veces.

| # | Qué se repite | Sedes (por título de apartado) | Sedes |
|---|---|---|---:|
| **D1** | **Qué mide cada familia de columnas de tiempo** y su salvedad de máquina no dedicada | `4.4` § *El coste se publica bajo dos alcances separados* + callout *Estos segundos no son una propiedad del algoritmo* · `5.0.4` tabla de familias (a)/(b) · `5.1.2` callout *Qué mide cada columna de tiempo, y hasta dónde vale* · `5.4` § *Qué NO mide la latencia publicada* · `6.1.4` límite 2, punto 1 · `A.3.4` viñeta *Las columnas de tiempo* | **6** |
| **D2** | **La dispersión 4,8× del `tiempo_s` del Autoencoder** (37,71 s ↔ 181,91 s), el reparto interno del bloque y la no reproducibilidad de `ac496cb` | `4.4` callout *Estos segundos no son una propiedad del algoritmo* (versión larga, con los Δ del residual) · `A.3.6` § *Bloque de máquina*, viñetas *Dispersión del `tiempo_s`, sin causa atribuida* y *Recuento de épocas* + callout *Salvedad obligatoria: `ac496cb` no es reproducible desde git* · `6.1.4` límite 2 | **3** |
| **D3** | **La salvedad de las tres decisiones tomadas mirando D2** (H-2, H-3, Q1/C). **Ojo: no todas las sedes la *enumeran*** — ver el desglose de §2, D3 | `4.3.5` § *Decisión experimental* (sede canónica declarada) · `4.3.7` última viñeta · `4.4` punto 3 del protocolo · `4.5` viñeta *D2 es intocable…* · `4.6` callout *Alcance real de la regla: qué sí miró D2* · `5.0.4` párrafo *Como contrapartida honesta* · `5.1.4` callout *La elección del detector ganador sí usó métricas de D2* · `5.2.3` callout *La elección del clasificador ganador sí usó métricas de D2* · `5.4` caveat 4 · `6.1.3` cuarta viñeta · `A.3.7` § *Límite de protocolo* | **11** (de ellas **7** enumeran) |
| **D4** | **Enumeración uno a uno de los 17 tipos 0-day** (`apache2`, `httptunnel`, …, `xterm`) | `4.2.1` callout *Procedencia del «17»: medido en disco, no citado* · `4.3.6` propiedad 1 (**la misma lista de 17 nombres**) · (`A.1`, no abierta aquí, la trae marcada con ★) | **2** (+`A.1`) |
| **D5** | **Composición de D3 por categoría**: `dos` 45.927 · `probe` 11.656 · `r2l` 995 · `u2r` 52, ratio ≈ 883:1 | `4.2.1` callout *Procedencia del 78,3 % de DoS en D3* (desglose completo en prosa) · `4.3.4` primer párrafo (883:1) · `4.3.6` propiedad 2 (**tabla**) · `4.5` viñeta *Métrica de selección* (52 / 45.927 / 0,09 %) · `5.2.2` tercera viñeta (52 en D3) · `5.4` § *Etapa 2 (firmas)* (52) | **6** |
| **D6** | **Tabla D1/D2/D3 con contenido y tamaños** | `4.2.1` § *Tamaño y reparto de los subconjuntos* · `4.3.6` tabla de tres filas · `5.0.1` tabla con función exclusiva y sub-splits | **3** |
| **D7** | **`delta = (A) − (B)` es una comparación, no una descomposición** (mismo callout, casi palabra por palabra) | `4.2.1` callout homónimo · `5.1.3` callout homónimo | **2** |
| **D8** | **El FPR real por variante, 10,2 % / 8,5 %, y la regla de no citarlo como rango** | `4.2.1` párrafo *Que exista desplazamiento en (A) no es un problema* · `5.0.4` callout *La misma cifra, dos variantes, dos números* · `5.1.3` tabla *El exceso, por variante* · `6.2.6` peldaño 2, § *Qué sí puede hacerse hoy* | **4** |
| **D9** | **Las cuatro transformaciones del preprocesado y dónde se ajusta cada una** | `4.3.7` tabla de cuatro filas (sede única declarada) · `5.0.6` § *C5 con detalle: dónde se ajusta cada transformación* (**las mismas cuatro, reenumeradas**) · `4.6` § *La ausencia de fuga…* · `6.1.4` fila P3 de la tabla | **4** |
| **D10** | **Rejillas de búsqueda y configuraciones ganadoras con sus valores** | `4.4` § *Algoritmos y espacios de búsqueda* + § *Configuraciones ganadoras* · `4.5` § *Algoritmos y espacios de búsqueda* + § *Configuraciones ganadoras* · `A.3.3` (**las mismas configuraciones, a 6 decimales**) | **5** |
| **D11** | **SMOTE dentro de cada *fold* como garantía anti-*leakage*** | `4.3.4` párrafo *Un detalle metodológico es crítico* + bloque de código · `4.5` viñeta *Balanceo* · `4.6` § *La ausencia de fuga…* · `5.2.3` callout de H-3 · `6.1.1` objetivo 5 | **5** |
| **D12** | **El eje de balanceo SMOTE vs `class_weight` no es constante entre semillas** (17/40 y 40/40) | `5.2.4.4` (desarrollo completo, tres tablas) · `5.4` § *Una decisión de preprocesado que se declara no establecida* (**las tres precisiones repetidas + tabla de qué publica 5.2**) | **2** |
| **D13** | **La banda de semillas de RandomForest** [0,7779–0,8205], media 0,8035, y «gana 8 de 10» | `5.2.3` callout *La distancia RandomForest–HistGradientBoosting no establece un orden* · `5.2.4.1` · `5.2.4.2` · `5.4` § *Etapa 2 (firmas)* · `5.4` caveat 2 · `A.3.6` § *El titular (semilla 42) frente a la banda* | **6** |
| **D14** | **El 13,4 % de enrutado a `unknown` + la aclaración P-5** (los 2.504 siguen alarmados) | `5.3` § *El enrutado a `unknown`: el 13,4 %, explicado* (desarrollo en 3 afirmaciones) · `5.3` cierre del § *Análisis de ataques desconocidos* (**repite el matiz P-5 y los 2.504**) · `5.4` segundo hallazgo · `6.1.3` tercera viñeta · `6.1.4` límite 5 · `6.2.2` + su callout de procedencia | **6** |
| **D15** | **Complementariedad de los detectores**: `mailbomb` 0,000 vs LOF 0,823 · `snmpguess` 0,018 vs IF 0,740 | `5.3` hallazgo 1 · `5.4` primer hallazgo · `6.2.1` tabla de dos filas | **3** |
| **D16** | **`snmpgetattack` como punto ciego universal** y límite de la representación por flujo | `5.3` hallazgo 2 · `5.4` tercer hallazgo · `6.1.3` última viñeta · `6.2.6` peldaño 3 (razonamiento en tres pasos) | **4** |
| **D17** | **Contraste con el baseline monolítico**: 0,771 vs 0,150 (≈5×), f1_macro 0,909 → 0,472, `r2l` 0,004 / `u2r` 0,010 | `5.3` § *Comparación con el baseline RF monolítico* (tabla + cuatro viñetas) · `5.4` § *Sobre el sistema híbrido* (tres viñetas con **las mismas cifras**) · `6.1.2` (**el mismo párrafo por tercera vez**) | **3** |
| **D18** | **El coste de la cascada sobre lo conocido**: 0,822 → 0,748, «~7,4 puntos» | `5.3` viñeta *El coste del filtro* · `5.3` párrafo de cierre de la sección · `5.4` caveat 2 · `4.6` § *Decisiones de preprocesado…* (variante 0,822 / 0,696) | **4** |

---

## 2. Qué hacer con cada solape, y dónde queda la versión canónica

Las frases de remisión están redactadas para **insertarse tal cual**. Siguen el patrón que la
memoria ya usa con éxito en `4.5` («La tabla completa del reparto **no se reproduce aquí**: su sede
es 4.3.6, y esta sección solo remite a ella»): no un wikilink suelto, sino una frase que dice **qué
no se repite y por qué**.

### D1 · Las dos familias de columnas de tiempo — **unificar; canónica en `5.0.4`**

| | |
|---|---|
| **Acción** | Dejar el desglose (a)/(b) **solo** en `5.0.4`. `4.4` y `5.1.2` sustituyen su explicación por una remisión de una frase |
| **Canónica** | **`5.0.4`**, tabla de familias — es protocolo, y ahí es donde el capítulo declara qué se puede y qué no se puede afirmar de una cifra de tiempo |
| **Qué se mueve a `A.3`** | Nada nuevo: `A.3.4` ya trae la viñeta *Las columnas de tiempo*. **T7 se cumple sin mover material** porque el destino ya lo contiene |
| **Verificación literal** | `4.4`: «**Entrenamiento (s)** = `tiempo_entrenamiento_s`: **solo los `fit` de la búsqueda en rejilla**». `5.1.2`: «**Entrenamiento (s)** = columna `tiempo_entrenamiento_s`: **solo los `fit` del grid de búsqueda**». `5.0.4`: «`tiempo_entrenamiento_s` es **solo los `fit` del grid**» |

> **Frase a insertar en `4.4`, sustituyendo al desglose y al callout largo:**
>
> «Las dos columnas de coste se publican por separado —`tiempo_entrenamiento_s`, solo los `fit` de
> la rejilla, y `tiempo_s`, el bloque completo del algoritmo— porque miden cosas distintas. **El
> alcance exacto de cada familia de columnas de tiempo, y la salvedad de que ninguna de ellas es una
> propiedad del algoritmo, se fijan en [[5.0 Protocolo de evaluación|5.0]] (§5.0.4, prohibición 4);
> aquí no se repiten.**»

> **Frase a insertar en `5.1.2`, sustituyendo al callout *Qué mide cada columna de tiempo*:**
>
> «Las dos columnas de tiempo se leen bajo la prohibición 4 del protocolo
> ([[5.0 Protocolo de evaluación|5.0]], §5.0.4): son *wall-clock* de un pase único en máquina no
> dedicada y **valen como comparación relativa dentro de esta corrida, no como propiedad del
> algoritmo**.»

### D2 · La dispersión 4,8× del `tiempo_s` — **recortar de `4.4`; ya está entera en `A.3`**

| | |
|---|---|
| **Acción** | Suprimir de `4.4` el callout *Estos segundos no son una propiedad del algoritmo* completo, incluidos los tres párrafos sobre el reparto interno del bloque y las dos salvedades |
| **Canónica** | **`A.3.6` § *Bloque de máquina (NO es calidad y NO se cita como resultado)*** |
| **Por qué ahí** | Es el apartado que el propio `A.3` abre diciendo «Se publica aparte a propósito». Y `6.1.4` **ya remite allí**: «véase [[A.3 Ficha del sistema]] § *Dispersión del `tiempo_s`, sin causa atribuida*» |
| **T7** | **Nada se pierde y nada hay que mover**: verificado en disco, `A.3.6` trae ya las tres piezas —el 37,71 ↔ 181,91 s con factor 4,8× y calidad idéntica al bit, la no atribución de causa por falta de recuento de épocas, y el callout de que `ac496cb` no es reproducible desde git—. **Lo único que `4.4` aporta y `A.3` no** es el análisis del **residual como fracción del bloque** (los 4,5 puntos porcentuales y el descenso de `IsolationForest` 122 del 4.º al 6.º puesto): **eso sí hay que trasladarlo a `A.3.6`, no borrarlo** |

> **Frase a insertar en `4.4` en su lugar:**
>
> «Estos segundos son *wall-clock* de un pase único en una máquina no dedicada y **su dispersión
> entre corridas es grande**: la banda medida, sus dos salvedades de procedencia y el análisis del
> reparto interno del bloque están en el [[A.3 Ficha del sistema|Apéndice A.3]] (§A.3.6, *Bloque de
> máquina*) y en `Implementacion\PIPELINE.md`. **Aquí las cifras valen solo como orden de magnitud
> dentro de esta misma corrida.**»

### D3 · El inventario de las tres decisiones sobre D2 — **once sedes; recortar CINCO a remisión**

> [!important] Corrección tras auditoría: `4.4` y `4.5` **ya cumplen y no se tocan**
> La versión anterior de este informe mandaba la frase sustituta a **nueve** sedes, incluidas `4.4` y
> `4.5`. Verificado literalmente en disco: **esas dos no enumeran nada**. `4.4` (punto 3 del
> protocolo) y `4.5` (viñeta *D2 es intocable…*) dicen exactamente «es una de las **tres** decisiones
> tomadas sobre D2, y el inventario completo está en las limitaciones de [[6.1 Conclusiones]]» —una
> sola oración, ya en forma de remisión—. Sustituirlas por la frase canónica, que **sí** enumera las
> tres con sus siglas, las **alargaría** en un pase cuyo objeto es recortar. **No se tocan.**

**Recuento sede por sede, verificado en el texto de cada nota:**

| Sede | ¿Enumera las tres una a una? | Evidencia literal | Qué se hace |
|---|---|---|---|
| `4.3.5` § *Decisión experimental* | Sí | Sede **canónica** autodeclarada | **No se toca** (canónica del alcance y las cifras) |
| `6.1.3` cuarta viñeta | Sí | «versión de referencia» del inventario, con las tres desarrolladas | **No se toca** (canónica del inventario) |
| `4.3.7` última viñeta | **Sí** | «Tres decisiones del sistema —el detector de la etapa 1, el clasificador de la etapa 2 y la elección del set de 54 características— se tomaron comparando métricas medidas sobre D2» | Recortar a la frase canónica |
| `4.6` callout *Alcance real de la regla* | **Sí**, y es la más larga: lista numerada de 3 puntos | «1. El **detector de la etapa 1** (Autoencoder…; decisión H-2). 2. El **clasificador de la etapa 2**… 3. El **set de características, 54 frente a 122**…» | Recortar a la frase canónica |
| `5.0.4` § *Como contrapartida honesta* | **Sí**, en prosa | «Tres decisiones del sistema —el detector de la etapa 1, el clasificador de la etapa 2 y el set de características— sí se tomaron con métricas medidas sobre D2» | Recortar a la frase canónica |
| `5.1.4` callout | **Sí** | «En total son **tres**…: esta (H-2), la de la etapa 2 (H-3…) y la del **set de características, 54 frente a 122** (Q1/C…)» | Recortar **solo** ese párrafo; conserva su propia decisión (H-2) |
| `5.2.3` callout | **Sí** | El mismo párrafo, con H-3 en el papel de «esta» | Recortar **solo** ese párrafo; conserva su propia decisión (H-3) |
| `5.4` caveat 4 | **Sí**, con siglas y criterios | «el detector de la etapa 1 (H-2, Autoencoder), el clasificador de la etapa 2 (H-3, RandomForest) y **el set de características, 54 frente a 122** (Q1/C…)» | Recortar a la frase canónica |
| `A.3.7` § *Límite de protocolo* | **Sí** | «**Lo que sí miró D2: tres decisiones.** El **detector de la etapa 1** (H-2), el **clasificador de…**» | Recortar a la frase canónica |
| `4.4` punto 3 del protocolo | **No** | «es una de las **tres** decisiones tomadas sobre D2, y el inventario completo está en las limitaciones de [[6.1 Conclusiones]]» | **YA CUMPLE — no se toca** |
| `4.5` viñeta *D2 es intocable…* | **No** | Misma oración, palabra por palabra | **YA CUMPLE — no se toca** |

**Resultado:** de las once sedes, **siete enumeran** (dos de ellas canónicas, que se quedan) y **dos
ya cumplen**. Las sedes a recortar son **cinco** —`4.3.7`, `4.6`, `5.0.4`, `5.4` y `A.3.7`— más los
**dos párrafos** de `5.1.4` y `5.2.3`, que no se sustituyen enteros.

| | |
|---|---|
| **Acción** | Ninguna de las once desaparece —el aviso es parte del rigor del trabajo—. Las dos canónicas se quedan enteras, `4.4` y `4.5` se quedan como están, y las siete restantes dejan de re-enumerar |
| **Canónica del alcance y las cifras** | **`4.3.5` § *Decisión experimental***, que ya se autodeclara sede canónica y cita los artefactos |
| **Canónica del inventario** | **`6.1.3`**, que ya se autodeclara «versión de referencia» del inventario |
| **Estado real** | El andamiaje de remisión **ya existe y es correcto**: `4.3.5` enumera sus diez remisiones y `6.1.3` declara ser la versión de referencia. **Lo que sobra no es la remisión, es que cada sede además re-enumere las tres decisiones con sus siglas y sus cifras** |

> [!important] Restricción vinculante: la formulación es canónica y está cerrada
> `resumen-de-decisiones.md` (punto **4. Formulación canónica**) fija literalmente el texto con el
> que se declara esta salvedad y obliga a usarlo «en cualquier sitio donde vuelva a aparecer esta
> salvedad, **para no tener dos redacciones de lo mismo**». Este informe **no propone redacción
> nueva**: la frase de abajo reproduce la canónica y solo le añade el reenvío. **No puede
> parafrasearse, resumirse ni omitirse su segunda mitad** —la que dice que las métricas son
> optimistas—, porque ahí vive la declaración de la limitación.

> **Frase a insertar en las cinco sedes que hoy reenumeran** (`4.3.7`, `4.6`, `5.0.4`, `5.4`,
> `A.3.7`), **sustituyendo a la lista de tres** — y **no** en `4.4` ni `4.5`, que ya remiten:
>
> «*Tres decisiones del sistema se tomaron mirando D2: el detector de la etapa 1, el clasificador de
> la etapa 2 y el set de características (54 frente a 122). Las tres son selección de modelo sobre
> el conjunto de test, es decir* data snooping, *y por tanto las métricas publicadas son optimistas
> respecto a lo que daría un test verdaderamente ciego.* Su alcance y sus cifras se fijan en
> [[4.3 Preprocesamiento de los datasets|4.3.5]] § *Decisión experimental*, y el inventario completo,
> como limitación del trabajo, en [[6.1 Conclusiones|6.1]] (§6.1.3); **el detalle de cada una no se
> reproduce aquí**.»
>
> *(Excepción: en `5.1.4` y `5.2.3` la sede conserva además **su propia** decisión —H-2 y H-3
> respectivamente—, porque es la que se toma en ese apartado. Lo que se recorta ahí es el párrafo
> «Este aviso cubre solo la decisión de esta etapa. En total son tres…», que reenumera las otras
> dos.)*

### D4 · Los 17 tipos 0-day enumerados — **recortar la segunda lista**

| | |
|---|---|
| **Acción** | En `4.3.6`, sustituir la enumeración de los 17 nombres por la cifra y la remisión. Conservar íntegro el callout de procedencia de `4.2.1`, que es lo que acredita el recuento |
| **Canónica de la enumeración** | **`A.1`** (los 17 marcados con ★ dentro de la tabla de los 40) |
| **Canónica del recuento** | **`4.2.1` callout *Procedencia del «17»***, que documenta que el 17 sale de los valores distintos de la columna `tipo` de `metricas_hibrido_0day.csv` y que su `n` suma 3.750 |
| **Verificación literal** | Los dos pasajes traen la **misma secuencia de 17 nombres**: `4.2.1` «`apache2`, `httptunnel`, `mailbomb`, `mscan`, `named`, `processtable`, `ps`, `saint`, `sendmail`, `snmpgetattack`, `snmpguess`, `sqlattack`, `udpstorm`, `worm`, `xlock`, `xsnoop` y `xterm`»; `4.3.6` la repite carácter por carácter |

> **Frase a insertar en `4.3.6`, propiedad 1, sustituyendo a la lista:**
>
> «De los 12.833 ataques de D2, **3.750 (el 29,2 %) pertenecen a 17 tipos ausentes de D3**,
> **enumerados uno a uno en el [[A.1 Columnas del dataset NSL-KDD|Apéndice A.1]]** y con su recuento
> acreditado en [[4.2 Base de datos utilizada|4.2]] (§4.2.1). Es una característica de diseño de
> NSL-KDD que este trabajo explota deliberadamente: esos 17 tipos hacen de banco de pruebas de
> detección 0-day. **La lista no se repite aquí.**»

### D5 · La composición de D3 por categoría — **recortar el callout de `4.2.1`**

| | |
|---|---|
| **Acción** | El callout *Procedencia del 78,3 % de DoS en D3* de `4.2.1` reproduce el desglose completo en prosa **y** después explica el artefacto. Conservar la explicación del artefacto —que es su función— y quitar el desglose |
| **Canónica** | **`4.3.6`**, propiedad 2, tabla de cuatro filas. Es donde el pipeline la produce |
| **Verificación literal** | `4.2.1`: «`dos` **45.927** · `probe` **11.656** · `r2l` **995** · `u2r` **52**, que suman los **58.630** ataques de D3». `4.3.6`: tabla con exactamente esas cuatro filas y esos cuatro valores |
| **Salvedad** | La precisión a cuatro decimales (`dos` 78,3336 %, `probe` 19,8806 %, `r2l` 1,6971 %, `u2r` 0,0887 %) y el nombre de las nueve columnas del CSV **solo están en `4.2.1`**. Si se recorta el callout, ese detalle **se mueve a `A.3`**, no se pierde (T7) |

> **Frase a insertar en `4.2.1`, sustituyendo al desglose del callout:**
>
> «El reparto de D3 por categoría —recuento, porcentaje y ratio de desbalance— **se publica en
> [[4.3 Preprocesamiento de los datasets|4.3]] (§4.3.6) y no se reproduce aquí**; de él sale el
> 78,3 % citado. Lo pertinente en este punto es su procedencia: lo emite `validacion.py` en
> `Resultados\specialized_nsl_kdd_composicion_d3.csv` […]»
>
> *(el resto del callout —la advertencia de no confundirlo con los soportes de `metricas_firmas.csv`—
> **se conserva íntegro**: es una vacuna contra un error concreto y no está en ningún otro sitio).*

### D6 · La tabla D1/D2/D3 — **recortar la de `4.2.1`**

| | |
|---|---|
| **Acción** | Suprimir la tabla de `4.2.1` § *Tamaño y reparto de los subconjuntos* y remitir |
| **Canónica** | **`4.3.6`** para contenido y tamaños; **`5.0.1`** para la función de cada partición y los sub-splits `D1_train`/`D1_val` |
| **Por qué la de `4.2.1` es la prescindible** | Es la única de las tres que **no aporta una columna propia**: `4.3.6` añade la función de entrenamiento y `5.0.1` la función exclusiva y los sub-splits; `4.2.1` solo repite contenido + instancias + «54 características», y ese 54 ya lo fija `4.3.5` |

> **Frase a insertar en `4.2.1`:**
>
> «Los tres subconjuntos y sus tamaños se construyen en [[4.3 Preprocesamiento de los datasets|4.3]]
> (§4.3.6) y su función dentro del protocolo de evaluación se declara en
> [[5.0 Protocolo de evaluación|5.0]] (§5.0.1); **no se anticipan aquí**. Lo que este apartado aporta
> es su caracterización empírica, que se desarrolla a continuación.»

### D7 · El callout `delta = (A) − (B)` — **REVERTIDO: NO se recorta**

> [!important] Corrección tras auditoría: la supresión propuesta se retira
> La versión anterior de este informe mandaba suprimir el callout de `5.1.3`. **Se revierte**, por
> coherencia con el propio criterio de §4: el callout **es una vacuna**, y las vacunas se conservan
> **en el punto donde se aplica el error que previenen**, no solo donde nació la cifra. Aquí el error
> a prevenir es leer `delta` como una **descomposición** del KS, y ese error se comete justo al
> interpretar (A) y (B) — que es lo que hace `5.1.3`, no `4.2.1`. Es el mismo argumento con el que §4
> conserva la vacuna `P5`/`P-5` y la del «14 de Tavallaee»; recortar esta y conservar aquellas sería
> aplicar dos criterios distintos al mismo tipo de material. **El coste de mantenerla son unas líneas;
> el coste de quitarla es un error de lectura en el punto exacto donde se induce.**

| | |
|---|---|
| **Acción** | **Ninguna.** El callout se conserva en las dos sedes |
| **Canónica de la cifra** | **`4.2.1`**, que sigue siendo la **fuente numérica única del KS** por decisión del 2026-08-11. La duplicación afecta al **argumento**, no al número: `5.1.3` no fija cifra propia |
| **Verificación literal** | Los dos callouts comparten el argumento palabra por palabra: «el estadístico KS es el **supremo de la diferencia entre dos funciones de distribución acumulada**, y un supremo **no es aditivo sobre una mezcla de poblaciones**». El de `5.1.3` **ya remite** a `4.2.1` en su última frase, de modo que la jerarquía de sedes queda explícita sin necesidad de borrarlo |
| **Único ajuste admisible** | Si se quisiera acortar, **comprimir la redacción de `5.1.3` a una o dos frases** manteniendo el enunciado del supremo y la remisión. **Suprimirlo entero, no** |

### D8 · El FPR por variante (10,2 % / 8,5 %) — **unificar; canónica en `5.1.3`**

| | |
|---|---|
| **Acción** | `5.1.3` conserva la tabla *El exceso, por variante* y la explicación. `5.0.4` conserva **solo la regla de citado** (por variante, nunca como rango), que es protocolo. `4.2.1` recorta su párrafo explicativo a una remisión |
| **Canónica de la explicación** | **`5.1.3`** — es donde se argumenta que la medición (B), y no la (A), es la que puede sostener la atribución |
| **Canónica de la regla** | **`5.0.4`** callout *La misma cifra, dos variantes, dos números* |
| **Salvedad importante** | El párrafo de `4.2.1` que hoy explica el exceso **contiene una pieza que no está en `5.1.3`**: la declaración de qué publica cada capítulo por variante («[[5.3]] discute **solo la variante de 54**… el desglose por detector de la variante de 122 no se publica allí»). **Esa pieza se conserva**; lo que se recorta es la explicación causal, duplicada |

### D9 · Las cuatro transformaciones sin fuga — **recortar `5.0.6` C5**

| | |
|---|---|
| **Acción** | Reducir `5.0.6` § *C5 con detalle* a dos frases: el asiento del criterio y la remisión |
| **Canónica** | **`4.3.7`**, que **ya se autodeclara sede única**: «Este apartado (4.3.7) es la sede única de la verificación punto por punto del preprocesado sin fuga» |
| **Estado real** | `5.0.6` **ya dice** ser «su asiento resumido en la rejilla, no un segundo control independiente» — pero acto seguido **reenumera las cuatro transformaciones con sus puntos de código**. El texto se contradice con su propia declaración |
| **Aviso adicional** | Las cuatro viñetas de `5.0.6` citan `program.py:308-320`, `program.py:332`, `program.py:335-344` y `program.py:516`. **No las cuatro incumplen la norma por igual**: todas llevan una pista textual al lado, pero solo dos nombran la función. Ver §5, discrepancia 1 |

> **Frase a insertar en `5.0.6`, sustituyendo a las cuatro viñetas:**
>
> «Las **cuatro** transformaciones del pipeline que aprenden algo de los datos —codificación
> *one-hot*, escalado, codificación de etiquetas y selección de características— se ajustan
> exclusivamente con datos de entrenamiento y sobre D2 solo se **aplican**. **La verificación punto
> por punto, con el punto de ajuste de cada una y el fragmento de código que lo demuestra, tiene su
> sede única en [[4.3 Preprocesamiento de los datasets#4.3.7 Preprocesado sin fuga de datos|4.3.7]];
> esto es su asiento en la rejilla, no un segundo control.**»

### D10 · Rejillas e hiperparámetros ganadores — **mover a `A.3`; es el caso central de la Decisión 5**

| | |
|---|---|
| **Acción** | En `4.4` y `4.5`, sustituir la tabla *Configuraciones ganadoras* por una frase que diga **qué se buscó y por qué**, con remisión. Las tablas *Algoritmos y espacios de búsqueda* se comprimen a una frase por algoritmo |
| **Canónica** | **`A.3.3` Configuraciones seleccionadas (semilla 42)**, verificado en disco: ya trae las ocho filas de la etapa 1 con su umbral a seis decimales y las ocho de la etapa 2 con su balanceo ganador, **para las dos variantes** |
| **T7** | **El destino ya contiene el material**, y con más precisión que el cuerpo (`A.3.3` da 0,440643 donde `4.4` da 0,4406, y cubre la variante de 122 que el cuerpo no publica). El recorte **no pierde nada** |
| **Excepción que se queda** | El **umbral p95** permanece en el cuerpo (Decisión 5): es el criterio, no un hiperparámetro. También permanecen las **tres particularidades de implementación** de `4.4` —submuestra de 20.000 filas del OneClassSVM, `novelty=True` del LOF, autoencoder como `MLPRegressor`—, que son argumentos y no valores de rejilla |
| **Qué NO se recorta de `4.5`** | Todo el § *Extracción de firmas legibles* y las cuatro reglas comentadas: es contenido único y el cumplimiento del requisito de interpretabilidad |

> **Frase a insertar en `4.4`, sustituyendo a la tabla de configuraciones ganadoras:**
>
> «La selección por AUC-ROC de validación resuelve una configuración por algoritmo, y de esa
> comparación salen dos hechos que sí importan aquí: **IsolationForest y el autoencoder parten como
> los candidatos más fuertes**, con OneClassSVM por detrás y LOF como el más débil, y **los umbrales
> no son comparables entre algoritmos** porque cada *score* vive en su propia escala —lo comparable
> es el criterio con el que se fijan, el percentil 95 sobre `D1_val`—. **Las configuraciones
> ganadoras de cada algoritmo, con su umbral y para las dos variantes de características, están
> tabuladas en el [[A.3 Ficha del sistema|Apéndice A.3]] (§A.3.3) y no se reproducen aquí.**»

> **Frase a insertar en `4.5`, sustituyendo a la tabla de configuraciones ganadoras:**
>
> «En validación cruzada los cuatro algoritmos superan 0,94, con RandomForest en cabeza; la
> generalización real a D2, donde estas cifras se degradan de forma desigual, se analiza en
> [[5.2 Resultados del modelo de detección basado en firmas|5.2]]. **La configuración ganadora de
> cada algoritmo y su esquema de balanceo están tabulados en el [[A.3 Ficha del sistema|Apéndice
> A.3]] (§A.3.3).**»

> [!warning] Cautela: un párrafo de `4.5` depende de los valores que se recortan
> El párrafo que empieza «Los valores de f1_macro en CV no son uniformemente distintos de los de la
> tabla de 4.3.4» **argumenta sobre las configuraciones concretas** (`n_neighbors=5` coincide con el
> defecto; `max_iter=300` frente a `max_iter=100`). Ahí **el número ES el argumento**, exactamente el
> supuesto de la excepción de la Decisión 5: ese párrafo **se conserva con sus valores**, aunque la
> tabla se vaya. Recortarlo lo dejaría sin sentido.

### D11 · SMOTE dentro del *fold* — **recortar a remisión en cuatro de las cinco sedes**

| | |
|---|---|
| **Acción** | Conservar el desarrollo íntegro en `4.3.4`. En `4.5`, `4.6`, `5.2.3` y `6.1.1` dejar la mención sin reexplicar el argumento |
| **Canónica** | **`4.3.4`**, párrafo *Un detalle metodológico es crítico* + bloque `_envolver_balanceo` |
| **Nota** | El informe del capítulo 3 sitúa además el **fundamento** del argumento en `2.1.6.5`. Este barrido **no ha abierto el capítulo 2**, de modo que la relación entre `2.1.6.5` y `4.3.4` queda fuera de su alcance y no se decide aquí |

### D12 · El eje de balanceo no constante — **recortar `5.4` casi entero**

| | |
|---|---|
| **Acción** | Reducir `5.4` § *Una decisión de preprocesado que se declara no establecida* a un párrafo: el hallazgo, su acotación en una línea y la remisión |
| **Canónica** | **`5.2.4.4`**, que trae las tres tablas, los cuatro márgenes, el reparto 17/40 y 40/40 y el callout *Qué se concluye y qué NO* |
| **Volumen** | Es, con `5.4` § *Sobre el sistema híbrido* (D17), **el recorte más rentable del capítulo 5**: la sección de `5.4` reproduce las tres precisiones de `5.2.4.4` **y además** una tabla de dos filas cuya única función es describir qué contiene `5.2` |
| **Verificación literal** | `5.2.4.4`: «el barrido **no descubre que la decisión de `4.3.4` estuviera mal: confirma que ese eje nunca estuvo establecido**». `5.4`: «el hallazgo no descubre que la decisión estuviera mal: **confirma que ese eje nunca estuvo establecido**» |

> **Párrafo que sustituye a la sección completa de `5.4`:**
>
> «El barrido de diez semillas obliga a matizar una decisión del capítulo 4: la elección de
> estrategia de balanceo de [[4.3 Preprocesamiento de los datasets|4.3.4]] **no es constante entre
> semillas** y así se declara, sin reabrir el experimento ni mover ninguna cifra publicada. La
> acotación es imprescindible: **afecta solo al eje SMOTE frente a `class_weight`** —el que aplica a
> DecisionTree y RandomForest—, mientras que **el eje SMOTE frente a no balancear sí está
> establecido**, con SMOTE ganando en las cuarenta celdas del barrido. **El desarrollo, con los
> márgenes celda a celda y los dos recuentos pareados, está en
> [[5.2 Resultados del modelo de detección basado en firmas|5.2]] (§5.2.4.4) y no se repite aquí.**»

### D13 · La banda de semillas de RandomForest — **unificar; canónica en `5.2.4`**

| | |
|---|---|
| **Acción** | El reparto de sedes **ya está declarado y es correcto** —`5.2.4` publica las bandas, `A.3` el volcado semilla a semilla—, y `5.4` lo repite explícitamente. Lo que sobra es que `5.4` **cite la banda dos veces** (en § *Etapa 2* y en el caveat 2) y que `5.2.3`, `5.2.4.1` y `5.2.4.2` enuncien tres veces el «8 de 10» |
| **Canónica** | **`5.2.4.1`** para el par banda/pareada; **`5.2.4.2`** para la lectura del titular |
| **Acción concreta** | En `5.4`, dejar la banda **una sola vez** (en § *Etapa 2 (firmas)*) y en el caveat 2 escribir solo «0,8223 (véase la banda en §5.2.4)». En `5.2.3`, el callout ya remite a `§5.2.4`: basta con quitar la repetición del recuento automatizado, que `5.2.4.1` da con más detalle |
| **Excepción de la Decisión 5** | **La semilla 42 se queda nombrada en todo `5.2`**: `5.2.4` la compara contra la banda, luego ahí el número **es** el argumento |

### D14 · El 13,4 % y el matiz P-5 — **unificar; canónica en `5.3`**

| | |
|---|---|
| **Acción** | Conservar íntegro `5.3` § *El enrutado a `unknown`: el 13,4 %, explicado*. Recortar: (a) la repetición **dentro del propio `5.3`**, al cierre del § 0-day; (b) el segundo hallazgo de `5.4`, que reproduce el matiz P-5 y los 2.504; (c) el callout de procedencia de `6.2.2`, que reproduce la fuente ya dada en `5.3` |
| **Canónica** | **`5.3`** § *El enrutado a `unknown`* |
| **Qué conserva cada sede** | `6.1.4` límite 5 conserva **la lectura teórica** (Scheirer, riesgo de espacio abierto), que es contenido propio y no duplicado. `6.2.2` conserva **la propuesta** (OpenMax), que tampoco lo es |
| **Verificación literal** | `5.3`: «los **2.504** 0-day que no llegan a `unknown` siguen estando alarmados». `5.4`: «los **2.504 0-day restantes siguen estando alarmados**, solo que con la categoría equivocada» |

> **Frase a insertar en `5.4`, sustituyendo al segundo hallazgo:**
>
> «**El RandomForest está sobre-confiado ante lo desconocido**: de los 0-day que la etapa 1 detecta,
> solo una fracción pequeña se enruta a `unknown`. **La cifra, su lectura correcta —no es una tasa
> de detección fallida, porque por la decisión P-5 el resto sigue alarmado— y su explicación teórica
> están en [[5.3 Resultados del sistema híbrido|5.3]]; aquí solo se retiene la consecuencia:**
> superarlo exige **reconocimiento de conjunto abierto** en lugar de un umbral sobre `predict_proba`.»

> **Frase a insertar en `6.2.2`, sustituyendo al callout *Procedencia de la cifra del 13,4 %*:**
>
> «La cifra, su procedencia en `Resultados/metricas_hibrido_calibracion.csv` y su alcance —las
> columnas `d2_` **solo se reportan y nunca deciden**— están en
> [[5.3 Resultados del sistema híbrido|5.3]].»

### D15 · Complementariedad de los detectores — **unificar; canónica en `5.3`**

| | |
|---|---|
| **Acción** | Recortar el primer hallazgo de `5.4` a una línea. `6.2.1` **conserva su tabla de dos filas**: ahí las cuatro cifras son la premisa de la línea futura y sin ellas el apartado no se sostiene |
| **Canónica** | **`5.3`** hallazgo 1, que se apoya en la tabla completa de 17 tipos × 4 detectores |
| **Verificación literal** | Las mismas cuatro cifras en las tres sedes: `mailbomb` 0,000 / 0,823 y `snmpguess` 0,018 / 0,740 |

### D16 · `snmpgetattack` — **unificar; dos canónicas complementarias**

| | |
|---|---|
| **Acción** | Recortar el tercer hallazgo de `5.4` y la última viñeta de `6.1.3` a una línea con remisión |
| **Canónica de la medición** | **`5.3`** hallazgo 2 |
| **Canónica del razonamiento** | **`6.2.6` peldaño 3**, que es el único sitio donde el argumento se desarrolla en tres pasos (los cuatro detectores son de familias distintas → lo común es la representación → el límite es del dataset) |
| **Salvedad** | No es la misma afirmación en los dos sitios: `5.3` **mide**, `6.2.6` **deriva de ahí una propuesta**. Es relación medición/consecuencia, no duplicación — lo duplicado son las paráfrasis de `5.4` y `6.1.3` |

### D17 · El contraste con el baseline — **recortar `5.4` y `6.1.2`**

| | |
|---|---|
| **Acción** | Conservar íntegro `5.3` § *Comparación con el baseline RF monolítico*. `5.4` reduce sus tres viñetas a dos frases sin repetir cifras. `6.1.2` conserva la afirmación de tesis y **una sola** pareja de cifras (0.771 / 0.150) |
| **Canónica** | **`5.3`**, donde están la tabla, las dos matrices de confusión y el análisis de forma del error |
| **Verificación literal** | Las tres sedes repiten el mismo bloque: recall 0-day «0.771 frente a 0.150», «≈ 5×», «f1_macro se desploma de 0.909… a 0.472», «recall `r2l` = 0.004, `u2r` = 0.010» y la frase del «~99 % de accuracy» que «no sobrevive al test oficial del NSL-KDD» |
| **Por qué no es repetición legítima de cierre** | `5.4` y `6.1.2` no **recapitulan**, **reproducen**: traen los mismos cinco pares de cifras con la misma redacción. Un cierre de capítulo legítimo enuncia el hallazgo; estos lo vuelven a demostrar |

> **Frase a insertar en `6.1.2`:**
>
> «Frente a un RandomForest monolítico entrenado sobre todo el tráfico, el sistema híbrido multiplica
> por aproximadamente **cinco** la detección de ataques 0-day (recall global 0.771 frente a 0.150), y
> el desglose por tipo muestra que la diferencia no es solo de sensibilidad: el baseline es
> *estructuralmente* incapaz de ver la mayoría de los tipos nunca vistos. **La comparación completa
> —tabla de métricas, matrices de confusión y análisis de la forma del error— está en
> [[5.3 Resultados del sistema híbrido|5.3]] y no se reproduce aquí.**»

### D18 · El coste de la cascada (0,822 → 0,748) — **unificar dentro de `5.3` y recortar `5.4`**

| | |
|---|---|
| **Acción** | `5.3` lo dice dos veces —en la viñeta *El coste del filtro* y en el párrafo de cierre—: dejar solo la viñeta. `5.4` caveat 2 remite |
| **Canónica** | **`5.3`** viñeta *El coste del filtro* |
| **Nota** | La variante de `4.6` (0.822 con 54 frente a 0.696 con 122) **es otra cosa**: compara variantes de características, no etapas. **No se toca** |

---

## 3. Volumen implicado

> [!check] Bases CONTADAS con `wc -w` — 2026-08-18, en el cierre de la Tanda B
> El agente que escribió este informe **no disponía de shell** y, correctamente, **se negó a
> estimar**: es el error que el proyecto ya cometió dos veces —la base del capítulo 3 estimada en
> ≈4.330 palabras cuando eran **6.670** (corta un ~54 %), y el desglose reportado de la Tanda A, que
> sumaba ~11.000 cuando el total real era **13.125**—. **El conteo se ejecutó en el hilo principal al
> cerrar la tanda** y estas son las bases reales, no estimaciones:
>
> | Nota | Palabras | | Nota | Palabras |
> |---|---:|---|---|---:|
> | `4.1` Tecnologías | 706 | | `5.0` Protocolo | 4.903 |
> | `4.2` Base de datos | 5.334 | | `5.1` Anomalías | 2.884 |
> | `4.3` Preprocesamiento | 5.712 | | `5.2` Firmas | 4.188 |
> | `4.4` Entren. anomalías | 2.060 | | `5.3` Híbrido | 3.536 |
> | `4.5` Entren. firmas | 1.580 | | `5.4` Conclusiones cap. 5 | 4.594 |
> | `4.6` Conclusiones cap. 4 | 1.054 | | `6.1` Conclusiones | 4.860 |
> | **Capítulo 4** | **16.446** | | `6.2` Líneas futuras | 3.640 |
> | | | | **Capítulo 5** | **20.105** |
> | | | | **Capítulo 6** | **8.500** |
>
> **Conjunto 4-6: 45.051 palabras.** `A.3 Ficha del sistema`, destino de lo que sale del cuerpo por
> la restricción T7, está hoy en **15.127**.
>
> **Corrección de una cifra que circulaba:** el encargo de este barrido hablaba de «~52.000 palabras»
> para los capítulos 4-6. **Son 45.051** — la cifra de partida venía inflada un ~15 % y no procedía
> de un conteo. Mismo patrón que este informe denunciaba: se corrige en su origen.
>
> **Lo que sigue sin publicarse, y con razón: los PORCENTAJES de encogimiento.** Las bases ya están,
> pero el volumen de cada pasaje recortado solo se conoce al aplicarlo. **El porcentaje se calcula
> recontando DESPUÉS del recorte**, contra estas bases, nunca antes y nunca a ojo.

**Lo que sí se puede afirmar sin contar**, porque depende de la estructura y no del volumen:

> [!warning] Esta tabla se corrigió tras la auditoría — léase la columna «recorte real»
> La versión anterior asignaba **D4** a `4.2` y **omitía la fila `4.3`**. Es un error con consecuencia
> práctica: el recorte de D4 vive en **`4.3.6`** (§2, D4: «Frase a insertar en `4.3.6`, propiedad 1»),
> mientras que **`4.2.1` conserva su callout íntegro** porque es justo lo que acredita el recuento de
> los 17. Un ejecutor que leyera la tabla vieja habría recortado la sede equivocada.

| Bloque | Solapes que lo afectan | Recorte real que le toca |
|---|---|---|
| `4.2` | D5, D6, D7, D8 | Recorte por supresión de **una tabla** (D6) y del **desglose** de un callout (D5), más un párrafo a remisión (D8). **`4.2.1` NO pierde**: el callout de procedencia del «17» (D4, sede acreditativa), el resto del callout de D5 ni el callout de D7 |
| `4.3` | D4, D5, D6, D9, D11 | **Sede canónica de cuatro solapes** (D5, D6, D9 en `4.3.7`, D11 en `4.3.4`): casi todo se queda. Recorte propio: **la lista de 17 nombres de `4.3.6`, propiedad 1** (D4) y la re-enumeración de D3 en `4.3.7` |
| `4.4` | D1, D2, D10 | **El más afectado del capítulo 4**: un callout largo entero (D2), dos tablas (D10) y una remisión (D1). **D3 no le aplica: ya cumple** |
| `4.5` | D10, D11 | Una tabla y una remisión; el bloque de firmas legibles no se toca. **D3 no le aplica: ya cumple** |
| `4.6` | D3, D9, D11, D18 | Recorte por remisión en cuatro puntos, ninguno estructural: es cierre de capítulo y su función recapituladora se conserva (§4) |
| `5.0` | D3, D8, D9 | Recorte acotado: `5.0` es protocolo y la mayoría de su contenido es canónico |
| `5.1` | D1, D7, D8 | Recorte de **un** callout (D1). **D7 se revierte** y `5.1.3` es **canónica** de D8: el neto es casi nulo |
| `5.2` | D3, D13 | Recorte pequeño: `5.2.4` es sede canónica de casi todo lo que contiene |
| `5.3` | D14, D15, D16, D17, D18 | **Canónica de cinco solapes**: casi no se recorta. Solo dos repeticiones **internas** (D14b y D18a) |
| `5.4` | D3, D12, D13, D14, D15, D16, D17, D18 | **El más afectado de toda la memoria**: ocho solapes, y en cinco de ellos reproduce cifras en lugar de recapitular |
| `6.1` | D3, D14, D16, D17 | Recorte en `6.1.2` y `6.1.3`; `6.1.4` es contenido propio |
| `6.2` | D14, D15 | Recorte mínimo: un callout de procedencia |

---

## 4. Solapes que NO son duplicación: repetición legítima

Estos casos aparecen dos o más veces y **deben seguir apareciendo**. Recortarlos empeoraría la
memoria.

| Caso | Dónde se repite | Por qué es legítimo |
|---|---|---|
| **Los tres callouts `> [!warning] Verificación pendiente — sin acceso al texto completo`** | `4.3.7`, `5.0.6`, `6.1.4` | **Los exige la regla permanente del 2026-08-14** (Decisión 4 de la Fase 0): el marcador tiene que estar **en la nota**, junto a la cita, porque Francisco revisa el informe y no el registro. Tocarlos rompería la decisión |
| **El FPR siempre al lado del recall (P-2)** | `5.0.3` métrica 1, `5.0.4` prohibición 2, `5.3` tabla 0-day, `5.4` caveat 1, `6.1.3` | No es repetición de una afirmación sino **aplicación repetida de una regla**. Cada aparición conjunta es el cumplimiento de la norma que el propio protocolo impone |
| **La rejilla C1-C7** | `5.0.6` (sede única declarada) y `5.4` § *Los criterios de admisión* | **Ya está bien resuelto**: `5.4` remite explícitamente («no se repiten aquí») en lugar de redefinir. Es el patrón a imitar en los demás casos |
| **La cifra 0,822** | `4.6`, `5.2.2`, `5.2.3`, `5.2.4`, `5.3`, `5.4` | Cifra **titular**: aparece donde se produce, donde se compara con la cascada y donde se declara el criterio con que se eligió el modelo. Repetir un titular no es duplicar contenido — **siempre que vaya con su banda**, como exige `5.2.4.2` |
| **`4.6` y `5.4` como cierres de capítulo** | Frente a `4.3`-`4.5` y `5.1`-`5.3` | Es un **género cuya función es recapitular**. Lo que este informe marca en ellos (D12, D17) **no es la recapitulación sino la reproducción de cifras y argumentos completos**; el cierre se conserva, lo que se retira es la segunda demostración |
| **Las dos nomenclaturas `P5` / `P-5`** | `5.0.4` callout homónimo | Vacuna contra una confusión real, en su primera aparición conjunta. Única sede. **No tocar** |
| **El callout `delta = (A) − (B)` es comparación, no descomposición (D7)** | `4.2.1` y `5.1.3` | **Vacuna aplicada en el punto donde se induce el error**: quien lee la interpretación de (A) y (B) en `5.1.3` es exactamente quien puede restarlas creyendo que descompone. `5.1.3` **no fija cifra propia** y ya remite a `4.2.1`, de modo que la jerarquía de sedes queda intacta. Mismo criterio que las dos filas siguientes. **No tocar** |
| **La vacuna «el 14 de Tavallaee es de KDD'99»** | `4.2.1` | Única sede, y previene un «arreglo» equivocado del 17. **No tocar** |
| **Las cuatro reglas comentadas del árbol** | `4.5` § *Extracción de firmas legibles* | Contenido único y cumplimiento del requisito de interpretabilidad. **No tocar** |
| **`5.3` § *Evaluación binaria* coincide con `5.1`** | Declarado como H-5 | **La coincidencia es el resultado**: se publica precisamente para dejar constancia de la equivalencia estructural. Recortarla borraría un hallazgo |

---

## 5. Discrepancias detectadas — se reportan, no se corrigen

> [!warning] Ninguna de estas entra en el recorte
> El encargo es recortar duplicación, no arbitrar defectos. Se registran para que se despachen por
> separado.

1. **`5.0.6` § C5 cita el código por `fichero:línea`, pero solo DOS de sus cuatro viñetas quedan sin
   ancla textual suficiente.** *(Matizado tras la auditoría: la versión anterior declaraba las cuatro
   contra la norma, y no es exacto.)* La norma de `CLAUDE.md` admite el `fichero:línea` **como pista
   auxiliar junto al título**; lo que prohíbe es que sea la **única** referencia. Verificado literal:

   | Viñeta | Referencia | Estado |
   |---|---|---|
   | Codificación *one-hot* | `program.py:308-320`, **paso 2 de `preprocess_specialized_splits`** | **Cumple**: la línea es auxiliar y la función está nombrada |
   | Selección de características | `program.py:516`, **dentro de `select_features`** | **Cumple**, por lo mismo |
   | Escalado | `program.py:332`, **«paso 3»** | **Insuficiente**: «paso 3» no dice de qué función, así que la línea acaba siendo el único localizador operativo |
   | Codificación de etiquetas | `program.py:335-344`, **«paso 4»** | **Insuficiente**, por lo mismo |

   Arreglo mecánico: completar las dos últimas a «paso 3 / paso 4 de `preprocess_specialized_splits`»,
   que es como ya lo escribe `4.3.7` («`program.py`, paso 2 de `preprocess_specialized_splits`»,
   «`program.py::select_features`»). **Si D9 se ejecuta, el problema desaparece con el recorte**;
   si no, hay que corregirlo aparte. Mismo defecto —y ahí sí, **sin ancla textual alguna**— en `5.2.4.4`
   (`firmas.py:40`, `firmas.py:146`, `firmas.py:103-108`), en `4.6` (`anomalias.py:18-22`,
   `firmas.py:23-25`, `hibrido.py:19-23`), en `5.1.4` (`anomalias.py:18-22`) y en `A.3.3`
   (`firmas.py:100-108`) — **seis notas en total**.

2. **El recuento «diez remisiones» de `4.3.5` no coincide con el recuento de sedes de este informe.**
   `4.3.5` enumera diez sedes que remiten a ella y declara «son **once** sedes en total contando
   esta». El barrido de §1 (D3) localiza **once sedes** que enuncian la desviación en los capítulos
   4-6 más `A.3`, pero la lista de `4.3.5` **no incluye `4.4` ni `4.5`**, que sí **mencionan** la
   desviación («es una de las **tres** decisiones tomadas sobre D2, y el inventario completo está en
   las limitaciones de 6.1»). **Matiz importante tras la auditoría:** esas dos **no enumeran** (§2,
   D3), así que **no son sedes a recortar**; pero sí son sedes que remiten, y por eso deberían
   figurar en una lista que se declara exhaustiva. **La corrección es de recuento, no de redacción**:
   añadirlas a la lista de `4.3.5` (diez remisiones enumeradas, «once contando esta») y pasar el
   total declarado de once a **trece** —doce remisiones más ella—, o bien reformular esa lista como
   «sedes que enuncian», que son otras. **Si se ejecuta D3, el recuento de `4.3.5` hay que rehacerlo
   en el mismo pase**; dejarlo sin tocar produciría una lista que se declara exhaustiva y no lo es.

3. **Los punteros al inventario siguen contradiciéndose, y el capítulo 3 no cierra el problema.** Es
   la discrepancia 1 del informe del capítulo 3, que allí se declaró «fuera del alcance de T9».
   Verificado hoy en los capítulos 4-6: `4.4` y `4.5` mandan a `6.1`; `4.6` manda a `6.1`; `5.0.4`
   manda a `6.1` **y declara `6.1` sede canónica**; `4.3.5` se declara **sede canónica** de otra cosa
   (alcance y cifras); `6.1.3` se declara **versión de referencia** del inventario. Hoy el reparto es
   coherente —`4.3.5` fija cifras, `6.1.3` fija el inventario— **pero solo si se lee entero**: no hay
   ninguna nota que declare ese reparto de dos canónicas en una sola frase. **Despacho sugerido:**
   una línea en `4.3.5` y otra en `6.1.3` que digan explícitamente «esta sede fija X; la otra fija Y».

4. **`5.4` cita el pitfall «P9» sin haberlo definido en el capítulo 5.** En su callout *La cifra de
   flujos por segundo es un techo de inferencia* escribe «la evaluación *solo-laboratorio* (**P9**)
   que este capítulo declara vigilar». El capítulo 5 **no define P9 en ningún punto**: quien lo define
   es `6.1.4`, posterior. Y `5.0.4` advierte expresamente de que en el capítulo 5 «solo se usa la
   serie **sin guion**», con `P5` como único ejemplo. **No es duplicación, es una referencia
   adelantada sin antecedente**; se reporta para que se despache con el recorte o aparte.

---

## 6. Orden recomendado de ejecución

Las remisiones no son independientes. Este orden evita rehacer trabajo:

1. **`5.3` primero.** No se recorta apenas (solo D14b y D18a, ambos internos), pero **es la canónica
   de cinco solapes** —D14, D15, D16, D17, D18— y hay que dejarla fijada antes de recortar contra
   ella.
2. **`5.2.4` después.** Igual: canónica de D12 y D13, con recorte propio mínimo.
3. **`5.4`**, que es donde está el grueso del trabajo (ocho solapes). Al hacerlo, releerla entera:
   tras los recortes de D12, D17 y D18 la sección cambia de proporciones y sus transiciones dejan de
   encajar.
4. **`4.3.6` y `4.2.1`** (D4, D5, D6): el orden importa, porque `4.2.1` remite a `4.3.6` y no al
   revés. Fijar antes `4.3.6`. **El recorte de D4 se hace en `4.3.6`, no en `4.2.1`**, cuyo callout de
   procedencia del «17» se conserva íntegro (§3).
5. **`4.4` y `4.5`** (D1, D2, D10). Antes de tocar `4.4`, **trasladar a `A.3.6` el análisis del
   residual como fracción del bloque**, que es lo único de ese callout que `A.3` no tiene (T7).
6. **`5.0` y `5.1`** (D1, D8, D9): recortes acotados, dependientes de que `4.3.7` y `4.2.1` estén ya
   cerrados.
7. **D3 en un pase propio y al final**, sobre las **cinco** sedes que reenumeran (`4.3.7`, `4.6`,
   `5.0.4`, `5.4`, `A.3.7`) más los dos párrafos de `5.1.4` y `5.2.3`, a la vez. **`4.4` y `4.5` no
   entran en el pase: ya cumplen** (§2, D3). Es el único solape que toca
   los tres capítulos, y hacerlo por partes dejaría redacciones divergentes de una formulación que
   está **cerrada y no se parafrasea**. En ese mismo pase, rehacer el recuento de remisiones de
   `4.3.5` (§5, discrepancia 2).
8. **`6.1` y `6.2` al final** (D3, D14, D15, D16, D17): son los que más remiten hacia atrás, de modo
   que conviene que sus destinos ya estén en su forma definitiva.

> [!caution] Dos cosas que NO se tocan en este recorte
> - **`A.3` la está editando otro agente en paralelo** (ejecución del capítulo 3). Todo lo que este
>   informe manda a `A.3` —el residual de D2, la precisión decimal de D5— **debe esperar a que ese
>   trabajo cierre**, y despacharse como pase propio.
> - **El capítulo 2 no se ha barrido aquí.** Los solapes 2↔4, 2↔5 y 2↔6 quedan **sin diagnosticar**.
>   El precedente del capítulo 3 dice que ahí hay material (`2.1.6.5` duplicaba el escalador y el
>   SMOTE por *fold*, ambos con sede en `4.3`), de modo que **es previsible que D9 y D11 tengan una
>   sede más en `2.1.6`** que este informe no ha visto.

---

## Fuentes de este informe

Todas las afirmaciones proceden de la lectura directa de las notas del vault, con la sede citada por
título en §1. No se ha consultado bibliografía externa y **no se introduce ninguna cita nueva**: este
informe no consume ningún número del contador global de `Bibliografía.md`.

Además de las trece notas de los capítulos 4-6, se han consultado:

- `Obsidian_TFG_Vault/Apéndices/A.3 Ficha del sistema.md` — §A.3.3, §A.3.4 y §A.3.6, para verificar
  que el material que D2 y D10 mandan fuera del cuerpo **ya está en el destino**.
- `Obsidian_TFG_Vault/99 Investigación/Datos repetidos en el capítulo 3.md` — plantilla de formato y
  origen de las discrepancias 1 y 3 de §5.
- `resumen-de-decisiones.md`, sección «Decisiones del 2026-08-18 — `grill-me` del Grupo IV» —
  criterios T7 y de hiperparámetros, y la nota de método sobre conteos frente a estimaciones.
- `mis-apuntes-del-informe.md` — contrastado punto por punto contra disco. **De sus puntos, solo la
  cita del profesor (última entrada) sigue viva para este encargo**; los puntos sobre resumen,
  abstract, título y bloque de IA están **cerrados** (Tanda 28 y Decisión 2 del Grupo IV) y no se han
  tomado como pendientes.
