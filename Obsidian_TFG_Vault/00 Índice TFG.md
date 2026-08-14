---
titulo: "Índice TFG"
estado: borrador
---

# Índice TFG — H-NIDS con ML

> [!info] Punto actual (2026-07-16): estructura ✅ · guiones de teoría ✅ · volcado de resultados a caps. 4-5 ✅ · Apéndice A.1 + 4.2.1 ✅ · **cap. 3 Diseño completo (3.1-3.6) ✅** · conclusiones 4.6, 5.4 y **6.1 ✅** · **4.1 Tecnologías ✅** · **A.2 Métricas ✅** (todo borrador) · **teoría en prosa: `redactor-tfg`** · **6.2 Líneas futuras: borrador del `redactor-tfg` con revisión de Francisco** (respaldo en `EL_FUTURO.md`) · lo único que sigue siendo de Francisco es la **bibliografía final en Zotero/IEEE** · Resumen/Abstract al final
>
> **Actualizado el 2026-08-09 (T0):** la regla «la teoría en prosa la escribe Francisco» quedó retirada. Ver «Autoría de la redacción — estado vigente desde T0» en `features.md`.

Mapa de contenido del TFG. Las notas MD son la fuente de verdad; el docx se rellena al final a partir de estas notas (Word + Zotero, estilo IEEE).

**Leyenda de estado:**

- `borrador` — redacción real existente, pendiente de revisión.
- `✍ teoría` — sección de investigación/teoría con guion ya propuesto; la redacta el `redactor-tfg` partiendo de ese guion. **La marca «(Francisco)» que llevaba antes se retiró el 2026-08-09 (T0).**
- `📊 pendiente de volcado` — esqueleto listo; falta volcar resultados desde `Resultados\` (mapa en `next-steps.md` §6.6).
- `esqueleto` — estructura creada, redacción pendiente.
- `pendiente` — sin contenido.

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

### 2.1 Machine Learning

- [[2.1.1 Introducción al ML]] — borrador
- [[2.1.2 Tipos de ML]] — borrador
- [[2.1.3 Ciclo de vida de un proyecto ML]] — borrador
- [[2.1.4 Algoritmos de ML]] — borrador
- [[2.1.5 Métricas de evaluación]] — borrador
- [[2.1.6 Metodologías y buenas prácticas]] — ✍ teoría — guion propuesto 2026-07-15, redacta el redactor-tfg

### 2.2 Ciberseguridad

- [[2.2.1 Introducción a la ciberseguridad]] — borrador (subestructura 2.2.2–2.2.5 creada 2026-07-15)
- [[2.2.2 Sistemas de detección de intrusiones]] — ✍ teoría — guion propuesto 2026-07-15, redacta el redactor-tfg
- [[2.2.3 Taxonomía de los IDS]] — ✍ teoría — guion propuesto 2026-07-15, redacta el redactor-tfg
- [[2.2.4 Detección por firmas frente a detección por anomalías]] — ✍ teoría — guion propuesto 2026-07-15, redacta el redactor-tfg
- [[2.2.5 Taxonomía de ataques y panorama de amenazas]] — ✍ teoría — guion propuesto 2026-07-15, redacta el redactor-tfg

### 2.3 Inteligencia Artificial

- [[2.3.1 IA, ML y Deep Learning]] — ✍ teoría — guion propuesto 2026-07-15, redacta el redactor-tfg
- [[2.3.2 La IA en ciberseguridad]] — ✍ teoría — guion propuesto 2026-07-15, redacta el redactor-tfg
- [[2.3.3 Límites y consideraciones éticas]] — ✍ teoría — guion propuesto 2026-07-15, redacta el redactor-tfg

## 3. Diseño del sistema

- [[3.1 Requisitos del sistema]] — borrador (2026-07-16)
- [[3.2 Arquitectura del sistema]] — borrador (2026-07-16, incl. diagrama de cascada)
- [[3.3 Metodología de funcionamiento del sistema]] — borrador (2026-07-16)
- [[03 Diseño del sistema/3.4 Modelo de detección de anomalías|3.4 Modelo de detección de anomalías]] — borrador (2026-07-16)
- [[3.5 Modelo de detección basado en firmas]] — borrador (2026-07-16)
- [[03 Diseño del sistema/3.6 Conclusiones del capítulo|3.6 Conclusiones del capítulo]] — borrador (2026-07-16)

## 4. Implementación del sistema

- [[4.1 Tecnologías utilizadas]] — borrador (2026-07-16)
- [[4.2 Base de datos utilizada]] — 📊 4.2.1 análisis previo volcado (borrador) + ✍ parte teórica: la redacta el `redactor-tfg` (borrador de «Origen» y «Las 41 características» ya existente); Francisco solo revisa el «por qué NSL-KDD». Contenido: ficha T10
- [[4.3 Preprocesamiento de los datasets]] — borrador (volcado 2026-07-16)
- [[4.4 Entrenamiento del modelo de detección de anomalías]] — borrador (volcado 2026-07-16)
- [[4.5 Entrenamiento del modelo de detección basado en firmas]] — borrador (volcado 2026-07-16)
- [[04 Implementación del sistema/4.6 Conclusiones del capítulo|4.6 Conclusiones del capítulo]] — borrador

## 5. Evaluación

- [[5.1 Resultados del modelo de detección de anomalías]] — borrador (volcado 2026-07-16)
- [[5.2 Resultados del modelo de detección basado en firmas]] — borrador (volcado 2026-07-16)
- [[5.3 Resultados del sistema híbrido]] — borrador (volcado 2026-07-16)
- [[05 Evaluación/5.4 Conclusiones del capítulo|5.4 Conclusiones del capítulo]] — borrador

## 6. Conclusiones

- [[6.1 Conclusiones]] — borrador (2026-07-16): cumplimiento de objetivos + validación de la tesis + limitaciones
- [[6.2 Líneas futuras]] — ✍ borrador del `redactor-tfg` con revisión final de Francisco (podría crecer a apartado propio); fuente: `EL_FUTURO.md`

## Apéndices

- [[A.1 Columnas del dataset NSL-KDD]] — 📊 volcado (borrador): 41 features por grupo + etiquetas + 17 tipos 0-day marcados
- [[A.2 Métricas de desempeño]] — borrador (2026-07-16): fórmulas de referencia + A.2.1 caso one-class
- [[A.3 Ficha del sistema]] — 📊 volcado (borrador, 2026-08-14): *model card* del sistema — configuraciones publicadas, alcance de cada métrica, dispersión entre 10 semillas y limitaciones declaradas

## Bibliografía

- [[Bibliografía]] — borrador (lista cruda; formateo IEEE con Zotero al final)

---

> [!warning] Carpeta obsoleta
> `03 Desarrollo/` **está vacía**: no contiene ninguna nota (verificado en disco el 2026-08-14; git no versiona directorios vacíos, por lo que no aparece en el repositorio). Queda **pendiente de eliminación física** del sistema de archivos. Mapeo aplicado: 3.1→3.1/3.2 Diseño · 3.2→4.2 · 3.3→4.1 · 3.4→3.4 Diseño · 3.5→3.5 Diseño · 3.6→3.3 Diseño.

**Totales:** 5 borrador (Intro) + 6 borrador (Marco 2.1–2.2) + 9 ✍ teoría (todas con guion propuesto 2026-07-15) + 10 📊 pendiente de volcado/mixto + 10 esqueleto + 2 pendiente + Bibliografía (de 43 notas).
