# features — tareas del TFG

> **Registro operativo.** Aquí vive lo que está **abierto** ahora mismo y lo que se ha
> **cerrado**, con el commit que lo hace durable. Es lo primero que lee el `leader` en cada
> mensaje.
>
> - `next-steps.md` queda **congelado en cuanto a casillas**: su §1-§5 es historial y su §6 es
>   la especificación técnica de cada script, que sigue vigente como referencia. Ya no se
>   marcan tareas allí.
> - `resumen-de-decisiones.md` sigue siendo el registro de **decisiones de diseño**.
> - Lo mantiene el agente `cronista`, disparado por el skill `cierre`. **Estar en Abiertas
>   significa estar abierto**: una tarea aceptada la borra el usuario, nadie más.

Estados: `[ ]` pendiente · `[~]` en curso · `[!]` bloqueado
Fechas absolutas `AAAA-MM-DD`. Track: **Código** / **Informe**.

---

## Abiertas

- [ ] **Auditar la bibliografía** · Informe · `researcher`
  10 entradas en `Bibliografía.md`, todas en uso. Detectado el 2026-08-01: `[9]` duplica `[8]`
  (mismo libro de Stallings) y es una copia alojada en un dominio de terceros; `[2]` (Anderson)
  y `[8]` (Stallings) están sin año ni editorial; `[1]` apoya una cifra de ciberataques en
  prensa sectorial. Completar datos de cita y marcar lo que no llegue a nivel 1-2. **Sin
  borrar nada**: las bajas las decide Francisco.

- [ ] **Resumen y Abstract** · Informe · `redactor-tfg`
  Se redactan **al final**, cuando el resto de capítulos esté cerrado.
  Notas: `00 Preliminares/Resumen.md` y `00 Preliminares/Abstract.md`.

### Fuera de la lista operativa — lo escribe Francisco

No se despachan a ningún agente. El `leader` no debe crear tareas para esto.

- Teoría en prosa de `02 Marco Teórico` (2.1.6, bloque 2.2 Ciberseguridad, bloque 2.3 IA).
  Los guiones de temas ya están propuestos en las 9 notas (2026-07-15).
- Prosa teórica de `4.2` (origen del dataset NSL-KDD, las 41 características, por qué NSL-KDD).
- `6.2 Líneas futuras` — material de respaldo en `EL_FUTURO.md`.
- Bibliografía final con Zotero en formato IEEE.

---

## Cerradas

| Fecha | Track | Tarea | Commit |
|---|---|---|---|
| 2026-08-01 | — | Arquitectura de agentes: `leader`, `researcher`, hook de entrada, skill `cierre`, `features.md`, git y README | `791a698` |
| 2026-07-16 | Informe | Apéndice A.2 — fórmulas de las métricas (borrador) | — |
| 2026-07-16 | Informe | 4.1 Tecnologías utilizadas (borrador) | — |
| 2026-07-16 | Informe | 6.1 Conclusiones (borrador) | — |
| 2026-07-16 | Informe | Apéndice A.1 + 4.2.1 — columnas del dataset, EDA y validación (borrador) | — |
| 2026-07-16 | Informe | Cap. 3 Diseño completo, 3.1–3.6 (borrador) | — |
| 2026-07-16 | Informe | Volcado de resultados a caps. 4 y 5 — dos auditorías adversarias, ambas aplicadas | — |
| 2026-07-16 | Código | Experimento H1: cierra Q1/C → **54 características (opción A)** | — |
| 2026-07-15 | Informe | Reestructuración del vault: 43 notas, MOC renumerado, 0 wikilinks rotos | — |
| ≤2026-07-16 | Código | `program.py` · `validacion.py` · `anomalias.py` · `firmas.py` · `baseline.py` · `hibrido.py` — implementados, auditados y ejecutados en 54 y 122 características | — |

> Las tareas anteriores al 2026-08-01 se cerraron sin git: el repositorio se creó ese día. El
> detalle de cada una está en la bitácora de `next-steps.md §5`.
