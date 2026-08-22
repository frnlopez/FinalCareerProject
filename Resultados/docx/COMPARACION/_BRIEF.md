# Encargo comun a los 6 agentes de comparacion

## Objetivo
Francisco esta pasando a limpio su memoria en Word. Quiere saber QUE SE ESTA
DEJANDO POR EL CAMINO y con que gravedad, para no saltarse nada importante.

## Los dos lados
- LIMPIO (destino, incompleto): `Resultados/docx/COMPARACION/docx_limpio.md`
  (conversion pandoc de `Proyecto_Fin_de_Grado-FJLM-2026.docx`, 2364 lineas).
- ACTUALIZADO (fuente de verdad): `Resultados/docx/memoria_completa_20260822-154416_fd089cc-sucio.md`
  (volcado del vault de hoy, 5017 lineas). Si necesitas contexto que el volcado
  no traiga, puedes abrir la nota original en `Obsidian_TFG_Vault/`.

## REGLAS DURAS
1. **Solo lectura.** No edites NI el .docx, NI su conversion, NI el volcado, NI
   ninguna nota del vault. Tu unica escritura es tu fichero de salida.
2. **NADA de diff palabra por palabra.** Francisco lo ha pedido explicitamente.
   Compara a nivel de CONTENIDO Y ARGUMENTO: que idea, que justificacion, que
   dato, que decision de diseno esta en el actualizado y no ha llegado al
   limpio. Un parrafo reformulado que dice lo mismo NO es una diferencia.
   Diferencias de maquetacion, orden de frases, sinonimos y estilo: IGNORAR.
3. **Es un RESUMEN analitico, no un inventario exhaustivo.** Agrupa: si faltan
   seis parrafos que sostienen un mismo argumento, es UNA diferencia, no seis.
   Apunta a ~10-25 entradas para tu bloque, no a 200.
4. **No inventes.** Si no puedes localizar algo, dilo.

## Taxonomia (decidida por Francisco hoy)
GRAVEDAD, una sola por entrada, excluyente:
  [C] CONTRADICE        - esta en el limpio pero afirma algo distinto de lo
                          actualizado (cifra vieja, umbral cambiado, tesis
                          que el vault ya retiro). ES LA MAS PELIGROSA.
  [B] FALTA-BLOQUEANTE  - sin esto, lo que YA esta en el limpio no se entiende
                          o queda sin justificar.
  [R] FALTA-RECOMENDABLE- complementa lo que ya hay; se echa de menos.
  [P] FALTA-PRESCINDIBLE- se puede omitir sin dano real.
  [D] SOLO-EN-DOCX      - esta en el limpio y el actualizado ya NO lo tiene
                          (o lo contradice por obsoleto). Puede ser un borrado
                          deliberado suyo en Word: no asumas que es un error.

FLAGS, cero, uno o dos por entrada, ortogonales a la gravedad:
  [PROFESOR] - responde a una peticion explicita del profesor o de la propia
               revision de Francisco. **SOLO si es trazable** a
               `mis-apuntes-del-informe.md` o a una ficha de `features.md`
               (S1-S15 cap.3, D1-D18 caps.4-6, rejilla 2.1.6.4, recortes).
               Si no lo puedes trazar, NO pongas el flag. Nada de intuiciones.
  [CIFRA]    - hay un numero, metrica, umbral o recuento en juego.

## Formato de cada entrada
### [GRAVEDAD][flags] <seccion> - <titulo corto de la diferencia>
**Que pasa:** 1-3 frases, a nivel de idea.
**Por que importa:** 1-2 frases. Que se rompe o que se pierde si no entra.
**Donde encaja en el limpio:** ancla TEXTUAL (titulo de seccion + frase literal
  junto a la que va). NUNCA numero de pagina ni de linea.
**Material:** de donde sacarlo en el actualizado (seccion + primeras palabras).
  Si es corto y autocontenido, pega el texto listo para copiar.

## Salida
Escribe UN solo fichero: `Resultados/docx/COMPARACION/parcial_<TU_LETRA>.md`
Empieza con 3-6 lineas de "veredicto del bloque" (estado general del limpio en
tu tramo) y luego las entradas ordenadas por gravedad: C, B, R, P, D.
