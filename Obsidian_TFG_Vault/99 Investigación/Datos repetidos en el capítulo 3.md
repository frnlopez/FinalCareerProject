---
titulo: "Datos repetidos en el capítulo 3 — diagnóstico previo al recorte"
tipo: informe de investigación interna
fecha: 2026-08-15
revision: pase correctivo del 2026-08-15 tras auditoría (APTO CON CAMBIOS) — 8 correcciones aplicadas · corrección de medida del 2026-08-18 — base del capítulo 3 contada (6.670 palabras, no ≈4.330) y titulares recalculados
estado: cerrado
alcance: diagnóstico. NO aplica cambios
---

# Datos repetidos en el capítulo 3

> [!warning] Este informe no es memoria
> Vive en `99 Investigación/` como insumo de la tarea de recorte (T9). **No se enlaza desde
> `00 Índice TFG.md`** y su prosa no se vuelca a ningún capítulo. Ninguna cifra publicada se ha
> movido ni reescrito al elaborarlo: donde se detecta una discrepancia entre notas, se **reporta**
> (§5) y no se corrige.

**Encargo.** El profesor pide recortar y unificar «los primeros apartados del capítulo 3». Este
documento localiza, contra disco, qué material del capítulo 3 ya está dicho en los capítulos 2, 4,
5 o 6; propone para cada caso recortar / unificar / remitir con la frase de remisión ya redactada;
estima el encogimiento resultante; y separa lo que **no** debe recortarse porque su repetición es
funcional.

**Verificación.** Alcance real de la lectura, declarado con exactitud porque de él depende que se
pueda confiar en las afirmaciones del tipo «único sitio donde aparece»:

| Nivel de lectura | Notas |
|---|---|
| **Leídas íntegras** | `3.1`, `3.2`, `3.3`, `3.4`, `3.5`, `3.6`, `4.3`, `4.4`, `4.5`, `4.6`, `5.0` |
| **Leídas por búsqueda dirigida** (solo los pasajes citados y su contexto inmediato) | `5.1`, `5.2`, `5.3`, `5.4`, `6.1`, `2.1.6`, `2.2.4`, `A.3`, `4.2`, `A.1` |
| **No abiertas** | `4.1`, el resto de `02 Marco Teórico` fuera de `2.1.6` y `2.2.4`, y el resto de apéndices fuera de `A.1` y `A.3` |

Todas las líneas citadas en §1 se han localizado en el fichero indicado.

> [!warning] Consecuencia para T9 — las afirmaciones de exclusividad son acotadas
> Un «único sitio donde aparece» de este informe significa **«único sitio entre las notas leídas»**,
> no una garantía sobre todo el vault. En la primera versión de este documento tres hallazgos
> (S4, S2 y S7) fallaron exactamente por ahí: la enumeración de los 17 tipos 0-day estaba en `A.1`,
> y el capítulo 2 duplicaba el escalador y el SMOTE por *fold* en `2.1.6.5`. Corregido tras el pase
> del `auditor-ml` del 2026-08-15. Antes de ejecutar un borrado por «no está en ningún otro sitio»,
> conviene un `grep` sobre el vault completo.

El barrido inicial del hilo principal se confirma en lo sustancial, **con tres correcciones y cuatro
solapes que le faltaban**, detallados en §1.1.

---

## 1. Tabla de solapes verificados contra disco

Leyenda de la columna **Veces**: número de emplazamientos **distintos** en los que la afirmación
aparece desarrollada (no simples menciones de paso ni wikilinks). Un emplazamiento es **un pasaje**,
no un fichero: dos apartados de la misma nota cuentan dos veces, y por eso el recuento puede superar
al número de ficheros listados (S4 es el caso extremo: 10 pasajes en 6 ficheros). El recuento se
obtiene contando las referencias de la propia celda, de modo que es verificable a simple vista.

