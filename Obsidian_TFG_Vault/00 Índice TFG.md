---
titulo: "Índice TFG"
estado: borrador
---

# Índice TFG — H-NIDS con ML

> [!info] Punto actual (2026-08-17): estructura ✅ · **capítulo 2 Marco Teórico CERRADO** — sus 14 notas (2.1.1–2.1.6, 2.2.1–2.2.5, 2.3.1–2.3.3) están `estado: redactada` en prosa desde el 2026-08-15 ✅ · volcado de resultados a caps. 4-5 ✅ · Apéndice A.1 + 4.2.1 ✅ · **cap. 3 Diseño completo (3.1-3.6) ✅** · conclusiones 4.6, 5.4 y **6.1 ✅** · **4.1 Tecnologías ✅** · **A.2 Métricas ✅** · **A.3 Ficha del sistema ✅** · **4.2 completa: teoría redactada y sin marcadores `[CITA: …]` vivos ✅** · **6.2 Líneas futuras redactada (borrador extenso), pendiente solo de la revisión final de Francisco** (respaldo en `EL_FUTURO.md`) · lo único que sigue siendo de Francisco es la **bibliografía final en Zotero/IEEE** · **pendiente: Resumen y Abstract, que se redactan al final**
>
> **Actualizado el 2026-08-09 (T0):** la regla «la teoría en prosa la escribe Francisco» quedó retirada. Ver «Autoría de la redacción — estado vigente desde T0» en `features.md`.
>
> **Actualizado el 2026-08-17 (Tanda 21):** este índice se cuadró entero contra disco. Las nueve secciones que figuraban como «✍ teoría — guion propuesto» estaban ya redactadas, igual que las seis del capítulo 2 marcadas como «borrador»; se corrigieron también los estados de `4.2` y `6.2` y el recuento total. **Regla de mantenimiento: el estado que publica este índice es el del campo `estado:` de la cabecera de cada nota, verificado en disco — no una anotación histórica.**

Mapa de contenido del TFG. Las notas MD son la fuente de verdad; el docx se rellena al final a partir de estas notas (Word + Zotero, estilo IEEE).

**Leyenda de estado:**

