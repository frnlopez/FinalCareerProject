---
titulo: "Índice TFG"
estado: borrador
---

# Índice TFG — Sistema híbrido de detección de intrusiones en red con ML

> [!info] Título del TFG (fijado el 2026-08-18)
> **Sistema híbrido de detección de intrusiones en red basado en aprendizaje automático: detección de anomalías y firmas en cascada sobre NSL-KDD**
>
> El encabezado de esta nota es una forma abreviada del título por legibilidad; el título válido para la memoria es el de arriba, literal.

> [!info] Punto actual (2026-08-18): estructura ✅ · **capítulo 1 CERRADO — sus 5 notas (1.0-1.4) están `estado: redactada`** ✅ · **capítulo 2 Marco Teórico CERRADO** — sus 14 notas (2.1.1–2.1.6, 2.2.1–2.2.5, 2.3.1–2.3.3) están `estado: redactada` en prosa desde el 2026-08-15 ✅ · volcado de resultados a caps. 4-5 ✅ · Apéndice A.1 + 4.2.1 ✅ · **cap. 3 Diseño completo (3.1-3.6) ✅** · conclusiones 4.6, 5.4 y **6.1 ✅** · **4.1 Tecnologías ✅** · **A.2 Métricas ✅** · **A.3 Ficha del sistema ✅** · **4.2 completa: teoría redactada y sin marcadores `[CITA: …]` vivos ✅** · **6.2 Líneas futuras redactada (borrador extenso), pendiente solo de la revisión final de Francisco** · lo único que sigue siendo de Francisco es la **bibliografía final en Zotero/IEEE** · **Resumen y Abstract redactados (2026-08-18): las 43 notas de la memoria están `estado: redactada`** ✅
>
> **Actualizado el 2026-08-18:** resincronizados los estados publicados con el frontmatter real. La
> tanda anterior pasó 26 notas de `borrador` a `redactada` en disco y este índice seguía publicando
> los valores viejos (decía 14/27/2). El recuento real de ese momento, verificado nota a nota, fue
> **40 `redactada` · 1 `borrador` · 2 `pendiente`**.
>
> **Actualizado el 2026-08-18 (tanda del capítulo 1):** reescritas `1.0`, `1.2`, `1.3` y `1.4`, con lo
> que **el capítulo 1 queda redactado por completo**: las cinco notas (1.0-1.4) están `estado:
> redactada` en su frontmatter, verificado en disco. `1.4 Estructura` cerró su hueco de contenido y
> deja de ser `borrador`. El recuento pasa a **41 `redactada` · 0 `borrador` · 2 `pendiente`**, sobre
> las mismas 43 notas de memoria y 44 entradas indexadas. Con ello **`borrador` no se aplica a
> ninguna nota de la memoria**: la única entrada que sigue en ese estado es `Bibliografía`, que no es
> nota de memoria y se cuenta aparte.
>
> **Actualizado el 2026-08-18 (Tanda 27):** redactadas `Resumen` y `Abstract`, las dos últimas notas
> que quedaban `pendiente`; su frontmatter dice ya `estado: redactada` (verificado en disco). El
> recuento pasa a **43 `redactada` · 0 `borrador` · 0 `pendiente`**, sobre las mismas 43 notas de
> memoria y 44 entradas indexadas. Con ello **ninguna nota de la memoria queda sin prosa**: lo que
> sigue pendiente no es redacción, sino la revisión de Francisco sobre `4.2` («Por qué se eligió
> NSL-KDD») y `6.2`, más la bibliografía final en Zotero/IEEE.
>
> **Actualizado el 2026-08-17 (Tanda 21):** este índice se cuadró entero contra disco. Las nueve secciones que figuraban como «✍ teoría — guion propuesto» estaban ya redactadas, igual que las seis del capítulo 2 marcadas como «borrador»; se corrigieron también los estados de `4.2` y `6.2` y el recuento total. **Regla de mantenimiento: el estado que publica este índice es el del campo `estado:` de la cabecera de cada nota, verificado en disco — no una anotación histórica.**

Mapa de contenido del TFG. Las notas MD son la fuente de verdad; el docx se rellena al final a partir de estas notas (Word + Zotero, estilo IEEE).

**Leyenda de estado:**