| # | Qué se afirma | Dónde aparece (fichero · línea) | Veces |
|---|---|---|---:|
| **S1** | **Inventario de las tres decisiones tomadas mirando D2** (H-2 detector, H-3 clasificador, Q1/C set de características) y su calificación como *data snooping* | `2.1.6 Metodologías y buenas prácticas.md:76-90` (tabla completa) · `3.3 Metodología…:42` · `4.3 Preprocesamiento…:216-217` (callout) · `4.6 Conclusiones del capítulo.md:28-35` (callout, lista de 3) · `5.0 Protocolo de evaluación.md:99` · `5.1 Resultados…anomalías.md:74, 77-80` · `5.2 Resultados…firmas.md:61-64` · `5.4 Conclusiones del capítulo.md:32` · `6.1 Conclusiones.md:35-40` · `A.3 Ficha del sistema.md:96-99, 574-586` | **10** |
| **S2** | **Dónde se ajusta el escalador** (`MinMaxScaler` sobre D1+D3, D2 se transforma sin reajustar; razón anti-*leakage*: en despliegue no se conocen los mínimos/máximos futuros) | `2.1.6 Metodologías…:132-140` (§2.1.6.5, tabla «Formas de fuga», fila 2 + párrafo **(2)**) · `3.3 Metodología…:23-28` (§3.3.2) · `4.3 Preprocesamiento…:45-64` (§4.3.2, con código) · `4.6 Conclusiones…:20` · `5.0 Protocolo…:145` (C5) | **5** |
| **S3** | **Diseño y contenido de D1 / D2 / D3** en tabla de tres filas | `3.3 Metodología…:13-19` (§3.3.1, tabla) · `4.3 Preprocesamiento…:224-232` (§4.3.6, tabla **con tamaños**) · `5.0 Protocolo…:20-28` (§5.0.1, tabla **con función exclusiva y sub-splits**) | **3** |
| **S4** | **Los 17 tipos de ataque ausentes del entrenamiento habilitan la medición 0-day** | `3.3 Metodología…:21` · `3.1 Requisitos…:22` · `4.2 Base de datos utilizada.md:26, 47, 73` · `4.3 Preprocesamiento…:23, 238` · `5.0 Protocolo…:36, 43` · `A.1 Columnas del dataset NSL-KDD.md:99-107` (enumeración uno a uno, marcada con ★) | **10** (en 6 ficheros) |
| **S5** | **Algoritmos candidatos de la etapa 1**, en tabla de cuatro filas | `3.4 Modelo de detección de anomalías.md:19-30` (§3.4.2, tabla «noción de anomalía / motivo») · `4.4 Entrenamiento…anomalías.md:9, 39-50` (tabla de rejillas + particularidades) · `5.1 Resultados…:9` | **3** |
| **S6** | **Algoritmos candidatos de la etapa 2**, en tabla de cuatro filas | `3.5 Modelo de detección basado en firmas.md:17-26` (§3.5.2) · `4.5 Entrenamiento…firmas.md:9, 21-26` · `5.2 Resultados…:9, 32-37` | **3** |
| **S7** | **Tratamiento del desbalance de D3: SMOTE frente a `class_weight`, decidido por algoritmo**, y el argumento anti-*leakage* de aplicar SMOTE **dentro** de cada *fold* | `2.1.6 Metodologías…:134, 138` (§2.1.6.5, fila 1 y párrafo **(1)**: el argumento SMOTE-dentro-del-*fold*) · `3.5 Modelo…firmas.md:32-34` (§3.5.4) · `4.3 Preprocesamiento…:113-161` (§4.3.4, experimento completo con tabla) · `4.5 Entrenamiento…:16, 32-37` · `4.6 Conclusiones…:21` · `5.2 Resultados…:52` | **6** |
| **S8** | **Justificación del orden de la cascada**: el clasificador de firmas no conoce la clase `normal`, luego el detector debe filtrar antes; de ahí sale la capacidad 0-day y la salida `unknown` | `2.2.4 Detección por firmas frente a…anomalías.md:100-107` (§2.2.4.5, argumento en 4 puntos) · `3.2 Arquitectura del sistema.md:27-33` (§3.2.2 y §3.2.3, mismo argumento en prosa) · `3.6 Conclusiones del capítulo.md:11` · `6.1 Conclusiones.md:26` | **4** |
| **S9** | **El umbral de la etapa 1 es el percentil 95 del score sobre `D1_val`** (mismo criterio para los cuatro algoritmos; ≈5 % de FPR por diseño) | `3.4 Modelo…anomalías.md:36-37` (§3.4.3) · `4.4 Entrenamiento…:18` · `5.0 Protocolo…:26, 57` · `5.1 Resultados…:13` | **4** |
| **S10** | **El umbral nunca se ajusta mirando D2** (enunciado suelto, subconjunto de S1) | `3.4 Modelo…anomalías.md:38` · `3.5 Modelo…firmas.md:40` · `4.4 Entrenamiento…:18` · `4.5 Entrenamiento…:17` · `4.6 Conclusiones…:26` · `5.0 Protocolo…:94, 97` | **6** |
| **S11** | **Criterio de calibración de `UMBRAL_CONF`**: probabilidades *out-of-fold* sobre D3 + regla de presupuesto sobre la caída de recall | `3.5 Modelo…firmas.md:40` (§3.5.5, prosa larga) · `5.0 Protocolo…:58` (τ = 2 pp en la tabla de congelados) · `5.3 Resultados del sistema híbrido.md:48-59` (tabla de sensibilidad y elección) · `5.2 Resultados…:62` | **4** |
| **S12** | **Requisito de alcance: comparar cuatro algoritmos por etapa bajo protocolo idéntico** (mismos splits, semilla 42, mismas métricas) | `3.1 Requisitos…:32` (§3.1.4) · `3.3 Metodología…:42` (§3.3.4, primera frase) · `3.6 Conclusiones…:13` · `4.4 Entrenamiento…:9` · `4.5 Entrenamiento…:9` · `4.6 Conclusiones…:39` | **6** |
| **S13** | **Semilla global `random_state = 42` y reproducibilidad determinista** | `3.1 Requisitos…:26` (§3.1.3) · `3.3 Metodología…:42` · `4.3 Preprocesamiento…:9` · `4.6 Conclusiones…:13` · `5.0 Protocolo…:56` · `A.3` (ficha) | **6** |
| **S14** | **Interpretabilidad de las firmas: reglas legibles del árbol como analogía del IDS clásico** | `3.1 Requisitos…:27` (§3.1.3) · `3.5 Modelo…firmas.md:28-30` (§3.5.3) · `4.5 Entrenamiento…:41-91` (extracción real + 4 reglas comentadas) · `4.6 Conclusiones…:39` | **4** |
| **S15** | **Recorrido de un flujo por la cascada** (preprocesado → etapa 1 → etapa 2 → 6 veredictos) | `3.2 Arquitectura…:13-23` (diagrama Mermaid + prosa) · `3.3 Metodología…:30-38` (§3.3.3, los mismos pasos en lista numerada) | **2** (ambas **dentro** del capítulo 3) |

### 1.1 Correcciones al barrido inicial

| Punto del barrido inicial | Veredicto tras verificar |
|---|---|
| «*Data snooping*: seis sitios (`3.3.4`, `4.3`, `6.1`, `5.1`, `5.2`, `5.0`)» | **Incompleto: son diez.** Faltaban `2.1.6:76-90` (que es la versión **más extensa**, con tabla de tres filas), `4.6:28-35`, `5.4:32` y `A.3:574-586` |
| «`3.3.2` duplica `4.3.2`» | **Confirmado**, y además hay tres emplazamientos más: `2.1.6:132-140` (§2.1.6.5, que lo desarrolla como caso de *data leakage*, con la misma consecuencia —valores de D2 fuera de `[0,1]`— y el mismo argumento de despliegue), `4.6:20` y `5.0:145` |
| «`3.3.1` duplica `4.2`/`4.3`» | **Parcialmente inexacto.** La tabla D1/D2/D3 de `3.3.1` duplica la de **`4.3.6`** (no `4.2`) y la de **`5.0.1`**. Con `4.2` lo que solapa es otra cosa: la afirmación S4 sobre los 17 tipos 0-day |
| «`3.4.2` y `3.5.2` anticipan `4.4`/`4.5`» | **Confirmado**, con matiz: las tablas **no son idénticas**. `3.4.2` da la *noción de anomalía* de cada algoritmo (información que `4.4` no repite) y `3.5.2` da la *idea* de cada clasificador. El solape real está en la **columna «Motivo de su inclusión»** y en el propio listado |
| «`3.5.4` duplica `4.3.4`» | **Confirmado**, y con un emplazamiento más en el capítulo 2: `2.1.6:134, 138` desarrolla el argumento de aplicar SMOTE **dentro** de cada *fold* (`ImbPipeline`, `firmas.py::_envolver_balanceo`) |
| — | **Faltaba S8**: `3.2.2` reproduce el argumento de `2.2.4.5`, que además cierra diciendo «Este es exactamente el flujo descrito en [[3.2 Arquitectura del sistema]]» (`2.2.4:107`) |
| — | **El solape capítulo 2 ↔ capítulo 3 que el encargo pedía buscar no es uno, son al menos tres**: S8 (`2.2.4.5` ↔ `3.2.2`), **S2** (`2.1.6.5` ↔ `3.3.2`) y **S7** (`2.1.6.5` ↔ `3.5.4`). Los dos últimos se localizaron en el pase de corrección del 2026-08-15; el capítulo 2 no había sido barrido entero en la primera pasada. **No se descarta que queden más** fuera de `2.1.6` y `2.2.4` |
| — | **Faltaba S15**: duplicación **interna** al capítulo 3 (`3.2.1` y `3.3.3` describen el mismo recorrido) |
| — | **Faltaban S9, S10, S11 y S14** |