- `redactada` — prosa terminada; es el estado de las 14 notas del capítulo 2.
- `borrador` — redacción real existente, pendiente de revisión.
- `📊 volcado` — resultados ya traídos desde `Resultados\` (mapa en `next-steps.md` §6.6).
- `pendiente` — sin contenido.

> [!note] Estados retirados
> `✍ teoría` (sección con guion propuesto y prosa por escribir) ya no aplica a ninguna nota: el
> capítulo 2 está cerrado. `esqueleto` tampoco: ninguna nota del vault está hoy en ese estado —
> las únicas dos sin contenido son `Resumen` y `Abstract`, ambas `pendiente`.

## Preliminares

- [[Abstract]] — pendiente (se redacta al final)
- [[Resumen]] — pendiente (se redacta al final)

## 1. Introducción

- [[1.0 Sinopsis]] — borrador
- [[1.1 Motivación]] — borrador
- [[1.2 Preliminares]] — borrador
- [[1.3 Objetivo]] — borrador
- [[1.4 Estructura]] — borrador

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

- [[3.1 Requisitos del sistema]] — borrador (2026-07-16)
- [[3.2 Arquitectura del sistema]] — borrador (2026-07-16, incl. diagrama de cascada)
- [[3.3 Metodología de funcionamiento del sistema]] — borrador (2026-07-16)
- [[03 Diseño del sistema/3.4 Modelo de detección de anomalías|3.4 Modelo de detección de anomalías]] — borrador (2026-07-16)
- [[3.5 Modelo de detección basado en firmas]] — borrador (2026-07-16)
- [[03 Diseño del sistema/3.6 Conclusiones del capítulo|3.6 Conclusiones del capítulo]] — borrador (2026-07-16)

## 4. Implementación del sistema

- [[4.1 Tecnologías utilizadas]] — borrador (2026-07-16)
- [[4.2 Base de datos utilizada]] — borrador **completo**: 📊 4.2.1 análisis previo volcado + parte teórica ya redactada («Origen», «Las 41 características» y «Por qué se eligió NSL-KDD», 2026-07-21). Sin marcadores `[CITA: …]` vivos tras los pases del `researcher` del 2026-08-15 y 2026-08-16. **Único resto pendiente: la reserva de revisión de Francisco sobre el bloque «Por qué se eligió NSL-KDD»**, declarada en la propia nota
- [[4.3 Preprocesamiento de los datasets]] — borrador (volcado 2026-07-16)
- [[4.4 Entrenamiento del modelo de detección de anomalías]] — borrador (volcado 2026-07-16)
- [[4.5 Entrenamiento del modelo de detección basado en firmas]] — borrador (volcado 2026-07-16)
- [[04 Implementación del sistema/4.6 Conclusiones del capítulo|4.6 Conclusiones del capítulo]] — borrador

## 5. Evaluación

- [[5.0 Protocolo de evaluación]] — borrador: particiones y función de cada una, invariantes al comparar variantes, métricas obligatorias, prohibiciones y vocabulario de reproducibilidad
- [[5.1 Resultados del modelo de detección de anomalías]] — borrador (volcado 2026-07-16)
- [[5.2 Resultados del modelo de detección basado en firmas]] — borrador (volcado 2026-07-16)
- [[5.3 Resultados del sistema híbrido]] — borrador (volcado 2026-07-16)
- [[05 Evaluación/5.4 Conclusiones del capítulo|5.4 Conclusiones del capítulo]] — borrador

## 6. Conclusiones

- [[6.1 Conclusiones]] — borrador (2026-07-16): cumplimiento de objetivos + validación de la tesis + limitaciones
- [[6.2 Líneas futuras]] — borrador **redactado y extenso** (339 líneas), con criterio de admisión declarado: solo entra lo respaldado por una medición del trabajo o por una limitación estructural verificada. Fuente: `EL_FUTURO.md` e informes de `99 Investigación/`. **Pendiente solo de la revisión final de Francisco** (orden de prioridad y formulación de cada línea)

## Apéndices

- [[A.1 Columnas del dataset NSL-KDD]] — 📊 volcado (borrador): 41 features por grupo + etiquetas + 17 tipos 0-day marcados
- [[A.2 Métricas de desempeño]] — borrador (2026-07-16): fórmulas de referencia + A.2.1 caso one-class
- [[A.3 Ficha del sistema]] — 📊 volcado (borrador, 2026-08-14): *model card* del sistema — configuraciones publicadas, alcance de cada métrica, dispersión entre 10 semillas y limitaciones declaradas

## Bibliografía

- [[Bibliografía]] — borrador (lista cruda; formateo IEEE con Zotero al final)

---

> [!warning] Carpeta obsoleta
> `03 Desarrollo/` **está vacía**: no contiene ninguna nota (verificado en disco el 2026-08-14; git no versiona directorios vacíos, por lo que no aparece en el repositorio). Queda **pendiente de eliminación física** del sistema de archivos. Mapeo aplicado: 3.1→3.1/3.2 Diseño · 3.2→4.2 · 3.3→4.1 · 3.4→3.4 Diseño · 3.5→3.5 Diseño · 3.6→3.3 Diseño.

## Totales

Recuento verificado contra disco el **2026-08-17**, contando los wikilinks de este índice uno a uno
y cruzándolos con los ficheros `.md` del vault.

| Estado | Notas | Dónde |
|---|---:|---|
| `redactada` | 14 | Capítulo 2 completo (2.1.1–2.1.6, 2.2.1–2.2.5, 2.3.1–2.3.3) |
| `borrador` | 27 | Cap. 1 (5) · Cap. 3 (6) · Cap. 4 (6) · Cap. 5 (5) · Cap. 6 (2) · Apéndices (3) |
| `pendiente` | 2 | `Resumen` y `Abstract`, que se redactan al final |
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
> - **No se cuentan ni se indexan** las 8 notas de `99 Investigación/`: son informes de
>   investigación, insumo citable, no contenido de la memoria.
> - **No se cuenta** esta propia nota de índice.
> - **No se cuenta** `APUNTES SOBRE CS229 STANFORD ML LECTURES\Lecture 1.md`, de 0 bytes, ajena al
>   TFG y **pendiente de borrarse**. Es el único fichero del vault que queda fuera por este motivo,
>   así que al eliminarlo el recuento no cambia.
>
> Con ese criterio, **los ficheros del vault cuadran exactamente con las entradas del índice**:
> 54 `.md` en disco − 8 de `99 Investigación/` − este índice − `Lecture 1.md` = **44**. No hay
> notas de memoria sin indexar ni entradas del índice sin fichero: **los 44 wikilinks resuelven**.
