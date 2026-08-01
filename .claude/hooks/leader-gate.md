REGLA DE ENRUTADO OBLIGATORIA — se aplica a este mensaje, sea cual sea su contenido.

No respondas tú. Delega en el agente `leader` con la herramienta Agent
(`subagent_type: "leader"`, `run_in_background: false`) y pásale el mensaje del usuario
literal, sin reinterpretarlo ni resumirlo.

El leader se ubica leyendo `how-to-work.md` y `features.md`, y abre `next-steps.md §6`,
`resumen-de-decisiones.md` o el vault solo si el carril lo exige. Después clasifica el
mensaje en un **carril** (proceso) y un **track** (área).

Qué hacer con lo que te devuelva:

| Devuelve | Tú haces |
|---|---|
| Texto de respuesta | Lo transmites. Fin |
| `done -> <resumen>` | Lo transmites. Fin |
| `done -> Obsidian_TFG_Vault/99 Investigación/<tema>.md` | Carril Investigación: dices dónde está el informe y resumes la respuesta corta. **Sin cierre**: no se ha tocado código ni notas de la memoria |
| `necesito_spec -> <tema>` | Ejecutas el skill `grill-me` sobre ese tema, y al terminar vuelves a llamar al leader con lo acordado |
| `necesito_cierre -> <qué se hizo>` | Ejecutas el skill `cierre`: `features.md` + commit |
| `necesito aclaración -> <pregunta>` | Se la haces al usuario y vuelves a llamar al leader |
| `blocked -> <descripción>` | Lo transmites y esperas instrucciones |

Excepción única: si el usuario pide configurar el harness (`settings.json`, hooks,
definiciones de `.claude/agents/`, skills, permisos, `.mcp.json`), eso es infraestructura del
propio andamiaje y lo atiendes tú directamente, no el leader.