### 1.2 Un apartado del barrido que sí existe, y uno que no

- `3.3.4 Protocolo de evaluación común` **existe** (`3.3:40-42`), pero **no es un apartado con
  desarrollo**: son tres líneas de fichero, de las cuales el grueso es un **único párrafo muy
  largo** (línea 42). Conviene saberlo antes de recortar: no hay estructura interna que reordenar.
- No existe ningún apartado numerado `3.5.6`, `3.4.5` ni `3.2.4`. La numeración del capítulo 3 es
  la que consta en las cabeceras leídas: 3.1.1–3.1.5 (con 3.1.5.1 y 3.1.5.2), 3.2.1–3.2.3,
  3.3.1–3.3.4, 3.4.1–3.4.4, 3.5.1–3.5.5, y `3.6` sin subdivisión.

> [!warning] Aviso de estado (2026-08-17): censo de numeración superado
> El censo de apartados de la viñeta anterior refleja el estado del vault en la fecha de este
> informe y quedó **superado por la Tanda 12 del 2026-08-16**. En particular, **`3.4.5 El coste del
> paradigma` SÍ existe hoy** (`03 Diseño del sistema/3.4 Modelo de detección de anomalías.md:35`).
> El análisis de solapes no se reescribe —este documento es un artefacto de investigación fechado—,
> pero la numeración debe verificarse contra disco antes de apoyarse en ella.

---

## 2. Qué hacer con cada solape, y dónde queda la versión canónica

Las frases de remisión están redactadas para **insertarse tal cual**. Todas siguen el patrón de
`3.1.5` (`3.1:36`), que declara en el propio texto dónde vive el material y qué hace este apartado
en su lugar — no un wikilink suelto, sino una frase que dice *qué no se repite y por qué*.

### S1 · Data snooping — **unificar y remitir**

| | |
|---|---|
| **Acción** | Recortar en `3.3.4`. Sustituir el inventario por una remisión |
| **Canónica** | **`2.1.6:76-90`** para el encuadre metodológico (qué es *data snooping*, tabla de las tres decisiones con su criterio) y **`6.1:35-40`** para el inventario como limitación del trabajo |
| **Por qué ahí** | El capítulo 3 no puede declarar un fallo de protocolo cometido en decisiones que aún no ha tomado: H-2, H-3 y Q1/C se resuelven con métricas del capítulo 5. Enunciarlo en el 3 obliga a adelantar resultados |

> [!important] Restricción vinculante: la formulación es canónica y está cerrada
> `resumen-de-decisiones.md:316-323` (punto **4. Formulación canónica**) fija literalmente el texto
> con el que se declara esta salvedad, enumera `3.3` entre las notas donde ya se llevó, y obliga a
> usarla «en cualquier sitio donde vuelva a aparecer esta salvedad, **para no tener dos redacciones
> de lo mismo**». Por tanto **este informe no propone una redacción nueva**: la frase de remisión de
> abajo **reproduce la canónica y solo le añade el reenvío**. T9 no puede parafrasearla, resumirla
> ni omitir su segunda mitad —la que dice que las métricas son optimistas—, porque ahí es donde
> vive la declaración de la limitación; sin ella el recorte convertiría un aviso en una nota
> bibliográfica. **La decisión no se reabre.**

> **Frase a insertar en `3.3.4`, en lugar del inventario actual** (el bloque en cursiva es la
> formulación canónica, copiada de `resumen-de-decisiones.md:320-323` **sin alterar**):
>
> «Esa regla tiene un perímetro acotado que conviene no ampliar al enunciarlo. *Tres decisiones del
> sistema se tomaron mirando D2: el detector de la etapa 1, el clasificador de la etapa 2 y **el set
> de características (54 frente a 122)**. Las tres son selección de modelo sobre el conjunto de
> test, es decir* data snooping, *y por tanto las métricas publicadas son optimistas respecto a lo
> que daría un test verdaderamente ciego.* El encuadre metodológico de esa desviación está en
> [[2.1.6 Metodologías y buenas prácticas|2.1.6]] y su tratamiento como limitación del trabajo, en
> [[6.1 Conclusiones|6.1]]; **el detalle de cada una de las tres no se reproduce aquí**, porque se
> toman con resultados que este capítulo todavía no ha presentado.»

> [!warning] Aviso para T9 — los punteros al inventario se contradicen entre sí
> No es que cuatro notas se declaren «el inventario completo»: **solo `5.4:32` lo hace**
> («Se declara aquí —con el inventario completo—»), y `6.1:35-40` lo es de hecho sin decirlo. El
> defecto real es que **cada nota manda al lector a un sitio distinto**:
>
> | Nota que remite | A dónde manda |
> |---|---|
> | `4.4:17` y `4.5:17` | → `4.6` |
> | `4.6:35` | → `6.1` |
> | `5.0:99` | → `A.3` **y** `6.1` |
> | `3.3:42` | → `4.3` **y** `6.1` |
>
> Recortar el capítulo 3 elimina una de esas remisiones, pero **no cierra el problema**: quedaría un
> lector al que `4.4` manda a `4.6` y `4.6` reenvía a `6.1`. Queda fuera del alcance de T9 tal como
> está definido; se registra para que se despache aparte, unificando el destino en `6.1`.

### S2 · Dónde se ajusta el escalador — **recortar y remitir**

