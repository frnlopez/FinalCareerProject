# Instrucciones del repaso .docx <-> vault (para retomar en sesión nueva)

Contexto: Francisco pasa a limpio su memoria en `Proyecto_Fin_de_Grado-FJLM-2026.docx`
y va capítulo por capítulo comprobando qué se dejó por el camino respecto al vault.
Capítulos 1-5 YA REPASADOS Y APLICADOS. **Siguiente: capítulo 6.**

## Fuentes

- Informe de comparación: `Resultados/docx/COMPARACION/INFORME_DIFERENCIAS.md`
  (Bloque F cubre el capítulo 6). Encargo original en `_BRIEF.md`.
- Extracción del .docx: **hay que regenerarla**, el .docx cambia cada sesión.
  No hay pandoc en la máquina. Se extrae con un script Python de stdlib que
  descomprime `word/document.xml` (ver "Cómo re-extraer" abajo).
- Fuente de verdad: las notas de `Obsidian_TFG_Vault/`.

## Cómo trabajar (lo que Francisco ha pedido explícitamente)

1. **Clasificar cada falta en IMPRESCINDIBLE / RECOMENDABLE / PRESCINDIBLE.**
   Filtro objetivo, no estético: *¿algún capítulo posterior remite a esto por
   título o lo da por sabido?* Se verifica buscando las remisiones en disco.
2. **Marcar aparte las CONTRADICCIONES** (cifra vieja publicada que los datos
   actuales ya no sostienen). Van primero, antes que cualquier omisión.
3. **SER CONCISO Y DIRECTO.** Pidió expresamente no marearle: nada de párrafos
   de justificación largos. Tabla escueta: qué / dónde / categoría.
4. **Dar el TEXTO REDACTADO listo para pegar**, no solo la sede. Sacarlo del
   vault donde exista, sin wikilinks y con referencias `[n]` por número.
5. **La sede, con la frase literal** tras la que va la inserción — nunca
   `fichero:línea` ni descripciones vagas.
6. **Verificar toda cifra contra los CSV de `Resultados/`** antes de darla.
7. **No meter tablas nuevas** salvo que él lo pida: prefiere prosa corrida.
8. **Solo lectura.** No editar el .docx, ni las notas del vault, ni el informe
   de comparación. Él aplica los cambios a mano en Word.
9. Al aplicar él los cambios, **re-extraer y comprobar**, porque ha introducido
   incoherencias nuevas al pegar (columnas nuevas con valores viejos, una
   corrección hecha en un sitio y no en su gemelo de otro capítulo).

## Decisiones que ya tomó (no reabrir)

- **2.1.6 Metodologías: DESCARTADA entera**, salvo el pitfall P3 (data snooping),
  que ya está metido en 3.3.2. Consecuencia viva: quedan remisiones huérfanas a
  2.1.6 repartidas por el documento (eran 8; 3.3.1, 3.3.2 y 4.6 ya corregidas).
- **2.2.5.2 (gradación de visibilidad) y 4.3.1(B) (segunda medición de drift):
  descartadas.** Por eso se cayeron dos puntos del capítulo 5 que dependían de
  ellas (inversión probe/r2l, y el exceso de FPR como dataset shift).
- Del capítulo 3 quedaron sin aceptar: 3.1.5.2 (P10, experimento adversario),
  3.4 (coste del paradigma), 3.5 (clásicas vs tabular profunda).
  **Aviso vivo: 3.5 y 2.3.1.3 están ambos descartados, así que el trabajo no
  justifica en ningún sitio por qué no usa deep learning.**
- Las citas que falten se repasarán **en una tarea aparte**, sobre el Word entero.

## Regla que aprendió por las malas (aplicarla al capítulo 6)

Al enunciar la regla anti-fuga, **no ampliarla**. El perímetro real es cerrado:
D2 es intocable para **entrenamiento, hiperparámetros, balanceo y umbrales** —
esas cuatro y nada más. Escribir "ni en la selección de modelos" contradice
literalmente la excepción declarada de las tres decisiones tomadas mirando D2.
Esa lista de cuatro debe decir lo mismo en **3.3.2, 4.6 y 5.0**.

## Cómo re-extraer el .docx

```bash
cd "C:/Users/francisco.lopez/KIKO_TFG/Working_Directory"
python <scratchpad>/extract.py "Proyecto_Fin_de_Grado-FJLM-2026.docx" salida.md
```
El script recorre `word/document.xml`, convierte estilos Heading/Título a `#`,
marca las imágenes como `[IMAGEN]` y las tablas entre `[TABLA]`/`[/TABLA]`.
Si no existe, se reescribe en 30 líneas con `zipfile` + `xml.etree`.

## Estado al cerrar la sesión

Los capítulos 1-5 están aplicados y verificados en el .docx. Quedaban cuatro
detalles menores de maquetación que Francisco dijo haber arreglado: el pie de la
Figura 5.11 y su imagen duplicada, la lista de cuatro en 4.6, 21 wikilinks
`[[...]]` sin convertir, y la posición de los pies de 5.1 / 5.5 / 5.6.
