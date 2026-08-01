# Diagramas Mermaid — H-NIDS

Diagramas extraídos de `../PIPELINE.md` como ficheros Mermaid (`.mmd`) sueltos,
para poder verlos y exportarlos a imagen fácilmente (p. ej. para la memoria en Word).

| Fichero | Contenido |
|---|---|
| `01_pipeline_completo.mmd` | Flujo completo: `program.py` (preprocesado + splits D1/D2/D3) → `validacion.py` → capa de modelos (`anomalias.py` · `firmas.py` · `baseline.py` · `hibrido.py`), implementada al completo desde el 2026-07-16 |
| `02_mapeo_ataques.mmd` | Mapeo de los tipos de ataque NSL-KDD → 5 categorías (normal, dos, probe, r2l, u2r) |
| `03_orquestacion_agentes.mmd` | Ciclo de trabajo multiagente (`.claude/agents/`): orquestador → implementador → auditor/ejecutor → redactor → cronista → `next-steps.md` |

## Cómo verlos / exportarlos

- **Online (rápido):** pega el contenido en <https://mermaid.live> → exporta a PNG/SVG.
- **VS Code:** instala la extensión *Mermaid Preview* (o *Markdown Preview Mermaid Support*) y abre el `.mmd`.
- **Obsidian / Markdown:** `PIPELINE.md` **no** contiene el código Mermaid; incrusta el `.svg`
  renderizado (ver «Flujo de edición»). Para ver el diagrama basta con abrir `PIPELINE.md`, pero
  lo que se muestra es la imagen ya generada, no un render en vivo del `.mmd`.
- **CLI (para PNG/SVG reproducibles):**
  ```bash
  # -s 3 = escala x3 (PNG de más resolución para la memoria)
  npx @mermaid-js/mermaid-cli -i 01_pipeline_completo.mmd -o 01_pipeline_completo.png -s 3
  npx @mermaid-js/mermaid-cli -i 01_pipeline_completo.mmd -o 01_pipeline_completo.svg
  ```

## Flujo de edición

El `.mmd` es la **única fuente**. `../PIPELINE.md` ya no contiene el código Mermaid:
incrusta el `.svg` renderizado. Por tanto, al cambiar un diagrama:

1. Edita el `.mmd`.
2. Regenera su `.png` **y** su `.svg` con los comandos de arriba.

Así `PIPELINE.md` (que apunta al `.svg`) queda actualizado automáticamente.