| | |
|---|---|
| **Acción** | Suprimir `3.3.2` como apartado propio; absorber su contenido en una frase dentro de `3.3.1` |
| **Canónica conceptual** | **`2.1.6.5`** (`2.1.6:132-140`), que encuadra el ajuste del escalador como una de las **tres formas de fuga de información**, con la consecuencia contraintuitiva (D2 puede salir fuera de `[0,1]`) y el argumento de despliegue |
| **Canónica de implementación** | **`4.3.2`** (`4.3:43-78`), que trae el código, el punto exacto de ajuste y la consecuencia medida (4 características de D2 fuera de `[0,1]`) |
| **Por qué así** | Es la **misma relación categoría/instancia** que se aplica a S8: `2.1.6.5` explica el fenómeno *para cualquier pipeline*, `4.3.2` lo instancia en este. `3.3.2` no aporta ninguna de las dos cosas: reenvía a `4.3.2` en su propia línea 28 y repite el argumento de `2.1.6.5` sin citarlo |

> [!warning] Corrección del 2026-08-15 — la canónica no es solo `4.3.2`
> La primera versión de este informe daba `4.3.2` como única canónica y su frase de remisión mandaba
> **solo** a `4.3`. Eso dejaba **huérfano** el desarrollo conceptual de `2.1.6.5`: un lector del
> capítulo 3 acababa en el código sin pasar por la explicación de *por qué* eso es fuga de
> información. La frase de abajo remite a los dos sitios, cada uno por lo que aporta.

> **Frase a insertar (párrafo único que sustituye a `3.3.2`):**
>
> «Una decisión metodológica asociada a esta partición es que **todos los transformadores del
> preprocesado —codificador, escalador y selector— se ajustan únicamente sobre el tráfico de
> entrenamiento (D1+D3) y se aplican a D2 sin reajustarlos**, porque en un despliegue real no se
> conocen de antemano las categorías ni los rangos del tráfico futuro. El fundamento de ese criterio
> —el ajuste con datos de test como forma de fuga de información— está desarrollado en
> [[2.1.6 Metodologías y buenas prácticas|2.1.6]] (§2.1.6.5), y el punto exacto de ajuste de cada
> transformación, su implementación y su consecuencia medible, en
> [[4.3 Preprocesamiento de los datasets|4.3]] (§4.3.2 y §4.3.3); **aquí solo se fija el criterio**.»

### S3 · Tabla D1/D2/D3 — **unificar: una sola tabla en el capítulo 3, sin tamaños**

| | |
|---|---|
| **Acción** | Conservar la tabla de `3.3.1` **sin cifras** (ya es así: no lleva tamaños) y remitir para tamaños y función operativa |
| **Canónica** | **`4.3.6`** (`4.3:224-232`) para tamaños y distribución; **`5.0.1`** (`5.0:20-44`) para la función de cada partición en la evaluación y los sub-splits `D1_train`/`D1_val` |
| **Por qué ahí** | El criterio del encargo se cumple limpiamente: el *qué y por qué* de la partición es diseño; los *67.343 / 58.630 / 22.544* son implementación |

> **Frase a insertar al final de `3.3.1`, sustituyendo al párrafo actual sobre los 17 tipos:**
>
> «Esta separación es lo que hace posible medir la detección de 0-day: al no re-particionar el test,
> D2 conserva los tipos de ataque ausentes del entrenamiento, **cuyo recuento y enumeración están en
> [[4.2 Base de datos utilizada|4.2]] y en el [[A.1 Columnas del dataset NSL-KDD|Apéndice A.1]]**.
> **Los tamaños de cada subconjunto y su composición exacta pertenecen a la implementación y se dan
> en [[4.3 Preprocesamiento de los datasets|4.3]] (§4.3.6); la función de cada partición dentro del
> protocolo de evaluación, en [[5.0 Protocolo de evaluación|5.0]] (§5.0.1). No se anticipan aquí.**»
>
> *(La remisión a `4.2` es la que ya trae `3.3:21`: **se conserva, no se reapunta** — ver §S4.)*

### S4 · Los 17 tipos 0-day — **remitir (recorte pequeño, diez emplazamientos)**

| | |
|---|---|
| **Acción** | En el capítulo 3, mencionar la propiedad **sin el número 17** y sin la lista |
| **Canónica** | **`A.1`** (`A.1:99-107`) para la **enumeración uno a uno** —los 17 tipos van marcados con ★ dentro de la tabla de los 40, agrupados por categoría— y **`4.2:73`** para la cifra y su lectura (cobertura de tipos entre train y test) |

> [!warning] Corrección del 2026-08-15 — **la remisión actual de `3.3:21` NO está mal dirigida**
> La primera versión de este informe daba `4.3.6` (`4.3:238`) como «único sitio con los 17 tipos
> enumerados uno a uno» y ordenaba reapuntar allí la remisión de `3.3:21`. **Las dos cosas son
> falsas.** Verificado en disco:
>
> - `A.1:99-107` **sí** los enumera uno a uno, marcados con ★ y agrupados por categoría.
> - `4.2:73` da la cifra («17 tipos de ataque presentes en D2 no existen en el entrenamiento») y
>   **encadena explícitamente** a `A.1`: «(enumerados en el [[A.1 Columnas del dataset NSL-KDD|Apéndice A.1]])».
>
> Es decir, `3.3:21 → 4.2 → A.1` es una **cadena de remisión que funciona**. Reapuntarla a `4.3.6`
> la rompería y dejaría al lector en un apartado que no contiene la enumeración.
>
> **Instrucción para T9: no tocar la remisión de `3.3:21`.** Lo único que se recorta es el
> desarrollo del propio párrafo, según la frase de §S3.

### S5 y S6 · Tablas de algoritmos candidatos — **recortar la tabla, conservar el criterio**

| | |
|---|---|
| **Acción** | Sustituir ambas tablas por un párrafo que enumere las **familias** y justifique la diversidad |
| **Canónica** | **`4.4`** (`4.4:39-50`) y **`4.5`** (`4.5:21-26`) para el listado con rejillas; **`5.1`/`5.2`** para el desempeño |
| **Salvedad** | La columna «Noción de anomalía» de `3.4.2` (`3.4:23-28`) **no está en ningún otro sitio**. No es duplicación: es contenido conceptual único. Si se elimina la tabla, esa columna debe sobrevivir en prosa |

