---
titulo: "Resumen"
numero: "-"
estado: redactada
docx_ref: "Resumen"
---

# Resumen

## Título del Trabajo Fin de Grado

**Sistema híbrido de detección de intrusiones en red basado en aprendizaje automático: detección de anomalías y firmas en cascada sobre NSL-KDD**

La versión inglesa del título y del resumen se recoge en [[Abstract]].

## Resumen

Los sistemas de detección de intrusiones en red (NIDS) se apoyan mayoritariamente en firmas de ataques conocidos, un enfoque preciso sobre lo catalogado pero estructuralmente ciego ante los ataques de tipo nuevo (*0-day*). Este Trabajo Fin de Grado diseña, implementa y evalúa un **sistema híbrido de detección de intrusiones (H-NIDS)** que combina, en cascada, una etapa de detección de anomalías —entrenada únicamente con tráfico legítimo— y una segunda etapa de clasificación multiclase basada en firmas aprendidas de ataques conocidos. El objetivo es conservar la capacidad de nombrar el ataque conocido sin renunciar a detectar el desconocido, que queda etiquetado como categoría accionable `unknown` en lugar de ser forzado a una clase existente.

El trabajo se realiza sobre el conjunto de datos **NSL-KDD**, del que se derivan tres particiones especializadas: D1 (solo tráfico normal, para la etapa de anomalías), D3 (solo ataques de tipo conocido, para la etapa de firmas) y D2 (el conjunto oficial de test completo, reservado para la evaluación). Se comparan cuatro detectores de anomalías (Isolation Forest, One-Class SVM, Local Outlier Factor y un autoencoder) y cuatro clasificadores supervisados (árbol de decisión, *random forest*, k-vecinos y *gradient boosting* por histogramas), cada grupo con el protocolo propio de su etapa: umbral en el percentil 95 de las puntuaciones de anomalía sobre una partición de validación de D1 en la primera etapa, y búsqueda en rejilla con validación cruzada por `f1_macro` y balanceo intra-*fold* en la segunda. Como control se entrena un ***random forest* monolítico** de cinco clases, representativo del patrón dominante en la literatura sobre este dataset. La estabilidad de los resultados se contrasta mediante un barrido de diez semillas con comparaciones pareadas.

La configuración seleccionada, autoencoder seguido de *random forest*, alcanza sobre D2 un **recall global de ataques 0-day de 0,771 frente a 0,150 del baseline monolítico**, y un f1_macro a cinco clases de 0,641 frente a 0,472, con una exactitud binaria de 0,860. La ventaja se obtiene a un coste declarado: una tasa de falsos positivos del 10,2 % y una pérdida de rendimiento sobre los ataques conocidos respecto a la etapa de firmas aislada. A ello se añade una limitación de protocolo: tres decisiones del sistema —la elección del detector, la del clasificador y la del conjunto de 54 características frente al de 122— se tomaron observando D2, de modo que las métricas publicadas son optimistas respecto a las que daría un conjunto de test verdaderamente ciego. Se concluye que la arquitectura híbrida aporta una capacidad de detección de lo desconocido que el clasificador cerrado no posee, y que la reducción de la tasa de falsos positivos es la prioridad de mejora, dada su proyección a prevalencias bajas de ataque, en el escenario ilustrativo declarado en el capítulo 5.

**Palabras clave:** detección de intrusiones en red; aprendizaje automático; detección de anomalías; ataques 0-day; NSL-KDD; sistema híbrido en cascada.
