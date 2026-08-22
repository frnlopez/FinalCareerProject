# Bloque F — Capítulo 6 (Conclusiones y Líneas futuras) + Apéndices

## Veredicto del bloque

El limpio se corta a mitad del capítulo 6: `6.1 Conclusiones` está pasada a limpio en una versión
**vieja** (anterior a la reapertura T2-T4 y a la reestructuración por los 9 objetivos de `1.3`), y
`6.2 Líneas futuras` es solo el título, sin una sola línea de contenido. **No hay ningún apéndice
real en el limpio**: lo que sigue al título "Líneas futuras" es un único bloque —el antiguo
`A.1 Columnas del dataset NSL-KDD`— seguido de una `Bibliografía` de 11 entradas y de texto de
plantilla de Word sin desarrollar ("Nombre del apéndice A", "Este texto está escrito en estilo
Normal..."). Los apéndices `A.2 Métricas de desempeño` y, sobre todo, `A.3 Ficha del sistema` —que
en el actualizado suman varios miles de palabras cada uno— **no han llegado al limpio en absoluto**.
Se diagnostica agrupado por apéndice/sección, no entrada a entrada, tal como pide el encargo.
`6.1`, `6.2` y `A.3` están modificadas sin commitear en el vault: el volcado de hoy ya las recoge.

---

## [B] 6.1 Conclusiones - falta el desglose de los 9 objetivos específicos en 4 bloques (A-D)
**Qué pasa:** el limpio conserva la versión antigua de "Grado de cumplimiento de los objetivos": 4
bullets sueltos (investigar métodos, revisar/preprocesar, entrenar/validar, estudiar resultados).
El actualizado la sustituyó por una correspondencia explícita **uno a uno** con los 9 objetivos
enunciados en `1.3 Objetivo`, agrupados en cuatro bloques temáticos (A: fundamentos teóricos —obj.
1—; B: dataset/preprocesado/validación —obj. 2-3—; C: entrenamiento e integración de la cascada
—obj. 4-6—, con la salvedad metodológica del objetivo 4 sobre H-2; D: contraste, medición 0-day y
análisis crítico —obj. 7-9—).
**Por qué importa:** si `1.3 Objetivo` ya enumera 9 objetivos (verificar en el propio limpio, que sí
llegó actualizado según el volcado de esa sección), el capítulo de conclusiones del limpio queda
descolgado: no cierra el círculo objetivo-por-objetivo que el resto de la memoria sí prometía.
**Dónde encaja en el limpio:** sección `## Conclusiones`, inmediatamente bajo el encabezado
"### Grado de cumplimiento de los objetivos", sustituyendo los 4 bullets actuales ("- Investigar los
dos métodos...", etc.).
**Material:** actualizado, `# Conclusiones` → `## Conclusiones` → "Sobre los **nueve objetivos
específicos** enunciados en 1.3 Objetivo, la valoración se agrupa en cuatro bloques temáticos..."
hasta el final de "Bloque D — contraste, medición de lo desconocido y análisis crítico".

## [B] 6.1 Conclusiones - falta entera la sección "Límites de lo medible con NSL-KDD" (6.1.4)
**Qué pasa:** el actualizado añade una subsección completa, distinta de "Limitaciones", que separa
límites *del sistema* de límites *del banco de pruebas NSL-KDD*: seis límites numerados (sin marca
de tiempo, sin despliegue real -P9-, sin adversario adaptativo -P10-, una sola semilla, el
clasificador cerrado no acota riesgo de espacio abierto, los 0-day del NSL-KDD no son amenazas
actuales) y una tabla de balance final contra los diez errores metodológicos de Arp et al.
(P1-P10), con "cubierto"/"cubierto hasta donde el dataset permite" para cada uno. Es contenido
sustancial (varios miles de palabras) que el limpio no tiene en ninguna forma, ni resumida.
**Por qué importa:** es la sección que sostiene metodológicamente por qué el trabajo no promete lo
que el NSL-KDD no puede medir (deriva temporal, adversario adaptativo, prevalencia real); sin ella
las "Limitaciones" que sí están en el limpio quedan sin el marco que las justifica y sin conectar
con `2.3.3` y `3.1.5`.
**Dónde encaja en el limpio:** justo después de "### Limitaciones" y antes de la sección
"## Líneas futuras", como nueva subsección "### Límites de lo medible con NSL-KDD".
**Material:** actualizado, sección "### Límites de lo medible con NSL-KDD" completa, con
subapartados "#### 6.1.4.1 Los seis límites, uno a uno" y "#### 6.1.4.2 Balance frente al catálogo
de errores metodológicos" (tabla P1-P10).

## [B] 6.2 Líneas futuras - toda la sección está vacía en el limpio (solo el título)
**Qué pasa:** en el limpio, "## Líneas futuras" no tiene ni una frase debajo; pasa directo al primer
apéndice. En el actualizado es una sección desarrollada de ~2.500-3.000 palabras, organizada en dos
bloques: **A. Refinamientos sobre el sistema actual** (6.2.1 ensemble de detectores de anomalías,
6.2.2 reconocimiento de conjunto abierto/open-set, 6.2.3 vector de error de reconstrucción por
característica como entrada de la etapa 2, 6.2.4 conjuntos de características distintos por etapa,
6.2.5 generación automática de firmas a partir de `unknown`) y **B. Ampliación del alcance
experimental** (6.2.6 migración a un dataset con marca de tiempo y representación de secuencia, en
tres peldaños, con la nota sobre por qué el aprendizaje incremental por ráfagas NO es *Nested
Learning*). Cada línea trae observación motivadora, propuesta concreta y qué habría que medir para
que cuente como mejora.
**Por qué importa:** es un entregable completo del capítulo de conclusiones, ya cerrado y
redactado; dejarlo en blanco en el limpio no es un recorte, es simplemente no haberlo pasado.
**Dónde encaja en el limpio:** bajo "## Líneas futuras", sustituyendo el vacío actual.
**Material:** actualizado, desde "## Líneas futuras" ("El criterio de admisión de esta sección es
deliberadamente restrictivo...") hasta el final de la sección "### Enlaces" (justo antes de
"::: {custom-style=\"Apéndice\"} Apéndices").

## [B][PROFESOR] Apéndices - falta entero `A.3 Ficha del sistema`
**Qué pasa:** el limpio no tiene ningún rastro de `A.3`. En el actualizado es el apéndice más
extenso del trabajo: una *model card* (A.3.1-A.3.9: detalles del modelo, particiones de datos,
configuraciones seleccionadas por semilla 42, alcance de cada métrica, infraestructura de cómputo,
resultados con dispersión entre semillas, límite de reproducibilidad de rutas *hardcodeadas*, las
tres decisiones tomadas mirando D2, y otros límites del alcance evaluado) más un anexo teórico
(A.3.10: algoritmos que el sistema NO usa —regresión logística, k-means/jerárquico, redes
neuronales—; A.3.11: desarrollo metodológico en extensión de CRISP-DM, la partición train/test, la
validación cruzada y el coste de GridSearchCV).
**Por qué importa:** `A.3` es donde fue a parar el material que el profesor pidió sacar del cuerpo
de la memoria (ficha T7 en `features.md`: "RESTRICCIÓN DURA (T7): lo que salga del cuerpo se MUEVE
a A.3, NO se elimina"). El propio `6.1 Conclusiones` del actualizado remite explícitamente a
`A.3 §A.3.7` para el volcado tabulado de las tres decisiones de *data snooping*. Sin `A.3`, esas
remisiones del cuerpo (ya presentes en el `6.1` actualizado, y candidatas a entrar en el limpio) no
tienen destino: no es un apéndice cosmético, es la contraparte de recortes ya aplicados en el
cuerpo.
**Dónde encaja en el limpio:** como tercer apéndice, después de un futuro `A.2 Métricas de
desempeño`, con el título "Ficha del sistema" en el mismo estilo "Título 2 de Apéndice" que usan
`A.1` y `A.2`.
**Material:** archivo `memoria_completa_20260822-154416_fd089cc-sucio.md`, desde
"::: {custom-style=\"Título 2 de Apéndice\"} Ficha del sistema" hasta el final del fichero (línea
~4240 hasta 5017); también disponible como nota independiente en
`Obsidian_TFG_Vault/Apéndices/A.3 Ficha del sistema.md`.

## [B] Apéndices - falta entero `A.2 Métricas de desempeño`
**Qué pasa:** el limpio salta de "Métricas de desempeño" (solo el título suelto, sin desarrollar,
justo antes de la Bibliografía) al final del fichero. El actualizado desarrolla ese apéndice
completo: convención de signo, matriz de confusión y conteos base, fórmulas de precision/recall/F1/
FPR "de consulta rápida", promedios macro vs. weighted, curvas ROC/PR, y dos subsecciones propias:
`A.2.1 Métricas del modelo de anomalías` (por qué el FPR del sistema es el FPR de la etapa 1,
umbral por percentil 95, FPR nominal 5 % frente al real medido: **10,2 % en 54 características y
8,5 % en 122**) y `A.2.2 Métricas ajenas a la clasificación, no reportadas por este trabajo` (MAE/
RMSE y coeficiente de silueta, por completitud del marco teórico).
**Por qué importa:** sin A.2.1 no hay dónde documentar la relación exacta entre `bin_fpr` del
híbrido y `fpr` del Autoencoder en `metricas_anomalias.csv`, que el actualizado usa para justificar
por qué "el FPR del sistema ES el FPR de la etapa de anomalías" — una afirmación que aparece citada
desde otras partes de la memoria.
**Dónde encaja en el limpio:** el limpio ya tiene el título "####### Métricas de desempeño" suelto
justo antes de la Bibliografía; ahí debe entrar todo el contenido.
**Material:** actualizado, desde "::: {custom-style=\"Título 2 de Apéndice\"} Métricas de
desempeño" hasta justo antes de "::: {custom-style=\"Título 2 de Apéndice\"} Ficha del sistema".

## [R] Apéndice A.1 (Columnas del dataset) - subtítulos con numeración A.1.1-A.1.5 ausentes
**Qué pasa:** el contenido de tablas de A.1 SÍ está en el limpio (las 41 características y las
etiquetas coinciden en sustancia), pero el limpio no usa la numeración `A.1.1`-`A.1.5` que trae el
actualizado en sus subtítulos ("A.1.1 Características básicas", ..., "A.1.5 Etiquetas: tipos de
ataque y categorías"); en el limpio son subtítulos sin numerar.
**Por qué importa:** es menor porque el contenido ya está, pero la numeración es la que después usan
las referencias cruzadas de otras secciones (p. ej. A.3 remite a "A.1" en general, y si se numeran
subapartados en otros sitios conviene que A.1 también los lleve, por consistencia con A.2/A.3).
**Dónde encaja en el limpio:** en cada uno de los cuatro subtítulos de tabla dentro del apéndice
"Columnas del dataset NSL-KDD".
**Material:** actualizado, títulos "A.1.1 Características básicas (1–9)" a "A.1.5 Etiquetas: tipos
de ataque y categorías".

## [P] Bibliografía - el limpio tiene 11 entradas frente a las ~78 numeradas del proyecto
**Qué pasa:** la Bibliografía que aparece intercalada en el limpio (entre el apéndice A.1 y el resto
de plantilla) trae solo 11 referencias en formato antiguo (sin `[n]` consistente con
`Bibliografía.md`). El vault vivo tiene 78 números emitidos (70 vivos + 8 quemados).
**Por qué importa:** se marca como prescindible en este bloque porque, según `CLAUDE.md`, "la
bibliografía final en Zotero/IEEE sigue siendo de Francisco" y es trabajo mecánico fuera del vault;
no es una diferencia de contenido del capítulo 6/apéndices que corresponda resolver por un agente.
Se deja constancia solo para que no se pierda de vista al pasar a limpio el documento entero.
**Dónde encaja en el limpio:** sección "Bibliografía" tras el apéndice A.1.
**Material:** `Obsidian_TFG_Vault/Bibliografía.md`, tabla completa de referencias `[1]`-`[78]`.

## [D] 6.1 Conclusiones - el limpio detalla f1_macro 0.909→0.472 en "Validación de la tesis"; el actualizado lo remite a 5.3
**Qué pasa:** el limpio, en el párrafo de "Validación de la tesis del híbrido", cita explícitamente
el desplome de f1_macro del baseline (0.909 en CV → 0.472 en test) dentro del propio 6.1. El
actualizado retiró esas cifras de 6.1 y las dejó solo en 5.3 ("La comparación completa —tabla de
métricas, matrices de confusión y análisis de la forma del error— está en 5.3 y no se reproduce
aquí"). Las cifras siguen vivas y son las mismas (`metricas_baseline.csv`), no hay contradicción de
valor.
**Por qué importa:** no es una pérdida de contenido, es una reorganización deliberada para no
duplicar cifras entre capítulos; se marca [D] porque, si se pasa el 6.1 actualizado tal cual, el
párrafo del limpio con esas cifras debe sustituirse (no fusionarse) por la versión resumida.
**Dónde encaja en el limpio:** párrafo "La hipótesis central del trabajo..." dentro de "### Grado de
cumplimiento..." → "### Validación de la tesis del híbrido".
**Material:** actualizado, párrafo que empieza "La hipótesis central del trabajo —que un enfoque
híbrido..." en `## Conclusiones` → `### Validación de la tesis del híbrido`.

## [D] Apéndices - el limpio trae texto de plantilla de Word sin desarrollar al final del fichero
**Qué pasa:** tras la Bibliografía, el limpio conserva literalmente instrucciones de plantilla
("Nombre del apéndice A", "Este texto está escrito en estilo Normal...", "Para introducir una
Figura/Tabla en un apéndice, debe proceder igual que...") con una figura y tabla de ejemplo vacías.
El actualizado no tiene nada de esto: los apéndices reales (A.1, A.2, A.3) sustituyen por completo
ese contenido de plantilla.
**Por qué importa:** confirma que el corte del limpio ocurrió literalmente a mitad de trabajo sobre
la plantilla de apéndices de Word, antes de rellenarla con A.2 y A.3; es la prueba física de que
falta pasar el bloque completo, no un detalle a limpiar.
**Dónde encaja en el limpio:** al final del fichero, tras la tabla de ejemplo "Tabla en Apéndice
A.1. Ejemplo de pie de tabla en apéndice."
**Material:** N/A — este contenido de plantilla debe eliminarse al pasar A.2 y A.3 a limpio, no
completarse.