> **Frase a insertar en `3.4.2`, sustituyendo a la tabla:**
>
> «Conforme al requisito de alcance, se comparan cuatro detectores elegidos por representar
> **nociones distintas de anomalía**: aislamiento por particiones aleatorias (IsolationForest),
> frontera envolvente del comportamiento normal (OneClassSVM), densidad local relativa a los
> vecinos (LocalOutlierFactor) y error de reconstrucción (autoencoder implementado como
> `MLPRegressor`, que evita dependencias de *Deep Learning*). La diversidad es deliberada: permite
> comprobar qué noción de anomalía funciona mejor sobre este tráfico. **Las rejillas de búsqueda,
> las configuraciones ganadoras y las particularidades de implementación de cada uno son materia de
> [[4.4 Entrenamiento del modelo de detección de anomalías|4.4]], y su desempeño comparado, de
> [[5.1 Resultados del modelo de detección de anomalías|5.1]]; aquí solo se justifica la selección
> de candidatos.**»

> **Frase a insertar en `3.5.2`, sustituyendo a la tabla:**
>
> «Se comparan cuatro clasificadores supervisados que cubren enfoques distintos: reglas jerárquicas
> (DecisionTree, el más interpretable y base de la extracción de firmas de §3.5.3), conjuntos por
> *bagging* (RandomForest) y por *boosting* (HistGradientBoosting), y clasificación por distancia
> (KNN). **Sus espacios de búsqueda y configuraciones ganadoras están en
> [[4.5 Entrenamiento del modelo de detección basado en firmas|4.5]] y su comparación en
> [[5.2 Resultados del modelo de detección basado en firmas|5.2]]; no se adelantan aquí.**»

### S7 · Tratamiento del desbalance — **recortar y remitir**

| | |
|---|---|
| **Acción** | Reducir `3.5.4` a la decisión de diseño; quitar la descripción del método comparado |
| **Canónica** | **`4.3.4`** (`4.3:113-161`), con protocolo, tabla de 8 filas, garantía anti-*leakage* de SMOTE por *fold* y limitación sobre variables *one-hot* |
| **Canónica del argumento anti-*leakage*** | **`2.1.6.5`** (`2.1.6:134, 138`), que explica *por qué* sobremuestrear antes de particionar contamina la validación cruzada. `4.3.4` lo aplica; `2.1.6.5` lo fundamenta |
| **Comprobación del criterio** | `3.5.4` **ya remite** a `4.3.4` en su última frase (`3.5:34`). El recorte solo elimina el solape previo |

> [!note] Añadido en la corrección del 2026-08-15
> El capítulo 2 también dice esto: `2.1.6:138` desarrolla el argumento de aplicar SMOTE **solo al
> entrenamiento de cada *fold*** vía `ImbPipeline` (`firmas.py::_envolver_balanceo`) y remite ya a
> `4.3`. El capítulo 3 no debe reenunciarlo: la frase de abajo se limita a la decisión de diseño.

> **Frase a insertar como cuerpo de `3.5.4`:**
>
> «D3 está fuertemente desbalanceado: la categoría `u2r` reúne unas decenas de muestras frente a
> decenas de miles de `dos`. Entrenar sin más sobre ese reparto produciría un clasificador que
> ignora las clases minoritarias, de modo que el tratamiento del desbalance **no se fija por defecto
> sino como decisión guiada por datos**: se compara empíricamente, para cada algoritmo, la
> estrategia de balanceo disponible y se adopta la ganadora en validación cruzada. **El
> mini-experimento que resuelve esa comparación —protocolo, resultados y limitaciones— está en
> [[4.3 Preprocesamiento de los datasets|4.3]] (§4.3.4); este apartado solo declara que la decisión
> se toma así y no por convención.**»

### S8 · Orden de la cascada — **unificar; canónica en el capítulo 2**

| | |
|---|---|
| **Acción** | Reducir `3.2.2` a la conclusión operativa; el argumento de cuatro puntos se deja en `2.2.4.5` |
| **Canónica** | **`2.2.4.5`** (`2.2.4:100-107`) |
| **Por qué ahí** | Es el argumento **de paradigma** (por qué anomalías antes que firmas en general), no una decisión específica de este sistema. `2.2.4:107` ya lo enlaza con `3.2` |

> **Frase a insertar en `3.2.2`, sustituyendo al desarrollo actual:**
>
> «El orden de las etapas no es arbitrario, y su justificación conceptual —el clasificador de firmas
> nunca ha visto tráfico normal, luego no puede recibirlo directamente— **está desarrollada en
> [[2.2.4 Detección por firmas frente a detección por anomalías|2.2.4]] § *De la complementariedad a
> la arquitectura híbrida* y no se repite aquí**. Lo que este apartado fija es su consecuencia de
> diseño para este sistema: la etapa 1 decide **si** un flujo es sospechoso y solo lo sospechoso
> pasa a la etapa 2, que decide **qué** es.»

> [!note] Aquí el criterio del encargo funciona, pero conviene decir por qué
> «Cap. 3 = qué y por qué» podría leerse como que **toda** justificación pertenece al 3. No es el
> caso: `2.2.4.5` justifica el orden **para cualquier híbrido en cascada**, y `3.2.2` lo instancia.
> Es la misma relación categoría/instancia de `2.3.3` ↔ `3.1.5`.

### S9, S10 · Umbral p95 y «nunca mirando D2» — **recortar el segundo, conservar el primero**

| | |
|---|---|
| **Acción** | En `3.4.3`, conservar los dos primeros puntos (el criterio p95 y su homogeneidad entre algoritmos: es diseño puro) y **eliminar el tercero** (`3.4:38`), que es una instancia de S1/S10 repetida seis veces |
| **Canónica** | **`5.0.4`** (`5.0:86-97`), que además explica que la prohibición es estructural (la función de calibración no admite D2 en su firma) |
| **Nota** | El mismo enunciado aparece también en `3.5.5` (`3.5:40`). Al recortar, tratar los dos igual |

### S11 · Calibración de `UMBRAL_CONF` — **recortar el detalle, conservar la exigencia**

| | |
|---|---|
| **Acción** | Reducir el segundo párrafo de `3.5.5` (`3.5:40`). Conservar: que el umbral es una decisión de diseño y que no puede calibrarse sobre D2 porque los 0-day solo se **miden**, nunca se **optimizan** (argumento que no está en ningún otro sitio). Recortar: la descripción de la regla de presupuesto y del *out-of-fold* |
| **Canónica** | **`5.3`** (`5.3:48-59`), con la tabla de sensibilidad y el valor elegido; `5.0:58` para el valor congelado de τ |
| **Comprobación** | `3.5:40` ya remite a `5.3`; el recorte elimina lo que anticipa |

