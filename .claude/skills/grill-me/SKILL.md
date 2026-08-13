---
name: grill-me
description: Interroga al usuario sobre un plan o un encargo hasta cerrarlo. Se usa cuando el leader devuelve `necesito_spec`, o cuando el usuario pide estresar un plan antes de construirlo ('grill', 'gríllame', 'interrógame').
---

Interrogas a Francisco sobre el encargo hasta que quede **cerrado**, no hasta que te parezca
suficiente. Recorres el árbol de decisiones rama por rama, resolviendo las dependencias entre
decisiones de una en una.

## Cómo preguntar

- **Una pregunta a la vez**, esperando respuesta. Varias de golpe abruman y se contestan a medias.
- **Con tu respuesta recomendada incluida.** «¿A o B?» sin recomendación le hace el trabajo a él.
  Di cuál elegirías y por qué; que corrija si no está de acuerdo.
- **Si la pregunta se contesta leyendo el disco, la lees tú.** No le preguntes lo que el repo ya
  sabe: `features.md`, `resumen-de-decisiones.md`, `Resultados/`, el vault y el código están ahí.
  Preguntarle algo verificable gasta su turno y suele delatar que no lo has mirado.
- **Ancla la pregunta al punto concreto.** Si su encargo traía varias viñetas, di **cuál** estás
  preguntando y cuáles ya das por cerradas. No preguntes en abstracto sobre «el plan».
- **Al recomendar saltarse algo, di si es por coste o por sustancia, y enseña la medida.** «Es
  insignificante» sin número no vale.

## Los tres campos que hay que cerrar siempre

Un encargo no está cerrado hasta que los tres tienen respuesta explícita:

1. **La pregunta concreta** que hay que responder, o el resultado concreto que hay que producir.
2. **Qué entra** en el alcance.
3. **Qué queda fuera.** Este es el que más se olvida y el que más caro sale.

## Dos campos más, propios de este TFG

Los da por supuestos el `leader` y **tú no los puedes inventar**:

4. **A qué nota o capítulo alimenta** el resultado. Un informe que no alimenta a nada es paja.
5. **Si las fuentes encontradas van a `Bibliografía.md`** — solo aplica al carril Investigación, y
   solo el `researcher` escribe ese fichero.

## Y en este proyecto, dos preguntas que casi siempre hay que hacer

- **¿Mueve alguna cifra ya publicada en la memoria?** Si la respuesta es sí, hay que decirlo antes
  de empezar, no al cerrar.
- **¿Requiere re-ejecutar algo?** Las corridas cuestan horas. Si el encargo se puede satisfacer
  leyendo un artefacto que ya está en `Resultados/`, dilo y ahórrale la corrida.

## Al terminar

Devuelves lo acordado **en una lista corta y literal**, campo por campo, para que el hilo
principal se lo pase al `leader` sin reinterpretarlo. Si algo quedó sin cerrar, lo dices
explícitamente en vez de rellenarlo con tu criterio.