- `redactada` — prosa terminada; es el estado de **las 43 notas** de la memoria.
- `borrador` — redacción real existente pero con hueco de contenido; **hoy no lo lleva ninguna nota
  de la memoria**. La única entrada del listado en `borrador` es `Bibliografía`, que es aparato de
  apoyo y se cuenta aparte de las 43.
- `📊 volcado` — resultados ya traídos desde `Resultados\`. La correspondencia entre cada artefacto
  y la sección que lo cita queda declarada en la propia nota de destino, donde el artefacto se
  nombra al presentar la tabla o la figura; la ficha consolidada del sistema y el alcance de cada
  métrica están en [[A.3 Ficha del sistema]].
- `pendiente` — sin contenido; **hoy no lo lleva ninguna nota**.

> [!note] Estados retirados
> `✍ teoría` (sección con guion propuesto y prosa por escribir) ya no aplica a ninguna nota: el
> capítulo 2 está cerrado. `esqueleto` tampoco. Y desde el 2026-08-18 **`pendiente` tampoco lo
> lleva ninguna nota**: `Resumen` y `Abstract`, las dos últimas que quedaban sin contenido, están
> redactadas.

## Preliminares

- [[Abstract]] — redactada (2026-08-18)
- [[Resumen]] — redactada (2026-08-18)

## 1. Introducción

- [[1.0 Sinopsis]] — redactada
- [[1.1 Motivación]] — redactada
- [[1.2 Preliminares]] — redactada
- [[1.3 Objetivo]] — redactada
- [[1.4 Estructura]] — redactada

## 2. Marco Teórico

> [!success] Capítulo cerrado
> Las **14 notas** de este capítulo están `estado: redactada` (verificado en la cabecera de cada
> nota, 2026-08-17). No queda prosa por escribir aquí; lo que pueda quedar son ajustes de revisión
> y el pase de numeración de citas, que es competencia del `researcher`.

### 2.1 Machine Learning

- [[2.1.1 Introducción al ML]] — redactada
- [[2.1.2 Tipos de ML]] — redactada
- [[2.1.3 Ciclo de vida de un proyecto ML]] — redactada
- [[2.1.4 Algoritmos de ML]] — redactada
- [[2.1.5 Métricas de evaluación]] — redactada
- [[2.1.6 Metodologías y buenas prácticas]] — redactada

### 2.2 Ciberseguridad

- [[2.2.1 Introducción a la ciberseguridad]] — redactada
- [[2.2.2 Sistemas de detección de intrusiones]] — redactada
- [[2.2.3 Taxonomía de los IDS]] — redactada
- [[2.2.4 Detección por firmas frente a detección por anomalías]] — redactada
- [[2.2.5 Taxonomía de ataques y panorama de amenazas]] — redactada

### 2.3 Inteligencia Artificial

- [[2.3.1 IA, ML y Deep Learning]] — redactada
- [[2.3.2 La IA en ciberseguridad]] — redactada
- [[2.3.3 Límites y consideraciones éticas]] — redactada

## 3. Diseño del sistema

- [[3.1 Requisitos del sistema]] — redactada
- [[3.2 Arquitectura del sistema]] — redactada (incl. diagrama de cascada)
- [[3.3 Metodología de funcionamiento del sistema]] — redactada
- [[03 Diseño del sistema/3.4 Modelo de detección de anomalías|3.4 Modelo de detección de anomalías]] — redactada
- [[3.5 Modelo de detección basado en firmas]] — redactada
- [[03 Diseño del sistema/3.6 Conclusiones del capítulo|3.6 Conclusiones del capítulo]] — redactada

## 4. Implementación del sistema

- [[4.1 Tecnologías utilizadas]] — redactada
- [[4.2 Base de datos utilizada]] — redactada: 📊 4.2.1 análisis previo volcado + parte teórica ya redactada («Origen», «Las 41 características» y «Por qué se eligió NSL-KDD», 2026-07-21). Sin marcadores `[CITA: …]` vivos tras los pases del `researcher` del 2026-08-15 y 2026-08-16. **Único resto pendiente: la reserva de revisión de Francisco sobre el bloque «Por qué se eligió NSL-KDD»**, declarada en la propia nota
- [[4.3 Preprocesamiento de los datasets]] — redactada (📊 volcado 2026-07-16)
- [[4.4 Entrenamiento del modelo de detección de anomalías]] — redactada (📊 volcado 2026-07-16)
- [[4.5 Entrenamiento del modelo de detección basado en firmas]] — redactada (📊 volcado 2026-07-16)
- [[04 Implementación del sistema/4.6 Conclusiones del capítulo|4.6 Conclusiones del capítulo]] — redactada

## 5. Evaluación

- [[5.0 Protocolo de evaluación]] — redactada: particiones y función de cada una, invariantes al comparar variantes, métricas obligatorias, prohibiciones y vocabulario de reproducibilidad
- [[5.1 Resultados del modelo de detección de anomalías]] — redactada (📊 volcado 2026-07-16)
- [[5.2 Resultados del modelo de detección basado en firmas]] — redactada (📊 volcado 2026-07-16)
- [[5.3 Resultados del sistema híbrido]] — redactada (📊 volcado 2026-07-16)
- [[05 Evaluación/5.4 Conclusiones del capítulo|5.4 Conclusiones del capítulo]] — redactada

## 6. Conclusiones

- [[6.1 Conclusiones]] — redactada: cumplimiento de objetivos + validación de la tesis + limitaciones
- [[6.2 Líneas futuras]] — redactada, extensa (339 líneas), con criterio de admisión declarado: solo entra lo respaldado por una medición del trabajo o por una limitación estructural verificada. **Pendiente solo de la revisión final de Francisco** (orden de prioridad y formulación de cada línea)

## Apéndices

- [[A.1 Columnas del dataset NSL-KDD]] — redactada (📊 volcado): 41 features por grupo + etiquetas + 17 tipos 0-day marcados
- [[A.2 Métricas de desempeño]] — redactada: fórmulas de referencia + A.2.1 caso one-class
- [[A.3 Ficha del sistema]] — redactada (📊 volcado, 2026-08-14): *model card* del sistema — configuraciones publicadas, alcance de cada métrica, dispersión entre 10 semillas y limitaciones declaradas

## Bibliografía

- [[Bibliografía]] — borrador (lista cruda; formateo IEEE con Zotero al final)

---

## Totales

Recuento verificado contra disco el **2026-08-18**, leyendo el campo `estado:` del frontmatter de
cada nota del vault una a una y cruzándolo con los wikilinks de este índice.

| Estado | Notas | Dónde |
|---|---:|---|
| `redactada` | 43 | Preliminares (2: `Resumen`, `Abstract`) · Cap. 1 completo (5: 1.0-1.4) · Cap. 2 completo (14) · Cap. 3 (6) · Cap. 4 (6) · Cap. 5 (5) · Cap. 6 (2) · Apéndices (3) |
| `borrador` | 0 | Ninguna nota de memoria; `Bibliografía` va aparte |
| `pendiente` | 0 | Ninguna: `Resumen` y `Abstract` se redactaron el 2026-08-18 |
| **Notas de memoria** | **43** | |
| + `Bibliografía` | 1 | Nota de apoyo, la mantiene el `researcher` |
| **Entradas indexadas** | **44** | |

> [!important] Criterio de recuento — declararlo evita que la cifra vuelva a desfasar
> El número anterior («43 notas») no cuadraba con los 44 wikilinks del propio listado porque
> **no decía qué contaba**. El criterio que se aplica aquí es:
>
> - **Se cuentan** las notas de la memoria: preliminares, capítulos 1-6 y apéndices.
> - **`Bibliografía` se cuenta aparte**, no como nota de memoria: es aparato de apoyo y su
>   contenido lo gestiona el `researcher`. De ahí que 43 notas den 44 entradas indexadas.
> - **No se cuentan ni se indexan** los documentos de trabajo auxiliares: notas de investigación
>   previa, material de consulta y borradores de apoyo. Son insumo del proceso de elaboración, no
>   contenido de la memoria, y por tanto no forman parte de lo que se entrega ni de este índice.
> - **No se cuenta** esta propia nota de índice.
> - **No se cuentan** los ficheros ajenos al TFG que puedan convivir en el vault (apuntes de
>   terceros, material descargado o ficheros vacíos). Al no aportar contenido a la memoria, su
>   presencia o su eliminación no altera el recuento.
>
> Con ese criterio la cuenta cierra sobre sí misma: **43 notas de memoria + `Bibliografía` = 44
> entradas indexadas**, exactamente las que enumera el listado de arriba. No hay notas de memoria
> sin indexar ni entradas del índice sin nota detrás: **los 44 wikilinks resuelven**.