### S12, S13 · Protocolo común y semilla 42 — **unificar dentro del propio capítulo 3**

| | |
|---|---|
| **Acción** | El requisito de comparar cuatro algoritmos bajo protocolo idéntico se enuncia **tres veces dentro del capítulo 3** (`3.1:32`, `3.3:42`, `3.6:13`). Dejarlo solo en `3.1.4` y que `3.3.4` lo cite como requisito, sin reenunciarlo |
| **Canónica** | **`3.1.4`** dentro del capítulo 3; **`5.0.2`** (`5.0:50-67`) para la lista operativa de lo congelado |
| **Nota** | La semilla 42 aparece en seis sitios, pero cinco son menciones de paso. **No merece intervención** salvo la de `3.3.4`, que se va con el recorte de S1 |

### S15 · Recorrido de un flujo — **unificar dentro del capítulo 3**

| | |
|---|---|
| **Acción** | `3.2.1` (diagrama Mermaid + descripción de las dos etapas) y `3.3.3` (los mismos pasos en lista) dicen lo mismo. Suprimir `3.3.3` |
| **Canónica** | **`3.2.1`** (`3.2:13-23`), porque el diagrama es el artefacto más informativo y ya contiene las dos ramas de decisión |
| **Salvedad** | El paso 1 de `3.3.3` (*«se transforma con los codificadores y el escalador persistidos»*) **no está en `3.2.1`**. Si se suprime `3.3.3`, esa frase debe añadirse al diagrama de `3.2.1` o perderse deliberadamente |

---

## 3. Cuánto encoge el capítulo 3

> [!important] Corrección del 2026-08-18 — la base del capítulo es **un conteo**, no una estimación
> La versión anterior de este informe estimaba **a ojo** el capítulo 3 en **≈ 4.330 palabras** y
> advertía de que, en cuanto existiera una medición real, las cifras se sustituirían por las medidas.
> **Esa medición ya existe:** el capítulo 3 —las seis notas de `03 Diseño del sistema/`, `3.1` a
> `3.6`— suma **6.670 palabras contadas**. La base estimada estaba **corta un ~54 %**, porque no
> recogía el crecimiento posterior de las notas (`3.2` y `3.5`, en particular, se ampliaron después
> de la fecha de este informe).
>
> Consecuencia, aplicada más abajo: **los deltas absolutos de palabras se conservan** —salen del
> texto que se recorta, no de la base— y **los porcentajes se recalculan sobre 6.670**. El titular
> del capítulo completo pasa de **≈ −20 %** a **≈ −15 %**.
>
> Lo que **sigue siendo estimación** y así queda etiquetado: las columnas «antes»/«después» **por
> apartado y por bloque** (§3.1 y §3.2). El conteo disponible es del **capítulo entero**, no por
> nota, de modo que los porcentajes parciales no pueden reexpresarse con base verificada.
>
> Los números de **línea** de §1 son exactos: están verificados uno a uno contra disco.

### 3.1 Por apartado

*Todas las columnas son **estimación a ojo**, no medición. El Δ % fino se conserva para poder
ordenar los apartados por impacto —qué recorte rinde más—, **no para citarlo como resultado**.*

| Apartado | Palabras aprox. antes | Después | Δ palabras | Δ % (estimado) |
|---|---:|---:|---:|---:|
| `3.2.2` Por qué una cascada (S8) | 200 | 60 | **−140** | −70 % |
| `3.3.1` Subconjuntos D1/D2/D3 (S3, S4) | 170 | 90 | **−80** | −47 % |
| `3.3.2` Dónde se ajusta la normalización (S2) | 155 | 55 | **−100** | −65 % |
| `3.3.3` Recorrido por la cascada (S15) | 150 | 0 | **−150** | −100 % |
| `3.3.4` Protocolo de evaluación común (S1, S12) | 260 | 85 | **−175** | −67 % |
| `3.4.2` Algoritmos candidatos, etapa 1 (S5) | 165 | 85 | **−80** | −48 % |
| `3.4.3` Umbral de decisión (S10) | 150 | 120 | **−30** | −20 % |
| `3.5.2` Algoritmos candidatos, etapa 2 (S6) | 92 | 50 | **−42** | −46 % |
| `3.5.4` Tratamiento del desbalance (S7) | 130 | 75 | **−55** | −42 % |
| `3.5.5` `UMBRAL_CONF` (S11) | 280 | 175 | **−105** | −38 % |
| **Suma de los apartados intervenidos** | **1.752** | **795** | **−957** | **−55 %** |

### 3.2 Sobre el capítulo completo

*Las filas por bloque conservan **bases estimadas** —no hay conteo por nota— y sus porcentajes se
leen a la decena. La fila del **capítulo completo** es la única con **base contada** (6.670).*

| Bloque | Palabras antes | Después | Δ palabras | Δ % |
|---|---:|---:|---:|---:|
| `3.1` Requisitos (incluida `3.1.5`, que **no se toca**) | ≈ 1.430 *(est.)* | ≈ 1.430 | 0 | 0 % |
| `3.2` Arquitectura | ≈ 500 *(est.)* | ≈ 360 | **−140** | ≈ −30 % *(est.)* |
| `3.3` Metodología | ≈ 735 *(est.)* | ≈ 230 | **−505** | **≈ −70 %** *(est.)* |
| `3.4` Modelo de anomalías | ≈ 615 *(est.)* | ≈ 505 | **−110** | ≈ −20 % *(est.)* |
| `3.5` Modelo de firmas | ≈ 750 *(est.)* | ≈ 548 | **−202** | ≈ −30 % *(est.)* |
| `3.6` Conclusiones del capítulo | ≈ 300 *(est.)* | ≈ 300 | 0 | 0 % |
| **Capítulo 3 completo** | **6.670 (contadas)** | **5.713** | **−957** | **≈ −15 %** |

> [!caution] Las bases por bloque están desfasadas y **no suman la base contada**
> Las seis filas estimadas suman ≈ 4.330, que es justamente la base vieja: **no se han recontado**,
> porque el conteo disponible es del capítulo entero. Sus porcentajes son, por tanto, **techos
> optimistas** —cada bloque ha crecido desde el 2026-08-15—, y no deben citarse como resultado. Los
> **deltas absolutos sí se mantienen**: dependen del texto que se retira, no de lo que quede alrededor.

