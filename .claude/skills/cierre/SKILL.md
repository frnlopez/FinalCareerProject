---
name: cierre
description: Cierra el trabajo de un agente — actualiza features.md y hace el commit. Úsalo cuando el leader devuelva `necesito_cierre`, o cuando el usuario pida commitear lo que tenga pendiente.
---

# Cierre

Cierras el trabajo que un agente acaba de terminar. Dos mitades de la misma pregunta —
*"¿queda esto registrado?"*:

1. **Registro operativo**: qué tarea se ha cerrado, en `features.md`.
2. **Durabilidad**: sin commit no queda ningún rastro del trabajo.

Corres en **hilo principal**, no como subagente, por una razón concreta: **tienes que
preguntarle al usuario antes de commitear** y un subagente no tiene canal para hacerlo.

---

## Paso 1 — `features.md`

Despacha al `cronista` (`subagent_type: "cronista"`) con qué se hizo y qué ficheros se tocaron.
Él mueve la tarea de `## Abiertas` a `## Cerradas` con su fecha. El hash lo pondrás tú en el
paso 3, cuando exista.

No lo hagas tú a mano: el `cronista` conoce el formato y detecta incoherencias con el resto de
documentos.

Si el trabajo **no tenía ficha** (carril Intervención), el `cronista` añade la línea
directamente a `## Cerradas`. Una Intervención sin ficha y sin commit no deja ningún rastro:
esto es lo único que evita que desaparezca.

---

## Paso 2 — Enséñale lo que hay y pregúntale

Ejecuta `git status --short` y `git diff --stat` y **muéstraselos al usuario**. Después
propón el mensaje de commit y pregunta.

No des el commit por hecho. El usuario puede decir que no — pero **enterado**, no por olvido.
Esa es toda la razón de que este paso exista.

**Mira el diff antes de proponer nada.** Si aparecen ficheros que el trabajo no debería haber
tocado, dilo antes de preguntar. Si aparece algo que `.gitignore` debería estar excluyendo (un
`.joblib`, un CSV procesado, el venv), **para y avísalo**: es un fallo del `.gitignore`, no
material para un commit.

### El mensaje de commit

- **En español**, coherente con el resto del proyecto.
- Una línea de asunto en imperativo, sin punto final, y cuerpo solo si hace falta.
- Prefijo por track: `codigo:` o `informe:`. Para el andamiaje, `harness:`.
- Referencia la tarea de `features.md` si la tenía.

```
informe: redactar 5.4 Conclusiones del capítulo

Cifras tomadas de Resultados/metricas_hibrido.csv. Auditado por auditor-ml
(APTO CON CAMBIOS, aplicados). Tarea: "5.4 Conclusiones cap.5".
```

**Un commit por tarea cerrada**, no por sesión: así el hash de `features.md` apunta a algo
concreto. Si el usuario tiene varias cosas sueltas de golpe, propón separarlas y que él decida.

---

## Paso 3 — Commit y push

Con el visto bueno del usuario:

```bash
git add <los ficheros del trabajo>    # nunca `git add -A` a ciegas
git commit -m "<mensaje>"
git push origin develop
```

Se trabaja siempre en **`develop`**. `main` solo se actualiza en hitos y **solo si el usuario lo
pide** — cierre de capítulo, entrega, defensa:

```bash
git push origin develop:main
```

Después, escribe el hash corto en la línea de `features.md` que el `cronista` acaba de cerrar.

Si el `push` falla por autenticación, **no reintentes en bucle**: díselo al usuario y pídele que
lo lance él con `! git push origin develop`.

---

## Trabajo del usuario sin commitear

Si el `git status` muestra ficheros que **ningún agente ha tocado en este ciclo** —típicamente
notas del vault que el usuario ha escrito a mano: la teoría 2.x, la 6.2, la bibliografía—
ofrécele commitearlos también, en un commit aparte y con su propio mensaje.

Es el caso que el proceso no cubre por sí solo: ese trabajo nunca dispara un `necesito_cierre`
porque no lo produjo ningún agente, y sin este recordatorio se queda sin commitear
indefinidamente.

---

## Qué NO haces

- ❌ Commitear sin preguntar.
- ❌ `git add -A` sin haber mirado el `git status`.
- ❌ Empujar a `main` sin que el usuario lo pida explícitamente.
- ❌ `push --force` a nada. El volcado inicial fue la excepción y ya pasó.
- ❌ Marcar una tarea como *aceptada* o borrarla de `features.md`. Eso es del usuario.
- ❌ Commitear ficheros que `.gitignore` debería excluir. Si aparecen, es un bug del
  `.gitignore` y se arregla primero.