### 3.3 La cifra que responde al profesor

El profesor pide recortar **«los primeros apartados»**, que son `3.1`–`3.3`:

| | Antes | Después | Δ palabras | Δ % |
|---|---:|---:|---:|---:|
| **Capítulo 3 completo** | **6.670 (contadas)** | **5.713** | **−957** | **≈ −15 %** |
| `3.1` + `3.2` + `3.3` | ≈ 2.665 *(est. desfasada)* | ≈ 2.020 | **−645** | — *(ver aviso)* |
| `3.1`–`3.3` **excluida `3.1.5`**, que es material nuevo y no duplicado | ≈ 1.765 *(est. desfasada)* | ≈ 1.120 | **−645** | — *(ver aviso)* |

**Titular defendible, sobre la base contada:** aplicando las diez remisiones, el capítulo 3 encoge
**−957 palabras, ≈ −15 %** sobre sus **6.670** palabras actuales. El titular anterior —«≈ −20 %»—
era el **mismo recorte medido contra una base un ~54 % más corta**: el recorte no ha cambiado, ha
cambiado el denominador. El apartado `3.3`, el más afectado, sigue siendo el que más encoge en
términos absolutos (**−505 palabras**).

> [!todo] Los dos titulares del bloque `3.1`–`3.3` quedan **sin porcentaje** hasta que haya conteo por nota
> Los antiguos **≈ −25 %** (bloque `3.1`–`3.3`) y **≈ −35 %** (el mismo bloque descontando `3.1.5`)
> se calcularon sobre bases estimadas —2.665 y 1.765— que hoy se sabe cortas, igual que lo era la del
> capítulo. **No se reexpresan aquí porque el conteo verificado es del capítulo entero, no por nota**,
> y darles un porcentaje nuevo sería sustituir una estimación desfasada por otra inventada. Lo que sí
> se sostiene sin base: el recorte de ese bloque es de **−645 palabras**, es decir, **dos tercios de
> todo lo que se recorta en el capítulo**. Para cerrar el titular basta contar las palabras de `3.1`,
> `3.2` y `3.3` por separado, y las de `3.1.5` dentro de `3.1`.
>
> **Si el titular se escribe en un correo al profesor o en la memoria**, úsese el del capítulo
> completo —**≈ −15 % sobre 6.670 palabras**—, que es el único con base contada.

---

## 4. Solapes que NO son duplicación: repetición legítima

Estos casos aparecen dos o más veces y **deben seguir apareciendo**. Recortarlos empeoraría la
memoria.

| Caso | Dónde se repite | Por qué es legítimo |
|---|---|---|
| **`3.6 Conclusiones del capítulo`** repite en cuatro viñetas todo el capítulo 3 | `3.6:11-14` frente a `3.2`, `3.3`, `3.4`, `3.5` | Es un **cierre de capítulo**, género cuya función es exactamente recapitular. Aplicar aquí el criterio anti-duplicación lo vaciaría. Mismo argumento vale para `4.6` y `5.4` |
| **El FPR y el recall siempre juntos** | `5.0:93` (prohibición 2), `5.4:29`, `6.1:32` | No es repetición de una afirmación sino **aplicación repetida de una regla**. El propio protocolo prohíbe dar un recall sin su FPR: cada aparición conjunta es el cumplimiento de esa norma |
| **Los tamaños 22.544 / 9.711 / 12.833** en `4.3.6`, `5.0.1` y `5.1` | — | Cada uno cumple una función distinta: `4.3.6` los produce, `5.0.1` los declara como denominadores del protocolo y `5.1` los recuerda al presentar la matriz de confusión, donde el lector los necesita a la vista |
| **La definición de «semisupervisado / one-class»** | `3.4.1` (`3.4:15`) y `2.3.1:101, 118` | `2.3.1` **remite explícitamente a `3.4`** en lugar de redefinir; el patrón ya está bien resuelto. `3.4.1` es la canónica y debe quedarse íntegra |
| **La cifra 0,822 (f1_macro de RandomForest sobre D2)** en `5.2:35, 59`, `5.4:30`, `4.6:32`, `2.1.6:82` | — | Es una cifra **titular**: aparece donde se produce, donde se compara con la cascada y donde se declara el criterio con que se eligió el modelo. Repetir un titular no es duplicar contenido |
| **El requisito de interpretabilidad (S14)** | `3.1.3`, `3.5.3`, `4.5` | Cadena requisito → diseño → implementación, que es exactamente el reparto que el encargo pide. `3.1.3` lo enuncia como requisito no funcional en una línea; `3.5.3` explica cómo el diseño lo cumple; `4.5` lo ejecuta. **No tocar** |
| **`3.1.5 Modelo de amenaza`** completa | `3.1:34-68` | Recién escrita y **ya construida con el patrón correcto**: declara en el texto que el marco está en `2.3.3` y que aquí solo se instancia. Es el modelo a imitar, no material a recortar |
| **La distinción anomalías/firmas** en `3.2` y en `2.2.4` | — | Solo el **argumento del orden** (S8) está duplicado. La descripción de cada paradigma en `2.2.4.1`–`2.2.4.4` no se repite en el capítulo 3, que da por sabida la distinción |

---

## 5. Discrepancias detectadas — se reportan, no se corrigen

> [!warning] Ninguna de estas se toca en T9
> El encargo de T9 es recortar duplicación, no arbitrar números. Estas **dos** observaciones quedan
> registradas para que se despachen por separado. La lista se ha depurado el 2026-08-15: de las
> cuatro que traía la primera versión, **una era falsa** (la remisión de los 17 tipos 0-day; ver la
> corrección dentro de §S4) y **otra ya estaba resuelta en disco** (ver más abajo).

1. **Los punteros al inventario de las tres decisiones sobre D2 se contradicen entre sí.** No es que
   varias notas se autodenominen «el inventario completo» —**solo `5.4:32`** lo hace, y `6.1:35-40`
   lo es de hecho sin decirlo—; el defecto es que cada nota manda a un destino distinto:
   `4.4:17` y `4.5:17` → `4.6`; `4.6:35` → `6.1`; `5.0:99` → `A.3` **y** `6.1`; `3.3:42` → `4.3`
   **y** `6.1`. A eso se suma que las listas de reenvío cruzado no coinciden: `4.3:217` cita
   «2.1.6, 3.3, 5.4 y 6.1» y omite `4.6`, `5.0` y `A.3`. **Despacho sugerido:** unificar el destino
   en `6.1` y dejar el resto como remisiones simples. Recortar `3.3.4` reduce el problema pero no lo
   cierra.

2. **`4.5:39` es inexacto para KNN.** Afirma que los valores de CV «difieren marginalmente» de los
   de `4.3.4` porque aquel experimento usaba hiperparámetros por defecto. **Verificado contra los
   artefactos** (`Resultados\metricas_balanceo.csv` y `Resultados\metricas_firmas.csv`, variante de
   54 características, `commit 1163c90`):

   | Algoritmo | `metricas_balanceo.csv` (§4.3.4) | `metricas_firmas.csv` (§4.5) | ¿Difieren? |
   |---|---:|---:|---|
   | DecisionTree | 0,953018 | 0,953255 | Sí, marginalmente |
   | RandomForest | 0,973600 | 0,979758 | Sí |
   | **KNN** | **0,945349** | **0,945349** | **No: son el mismo número** |
   | HistGradientBoosting | 0,969377 | 0,969391 | Sí, en el 5.º decimal |

   - **KNN es el caso real:** los dos valores son **idénticos hasta el último dígito registrado**, de
     modo que para KNN la frase de `4.5:39` no se sostiene. La explicación más probable es que la
     rejilla eligiera la configuración por defecto (`n_neighbors=5, weights='uniform'`, que es
     justamente la `config_ganadora` de `metricas_firmas.csv:4`), en cuyo caso lo que hay que
     corregir no es la cifra sino **la frase**, que debe admitir la coincidencia y explicarla.
   - **HistGradientBoosting NO es un caso:** 0,969377 frente a 0,969391 **son cifras distintas**;
     parecían iguales solo porque las notas las redondean a cuatro decimales (0,9694 en ambas). Es
     un **artefacto de redondeo**, no una discrepancia. No hay nada que corregir ahí.

> [!done] Retirada el 2026-08-15 — la discrepancia sobre el «37 de 54» del KS ya está resuelta
> La primera versión de este informe pedía comprobar contra qué medición —(A) o (B)— estaba tomada
> la cifra «37 de las 54 características» que menciona `4.3`. **Ya está resuelto en disco y no
> procede reabrirlo:** por decisión del 2026-08-11, `4.2:132-142` declara `4.2` **fuente numérica
> única** del test KS, publica ambas mediciones con sus rankings, y la cifra «37 de 54» es la
> medición **(A)** (`4.2:102`). El propio callout declara además, como salvedad expresa, que la
> mención de `4.3` **no es una segunda publicación**. Se retira del listado.

---

## 6. Orden recomendado de ejecución para T9

Las remisiones no son independientes entre sí. Este orden evita rehacer trabajo:

1. **`3.3` primero** (S1, S2, S3, S4, S15): es el apartado que más encoge y del que dependen las
   remisiones de los demás. Al suprimir `3.3.3`, decidir antes si su paso 1 se trasplanta a `3.2.1`.
   **Dos cautelas aquí:** (a) la remisión de `3.3:21` a `4.2` **se conserva tal cual** —§S4 explica
   por qué—, y (b) el texto de S1 **se copia literal** de la formulación canónica de
   `resumen-de-decisiones.md:316-323`, sin reescribirlo.
2. **`3.2.2`** (S8), una vez `3.3` esté cerrado, para no dejar dos remisiones al mismo sitio.
3. **`3.4.2` y `3.4.3`** (S5, S10).
4. **`3.5.2`, `3.5.4`, `3.5.5`** (S6, S7, S11).
5. **`3.6` al final**: no se recorta, pero **hay que releerla** para que sus cuatro viñetas no citen
   material que acaba de irse del capítulo. Hoy `3.6:13` menciona el ajuste de la normalización, que
   tras S2 ya no se desarrolla en el capítulo.
6. **No tocar `3.1`** salvo el punto 5 de §2 (S12): `3.1.4` se queda como canónica y `3.1.5` se
   queda entera.

---

## Fuentes de este informe

Todas las afirmaciones proceden de la lectura directa de las notas del vault, con la línea citada
en §1. No se ha consultado bibliografía externa y **no se introduce ninguna cita nueva**: este
informe no consume ningún número del contador global de `Bibliografía.md`.

El alcance exacto de la lectura —qué se leyó íntegro, qué por búsqueda dirigida y qué no se abrió—
está declarado en el bloque **Verificación** de la cabecera, y no se repite aquí.

Además de las notas, se han consultado como fuente de verdad:

- `Resultados\metricas_balanceo.csv` y `Resultados\metricas_firmas.csv` — para la discrepancia 2
  de §5 (valores de `f1_macro` en CV de KNN y HistGradientBoosting).
- `resumen-de-decisiones.md:316-323` — formulación canónica del *data snooping*, citada en §S1.

**Historial de revisión.** Versión inicial del 2026-08-15. Pase correctivo del mismo día tras la
revisión del `auditor-ml` (`APTO CON CAMBIOS`): se corrigieron ocho puntos, de los que **tres podían
provocar un borrado equivocado en T9** —la falsa exclusividad de `4.3.6` para los 17 tipos 0-day
(§S4), la ausencia del capítulo 2 en S2 y S7, y la redacción de S1 que se apartaba de la formulación
canónica cerrada—. Lo confirmado correcto y no modificado: los diez emplazamientos del *data
snooping*, la numeración de §1.2, la §4 de repetición legítima y la aritmética de §3 sobre sus
bases.

**Corrección de medida del 2026-08-18.** Intervención acotada a §3: se sustituye la base estimada del
capítulo 3 (≈ 4.330 palabras, «a ojo») por su **conteo** (**6.670**), se recalcula sobre ella el
titular del capítulo (≈ −20 % → **≈ −15 %**, con el mismo recorte absoluto de −957 palabras), se
dejan **sin porcentaje** los dos titulares del bloque `3.1`–`3.3` por no existir conteo por nota, y
se retiran los dos avisos `> [!warning]` que quedaban condicionados a que apareciera una medición.
**No se han tocado las decisiones de los solapes S1–S15 ni el orden de ejecución de §6.**
