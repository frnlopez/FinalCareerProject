# features — tareas del TFG

> **Registro operativo.** Aquí vive lo que está **abierto** ahora mismo y lo que se ha
> **cerrado**, con el commit que lo hace durable. Es lo primero que lee el `leader` en cada
> mensaje.
>
> - `next-steps.md` queda **congelado en cuanto a casillas**: su §1-§5 es historial y su §6 es
>   la especificación técnica de cada script, que sigue vigente como referencia **salvo §6.5
>   (`hibrido.py`), superada por el grill H-1…H-7 de `resumen-de-decisiones.md`** — no calibrar
>   `UMBRAL_CONF` con el método de §6.5. Ya no se marcan tareas allí.
> - `resumen-de-decisiones.md` sigue siendo el registro de **decisiones de diseño**.
> - Lo mantiene el agente `cronista`, disparado por el skill `cierre`. **Estar en Abiertas
>   significa estar abierto**: una tarea aceptada la borra el usuario, nadie más.
>
> **Refactorización integral autorizada por Francisco el 2026-08-13.** Excepción **puntual** al
> invariante de edición quirúrgica del `cronista`: se reorganizó y compactó el fichero entero para
> eliminar contradicciones acumuladas por capas. **No es precedente.** El histórico retirado vive en
> git, en el commit anterior a este ciclo (último commit: **`9d4c26d`**, con el estampado de ese hash
> en su ficha cerrada encima, sin commitear). **No existe `features-historico.md` y no se crea.**

Estados: `[ ]` pendiente · `[~]` en curso · `[!]` bloqueado
Fechas absolutas `AAAA-MM-DD`. Track: **Código** / **Informe**.

---

## PRÓXIMOS PASOS — próxima sesión

> ### ⚡ EMPIEZA POR AQUÍ — apunte de traspaso del 2026-08-16
>
> **CAPÍTULO 2: CERRADO** (Tanda 11 — `d31e20f`, `296de24`, `2c5e36e`). Prosa completa, auditado en
> dos pases, figura del NIDS embebida. ~~**Solo le falta el pase de citas del `researcher`.**~~
> **— HECHO el 2026-08-16 (TANDA 13). El capítulo 2 no tiene ya ningún `[CITA: …]` pendiente.**
>
> **TANDA 12 (capítulo 3) — PARCIAL, commiteada en `669fd9f`. NO está cerrada.**
> Hecho: `3.3` de cuatro apartados a dos (45→34 líneas), con la formulación canónica del *data
> snooping* reproducida **literal**; `3.2`, `3.4`, `3.5` y `3.6` con recorte **y** contenido nuevo a la
> vez —por eso **crecen en neto**, que es lo esperado—; `2.3.3` retocada; y **81 líneas de decisiones
> técnicas** nuevas en `resumen-de-decisiones.md`, fechadas y reversibles como exige la delegación.
>
> **Verificado a mano desde el hilo principal** (la auditoría no corrió): **cero `[n]` inventados** en
> el capítulo 3 y **cero wikilinks rotos** — todos los destinos existen en disco.
>
> **ESTADO A 2026-08-16 DE ESTA LISTA DE CUATRO: los puntos 1 y 3 están HECHOS — NO se vuelven a
> despachar.** La **auditoría corrió** (`APTO CON CAMBIOS`, 10 hallazgos, ninguno 🔴; **9 aplicados**
> por cuatro redactores en paralelo) y el **ancla de `2.3.3` se verificó y era correcta**. **Siguen
> vivos los puntos 2 y 4.** Detalle en `## Cerradas`, filas del 2026-08-16.
>
> **⚠️ CADUCADO EL 2026-08-17 — ESTA LISTA DE CUATRO NO DEJA NADA VIVO. NO SE VUELVE A DESPACHAR.**
> Verificado contra disco: **los cuatro puntos están hechos.** El **2** lo cerró la **TANDA 19**; el
> **1** y el **3**, el **2026-08-16**; y el **4 lo cerró T9 hoy, 2026-08-17** (su ficha cerrada está en
> `## Cerradas`). Se conserva el texto **solo como historial**: no leas de aquí trabajo pendiente.
>
> **LO QUE FALTA PARA CERRAR LA TANDA 12, por orden:**
> 1. **LA AUDITORÍA, que NO corrió.** Es lo que decide si el capítulo 3 es revisable. **Foco propio de
>    un recorte, que la verificación mecánica NO cubre: que ninguna afirmación se haya quedado
>    HUÉRFANA** —lo que se quita de un sitio tiene que seguir vivo en su sede canónica—.
> 2. ~~**Completar el barrido de solapes del capítulo 2**~~ → **HECHO Y CERRADO en la TANDA 19
>    (2026-08-17):** 12 notas revisadas, 6 solapes corregidos. **Ya se pueden escribir las remisiones
>    del 3 al 2.**
> 3. **Confirmar si se reconsideró el ancla de `2.3.3:91`** al renumerar el capítulo 3. Era el punto 3
>    del encargo y no consta que se cerrara.
> 4. Comprobar contra el informe `99 Investigación/Datos repetidos en el capítulo 3.md` (`3fadf13`)
>    **qué solapes de los 15 quedan sin aplicar**. `3.1` no se tocó — puede ser correcto (`3.1.5` es
>    nueva y está exenta), pero hay que confirmarlo.
>
> **DESPUÉS de cerrar la 12:** el **pase en serie del `researcher`**, que cubre de una vez los
> `[CITA: …]` del capítulo 2 y los del 3. Se aplazó a propósito para **no tocar `Bibliografía.md`
> dos veces**. **— EJECUTADO el 2026-08-16 como TANDA 13. NO se vuelve a despachar**: 36 marcadores
> convertidos, **cero `[CITA: …]` vivos en la memoria**, y `Bibliografía.md` tocada una sola vez,
> absorbiendo también el Hallazgo 10 y el descuadre 36/33. Detalle en `## Cerradas`.
>
> > **⚠️ TRAZA HISTÓRICA — SUPERADA. Ni el «`[68]`» de abajo ni el «`[74]` / 72 filas» de la Tanda 13
> > son vigentes: el valor de HOY (2026-08-17, tras el pase en serie del `researcher`) es
> > **`[1]`–`[8]` + `[10]`–`[77]`, 76 filas, `[9]` quemada, primer libre `[78]`**, contado contra
> > `Bibliografía.md` y fijado en `CLAUDE.md`. No leas de aquí el contador.**
> > **CENSO CONTADO CONTRA DISCO AL CERRAR LA SESIÓN (2026-08-16), no recordado.** El primer `[n]`
> > libre **sigue siendo el `[68]`** (máximo dado de alta: `[67]`) — la Tanda 12 **no dio de alta
> > ninguna entrada**, coherente con que no se inventó ningún `[n]`.
> > **Líneas con `[CITA: …]` pendientes: 37**, así repartidas — `2.1.1`=3, `2.1.3`=4, `2.1.4`=16,
> > `2.1.5`=8, `2.2.4`=3 (**34 en el capítulo 2**), `3.2`=1, `3.5`=2 (**3 en el capítulo 3**).
> > **No son 33**: esa cifra venía de antes de la Tanda 11 y ya está caducada. **Ojo**: son LÍNEAS,
> > no marcadores —alguna línea lleva dos—, y los `[CITA:` de `4.2` (1) y `Bibliografía.md` (2) son
> > **prosa sobre la conversión**, no marcadores pendientes: no los cuentes.
> > **Recuéntalo antes de empezar**, no lo leas: `grep -rc "\[CITA:" --include=*.md Obsidian_TFG_Vault`.
> >
> > **ACTUALIZACIÓN DEL 2026-08-16, tras aplicar la auditoría de la TANDA 12 — contado contra disco:
> > las líneas con `[CITA: …]` bajan de 37 a 36** (**34 en el capítulo 2**, **2 en el capítulo 3**).
> > **Bajó una al unificar la sede de Kim et al.**, no porque se convirtiera ningún marcador. **El
> > primer `[n]` libre SIGUE SIENDO EL `[68]` y `Bibliografía.md` sigue en 66 entradas**: la Tanda 12
> > no dio de alta ninguna. **El «37» de arriba queda como traza, no como recuento vigente.**
> > **⚠️ Y esta actualización también quedó superada horas después: la TANDA 13 convirtió los 36 y
> > dio de alta `[68]`–`[73]` (`[74]` / 72 filas). **Eso TAMPOCO es vigente**: hoy son 76 filas y el
> > primer libre es el `[78]`.**
> >
> > **ACTUALIZACIÓN DEL 2026-08-16, tras la TANDA 13 (pase en serie de citas) — TODO ESTE CENSO QUEDA
> > COMO TRAZA: los 36 marcadores están CONVERTIDOS y quedan CERO `[CITA: …]` vivos en la memoria.**
> > `Bibliografía.md` pasa a **72 filas** y **el primer `[n]` libre es el `[74]`** — ver el bloque
> > «CONTADOR GLOBAL DE CITAS», que es el único sitio donde se mantiene la cifra. Los `[CITA:` que
> > queden en disco son **prosa sobre la convención** (`4.2` ×1, `Bibliografía.md` ×7) o **informe**
> > (`99 Investigación/Reconstrucción…` ×11): **no los cuentes como pendientes.**
> >
> > **⚠️ AVISO PARA QUIEN VEA UNA CONTRADICCIÓN AQUÍ, PORQUE NO LA HAY.** Este «cero» del 2026-08-16
> > es cierto **en su fecha**, y una ficha cerrada del **2026-08-17** registra el cierre de **tres
> > `[CITA: …]` vivos**: no se contradicen. La **TANDA 17 redactó el capítulo 5** e introdujo tres
> > marcadores nuevos (`5.0:160`, `5.1:86`, `5.4:78`) —lo correcto: ningún redactor inventó un `[n]`—
> > y el pase en serie del `researcher` del 2026-08-17 los convirtió. **Estado de hoy, contado contra
> > disco: CERO marcadores pendientes en la memoria.** El contador de `[CITA:` no es monótono: baja al
> > convertir y **sube cada vez que se redacta prosa nueva**. Se recuenta, no se arrastra.
>
> ---
>
> ### Apunte de traspaso anterior — del 2026-08-15
>
> **TANDA 11 — CERRADA el 2026-08-15 en DOS commits: `d31e20f` (redacción + creación de la figura) y
> `296de24` (embebido de la figura + auditoría aplicada). CON ELLA SE CIERRA EL CAPÍTULO 2 ENTERO y
> con él la FASE 4 del plan de cierre.** `2.1.5 Métricas` completada al nivel de `A.2` (**cierra T8**);
> `2.1.1`–`2.1.4` y `2.2.1` pasan de apuntes a prosa de memoria; **la figura del diagrama de bloques
> del NIDS existe, es reproducible (`Implementacion/app/figura_nids_bloques.py`) y está embebida en
> `2.2.2`**, con lo que cae su `[!todo]`. **Cierra además T24, T25 y la ficha de las 7 correcciones de
> la Tanda 5.** Detalle en `## Cerradas`. **Lo que deja vivo: dos fichas nuevas** —el pase en serie
> del `researcher` (33 `[CITA: …]` + 3 arreglos en `Bibliografía.md`) y los **pies de figura de los
> capítulos 4 y 5**— y **el recuento de `00 Índice TFG.md`, que YA SE PUEDE CUADRAR** porque su
> condición era que acabase la Fase 4.
>
> **Los tres `[!todo]` que quedan en el capítulo 2 son MARCAS DELIBERADAS, no huecos: no se
> «arreglan».** Los de `2.2.4:109`, `2.2.5:76` y `2.3.3:159` **ya no existen**.
>
> **TANDA 10 — CERRADA ENTERA el 2026-08-15, sus DOS piezas: A en `55ef3c6` y B en `3fadf13`.**
> El «PIEZA B PENDIENTE» que este bloque decía **ya no es vigente**: se escribió en el ciclo siguiente
> al corte de API. Detalle en `## Cerradas`. **⚠️ CADUCADO EL 2026-08-17: T9 ESTÁ CERRADA (`198fab6`),
> así que los dos «ejecuta / se reconsidera» que este bloque escribe EN PRESENTE ya ocurrieron.**
> **Lo que la Tanda 10 dejó vivo (historial): T9 ejecuta el recorte**
> (instrucciones en `99 Investigación/Datos repetidos en el capítulo 3.md`, anotadas dentro de su
> ficha) y **tres hallazgos laterales con ficha propia** en `## Abiertas`.
>
> **Pieza A (hecha):** `3.1.5 Modelo de amenaza` añadida —adversario en las seis dimensiones y por
> qué no hay experimento adversario—, cerrando los tres `[!todo]` de `6.1:75`, `A.3:52` y `A.3:647`.
> **Con esto queda desbloqueado el cierre del capítulo 2**, que remitía dos veces a `3.1`.
> Decisión técnica delegada y registrada: **`2.3.3:91` NO se repunta al ancla `3.1.5`** —se deja el
> wikilink a nota, que es la convención del vault—, porque **T9 va a renumerar el capítulo 3** al
> aplicar el recorte. Se reconsidera después de T9. **— T9 CERRADA el 2026-08-17 (`198fab6`): esa
> reconsideración ya no está «después», está VENCIDA. Si no consta hecha, se recuenta contra disco
> antes de darla por resuelta.**
>
> **Pieza B (HECHA, `3fadf13`):** el **análisis de datos repetidos del
> capítulo 3**, que Francisco encarga expresamente a los agentes y que su **profesor motivó** al pedir
> recortar y unificar «los primeros apartados del Capítulo 3». **Fue ANTES de T9**, para no redactar y
> luego tirar. Entregable, entregado: `99 Investigación/Datos repetidos en el capítulo 3.md`, **513
> líneas**, con los **15 solapes verificados** y, para cada uno, si se recorta / unifica / remite y
> **dónde queda la versión canónica**. **No ejecuta el recorte** — eso es T9.
> **Barrido inicial de este bloque, YA VERIFICADO Y CORREGIDO por el informe — se queda CORTO y se lee
> solo como historial: el *data snooping* está en 10 sitios, no 6.** Decía así:
> `3.3.4 Protocolo de evaluación común` enuncia
> entero el *data snooping* de las tres decisiones y **lo mismo está en `4.3`, `6.1`, `5.1`, `5.2` y en
> la nueva `5.0`** (seis sitios; **`5.0` la creamos nosotros en la Tanda 7, así que parte de la
> duplicación es propia**) · `3.3.2` duplica `4.3.2` · `3.3.1` duplica `4.2`/`4.3` · `3.4.2` y `3.5.2`
> anticipan `4.4`/`4.5` · `3.5.4` duplica el experimento de `4.3.4`.
> **Criterio de reparto a contrastar:** el **cap. 3 dice QUÉ y POR QUÉ** (diseño); los **caps. 4 y 5
> dicen CÓMO y QUÉ SALIÓ** (parámetros y cifras). Lo que en el 3 tenga detalle o números → **remisión**.
> Modelo a imitar: **`3.1.5` ya lo hace bien** — dice «no se repite aquí» y remite a `2.3.3`.
>
> **El árbol está LIMPIO. Tandas 6, 7 y 8 cerradas y commiteadas.** La sesión se cortó por **límite
> de API** (se reajusta a las 15:30, Europe/Madrid), no por ningún problema del trabajo.
>
> **LA TANDA 9 (pase de citas del `researcher`) ESTÁ EJECUTADA Y COMMITEADA el 2026-08-15 en
> `e286cce`.** El intento anterior se despachó y no escribió nada; **este sí**. Detalle en
> `## Cerradas`.
>
> ### ⛔ CONTADOR GLOBAL DE CITAS — el dato con riesgo real de este fichero
>
> **ESTADO VIGENTE A 2026-08-17, DESPUÉS DEL PASE EN SERIE DEL `researcher` — contado contra disco
> por el `researcher` y RECONTADO al cerrar, las dos cuentas coinciden: `Bibliografía.md` tiene
> **76 FILAS**, rango `[1]`–`[8]` y `[10]`–`[77]`, con **`[9]` SIGUE QUEMADA** (retirada sin
> renumerar). **EL PRIMER `[n]` LIBRE ES EL `[78]`.** Las dos altas nuevas del pase son
> **`[76]`** Quiñonero-Candela *et al.* (MIT Press, 2009) y **`[77]`** Hindy *et al.* (2020).
> **Todo lo que este fichero diga más abajo sobre «74 filas» o «primer libre `[76]`» es TRAZA
> HISTÓRICA, no recuento vigente.**
>
> **Estado a 2026-08-16, después de la TANDA 13 — SUPERADO, se deja como traza: contado contra disco, no recordado:
> `Bibliografía.md` tiene 72 FILAS, `[1]`–`[8]` y `[10]`–`[73]`, con `[9]` QUEMADA. EL PRIMER `[n]`
> LIBRE ES EL `[74]`.** Las seis altas nuevas de la Tanda 13 son las **`[68]`–`[73]`**. **Todo lo que
> este fichero diga más abajo sobre el `[68]` o sobre «66 entradas» es TRAZA HISTÓRICA, no recuento
> vigente.**
>
> **Estado a 2026-08-15, después de la TANDA 9 — SUPERADO, se deja como traza: `Bibliografía.md` tiene 66 entradas, `[1]`–`[8]` y
> `[10]`–`[67]`, con `[9]` QUEMADA (retirada sin renumerar, `396e283`). EL PRIMER `[n]` LIBRE ES EL
> `[68]`.** Las diez altas nuevas de la Tanda 9 son las **`[58]`–`[67]`**.
>
> **El rango se CUENTA, no se recuerda:** `grep -oE '^\| *\[[0-9]+\]' Bibliografía.md`. **Ya ha ido
> mal DOS VECES el mismo día (2026-08-15):** `leader.md` decía `[11]` cuando el libre era el `[58]`,
> y este mismo bloque quedó diciendo `[58]` cuando ya era el `[68]`. Si esta cifra se queda
> desfasada, la próxima tanda arranca en el `[58]` y **machaca en silencio las diez altas de hoy**,
> que es justo el solape que el protocolo de citas existe para evitar.
>
> **El localizador de página NO consume número:** `[8, p. 45]` y `[8, p. 90]` son la misma entrada
> `[8]`. La columna «Localizador por uso» de `Bibliografía.md` ya existe desde esta tanda.
>
> **LO QUE ESPERA DECISIÓN DE FRANCISCO, aparcado:** las **5 citas no reconstruidas** —de `[27]`,
> `[28]` y `[44]` no se conoce ni la obra, así que **nunca podrán llevar libro+página**, lo que
> inclina a retirar la afirmación—; ~~**`[6]` Goodfellow**, dada de alta pero **huérfana en todo el
> vault** (depende de T24)~~ **— RESUELTO: anclada en la TANDA 11 (`296de24`) y las tres
> declaraciones falsas de orfandad retiradas de `Bibliografía.md` en la TANDA 13 (2026-08-16)**;
> **`[54]` Molnar**, con la **edición sin fijar** —**alcance reducido el 2026-08-16: ya no bloquea
> ningún localizador del capítulo 2**, ficha propia en `## Abiertas`—; la **edición de
> Stallings `[8]`** (4.ª vs 5.ª); ~~**`2.3.3:91`**, que remite el modelo de amenaza a `3.1`, vacía
> (declarado con `[!todo]` en tres notas)~~ **— RESUELTO el 2026-08-15 en la TANDA 10 pieza A
> (`55ef3c6`): `3.1.5` escrita y los tres `[!todo]` retirados**; y el **borrado físico de `03 Desarrollo/`**, que no tiene
> permiso concedido.
>
> **Lo único que tiene que hacer Francisco: `! git push origin develop`.** Van **setenta y cinco** commits
> sin subir —**verificado con `git rev-list --count origin/develop..develop` el 2026-08-17, no contado
> a mano**—, **más el commit que lleva esta misma línea**, que por construcción no puede contarse a
> sí mismo: **SETENTA Y SEIS al cerrar el pase en serie del `researcher`**. **Esta cifra se RECALCULA, no se
> incrementa**: estuvo congelada en «cuarenta y siete» desde el 2026-08-15 mientras el repo seguía
> acumulando commits. Falla por autenticación desde el harness, no
> desde su máquina.
>
> **Este número se recalcula, NUNCA se incrementa a mano.** Ha ido mal dos veces (llegó a decir
> «quince» arriba y «catorce» abajo en el mismo fichero): cada tanda añade su commit **y** el del
> estampado, así que sumar de memoria falla siempre.
>
> **Las tres tareas cortas ya están repasadas y priorizadas. Se pueden despachar tal cual, sin volver
> a analizar nada:**
>
> | # | Tarea | Track / agente | Coste | Ojo con |
> |---|---|---|---|---|
> | **1** | **`00 Índice TFG.md`**: dar de alta **`A.3`** en `:92-93` (hoy solo lista `A.1` y `A.2`) y corregir `:101-102`, que dice que `03 Desarrollo/` «contiene solo avisos de migración» | Informe · `redactor-tfg` | Minutos | **NO tocar el «de 43 notas» de `:104`** — se cuadra al final, cuando la Fase 4 haya movido el reparto redactadas/guion. Hacerlo hoy es escribir una cifra que la primera tanda del cap. 2 vuelve a falsear |
> | **2** | **QUINTO re-anclaje de sello: `6bb224c-sucio → 1cb5c26`**. Tres puntos ya localizados: `PIPELINE.md:1332`, `PIPELINE.md:1454-1458`, `A.3:609-612` | Código · `ml-implementador` | Minutos de escritura, **pero arrastra pase obligatorio de `auditor-ml`** | **El sello impreso DENTRO del artefacto no se toca** (lo estampa `config.commit_actual()`). Misma forma que los cuatro anteriores. El hash `1cb5c26` está **verificado con git**, no inventado |
> | **3** | **T25** — tres correcciones de una línea: `Bibliografía.md:32`, `:86` y `Auditoría de Bibliografía.md:140` | Solo `researcher` | Minutos | **No se despacha sin que Francisco lo pida explícitamente.** El anclaje de `[6]` en `2.1.4` **NO es esto**: exige redactar el bloque de redes neuronales, que es Fase 4 |
>
> **Recomendación: 1 y 2 en el mismo ciclo.** Tocan ficheros distintos, así que van en paralelo, cierran
> dos fichas con un solo commit de tanda, y el pase de `auditor-ml` que el re-anclaje exige de todas
> formas aprovecha para auditar la coherencia entre ambas.
>
> **ESTADO A 2026-08-14: las tareas 1 y 2 de esa tabla están HECHAS — se despacharon como TANDA 3, en
> paralelo y con un solo commit** (ver `## Cerradas`). **No se vuelven a despachar.** De la tabla
> **solo sigue viva la 3 (`T25`)**, que además **no se despacha sin que Francisco lo pida**. Lo que
> dejan pendiente: el **borrado físico** de `03 Desarrollo/` (necesita shell) y la cifra de `:104`,
> intacta a propósito hasta la Fase 4.
>
> **Dato verificado en disco el 2026-08-14, para que nadie lo repita:** `Obsidian_TFG_Vault/03 Desarrollo/`
> **existe pero está VACÍA**, y git no la trackea (git no versiona directorios vacíos). Un `Glob` sobre
> ella sale vacío y **eso no prueba que no exista**. Si se quiere borrar la carpeta física hace falta un
> agente con shell: el `redactor-tfg` no tiene.
>
> **Lo que PARECE de minutos y no lo es** (ya medido, no volver a evaluarlo): ~~las figuras de
> `assets/`~~ **HECHO Y CERRADO el 2026-08-15 (`8976944`): copiar en la Tanda 7, embeber en la
> Tanda 8. Ya NO es dependencia de T10 ni cuello de nada** — barrido contra disco: 35 ficheros en
> `assets/`, 23 embebidos, y las 12 restantes son las `_122_sin_seleccion`, que `4.2:120` declara
> deliberadamente no publicadas; **T21** (sus destinos son `5.4`, territorio de T11, y el
> inventario de T6, que no existe); **T19** (hay que regenerar cada cifra desde `Resultados/` y envolverla
> en la salvedad de la dispersión 4,8×).
>
> **Bloqueado por dependencia, no por olvido:** **T4** no se puede cerrar — su único consumidor vivo es
> **T11** (Fase 5); T7 ya lo consumió. Y la **Fase 4** (las 8 notas del cap. 2, en tandas de 3-4 en
> paralelo) es el grueso real que mueve el TFG, pero no es material de «pocos minutos».

> Derivado del «Plan de cierre» de más abajo. **Orden de ejecución, no estado**: lo abierto sigue
> siendo lo que está en `## Abiertas`.

> **Dónde queda el 2026-08-14: la Fase 0 está CERRADA.** Francisco tomó el **2026-08-14** las **ocho
> decisiones** que quedaban (ver `## Cerradas`, ocho filas de esa fecha; contenido en **`ff54553`** y
> estampado de sus hashes en **`9077500`**). **El cuello de botella declarado del plan desaparece**: a
> partir de aquí todo lo abierto es despachable por agentes, salvo lo que la Fase 6 y la bibliografía
> Zotero/IEEE reservan a Francisco.
>
> **Y la Tanda 1 de la Fase 1 queda EJECUTADA y COMMITEADA** en **`cd407b1`** —el **primer commit por
> tanda** bajo la Decisión 7—, más el commit que estampa ese hash en las ocho filas de `## Cerradas` y
> que, por construcción, no lleva hash propio en este fichero. El detalle está en el bloque de la
> **Tanda 1**, más abajo: no se repite aquí. **Lo único vivo de esa tanda es `T25`**, en serie y solo
> `researcher`. El árbol queda **limpio**.
>
> **Y la Tanda 2 de la Fase 2 queda EJECUTADA y COMMITEADA el 2026-08-14 en `1cb5c26`** —el **segundo
> commit por tanda** bajo la Decisión 7—: `A.3` creada (T7), reconciliación de sellos y **cuarto
> re-anclaje** (`ddade37-sucio → 9d4c26d`) escritos. El detalle está en el bloque de la **Tanda 2** y
> en `## Cerradas`. **Ese commit arrastró además los tres ficheros que venían sin commitear de
> sesiones anteriores** —`Implementacion/app/agregar_semillas.py`,
> `Resultados/dispersion_semillas.csv` y `Resultados/dispersion_semillas.md`—, nombrados en su cuerpo
> para que no entraran de tapadillo. **`1cb5c26` es el commit que habilita el QUINTO re-anclaje**, el
> del sello `6bb224c-sucio`, que sigue abierto.
>
> **La sesión siguiente arranca por la Tanda 3.** De la Tanda 2 quedan vivos `T25`, el alta de `A.3`
> en `00 Índice TFG.md` y los dos `> [!todo]` internos de `A.3`.
>
> **Dónde quedó la sesión del 2026-08-13.** De las decisiones, la **1 (rango
> de FPR)** y la **3 (automatizar el «13 de 98»)** están **resueltas**, y la **Tarea B queda APLICADA**
> (`c5ceca5`). **La Fase 4 ya NO está bloqueada por el andamiaje**: la prohibición derogada seguía viva
> en `leader.md` y se retiró el 2026-08-13 (`0fb5f2b`) — era la razón estructural de que las 8 notas
> del capítulo 2 llevaran semanas en guion. La Fase 4 se ejecutará en **tandas de 3-4 notas en
> paralelo**.
>
> **El `push` está PENDIENTE.** Con hash y sin subir van **once**: `ea35ce3`, `dbba05e`, `ddade37`,
> `9d4c26d`, `0fb5f2b`, `6bfc779`, `c5ceca5`, `0dec53e`, los **dos de la Fase 0** — `ff54553` (el
> contenido) y `9077500` (el estampado de sus hashes) — y **`cd407b1`, el commit de la TANDA de la
> Fase 1** (2026-08-14), que es el **primer commit por tanda** bajo la Decisión 7. **A esos se suman
> dos que ya existen y tampoco están subidos**: `1d2a7dd` (el estampado de `cd407b1` en las ocho filas
> de `## Cerradas`) y `6bb224c` (el registro del cierre de sesión del 2026-08-14). Van **trece**,
> **verificado con `git log origin/develop..develop`, no contado a mano**. **A esos se suma
> `1cb5c26`, el commit de la TANDA 2** (2026-08-14), **`e38429b`, `49b210b` y `6bb224c`** (los
> estampados y el cierre de sesión de ese día) y **`cbdd084`, el commit de la TANDA 3**. **El recuento
> al cerrar la Tanda 3 fueron DIECISIETE**, verificado con `git rev-list --count origin/develop..develop` el
> 2026-08-14, más el commit que estampó `cbdd084`, que por construcción no podía llevarlo aquí:
> **dieciocho**. **Ese «dieciocho» YA NO ES VIGENTE** —el vigente son los **treinta y cuatro** de arriba,
> tomados el 2026-08-15 al cerrar la Tanda 8—. **Las cifras «once», «trece» y «catorce» de este párrafo son la traza histórica de
> cómo fue creciendo, no recuentos vigentes** — el número que vale es el de arriba, y se recalcula con
> git, nunca a mano. En este fichero no se escribe ningún hash
> inventado. Sigue fallando por **autenticación desde el harness**, así que **el `push` lo tiene
> que lanzar Francisco**.

**Tanda 0 — YA NO EXISTE: las ocho decisiones están tomadas (2026-08-14).** Se deja la línea para que
nadie la busque. Lo que dejan como **precondiciones vivas de otras tandas**, y que no está en ninguna
de las tandas de abajo:
- **Andamiaje del hilo principal — los tres ítems quedan APLICADOS.** Comprobado **contra disco el
  2026-08-14**: el registro decía «pendiente» cuando ya estaba hecho, es decir, la divergencia iba
  **al contrario** de la habitual. Se deja escrito, no borrado, porque el defecto reincidente del
  proyecto es que regla vigente y práctica divergen en silencio.
  - **Commit por tanda — APLICADO.** `CLAUDE.md` §Git, **línea 239**: «Un **commit por tarea
    cerrada, o un commit por tanda paralela** nombrando en el cuerpo las fichas que cierra», con el
    razonamiento de la **Decisión 7** al lado (granularidad ficticia: los 3-4 agentes de una tanda
    terminan sobre el mismo estado del árbol) y fechado 2026-08-14.
  - **Permiso ACOTADO de `ml-implementador` — APLICADO.** `.claude/agents/ml-implementador.md:63`:
    «En `resumen-de-decisiones.md` solo **añades nota fechada**, nunca reescritura».
  - **Marcado de fuentes sin acceso — APLICADO.** `.claude/agents/redactor-tfg.md:28` lleva el
    callout `> [!warning] Verificación pendiente — sin acceso al texto completo`, y `:41` el
    criterio «no verificable sin acceso institucional; no sostiene ninguna afirmación del trabajo».
  - **Por tanto la Fase 4 ya NO tiene precondición de andamiaje pendiente.** No se cita hash para
    estos tres: son andamiaje aplicado en commits ya existentes, y aquí se verifican por fichero y
    línea.
- **La Fase 6 se lleva los tres `grill-me`** (`2.1`, revisión del profesor, `1.4`) y va **detrás de
  absolutamente todo**.

**Tanda 1 — barrido de correcciones de una línea. EJECUTADA el 2026-08-14** (Fase 1 del plan de
cierre), en los **dos ciclos EN PARALELO** previstos, uno por track. Se deja la línea, como la Tanda 0,
**para que nadie la vuelva a despachar**: el detalle y la evidencia están en `## Cerradas`, en las
**ocho filas del 2026-08-14 con hash `cd407b1`** (cabecera de tanda, cinco fichas y dos hallazgos).
- **Código — HECHO:** `warnings.filterwarnings('ignore')` retirado de `program.py:12` y
  `validacion.py:57` (**`validacion.py:21` NO se tocó: es comentario**) + **nota fechada** en
  `resumen-de-decisiones.md:820-821`.
- **Informe — HECHO:** `4.2:105`, el **sello de `4.2:145`** (re-anclado a `9af842c`) y **T20**, que
  con esto **deja desbloqueada T9**. **No volver a mandar a nadie a corregir `4.2:105`: ya está
  corregido.**
- **Decisión 1 del FPR — APLICADA** en sus sitios: la cifra por variante (**10,2 % en 54 · 8,5 % en
  122**) sustituye al rango viejo en `4.2:120`, `A.2:69`, los dos comentarios de `validacion.py` y
  `GUIA_RESULTADOS.md`.
- **LO ÚNICO VIVO DE ESTA TANDA ES `T25`** — las tres correcciones de `Bibliografía.md:32`, `:86` y
  `Auditoría de Bibliografía.md:140`. Va **en serie y solo `researcher`**, que es el único que escribe
  ese fichero: **no se combina con ningún otro agente ni entra en tanda paralela.**
- **Observación de registro, anotada y NO resuelta aquí:** **`T20` nunca tuvo ficha `- [ ]` propia** en
  `## Abiertas` —vive como la **viñeta `3.5` dentro de T9**—, pero este bloque y el «Plan de cierre»
  la nombran como si fuera independiente. Resolverlo es **decidir cómo se fichan las sub-tareas**, y
  eso no se decide en un cierre: queda apuntado para que no se pierda.

**Tanda 2 — `A.3` y cierre de T4. EJECUTADA el 2026-08-14** (Fase 2 del plan de cierre). Se deja la
línea, como las dos anteriores, **para que nadie la vuelva a despachar**: el detalle está en
`## Cerradas`, en las filas del 2026-08-14 de esta tanda.
- **`A.3` (T7) — HECHA:** `Obsidian_TFG_Vault/Apéndices/A.3 Ficha del sistema.md`, *model card*
  completa, con la tabla de dispersión y sus salvedades. `auditor-ml`: **APTO CON CAMBIOS**, 8
  hallazgos, ninguno crítico, **todos corregidos**.
- **Reconciliación de sellos y CUARTO re-anclaje (`ddade37-sucio → 9d4c26d`) — HECHOS** en
  `Implementacion/PIPELINE.md` y `Resultados/GUIA_RESULTADOS.md`.
- **T4 NO se cierra todavía:** su consumidor vivo es **T11** (`5.2`/`5.4`), que sigue abierto.
- **Vivos de esta tanda:** `T25` (en serie, solo `researcher`), el **alta de `A.3` en
  `00 Índice TFG.md`** (pase en serie sobre el índice) y los **dos `> [!todo]` internos de `A.3`**
  —los seis ítems no-FT de Pineau y la remisión a `5.0` (T5)—, más el **quinto re-anclaje**, el del
  sello `6bb224c-sucio`, que ya **no** espera a nada: el commit de la Tanda 2 existe y es `1cb5c26`.
- **Estado a 2026-08-14: de esos vivos, el alta de `A.3` en el índice y el quinto re-anclaje quedan
  CERRADOS en la Tanda 3.** Siguen vivos `T25` y los dos `> [!todo]` internos de `A.3`.

**Tanda 3 — alta de `A.3` en el índice + quinto re-anclaje. EJECUTADA el 2026-08-14** (Fase 3 del
plan de cierre), **en paralelo, un track cada ficha y ficheros disjuntos**. Se deja la línea, como las
tres anteriores, **para que nadie la vuelva a despachar**: el detalle está en `## Cerradas`, en las
tres filas del 2026-08-14 de esta tanda.
- **Índice (Informe) — HECHO:** `A.3` dada de alta en `00 Índice TFG.md:92-93` con el formato de
  `A.1`/`A.2`, y corregida la frase falsa de `:101-102` sobre `03 Desarrollo/`. **El «de 43 notas» de
  `:104` se dejó intacto a propósito** (se cuadra en la Fase 4; el auditor confirmó que además cuadra
  con disco).
- **Quinto re-anclaje (Código) — HECHO:** `6bb224c-sucio → 1cb5c26` en `Implementacion/PIPELINE.md`,
  `A.3` y —**el fichero que el implementador se había dejado fuera**— `Resultados/GUIA_RESULTADOS.md`.
  Dos pases de `auditor-ml`, **APTO** tras aplicar hallazgos.
- **Vivos de esta tanda:** el **borrado físico** de `03 Desarrollo/` (necesita shell) y el recuento de
  `00 Índice TFG.md:104`, ambos con ficha propia abierta.
  **⚠️ 2026-08-17: el borrado físico YA ESTÁ HECHO** —la carpeta no existe en disco—, así que de estos
  dos **solo sigue vivo el recuento del índice**, y su alcance se ha **ampliado a nueve sitios** (ver
  «Altas del pase de registro — 2026-08-17»).
- **ABIERTO Y A CRITERIO DE FRANCISCO, no despachado:** el callout «**Punto actual**» de
  `00 Índice TFG.md:8` **no menciona `A.3`**, pero está **fechado el 2026-07-16**, así que es
  **historial** y la recomendación fue **no tocarlo**.

**Tanda 4 — prosa del bloque `2.2` completo. EJECUTADA el 2026-08-14** (arranque de la **Fase 4** del
plan de cierre), con **4 redactores en paralelo, un fichero cada uno**. Se deja la línea, como las
cuatro anteriores, **para que nadie la vuelva a despachar**: el detalle está en `## Cerradas`, en las
filas del 2026-08-14 de esta tanda.
- **Cubre 4 de las 8 notas del capítulo 2**, todas en
  `Obsidian_TFG_Vault/02 Marco Teórico/2.2 Ciberseguridad/`: `2.2.2`, `2.2.3`, `2.2.4` y `2.2.5`.
- **T8 entra en la misma pasada, pero SOLO su parte de `2.2.3`/`2.2.4`** — los cuatro sentidos de
  «híbrido» (el TFG usa el (a)), que Khraisat et al. 2019 no taxonomiza lo híbrido, y el linaje
  ADAM 2001 / Tombini 2004. La **definición canónica de «híbrido»** queda fijada en callout
  `[!important]` de `2.2.3`, y es la que referencia el resto del capítulo.
- **Decisión 8 APLICADA en `2.2.4`:** término canónico «semisupervisado (one-class)», sin
  reintroducir «no supervisado».
- **Proceso:** 4 redactores → auditoría de coherencia entre notas → 3 correctores en paralelo →
  segunda auditoría → 1 corrección residual. **Dos pases de `auditor-ml`, ambos cerrados sin ningún
  🔴.**
- **VIVO Y CON FICHA: las 4 notas restantes del capítulo 2** — `2.1.6`, `2.3.1`, `2.3.2` y `2.3.3`
  (esta última con la carga T8 de P9/P10 y el modelo de amenaza). Van en la **Tanda 5**.
- **VIVO dentro de `2.2.2`:** un `> [!todo]` por el **diagrama de bloques del NIDS**, que va a
  `assets/` — ~~mismo cuello que las figuras de `assets/` que ya bloquean T10~~. **CORREGIDO el
  2026-08-15: ese cuello YA NO EXISTE** (la ficha de las figuras de `assets/` está cerrada en
  `8976944`). **El cuello real de este `[!todo]` es otro y hay que decirlo bien: la figura del
  diagrama de bloques NO EXISTE todavía en `Resultados/`**, así que no es «copiar y embeber» como
  aquellas, sino **crearla primero**. Merece ficha propia; no la hereda de una ficha ya cerrada.
  **CERRADO el 2026-08-15 en la TANDA 11** (`d31e20f` + `296de24`): la figura se **creó** con
  `Implementacion/app/figura_nids_bloques.py` (reproducible), se copió a `assets/` **byte-idéntica** y
  se **embebió en `2.2.2` con pie**, retirando el `[!todo]`. **No se vuelve a encargar.**
- **AVISO QUE TIENE QUE SOBREVIVIR AL PASE EN SERIE DEL `researcher`:** las citas nuevas quedan como
  `[CITA: …]`, **cero `[n]` nuevos y ningún `[n]` preexistente renumerado**; y **Anderson 1980 ya es
  `[2]` y Denning 1987 ya es `[3]`**, así que en ese pase hay que **MAPEAR, no dar de alta**.

**Tanda 5 — prosa de las 4 notas restantes del capítulo 2. EJECUTADA el 2026-08-14** (cierre de la
**Fase 4** del plan de cierre). Se deja la línea, como las cinco anteriores, **para que nadie la
vuelva a despachar**: el detalle está en `## Cerradas`, en las filas del 2026-08-14 de esta tanda.
- **Con ella el capítulo 2 queda en 8 de 8**: `2.1.6 Metodologías y buenas prácticas`,
  `2.3.1 IA, ML y Deep Learning`, `2.3.2 La IA en ciberseguridad` y
  `2.3.3 Límites y consideraciones éticas`. **La ficha de la prosa de las 8 notas queda CERRADA.**
- **INCIDENTE QUE TIENE QUE QUEDAR ESCRITO, porque el patrón se repetirá: el agente que despachaba
  la tanda MURIÓ POR LÍMITE DE SESIÓN DE LA API después de terminar la redacción y ANTES de
  reportar.** Se retomó en un segundo ciclo. **Ninguna nota quedó truncada** —verificado
  explícitamente por `auditor-ml`: las cuatro cierran su última sección (`2.1.6` «Relación con otras
  notas», `2.3.1` §2.3.1.5, `2.3.2` §2.3.2.6, `2.3.3` §2.3.3.8)—. Un pase de verificación dedicado
  murió además por un **529 del servidor**, y su cometido lo cubrió el propio `auditor-ml`. **Regla
  que se deriva: un agente que muere por límite deja el trabajo HECHO EN DISCO y NINGÚN reporte, así
  que lo primero al retomar es COMPROBAR TRUNCAMIENTO, no relanzar.**
- **Lo que salió LIMPIO, que era el riesgo declarado de la tanda:** «híbrido» **no se redefine**
  (`2.3.1:11` y `2.3.2:55` remiten al callout canónico de `2.2.3:62-63`); «semisupervisado
  (one-class)» sin sinónimos contradictorios en las cuatro, coherente con
  `resumen-de-decisiones.md:463-467`; el «51» no aparece; **cero `[n]` nuevos** —el único es `[3]`
  en `2.3.2:36`, correctamente mapeado a Denning 1987, y `[9]` no reaparece—; todas las rutas y
  cifras verificadas contra disco.
- **La Decisión 4 NO está sobreaplicada aquí** (comprobado contra `99 Investigación/`): el problema
  es **el contrario**, faltan marcadores en `2.3.3` y `2.3.1`. Es la asimetría de la corrección 4.
- **SE COMMITEA CON 7 CORRECCIONES ABIERTAS, por decisión de Francisco:** el trabajo estaba escrito
  y **sin respaldo en git tras un corte por límite**, así que se prioriza preservarlo. Las 7 están
  dadas de alta en `## Abiertas`, en dos fichas. **Los puntos 4, 5 y 7 son CROSS-FILE y ACOPLADOS:
  NO se paralelizan** —exigen un redactor **en serie** con las cuatro notas en contexto—. La
  corrección se despacha **inmediatamente después** de este commit.
- **PROCEDE AHORA el pase EN SERIE del `researcher`** para convertir los `[CITA: …]` a `[n]`: es la
  dependencia declarada del final de cada fase, y esta fase cierra aquí.
- **VIVO y NO cerrado: T8.** Su viñeta `2.3.3` (P9/P10 y modelo de amenaza) entra en esta tanda y
  queda hecha, pero **`2.1.5` sigue siendo un stub sin tocar** — ver la nota en su ficha.
- **Dato aparte, NO versionado y SIN ficha:** apareció sin trackear
  `Obsidian_TFG_Vault/APUNTES SOBRE CS229 STANFORD ML LECTURES/` con un único `Lecture 1.md`
  **vacío**. Material propio de Francisco; se decidió **no versionarla** (un fichero vacío no
  preserva nada). **No se toca.**

---

## Abiertas

### 📊 TRIAJE DE LAS FICHAS ABIERTAS — por qué NO se lanzan todas (2026-08-18)

**Motivo del apunte:** Francisco preguntó por qué no se despachan de golpe todas las fichas
abiertas. La respuesta es que **no son trabajo homogéneo**. Recuento contado contra disco hoy:
**35 fichas con `[ ]`** (`grep -c '^- \[ \]' features.md`) — pero ese recuento **infravalora el
total**, porque solo cuenta los bullets `[ ]`. El inventario completo de `## Abiertas`, verificado,
es de **51 bullets-ficha: 35 con `[ ]`, 2 con `[~]` y 14 con `[x]`** (ver el **apartado D**).
Reparto de las 35:

**A. Bloqueadas en una decisión de Francisco — 21 fichas. Ningún agente puede ejecutarlas.**
Líneas `:514`, `:556`, `:581`, `:589`, `:596`, `:603`, `:610`, `:631`, `:643`, `:690`, `:703`,
`:751`, `:766`, `:786`, `:790`, `:945`, `:1456`, `:2052`, `:2058`, `:2065`, `:2071`.
**`:1456`/T14 entró en este grupo, no en el C.** Por la **DECISIÓN 4 de la Fase 0 (Francisco,
2026-08-14)** la ficha cambió de naturaleza: dejó de ser «cerrar las verificaciones por criterio»
y es hoy un **inventario de puntos que Francisco revisará él en la revisión final del informe**.
**No está caducada y no es ejecutable por un agente.**
Son de tres clases: (1) datos bibliográficos que **no se pueden establecer sin inventarlos**
(ediciones de `[8]` y `[54]`, versión de la CCN-STIC-401 `[10]`, página de `[76]`, metadatos de
`[26]`, las 5 citas colgantes irreconstruibles, los tres anclajes de `2.1.4`/`2.1.5`);
(2) **autorizaciones de escritura** sobre ficheros cuyo permiso no está concedido
(`resumen-de-decisiones.md`, `CLAUDE.md`, tres docstrings de código publicados,
`next-steps.md:493`); (3) **decisiones de contenido** (figuras duplicadas, `4.6:24`,
`03 Desarrollo/`, el wikilink de `6.2`). Despacharlas no adelantaría nada: un agente solo podría
**inventar** el dato o **tocar sin permiso** el fichero.

**B. Informativas — 4 fichas. No hay nada que ejecutar.** `:649`, `:656`, `:662`, `:709`. Son
**anotaciones de método** (el `auditor-ml` no puede calcular `md5`, cómo se verificó la
intocabilidad de los artefactos) y constataciones de que unos `[!todo]` son correctos. Están
abiertas porque **solo Francisco las borra**, no porque falte trabajo.

**C. Ejecutables por agente — 10 fichas, y NO todas son sustancia.** `:547` (erratas de `1.1`),
`:618` (celda de `[76]` en `Bibliografía.md`, solo `researcher`), `:882` (`[54]` Molnar, **ya
decidida** el 2026-08-17, pendiente de aplicar), `:921` (patrón de referencias `fichero:línea`,
vigilancia, no acción), `:968` (diagrama de agentes, **la acepta o la retira Francisco**), `:976`
(**Preliminares, Fase 7 — sin dependencias desde hoy**), `:1548` (bloqueada en
acceso institucional a un PDF), `:1691`, `:1713`, `:1743`.
**Ninguna de ellas está caducada — verificado contra disco el 2026-08-18:**
- **`:1691`** (`1.4`, conceptos de IA): su **punto 2** (resúmenes escuetos) **sí** lo cubre la
  Fase B, pero su **punto 1** —«qué conceptos de IA entran de verdad en el capítulo 2»— **sigue
  vivo**, tiene **ALCANCE NO CERRADO** y es una **decisión de contenido que no puede tomar un
  agente**. Además Francisco ordenó el **2026-08-12** que esta ficha se ejecute **LA ÚLTIMA**,
  después de todas las demás.
- **`:1713`** (`2.1`, coherencia y densidad): **seis puntos de contenido vivos** salidos de
  `mis-apuntes-del-informe.md`, y **ninguno** lo resuelve el cierre del capítulo 2. Converge con
  `:1743`, y su **punto 6 es una decisión de densidad**.
- **`:1743`** (revisión del profesor: simplificar y desduplicar del capítulo 3 en adelante):
  sustancia, y también con **alcance no cerrado**.

**Conclusión que se registra:** «estaba todo resuelto» es **cierto en lo que importa** — los
capítulos 1 a 6 están redactados y el track de código está cerrado. Lo que queda abierto **no es
contenido faltante**: son **25 fichas de 35 que no son despachables por construcción**
(21 decisiones + 4 informativas), y de las 10 restantes las **tres de sustancia real**
—`:1691`, `:1713` y `:1743`— tienen **las tres el ALCANCE NO CERRADO** y exigen **`grill-me` con
Francisco antes de tocar una sola nota**. Por tanto **la única ficha de sustancia despachable HOY
sin interrogatorio previo son los Preliminares (Fase 7)**, acompañada de las tres mecánicas: las
erratas de `1.1` (`:547`), la celda de `[76]` en `Bibliografía.md` (`:618`) y la aplicación de
`[54]` Molnar (`:882`, ya decidida). El cuello de botella del proyecto **ya no es capacidad de
agente: son las decisiones de Francisco y la bibliografía en Zotero.** Y ni siquiera lo ejecutable
lo desbloquea del todo: **tres de las cuatro fichas grandes que quedan necesitan primero una
conversación con él.**

**D. Lo que el recuento de 35 NO cubría — 3 fichas más.** El triaje contó solo `[ ]`, y con eso se
quedaron fuera dos `[~]` con trabajo vivo y una `[x]` que se declara abierta en su propio cuerpo:

1. **`[~]` «`03 Desarrollo\` está vacía en disco y solo falta borrar la carpeta»:** la mitad de
   texto está hecha; **queda vivo el borrado físico de la carpeta**, que el `redactor-tfg` **no
   puede ejecutar porque no tiene shell**. Necesita un agente con shell o a Francisco, y **el
   permiso de borrado concedido se limitó a `Lecture 1.md`**. Solapa con la ficha del grupo A sobre
   esa misma carpeta. **Decide Francisco.**
2. **`[~]` «Seis afirmaciones del vault que la TANDA 7 dejó desfasadas»:** cinco cerradas, **queda
   viva la 5** —los números de línea de **T25** están desplazados y hay que localizarlos **por
   contenido, no por línea**—. Es **ejecutable**, y es otra manifestación del patrón de la ficha
   `:921`.
3. **T23 sigue marcada `[x]` y su cuerpo se declara «CIERRE PARCIAL en la TANDA 25 — la ficha SIGUE
   ABIERTA», pero lo que ese cuerpo alega ya NO se sostiene.** Afirma que el párrafo de Snort de
   `1.2` sigue sin cita, y **en disco está citado con `[26]` desde el pase en serie del
   2026-08-18**: `01 Introducción/1.2 Preliminares.md`, **línea 32**, cierra el párrafo con `[26]`,
   y las líneas **34-39** llevan un callout `[!note] Sobre la fecha` que distingue el artículo de
   **LISA'99 (USENIX, nov. 1999)** de la publicación de la herramienta en **1998**. `[26]` **ya
   existía** desde la reconstrucción de las 47 citas colgantes, donde la usa `2.2.2`: se **MAPEÓ, no
   se dio de alta**, que es la disciplina correcta. Coincide con el bloque de este mismo fichero que
   ya declara **«P4 y P4-bis — CERRADAS el 2026-08-18»**.
   **Lo único que mantiene viva a T23 son P5 y P6**, que son **decisiones de Francisco** (edición de
   `[8]` Stallings y versión de la CCN-STIC-401 `[10]`) y que **ya están fichadas por separado en el
   grupo A**. Luego **T23 no aporta trabajo nuevo: es un duplicado que apunta a dos fichas del
   grupo A.**
   **La lección de método es lo que vale:** el cuerpo de T23 fue la **sexta ocurrencia del patrón de
   la ficha `:921`** —un registro que afirma en presente algo que el disco ya desmiente—, y esta vez
   **mordió al propio triaje**. Se detectó porque **se verificó contra `1.2` antes de repetirlo**.

**Consecuencia sobre el grupo C:** las fichas mecánicas que acompañan a los Preliminares **siguen
siendo TRES** —las erratas de `1.1`, la celda de `[76]` en `Bibliografía.md` y la aplicación de
`[54]` Molnar—: la aplicación de P4 **no se suma**, porque ya está en disco. **Una
ficha marcada `[x]` que se declara abierta en su cuerpo es invisible a `grep '^- \[ \]'`: ese es el
fallo de método que este addendum corrige.**

**Fichar no es resolver: este addendum no corrige nada.**

**Fichar no es resolver: este bloque no corrige nada.**

> ⚠️ **Las referencias `fichero:línea` de este bloque apuntan al estado del documento ANTES de
> insertarlo.** Al escribirse al inicio de `## Abiertas`, el bloque desplazó ~45 líneas hacia abajo
> todo lo que numera, incluidas sus propias citas. Es **exactamente el patrón de la ficha `:921`**:
> **cada ficha se localiza por su TÍTULO, no por su número de línea.**

> **El 🟡 «`PIPELINE.md` llama determinista a un recuento que se apoya en `ac496cb`» queda CERRADO en
> la TANDA 19** (2026-08-17). Su ficha vive ya en `## Cerradas`. **Ojo: la palabra sigue viva FUERA
> de `PIPELINE.md`, y eso es ficha NUEVA, más abajo.**

> ### 🧾 CÓMO SE BUSCAN LOS HASHES EN ESTE DOCUMENTO — no es una foto del árbol
>
> **Este bloque ya no afirma en presente que el árbol esté limpio, y el cambio es deliberado.**
> Lo afirmó en su forma anterior y **mintió en las dos tandas del 2026-08-17**, no por descuido de
> nadie: se escribía al cerrar una sesión declarando un estado que **el primer cierre de la tanda
> siguiente invalidaba**. Era un artefacto que se autoinvalidaba por construcción, así que se
> sustituye por el **procedimiento**, que no caduca:
>
> - **El estado real del árbol se consulta con `git status`, nunca aquí.**
> - **Una fila con `` `—` `` en la columna Commit significa que su commit no existía cuando el
>   `cronista` la escribió.** El skill `cierre` lo estampa justo después, en un segundo commit. Si
>   encuentras un `` `—` ``, mira si hay un commit posterior que lo cubra antes de suponer que el
>   trabajo no está versionado. Localízalas con `grep -n '| `—` |$' features.md`.
> - **Las nueve filas de julio con `` `—` `` NO están pendientes**: son anteriores al versionado del
>   proyecto y **no van a recibir hash nunca**. No las busques.
>
> **Ciclos del barrido**, cada uno con su commit de trabajo y su commit de estampado. La lista se
> **añade por abajo** al cerrar cada tanda; no se reescribe:
>
> - **2026-08-17:** **`822e4c5`/`15665ae`** · **`198fab6`/`785fb40`** · **`8b5ce15`/`ac36b88`** ·
>   **`312c179`/`7f2645a`** · **`5c2a484`/`f9d8ce4`** (TANDA 20, séptimo re-anclaje de sello) ·
>   **`1075dfd`/`db640be`** (TANDA 21, seis fichas).
> - **2026-08-18:** **`7029873`/`6f75fa2`** (TANDA 22, campo `estado:` en 26 notas) ·
>   **`02ff9fb`/`cb0b9e9`** (TANDA 23, estados y totales de `00 Índice TFG.md`) ·
>   **`6ada8c2`/`0fc77c9`** (TANDA 24, tres fichas: nomenclatura de Procedencia en `4.2`, remisiones a
>   `4.3.5` y la mitad de P9 en `5.4`) · **`babf9a6`/`77dd5b1`** (TANDA 25, pies de figura de los capítulos 4
>   y 5, cierre parcial de T23 y residuos de `A.3`) · **`c7ab48d`/`bcb78a7`** (TANDA 26, cierre de
>   T17: bloque de decisiones en los cuatro informes de `99 Investigación/` y deriva de `evaluacion.py`) ·
>   **`2172b42`** (andamiaje, hilo principal: `assets/` documentada en `CLAUDE.md` y la fila de
>   `evaluacion.py` rehecha con las seis funciones de T1) · **`5ebf8f9`** (**FASE A — pase EN SERIE del
>   `researcher`**: cierra P4, P4-bis, P5, P6, el desdoble de `[76]`, **T16 por agotamiento** y **T23**,
>   con **CERO altas de `[n]`** —76 filas antes y después, primer libre `[78]`— y el «37 en D2» de los
>   dos informes reetiquetado a **37/163/200/52**. Deja **cinco decisiones de Francisco** bloqueadas)) · **`3203420`/este mismo** (**FASE B — EL CAPÍTULO 1**, fin del barrido: `1.0`, `1.2`, `1.3` y
>   `1.4` redactadas, más `6.1` realineada a los nueve objetivos y el estado de `00 Índice TFG.md`
>   corregido. **Cero `[n]` y cero `[CITA: …]` nuevos**).
>
> **Y del día anterior solo queda un 🟠 abierto:** el de **las 5 citas colgantes irreconstruibles**
> (ficha más abajo, alta del 2026-08-15). Es **el único 🟠 que viene de antes de hoy** — los demás 🟠
> que aparecen en `## Abiertas` nacieron el 2026-08-17.

### Altas del pase de registro — 2026-08-17

> **Ocho fichas que hasta ahora solo existían en la conversación.** Se ponen en disco porque hoy han
> caído cinco agentes por límite de API: **lo que no está aquí se vuelve a preguntar.** Ninguna se
> cierra —**ninguna está ejecutada**— y **ninguna mueve una cifra publicada.** **Fichar no es
> resolver: aquí no se ha corregido nada.**

> **El 🟠 «SÉPTIMO re-anclaje de sello — y lo generó el ciclo de Código de HOY» queda CERRADO en la
> TANDA 20** (2026-08-17): re-anclado **en prosa** en `4.2` y `4.3`, con el sello impreso dentro de los
> artefactos de `Resultados/` **intacto**, como manda la regla. Su ficha vive ya en `## Cerradas`.

- [ ] 🟠 **`resumen-de-decisiones.md` contradicho EN SILENCIO por el ciclo de Código del 2026-08-17** · Informe · **decide Francisco**, ejecuta `redactor-tfg` o `cronista`
  Alta el **2026-08-17**. El fichero **sigue afirmando en presente lo contrario de lo que hay en
  disco**: `:825-826` y `:894-895` («lo que hay hoy en disco es `a8c20e9-sucio`, común a las dos
  variantes») y `:1460` («sigue vivo el otro re-anclaje pendiente… el de la re-corrida de
  `validacion.py`»). **En disco el sello es `ac36b88` LIMPIO y ese pendiente está CERRADO.**
  `PIPELINE.md`, `GUIA_RESULTADOS.md` y `features.md` sí se actualizaron; **el fichero de decisiones,
  no.** **BLOQUEADA esperando autorización de Francisco:** el permiso concedido sobre ese fichero cubre
  **solo la línea `:103`** (el `~52`). **Vía propuesta: añadir nota fechada sin reescribir el texto
  previo**, la misma disciplina del «~17» y del residuo de T22.

> **El 🟡 «Imprecisión NOMINAL en `4.2`, callout de Procedencia» queda CERRADO en la TANDA 24**
> (2026-08-18): la nota cita ya los campos literales `Commit del código:` y `Fecha de la corrida:`,
> verificados contra las cabeceras de los dos `Resultados/*_validation_report.txt` (sello `ac36b88`).
> Su ficha vive ya en `## Cerradas`.

> **El 🟠 «Deuda de CIFRA en `5.4:129` — las dos celdas de KNN del eje SMOTE-vs-nada» queda CERRADO en
> la TANDA 21** (2026-08-17): volcadas a `5.2` §5.2.4.4 desde `Resultados/metricas_balanceo.csv`. Era
> **la última deuda de dato real del vault**. Su ficha vive ya en `## Cerradas`.

> **El 🟡 «El capítulo 1 es el hueco de completitud que queda, y solo está fichado EN PARTE» queda
> CERRADO en la FASE B DEL BARRIDO — CAPÍTULO 1** (2026-08-18): reescritas `1.0 Sinopsis` y
> `1.3 Objetivo`, desarrollados los cinco desafíos de `1.2 Preliminares` y rehecha `1.4 Estructura`.
> Su ficha vive ya en `## Cerradas`.

> **El 🟡 «`1.4 Estructura` omite el capítulo 6 entero y atribuye mal las conclusiones» queda CERRADO
> en la FASE B DEL BARRIDO — CAPÍTULO 1** (2026-08-18): los tres defectos verificados en disco, más
> la errata «evolución»→«evaluación» y el `estado:` a `redactada`. Su ficha vive ya en `## Cerradas`.

### Altas de la FASE B del barrido — capítulo 1 · 2026-08-18

> Dos fichas, **ninguna bloqueante**, **ninguna mueve una cifra publicada**. **Fichar no es resolver:
> aquí no se ha corregido nada.**

- [x] ~~🟡 **Erratas de estilo en `1.1 Motivación`** · Informe · `redactor-tfg`~~
  **CERRADA el 2026-08-18 en la TANDA 27.** Su fila vive ya en `## Cerradas`. Se corrigieron **las 4
  erratas fichadas más 4 del mismo tipo** halladas al pasar; **sin tocar cifras ni citas**.
  Alta el **2026-08-18**. `1.1` es la **única nota del capítulo 1 que no se ha tocado** en esta tanda
  (su única ficha, la del dato agregado de INCIBE en `1.1:12`, ya estaba ejecutada). Erratas
  verificadas: **`:10`** «dominan **las** titulares» (concordancia: *los* titulares); **`:14`** «por
  **consecuente**» (debe ser *por consiguiente*); **`:18`** «**En cuestión al** objetivo de este
  proyecto» (giro incorrecto) y «mejoran la capacidad de detección de ataques **y a que** cada vez sea
  más fácil» (sintaxis rota). **Fichada, no arreglada**: no estaba en el alcance de la Fase B y **no se
  abre alcance por cuenta propia**.

- [ ] 🟢 **Dos peticiones de Francisco de `mis-apuntes-del-informe.md` quedan RESUELTAS por esta tanda** · Informe · **verificar con Francisco**
  Alta el **2026-08-18**. `mis-apuntes-del-informe.md:11` («ese resumen de cada capítulo es
  excesivamente escueto, ofrecer una propuesta más completa») lo cumple la **reescritura de `1.4`**; y
  `:9` («en el 1.4 digo que el capítulo 2 son 3 bloques… ¿qué conceptos de IA estoy incluyendo?
  ¿ninguno?») queda contestado: **`1.4:14` nombra ya los tres bloques** y el vault **sí tiene** el
  bloque de IA, con `2.3.1`, `2.3.2` y `2.3.3`. **Queda para que Francisco lo dé por bueno**: no se
  marca aceptada.

> **El 🟡 «El campo `estado:` del frontmatter está sin mantener y MIENTE» queda CERRADO en la TANDA 22**
> (2026-08-18): resincronizadas **26 notas** de `borrador` a `redactada`. Su ficha vive ya en
> `## Cerradas`. **Efecto colateral esperado: `00 Índice TFG.md` queda desfasado — ficha nueva más
> abajo.**

### Altas del pase en serie del `researcher` — 2026-08-18

> **Cinco decisiones que SOLO puede tomar Francisco, más un 🟡 de coherencia.** El `researcher`
> **marcó en vez de inventar**, que es la disciplina correcta. **Las cinco quedan BLOQUEADAS a la
> espera de él**: no hay nada que un agente pueda ejecutar. **Ninguna es bloqueante para el resto del
> trabajo** y **ninguna mueve una cifra publicada.** **Fichar no es resolver: aquí no se ha corregido
> nada.**
>
> **Contador verificado contra disco en el mismo pase: 76 filas antes y 76 después, `[1]`–`[8]` +
> `[10]`–`[77]`, CERO altas, `[9]` sigue quemada, ningún `[n]` renumerado. El primer libre sigue
> siendo el `[78]`.**

- [ ] 🟡 **Edición de `[8]` Stallings: 4.ª (2018) vs 5.ª (2023)** · Informe · **BLOQUEADA — decide Francisco, con el libro delante**
  Alta el **2026-08-18**. La entrada queda **⚠️ EDICIÓN NO ESTABLECIDA**. Las dos ediciones coexisten
  (Pearson 2018, ISBN 978-0-13-479410-5 · Pearson 2023, ISBN 978-0-13-809167-5) y **el texto del TFG no
  discrimina**: los tres usos de `2.2.1` viven en el **cap. 1, §1.1**, sección presente en todas las
  ediciones. Se declaró expresamente que **no se elige la 4.ª «por ser la más difundida»**: eso sería
  inventar un dato bibliográfico. `[8]` es uno de los 8 libros con **localizador obligatorio**, así que
  su página depende de esta decisión.

- [ ] 🟡 **Versión, fecha y URL del PDF de la CCN-STIC-401 `[10]`** · Informe · **BLOQUEADA — decide Francisco**
  Alta el **2026-08-18**. El enlace ya **no** apunta al término suelto del visor HTML, sino a la **ficha
  oficial de la guía**. Lo que **no se ha podido verificar, y está marcado**: `WebFetch` da **403**, el
  navegador real da **403 contra un test anti-bot** y la ruta del PDF da **503**. **No se ha inventado
  ninguna URL de descarga.** **Versión y fecha siguen sin fijar** (un comunicado del CCN-CERT habla de
  1.069 términos: dato de segunda mano y sin verificar).

- [ ] 🟡 **Página exacta dentro del cap. 1 de `[76]` (Storkey)** · Informe · **BLOQUEADA — decide Francisco**
  Alta el **2026-08-18**. **El rango del capítulo SÍ está establecido y verificado: pp. 3-28**, contra el
  registro institucional del autor (University of Edinburgh Research Explorer), coincidente con MIT
  Press Scholarship Online. **El punto exacto de la afirmación dentro de ese rango, no**: MIT Press
  devuelve 403. Anotado de paso: **el desdoble de `[76]` sigue disponible** si Francisco acepta
  repuntar `5.1:86` a un `[78]` — con los datos ya en la fila es un cambio de dos líneas.

- [ ] 🟡 **Metadatos de `[26]` (Roesch, LISA'99) contra la fuente viva** · Informe · **BLOQUEADA — decide Francisco**
  Alta el **2026-08-18**. USENIX devuelve **403** a todo acceso automático, PDF e índice. **Se conservan
  los metadatos de la reconstrucción previa y NO se han reinventado.** Anotada también la aparente
  discrepancia de fecha, que **no es un error**: la nota dice **1998** (publicación de la herramienta) y
  el artículo es de **1999**; ambas son correctas, y la nota lo explica en un callout sin reescribir la
  prosa.

- [ ] 🟡 **¿Recuperar la frase sobre Anderson en `1.2:14`?** · Informe · **BLOQUEADA — decide Francisco**
  Alta el **2026-08-18**. La afirmación de que «la literatura del área señala de forma recurrente a
  Anderson (1980) como el punto de partida de la detección de intrusiones» **se retiró del cuerpo** por
  falta de aval de nivel 1: **Khraisat *et al.* 2019 `[31]` no menciona a Anderson** (verificado sobre
  el PDF del editor) y **Yost 2016** (*IEEE Annals of the History of Computing*, DOI
  10.1109/MAHC.2015.41, metadatos verificados en Crossref) **está tras muro de pago**. **Basta con
  acceso al Yost o a otra revisión de nivel 1 para recuperarla: sería la PRIMERA ALTA del `[78]`.**

- [ ] 🟡 **La celda de `[76]` en `Bibliografía.md` se contradice a sí misma** · Informe · `researcher`
  Alta el **2026-08-18**, detectada al verificar el pase. La celda contiene **a la vez** la marca antigua
  «⚠️ Página exacta NO ESTABLECIDA … el rango del capítulo no se ha podido verificar» **y, más abajo, el
  rango pp. 3-28 ya verificado**. La marca vieja **no se retiró**: solo se dice al final que «decae para
  el rango». **Ficha: retirar o reescribir la marca antigua en un próximo pase del `researcher`**, que es
  el único agente que escribe `Bibliografía.md`.

### Altas de la TANDA 26 — 2026-08-18

> Cinco fichas, **ninguna bloqueante**, **ninguna mueve una cifra publicada**. Salen del pase de
> `auditor-ml` (dos hallazgos 🟠 **no aplicados, y no por descuido**) y de lo que T17 dejó vivo al
> cerrarse. **Fichar no es resolver: aquí no se ha corregido nada.**

- [ ] 🟠 **La deriva de `evaluacion.py` quedó corregida en 2 de sus 4 sedes** · Informe · **decide Francisco / hilo principal**
  Alta el **2026-08-18**. T17 punto 2 enumeraba cuatro sedes: `CLAUDE.md`, `next-steps.md`,
  `resumen-de-decisiones.md` y `Guia_ML`. **La TANDA 26 hizo las dos últimas citadas.** **Siguen con el
  contrato pre-T1:** la fila de `evaluacion.py` en **`CLAUDE.md:64`** —«módulo común de métricas y
  figuras… `guardar_metricas` (CSV acumulado)», **sin esquema, sin procedencia, sin `metricas_tiempo`**;
  verificado: `CLAUDE.md` **no contiene** ni `metricas_tiempo` ni `COLUMNAS_MINIMAS`— y
  **`resumen-de-decisiones.md:88-92` (Q3)**. **No se tocaron a propósito:** `CLAUDE.md` es **andamiaje del
  hilo principal**, y sobre `resumen-de-decisiones.md` el permiso concedido **no cubre esto** (misma
  restricción que la ficha 🟠 de `features.md:506`). **Matiz verificado que ahorra trabajo:** Q3 define la
  superficie **por referencia a §6.5b**, que esta tanda **ya ha actualizado**, así que lo único desfasado
  ahí es su **enumeración entre paréntesis**. Es el defecto de «barrer la primera aparición, no todas».

- [ ] 🟡 **`resumen-de-decisiones.md:570-571` quedó contradicho por esta misma tanda** · Informe · **decide Francisco**
  Alta el **2026-08-18**. Dice **en presente** que «falta el bloque "Decisiones tomadas a partir de este
  informe" **en los cuatro informes**» y que falta la deriva de `evaluacion.py`. **Los cuatro bloques
  existen ya en disco desde hoy.** Una decisión cerrada **no se contradice en silencio**. **Vía propuesta,
  la de siempre: nota fechada sin reescribir el texto previo. Requiere autorización de Francisco.**

- [ ] 🟡 **Asimetría de remedio entre dos informes de la misma tanda** · Informe · **informativa**
  Alta el **2026-08-18**. Ante el mismo defecto —la frase caducada sobre `6.2`—,
  `aprendizaje-continuo:25` **conservó** la frase y la corrigió con un callout `[!info]` encima, y
  `clasificadores-tabulares:30-31` la **reescribió en línea**. **Las dos son honestas**; solo obliga a leer
  dos veces. El cuerpo de `aprendizaje-continuo` sigue diciendo «material para que Francisco escriba 6.2»
  en `:423` y `:529`, **cubierto por el callout**.

- [ ] 🟡 **Anotación de MÉTODO, no defecto: cómo se verificó la intocabilidad de los artefactos** · — · **informativa**
  Alta el **2026-08-18**. El `auditor-ml` **sigue sin poder calcular hashes** (su definición no incluye
  Bash), así que lo verificó **por contenido y por sello de procedencia**, no por `md5`. Es la **segunda
  vez** que se registra (la primera, TANDA 24). **Queda escrito cómo se verificó para que nadie lo lea como
  comprobación de hash.**

- [ ] 🟡 **Los cuatro informes dejan un `> [!todo]` cada uno, y son correctos** · — · **informativa**
  Alta el **2026-08-18**. Marcan **propuestas del informe sin decisión registrada** en lugar de
  inventarlas: la **etiqueta del `bin_accuracy` 0,8605 frente a H-6** (verificado: esa etiqueta **no está
  decidida en ningún sitio del repo**), los **10 candidatos de la tabla B**, la **fusión de peldaños de
  `6.2`**, el **análisis D1→D2** y la **dilución del término «híbrido»**. **No se resuelven aquí: son
  decisiones de contenido de Francisco.**

### Altas de la TANDA 25 — 2026-08-18

> Tres fichas, **ninguna bloqueante**, **ninguna mueve una cifra publicada**. **Fichar no es resolver:
> aquí no se ha corregido nada.**
>
> **RETIRADA el 2026-08-18 (misma fecha del alta): el alta sobre «`1.2:27` atribuye Snort a Roesch
> (1998) sin ninguna cita» era DUPLICADA, no un hallazgo nuevo.** Ya estaba fichada como **P4**
> (más abajo, «Altas del pase en serie del `researcher` — 2026-08-17»), que además tiene **decisión
> de Francisco del 2026-08-17**. Lo pendiente de Snort vive en P4 y **lo ejecuta el `researcher` en
> el pase en serie**. Quedan **dos fichas** en esta tanda.

- [x] 🟡 **`CLAUDE.md` no menciona `Obsidian_TFG_Vault/assets/` en la estructura del repo** · **CERRADA el 2026-08-18 en `2172b42`** (hilo principal). `assets/` está en el árbol y descrita con el censo verificado —**36 ficheros, 24 nombres distintos embebidos en 27 embebidos de 7 notas, 12 huérfanos, cero embebidos rotos**—, más el aviso de que las figuras se copian a mano desde `Resultados/figuras/` y por tanto **`assets/` no se regenera solo**. El «22 ficheros» que decía esta ficha era erróneo · — · **hilo principal**
  Alta el **2026-08-18**. Ahí viven los **22 ficheros de imagen** embebidos, **verificados en disco**
  durante la TANDA 25, y el árbol que documenta `CLAUDE.md` los omite: la estructura está
  **incompleta**. **Fichado, no arreglado**: `CLAUDE.md` es andamiaje y **lo toca solo el hilo
  principal**.

> **El 🟡 «Erratas en `1.2:14`» queda CERRADO en la FASE B DEL BARRIDO — CAPÍTULO 1** (2026-08-18):
> «trackeados» → «monitorizados y registrados» y «de como» → «de cómo», con **cero ocurrencias** de
> ambas en todo el vault verificado por `grep`. Su ficha vive ya en `## Cerradas`.

- [ ] 🟡 **Dos figuras duplicadas — decisión pendiente** · Informe · **decide Francisco**
  Alta el **2026-08-18**. `[!todo]` en **`4.3:306`** —las **Figuras 4.8 y 4.9** embeben los mismos
  ficheros que las **4.1 y 4.2** de `4.2`: `eda_distribuciones_divisiones.png` y
  `validacion_distribucion_clases.png`— y en **`5.3:155`** —`hibrido_cm_54.png` embebido **dos veces**,
  Figuras **5.11 y 5.12**—. Se numeraron como **instancias propias** para que ningún embebido quedara
  sin pie, pero **en el volcado al `.docx` la misma imagen aparecería dos veces con dos números
  distintos**. Resolverlo implica **tocar la prosa de dos notas**, y **excedía el alcance del pase**.

### Altas de la TANDA 24 — 2026-08-18

> Dos fichas, **ninguna bloqueante**, **ninguna mueve una cifra publicada**. **Fichar no es resolver:
> aquí no se ha corregido nada.**

- [ ] 🟡 **`4.6:24` roza fijar alcance propio** · Informe · **decide Francisco**
  Alta el **2026-08-18**. La nota declara «no fijar cifras ni alcance por cuenta propia» y **a
  continuación enuncia el veredicto cualitativo** «doble efecto beneficioso» / «mejor generalización».
  El `auditor-ml` lo dejó como **informativo**: es **criterio de Francisco** si se aplica el criterio
  estricto. **Fichada, no tocada.**

- [ ] 🟡 **Anotación de MÉTODO, no defecto: el `auditor-ml` no puede calcular `md5`** · — · **informativa**
  Alta el **2026-08-18**. Su definición **no incluye Bash**, así que la **intocabilidad de los
  artefactos** de la TANDA 24 la verificó **por contenido**, no por hash: las **cuatro tablas de
  métricas** siguen con **`semilla=42`** y **`commit=1163c90`** en todas sus filas, **sin filas del
  barrido**. Queda escrito **cómo se verificó** para que nadie lo lea como una comprobación de hash.

### Altas de la TANDA 22 — 2026-08-18

> **El 🟡 «`00 Índice TFG.md` publica estados desfasados tras la resincronización del frontmatter»
> queda CERRADO en la TANDA 23** (2026-08-18): el índice publica ya **40 `redactada` / 1 `borrador` /
> 2 `pendiente`**. Su ficha vive ya en `## Cerradas`.
>
> **Dos observaciones del `redactor-tfg` que NO se cierran y NO se resuelven aquí:**
>
> 1. **Aclaración, no defecto:** el frontmatter de `00 Índice TFG.md` sigue en `estado: borrador`, y
>    es **deliberado** — la nota de índice **no se cuenta entre las 43 notas de memoria**. Que nadie
>    lo lea como el 1 `borrador` pendiente ni lo «arregle».
> 2. **Correcto según las reglas del proyecto:** el listado del índice **sigue declarando las
>    reservas de revisión de Francisco** sobre `4.2` («Por qué se eligió NSL-KDD») y
>    `6.2 Líneas futuras` aunque **ambas notas ya sean `redactada`**. Esas dos revisiones son suyas
>    (CLAUDE.md, autoría de la redacción): **no es una incoherencia y no se toca.**

> **El 🟡 «AMPLIACIÓN de la ficha `00 Índice TFG.md`: desfasado en NUEVE sitios» queda CERRADO en la
> TANDA 21** (2026-08-17), y **eran QUINCE, no nueve**. Su ficha vive ya en `## Cerradas`, junto con la
> del recuento de `:106`.

> **El 🟡 «`A.3:648` — `[!todo]` "Qué faltaría para cerrarlo", sobre algo que NO se va a hacer» queda
> CERRADO en la TANDA 21** (2026-08-17): pasa a `[!warning]` de **límite declarado de alcance**. Su
> ficha vive ya en `## Cerradas`.

- [x] 🟡 **Tercera nota vacía del vault, ahora CON NOMBRE: `Lecture 1.md` (0 bytes)** · **CERRADA el 2026-08-18: BORRADA** con `git rm`, bajo la autorización expresa de Francisco del 2026-08-17. Su carpeta `APUNTES SOBRE CS229 STANFORD ML LECTURES/` queda vacía. **`03 Desarrollo/` NO se toca**: ese borrado no está autorizado · — · `cronista`
  Alta el **2026-08-17**. Es
  **`Obsidian_TFG_Vault/APUNTES SOBRE CS229 STANFORD ML LECTURES/Lecture 1.md`, 0 bytes**: ajena al TFG
  y **no indexada**. Es la **tercera «vacía»** que la ficha del recuento de notas contaba **sin
  nombrar**. Registrada solo para que deje de ser anónima: **qué se hace con ella lo decide Francisco**
  — está fuera del árbol de la memoria.

### Altas de la TANDA 21 — 2026-08-17

> Siete fichas, **ninguna bloqueante**, **ninguna mueve una cifra publicada**. **Fichar no es
> resolver: aquí no se ha corregido nada.**

- [ ] 🟠 **El `~52` tiene MÁS sedes fuera del vault de las que la ficha contaba — y TRES son código** · Código/Informe · **decide Francisco**
  Alta el **2026-08-17**. La ficha cerrada hoy cubría las cuatro sedes del vault y las tres de
  trazabilidad autorizadas. **Quedan SIN AUTORIZAR:** `Resultados\GUIA_RESULTADOS.md:497`, **cuatro
  líneas en `Guia_ML\*`**, `.claude\agents\ml-implementador.md`, `.claude\agents\auditor-ml.md` y
  **tres docstrings: `program.py:427`, `firmas.py:18` y `firmas.py:110`**. **Los tres docstrings son
  track Código sobre ficheros publicados: requieren autorización expresa de Francisco.** El permiso
  concedido cubría **solo** las tres sedes de `resumen-de-decisiones.md`/`next-steps.md`.

> **El 🟡 «Las nueve notas remitentes de `4.3.5` no declaran que remiten» queda CERRADO en la TANDA 24**
> (2026-08-18), **con dos correcciones a su propio enunciado**: la lista canónica de `4.3:266` da
> **diez sedes de remisión** (once contando la canónica), **no nueve** —la décima, `4.3.7`, vive dentro
> de la propia nota sede—; y **`2.1.6` ya declaraba la remisión** en `:94`, así que **no se le añadió
> línea** para no duplicar. Líneas de remisión añadidas en **7 notas**: `3.3:31`, `4.6:39`, `5.0:123`,
> `5.1:135`, `5.2:71`, `6.1:42`, `A.3:106`. Su ficha vive ya en `## Cerradas`.

- [ ] 🟡 **`03 Desarrollo/` SIGUE EXISTIENDO en disco, vacía — el registro la daba por caducada** · — · **decide Francisco**
  Alta el **2026-08-17**, verificado por el agente del índice: **la carpeta está ahí** y el aviso de
  eliminación **sigue vigente** en `00 Índice TFG.md`. **La ficha de este mismo documento la marcaba
  «CADUCADA el 2026-08-17» y eso es FALSO** (anotado en su sitio, más abajo). Es la **misma clase de
  divergencia registro↔disco** que ha mordido varias veces. **El permiso de borrado concedido se
  limitó a `Lecture 1.md`.**

- [x] 🟡 **«37 muestras en D2» mal atribuido en dos informes de `99 Investigación/`** · **CERRADA el 2026-08-18 en `5ebf8f9`**. Reetiquetado a **37 u2r de tipo conocido** (denominador del `f1_u2r`) frente a **200 en D2** = 37 + 163 0-day (denominador del recall 0-day) y **52 en D3**. Verificado en disco: la única ocurrencia que queda del literal es el callout que *narra* la corrección · — · `researcher`
  Alta el **2026-08-17**. `benchmark-comparativo-nsl-kdd.md:141` y
  `clasificadores-tabulares-y-arquitecturas-hibridas.md:364`. En **D2 completo son 200**; **37** es el
  soporte entre los **ataques de tipo conocido** (9.083). **No es memoria**, pero **`5.4` remite al
  primero** como «material de respaldo con las fuentes revisadas una a una», así que la corrección de
  la tanda **queda incompleta hacia abajo**. Esa carpeta es del `researcher`.

- [x] 🟡 **`Bibliografía.md` sigue anunciando `[76]` como primer número libre en CUATRO sitios** · **CERRADA el 2026-08-18 en `5ebf8f9`**. Las cuatro quedan tachadas y corregidas al `[78]`. Contado al commitear: **76 filas, máximo `[77]`, `[9]` ausente de la tabla** · Informe · `researcher`
  Alta el **2026-08-17**. `:55`, `:61`, `:87` y `:112` dicen `[76]`, mientras `:136` y
  `99 Investigación\Auditoría de Bibliografía.md:184` dicen **`[78]`, que es el valor real**. Es **el
  mecanismo exacto** por el que dos agentes acabarían asignando el mismo `[n]`. **Lo toca SOLO el
  `researcher`**, en el pase en serie.

- [ ] 🟡 **`6.2` enlaza `[[aprendizaje-continuo-nested-learning]]`, que vive en `99 Investigación/`** · Informe · **confirmar con Francisco**
  Alta el **2026-08-17**. Wikilink a un informe: **permitido**, pero al volcar a Word **apunta a algo
  que no es memoria**. Confirmar si se quiere así.

- [ ] 🟡 **`next-steps.md:493` mantiene `dos ~45,9k · probe ~11,7k · r2l ~1,0k` con virgulilla** · Informe · **decide Francisco**
  Alta el **2026-08-17**. La autorización de Francisco cubría **el `~52` de `u2r`**, y **se respetó el
  límite**. Ficha de una línea si quiere esa línea entera exacta (`45.927 / 11.656 / 995`).

### Altas del pase en serie del `researcher` — 2026-08-17

> **CUATRO decisiones que quedan para Francisco.** El `researcher` las **marcó en vez de
> inventarlas**, que es la disciplina correcta: la que no se puede establecer con honestidad se
> señala, no se rellena. **Ninguna es bloqueante** y **ninguna mueve una cifra publicada.**
> **Fichar no es resolver: aquí no se ha corregido nada.**
>
> **LAS CUATRO ESTÁN YA RESPONDIDAS — Francisco decidió el 2026-08-17, y en las cuatro eligió la
> opción recomendada.** Las fichas **siguen ABIERTAS**: falta **aplicarlas** en `Bibliografía.md` y en
> las notas, y eso lo ejecuta el `researcher` en un pase en serie. **Ya no hay nada que preguntar:
> quien las lea, las aplica.** La respuesta concreta va escrita dentro de cada ficha.

> **ENCARGOS ACUMULADOS PARA ESE MISMO PASE EN SERIE — añadidos el 2026-08-17 (TANDA 21), sin abrir
> tanda:**
> - **Identificar los seis ítems no-FT del checklist de `[20]`.** El `[!todo]` de `A.3.8` **queda
>   marcado a propósito**: el dato **no está en la nota** y **no se puede resolver sin inventarlo**. El
>   redactor reescribió el bloque separando **lo establecido de lo pendiente** y dejó constancia de que
>   **ninguna afirmación del apéndice depende de ese dato**.
> - **El arreglo de `Bibliografía.md` (`[76]`→`[78]`)** y **el «37 en D2» de los dos informes de
>   `99 Investigación/`** — fichas nuevas 5 y 4 de la TANDA 21, más arriba.

> **P4 y P4-bis — CERRADAS el 2026-08-18** en el pase en serie del `researcher`. `1.2:32` queda
> anclado a **`[26]`, que YA existía** (se MAPEÓ, no se duplicó), y la atribución historiográfica a
> Anderson de `1.2:14` se **RETIRÓ del cuerpo** por falta de aval de nivel 1. Sus fichas viven ya en
> `## Cerradas`. **Lo que dejan vivo son dos decisiones de Francisco**, fichadas más arriba.
> Se conserva el texto original de la ficha, tachado, por su historial de divergencias:

- [x] ~~🟡 **P4 · falta aval de nivel 1 para `1.2:14`** · Informe · **DECIDIDO — pendiente de aplicar** · ejecuta `researcher`~~
  Alta el **2026-08-17**. La afirmación de `1.2:14` no tiene hoy fuente primaria que la sostenga.
  O se ancla a un aval de nivel 1, o se reformula para decir solo lo que la fuente disponible
  respalda.
  **DECISIÓN DE FRANCISCO (2026-08-17): se ancla a la FUENTE PRIMARIA.** El párrafo de `1.2` sobre
  Martin Roesch y Snort (1998) se respalda con el paper original: **M. Roesch, «Snort — Lightweight
  Intrusion Detection for Networks», LISA'99, USENIX**. Razón registrada: es fuente primaria, del
  propio autor, del año que la nota cita, y USENIX la sirve **gratis y de forma estable** — el mismo
  criterio de nivel 1 que ya cumplen `[2]` Anderson y `[3]` Denning, **citadas en ese mismo pasaje
  mientras Snort se quedaba sin `[n]`**. Pendiente: alta en `Bibliografía.md` y marcador en `1.2:14`.
  **DIVERGENCIA REGISTRADA el 2026-08-18 (TANDA 25) — P4 SIGUE ABIERTA.** El agente de la Tanda 25
  **aplicó P4 sobre una afirmación distinta de la decidida**: en vez del pasaje de Roesch y Snort,
  avaló la de **Anderson como punto de partida de la detección de intrusiones**, dejando en `1.2:14`
  un `[CITA: revisión o survey del área que atribuya a Anderson (1980) el origen de los IDS]` con su
  `[!todo]`. Consecuencias:
  - **Lo aplicado NO es lo que Francisco decidió**; el anclaje al paper de Roesch **sigue sin hacerse**.
  - **El párrafo de Snort, hoy en `1.2:27`, sigue SIN NINGUNA CITA** — que era justo el objeto de la
    decisión.
  - Queda **una segunda afirmación sin aval** (la de Anderson), ya marcada con `[CITA: …]`, que **no
    estaba en ninguna ficha**. **Las dos** van al **pase en serie del `researcher`**.
  - **Referencia de línea desfasada:** la ficha apunta a `1.2:14` y el pasaje de Snort está en
    `1.2:27`. **Mismo patrón que ya ha mordido cuatro veces**: verificar la línea en disco antes de
    aplicar.

> **P5 y P6 — CERRADAS el 2026-08-18, y NO como se había decidido: se MARCARON, no se fijaron.**
> `[8]` Stallings queda **⚠️ EDICIÓN NO ESTABLECIDA** (la 4.ª de 2018 y la 5.ª de 2023 coexisten y el
> texto no discrimina: los tres usos viven en el cap. 1 §1.1, presente en todas las ediciones), y el
> enlace de `[10]` CCN-STIC-401 se sustituye por la **ficha oficial de la guía**, con lo no
> verificable marcado (403 anti-bot incluso con navegador real, 503 en la ruta del PDF) y **sin
> inventar ninguna URL**. Sus fichas viven ya en `## Cerradas`; **la versión y la edición pasan a ser
> decisión de Francisco**, fichadas más arriba.

- [x] ~~🟡 **P5 y P6 · dos ediciones/versiones sin fijar: Stallings `[8]` y CCN-STIC-401 `[10]`** · Informe · **DECIDIDO — pendiente de aplicar** · ejecuta `researcher`~~
  Alta el **2026-08-17**. **P5:** la edición de Stallings `[8]` sigue sin fijar (4.ª vs 5.ª) — y `[8]`
  es uno de los 8 libros con localizador obligatorio, así que la página depende de qué edición se
  elija. **P6:** la versión de la CCN-STIC-401 `[10]` tampoco está fijada. **Decide Francisco: no se
  inventa ninguna de las dos.**
  **DECISIÓN DE FRANCISCO (2026-08-17): las dos se fijan A LO QUE HAY EN DISCO.** **P5:** `[8]`
  Stallings a la **4.ª ed., Pearson, 2018** (ISBN 978-0-13-479410-5, que **ya consta** en la entrada).
  **P6:** `[10]` **CCN-STIC-401 a la versión que sirve hoy el CCN**, con **fecha de consulta**.
  Con esto **se desbloquea el localizador de `[8]`**, que dependía de la edición.

> **`[76]` — CERRADA el 2026-08-18, y el desdoble decidido se descarta CON RAZÓN ESCRITA y con la
> alternativa ejecutada.** Desdoblar exigiría **repuntar el marcador de `5.1:86`**, que no es mano del
> `researcher`, y dejaría `[76]` **huérfana** —justo lo que prohíbe la regla dura de T16—. En su lugar,
> la fila lleva ya **los datos completos del capítulo de Storkey, pp. 3-28**, verificados contra el
> registro institucional del autor: **la página deja de estar sin establecer a nivel de capítulo**. El
> desdoble sigue disponible si Francisco acepta repuntar `5.1:86`. Su ficha vive ya en `## Cerradas`.

- [x] ~~🟡 **`[76]` Quiñonero-Candela *et al.* · página del cap. 1 no establecida Y reserva de AUTORÍA** · Informe · **DECIDIDO — pendiente de aplicar** · ejecuta `researcher`~~
  Alta el **2026-08-17**, con el alta de la entrada. Son **dos cosas**: **(1)** la página exacta del
  capítulo 1 **no se pudo establecer** —MIT Press devuelve 403—, y **se marcó, no se inventó**;
  **(2)** la nota **atribuye el capítulo a los editores**, pero su autor es **Storkey**. Francisco
  decide si la referencia **se desdobla como capítulo** con su autor propio.
  **DECISIÓN DE FRANCISCO (2026-08-17): SÍ, se DESDOBLA como capítulo.** Forma acordada: **A. Storkey,
  «When Training and Test Sets Differ», en *Dataset Shift in Machine Learning*, J. Quiñonero-Candela,
  M. Sugiyama, A. Schwaighofer y N. D. Lawrence, Eds. Cambridge, MA: MIT Press, 2009.** Razón doble:
  es como **IEEE trata un capítulo de volumen editado**, y **el rango de páginas del capítulo sustituye
  a la página exacta** que MIT Press no deja verificar (403). Corrige además una **atribución falsa**:
  el capítulo lo escribió **Storkey**, no los editores.

- [x] ~~🟡 **`[54]` Molnar · edición sin fijar — NO SE TOCÓ en este pase** · Informe · **DECIDIDO — pendiente de aplicar** · ejecuta `researcher`~~
  **APLICADA Y CERRADA el 2026-08-18 en la TANDA 27**: la fila de `[54]` en `Bibliografía.md` queda
  fijada a la **2.ª ed., 2022**. Su fila vive ya en `## Cerradas`, igual que la ficha hermana de
  alcance reducido de más abajo.
  Anotado el **2026-08-17**. **No se duplica ficha: la suya vive más abajo, con el alcance ya reducido
  tras la Tanda 13.** Se registra aquí solo para que conste que el pase en serie **la dejó
  deliberadamente intacta**, por ser decisión de Francisco.
  **DECISIÓN DE FRANCISCO (2026-08-17): se fija a la 2.ª EDICIÓN, 2022** — la que cita la literatura,
  frente a la 3.ª que sirve hoy la web. **Con esto queda determinada su página** para el uso de
  `2.3.3`, que era lo único que la ficha reducida dejaba pendiente. **Al aplicarla, actualizar también
  el aviso de `CLAUDE.md` que la declara «sin fijar»** — pero eso lo decide quien mantenga ese fichero.

### Altas de la TANDA 19 — 2026-08-17

> Cinco fichas, **ninguna bloqueante**, **ninguna mueve una cifra publicada**. **Fichar no es
> resolver: aquí no se ha corregido nada.**

> **El 🟠 «El "8 de 10" PAREADO no lo emite ningún script» queda CERRADO el 2026-08-17**: lo emite
> ahora `agregar_semillas.py` en `Resultados/comparaciones_pareadas.csv`. Su ficha vive ya en
> `## Cerradas`.

> **El 🟡 «`~52` para un número que el script emite EXACTO» queda CERRADO en la TANDA 21**
> (2026-08-17): resuelto en las **cuatro sedes del vault** y en las **tres de trazabilidad autorizadas
> por Francisco**. Su ficha vive ya en `## Cerradas`. **Ojo: quedan sedes SIN AUTORIZAR fuera de ahí,
> tres de ellas en código, y eso es ficha NUEVA, más abajo.**

> **El 🟡 «la palabra "determinista" sigue viva FUERA de `PIPELINE.md`» queda CERRADO el 2026-08-17**,
> con la salvedad escrita en `agregar_semillas.py` (`:226`/`:245`) y en `anomalias.py`, y el residuo de
> T22 registrado como **reapertura autorizada** en `resumen-de-decisiones.md` sin reescribir `:633`,
> `:636` ni `:1154`. Su ficha vive ya en `## Cerradas`.

### Altas del ciclo de Código — 2026-08-17

> **El 🟠 «SEXTO re-anclaje de sello: `commit_agregador = 0276039-sucio`» queda CERRADO el
> 2026-08-17**, re-anclado **en prosa** y con el sello impreso dentro de los tres artefactos
> **intacto** (`0276039-sucio`, verificado en los tres), como manda la regla. Su ficha vive ya en
> `## Cerradas`.

> **El 🟠 «El re-anclaje pendiente de `validacion.py` (`a8c20e9-sucio`) NO TENÍA FICHA» queda
> CERRADO el 2026-08-17**: se **ejecutó** el re-anclaje y los seis artefactos llevan ya el sello
> **limpio `ac36b88`**. Su ficha vive ya en `## Cerradas`.

- [ ] 🟡 **`features.md` citaba `3.3:42` como sede pendiente; en disco es `3.3:29` y ya está resuelta** · — · `cronista`
  Alta el **2026-08-17**. Referencia con línea **desfasada** dentro del propio registro. Queda
  fichado como **patrón a vigilar**, no como incidencia suelta: las referencias `fichero:línea` de
  este documento **se recuentan contra disco antes de repetirlas**.
  **CADUCADA en su parte concreta (2026-08-17): la sede `3.3:29` está RESUELTA en disco.** Lo que sigue
  vivo es **solo el patrón**, y hoy ha vuelto a morder dos veces más: el `[!todo]` de los seis ítems
  no-FT que este registro situaba en `A.3:574` **está en `A.3:681`**, y `3.3:42`→`3.3:29`. **Tres veces
  el mismo fallo en un día.**
  **CUARTA OCURRENCIA (2026-08-17, TANDA 20): la ficha del SÉPTIMO re-anclaje citaba `4.2:269`, y en
  disco el contenido vive en `:264`/`:266`.** Forma canónica acordada en
  `resumen-de-decisiones.md:834-835` y aplicada al cerrarla: **se cita por nombre de callout o de
  campo, nunca por número de línea.** **Cuatro veces el mismo fallo en dos días.** La ficha **sigue
  ABIERTA**: lo vivo es el patrón.
  **QUINTA OCURRENCIA (2026-08-17, TANDA 21), y esta la generó un agente EN EL MISMO TURNO, no un
  registro viejo:** el `auditor-ml` situó el hedge de `2.1.6` en **§2.1.6.6** y el `redactor-tfg` lo
  encontró en **§2.1.6.3**. Se apunta junto a la de la TANDA 20 (`4.2:269` → `:264`/`:266`). **Van
  CINCO en dos días**, y con la de hoy el patrón **ya no describe un descuido del pasado: describe
  cómo se comporta este vault.** Refuerza la forma canónica: **se cita por nombre de callout, de
  sección o de campo, nunca por número de línea.**

> **El 🟡 «`Bibliografía.md:177` — el localizador de `[49]` apunta a `2.3.2.5`» queda CERRADO el
> 2026-08-17** en el pase en serie del `researcher`, junto con los **tres `[CITA: …]` vivos**. Su
> ficha vive ya en `## Cerradas`.

- [ ] 🟠 **5 de las 47 citas colgantes NO se han podido reconstruir — falta criterio de Francisco** · Informe · **decide Francisco**, ejecuta `researcher`
  Alta el **2026-08-15**, residuo de la reparación de las 47 citas colgantes (ver `## Cerradas`, misma
  fecha). De los 47 `[n]` que dejó colgando el pase interrumpido, **42 quedan reconstruidos y
  verificados con DOI/URL** y dados de alta en `Bibliografía.md`; **5 no se han podido reconstruir** y
  quedan **marcados como tales**, con el detalle en
  `Obsidian_TFG_Vault/99 Investigación/Reconstrucción de las 47 citas colgantes.md`.
  **Lo que hay que decidir, y no lo decide un agente:** para cada una de las cinco, **retirar la
  afirmación que sostienen** o **buscar una fuente alternativa** que las respalde. Hasta que se
  decida, son referencias sin entrada verificada — el mismo defecto que hacía 🔴 a la ficha madre,
  con la diferencia decisiva de que ahora **están marcadas y se ven al leer**.

> **Los 7 marcadores `[CITA: …]` de `A.3` y los 3 de `EL_FUTURO.md` quedan CERRADOS en la TANDA 9**
> (2026-08-15, `e286cce`), dentro del pase en serie del `researcher`. Sus fichas viven ya en
> `## Cerradas`.

> **El reparto por categoría de D3 (45.927 / 11.656 / 995 / 52) queda EMITIDO POR SCRIPT en la
> TANDA 16** (2026-08-16). Su ficha vive ya en `## Cerradas`, y con ella el efecto lateral sobre
> `4.6:13`, acotado en la misma tanda.

> **La frontera `validacion.py` → `config.py` queda RESUELTA en la TANDA 16** (2026-08-16):
> Francisco **aprobó** la extensión, preguntado con las dos alternativas sobre la mesa. Su ficha
> vive ya en `## Cerradas`.

- [ ] **Diagrama y README de agentes describen la arquitectura anterior** · Código · `ml-implementador`
  Detectado el 2026-08-01. `Implementacion/diagramas/README.md:10` y
  `Implementacion/diagramas/03_orquestacion_agentes.mmd` documentan el ciclo «orquestador →
  implementador → auditor/ejecutor → redactor → cronista → `next-steps.md`», cuando hoy la
  entrada es el `leader` con carriles y tracks (`CLAUDE.md`, «Arquitectura de agentes») y
  `next-steps.md` está congelado: el roadmap vivo es `features.md`. Regenerar `.png` y `.svg` si
  se toca el `.mmd`. **La acepta o la retira Francisco.**

- [~] **Preliminares: título, resumen y abstract** · Informe · `redactor-tfg`
  **PARCIAL — 2026-08-18, TANDA 27 (Fase 7).** **Resumen y abstract HECHOS y verificados**:
  `00 Preliminares/Resumen.md` y `Abstract.md` con resumen académico completo, traducción fiel al
  inglés y palabras clave; cifras ancladas a `Resultados/metricas_hibrido.csv` y
  `metricas_baseline.csv` (fila `set_features=54`, commit `1163c90`); **cero `[n]`**. Su fila de
  ejecución vive ya en `## Cerradas`. **LO QUE MANTIENE ABIERTA ESTA FICHA ES SOLO EL TÍTULO**: hay
  **5 candidatos propuestos en `Resumen.md`** y **lo elige Francisco** (Decisión 6). Nada más de esta
  ficha queda pendiente.
  Se redactan **al final**, cuando el resto de capítulos esté cerrado.
  Notas: `00 Preliminares/Resumen.md` y `00 Preliminares/Abstract.md`.
  - **Ampliada el 2026-08-12** a partir de `mis-apuntes-del-informe.md:5` (el **resumen no está
    escrito** y Francisco pide propuesta; el **abstract** es ese mismo texto en inglés) y
    `mis-apuntes-del-informe.md:7` (**falta el título del proyecto**). Ese fichero es
    **incremental**: al ejecutar esta ficha hay que **releerlo entero** y no fiarse de lo anotado
    aquí, que es el estado del **2026-08-12**.
  - **El título es decisión de Francisco, no de un agente:** un agente puede **proponer
    candidatos**, no fijarlo.
  - **DECISIÓN 6 de la Fase 0, tomada por Francisco el 2026-08-14: el título queda APLAZADO.** Los
    preliminares se redactan al final por decisión ya registrada, y fijar el título antes de que
    existan el capítulo 2 y las conclusiones es fijarlo con menos información. Sigue siendo suyo.
    **No se pide todavía lista de candidatos**: se pedirá dentro de esta misma ficha, en la Fase 7.
  - **ESTA FICHA QUEDA SIN DEPENDENCIAS el 2026-08-18**, al cerrarse el **capítulo 1** en la FASE B
    del barrido (lo último ejecutable del barrido). Era lo que esperaba a que el resto de capítulos
    estuviera cerrado, así que es el **siguiente paso natural (Fase 7)**. **El título sigue siendo
    decisión de Francisco** (Decisión 6): un agente propone candidatos, no lo fija. Al ejecutarla hay
    que **releer `mis-apuntes-del-informe.md` entero**, que es incremental.

### Lote 2026-08-06 — los 4 informes del `researcher` convertidos en tareas

> Alta de las 18 fichas T0-T17 acordadas con Francisco en el `grill-me` de 13 preguntas cerrado el
> **2026-08-06**, a partir de los cuatro informes de `Obsidian_TFG_Vault/99 Investigación/`.
> **Criterio rector:** nada que no refine el proyecto o no ayude al lector a ver que con NSL-KDD se
> hizo todo lo posible; las imposibilidades se **declaran con su razón técnica**, no se omiten ni se
> sustituyen por sucedáneos sintéticos. Y el dataset tiene argumento positivo propio (Goldschmidt y
> Chudá: solo el 23 % de los datasets NIDS trae partición train/test predefinida, 16 % desde 2020, y
> su ausencia es «*prone to biased evaluations and selective reporting*»; NSL-KDD sí la trae y este
> TFG la respeta), y ese argumento va **antes** de cualquier límite.
>
> **Decisión marco (a) — se REABRE el track de código**, cerrado el 2026-07-16, de forma
> **declarada** y con el alcance exacto de la spec: Nivel 1 (esquema de métricas, no mueve ningún
> número publicado) + Nivel 2 acotado (10 semillas, los titulares siguen siendo semilla 42) + dos
> mediciones baratas. Todo pasa por `auditor-ml`. Nada más.
>
> **Decisión marco (b) — se retira la regla «lo escribe Francisco», en dos velocidades:** `2.x`
> retirada completa (`redactor-tfg` redacta la prosa desde los guiones existentes); `6.2` pasa a
> **borrador de agente con revisión final de Francisco** (es el sitio natural del material de NL, y
> bloqueada dejaba a medias un entregable del encargo); **la bibliografía final en Zotero/IEEE sigue
> siendo de Francisco** (trabajo mecánico en su máquina).

- [x] **T4 · Nivel 2: 10 semillas** · Código · `ml-implementador` → `auditor-ml` → `ejecutor-experimentos`
  > ✅ **CERRADA EN LA TANDA 19 (2026-08-17).** Su última condición viva —que `5.2`/`5.4`
  > **consumieran** la banda, no solo que existieran— se **verificó contra disco celda a celda**: la
  > banda está genuinamente consumida y el 🔴 histórico *folds vs semillas* **NO ha reaparecido**.
  > Veredicto **APTO**. Lo que sigue debajo es el historial de la ficha, no trabajo pendiente.
  > **Resto ABIERTO que NO es de esta ficha:** el «8 de 10» pareado no lo emite ningún script, con
  > fila propia en `## Abiertas`.
  10 semillas × **5 scripts** (`cascada_invertida.py` entra también) × 2 sets de características.
  **Duración medida del barrido: 2026-08-12T22:09 → 2026-08-13T00:38, ≈2 h 29 min** — es la única
  cifra de duración citable.
  - **La parte de CÓMPUTO está CERRADA** (barrido corrido y agregado, ver `## Cerradas`, `9ad971b`).
    Lo que queda vivo de T4 es el **consumo del resultado en el informe**: la tabla de dispersión de
    `A.3` (**T7**) y los párrafos de `5.2`/`5.4` (**T11**). **T4 no se cierra hasta que esos dos
    consuman la banda.**
    - **Estado a 2026-08-14: T7 está CERRADA** —`A.3` ya pega la tabla con sus salvedades—, así que
      **el único consumidor vivo es T11**. **T4 no se cierra hasta que `5.2`/`5.4` estén escritos.**
    - ✅ **DESBLOQUEADA el 2026-08-17: la condición SE CUMPLIÓ. `5.2` y `5.4` están escritos desde la
      TANDA 17** (`9bcfe1f`), que cerró **T11** con el capítulo 5 completo. **T4 ya no espera a
      nadie**; lo que queda es **verificar que la banda está efectivamente consumida** en `5.2`/`5.4`
      —y no solo que las notas existan— antes de cerrarla. **Ojo al leer `5.2`:** el 🔴 de aquella
      auditoría fue precisamente presentar como dispersión entre semillas unos `±` que eran la sd
      **entre los 5 folds** de la semilla 42; corregido en `5.2:145-146`, pero **es el error que T4
      existe para evitar** y hay que confirmar que la tabla que se consume es la de
      `dispersion_semillas.csv`.
  - **Los titulares de 5.1-5.3 siguen siendo los de la semilla 42.** La dispersión (media, sd, mín,
    máx) entra como tabla nueva en `A.3` más un párrafo en `5.4`. **No se reescribe el capítulo.**
  - Cierra los ítems FT *number of runs*, *error bars* y *central tendency* de Pineau et al.
  - **Sin p-valor, con la renuncia declarada y su razón: 10 puntos sobre un único dataset no
    sostienen un contraste.** Declarar la renuncia **cumple** el ítem *statistics*; callarla no.
  - **Objetivo real, YA RESPONDIDO por el barrido:** dos decisiones cerradas descansaban en huecos de
    1-2 pp medidos con n=1 — RandomForest 0,822 vs HistGradientBoosting 0,804 (firmas) y Autoencoder
    vs IsolationForest (anomalías). **El primero solapa** —hay que decirlo y **no establecer el
    orden**— y **el segundo aguanta**. Detalle y forma de escribirlo, en la viñeta `5.2` de **T11**.
    Es un hallazgo para `5.4`, no un desastre.
  - **Aviso heredado de T1 (cerrada el 2026-08-08):** T4 **no puede escribir en las cuatro tablas
    principales** — choca contra el borrado por variante, la `CLAVE_UNICIDAD` sin `semilla` y su
    recuento fijo. Por eso la dispersión va a **tabla nueva** en `A.3`. Ya está escrito en
    `PIPELINE.md` y en el docstring de `comprobar_recuento()`.
  - **El lanzador del barrido exige CINCO recuentos por (variante, semilla): 4/4/1/1/5** — las 5
    filas de la cascada invertida entran también (`barrido_semillas.py:107-109`).
  - **Dispersión del wall-clock:** hasta **4,8× entre corridas en máquina no dedicada** con calidad
    idéntica al bit (Autoencoder-54: 37,71 → 181,91 s). **CORREGIDO el 2026-08-17 (Tanda 18): esta
    ficha decía «con el recuento de épocas idéntico … así que es carga de máquina, no épocas», y era
    FALSO.** Esas dos corridas **no registran épocas** (`PIPELINE.md:923-929`): `n_iter_total_grid`
    solo existe en `ac496cb` y `1163c90`. La banda se declara como **magnitud observada, sin causa
    atribuida**. Las columnas de tiempo de las 10 semillas **no** se leen como propiedad del algoritmo
    sin declarar esa dispersión.
  - **Estado del barrido verificado en disco:** corrido y **agregado** — **2.320 filas**, **20/20
    celdas** (10 semillas × 2 variantes), sello `df30cb2` único y limpio;
    `Resultados/dispersion_semillas.csv` y `.md`, **198 filas**, `sd` muestral `ddof=1`.
  - **El andamiaje de semilla (flag `--semilla N`, nueve tablas `*_semillas.csv`, lanzador reanudable
    y agregador) está cerrado y auditado**, con los **ocho hallazgos aplicados el 2026-08-12**: borrado
    de `.joblib` por semilla tras `hibrido.py` y `cascada_invertida.py`; `SEMILLAS_BARRIDO = [1..10]`
    en `config.py` (42 **fuera** a propósito); agregador nuevo `Implementacion/app/agregar_semillas.py`;
    `Resultados/figuras/*_semilla*` excluido en el `.gitignore` raíz; tabla «qué SÍ varía dentro de
    cada semilla» en `PIPELINE.md`; traza `Resultados/verificacion_semilla_joblib.txt` (**20/20
    `.joblib` publicados con `semilla = 42`**); salvaguarda simetrizada en
    `cascada_invertida._leer_umbral_conf`; y `--semilla` documentado en los cinco scripts, `README.md`
    y `GUIA_RESULTADOS.md`. Cifras medidas: `Resultados/modelos/` **481,33 MB**, el barrido **200
    modelos ≈ 4,8 GB**, **65,2 GB libres** en C: — el espacio **no** es blocker, y los `.joblib` del
    barrido se borran por semilla por higiene, no por falta de sitio.
  - **LÍMITE DEL DISEÑO, a declarar en `A.3` (T7) y en `5.4`/`5.2` (T11):** `program.py` **no está
    parametrizado** —su `random_state=42` es literal y no importa `config.py`—. Las 10 semillas miden
    dispersión **de los modelos sobre splits D1/D2/D3 y set de características FIJOS**: **no**
    incluyen variabilidad del preprocesado ni de la selección de características. Escribirlo así, no
    como «dispersión del sistema».
  - **El runbook del barrido está en `Implementacion/PIPELINE.md`, sección «Runbook del barrido de
    semillas»**, y es lo que hay que teclear para relanzar. Su **paso 2** exige que
    `Get-ChildItem -Recurse ..\Resultados -Filter *_semilla*` salga **VACÍO** antes de lanzar,
    **excluyendo `verificacion_semilla_joblib.txt`** —esa traza casa con el patrón, está versionada y
    es permanente—: cualquier corrida interrumpida repone residuos `*_semilla*` y la reanudación los
    tomaría como celdas ya hechas.
  - **🟡 La rama del agregador «1 semilla de 10» sigue sin ejercitarse en ejecución** — solo auditada
    su lógica; llegar a ella exige correr `anomalias.py` y `firmas.py` de una semilla entera. **Lo
    asume o lo cubre Francisco.**
  - **Historial de los tres pasos previos, los tres HECHOS y verificados** (2026-08-12/13):
    1. **Residuo `_semilla1` borrado** — 11 ficheros (6 figuras `*_54_semilla1*`, 4 `.joblib`
       `anomalia_*_54_semilla1` y `metricas_anomalias_semillas.csv`), con OK explícito de Francisco y
       **antes del commit `54d1349`**. Verificado en disco después: el único fichero de todo
       `Resultados/` que casa con `*_semilla*` es la traza `verificacion_semilla_joblib.txt`, y lo
       publicado quedó intacto (20 modelos, 39 figuras, 9 tablas).
    2. **Ensayo de humo rematado:** los tres puntos que faltaban **PASAN** — salvaguarda de mezcla de
       semillas (aborta con exit 1 y escritura cero), reanudación sin duplicar filas (10 corridas → 9
       con 1 saltada; tablas en 1 y 18 filas tras relanzar, no en 2 y 36) y el agregador aborta (por
       la guarda de tabla inexistente, `agregar_semillas.py:235`). En el mismo pase se escribió el
       **runbook del barrido**, que no existía, con puntero desde `README.md`.
    3. **Barrido lanzado y agregado**, con dictamen **APTO** de `auditor-ml` a la tercera pasada. Las
       cifras están en «Estado del barrido verificado en disco», arriba.
    - **Las cargas de `.joblib` ausente ya dan mensaje accionable** (`hibrido.py:200-219`,
      `cascada_invertida.py:198-213`): relanzan `RuntimeError` con ruta, script previo, variante con su
      flag y semilla, y **siguen abortando con exit ≠ 0 y escritura cero**.
    - **Dato de un solo punto, no concluyente pero del mismo signo:** a semilla 1, Autoencoder
      `f1` **0,8632** / `accuracy` **0,8520** frente a IsolationForest `f1` **0,8226** / `accuracy`
      **0,8157** — **mismo signo que el hueco publicado** con la 42, que en `accuracy` es
      **0,8605 vs 0,8257** y en `f1` **0,8716 vs 0,8341** (`Resultados/metricas_anomalias.csv`, set 54).
      El signo se sostiene en las dos métricas. **No sustituye al barrido.**
      → **Aviso de procedencia, y no es formalismo:** estas cuatro cifras de la semilla 1
      **no son verificables desde git por un tercero**. El CSV que las respaldaba
      (`metricas_anomalias_semillas.csv`) se borró como residuo y **nunca se commiteó**, así que no
      hay ninguna coincidencia de `0.8632|0.8520|0.8226|0.8157` en el repositorio. Sirven como
      indicio interno para decidir; **no valen como evidencia citable en la memoria**. Las de la 42 sí
      están en disco y versionadas.

> **T5 — CERRADA el 2026-08-15 en la TANDA 7** (ver `## Cerradas`).
> `Obsidian_TFG_Vault/05 Evaluación/5.0 Protocolo de evaluación.md` existe: **nota nueva de 191
> líneas**, íntegra en disco, que cubre el encargo punto por punto **incluido el arreglo de C3/C6
> contado**, con el caso concreto de la columna `accuracy_D2` homónima. **No se vuelve a encargar.**
> Lo que deja vivo tiene ficha propia: **5 de los 20 `[CITA: …]` nuevos** son de esta nota, y dos de
> los **5 hallazgos 🔴** de su auditoría. Se deja esta línea para que nadie la vuelva a despachar; el
> encargo original vive en git.

> **T6 — CERRADA el 2026-08-15 en la TANDA 7** (ver `## Cerradas`). El apartado **`6.1.4`** existe
> dentro de `Obsidian_TFG_Vault/06 Conclusiones/6.1 Conclusiones.md` (**+77 líneas**), en el **cuerpo
> y no en apéndice** como pedía el encargo, con los **seis límites** y la **tabla P1-P10**. **No se
> vuelve a encargar.** Lo que deja vivo tiene ficha propia: **7 de los 20 `[CITA: …]` nuevos** son de
> esta nota, y **cuatro de los 5 hallazgos 🔴** de su auditoría caen dentro de ella —incluido el que
> se enlaza con **T21**—. Se deja esta línea para que nadie la vuelva a despachar; el encargo
> original vive en git.

> **Los «Residuos de `A.3` (T7 cerrada el 2026-08-14)» quedan CERRADOS COMO AGOTADOS en la TANDA 25**
> (2026-08-18), **sin tocar la nota**. En disco queda **un único `[!todo]` vivo** en `A.3`, el de la
> caracterización de los seis ítems no-FT del checklist de Pineau (**`A.3:698`**), y **no es
> resoluble por un agente**: depende del **checklist original**, fuente externa que no está en disco
> — nombrarlos sería inventarlos. Deja de ser trabajo pendiente y pasa a ser **dependencia de fuente
> externa**. El `[!warning]` de límite declarado de alcance está en **`A.3:654`**. Su ficha vive ya en
> `## Cerradas`. **Texto original conservado abajo solo como historial: no leas de ahí trabajo
> pendiente, y sus números de línea (`:574`, `:681`, `:648`) estaban CADUCADOS.**

> **T8 — CERRADA el 2026-08-15 en la TANDA 11** (`d31e20f`, ver `## Cerradas`). Lo único que la
> mantenía abierta era **`2.1.5`**, hoy **completada al nivel de `A.2`** (17 bloques de fórmulas,
> frase cortada cerrada, aparato de citas): **FPR, F1 y macro/weighted ya están definidos**, así que
> las **tres remisiones colgadas** de `2.3.3:31`, `2.3.3:139` y `2.1.6:132` dejan de apuntar a
> contenido inexistente. Las cargas de `2.2.3`/`2.2.4` (Tanda 4) y de `2.3.3`/`2.1.6` (Tanda 5)
> ya estaban verificadas contra disco. **No se vuelve a encargar.** El encargo original vive en git.


- [x] **T9 · Cita en el punto de la decisión — capítulo 3** · Informe · `redactor-tfg`
  > ✅ **RESUELTA el 2026-08-17, sin trabajo de recorte pendiente. Ficha en `## Cerradas`.**
  > **La ficha iba UN DÍA POR DETRÁS DEL DISCO**: el recorte que estos bullets describían como vivo
  > **ya estaba ejecutado desde la TANDA 12 (2026-08-16)**, con respaldo en
  > `resumen-de-decisiones.md:983-1049`. El `redactor-tfg` no modificó nada porque no había nada que
  > aplicar. **Es la misma clase de divergencia registro/disco que ya costó un ciclo entero de
  > reconciliación**: queda escrito que el registro mentía, no solo que la tarea se cerró.
  > **NO está aceptada**: aceptar y retirar la ficha es decisión de Francisco.
  > Lo que sigue debajo es el historial de la ficha, no trabajo pendiente.
  - `3.1`: **modelo de amenaza explícito** = aplicar P10. Atacante no adaptativo, sin conocimiento
    del modelo, que no intenta evadirlo; opera sobre flujos ya extraídos, no sobre paquetes; sin
    envenenamiento del entrenamiento. **Y la razón citada de por qué no hay experimento adversario:**
    muchas características de NSL-KDD son derivadas y agregadas (`count`, `srv_count`, tráfico-host,
    contenido); perturbarlas libremente produce vectores que ningún atacante real puede generar —un
    ataque en espacio de características sin correspondencia en el espacio del problema. **Esa
    distinción (*feature space* / *problem space*) es de Pierazzi et al., «Intriguing Properties of
    Adversarial ML Attacks in the Problem Space», NO de Arp et al.** —mismo error ya corregido en
    la nota `2.3.3`; no reintroducirlo. **Intentar P10 a fondo con este dataset produciría
    exactamente ese ataque irrealizable en el espacio del problema.** Eso es un resultado, no una
    excusa.
  - `3.2.2`: por qué anomalías primero. Tres patas: diseño (la etapa 2 no conoce `normal`), cobertura
    (Tombini et al. 2004), y el *semantic gap* de Sommer y Paxson 2010 —la etapa 2 no existe para
    detectar sino para **traducir** «esto es anómalo» en «esto es un `dos`»—. Más **Kim et al. 2014
    como antagonista directo** (mismo dataset, orden inverso) y el precio declarado: FPR 0,102 frente
    al 0,027 del baseline monolítico. Más **el número de T3**.
    → **El número de T3 ya existe (cierre del 2026-08-10):** de las **9.711 filas normales de D2**, el
    clasificador de firmas condenaría **6.558 (67,53 %)** a 54 características y **3.329 (34,28 %)** a
    122. **Se cita como COTA INFERIOR de falsos positivos irrecuperables, NO como «el FPR de un
    sistema de firmas-primero»**: en el sistema publicado `unknown` es alarma (decisión **P-5**,
    respaldada **por símbolo: `hibrido.py::_ensamblar_prediccion`**), así que lo que cae bajo umbral no
    queda exonerado. Lectura, tabla y forma de citarlo en `Implementacion/PIPELINE.md`, sección «La
    cascada invertida (T3)».
  - `3.2`/`3.6`: la divergencia declarada. En ADAM la etapa 2 etiqueta «falsa alarma» y **la filtra**;
    aquí se le prohíbe por diseño (H-5, P-5). Matiz: H-5 es correcta *dentro* de su premisa, pero su
    redacción actual puede leerse como si **toda** cascada anomalía→firmas tuviera esa propiedad, y
    no es así: la tienen las cascadas cuya etapa 2 carece de clase `normal`, que es una **elección**.
  - `3.3`: Mitchell et al. (el recall 0-day por tipo **es** evaluación desagregada, con nombre y
    precedente) + Scheirer et al. (`unknown` es formalmente *open-set recognition*, lo que justifica
    reportar la tasa de enrutado como métrica propia con su alcance — decisión H-6).
  - `3.4`: Sommer y Paxson, verbatim: entrenar solo con normal es obligado para aspirar a lo novedoso,
    y **cuesta** —«exige tener un modelo *perfecto* de normalidad»—. Es la explicación teórica del FPR
    del híbrido, que se cita **por variante: 10,2 % en 54 y 8,5 % en 122** (`metricas_hibrido.csv`,
    `bin_fpr`), **nunca como rango redondeado**. No es un defecto del autoencoder.
  - `3.5`: **por qué RandomForest y no una arquitectura profunda.** Los 5 criterios de McElfresh et
    al. cruzados con los números de D3 (58.630 filas, razón 1.086 muestras/característica,
    distribuciones con colas larguísimas, 60 de 122 características descartadas por importancia)
    apuntan todos al cuadrante de los árboles; más Grinsztajn et al. y Shwartz-Ziv y Armon. La
    familia tabular profunda se nombra **una vez y en positivo** (TabNet, FT-Transformer, TabPFN),
    nunca como «lo descartamos», que invita a «¿y por qué no lo probaste?». Dos apoyos duros: el
    contraste interno de calidad (**HistGradientBoosting `f1_macro` 0,804 frente a RandomForest
    0,822** — si el GBDT de la propia sklearn no despega, el argumento se sostiene solo) y
    **TabPFN v2 de *Nature* admite 10.000 muestras y D3 tiene 58.630**. Usar la formulación C.1 del
    informe tabular.
    → **VIÑETA REFORMULADA el 2026-08-14, que es lo que RESUELVE T20** (ver `## Cerradas`). El par
    **`68,7 s / 54,8 s`** que esta viñeta arrastraba **no existe en ningún artefacto** (detectado el
    2026-08-08 al cerrar T1) y **queda retirado: no se usa**. Lo citable, y ni una palabra más
    (formulación anclada en **`PIPELINE.md:493-498`**):
    - **El coste de ENTRENAMIENTO de HistGradientBoosting es mayor que el de RandomForest en 8 de
      los 10 pares intra-corrida medidos**, con los **dos contraejemplos ambos en la variante de
      54** (2 de cada 5 corridas invierten ese par). **No hay horquilla en segundos que citar** y
      **la afirmación solo es sólida en la variante de 122**: escribirla acotada así, nunca en
      absoluto.
    - **En INFERENCIA a 54 características el orden se invierte:** HistGradientBoosting **0,0032
      ms/flujo** frente a RandomForest **0,0072**. Si se habla de coste, decir **de cuál**.
    - **Lo que no se mueve es la calidad:** HistGradientBoosting sigue **sin ganar `f1_macro`**
      (0,804 vs 0,822), y ese es el apoyo duro del argumento. **La dirección aguanta; lo que era
      falso era la formulación.**
  - **AMPLIACIÓN del 2026-08-15 — T9 EJECUTA EL RECORTE que la TANDA 10 (pieza B) dejó ANALIZADO.**
    El informe `Obsidian_TFG_Vault/99 Investigación/Datos repetidos en el capítulo 3.md` (513 líneas,
    `3fadf13`) responde a la crítica del profesor y trae, para cada uno de los **15 solapes
    verificados con línea exacta**, la acción (**recortar / unificar / remitir**), la **sede canónica**
    y **la frase de remisión concreta** que T9 debe insertar. **Ese informe es análisis, no ejecución:
    aquí es donde se aplica.** Cifra a sostener ante el profesor: el capítulo 3 encoge **≈20 % en
    total** y **≈25 % en `3.1`–`3.3`** —**estimación redondeada a la decena**, sin script de conteo,
    y así se publica—.
    - **NO SE TOCA la sección de repetición LEGÍTIMA** que el informe valida y el auditor confirmó:
      `3.4.1`↔`2.3.1`, la cadena `3.1.3`→`3.5.3`→`4.5` y los cierres de capítulo.
    - **LAS TRES TRAMPAS QUE LA AUDITORÍA CAZÓ ANTES DE QUE T9 LAS PISARA, y por eso quedan escritas
      aquí y no solo en el informe:** (1) el informe declaraba `4.3.6` «único sitio con los 17 tipos»
      y es **FALSO** —`A.1:99-106` los enumera—, y su instrucción **habría roto una remisión buena**;
      (2) S2 y S7 ignoraban `2.1.6:132-140`; (3) S1 creaba una **segunda redacción** del *data
      snooping*, contra `resumen-de-decisiones.md:316-323`. **Los tres están aplicados en el informe**,
      pero son el tipo de instrucción que se ejecuta sin releer.
    - **El *data snooping* está en 10 sitios, no 6:** el barrido inicial de este fichero se quedaba
      corto —faltaban `2.1.6:76-90`, `4.6:28-35`, `5.4:32` y `A.3:574-586`—. Más un solape cap. 2 ↔
      cap. 3 (`2.2.4.5` ↔ `3.2.2`) y uno interno (`3.2.1` ↔ `3.3.3`).
    - **HUECO DECLARADO del informe, no oculto: el barrido del capítulo 2 solo cubre `2.1.6` y
      `2.2.4`.** Tiene ficha propia; conviene completarlo antes o durante T9.
    - ~~**PENDIENTE DE RECONSIDERAR DENTRO DE T9:** `2.3.3:91` **no** se repuntó al ancla `3.1.5`
      —se dejó el wikilink a nota, convención del vault— precisamente porque T9 **renumera el
      capítulo 3**. Al renumerar, decidir si procede el ancla.~~
      → **VERIFICADO Y CERRADO el 2026-08-16 (auditoría de la TANDA 12): el ancla era CORRECTA y no
      había nada que repuntar.** La renumeración de T9 fue **local a `3.3`**; **`3.1` no se renumeró**,
      así que el destino del wikilink no se movió. **La condición que motivaba la reconsideración
      nunca llegó a darse.** Ficha en `## Cerradas`, 2026-08-16.
    - **LO QUE SIGUE VIVO DE T9 tras la TANDA 12** (la auditoría ya corrió; ver `## Cerradas`): el
      ~~**barrido de solapes del capítulo 2**~~ —**CERRADO en la TANDA 19, 2026-08-17**— y la **comprobación contra `99 Investigación/Datos repetidos en el capítulo 3.md` de qué solapes
      de los 15 quedan sin aplicar** — `3.1` no se tocó, y hay que **confirmar** si eso es correcto
      (`3.1.5` es nueva y está exenta) en vez de darlo por bueno.
      → **CERRADO el 2026-08-17: la comprobación se hizo y NO quedaba nada por aplicar.** Verificado
      **S1–S13 y S15 vivos**, `S14` y las repeticiones legítimas **intactas por diseño**, `3.3`
      renumerada **sin remisiones rotas** en ninguna nota de memoria, las **once anclas** emitidas por
      el capítulo 3 existentes, los **diez `[n]`** del capítulo presentes en `Bibliografía.md` sin
      huérfanos, y el *data snooping* **enunciado una sola vez** (`3.3:29`, literal respecto a la
      decisión registrada). **`3.1`: confirmado que NO procedía intervención** — era el único bullet
      que esta ficha dejaba explícitamente sin resolver.

- [x] **T10 · Capítulo 4** · Informe · `redactor-tfg`
  > ✅ **CERRADA EN LA TANDA 17 (2026-08-17, `9bcfe1f`).** Su último bullet vivo era el del «17», de
  > track mixto, y se cerró ahí: verificado contra disco que son **17 tipos 0-day y 3.750 filas de
  > D2**, con la ficha mintiendo en dos sitios —`firmas.py:157` era `:174`, y los supuestos «~17» de
  > `.gitignore` y `README.md` eran **`~170 MB`**—. ~~**Queda un resto ABIERTO** … las 7 ocurrencias
  > del «~17».~~ → **APLICADO Y CERRADO en la TANDA 19 (2026-08-17)**: las **7 ocurrencias**
  > (4 en `resumen-de-decisiones.md`, 3 en `next-steps.md`) están sustituidas, con la **nota fechada**
  > registrando la excepción expresa de Francisco (`resumen-de-decisiones.md:1388-1396`). **Verificado
  > contra disco: cero «~17» en el árbol**; los `~170 MB` de `.gitignore` y `README.md` siguen
  > intactos, como debe ser. Ficha en `## Cerradas`.
  > Lo que sigue debajo es el historial de la ficha, no trabajo pendiente.
  >
  > **AVANZADA, NO CERRADA en la TANDA 14 (2026-08-16): hechos 2 de sus 5 bullets** —«Las tres
  > particiones oficiales» con la vacuna sobre KDDTest-21, y la 5.ª razón de «por qué NSL-KDD» con
  > Goldschmidt y Chudá—. ~~**Siguen VIVOS: el «~33 %» de DoS con su denominador (`4.2:92`), la nota de
  > procedencia del «17», y `4.3` entera.**~~
  > **AVANZADA OTRA VEZ, Y SIGUE SIN CERRAR — TANDA 15 (2026-08-16): hechos el «~33 %» de DoS con sus
  > dos denominadores y `4.3` entera** (nueva `4.3.7`, peso real del one-hot en `4.3.3`, poda de
  > *dummies* en `4.3.5`). **De los 5 bullets quedan 4 hechos y UNO vivo: el del «17», de track
  > MIXTO.** Se dejó fuera de la Tanda 15 **a propósito, no por olvido**: toca **2 ficheros de código**
  > (`baseline.py:12`, `firmas.py:157`) y por tanto exige `auditor-ml` sobre código, no sobre prosa.
  > **AVISO PARA CUANDO SE DESPACHE EL BULLET DEL «17»: la lista de sitios que da la ficha está
  > CADUCADA.** Recontado contra disco el 2026-08-16: **`2.1.6:55` ya NO lo tiene**, y en cambio
  > aparece en **`.gitignore`** y **`README.md`**, que la ficha no nombra. Son **18 ocurrencias en 12
  > ficheros**, y **dos son CÓDIGO** (`baseline.py:12`, `firmas.py:157`), así que ese bullet es de
  > **track MIXTO**, no solo Informe. **Contar antes de sustituir.**
  > **Pendiente del `researcher`** (requiere petición explícita de Francisco): el **alta de Goldschmidt
  > y Chudá 2025**, único `[CITA: …]` vivo de la memoria (`4.2:62`), y el **censo de `[23]` en
  > `Bibliografía.md:126`, que dice `×3` cuando ahora son `×5`**. **AMPLIADO en la TANDA 15
  > (2026-08-16):** añadir además `4.3` a la fila «dónde se usa» de **`[17]` Kapoor y Narayanan** y de
  > **`[18]` Arp et al.** (`Bibliografía.md:120-121`), que la nueva `4.3.7` cita y el registro no
  > recoge. Sigue siendo del `researcher` y sigue requiriendo petición explícita de Francisco.
  - ~~`4.2`: definición correcta de las tres particiones (KDDTrain+ 125.973 · KDDTest+ 22.544 ·
    KDDTest-21 11.850) y **vacuna contra el error que circula por la literatura**: KDDTest-21 **no**
    es «el subconjunto con 21 tipos de ataque», es el de dificultad alta —`#successfulPrediction` ∈
    [0,21] sobre **21 máquinas aprendidas (7 algoritmos × 3 entrenamientos)**, excluyendo los
    registros que todas acertaron—. Comprobado que ese error **no está hoy en ningún fichero del
    repo**: se vacuna, no se corrige. Escribir que **D2 es KDDTest+ completo**, requisito de entrada a
    toda comparación externa. Y el matiz de los baselines canónicos: se entrenaron con **el primer
    20 % de KDDTrain+**.~~ → **HECHO en la TANDA 14, 2026-08-16.**
  - ~~`4.2` · **el 17**: unificar «~17» → «17»~~ → **HECHO Y CERRADO** (Tandas 17 y 19).
    **El censo de sedes que esta viñeta traía queda RETIRADO por caducado POR SEGUNDA VEZ**: decía
    `resumen-de-decisiones.md:143` (era `:153`), `2.1.6:55` (ya no lo tenía) y `firmas.py:157` (era
    `:174`). **Recontado contra disco el 2026-08-17: CERO ocurrencias de «~17» en todo el árbol.** No
    se copia una lista nueva: si vuelve a hacer falta, se cuenta. Historial y nota de procedencia: **17 contados sobre
    `metricas_hibrido_0day.csv`; la cifra 14 de Tavallaee et al. se refiere a KDD'99, no a
    NSL-KDD**. El 17 se justifica **por medición en disco, nunca por cita**.
  - ~~`4.2` · **por qué NSL-KDD**, con Goldschmidt y Chudá (el argumento positivo del criterio
    rector).~~ → **HECHO en la TANDA 14, 2026-08-16** (5.ª razón). **Su alta bibliográfica NO está
    hecha**: baja como `[CITA: Goldschmidt y Chudá 2025]` en `4.2:62`, y el alta es del `researcher`.
  - ~~`4.2:72` · **el «~33 %» de DoS en D2 está mal referido** (anclado aquí el **2026-08-12**, salido de
    la auditoría del despacho de las dos fichas del `4.2`; **no abre ficha propia porque es
    preexistente y cae de lleno en el alcance de T10**). Ese ~33 % es sobre **D2 entero**, no sobre
    **sus ataques**: sobre los ataques de D2 el DoS es el **58,1 %**. Al redactar, decir **sobre qué
    denominador** se da cada porcentaje.~~ → **HECHO en la TANDA 15, 2026-08-16**, y con los **dos**
    denominadores publicados en tabla (**58,1 % sobre los ataques de D2**, **33,1 % sobre D2
    completo**) y su procedencia (`soporte_*` de `metricas_baseline.csv`).
  - ~~`4.3`: C5 sin fuga con las cuatro líneas verificadas (Kapoor y Narayanan; P3/P5 de Arp et al.) y
    el peso del one-hot: **84 de 122 características (69 %) vienen de la codificación**, 70 de ellas
    de `service` sola; de las 60 eliminadas por importancia, **58 son *dummies*** → la selección de
    4.3.5 es en la práctica un mecanismo de poda del one-hot de `service`.~~ → **HECHO en la TANDA 15,
    2026-08-16**: nueva **`4.3.7 Preprocesado sin fuga de datos`** con las cuatro transformaciones
    contrastadas contra `program.py` y las citas `[17]`/`[18]`; **84/122 = 68,9 %** en `4.3.3`
    (`service` aporta 70); y en `4.3.5` **58 de las 60** eliminadas son *dummies* (`service` 70→15).

- [x] **T11 · Capítulo 5** · Informe · `redactor-tfg`
  > ✅ **CERRADA EN LA TANDA 17 (2026-08-17, `9bcfe1f`).** Las cinco notas `5.0`–`5.4` redactadas en
  > paralelo sobre ficheros disjuntos, con **tres pases de auditoría**. **El primero fue NO APTO con
  > dos 🔴, y los dos eran cifras falsas**: `5.2` presentaba como dispersión **entre semillas** la sd
  > **entre los 5 folds** de la semilla 42, y `5.1` publicaba **cuatro tiempos inexistentes** de los
  > que salía un titular ya propagado a `5.4`. Ambos corregidos y verificados cerrados.
  > **Restos ABIERTOS que NO son de esta ficha y viven en sus propias filas de `## Cerradas`:** los
  > **3 `[CITA: …]` vivos** (`5.0:160`, `5.1:86`, `5.4:78`) y la atribución de **`5.4:42` a `[18]`**.
  > Lo que sigue debajo es el historial de la ficha, no trabajo pendiente.
  >
  - **AMPLIACIÓN del 2026-08-16, hallazgo NO FORZADO de la auditoría de la TANDA 15 — `5.0 Protocolo
    de evaluación.md` arrastra dos defectos que la Tanda 15 corrigió en `4.3` pero NO tocó aquí,
    porque es fichero de esta ficha.** (1) **La misma sobreafirmación de prevalencia** en `5.0:149`,
    que en `4.3.7` se bajó al nivel prudente. (2) **CUATRO ANCLAJES DE LÍNEA CADUCADOS** en
    `5.0:144-147`, **dos de ellos verificados contra disco**: el `scaler.fit` está en
    **`program.py:332`**, no en `:316`, y el `rf.fit` en **`:516`**, no en `:500`. Los otros dos **no
    se comprobaron**: recontar los cuatro antes de repuntar, no repuntar solo los dos verificados.
  - **AMPLIACIÓN del 2026-08-15, residuo declarado de la TANDA 8 — la salvedad de no-proyección a
    prevalencia, INLINE en `5.1`/`5.2`/`5.3`. LO DECIDE FRANCISCO, no un agente.** La Tanda 8 corrigió
    **la afirmación de `6.1`** —la salvedad se declara **una sola vez**, en el límite 2 de `6.1.4.1`,
    como instancia del enunciado de marco de `2.3.3:53`— y **NO** sembró declaraciones por todo el
    capítulo 5. **El razonamiento, que queda escrito para no rediscutirlo:** `6.1:66` es una
    **metaafirmación sobre el documento**, así que sembrar la salvedad junto a cada cifra de precisión
    sería **cambio de contenido en notas que están bajo esta ficha (T11)**, sin decisión de Francisco,
    y **obligaría igualmente a reescribir `6.1:66`**. O sea: hacerlo por iniciativa propia no ahorraba
    el trabajo, solo lo hacía sin permiso. Si Francisco quiere además la versión inline, **se ejecuta
    desde aquí**, no como ficha suelta.
  - `5.2` · **dispersión de T4, YA MEDIDA: los intervalos RF/HGB SÍ se solapan, así que hay que
    escribir que el orden NO queda establecido.** `f1_macro` RF-54 **[0,7779–0,8205]** vs HGB-54
    **[0,7680–0,8327]**, y el **máximo de HGB supera la media de RF**; como observación **pareada**,
    RF gana en **8 de 10** semillas. Tres cosas más que este capítulo tiene que absorber:
    (a) **el titular publicado de firmas (54-RF `f1_macro` 0,8223) es el punto más favorable de once
    corridas** —por encima del **máximo** de las diez semillas (**0,8205**), media **0,8035**—, así
    que **la banda va junto al titular**, y en **122** el mismo modelo cae **al otro lado**; (b) el
    hueco **Autoencoder vs IsolationForest SÍ aguanta** (bandas **disjuntas** en `f1`, AE **10 de
    10**), pero el contraste publicado **0,8605 vs 0,8257** son *accuracies* y `accuracy` **no está en
    la lista cerrada de `ESPECIFICACION` para anomalías**: **no figura en la tabla de dispersión**,
    cítese por `f1`; (c) **la semilla 42 cae fuera de la banda en 13 de 98 celdas** — recuento
    **automatizado** (`9d4c26d`), que **sale del artefacto** y **se puede citar**, con las **tres
    salvedades detalladas en T7**, que van escritas al lado y no omitidas.
    Y **la decisión de balanceo de `4.3.4` no es constante entre semillas.** **DECIDIDO por Francisco
    el 2026-08-14 (Decisión 1 de la Fase 0): NO se reabre el eje; se DECLARA NO CONSTANTE.** No se
    toca `firmas.py` y no se mueve ninguna cifra publicada. **T11 lo CONSUME y lo redacta en `5.4` (y
    la nota correspondiente de `4.3.4`), y se escribe exactamente así:**
    - **Qué ganó con la semilla 42** en el eje SMOTE vs `class_weight` —que solo aplica a
      **DecisionTree y RandomForest**—, verificado contra `Resultados/metricas_balanceo.csv` (16
      filas, sello `1163c90`, 2026-08-09): 54-DecisionTree `class_weight` **0,9530 ± 0,0087** vs
      SMOTE **0,9350 ± 0,0165**; 54-RandomForest SMOTE **0,9736 ± 0,0079** vs `class_weight`
      **0,9715 ± 0,0147**; 122-DecisionTree `class_weight` **0,9568 ± 0,0118** vs SMOTE
      **0,9513 ± 0,0184**; 122-RandomForest SMOTE **0,9795 ± 0,0099** vs `class_weight`
      **0,9751 ± 0,0186**.
    - **Con n=1 el reparto YA era 2-2** (DecisionTree para `class_weight`, RandomForest para SMOTE, en
      las dos variantes). A n=10 es **17 de 40 (42,5 %)**. El barrido **no descubre que la decisión
      estuviera mal: confirma que ese eje nunca estuvo establecido.**
    - **Los márgenes están dentro del ruido:** RandomForest-54 decide por **0,0021**, un margen **~7
      veces menor que su propia sd** (0,0079 y 0,0147). Es un **desempate arbitrario** y así se
      escribe.
    - **ACOTACIÓN OBLIGATORIA, no omitirla:** el «no es constante» aplica **solo al eje SMOTE vs
      `class_weight`**. **El eje SMOTE vs NADA (KNN e HistGradientBoosting) SÍ está establecido**:
      SMOTE gana en las **4 celdas**, y en HistGradientBoosting con holgura enorme —**0,9694 vs
      0,8327** (54) y **0,9724 vs 0,8044** (122)—. Sin esta acotación se entiende que todo `4.3.4` es
      arbitrario, **y no lo es**.
    - **Configuración publicada, verificada en `firmas.py:146`** (`self.balanceo_ganador` alimenta el
      entrenamiento final), **idéntica en las dos variantes**: DecisionTree → `class_weight`;
      RandomForest, KNN e HistGradientBoosting → **SMOTE**.
    - **Causa mecánica del 17 de 40, a citar AL LADO del recuento** (`firmas.py:40`, cabecera):
      cambiar la semilla cambia el `StratifiedKFold`, así que **el ganador de `4.3.4` y la config del
      grid pueden cambiar con ella**.
    - **RESIDUO ANOTADO EL 2026-08-16, salido de la auditoría de la TANDA 12 — comprobar que `5.2` y
      `A.3` NO repitan el par `0,804 / 0,822` como orden ESTABLECIDO.** En la Tanda 12 se cazó
      exactamente ese defecto en `3.5`, que lo llamaba «apoyo duro» cuando `A.3` declara el orden **no
      establecido** (bandas solapadas, y la semilla 42 de RandomForest **fuera de su propia banda**).
      Corregido allí a la forma **pareada** —**RF gana en 8 de 10 semillas**—; **queda por verificar si
      la misma formulación absoluta sigue viva en las notas de esta ficha**. **Es verificación, no
      corrección presupuesta:** puede estar ya bien.
  - `5.3`: **el 13,4 % de enrutado a `unknown` explicado, no disculpado.** Scheirer et al.
    (umbralizar un clasificador de conjunto cerrado no acota el riesgo de espacio abierto), Bendale y
    Boult (OpenMax supera explícitamente al umbralizado de la salida probabilística, que es el
    mecanismo de `UMBRAL_CONF`), Chow (la regla de rechazo es óptima sobre las posteriores
    verdaderas). Pasa de «esto nos ha salido regular» a «esto es lo que la teoría predice y lo hemos
    cuantificado».
  - `5.4` · **comparación externa reducida, cuatro párrafos y ninguna tabla grande de *accuracies***:
    (1) los criterios C1-C7; (2) la tabla pequeña de supervivientes —los 7 baselines canónicos de
    Tavallaee et al. frente al `bin_accuracy` 0,8605 del híbrido, que está **por encima del mejor**
    (NBTree 82,02 %), en la misma partición y la misma tarea— **con sus dos reservas declaradas**: la
    granularidad de etiqueta de los canónicos no está declarada en el artículo (ni la referencia
    canónica cumple C3 limpiamente) y su presupuesto de datos fue el 20 % de KDDTrain+; (3) el
    descarte y su magnitud, **apoyado en el dato citable de Goldschmidt y Chudá** (NSL-KDD aparece
    3 veces en la investigación NIDS de primer nivel 2020-2023), **no** en el ≈87 % del conteo
    propio, que es una muestra acotada de búsqueda web y así debe declararse; (4) el hueco: no se ha
    encontrado trabajo verificable que reporte recall por tipo sobre los 17 tipos ausentes con FPR
    declarado — formulado como «no lo he encontrado en la literatura revisada», no como «nadie lo
    hace».
  - `5.4` · **Hindy et al. 2020 se cita por el método, no por el número.** Su 89-99 % incumple C7 (su
    «0-day» es toda clase de ataque; agrupan ataques de KDDTrain+ y KDDTest+; barren umbral sin fijar
    punto de operación, FPR ≈15-21 % frente al 0,1017 de este proyecto). Lo comparable y valioso es
    la forma: precedente de nivel 1 de que el desglose por clase es la manera correcta de reportar un
    detector de 0-day, y de que un AE supera a un OCSVM en esa tarea — que es lo que mide
    `metricas_anomalias.csv` (AE `roc_auc` 0,9288 vs OCSVM 0,8360 en 54).
  - `5.4` · **proyección a prevalencia realista** (mitad viable de P9, cero código): D2 tiene 43 % de
    tráfico normal y el tráfico real ronda el 99 %; con `bin_recall` 0,8318 y `bin_fpr` 0,1017 se
    proyecta la precisión a prevalencia realista. El resultado va a ser incómodo, **y ese es el
    punto**: enseña que un FPR del 10 % es un problema operativo, no un decimal. Es NIST SP 800-94 y
    la falacia de la tasa base de Axelsson (ya en el guion de `2.2.4`).
  - `5.1` o `5.4` · **el desplazamiento D1→D2 medido y atribuido** con el KS de T2. Nombrarlo con
    precisión: **desplazamiento entre particiones, no deriva temporal** — sin esa precisión la
    afirmación se cae en cuanto alguien pregunte por la marca de tiempo. El umbral p95 promete ≈5 %
    de FPR y el real es **10,2 % en 54 y 8,5 % en 122** (`metricas_hibrido.csv`, `bin_fpr`); el exceso
    tiene explicación medible **sin necesidad de reloj**.
    → **Las cifras de T2 ya existen (cierre del 2026-08-10):** el drift KS son **dos mediciones
    separadas y no intercambiables** — (A) D1 vs D2 completo: **37/54** y **44/122** características
    con drift; (B) D1 vs las **9.711 normales de D2**: **25/54** y **31/122** (`src_bytes` 0,346 →
    0,091, `dst_bytes` 0,317 → 0,107). El `delta = (A) − (B)` **se publica como comparación, nunca
    como descomposición aditiva**: el KS es un supremo de diferencia de CDF y no es aditivo sobre una
    mezcla. La salvedad está impresa en los dos informes de validación; escribirla también aquí.
    → **Estrechamiento decidido por Francisco el 2026-08-11: T11 pasa a INTERPRETAR, no a publicar.**
    `4.2.1` es la **FUENTE NUMÉRICA** del KS y `5.1` la usa **por referencia, sin repetir cifras**.
    Las cifras de (A) y (B) y la salvedad del `delta` se publican **una sola vez, en `4.2.1`**; aquí se
    citan y se interpretan. Registrado como decisión en `resumen-de-decisiones.md`
    (§ Decisiones del 2026-08-11).

> **T12 — CERRADA el 2026-08-15 en la TANDA 7** (ver `## Cerradas`).
> `Obsidian_TFG_Vault/06 Conclusiones/6.2 Líneas futuras.md` pasa de **placeholder** (688 B, una de
> las tres notas vacías del recuento) a **documento entero**: **+341/-8 líneas**, redactado desde
> `EL_FUTURO.md`. **No se vuelve a encargar.** Recordatorio para la revisión final, que sigue siendo
> de Francisco por la decisión marco (b): **`6.2` es borrador de agente con revisión suya**, y esa
> revisión **no** está hecha. Lo que deja vivo tiene ficha propia: **8 de los 20 `[CITA: …]` nuevos**
> son de esta nota, y el hallazgo 🔴 **(a)** —el `[!todo]` falso del 13,4 % en `6.2:84-88`—. Se deja
> esta línea para que nadie la vuelva a despachar; el encargo original vive en git.

- [ ] **T14 · Cerrar las verificaciones pendientes** · — · `researcher`
  Francisco **no tiene acceso institucional**. **Esta es la ficha ejecutable y el inventario completo
  vive solo aquí** (consolidado el 2026-08-09: la ficha de guardia «PDF sin acceso institucional»
  duplicaba el mismo listado y se ha reducido a su función propia, con puntero a T14).
  **Las siete verificaciones — 3 degradadas + 5 cerradas por escrito.** Criterio de cierre aplicado
  a las cinco últimas el 2026-08-06: **«no verificable sin acceso institucional; no sostiene ninguna
  afirmación del trabajo»**. Cerrarlas explícitamente vale más que dejarlas como deuda flotante.
  - Citadas **degradadas** (3):
    - `Yin et al. 2017` y `Khraisat et al. 2020`: se citan **sin cifra** (metadatos verificados).
    - `Kim et al. 2014`: se cita **por su resumen**, y `3.2.2` declara que la comparabilidad exacta de
      su métrica de desconocidos no se ha podido verificar.
  - **Cerradas por escrito** (5): Arp Fig. 1 · Shyaa et al. texto completo · MDPI *Algorithms*
    18(12):749 · columnas de tiempo de UNSW-NB15 · la CV de Shone et al.
  - **DECISIÓN 4 de la Fase 0 (Francisco, 2026-08-14): NO se cierra T14 como «no disponible». Los
    puntos quedan MARCADOS.** Decisión literal: quizá pueda encontrar esa información en otras
    fuentes; **al revisar el informe completo, al final de todo, irá revisando esos puntos y verá de
    dónde sacar las citas**. **T14 sigue ABIERTA y cambia de naturaleza:** deja de ser «cerrar por
    criterio» y pasa a ser **inventario de puntos a revisar por Francisco en la revisión final**.
  - **Hallazgo verificado en el vault el 2026-08-14: NINGUNA nota de la memoria cita hoy ninguna de
    esas fuentes.** El único hit fuera de `99 Investigación/` es «UNSW-NB15» en el **guion** de
    `2.3.2`, y es **coincidencia de cadena** (habla del panorama de datasets, no de las columnas de
    tiempo). **Kim et al. 2014 NO está en `3.2.2`**: esa cita es **trabajo pendiente de T9**.
    **⚠️ CADUCADO EL 2026-08-17 — Y NO LO SUSTITUYAS POR SU CONTRARIO. T9 está CERRADA (`198fab6`),
    así que «pendiente de T9» ya no dice nada; pero la Tanda 12 arrastró además un «Kim et al.
    duplicado», así que el estado real de esa cita en `3.2.2` **hay que VERIFICARLO contra disco antes
    de repetirlo**. No lo des por cierto ni por falso desde este registro.**
  - **Consecuencia: el marcado NO se puede hacer ahora**, porque las notas que citarán esas fuentes
    **no están escritas**. Se convierte en **REGLA PERMANENTE para el `redactor-tfg`**: toda nota que
    cite una de esas fuentes **nace con un marcador VISIBLE DENTRO de la nota** —
    `> [!warning] Verificación pendiente — sin acceso al texto completo`—, **no solo anotado en
    `features.md`**. Marcarlo solo aquí no sirve: **Francisco revisará el informe, no el registro.**
    (Escribir la regla en `.claude/agents/redactor-tfg.md` es **andamiaje del hilo principal**.)
  - **El único que merece la pena reabrir si aparece acceso es `Kim et al. 2014`:** es el
    **antagonista directo de `3.2.2`** (mismo dataset, cascada en orden inverso) y hoy se cita **por
    el abstract**. Los otros seis **no sostienen ninguna afirmación**.
  - **DISCREPANCIA ARITMÉTICA a cuadrar AL EJECUTAR T14, sin resolverla por iniciativa de nadie:**
    esta ficha dice «**siete verificaciones — 3 degradadas + 5 cerradas**», y **3+5 son OCHO**.
    Lectura probable (**NO verificada**): las degradadas son **2 ítems** (Yin y Khraisat en un bullet,
    Kim en otro) con **3 citas** afectadas, luego **2+5=7**. Un apéndice que **declare siete y liste
    ocho** es justo el detalle que ve un tribunal.
  - **AÑADIDO el 2026-08-15, residuo de T13 · las cifras de Hwang et al. 2007.** «60 % / 30 % / 22 %,
    <3 % de falsas alarmas y +33 % sobre SNORT», citadas en `EL_FUTURO.md:96`, **no están verificadas
    contra el texto completo**; la propia entrada de `EL_FUTURO.md` lo deja marcado. Si llegan a
    **`6.2` (T12)** sin verificar, se degradan a «reportan mejoras» **sin cifra**, igual que se hizo
    con Yin et al. 2017 y Khraisat et al. 2020. **No entra en el recuento de «siete» de arriba**: es
    un ítem nuevo, posterior al inventario, y por tanto **no toca la discrepancia aritmética**.

> **T16 — CERRADA el 2026-08-18, SATISFECHA POR AGOTAMIENTO, no por volcado.** Contado contra disco:
> **no queda ni un `[CITA: …]` vivo en la memoria** —el último era el de `1.2:14`, retirado en el pase
> de hoy; las ocurrencias restantes en `4.2`, `1.2`, `00 Índice TFG.md` y los informes son **prosa
> sobre la convención**, no marcadores—. Luego **no hay ninguna fuente citada en el texto que siga sin
> entrada**, y volcar las **no citadas** es exactamente lo que su regla dura prohíbe. Su ficha vive ya
> en `## Cerradas`.

- [x] ~~**T16 · B2: volcado de fuentes, DESPUÉS de la redacción** · — · `researcher`~~
  **Va después de la redacción (T8-T13): no se arranca antes.** Regla dura: **ninguna entrada sin
  cita en el texto.** Los cuatro informes aportan ≈40 fuentes con datos completos y nivel asignado;
  se filtran por el mapa de T8-T12. Estimación: entran 25-30. Volcar ahora produciría una
  bibliografía inflada con entradas que no aparecen citadas en ningún sitio — lo contrario del rigor
  que busca todo este lote.
  - **AVISO PARA EL PASE EN SERIE DE `[CITA: …]` → `[n]` (2026-08-14, Tanda 4):** el bloque `2.2`
    quedó redactado **sin un solo `[n]` nuevo** y sin renumerar ninguno preexistente, tal como manda
    el protocolo. **Anderson 1980 ya es `[2]` y Denning 1987 ya es `[3]`: en ese pase hay que
    MAPEAR a los números existentes, NO dar de alta entradas nuevas.** Darlas de alta duplicaría dos
    referencias que ya están en `Bibliografía.md`.

> **T17 — CERRADA el 2026-08-18 en la TANDA 26** (ver `## Cerradas`). **La cierran sus dos puntos,
> ejecutados hoy:** el bloque «Decisiones tomadas a partir de este informe» **en los cuatro informes** de
> `99 Investigación/` —con las dos declaraciones caducadas sobre `6.2` corregidas en la misma pasada— y la
> **deriva de documentación de `evaluacion.py`**, corregida en `next-steps.md` §6.5b (nota fechada, **sin
> tocar casillas**) y en `Guia_ML/03_validacion_y_metricas.md` §7, verificadas **función a función**.
> **Lo que deja vivo NO es T17, son fichas propias más abajo:** la deriva sigue en pie en **`CLAUDE.md:64`**
> y en **Q3 de `resumen-de-decisiones.md`**, que un agente no toca. **No se vuelve a despachar.** Se conserva
> su texto solo como historial.

- [x] **T17 · Volcar las decisiones del grill a `resumen-de-decisiones.md`** · — · `cronista` + `redactor-tfg`
  Acompaña cada cierre del lote. **Parcialmente cubierta:** el volcado a `resumen-de-decisiones.md`
  está hecho (§ Decisiones del 2026-08-06 y del 2026-08-09, más sus dos entradas de bitácora) —
  reapertura declarada del track de código con alcance y motivo, retirada de la regla de autoría en
  dos velocidades, criterio rector del lote, renuncia al p-valor, anclaje de `[6]` en `2.1.4` con sus
  tres descartes, y las conclusiones de diseño de T18 y T22.
  **Sigue pendiente, y es lo que mantiene la ficha abierta:**
  1. El bloque «Decisiones tomadas a partir de este informe» en **cada uno de los cuatro informes** de
     `Obsidian_TFG_Vault/99 Investigación/`, con qué se convirtió en decisión y qué se descartó. En la
     misma pasada se corrige que **dos de ellos siguen diciendo que `6.2` la redacta Francisco**
     (`aprendizaje-continuo-nested-learning.md:25` y
     `clasificadores-tabulares-y-arquitecturas-hibridas.md:30`), cuando la decisión marco (b) la pasó
     a **borrador del `redactor-tfg` con revisión final de Francisco**.
  2. La **deriva de documentación de `evaluacion.py`**: su contrato cambió con T1 y sigue descrito en
     la forma anterior en `CLAUDE.md:63`, `next-steps.md:621`,
     `resumen-de-decisiones.md:319,343` y `Guia_ML\03_validacion_y_metricas.md:153`.

- [ ] **PDF sin acceso institucional — reabrir si Francisco consigue acceso** · — · `researcher`
  Ficha de guardia abierta el 2026-08-06 junto a T14. **Su única función es esa: quedarse de guardia.**
  Si Francisco consigue acceso institucional, se reabren las verificaciones degradadas o cerradas por
  escrito y se revisa qué afirmaciones pueden dejar de ir con salvedad.
  **El inventario de las siete verificaciones (3 degradadas + 5 cerradas) está en T14**, que es la
  ficha ejecutable. Se retiró de aquí el 2026-08-09 por duplicado; no volver a copiarlo.

### Residuos de T1 — altas del 2026-08-08

> T1 se cerró en su objetivo (ver `## Cerradas`, `5f98d88`). Estas cinco fichas son lo que **quedó
> fuera** de ese cierre, anotado con el detalle necesario para retomarlo en frío.
>
> **Dato transversal que no debe perderse:** las corridas anteriores **están en git**
> (`077119e` guarda la del código `c7cf319`; `34bee30` la de `38fdd4b`), así que los
> `.esquema-anterior.bak` son **prescindibles** y **cualquier cita a una corrida vieja debe apuntar
> al commit, nunca al `.bak`**.

> **T19 — CERRADA el 2026-08-17 en la TANDA 18** (ver `## Cerradas`). Sus **cuatro** sedes están
> resueltas: `5.1:44-47`, `5.1:58` y `5.2:59` en la Tanda 17, y **`4.4 …anomalías.md`** —la última, y
> la que contradecía a `5.1`— en la 18. **No se vuelve a despachar.**
>
> ⚠️ **La ficha de T19 sembraba DOS afirmaciones FALSAS y por eso se retira su texto, no solo su
> casilla.** Decían que la banda de **4,8×** del Autoencoder se da «con el recuento de épocas
> idéntico» y que el reparto interno «conserva **el orden de las ocho filas**». **Las dos son
> falsas** y llegaron a publicarse en dos notas antes de cazarse:
> 1. Las dos corridas de la banda 4,8× (`38fdd4b` → `5516b60`) **NO registran épocas**
>    (`PIPELINE.md:923-929`); `n_iter_total_grid` solo existe en `ac496cb` y `1163c90`. La banda se
>    declara como **magnitud observada, SIN causa atribuida** — ni a épocas ni a carga de máquina.
> 2. El orden se conserva **casi entero, no entero**: `IsolationForest` 122 **baja del 4.º al 6.º**
>    puesto. Y los **4,5 pp** son del **residual**, no de «cada tramo».
>
> **La formulación correcta, si alguien necesita reusarla, está en `4.4` y en `A.3:417-431`**, con la
> salvedad obligatoria de que **`ac496cb` no es reproducible desde git**.

> **T21 — CERRADA el 2026-08-18 en la TANDA 24** (ver `## Cerradas`): `5.4` declara ya que
> `latencia_ms_por_flujo` mide **solo `predict`/`score`** sobre características ya calculadas y en
> memoria —el **coste real de despliegue** (captura, ensamblado de flujo, extracción de las 41
> características) **no está medido**—, y que la cifra es **techo de inferencia en laboratorio, no
> capacidad operativa**. Citarla sin esa salvedad sería el propio pitfall **P9** (*Lab-Only
> Evaluation*) que se dice estar cubriendo.
>
> ⚠️ **La ficha citaba «4,4 millones de flujos/s» y esa cifra NO EXISTE EN NINGÚN ARTEFACTO DE DISCO.**
> El valor real es **4.196.350,2 flujos/s** con latencia **0,000238 ms** (DecisionTree,
> `set_features=54`, `semilla=42`, `commit=1163c90`, `Resultados/metricas_firmas.csv:2`). El auditor
> verificó que **la única aparición de ese «4,4» en todo el repo era esta propia ficha**
> (`features.md:1366`), ya retirada aquí. Mismo patrón que el precedente del «13 de 98».

### Residuos de T15 y T18 — altas del 2026-08-09

> T15 (auditoría de `Bibliografía.md`) y T18 (rediseño de `alcance_tiempo_s`) se cerraron el
> 2026-08-09 (ver `## Cerradas`). Estas tres fichas son lo que **quedó fuera** de esos cierres.

> **T23 — CERRADA el 2026-08-18.** Su propio texto declaraba que **P5 y P6 eran lo único que la
> mantenía abierta**, más la P4 que la TANDA 25 dejó sin aplicar. El pase en serie del `researcher`
> del 2026-08-18 cierra las tres: P4 anclada a `[26]`, P4-bis retirada, y P5/P6 **marcadas** en
> `Bibliografía.md`. Su ficha vive ya en `## Cerradas`.

- [x] ~~**T23 · Correcciones del texto que la auditoría de bibliografía dejó sin autorizar** · Informe · `redactor-tfg`~~
  Salen del informe `Obsidian_TFG_Vault/99 Investigación/Auditoría de Bibliografía.md` (T15). Son las
  correcciones de texto que **no estaban autorizadas** en aquel encargo y por tanto no se aplicaron.
  **Fuera de esta ficha, ya ejecutadas:** reformular `1.1:12` al dato agregado de INCIBE, repuntar
  `2.1.2:30,64` de `[6]` a `[5]`, y `2.2.1:32` de `[9]` a `[8]`.
  > **CUERPO CADUCADO — marcado el 2026-08-18.** Todo lo que sigue describe el estado **anterior**
  > al pase en serie del `researcher`, y **T23 ya está CERRADA** (ver `## Cerradas`). En concreto,
  > **el punto P4 de abajo es FALSO en disco**: el párrafo de Snort **sí tiene cita**, `1.2:32`
  > apunta a `[26]` con un callout que explica **LISA'99 vs 1998**, y `[26]` se **mapeó** en vez de
  > duplicarse. **Sexta ocurrencia del patrón de registro caducado.** Se conserva el texto como
  > traza histórica; **no se ejecuta nada de aquí**.

  **CIERRE PARCIAL en la TANDA 25 (2026-08-18) — ~~la ficha SIGUE ABIERTA~~ (ya cerrada):**
  - **P1–P3: ya estaban ejecutadas** (constaba en esta misma ficha).
  - **P4: NO aplicada — la Tanda 25 marcó una afirmación DISTINTA de la decidida.** La decisión de
    Francisco (2026-08-17) era anclar el pasaje de **Roesch y Snort** al paper primario de **LISA'99
    (USENIX)**, y **eso sigue sin hacerse**: el pasaje de Snort, hoy en `1.2:27`, **no tiene ninguna
    cita**. Lo que sí se aplicó en `1.2:14` fue un **`[CITA: …]` + `[!todo]`** sobre la afirmación de
    **Anderson como punto de partida de la detección de intrusiones** —que **no estaba en la ficha
    P4**— y que queda como **segunda afirmación sin aval**. **P4 SIGUE ABIERTA**: ver la divergencia
    registrada en su propia ficha (`features.md:700`, «P4 · falta aval de nivel 1 para `1.2:14`»).
  - **P5 y P6: NO se aplican aquí.** Caen en `Bibliografía.md` —edición de Stallings `[8]` y *deep
    link* de `[10]` CCN-STIC-401— y son **decisión de Francisco**. Van al **pase en serie del
    `researcher`** del final del barrido. **Es lo único que mantiene abierta T23.**

> **T24 y T25 — CERRADAS el 2026-08-15 en la TANDA 11** (`d31e20f`, ver `## Cerradas`). `2.1.4` ya
> tiene su bloque de redes neuronales y **`2.1.4.3` ancla `[6]` (Goodfellow) con `[6, cap. 6]`**,
> aplicando la decisión de Francisco del 2026-08-09 —referencia canónica **del concepto** de error de
> reconstrucción, **sin** afirmar que el modelo del TFG sea profundo—. **`[6] ya NO está huérfana:
> 7 ocurrencias verificadas en disco por el hilo principal.** **No se vuelven a encargar.**
> **Lo que dejan vivo tiene ficha propia, abajo:** `Bibliografía.md` **sigue declarando `[6]`
> huérfana en tres sitios** (`:75`, `:63` y `:199`) y arrastra las otras dos correcciones que T25
> encargaba — **fichero del `researcher`, y por eso no se resuelve aquí**.

### Migración de `next-steps.md` §3.2 — altas del 2026-08-11

> Las dos fichas siguientes salen de la **migración de la deuda técnica de `next-steps.md` §3.2**,
> hecha el **2026-08-11**: eran casillas `☐` dentro de un fichero congelado, donde nadie las miraba.
> **§3.2 y §3.3 quedan como historial**, sin reescribir ni una casilla; el estado vivo de lo que siga
> abierto es **este**.
>
> De las **cinco** fichas migradas, **tres están cerradas** (ver `## Cerradas`): las de
> `validacion.py`, completadas sobre el código WIP de `d9225be` **sin reescribir sus ~231 líneas** y
> **re-corridas en las dos variantes** (`EXITCODE=0`, `Integridad: APROBADA`, 16 artefactos
> regenerados el 2026-08-11 19:28). También se cerraron las **constantes duplicadas** —Francisco
> decidió ejecutarlo, no aceptarlo como deuda—: son ahora de **módulo** en `program.py:36-37` y
> `validacion.py` las importa. **De las dos que quedaban, la de las RUTAS ABSOLUTAS se retiró el
> 2026-08-14 por la Decisión 2 de la Fase 0** (no se regeneran los splits): ver `## Cerradas`; se
> declara como límite conocido en `A.3`, dentro de **T7**. **La quinta y última, la del
> `warnings.filterwarnings('ignore')` global, se CERRÓ el 2026-08-14** en la Fase 1 del plan de
> cierre (ver `## Cerradas`). **Esta sección queda sin fichas abiertas.**

### Residuos del despacho de `4.2` — altas del 2026-08-12

> Salen del cierre **en una sola pasada de `redactor-tfg`** de las dos fichas de
> `Obsidian_TFG_Vault\04 Implementación del sistema\4.2 Base de datos utilizada.md` (la «mediana» de
> `:107` y el KS (B) de `:110`), con dictamen **APTO CON CAMBIOS** de `auditor-ml`: sin leakage, sin
> cifras caducadas, sin hash inventado y sin invadir T10. **Ninguno de estos residuos es 🔴.** La
> cuarta observación de esa auditoría —el «~33 %» de DoS de `4.2:72`, que está sobre D2 entero y no
> sobre sus ataques (**58,1 %**)— **no abre ficha: es preexistente y queda anclada dentro de T10**.

> **La segunda ficha de esta sección —«Dos imprecisiones de una línea en `4.2`»— se CERRÓ el
> 2026-08-14** en la Fase 1 del plan de cierre, junto con la del sello de `4.2:145` (ver
> `## Cerradas`). **La de las figuras de `assets\` se CERRÓ el 2026-08-15**, sus dos mitades, con el
> barrido de disco que la respalda (ver `## Cerradas`): **esta sección ya no tiene fichas abiertas.**
> El inventario de
> **texto congelado o histórico que arrastra el rango de FPR viejo y que NO se toca** (es foto de su
> fecha) se conserva aquí para que nadie lo «corrija»: `next-steps.md:178,370,451`,
> `resumen-de-decisiones.md:346,580`, `EL_FUTURO.md:96`, `sesion-2026-07-06.md:66`,
> `Guia_ML\04_los_tres_modelos.md:35` y los tres informes de
> `Obsidian_TFG_Vault\99 Investigación\`, que **no es memoria**.

### Residuos del clúster de `PIPELINE.md` — altas del 2026-08-12

> Salen del cierre **en una sola pasada** de las **cinco fichas de `PIPELINE.md`** (ver
> `## Cerradas`), con dictamen **APTO CON CAMBIOS** de `auditor-ml`, todo aplicado. **Documentación
> pura: ningún script de `app/` tocado, ninguna corrida, ninguna cifra publicada movida.** **Ninguno
> de estos residuos es 🔴.**
>
> **Anclas vigentes de `PIPELINE.md` tras ese cierre, contadas en disco el 2026-08-12** (el fichero
> creció ~40 líneas): tabla canónica del sello en **`:994`** (encabezado) + **`:1001-1005`** (valores);
> glosa del `-sucio` en **`:186-190`**, colgando de su primera aparición en **`:184`**; las tres filas
> de la tabla de corridas en **`:369-371`**; y el bloque citable de **T20** en **`:493-498`**.

> **Las DOS fichas de esta sección se CERRARON el 2026-08-14** en la Fase 1 del plan de cierre (ver
> `## Cerradas`): la de `resumen-de-decisiones.md:820-821` —resuelta con **nota fechada**, primera
> aplicación del permiso ACOTADO de la Decisión 3— y la del **sello de `4.2:145`**, re-anclado a
> **`9af842c`** conservando literal el `fc1c6b4-sucio` impreso dentro del artefacto. **Esta sección
> queda sin fichas abiertas.** Las **anclas vigentes de `PIPELINE.md`** del recuadro de arriba **se
> conservan**: siguen siendo la referencia de quien cite ese fichero.

### Apuntes de relectura de la memoria — alta del 2026-08-12

- [ ] **`1.4`: qué conceptos de IA entran de verdad en el capítulo 2, y resúmenes de capítulo demasiado escuetos** · Informe · `redactor-tfg`
  Sale de la **relectura de la memoria completa** que está haciendo Francisco. **Fuente viva:
  `mis-apuntes-del-informe.md`**, en la raíz del repo. Ese fichero es **incremental**: Francisco lo
  sigue ampliando conforme relee, así que **al ejecutar esta ficha hay que releerlo entero** y
  trabajar sobre lo que diga ese día — **no fiarse de lo copiado aquí**, que es solo el estado del
  **2026-08-12**.
  - **ORDEN — se ejecuta LA ÚLTIMA:** después de **todas** las fichas abiertas hoy en este fichero.
    Lo pidió Francisco el **2026-08-12**.
  1. **`1.4` dice que el capítulo 2 introduce los conceptos en tres bloques, uno de ellos de IA** —
     y la pregunta de Francisco es **qué conceptos de IA se están incluyendo realmente, si es que
     hay alguno**. O el capítulo 2 cumple lo que `1.4` promete, o hay que ajustar una de las dos
     partes.
  2. **El resumen de cada capítulo en `1.4` es excesivamente escueto.**
  - **DELIMITACIÓN DURA — no absorbe ni sustituye a `T24` ni a `T25`.** `T24` (`2.1.4 Algoritmos de
    ML` sin bloque de redes neuronales) y `T25` (anclaje de `[6]` Goodfellow en ese mismo bloque)
    son **una nota concreta y un hueco concreto**. Esta ficha es otra cosa: pregunta si el
    **capítulo 2 en su conjunto cumple lo que `1.4` promete** sobre el bloque de IA, y **añade el
    punto de los resúmenes escuetos, que no está en ninguna ficha**.
  - **ALCANCE NO CERRADO:** cuando le llegue el turno hará falta un **`grill-me` con Francisco**.
    «Qué conceptos de IA entran en el capítulo 2» es una **decisión de contenido** y **no la puede
    tomar un agente**.

- [ ] **`2.1` · coherencia y densidad del guion teórico** · Informe · `redactor-tfg`
  Sale de la misma relectura. **Fuente viva: `mis-apuntes-del-informe.md`**, en la raíz del repo.
  Ese fichero es **incremental**: Francisco lo sigue ampliando conforme relee, así que **al
  ejecutar esta ficha hay que releerlo entero** y trabajar sobre lo que diga ese día — **no fiarse
  de lo anotado aquí**, que es solo el estado del **2026-08-12**.
  1. `mis-apuntes-del-informe.md:13` — `2.1.1` introduce la IA en un punto que Francisco considera
     equivocado: la definición debe ir **más adelante**, aunque la comparación IA/ML sí aporta
     perspectiva ahí.
  2. `mis-apuntes-del-informe.md:16` — la figura de `1.4` menciona el **aprendizaje continuo** y no
     está definido en ningún sitio; Francisco propone definirlo. **Punto de contacto con `T12`**
     (`6.2 Líneas futuras`), que es donde vive el material de aprendizaje continuo: **no duplicar**,
     decidir qué se define en `2.x` y qué se queda en `6.2`.
  3. `mis-apuntes-del-informe.md:18` y `:22` — en `2.1.3`, etapa 3, se citan juntos
     *cross-validation*, N-fold y desviación estándar; Francisco pregunta si son **tres cosas
     distintas** y si la frase de validación cruzada es un punto propio de la enumeración o va
     dentro de «Medir y comparar su rendimiento».
  4. `mis-apuntes-del-informe.md:20` — la lista larga que sigue son, presumiblemente, las
     **métricas de selección de modelo**; hay que confirmarlo y darle **encabezado propio** si lo es.
  5. `mis-apuntes-del-informe.md:26` — **asimetría de formato**: lo importante del algoritmo va en
     enumeración separada por párrafos y las propiedades que lo hacen bueno, no.
  6. `mis-apuntes-del-informe.md:28` — Francisco pregunta si el apartado incluye **demasiada
     información**. Es una **decisión de densidad, no de estilo**: converge con la ficha de la
     revisión del profesor (justo debajo), que pide simplificar. **Ejecutarlas con el mismo
     criterio.**
  - `mis-apuntes-del-informe.md:24` — **NO es trabajo de agente.** Francisco lo apunta como **tarea
    suya**: cómo maquetar las fórmulas de probabilidad dentro de la definición de la regresión
    logística. Queda anotado aquí **solo para no perderlo**.
  - **ALCANCE NO CERRADO:** «cuánta teoría sobra» y «dónde se define la IA» son **decisiones de
    contenido**; hará falta un **`grill-me` con Francisco** antes de ejecutar.

- [ ] **Revisión del profesor: simplificar, unificar y desduplicar del capítulo 3 en adelante** · Informe · `redactor-tfg`
  **El material que el profesor pide quitar del cuerpo se MUEVE al apéndice `A.3 Ficha del
  sistema` (`T7`), NO se elimina.** `T7` es exactamente la *model card* donde viven semilla,
  hiperparámetros y configuraciones ganadoras; borrar esos datos rompería `T7` y la
  **reproducibilidad declarada** del trabajo.
  **Fuente viva: `mis-apuntes-del-informe.md`**, en la raíz del repo. Ese fichero es
  **incremental**: Francisco lo sigue ampliando conforme relee, así que **al ejecutar esta ficha
  hay que releerlo entero** y trabajar sobre lo que diga ese día — **no fiarse de lo anotado
  aquí**, que es solo el estado del **2026-08-12**.
  - `mis-apuntes-del-informe.md:30` y `:32` — **cita textual del profesor** tras su primer revisado
    del informe completo: mejorar la redacción, **simplificar las explicaciones de las soluciones
    analizadas sin dar todos los hiperparámetros** (su propio ejemplo: la semilla 42), y
    **recortar/unificar apartados** — señala explícitamente **los primeros apartados del
    capítulo 3**.
  - `mis-apuntes-del-informe.md:34` — encargo de Francisco: **interpretar** esas palabras, **no
    rehacer el informe**; identificar qué apartados conviene **recortar o unificar** y hacer un
    **repaso de duplicación en todo el informe**, incluidos los puntos definidos últimamente.
    Francisco confirma haber notado que **en el capítulo 3 se repiten muchas veces los mismos
    datos**.
  - **Alcance: del capítulo 3 en adelante** (es la parte redactada por agente).
  - **ALCANCE NO CERRADO:** qué se unifica y qué se recorta necesita un **`grill-me` con
    Francisco** antes de tocar ninguna nota.

### Residuos del cómputo de T4 — altas del 2026-08-13

> Salen del **cierre de sesión del 2026-08-13**, al verificar el registro contra disco tras cerrar la
> parte de cómputo de T4 (`9ad971b`). **Fichar no es resolver: aquí no se ha tocado ni una línea de
> código.** Nacieron **cuatro**: tres estaban **enterradas dentro de la fila `9ad971b` de
> `## Cerradas`** o **dentro de T11**, donde nadie las mira, y la cuarta **no estaba en ninguna
> parte**. Por la regla de este fichero —**estar en Abiertas significa estar abierto**—, hoy eran
> invisibles para quien retome el proyecto.
>
> **Estado al cerrar la sesión del 2026-08-13: de las cuatro, tres ya están cerradas** —el
> re-anclaje del sello (`ea35ce3`), la automatización del «13 de 98» (`9d4c26d`) y la Tarea B del
> bullet Q6 (`c5ceca5`)—, **y aquí abajo queda solo una**, que es decisión de Francisco. El
> encabezado dice «cuatro» porque describe el lote de altas, no lo que queda pendiente.
>
> **Estado a 2026-08-14: la cuarta, el eje de balanceo de `4.3.4`, la DECIDIÓ Francisco** (Decisión 1
> de la Fase 0) y está en `## Cerradas`. **Esta sección queda sin fichas abiertas.**

### Residuos de la automatización del «13 de 98» — altas del 2026-08-13

> Salen del ciclo que **cerró** la ficha 🟠 del recuento manual (Decisión 3 de la Fase 0 del plan de
> cierre, aprobada por Francisco el **2026-08-13**; ver `## Cerradas`). **Estado a 2026-08-14: las
> dos quedan resueltas** —la de los recuentos 94/4 y la del re-anclaje `ddade37-sucio → 9d4c26d`,
> ambas en `## Cerradas`—, pero **el re-anclaje deja descendencia**: la cuarta pasada del agregador
> imprimió un sello nuevo, y esa fue la ficha que quedó abierta aquí.
>
> **Estado a 2026-08-14: esa descendencia también queda CERRADA.** El **quinto re-anclaje**
> (`6bb224c-sucio → 1cb5c26`) se escribió en la **Tanda 3** y está en `## Cerradas`. **Esta sección
> queda sin fichas abiertas.**

### Huecos del informe detectados contra disco — altas del 2026-08-13

> Salen del **pase de verificación contra disco del 2026-08-13**, hecho al preparar el plan de cierre
> que Francisco aprobó ese mismo día. **Fichar no es resolver: aquí no se ha redactado ni una línea de
> la memoria.** La primera es **el mayor bloque de trabajo pendiente del TFG y hoy era invisible en
> este fichero**; las otras tres son residuos menores sin ficha. **Ninguna lleva commit ni fecha de
> cierre: no se ha cerrado nada.**
>
> **Recuento real del vault hoy, medido en disco: 44 notas — 31 redactadas, 8 en guion, 3 vacías**
> (`Resumen` 120 B, `Abstract` 123 B, `6.2 Líneas futuras` 688 B).

> **La ficha «La prosa de las 8 notas en guion del capítulo 2 no la encarga ninguna ficha» está
> CERRADA el 2026-08-14, 8 de 8** (Tanda 4 el bloque `2.2`, Tanda 5 las cuatro restantes): ver
> `## Cerradas`. Se deja esta línea para que nadie la vuelva a dar de alta como hueco. **Lo que
> dejó vivo, con ficha propia:** el `> [!todo]` del **diagrama de bloques del NIDS** en `2.2.2`
> (mismo cuello de `assets/` que bloquea T10) y las **7 correcciones de la Tanda 5**.
> **Las DOS quedan CERRADAS el 2026-08-15 en la TANDA 11** (`d31e20f` + `296de24`): la figura existe y
> está embebida, y de las 7 correcciones **solo sobrevive la (6)**, que es del `researcher`.

> **La ficha «Las 7 correcciones de la auditoría de la TANDA 5» — CERRADA ENTERA el 2026-08-15 en la
> TANDA 11** (`d31e20f` + `296de24`, ver `## Cerradas`). La **(1)** se resolvió por la vía de
> **redactar `2.1.5`** (con ella cae T8); la **(5)** queda resuelta —**`2.1.6` ya no adelanta el
> `0,822`**—; y las **(2), (3), (4) y (7)** estaban hechas desde la Tanda 6. **De las siete sobrevive
> SOLO la (6)**, que es del **`researcher`** y **vive en la ficha hermana de abajo**, no aquí. **No se
> vuelve a despachar.**

> **«Las 3 correcciones LOCALES de la auditoría de la TANDA 5» queda CERRADA ENTERA el 2026-08-17**:
> su última superviviente, la **(6)** («Dónde se usa» de `[2]` y `[3]`), la resolvió el pase en serie
> del `researcher`. Su ficha vive ya en `## Cerradas`. **Se deja el texto abajo como historial, sin
> casilla: no se vuelve a despachar.**

**Las 3 correcciones LOCALES de la auditoría de la TANDA 5 — CERRADA, historial** · Informe · `redactor-tfg` / `researcher`
  > **VERIFICADO CONTRA DISCO EL 2026-08-15: las correcciones (2) y (3) YA ESTÁN HECHAS**, absorbidas
  > por el pase de la **TANDA 6** sin registrarlo. **No se vuelven a despachar.** **Vive solo la
  > (6)**, que es del **`researcher`** y entra en su pase en serie.
  Alta el **2026-08-14**, misma auditoría que la ficha de arriba. **Estas tres sí son locales a un
  fichero**, así que pueden ir sueltas — pero **el punto 6 no lo toca un redactor**.
  - **(2) `2.3.3:50` promete un resultado que NO EXISTE.** El callout «Alcance de este trabajo»
    anuncia una «**proyección a prevalencia realista**» como resultado **del capítulo 5**, y esa
    proyección **no está en código, ni en `Resultados/`, ni en ninguna nota** (verificado el
    2026-08-14). **O se retira la promesa, o se decide que la proyección se hace** —y entonces es
    alcance nuevo, no una corrección de redacción, y la decide Francisco.
  - **(3) `2.3.3:85` atribuye a Arp et al. un error que NO es suyo.** Ese error **no está entre sus
    diez pitfalls verificados** (`Obsidian_TFG_Vault/99 Investigación/benchmark-comparativo-nsl-kdd.md:131`):
    es de la línea **Pierazzi et al.** Reatribuir, no borrar.
  - **(6) `Bibliografía.md:29` necesita actualizar «Dónde se usa»** por el nuevo uso de `[3]`
    (Denning 1987) en `2.3.2:36`. **Es pase del `researcher`, NO del redactor** —es el único que
    escribe ese fichero, y va **en serie**—. Encaja de forma natural en el pase de `[CITA: …]` → `[n]`
    que toca ahora al cerrar la Fase 4.
    - **SIGUE VIVA DESPUÉS DE LA TANDA 9, y hay que decirlo porque el pase en serie era justo donde
      tocaba resolverla: NO quedó cubierta.** Verificado contra disco el **2026-08-15**: el «Dónde se
      usa» de **`[3]` (Denning) OMITE `2.3.2:36`** —el uso exacto que originó esta corrección— **y
      otros tres usos**, y el de **`[2]` (Anderson) OMITE `2.2.2:35`**. **Solo el `researcher`.**

- [~] **`03 Desarrollo\` está vacía en disco y solo falta borrar la carpeta** (🟡) · Informe · `redactor-tfg`
  `00 Índice TFG.md:101-102` la marca «pendiente de borrado físico», y **además su texto afirma que
  «contiene solo avisos de migración», lo que YA ES FALSO**: en disco **no hay ni un `.md`**. Son dos
  cosas: borrar la carpeta y corregir esa frase del índice.
  - **La MITAD DE TEXTO está HECHA (2026-08-14, Tanda 3):** la frase falsa de `:101-102` quedó
    corregida. **Queda vivo solo el BORRADO FÍSICO de la carpeta**, que el `redactor-tfg` no puede
    hacer —no tiene shell—: necesita un agente con shell o a Francisco.
  - **⚠️ CADUCADA EL 2026-08-17: `Obsidian_TFG_Vault/03 Desarrollo/` YA NO EXISTE en disco, verificado.**
    El borrado físico que esta ficha dejaba vivo **está hecho**. No queda nada que despachar aquí; la
    ficha se conserva para que nadie vuelva a abrir el mismo encargo. **La retira el usuario, no yo.**
  - **⚠️ ESA «CADUCADA» ES FALSA, verificado en disco el 2026-08-17 (TANDA 21): `Obsidian_TFG_Vault/03
    Desarrollo/` SIGUE EXISTIENDO, vacía**, y el aviso de eliminación sigue vigente en
    `00 Índice TFG.md`. El borrado físico **NO está hecho**. La ficha queda **ABIERTA en su parte de
    borrado**; ficha nueva de la TANDA 21 con el detalle. **Decide Francisco:** el permiso de borrado
    concedido se limitó a `Lecture 1.md`.

> **La ficha «`00 Índice TFG.md:106` declara un recuento que no cuadra con su propio listado» queda
> CERRADA en la TANDA 21** (2026-08-17), **con criterio declarado**, que era lo que faltaba: **44
> entradas indexadas = 43 notas de memoria + `Bibliografía`**. Su ficha vive ya en `## Cerradas`.

> **Los 6 marcadores `[CITA:` de `4.2` quedan CERRADOS en la TANDA 9** (2026-08-15, `e286cce`),
> convertidos en el pase en serie del `researcher`. Ficha en `## Cerradas`. **Ojo al leer `4.2` hoy:
> los `[CITA:` que quedan en esa nota son PROSA SOBRE la conversión, no marcadores pendientes** —
> verificado contra disco al cerrar la tanda.

### Altas del cierre de sesión del 2026-08-13

> Salen del **cierre de sesión del 2026-08-13**, tras la corrección de `leader.md` y la política de
> despacho en paralelo (`0fb5f2b`). **Fichar no es resolver: ninguna de las tres se ha tocado.**
> **Ninguna lleva commit ni fecha de cierre.** Las dos últimas eran **de Francisco**: un agente puede
> presentar las opciones, no fijarlas.
>
> **Estado a 2026-08-14: las dos de Francisco están DECIDIDAS** —granularidad del commit (Decisión 7)
> y la divergencia de `resumen-de-decisiones.md:459` (Decisión 8)— y viven en `## Cerradas`. **Queda
> abierta solo la primera, la reconciliación del contador de citas.**

> **CERRADA en la TANDA 9** (2026-08-15, `e286cce`): la reconciliación del contador de citas se
> ejecutó en serie —23 marcadores mapeados, 13 resueltos con 10 altas `[58]`–`[67]`—. Su ficha vive
> ya en `## Cerradas`. **Sigue vigente la regla de la que nació: el pase va al FINAL DE CADA FASE de
> redacción, no una sola vez al final del plan**, y lo ejecuta **solo el `researcher`, en serie**.
> **Lo que NO cerró y sigue vivo: `[6]` (Goodfellow) sigue huérfana** (depende de T24) y la
> **corrección (6) de la Tanda 5** sobre «Dónde se usa» (ficha propia más abajo).

### Residuos de la TANDA 7 — altas del 2026-08-15

> Salen de la **auditoría rehecha de la TANDA 7** (la original murió por límite de API) y de la
> verificación contra disco al cerrarla. **La tanda se commiteó con dictamen NO APTO y 5 🔴 abiertos**,
> por el precedente que Francisco ratificó en la Tanda 5 y porque el trabajo llevaba **tres cortes de
> API sin respaldo en git**. **Los cinco son TEXTUALES: no mueven ninguna cifra publicada ni tocan
> código.** **Fichar no es resolver: aquí no se ha corregido nada.**

> **La ficha «`2.3.3:91` remite el modelo de amenaza CONCRETO a `3.1`, que está VACÍA» (🟠) queda
> CERRADA en la TANDA 10, pieza A** (2026-08-15, `55ef3c6`): se resolvió por la **primera** de sus dos
> vías —escribir el apartado—, con `3.1.5 Modelo de amenaza`. Su ficha vive ya en `## Cerradas`.

> **Los 20 marcadores `[CITA: …]` nuevos de la TANDA 7 (`5.0` = 5 · `6.1` = 7 · `6.2` = 8) quedan
> CERRADOS en la TANDA 9** (2026-08-15, `e286cce`), dentro del pase en serie del `researcher`. Su
> ficha vive ya en `## Cerradas`. **El contador global que este bloque llevaba está OBSOLETO: ya no
> es el `[58]`, es el `[68]`** — ver el bloque «CONTADOR GLOBAL DE CITAS» de PRÓXIMOS PASOS, que es
> el único sitio donde se mantiene esa cifra.

- [~] **Seis afirmaciones del vault que la TANDA 7 dejó desfasadas — TRES CERRADAS en la TANDA 8, UNA en la TANDA 9 y UNA en la TANDA 11; queda UNA** (🟡) · Informe · `redactor-tfg` / `researcher`
  Alta el **2026-08-15**, **las seis verificadas contra disco**. Son residuos de coherencia, no
  trabajo de redacción: cada uno es una línea que dice que algo no existe cuando ya existe.
  1. ~~**`4.2:117-118` afirma que las figuras «aún no se han copiado».**~~ **HECHO en la TANDA 8**
     (2026-08-15): `[!todo]` falso retirado **y las dos KS embebidas** desde `assets/`, más el callout
     «Fuente numérica única» acotado. **Con esto la mitad «embeber» de la ficha de figuras también
     queda servida en `4.2`.**
  2. ~~**`A.3:176-180` remite a `5.0` como inexistente.**~~ **HECHO en la TANDA 8** (2026-08-15):
     remisión corregida; y de paso `A.3:48` y `:634` repuntadas a `2.3.3`.
  3. ~~**`5.0` no está de alta en `00 Índice TFG.md`.**~~ **HECHO en la TANDA 8** (2026-08-15), en
     serie sobre el índice. **El recuento del índice se dejó intacto a propósito**: tiene ficha propia
     (ojo, la línea ya **no** es `:104` — ver esa ficha).
  4. ~~**`Bibliografía.md:153` dice «propuesta, no ejecutada» sobre algo que YA está ejecutado.**~~
     **HECHO en la TANDA 9** (2026-08-15, `e286cce`): el `researcher` corrigió **tres callouts** que
     declaraban «propuesta, no ejecutada» sobre acciones que el disco demuestra ya ejecutadas.
  5. **Los números de línea de T25 están desplazados** por el callout que la Tanda 6 insertó en
     `Bibliografía.md`. Anotado también dentro de la propia ficha de T25: **localizar por contenido**.
  6. ~~**`[6]` (Goodfellow) sigue HUÉRFANA en todo el vault.**~~ **RESUELTO en la TANDA 11**
     (2026-08-15, `d31e20f`): `2.1.4.3` la ancla con **`[6, cap. 6]`**, **7 ocurrencias verificadas en
     disco**. **PERO el registro bibliográfico NO se ha enterado:** `Bibliografía.md:75`, `:63` y
     `:199` **la siguen declarando huérfana**. Esa corrección es del **`researcher`** y va en su ficha
     propia, más abajo.

### Residuos de la TANDA 9 — altas del 2026-08-15

> Salen del **pase EN SERIE del `researcher`** (`[CITA: …]` → `[n]`) y de su auditoría, **APTO CON
> CAMBIOS y sin ningún 🔴**. **Ninguno es bloqueante** y **ninguno mueve una cifra publicada.**
> **Todos tocan `Bibliografía.md` o `99 Investigación/`, así que son del `researcher` y van EN
> SERIE.** **Fichar no es resolver: aquí no se ha corregido nada.**
>
> **La corrección (6) de la Tanda 5 —«Dónde se usa» de `[2]` y `[3]`— también es residuo de esta
> tanda**, pero NO se duplica aquí: está anotada dentro de su ficha original, más arriba.

> **Las CUATRO fichas de este bloque quedan CERRADAS el 2026-08-17** en el pase en serie del
> `researcher` —la leyenda `— (no es libro)` de `:58`, la reserva del `[58]` para Mitchell, las cinco
> contradicciones de la `Auditoría de Bibliografía.md` y el barrido de localizadores—. **Tres de
> ellas describían problemas que NO EXISTÍAN**: el equivocado era el informe, no `Bibliografía.md`.
> Sus fichas viven ya en `## Cerradas`. **El texto de abajo se deja como historial, sin casilla.**

**`Bibliografía.md:58` promete un `— (no es libro)` que solo existe en las filas NUEVAS — CERRADA, historial** (🟡) · Informe · **solo `researcher`**
  Alta el **2026-08-15**. La leyenda de la columna «Localizador por uso» anuncia esa marca como
  convención del fichero, pero **solo la llevan las entradas dadas de alta en esta tanda**
  (`[58]`–`[67]`). En las anteriores la celda queda muda, así que **no se distingue «no aplica» de
  «sin rellenar»** — que es precisamente lo que la columna venía a evitar. **O se propaga la marca a
  las filas viejas, o se reescribe la leyenda para que describa lo que hay.**

**`Reconstrucción de las 47 citas colgantes.md:283` reservaba el `[58]` para Mitchell — CERRADA, historial** (🟡) · Informe · **solo `researcher`**
  Alta el **2026-08-15**. Es una **reserva de número que ya no se cumplió**: el informe apunta a un
  `[n]` distinto del que `Bibliografía.md` asignó de verdad. No rompe ninguna cita —**el informe no
  es memoria**—, pero es exactamente el tipo de número recordado en vez de contado que **ya ha
  provocado dos solapes el mismo día**. Corregir a `[60]` o retirar la reserva.

**`Auditoría de Bibliografía.md` contradecía en CINCO líneas los «✅ EJECUTADO» — CERRADA, historial** (🟡) · Informe · **solo `researcher`**
  Alta el **2026-08-15**. El informe de auditoría (T15) sigue describiendo como pendientes acciones
  que `Bibliografía.md` ya declara ejecutadas. **Mismo defecto que la Tanda 9 acaba de corregir en
  los tres callouts**, pero en el otro fichero: la corrección se aplicó donde se leía y no donde se
  auditaba. **Encaja con T25**, que ya tiene encargada una línea de ese mismo fichero (`:140`).

**La afirmación de «localizadores de página en las notas» solo era cierta para `6.2:306` — CERRADA, historial** (🟡) · Informe · **solo `researcher`**
  > **CERRADA el 2026-08-17 CON RESULTADO VACÍO, y el vacío es el resultado**: barridos los
  > capítulos 1, 4, 5, 6 y los apéndices, **no hay ni una sola cita a un libro fuera del capítulo 2**,
  > así que **no había nada que estampar**.
  **AVANZADA, NO CERRADA, en la TANDA 13 (2026-08-16): de los 36 marcadores convertidos, 27 bajan
  CON localizador de capítulo**, así que el localizador ya **sí** ha llegado al texto en los
  capítulos 2 y 3 — la afirmación de esta ficha **ya no es cierta tal como está escrita**. Queda
  abierta porque el alcance eran **los 8 libros en todo el vault**, y las citas a libros de los
  capítulos 4, 5, 6 y apéndices **no se han barrido**. `[54]` Molnar sigue con la **edición sin
  fijar**, pero **ya no bloquea ningún localizador del capítulo 2** (ver la ficha de la Tanda 13).
  Alta el **2026-08-15**. La tanda estableció **5 localizadores** y marcó **5 como no establecibles**
  —disciplina correcta, se aplaude—, pero **en las notas de la memoria solo hay UN marcador con
  localizador**, `6.2:306`. O sea: el localizador está registrado en `Bibliografía.md` y **casi no ha
  bajado al texto**, que es donde la decisión del 2026-08-15 lo pedía. **No es un error, es alcance
  no cubierto**: hay que sembrarlo en las citas a los **8 libros** (`[4]`, `[5]`, `[6]`, `[7]`, `[8]`,
  `[12]`, `[39]`, `[54]`), con los avisos ya conocidos de `[6]` (huérfana, depende de T24) y `[54]`
  (edición sin fijar).

> **El DESCUADRE DE CIFRAS «36 marcadores vs 33»** que vivía aquí queda **CERRADO en la TANDA 13**
> (2026-08-16): `Bibliografía.md:46-47` ya dice «36 marcadores — 33 en las notas más los 3 de
> `EL_FUTURO.md`», con **unidad y número casando**. Su ficha vive en `## Cerradas`.

### Hallazgos laterales de la TANDA 10 — altas del 2026-08-15

> Salen del análisis de datos repetidos del capítulo 3 (pieza B, `3fadf13`), **detectados FUERA del
> encargo y deliberadamente SIN TOCAR**. **Ninguno es bloqueante** y **ninguno mueve una cifra
> publicada.** **Fichar no es resolver: aquí no se ha corregido nada.**

> **El 🟡 «los punteros al "inventario completo" apuntan a CUATRO destinos distintos» queda CERRADO
> el 2026-08-17**: hoy hay **exactamente una sede canónica, `6.1`**, y las **nueve remisiones**
> apuntan allí. Su ficha vive ya en `## Cerradas`.

> **El 🟡 «`4.3:262` enumera las diez sedes sin decir cuál es la canónica» queda CERRADO en la
> TANDA 21** (2026-08-17): canónica **`4.3.5` § «Decisión experimental: 54 frente a 122 (experimento
> H1)»**. Su ficha vive ya en `## Cerradas`.

> **La ficha «`4.5:39` es INEXACTO para KNN» queda CERRADA el 2026-08-16 en la TANDA 14**, con las
> cifras exactas que ella misma exigía. Detalle en `## Cerradas`.

> **El 🟡 «el barrido de solapes del capítulo 2 quedó INCOMPLETO» queda CERRADO en la TANDA 19**
> (2026-08-17): revisadas las 12 notas que faltaban, 6 solapes corregidos con sede canónica y
> remisión. Su ficha vive ya en `## Cerradas`. **Con él cae el bloqueante declarado de la Fase 5.**

### Residuos y hallazgos de la TANDA 11 — altas del 2026-08-15

> Salen del cierre del **capítulo 2 entero** (`d31e20f` + `296de24`) y de sus dos pases de auditoría.
> **Ninguno es bloqueante** y **ninguno mueve una cifra publicada.** **Fichar no es resolver: aquí no
> se ha corregido nada.**

> **El «Pase EN SERIE del `researcher`: 33 `[CITA: …]` del capítulo 2 + 3 arreglos en
> `Bibliografía.md`» queda CERRADO en la TANDA 13** (2026-08-16), y con **36 marcadores**, no 33:
> el recuento vigente incluía ya los 2 del capítulo 3. Sus **arreglos 1 (`[6]` huérfana en falso) y
> 2 (`[4]` Chio) están HECHOS y verificados contra disco**. **El arreglo 3 —la corrección (6) de la
> Tanda 5, «Dónde se usa» de `[2]` y `[3]`— SIGUE VIVO en su ficha propia**, no aquí: verificado el
> 2026-08-16, ambas filas siguen diciendo solo `1.2 Preliminares`. Detalle en `## Cerradas`.

> **El 🟡 «De las 27 imágenes embebidas del vault, solo las 5 del capítulo 2 llevan pie de figura»
> queda CERRADO en la TANDA 25** (2026-08-18): las **22 de los capítulos 4 y 5** (cap. 4: 9 · cap. 5:
> 13) llevan ya pie numerado con el criterio `Figura <capítulo>.<orden>` — **4.1–4.9** y **5.1–5.13**.
> Su ficha vive ya en `## Cerradas`. **La colisión que esta ficha temía NO existía**: `2.1.1` numera
> hoy `Figura 2.1`–`2.4`, no «1.1–1.4», y en los capítulos 4 y 5 no había numeración previa que
> corregir. **Deja UNA ficha nueva**, la de las dos figuras duplicadas.

### Residuos de la TANDA 12 — altas del 2026-08-16

> Salen de la auditoría de coherencia de la Tanda 12 (`APTO CON CAMBIOS`, 10 hallazgos, ninguno 🔴).
> **Nueve de los diez quedan aplicados y cerrados**; aquí vive lo que no se podía aplicar en esa
> tanda. **Ninguno es bloqueante** y **ninguno mueve una cifra publicada.**

> **El Hallazgo 10 —«Dónde se usa» desfasada en OCHO entradas— queda CERRADO en la TANDA 13**
> (2026-08-16), justo donde estaba previsto: dentro del pase en serie, para tocar `Bibliografía.md`
> una sola vez. **7 de las 8 estaban desfasadas por el capítulo 3 y quedan recontadas; `[52]` era
> CORRECTA**, así que el hallazgo sobreestimaba en una. **Sigue vivo el defecto de la misma familia
> en `[2]` y `[3]`** —corrección (6) de la Tanda 5—, que tiene ficha propia. Detalle en
> `## Cerradas`.

### Residuos de la TANDA 13 — altas del 2026-08-16

> Salen del **pase EN SERIE de citas del `researcher`** (`[CITA: …]` → `[n]`, 36 marcadores). **Las
> cuatro ESPERAN DECISIÓN DE FRANCISCO y ninguna la forzó el agente**: en las tres primeras el
> marcador se convirtió **sin capítulo** en vez de trasladarlo o sustituir la fuente por cuenta
> propia, que es la disciplina acordada. **Ninguna es bloqueante** y **ninguna mueve una cifra
> publicada.** **Fichar no es resolver: aquí no se ha decidido nada.**

- [ ] **`2.1.5:114` (MAE frente a RMSE) — el capítulo del marcador NO cuadra** (🟡) · Informe · **decide Francisco**, ejecuta `researcher`
  Alta el **2026-08-16**. El marcador decía «Géron, cap. 4» («Training Models») y la contraposición
  MAE/RMSE de Géron vive en el **cap. 2** («Select a Performance Measure»). **Convertido a `[5]` sin
  capítulo** en vez de trasladarlo por cuenta propia. Queda marcado como ⚠️ **NO ESTABLECIDO** en la
  fila de `[5]` de `Bibliografía.md`. **Decidir: fijar `[5, cap. 2]` o dejarlo sin localizador.**

- [ ] **`2.1.4:77` (LOF) — «Hastie, cap. 14» no trata LOF; la primaria correcta sería Breunig et al. 2000** (🟡) · Informe · **decide Francisco**, ejecuta `researcher`
  Alta el **2026-08-16**. **Convertido a `[12]` sin capítulo.** La fuente primaria correcta es
  **Breunig, Kriegel, Ng y Sander (2000)**, SIGMOD, DOI `10.1145/335191.335388`, **propuesta pero NO
  dada de alta**: **sustituir una fuente por otra no lo decide un agente**. Mismo patrón que la
  reasignación del Isolation Forest, que sí venía con encargo escrito. **Decidir: dar de alta la
  primaria y reapuntar, o dejar `[12]` sin capítulo.**

- [ ] **Reserva menor sobre `2.1.4:46` y `:51` (k-NN) apuntando a Géron cap. 3** (🟡) · Informe · **decide Francisco**, ejecuta `researcher`
  Alta el **2026-08-16**. El cap. 3 («Classification») **usa** k-NN en sus ejercicios pero **no
  desarrolla el aprendizaje perezoso ni las métricas de distancia** con el detalle que el texto le
  atribuye. **Dejado como estaba** y anotado en la fila de `[5]` de `Bibliografía.md`. Es el menor de
  los tres: la obra es correcta, lo dudoso es el capítulo.

- [x] ~~**`[54]` Molnar sigue con la EDICIÓN SIN FIJAR — alcance REDUCIDO tras la Tanda 13** (🟡) · Informe · **decide Francisco**~~
  **CERRADA el 2026-08-18 en la TANDA 27**: decidida por Francisco el 2026-08-17 (**2.ª ed., 2022**) y
  **aplicada** ese día en la fila de `[54]` de `Bibliografía.md`. Su fila vive ya en `## Cerradas`.
  **Queda fuera de esta ficha** el aviso de `CLAUDE.md` que aún la declara «sin fijar»: lo decide quien
  mantenga ese fichero.
  Alta el **2026-08-16** como recorte del aviso que ya vivía en PRÓXIMOS PASOS. La web sirve hoy la
  **3.ª edición** y la literatura cita la **2.ª de 2022**, así que su página depende de qué edición
  se elija. **Lo que cambia: tras reasignar el Isolation Forest a `[73]` Liu, Ting y Zhou (2008), ya
  NO bloquea ningún localizador del capítulo 2** — solo afecta a su uso en `2.3.3`.

### Descartado — no reabrir

> Descartes **cerrados en el `grill-me` del 2026-08-06**. No son tareas pendientes ni pospuestas:
> están decididos. **Reabrir cualquiera de ellos exige decisión expresa de Francisco.**

| Descartado | Razón |
|---|---|
| **E-INC** (autoencoder incremental por ráfagas) | Viable, pero responde a una pregunta de despliegue, no a la del TFG. Complejidad innecesaria |
| **Cascada invertida completa** | No se puede invertir esta cascada, solo construir otro sistema: la etapa 2 no tiene clase `normal` (`firmas.py:5`, `153-154`). Exigiría reentrenar a 5 clases y mover 4.5, 5.2 y la comparabilidad de H1. Y Kim et al. tampoco solo invierte el orden. Sustituido por la medición T3 |
| **Experimento adversario** para P10 | Incumpliría otro pitfall del propio Arp et al. (espacio de características sin correspondencia en el espacio del problema). Sustituido por el modelo de amenaza escrito |
| **Sustituir las 54 características por el latente de 32 del AE** | El latente está entrenado solo con D1 para reconstruir lo que **no** es ataque; `root_shell`, `num_shells`, `su_attempted` son ≈0 en D1 por construcción, así que el cuello de botella no tiene incentivo para reservarles dirección — y `u2r` ya es el eslabón débil (f1 0,452, 37 muestras). Además destruye las reglas legibles y `MLPRegressor` no expone `transform()` |
| **Stacking como solución al `unknown`** | No puede aprender la clase que importa: de `unknown` no hay ni un ejemplo en el entrenamiento (D3 son solo ataques conocidos). Es un problema de conjunto abierto y el stacking supervisado no es la herramienta. Rebajar la expectativa de `EL_FUTURO.md:66-68` |
| **TabNet / FT-Transformer / SAINT / NODE / TabM / TabPFN** | PyTorch, ruptura de la persistencia `.joblib` y del protocolo homogéneo, sin respaldo para este régimen. TabPFN v2 ni admite D3 (58.630 > 10.000) |
| **Aprendizaje semisupervisado** | La premisa no existe: no hay datos sin etiquetar. Cada fila de NSL-KDD trae `attack` y `level` |
| **p-valor sobre las 10 semillas** | 10 puntos sobre un único dataset. Se declara la renuncia con su razón |
| **Tabla grande de *accuracies* de la literatura en `5.4`** | Con 87 % de descarte en la muestra y NSL-KDD casi ausente de los venues de primer nivel, sería una colección de cifras indefendibles una por una. El descarte **es** el hallazgo |
| **Nota propia para «híbrido», cascada invertida o TabNet** | Son párrafos dentro de notas que ya existen. Sacarlos a nota propia es la complejidad que el criterio rector prohíbe |

### Secuencia del lote 2026-08-06

`T0` → `T1`-`T4` (código, cada uno con `auditor-ml`; `T4` lo corre `ejecutor-experimentos`) →
`T2`/`T3` alimentan `T9`/`T11` → `T5`-`T13` (redacción) → `T15` en paralelo desde el principio →
`T16` al final → `T17` acompaña cada cierre.

> **Estado del lote, consolidado el 2026-08-13.** Cerradas: `T0`; `T1` (`5f98d88`, 8 tablas sobre el
> esquema nuevo, con residuos `T18`-`T22`); `T2` y `T3` (`b1f1df2`, las **dos mediciones baratas**,
> ambas APTO); `T15` (con residuos `T23`-`T25`); `T18` y `T22` (`8fdc421`). Del track de código
> reabierto el 2026-08-06 **solo quedaba `T4`**, y solo por el **consumo** de su banda en `A.3` (**T7**)
> y en `5.2`/`5.4` (**T11**). **Estado corregido el 2026-08-17: `T11` está CERRADA desde la TANDA 17
> (`9bcfe1f`, capítulo 5 completo) y `T4` CERRADA en la TANDA 19 (`b276f97`) — su casilla `- [ ]` ya
> no existe, así que esta prosa las daba por abiertas contra el propio registro.** De aquel par solo
> **`T9` sigue abierta**: T2 y T3 no la cierran, solo la alimentan —el número de la cascada invertida
> va a `3.2.2`—, y sus cifras quedan anotadas dentro de la ficha con su salvedad de uso.

### Autoría de la redacción — estado vigente desde T0 (2026-08-09)

Antes había aquí una lista de secciones vedadas a los agentes. Solo **una** sobrevive como redacción.

**Lo que sigue siendo de Francisco:**

- **La bibliografía final con Zotero en formato IEEE.** Trabajo mecánico en su máquina, fuera del
  vault. No confundir con `Bibliografía.md`, que es del `researcher`.
- Y, fuera de la redacción: **el título del TFG**, **las decisiones de diseño y de alcance** y la
  **revisión final de `6.2`**.

**Lo que pasó a los agentes:**

| Sección | Quién redacta | Condición |
|---|---|---|
| Todo `02 Marco Teórico` — 2.1.6, **`2.1.4`**, bloque 2.2, bloque 2.3 | `redactor-tfg` | Ninguna. Parte de los guiones ya propuestos en las 8 notas (2026-07-15) |
| `4.2` — origen del dataset, las 41 características | `redactor-tfg` | El borrador **ya existe** en la nota (decisión del 2026-07-21). El «por qué NSL-KDD» lo revisa Francisco. Contenido: **T10** |
| `6.2 Líneas futuras` | `redactor-tfg` | Revisión final de Francisco. Respaldo en `EL_FUTURO.md` |

> **`2.1.4` no queda exceptuada.** Era la pregunta que T0 y T25 compartían y **la decidió Francisco
> el 2026-08-09**: exceptuar una sola nota reintroduciría a mano la regla que la decisión marco (b)
> acababa de retirar del capítulo entero. Con esto **T25 queda desbloqueada**, y con ella **T24**.

> **Recuento:** la lista anterior decía «las 9 notas». Son **8** — `2.2.1` nunca llevó el callout de
> autoría, como ya corrigió la ficha de T0.

---

## Plan de cierre — aprobado por Francisco el 2026-08-13

> **AVISO: esto es un ORDEN DE EJECUCIÓN, no un estado.** Las **fichas de `## Abiertas` siguen siendo
> la única fuente de verdad de lo que está abierto**; esta sección solo dice **en qué orden
> atacarlas**. Aquí no se cierra nada, no se acepta nada y no se borra nada: leer una ficha nombrada
> en una fase **no** significa que esté hecha ni empezada.
>
> **Objetivo declarado por Francisco el 2026-08-13:** cerrar todas las tareas pendientes para poder
> **dar él una última vuelta al informe y cerrarlo**.
>
> **Decidido el 2026-08-13: NO se elimina ningún fichero del proyecto.** `Guia_ML`,
> `resumen-de-decisiones.md`, `99 Investigación/`, `PIPELINE.md` y `GUIA_RESULTADOS.md` **se
> CONSERVAN** — son la trazabilidad de las decisiones y la procedencia de los artefactos, y borrarlos
> ahorraría bytes a cambio de perder justificación citable. **Los agentes tampoco se colapsan.**

### Las decisiones que solo puede tomar Francisco

Eran **el cuello de botella real del plan, no el volumen de trabajo**. **TODAS DECIDIDAS: las dos
primeras el 2026-08-13 y las ocho restantes el 2026-08-14.** La tabla se conserva como registro de
qué desbloqueó cada una; el detalle de cada decisión está en `## Cerradas` y en la ficha que la
consume. Las dos del **2026-08-13**: el **rango de FPR** (hoy instrucción vigente: cifra por
variante, 10,2 % en 54 y 8,5 % en 122) y **automatizar el «13 de 98»** (hecho en `9d4c26d`; la
prohibición de citarlo está levantada).

| # | Decisión (2026-08-14) | Qué desbloqueó |
|---|---|---|
| 1 | **Eje de balanceo de `4.3.4`: NO se reabre, se DECLARA NO CONSTANTE** — solo el eje SMOTE vs `class_weight`; el eje SMOTE vs nada SÍ está establecido. No se toca `firmas.py` | **T11**, que lo consume y lo redacta en `5.4`/`4.3.4` |
| 2 | **NO se regeneran los splits** (son del 2026-07-05 y de ellos cuelga todo lo publicado) | La ficha de las **rutas absolutas**: **NO se ejecuta**, pasa a límite conocido en `A.3` (**T7**) |
| 3 | **Permiso ACOTADO, no general:** el `ml-implementador` solo puede **AÑADIR nota fechada** en `resumen-de-decisiones.md`; **nunca reescribir texto previo** | Las fichas de corrección de ese fichero. Aplicarlo en `.claude/` es del hilo principal |
| 4 | **NO se cierra T14 como «no disponible»: los puntos quedan MARCADOS** dentro de las notas, para la revisión final de Francisco | **T14** cambia de naturaleza: pasa a inventario de revisión. La ficha de guardia del PDF sigue de guardia |
| 5 | **Los tres `grill-me` salen de la Fase 0 y se APLAZAN a la Fase 6**, detrás de absolutamente todo | La Fase 0 entera. Las dependencias técnicas siguen vigentes (ver Fase 6) |
| 6 | **El título del TFG queda APLAZADO** a la Fase 7 | **Preliminares**. Un agente **propone candidatos**, no lo fija |
| 7 | **UN COMMIT POR TANDA**, nombrando en el cuerpo las fichas que cierra | La Fase 4. **Precondición: matizar `CLAUDE.md` §Git** |
| 8 | **La divergencia de `resumen-de-decisiones.md:459` NO era decisión de contenido**: es una instrucción al redactor de `2.2.4` | Nada: se resuelve dentro de la Fase 4, sin ciclo propio |

### Las siete fases, en orden

- **Fase 0 — Decisiones. CERRADA el 2026-08-14.** Las **ocho** de la tabla de arriba quedan tomadas
  (ocho filas de esa fecha en `## Cerradas`). **Cero cómputo, cero código, ninguna cifra publicada
  movida.** Iba primera porque cuatro fases posteriores arrancaban a medias sin esto.
  **La Tarea B ya NO formaba parte de esta fase: se aplicó el 2026-08-13 en `c5ceca5`** (bullet Q6 de
  `resumen-de-decisiones.md`). Si algún texto la sigue pidiendo, está desfasado.
  **Lo único que deja pendiente, y es del hilo principal, no de un agente:** matizar `CLAUDE.md` §Git
  (**precondición de la Fase 4**), el permiso acotado en `.claude/agents/ml-implementador.md` y la
  regla de marcado en `.claude/agents/redactor-tfg.md`.
- **Fase 1 — Barrido de correcciones de una línea.** **DOS ciclos, uno por track**, porque el agente
  difiere.
  - **Código:** `warnings.filterwarnings('ignore')` en **`program.py:12`** y **`validacion.py:57`**
    —**ojo: NO `validacion.py:21`, que es comentario**— y la **nota fechada de
    `resumen-de-decisiones.md:820-821`**.
  - **Informe:** **`4.2:105`**, el **rango de FPR en sus cuatro sitios** (`4.2:120`, `A.2:69` y las dos
    viñetas de este fichero, **en la misma pasada**), el **sello de `4.2:145`**, **T20** (desbloquea
    **T9**) y las **tres correcciones de una línea de T25** en `Bibliografía.md:32`, `:86` y
    `Auditoría de Bibliografía.md:140`, **que solo toca el `researcher`, y en serie**.
  - **Minutos de trabajo, cierra seis fichas.** Por eso va tan arriba.
- **Fase 2 — Cerrar T4.** **Crear `A.3` (T7)** pegando la tabla de `Resultados/dispersion_semillas.md`
  con sus **tres salvedades** y el sello re-anclado → **queda servido T11** → **con eso T4 se puede
  cerrar**. El «13 de 98» ya está automatizado (`9d4c26d`), así que esta fase no espera a nada. **T7 va
  ANTES de la revisión del profesor** porque el material que se recorte del cuerpo **se MUEVE a `A.3`,
  no se elimina**.
- **Fase 3 — Deuda de datos del informe.** **Figuras de `assets\`** (va **antes de T10** y **retira un
  `[!todo]` vivo en `4.2:117`**), **T19**, **T21**.
- **Fase 4 — Capítulo 2.** La **ficha nueva de la prosa de las 8 notas en guion** (alta del
  2026-08-13), con **T8 y T24 integrados en la misma pasada por nota**. **La fase más larga del
  plan.**
- **Fase 5 — Capítulos 3 a 6.** **T5** (crea `5.0`, que **NO existe en disco**), **T10**, **T11**,
  **T9**, **T6**, **T13**, **T12**.
- **Fase 6 — Los tres `grill-me`.** `2.1`, revisión del profesor, y **la ficha `1.4` la ÚLTIMA de
  todas**, como pidió Francisco el **2026-08-12**.
  - **DECISIÓN 5 de la Fase 0 (Francisco, 2026-08-14), literal y más fuerte que lo propuesto: se
    hacen TODAS las tareas de volcado de información al informe y, una vez TODO esté cerrado, revisa
    él el informe completo.** Por eso los tres `grill-me` **salen de la Fase 0** y **la Fase 6 va
    detrás de absolutamente todo**, con **`1.4` la última**. Razón adicional: **dos de los tres se
    alimentan de `mis-apuntes-del-informe.md`, que es incremental y sigue creciendo**; fijar hoy su
    alcance es decidir sobre un fichero que va a cambiar.
  - **MATIZ QUE NO SE PIERDE: el orden entre fases da igual PARA FRANCISCO, pero las dependencias
    técnicas siguen vigentes y NO son negociables** — **T7 (`A.3`) antes de la revisión del profesor**
    (lo que el profesor recorte del cuerpo **se MUEVE** a `A.3`); **figuras de `assets\` antes de
    T10** (si no, T10 vuelca `4.2` con un `[!todo]` vivo); **T20 antes de T9**; y **la conversión de
    `[CITA: …]` a `[n]` al final de CADA fase**, no una sola vez al final del plan, o reaparece el
    solapamiento silencioso de números.
- **Fase 7 — Cierre.** **T16** (obligatoriamente **después de T8-T13**, por su regla dura «ninguna
  entrada sin cita en el texto»), **T17**, **Preliminares con el título**, **borrar `03 Desarrollo\`**
  y **cuadrar el recuento del índice**. **La bibliografía final Zotero/IEEE es de Francisco**, no
  entra en ninguna fase.
- **Fuera de fases, a aceptar o retirar por Francisco:** el **diagrama de agentes desactualizado** y
  las **rutas hardcodeadas**.

### Política de paralelismo — regla nueva del 2026-08-13

**El criterio es el FICHERO, no el tema: dos redactores a la vez solo si escriben ficheros distintos.**

- **La Fase 4 (capítulo 2) se ejecuta en tandas de 3-4 notas en paralelo, no nota a nota.** Son 8 notas
  en guion, con **T8 y T24 integrados en la misma pasada por nota**. Es la fase más larga del plan y la
  que más se acorta con esto.
- **La Fase 5 admite paralelismo por nota**, respetando las ordenaciones duras de abajo.
- **NUNCA en paralelo:** dos agentes sobre la **misma nota**; `Bibliografía.md`; `features.md`; la
  **asignación de números de cita `[n]`**; y el pase de **`auditor-ml`**, que va **después**, no a la vez.
- **Protocolo de citas bajo paralelismo:** un redactor en paralelo **no asigna nunca un `[n]` nuevo** —
  son un contador global, y hoy `[4]`, `[5]`, `[7]`, `[8]` y `[10]` ya están en uso en las notas de
  `2.1` y `2.2`, así que cuatro redactores simultáneos empezarían los cuatro en `[11]` y se solaparían
  en silencio. Se escribe **`[CITA: autor o tema]`**, convención que el proyecto ya usa (`4.2` arrastra
  6 marcadores). **La conversión a `[n]` y el alta en `Bibliografía.md` es un pase posterior y EN SERIE
  del `researcher`.**
- **La prohibición de que el `redactor-tfg` escriba la teoría `2.x` y el borrador de `6.2` está
  RETIRADA del andamiaje** (corregido en `leader.md` el **2026-08-13**): era lo que bloqueaba la Fase 4
  entera. **Sigue siendo de Francisco:** la bibliografía Zotero/IEEE, el título del TFG, las decisiones
  de diseño y alcance, y la **revisión final de `6.2`**.

### Ordenaciones duras heredadas que el plan respeta

Se dejan listadas para que **nadie las rompa** al reordenar:

- **T16 después de T8-T13.**
- **Figuras de `assets\` y el sello `4.2:145` antes de T10** — **SATISFECHA**: la ficha de las figuras
  de `assets\` se cerró el **2026-08-15**, así que **despachar T10 el 2026-08-16 fue legítimo**.
- **T20 antes de T9.**
- **La ficha `1.4`, la última de todas.**
- **El recorte del profesor va a `A.3`**, así que **T7 antes**.
- **«13 de 98» automatizado antes de que T7 y T11 lo citen** — **satisfecha** en `9d4c26d`.

### Estimación y límite declarado

**Entre diez y catorce sesiones**, **dominadas por la Fase 4** — menos con la política de paralelismo.

**El límite, dicho sin rodeos: NO se pueden cerrar «todas» las fichas por parte de agentes.** Eran
**seis estructuralmente de Francisco** — bibliografía Zotero/IEEE, título del TFG, eje de balanceo,
alcance de los tres `grill-me`, acceso institucional y regeneración de los splits—, y **si se
quedaban quietas el plan se atascaba en la Fase 0, no en la Fase 4**.

> **Actualización del 2026-08-14: ese atasco YA NO EXISTE.** Cuatro de las seis quedan resueltas
> (eje de balanceo, splits, acceso institucional, alcance de los `grill-me`) y las otras dos quedan
> **aplazadas a su sitio natural**: el **título** a la Fase 7 y la **bibliografía Zotero/IEEE** fuera
> de fases. Lo que sigue siendo de Francisco y no lo cierra ningún agente: la **Fase 6 entera**
> (revisión del informe completo, `1.4` la última), la **bibliografía final**, la **revisión final de
> `6.2`** y el **título**.

---

## Cerradas

| Fecha | Track | Tarea | Commit |
|---|---|---|---|
| 2026-08-18 | Informe | **TANDA 27 · FASE 7 — PRELIMINARES + 2 MECÁNICAS DE BIBLIOGRAFÍA. Cinco ficheros, verificados contra `git status`.** **(1) Resumen y abstract redactados** (`00 Preliminares/Resumen.md`, `Abstract.md`): resumen académico completo y **traducción literal al inglés**, con palabras clave; cifras ancladas a `Resultados/metricas_hibrido.csv` y `metricas_baseline.csv` (**fila `set_features=54`, commit `1163c90`**), verificadas columna a columna; **cero `[n]`**. **El TÍTULO NO queda fijado**: se proponen **5 candidatos** en `Resumen.md` y **lo elige Francisco** (Decisión 6), así que la ficha de Preliminares **queda `[~]` con el título como único pendiente**. **(2) `01 Introducción/1.1 Motivación.md`**: corregidas **las 4 erratas fichadas más 4 del mismo tipo**, sin tocar cifras ni citas — **cierra la ficha de erratas de `1.1`**. **(3) `Bibliografía.md`**: celda de **`[76]` Storkey** desambiguada (**rango pp. 3-28 verificado**; **solo la página exacta sigue por decidir**, así que esa ficha **sigue abierta**) y **`[54]` Molnar fijada a la 2.ª ed., 2022** — **cierra las DOS fichas de `[54]`** (la de «pendiente de aplicar» y la de alcance reducido de la Tanda 13). **Protocolo de citas intacto: 76 entradas antes / 76 después, cero altas, cero renumeraciones, primer libre sigue `[78]`.** **(4) `00 Índice TFG.md`** cuadrado tras la tanda: **43 `redactada` / 0 `borrador` / 0 `pendiente`**, recontado contra el frontmatter en disco. **Auditoría `auditor-ml`: APTO CON CAMBIOS, ningún 🔴** — sin cifra sin respaldo, sin confusión 54/122, Abstract = traducción literal del Resumen. **Cambios mecánicos aplicados en un segundo pase:** `0,861`→**`0,860`** (`bin_accuracy`=0,860451; el resto de la memoria publica 0,8605), el hedge de «prevalencias realistas» convertido en **escenario ilustrativo declarado**, añadida la limitación de **data snooping**, y precisado que umbral, balanceo y CV son protocolos **por etapa**, no comunes a los ocho algoritmos. **Cero código, cero cómputo, ninguna cifra publicada movida.** Deja **un residuo** y **una decisión** pendientes de fichar (reportados al `leader`, no fichados por el `cronista`) | — |
| 2026-08-18 | Ninguno | **TRIAJE DE LAS FICHAS ABIERTAS — «por qué no se despachan de golpe todas las fichas abiertas», pregunta de Francisco. Sin ficha previa (carril Intervención).** Añadido al **inicio de `## Abiertas`** el bloque «📊 TRIAJE DE LAS FICHAS ABIERTAS — por qué NO se lanzan todas (2026-08-18)», con cuatro apartados: **21 fichas bloqueadas en una decisión de Francisco** (ejecutarlas exigiría **inventar un dato** o **escribir en un fichero sin permiso concedido**); **4 informativas**, que **solo Francisco borra**; **10 ejecutables por agente**, de las que las **3 de sustancia tienen el alcance sin cerrar y exigen `grill-me`** (`1.4` conceptos de IA, `2.1` coherencia y densidad, y la revisión del profesor del **cap. 3 en adelante**); y **4 despachables ya sin preguntar** (Preliminares Fase 7, erratas de `1.1`, celda de `[76]` en `Bibliografía.md`, aplicar `[54]` Molnar). El bloque advierte que **sus referencias se localizan por título, no por número de línea**. **Dos hallazgos de método:** (1) el recuento de «**35 fichas abiertas**» **infravaloraba el total** —contaba solo los `- [ ]`— y dejaba fuera **dos `[~]` con trabajo vivo** (el **borrado físico de `03 Desarrollo/`**, que ningún redactor puede hacer por **no tener shell**, y los **números de línea desplazados de T25**) más **T23**, marcada `[x]` pero **declarada abierta en su propio cuerpo**: invisible a cualquier `grep '^- \[ \]'`; (2) **el cuerpo de T23 está caducado** —alegaba que el párrafo de Snort de `1.2` seguía sin cita cuando **`1.2:32` ya cita `[26]`** con el callout de **LISA'99 vs 1998**, con **P4 aplicada** y `[26]` **mapeada, no duplicada**—: **sexta ocurrencia del patrón de registro caducado**, y el cuerpo queda **marcado como traza histórica** en su ficha. **Cero código, cero cómputo, ninguna cifra movida.** Fichero tocado: **únicamente `features.md`**| `9299863` |
| 2026-08-18 | Informe | **FASE B DEL BARRIDO — EL CAPÍTULO 1. Es lo último ejecutable del barrido. Cierra TRES fichas** (el hueco de completitud del capítulo 1, los tres defectos de `1.4 Estructura` y las erratas de `1.2:14`). **Cero código, cero cómputo, cero corridas, ninguna cifra publicada movida.** Ficheros del vault: `01 Introducción/1.0 Sinopsis.md`, `1.2 Preliminares.md`, `1.3 Objetivo.md`, `1.4 Estructura.md`, más `00 Índice TFG.md` y `06 Conclusiones/6.1 Conclusiones.md` por coherencia. **`1.1 Motivación` es la única nota del capítulo que NO se toca** — queda en ficha nueva. **Protocolo de citas respetado sin excepción: CERO `[n]` nuevos y CERO `[CITA: …]` nuevos**, verificado por `grep` sobre `01 Introducción/` **después** de los dos pases; el capítulo 1 sigue usando solo `[1]`, `[2]`, `[3]` y `[26]`. **El `[CITA: …]` y el `[31]` de `1.2:19,22` viven DENTRO del callout `[!warning]` de traza histórica** que narra la atribución retirada en P4-bis: **no son marcadores vivos, así que T16 NO se reabre.** Los dos callouts que dejó la Fase A en `1.2` —**P4-bis** (Anderson/`[2]`) y el de la **fecha 1998 vs LISA'99** (`[26]`)— quedan **íntegros y pegados a sus párrafos**, como se exigió. **Las cinco notas de `01 Introducción/` están hoy `estado: redactada`**, frontmatter verificado en disco una a una. **Deja DOS fichas nuevas**, ninguna bloqueante| `3203420` |
| 2026-08-18 | Informe | **🟡 «El capítulo 1 es el hueco de completitud que queda, y solo está fichado EN PARTE» — CERRADA.** El hueco se cierra en las tres notas que no tenían ficha propia y en la que sí: **`1.0 Sinopsis`** pasa de **478 B / un único párrafo de anuncio** a una sinopsis real de **cuatro párrafos**, con los **nueve objetivos agrupados en cinco bloques** y wikilinks a las cuatro notas hermanas; **`1.3 Objetivo`** pasa de **705 B / cinco frases-párrafo sin hilo** a **objetivo general desarrollado** (con tabla de las dos etapas de la cascada y los splits D1/D3) más **nueve objetivos específicos numerados, cada uno con su criterio de cumplimiento verificable**; **`1.2 Preliminares`** desarrolla los **cinco desafíos** que estaban como párrafos huérfanos **sin una sola frase de explicación**, y reescribe el párrafo de la **detección basada en el estado**, que colgaba del hilo cronológico; **`1.4 Estructura`** en su propia fila| `3203420` |
| 2026-08-18 | Informe | **🟡 «`1.4 Estructura` omite el capítulo 6 entero y atribuye mal las conclusiones» — CERRADA, los TRES defectos verificados en disco:** (1) ya enumera **hasta el capítulo 6** e incluye **Apéndices y Bibliografía**; (2) las **conclusiones se atribuyen al capítulo 6** y el **5 queda como Evaluación**; (3) la **frase del capítulo 4 está completa y cerrada con punto**. **Extra sobre la ficha:** corregida la errata «una **evolución** de los resultados» → **evaluación**, y `estado:` pasado de `borrador` a **`redactada`**| `3203420` |
| 2026-08-18 | Informe | **🟡 «Erratas en `1.2:14`» — CERRADA.** «trackeados» → «**monitorizados y registrados**»; «de como» → «**de cómo**». **Verificado con `grep` en el vault entero: cero ocurrencias de ambas**| `3203420` |
| 2026-08-18 | Informe | **AUDITORÍA DE LA FASE B — coherencia ENTRE las cinco notas del capítulo 1, no nota por nota. Veredicto `NO APTO`, OCHO hallazgos, LOS OCHO APLICADOS y verificados en disco** en un segundo pase paralelo. **🔴** `1.0:14` anunciaba los **cuatro objetivos antiguos** cuando `1.3` tiene **nueve**, omitiendo justo el **baseline de control**, el **recall 0-day por tipo**, la **validación de splits** y las **reglas legibles**, y daba el objetivo general como «implementar» frente al «**diseñar, implementar y evaluar**» de `1.3` — corregido. **🔴** `1.3:25` atribuía a `[[1.1 Motivación]]` el razonamiento del híbrido, que está en **`1.2:49`** y así lo atribuye `1.0:12` — repuntado a `[[1.2 Preliminares]]`. **🟠** `1.4:20` describía un capítulo 5 **sin el baseline monolítico ni el recall 0-day desagregado**, que son el resultado central de la memoria — añadidos, **sin colar ninguna cifra**. **🟠 `00 Índice TFG.md` publicaba un estado falso** — actualizado: `1.4` a `redactada`, retirada la frase «única `borrador` legítima del vault» de `:24` y `:44`, y **recuento de 40/1/2 a 41 `redactada` · 0 `borrador` · 2 `pendiente`**, sobre las mismas **43 notas de memoria y 44 entradas indexadas** (suma verificada): **`borrador` ya no se aplica a ninguna nota de la memoria**, la única entrada en ese estado es `Bibliografía`, que se cuenta aparte. **🟠 `6.1 Conclusiones.md` evaluaba el cumplimiento contra la lista vieja de cuatro objetivos** — realineada `6.1.1` a los **nueve**, agrupados en **cuatro bloques A-D que declaran qué objetivos numerados cubre cada uno**; **ni una cifra tocada:** `6.1.2` y `6.1.3` intactas, con el **0.771 vs 0.150**, el desplome **0.909→0.472**, el **FPR ~10 % / ~5 %**, las tres decisiones **H-2/H-3/Q1-C** y **`snmpgetattack`** verificados en disco tras la edición. **🟡** `1.3` obj. 4: el criterio insinuaba una garantía anti-*leakage* más amplia de la real — acotado para distinguir que **el umbral se fija sin ver D2, pero la elección del detector sí se resolvió mirando D2** (decisión **H-2**), remitiendo a `6.1.3`: **la limitación no se ha diluido**. **🟡** `1.0:16` describía una `1.4` incompleta (sin capítulo 6, apéndices ni bibliografía) — corregido. **🟡** `1.3` obj. 2: el criterio anclaba el pipeline en «capítulos 3 y 4»; está solo en el **4** (4.2 y 4.3) — corregido| `3203420` |
| 2026-08-18 | Informe | **TANDA 26 — cinco redactores en paralelo (un fichero cada uno), pase de `auditor-ml` de coherencia ENTRE notas y dos correctores en paralelo. Ejecuta y CIERRA T17.** **Cero código, cero cómputo, cero corridas, ninguna cifra publicada movida** — verificado contra disco: las **cuatro tablas principales** siguen con `semilla=42` y `commit=1163c90`, y `metricas_cascada_invertida.csv` con sus **10 filas** y `274923d-sucio`. **Ficheros:** los cuatro informes de `Obsidian_TFG_Vault/99 Investigación/` (`aprendizaje-continuo-nested-learning.md`, `clasificadores-tabulares-y-arquitecturas-hibridas.md`, `benchmark-comparativo-nsl-kdd.md`, `arquitecturas-hibridas-en-la-literatura.md`), más `next-steps.md` §6.5b y `Guia_ML/03_validacion_y_metricas.md` §7. **Protocolo de citas respetado: CERO `[n]` nuevos y ningún `[n]` preexistente renumerado**; único marcador nuevo, `[CITA: Goldschmidt y Chudá 2025]`. **Contador recontado hoy contra disco: 76 filas, `[1]`–`[8]` + `[10]`–`[77]`, `[9]` quemada, primer libre `[78]`.** **Líneas prohibidas intactas**, como se ordenó: el «37 muestras en D2» de `benchmark-comparativo:141` y de `clasificadores-tabulares:364`, que son del `researcher`. **Deja CINCO fichas nuevas**, ninguna bloqueante| `c7ab48d` |
| 2026-08-18 | Informe | **T17 · punto 1 — CERRADO: el bloque «Decisiones tomadas a partir de este informe» existe ya en LOS CUATRO informes** de `99 Investigación/`, con qué se convirtió en decisión y qué se descartó. Era lo que faltaba desde el **2026-08-09**. **En la misma pasada, corregidas las DOS declaraciones caducadas** de que `6.2 Líneas futuras` la redacta Francisco (`aprendizaje-continuo:25` y `clasificadores-tabulares:30`), **falsas desde la decisión marco (b) del 2026-08-06**| `c7ab48d` |
| 2026-08-18 | Informe | **T17 · punto 2 — CERRADO EN DOS DE SUS CUATRO SEDES: la deriva de documentación de `evaluacion.py`**, cuyo contrato cambió con T1. Corregidos **`next-steps.md` §6.5b** —con **nota fechada 2026-08-18 y SIN tocar ninguna casilla**: el fichero sigue congelado— y **`Guia_ML/03_validacion_y_metricas.md` §7**. **Ambos verificados FUNCIÓN A FUNCIÓN** contra `Implementacion/app/evaluacion.py`. **`CLAUDE.md:64` y `resumen-de-decisiones.md:88-92` (Q3) NO se tocaron a propósito** —andamiaje y fichero de decisiones— y quedan en ficha nueva| `c7ab48d` |
| 2026-08-18 | Informe | **AUDITORÍA DE LA TANDA 26 — `APTO CON CAMBIOS`, cuatro hallazgos 🟠, ningún 🔴; DOS aplicados en el mismo ciclo.** (1) **`clasificadores-tabulares` atribuía a *ese* informe T18, T22 y la renuncia al p-valor** (más tres descartes derivados), que **no salen de él** y **ya estaban reclamadas** en `benchmark-comparativo:267-268` — **aplicado por vía (b):** movidas a una **§ D.2-bis rotulada como contexto del lote, NO origen**, remitiendo a su sede documentada. (2) **`aprendizaje-continuo:559` clasificaba como decisión CERRADA un punto de una ficha ABIERTA** (`features.md:1541-1552`, «no duplicar la definición de aprendizaje continuo entre `2.x` y `6.2`») — **aplicado:** movido al `> [!todo]` como tercer punto pendiente. **Los otros dos hallazgos quedan como fichas nuevas.** **Método declarado: el `auditor-ml` sigue sin poder calcular hashes**, así que la intocabilidad de los artefactos la verificó **por contenido y por sello de procedencia**, no por `md5`| `c7ab48d` |
| 2026-08-18 | Informe | **T17 — CERRADA.** La cierran sus dos puntos, ejecutados hoy por la TANDA 26: el bloque de decisiones en los cuatro informes de `99 Investigación/` y la deriva de `evaluacion.py`. **Lo que deja vivo, en fichas propias:** la deriva **corregida en 2 de sus 4 sedes** (`CLAUDE.md:64` y Q3 de `resumen-de-decisiones.md`, no tocables por un agente), la **contradicción de `resumen-de-decisiones.md:570-571`**, la **asimetría de remedio entre dos informes** y los **cuatro `> [!todo]` de contenido** que quedan para Francisco. **El volcado a `resumen-de-decisiones.md` ya estaba hecho desde el 2026-08-09**| `c7ab48d` |
| 2026-08-18 | Informe | **TANDA 25 — pies de figura de los capítulos 4 y 5, más el cierre parcial de T23. Cierra DOS fichas** (los pies de figura de las 27 imágenes embebidas y los residuos de `A.3`) **y deja T23 ABIERTA a propósito**. **Seis ficheros del vault:** `1.2 Preliminares.md`, `4.2 Base de datos utilizada.md`, `4.3 Preprocesamiento de los datasets.md`, `5.1 …`, `5.2 …`, `5.3 Resultados del sistema híbrido.md`. **`A.3` NO se tocó.** **T23 · cierre PARCIAL:** P1–P3 ya estaban ejecutadas; **P4 NO aplicada — se marcó una afirmación DISTINTA de la decidida**: la decisión de Francisco era anclar el pasaje de **Roesch y Snort** al paper de **LISA'99 (USENIX)** y eso sigue sin hacerse (`1.2:27` sigue sin cita); lo aplicado en `1.2:14` fue un **`[CITA: …]` + `[!todo]`** sobre **Anderson como punto de partida de la detección de intrusiones**, que **no estaba en la ficha P4** y queda como **segunda afirmación sin aval**. **P4 SIGUE ABIERTA** (ver su ficha en `## Abiertas`); **P5 y P6 NO se aplican aquí**: caen en `Bibliografía.md` (edición de Stallings `[8]`, *deep link* de `[10]` CCN-STIC-401), son **decisión de Francisco** y van al **pase en serie del `researcher`**. **Auditoría `auditor-ml` de coherencia ENTRE notas: `APTO CON CAMBIOS`, 5 puntos, TODOS aplicados** en un pase correctivo de dos agentes en paralelo. **Deja TRES fichas nuevas**, ninguna bloqueante | `babf9a6` |
| 2026-08-18 | Informe | **🟡 «De las 27 imágenes embebidas del vault, solo las 5 del capítulo 2 llevan pie de figura» — CERRADA.** Las **22 de los capítulos 4 y 5** (cap. 4: **9** · cap. 5: **13**) llevan ya pie numerado con el criterio **`Figura <capítulo>.<orden>`**: **4.1–4.9** y **5.1–5.13**. **Recuento verificado contra disco: 27 embebidos exactos en 7 notas de todo el vault, los 27 con pie.** **La colisión que la ficha temía YA NO EXISTÍA:** `2.1.1` numera hoy correctamente `Figura 2.1`–`2.4`, no «1.1–1.4», y **en los capítulos 4 y 5 no había ninguna numeración previa que corregir**. **Los capítulos 3 y 6, los apéndices y el índice no tienen ninguna imagen embebida**, así que el 27 es censo completo. Los **22 ficheros embebidos existen en `Obsidian_TFG_Vault/assets/`**, comprobados uno a uno: **ningún embebido roto**. **Deja UNA ficha nueva:** las dos figuras duplicadas | `babf9a6` |
| 2026-08-18 | Informe | **«Residuos de `A.3` (T7 cerrada el 2026-08-14)» — CERRADA COMO AGOTADA, sin tocar la nota.** `A.3` tiene hoy **un único `[!todo]` vivo**, el de la **caracterización de los seis ítems no-FT del checklist de Pineau** (**`A.3:698`**), que **depende del checklist original** y no de material en disco: nombrarlos sería inventarlos. **No es resoluble por un agente**, así que deja de ser trabajo pendiente y **lo que queda es una dependencia de fuente externa**. **Referencias de línea recontadas en disco porque habían caducado tres veces:** el `[!todo]` de Pineau está en **`A.3:698`** (la ficha decía `:574`, luego `:681`) y el `[!warning]` de **límite declarado de alcance** en **`A.3:654`** (decía `:648`) | `babf9a6` |
| 2026-08-18 | Informe | **AUDITORÍA DE LA TANDA 25 — `APTO CON CAMBIOS`, 5 puntos, todos aplicados. Los dos de fondo, de la clase que solo se ve mirando las notas juntas:** (1) **🟠 ninguna de las 22 figuras nuevas se llamaba por número desde la prosa, y las 5 del capítulo 2 sí** — al volcar al `.docx` habrían quedado **sin *cross-reference***, huérfanas del texto; corregido con **7 llamadas en el cap. 4** y **5 llamadas por bloque en el cap. 5**, con la convención de `2.1.1:16`. (2) **Cuatro pies afirmaban más de lo que la figura muestra, verificado contra el CÓDIGO GENERADOR**: las **Figuras 4.4 y 4.5** omitían el **segundo panel** (histograma de p-valores con línea `p = 0,01`, `validacion.py:836-890`) y el «top 20»; la **4.7** decía «por característica» cuando `validacion.py:960-975` solo pinta el **top 15 en D1**; y «**confirma** la pureza de D1» era **falso** —en `validacion.py:587-603` ese panel es **una barra única rotulada `normal` con `len(self.D1_X)` hardcodeada**: dibuja la pureza **por construcción**, no la verifica—, así que ahora dice «**ilustra**» y remite la confirmación a `specialized_nsl_kdd_validation_report.txt` | `babf9a6` |
| 2026-08-18 | Informe | **TANDA 24 — nueve notas del vault en paralelo y DOS vueltas de `auditor-ml` sobre la COHERENCIA ENTRE ellas. Cierra TRES fichas**: la imprecisión nominal del callout de Procedencia de `4.2`, las remisiones a la sede canónica `4.3.5` y **T21** (la mitad de P9 que T1 no cubre). Ficheros del vault (11): `2.1.6`, `3.3`, `4.2`, `4.3`, `4.6`, `5.0`, `5.1`, `5.2`, `5.4`, `6.1`, `A.3`; registro: `features.md` y `resumen-de-decisiones.md`. **Ronda 1 de auditoría: `APTO CON CAMBIOS`, 9 puntos. Ronda 2: los 8 aplicados verificados y 3 hallazgos nuevos, ya corregidos.** **Cero `[n]` nuevos** (máximo en uso sigue `[77]`). **Corrección de dato en el propio registro:** retirado de `features.md:1366` el «**4,4 millones de flujos/s**», cifra **sin origen en ningún artefacto de disco** —el auditor verificó que **su única aparición en todo el repo era esa ficha**—, sustituido por el valor real **4.196.350,2 flujos/s** con latencia **0,000238 ms** (DecisionTree, `set_features=54`, `semilla=42`, `commit=1163c90`, `Resultados/metricas_firmas.csv:2`). Mismo patrón que el precedente del «13 de 98». **Deja DOS fichas nuevas**, ninguna bloqueante | `6ada8c2` |
| 2026-08-18 | Informe | **🟡 Imprecisión NOMINAL en `4.2`, callout de Procedencia — CERRADA.** La nota cita ya las **etiquetas literales** de los informes, `Commit del código:` y `Fecha de la corrida:`, en vez de «el `commit` y la `fecha`». **Verificadas contra las cabeceras de los dos `Resultados/*_validation_report.txt`** (sello **`ac36b88`**). **No era cifra sin respaldo: era nomenclatura** | `6ada8c2` |
| 2026-08-18 | Informe | **🟡 Las notas remitentes de `4.3.5` no declaraban que remiten — CERRADA, con DOS correcciones a su propio enunciado.** (1) La lista canónica de `4.3:266` da **diez sedes de remisión** —once contando la canónica—, **no nueve**: la décima, **`4.3.7`**, vive **dentro de la propia nota sede**. (2) **`2.1.6` ya declaraba la remisión** en `:94`, así que **no se le añadió línea**, para no duplicar. Líneas de remisión añadidas en **7 notas**: `3.3:31`, `4.6:39`, `5.0:123`, `5.1:135`, `5.2:71`, `6.1:42`, `A.3:106`, todas con la **grafía normalizada** `[[4.3 Preprocesamiento de los datasets\|4.3.5]]` § «Decisión experimental: 54 frente a 122 (**experimento H1, medido sobre D2**)» | `6ada8c2` |
| 2026-08-18 | Informe | **T21 · La mitad de P9 que T1 no cubre — CERRADA en `5.4`.** Declarada la salvedad: `latencia_ms_por_flujo` y `flujos_por_segundo` miden **solo `predict`/`score`** sobre características **ya calculadas y en memoria**, así que la cifra es **techo de inferencia en laboratorio, no capacidad operativa** —el coste de captura, ensamblado de flujo y extracción de las 41 características **no está medido**—. Añadida además en `5.4` la **incoherencia interna de la fila** ya declarada en `Implementacion/PIPELINE.md:643-646`: **`9.083 / 0,002` = 4.541.500** frente a los **4.196.350,2** publicados. **La ficha citaba «4,4 millones de flujos/s» y ese valor NO EXISTÍA EN DISCO**: retirado del registro y sustituido por **4.196.350,2 flujos/s** / **0,000238 ms** (`Resultados/metricas_firmas.csv:2`, DecisionTree, 54 features, `semilla=42`, `commit=1163c90`) | `6ada8c2` |
| 2026-08-18 | Informe | **AUDITORÍA DE LA TANDA 24 — dos vueltas, coherencia ENTRE las nueve notas, no nota por nota. Cuatro defectos de fondo, de la clase que solo se ve mirándolas juntas:** (1) **`5.2:71` y `5.0:126` afirmaban «no fijo cifras por cuenta propia» y acto seguido las fijaban** —la tabla `f1_macro` 54-vs-122 por algoritmo en `5.2:75-82` y los **FPR 10,2 % / 8,5 %** en `5.0`—: ambas frases **acotadas a la declaración de *data snooping***, y **el de `5.0` no estaba en ninguna ficha**; (2) **`5.4:15` atribuía a `§4.3.5` el par 0.822→0.696**, que es de **`5.2:78`** — reatribuido; (3) **`4.3:326` decía «las otras ocho» sedes frente a las «diez, verificado» de `4.3:266`**, dos censos del mismo conjunto **en la misma nota**: el «ocho» era el error, y `:326` **ya no lleva número** y remite a la enumeración de `:266` como **fuente única del recuento**; (4) **la grafía de la sede canónica estaba en TRES versiones** — normalizada en las 7 remisiones nuevas más `2.1.6:83`/`:92`, `4.3:326` y `5.4:32`, dejando **a propósito** el alias genérico `\|4.3` en `3.3:21` y `:23`, que apuntan a §4.3.6 y a §4.3.2/3/5/7 y **no** a la sede de H1 (**el auditor validó el razonamiento**). **Dos afirmaciones falsas más, retiradas:** `A.3:644` decía que la comparación 54-vs-122 «se tabula **íntegra**» en `4.3` y es **falso** —la comparación por algoritmo de firmas se tabula en `5.2:75-80`—; y **`5.4:32`, catalogada como sede de remisión, no remitía** a `4.3.5` — ya remite, y **sin** la fórmula «no fija cifras», porque **`5.4` sí publica cifras propias**. **Método declarado: el `auditor-ml` NO pudo calcular `md5`** (su definición no incluye Bash), así que la **intocabilidad de los artefactos** la verificó **por contenido**: las cuatro tablas de métricas siguen con **`semilla=42`** y **`commit=1163c90`** en todas sus filas, **sin filas del barrido** | `6ada8c2` |
| 2026-08-18 | Informe | **TANDA 23 — `00 Índice TFG.md` puesto al día tras la resincronización del frontmatter de la TANDA 22. Cierra la ficha 🟡 «el índice publica estados desfasados». Un solo fichero: `Obsidian_TFG_Vault/00 Índice TFG.md`.** Corregidos los **estados publicados** de las notas y la **tabla de totales**, que decía **14 `redactada` / 27 `borrador` / 2 `pendiente`** y publica ahora el **recuento real: 40 `redactada` / 1 `borrador` / 2 `pendiente`** — sobre las **44 entradas indexadas** (43 notas de memoria + `Bibliografía`), con el criterio que fijó la TANDA 21. **Desglose de `redactada`, verificado abriendo el `estado:` de cada nota una por una, y coincidió:** cap. 1 (**4**) · cap. 2 (**14**) · cap. 3 (**6**) · cap. 4 (**6**) · cap. 5 (**5**) · cap. 6 (**2**) · apéndices (**3**). **Va sobre la versión ya saneada en la TANDA 21**, no sobre la vieja. **Deja DOS observaciones registradas y NO resueltas, ninguna es defecto:** (1) el frontmatter del propio índice sigue en `estado: borrador` **a propósito** —no se cuenta entre las 43 notas de memoria—; (2) el listado **conserva declaradas las reservas de revisión de Francisco** sobre `4.2` («Por qué se eligió NSL-KDD») y `6.2 Líneas futuras` aunque ambas notas sean ya `redactada`, **correcto según las reglas de autoría del proyecto** | `02ff9fb` |
| 2026-08-18 | Informe | **TANDA 22 — barrido de resincronización del campo `estado:` del frontmatter contra el estado real en disco. Cierra la ficha 🟡 «el campo `estado:` está sin mantener y MIENTE».** **26 notas** pasan de `borrador` a `redactada`, **verificadas abriendo cada nota una por una**: `01 Introducción/1.0`, `1.1`, `1.2`, `1.3` · `03 Diseño del sistema/3.1`–`3.6` · `04 Implementación del sistema/4.1`–`4.6` · `05 Evaluación/5.0`–`5.4` · `06 Conclusiones/6.1`, `6.2` · `Apéndices/A.1`, `A.2`, `A.3`. **Solo el valor de `estado:`, ni una línea más** — verificado: **26 ficheros, 26 inserciones, 26 supresiones, cero líneas ajenas al campo**. **Recuento final del vault: 40 `redactada`, 1 `borrador`, 2 `pendiente`.** **`1.4 Estructura.md` se queda en `borrador` A PROPÓSITO**: tiene hueco real de contenido y es justo la ficha viva de `features.md:527` — **no es un olvido de esta tanda**. `Resumen.md` y `Abstract.md` siguen en `pendiente`, **correctamente**. **Fuera de alcance y sin tocar:** `00 Índice TFG.md` y `Bibliografía.md`. Las **8 notas de `99 Investigación/`** usan **vocabulario de estado propio** (`informe`, `permanente`, `cerrado`) y quedaron **intactas con criterio, no por descuido**. Confirmado de paso: `APUNTES SOBRE CS229 STANFORD ML LECTURES/Lecture 1.md` **no tiene frontmatter (0 bytes)** — es la que Francisco autorizó borrar, y **sigue sin borrar**. **Deja UNA ficha nueva**, efecto colateral esperado: `00 Índice TFG.md` publica ahora estados desfasados | `7029873` |
| 2026-08-17 | Informe | **TANDA 21 — cuatro redactores en paralelo y DOS rondas de corrección de auditoría.** Cierra **seis fichas**: el `[!todo]` de `A.3:648`, la **deuda de cifra de KNN**, el **`~52`**, la **ampliación del índice**, el **recuento de `00 Índice TFG.md:106`** y la **sede canónica de `4.3:262`**. **Ninguna cifra publicada movida sin artefacto de respaldo, cero `[n]` nuevos** (máximo en uso sigue `[77]`), **cero marcas temporales de corrida en prosa** en todo el vault, verificado en las dos rondas. Deja **SIETE fichas nuevas**, ninguna bloqueante, y **dos encargos acumulados** al pase en serie del `researcher` | `1075dfd` |
| 2026-08-17 | Informe | **🟠 Deuda de CIFRA de KNN en el eje SMOTE-vs-nada — CERRADA, y era LA ÚLTIMA DEUDA DE DATO REAL DEL VAULT.** Volcadas a `5.2` §5.2.4.4 desde `Resultados\metricas_balanceo.csv`: **KNN-54 SMOTE 0,9453 ± 0,0058 vs nada 0,9187 ± 0,0252** (margen **0,0266**) y **KNN-122 0,9523 ± 0,0096 vs nada 0,9172 ± 0,0253** (margen **0,0351**). Añadida **columna «Margen»** y las **desviaciones que faltaban a HistGradientBoosting**. **Dato que REFUERZA la Decisión 1 de Francisco:** el margen **más estrecho** de este eje (**0,0266**) **supera al más amplio** del eje SMOTE-vs-`class_weight` (**0,0180**, DT-54), verificado contra el CSV | `1075dfd` |
| 2026-08-17 | Informe | **🟡 El `~52` — CERRADO en las cuatro sedes del vault (`4.2`, `5.2`, `5.4`, `2.1.6`) y en las TRES de trazabilidad autorizadas EXPRESAMENTE por Francisco** (`resumen-de-decisiones.md:103`, `next-steps.md:493` y `:550`), que **citan ahora el artefacto de origen**. Corregida de paso la **autocontradicción de `4.2`** (decía `~52` en una viñeta y publicaba el **52 exacto** en su tabla), precisado el **ratio a 883,21:1** (`ratio_desbalance_max_min`) y el **`dos` a 45.927**. **Falso positivo respetado: el `~52,5 %` de `4.2` es un porcentaje.** **Las sedes NO autorizadas —tres de ellas docstrings de código— quedan en ficha nueva** | `1075dfd` |
| 2026-08-17 | Informe | **🟡 AMPLIACIÓN del `00 Índice TFG.md` — CERRADA, y eran QUINCE sitios, no nueve.** Además de las **nueve** secciones marcadas «✍ teoría — guion propuesto» que en disco están `redactada`, había **seis entradas más del capítulo 2** (`2.1.1`–`2.1.5` y `2.2.1`) **dadas por borrador**. Corregidos también **`4.2`**, **`6.2`** (339 líneas), la **leyenda** (retirados `✍ teoría` y `esqueleto`, que **no los llevaba ninguna nota**) y la **cabecera y totales**, ahora **en tabla por estado**. **Hallazgo propio del agente: el capítulo 2 tiene 14 notas, no 12** — él mismo escribió 12 al principio y **lo corrigió contando**, que es el error exacto que produjo el desfase original | `1075dfd` |
| 2026-08-17 | Informe | **El recuento de `00 Índice TFG.md:106` — CERRADO CON CRITERIO DECLARADO, que era lo que faltaba: 44 entradas indexadas = 43 notas de memoria + `Bibliografía`.** Aritmética **publicada en la nota**: 54 `.md` en disco − 8 de `99 Investigación/` − el propio índice − `Lecture 1.md` = **44**. Verificado: **los 44 wikilinks resuelven a fichero existente** y **ninguna nota de memoria queda sin indexar**. **El «43» anterior no estaba mal calculado, estaba SIN CRITERIO** | `1075dfd` |
| 2026-08-17 | Informe | **🟡 `4.3:262` — CERRADA: declarada canónica `4.3.5` § «Decisión experimental: 54 frente a 122 (experimento H1)»**, por ser **la única que publica la tabla H1 y cita los artefactos generadores**. Recuento corregido a **diez remisiones / once sedes con la canónica** (decía «nueve» y enumeraba diez). Corregido de paso un **error interno**: el callout **se autodenominaba «este mismo apartado (4.3.7)»** | `1075dfd` |
| 2026-08-17 | Informe | **🟡 El `[!todo]` de `A.3:648` — CERRADO convirtiéndolo en LÍMITE DECLARADO, que es lo que de hecho era.** En `A.3.7` § «Límite de protocolo: tres decisiones del sistema se tomaron con métricas medidas sobre D2», el callout pasa a **`[!warning] Límite declarado de alcance: la corrección no se ejecuta en este trabajo`**, con la **razón técnica** —regenerar los splits **invalidaría las cifras selladas en `A.3.9`**, coherente con la **Decisión 2 de Francisco del 2026-08-14**— y **enlaces a `6.1` y `6.2`** | `1075dfd` |
| 2026-08-17 | Informe | **AUDITORÍA DE LA TANDA 21 — dos rondas, ambas `APTO CON CAMBIOS`, ningún 🔴.** **Ronda 1, 6 hallazgos.** El de fondo, 🟠: **`5.2` etiquetaba como «en D2» soportes que son de los 9.083 ataques de TIPO CONOCIDO de D2** (37 de `u2r`), **chocando con los 200 de `u2r` en D2 completo que publica `4.2`** — **la métrica era correcta; la población, mal etiquetada**. Corregido en **tres sedes de `5.2`**, distinguiendo **37 / 200 / 52 con procedencia**. Los otros cinco: `5.4` afirmaba **en falso** que `5.2` no publicaba las celdas de KNN **y su `[!todo]` ordenaba un trabajo ya hecho** —falso **incluso antes de la tanda**, porque `4.3` ya tabulaba KNN-54—; `4.3` decía «nueve» y enumeraba diez; `5.4` afirmaba que el detalle se publica «una sola vez, en 5.2»; y `2.1.6` seguía con «unas 52 / ~45.900». **Ronda 2, 4 hallazgos:** 🟠 `4.2` definía los soportes de `metricas_firmas.csv` como «partición interna de evaluación», **reabriendo la confusión 52/37 por la puerta de atrás** —corregido a «los ataques de D2 cuyo tipo está presente en el entrenamiento (**9.083 flujos**)»—; 🟡 la frase de sede de `5.4` era **cierta a medias** (`4.3.4` tabula **solo la variante de 54**; las **8 celdas de 122 con `±`** solo están en `5.2`), acotada; 🟡 **doble declaración de canonicidad** entre `4.3.5` y `2.1.6`, desambiguada con tabla: **`6.1` es sede del inventario como limitación, `4.3.5` del alcance y cifras de la desviación 54/122**. **NO hubo tercera auditoría completa, y fue decisión DELIBERADA del `leader`:** los tres hallazgos vivos de la ronda 2 eran **de redacción**, las cifras **ya se habían cotejado celda a celda contra los cuatro CSV en la ronda 1**, y los cuatro pasajes **se verificaron a mano en disco**. Coste evitado **~200 s de auditor para tres frases** | `1075dfd` |
| 2026-08-17 | Informe | **🟠 SÉPTIMO re-anclaje de sello — CERRADO EN PROSA en la TANDA 20, con el sello impreso dentro de los artefactos de `Resultados/` INTACTO** (regla del patrón respetada, verificado). Re-ancladas **`4.2` y `4.3`**: la **tabla de sellos de `4.2`** y su **párrafo de Procedencia** pasan de `a8c20e9-sucio` a **`ac36b88`**, con el commit versionador **`312c179`**, y se retira el **`[!todo]` «Hash del commit de cierre, pendiente de sellar»**. **Citado por nombre de callout y de campo, no por línea** —el anclaje `4.2:269` de la propia ficha estaba desfasado (`:264`/`:266` en disco): **cuarta ocurrencia en dos días** del patrón «referencia `fichero:línea` desfasada», sumada a su ficha abierta, que **no se cierra**. **Hallazgo lateral que la ficha NO preveía:** `4.3:128` no solo repetía el hash viejo, **atribuía mal el mecanismo de sellado** —citaba los campos `Commit del código:` / `Fecha de la corrida:`, que son de los `.txt`, para un artefacto que es `specialized_nsl_kdd_vocabulario_onehot.csv`, **que sella en columnas `commit`/`fecha`**—; corregido en el mismo pase. **Auditoría: PRIMER PASE NO APTO CON DOS 🔴, corregidos y reauditados APTO.** Quedan escritos porque **son patrón**: **(a)** el arreglo afirmó un re-anclaje `a8c20e9-sucio → ac36b88` **QUE NUNCA OCURRIÓ** —el pendiente se cerró **re-corriendo `validacion.py` sobre árbol limpio**, y `ac36b88` es el **sello de la corrida**, no un commit de cierre—; **(b)** transcribió **tres marcas temporales en prosa** contra la decisión cerrada de `resumen-de-decisiones.md:892-905`, **contradiciendo además a `4.2:253-256` ocho líneas antes**. Ambos corregidos: ahora **se remite al campo del artefacto** y hay **cero timestamps en las dos notas**, verificado por `grep` | `5c2a484` |
| 2026-08-17 | Informe | **PASE EN SERIE DEL `researcher` — mantenimiento de `Bibliografía.md` y conversión de los tres últimos `[CITA: …]`. Cierra SIETE fichas, y TRES de ellas describían problemas que NO EXISTÍAN: manda el disco, no el registro.** **Censo actualizado y recontado por dos vías: `Bibliografía.md` pasa a 76 FILAS, `[1]`–`[8]` y `[10]`–`[77]`, `[9]` sigue QUEMADA, PRIMER LIBRE EL `[78]`.** Altas: **`[76]`** Quiñonero-Candela *et al.* (MIT Press, 2009) y **`[77]`** Hindy *et al.* (2020). **6 ficheros**: `Bibliografía.md`, `99 Investigación/Auditoría de Bibliografía.md`, `99 Investigación/Reconstrucción de las 47 citas colgantes.md` y, en el vault, `5.0`, `5.1` y `5.4`. **NO se despachó `auditor-ml`, y con criterio: el pase no toca cifras ni afirmaciones sobre resultados, solo marcadores de cita y metadatos bibliográficos.** Deja **CUATRO decisiones para Francisco**, marcadas en vez de inventadas | `8b5ce15` |
| 2026-08-17 | Informe | **🟡 «`Reconstrucción de las 47 citas colgantes.md:283` reserva el `[58]` para Mitchell» — CERRADA, Y EL EQUIVOCADO ERA LA FICHA.** El `[58]` de `Bibliografía.md` **estaba bien** (KDD Cup 1999 Data); quien mentía era el informe, que escribió una **previsión antes de la Tanda 9** y quedó leyéndose como un hecho. **Mitchell ya existía como `[60]` y lo citan tres notas**: no procedía ni alta ni renumeración. Corregida la reserva en el informe, sin borrar su historial | `8b5ce15` |
| 2026-08-17 | Informe | **🟡 «`Auditoría de Bibliografía.md` contradice en CINCO líneas los ✅ EJECUTADO de `Bibliografía.md`» — CERRADA, y EL EQUIVOCADO ERA EL INFORME DE AUDITORÍA EN LAS CINCO.** Anotadas como **superadas, sin borrar el historial** del informe. Mismo patrón que la ficha de arriba: un artefacto fechado se sigue leyendo como estado vigente | `8b5ce15` |
| 2026-08-17 | Informe | **🟡 «Los localizadores de página solo han bajado a `6.2:306`» — CERRADA CON RESULTADO VACÍO, Y EL VACÍO ES EL RESULTADO, no un no-hacer.** Barrido de los **8 libros** (`[4]`, `[5]`, `[6]`, `[7]`, `[8]`, `[12]`, `[39]`, `[54]`) **fuera del capítulo 2**: los capítulos **1, 4, 5, 6 y los apéndices NO contienen ni una sola cita a un libro**. **No había nada que estampar.** El alcance de la ficha queda por tanto agotado | `8b5ce15` |
| 2026-08-17 | Informe | **🟡 TRES `[CITA: …]` VIVOS en la memoria — CERRADA: convertidos los de `5.0:160`, `5.1:86` y `5.4:78`.** Eran los primeros desde que la Tanda 16 los dejó a cero, y **estaban bien puestos**: ningún redactor inventó un `[n]`. **Recontado al cerrar: CERO marcadores `[CITA: …]` pendientes en la memoria** | `8b5ce15` |
| 2026-08-17 | Informe | **🟡 «`Bibliografía.md:58` promete un `— (no es libro)` que solo existe en las filas nuevas» — CERRADA**, junto con el **localizador de `[49]` Bendale y Boult** (apuntaba a `2.3.2.5`; en disco está en **`2.3.2.4`**). Dos correcciones locales del mismo fichero, del `researcher` y en serie | `8b5ce15` |
| 2026-08-17 | Informe | **La corrección (6) de la TANDA 5 — CERRADA, y con ella la ficha entera de «las 3 correcciones LOCALES».** El «Dónde se usa» de **`[2]` (Anderson)** y **`[3]` (Denning)** omitía usos reales —`2.3.2:36` y `2.2.2:35` entre ellos—, y **sobrevivió al pase de la Tanda 9, donde tocaba resolverla**. Las correcciones (2) y (3) de esa ficha ya estaban absorbidas por la Tanda 6. **De paso, dato falso propio de `Bibliografía.md` corregido: `[8]` declaraba DOS usos y en disco son TRES** | `8b5ce15` |
| 2026-08-17 | Informe | **T9 · RESUELTA — y el hallazgo es que LA FICHA IBA UN DÍA POR DETRÁS DEL DISCO.** El recorte del capítulo 3 **ya estaba ejecutado desde la TANDA 12 (2026-08-16)**, con respaldo en `resumen-de-decisiones.md:983-1049`; el `redactor-tfg` no modificó nada porque no había nada que aplicar, y los bullets «lo que sigue vivo» describían trabajo hecho la víspera. **Auditoría adversaria: APTO CON CAMBIOS, no pudo falsar el hallazgo** — S1–S13 y S15 vivos, S14 y las repeticiones legítimas intactas por diseño, `3.3` renumerada sin remisiones rotas, las once anclas del capítulo existentes, los diez `[n]` sin huérfanos, el *data snooping* enunciado una sola vez (`3.3:29`), y **`3.1` confirmada como «no procedía intervención»**. **Tres correcciones de una o dos líneas, sin tocar cifras ni citas:** aviso de estado fechado en `99 Investigación/Datos repetidos en el capítulo 3.md` (su censo afirmaba **en presente** que `3.4.5` no existe, y sí existe; análisis **no reescrito**, por ser artefacto fechado), retirada de las auto-remisiones a §3.5.2 desde dentro de §3.5.2 (`3.5:48,52`) y alta de «4.3.7 Preprocesado sin fuga de datos» en la remisión anti-*leakage* de `3.3:23`. **La cifra para el profesor se mantiene TAL CUAL y nadie la ha tocado: ≈20 % en total y ≈25 % en `3.1`–`3.3`, estimación redondeada a la decena y SIN script de conteo que la respalde.** **No marcada como aceptada: eso lo decide Francisco** | `198fab6` |
| 2026-08-17 | Informe | **CICLO DE RECONCILIACIÓN del trabajo huérfano — 11 ficheros, cero código, cero corridas, ninguna cifra publicada movida.** Los ficheros sin commitear los habían dejado **tres agentes muertos por límite de API**; verificado contra disco, su trabajo estaba **completo, no a medias**, pero **no había pasado auditoría**, así que se auditó antes de nada. **Dos pases, ambos APTO CON CAMBIOS, ningún 🔴**; los **8 hallazgos aplicados y verificados**. Censo de citas **intacto: 74 filas, primer libre `[76]`, cero `[n]` nuevos o renumerados, cero `[CITA: …]` nuevos**. Ficheros: `Implementacion/PIPELINE.md`, `Resultados/GUIA_RESULTADOS.md`, `resumen-de-decisiones.md` y, en el vault, `2.1.6`, `4.4`, `4.5`, `5.0`, `5.2`, `5.4`, `6.1`, `A.3` | `822e4c5` |
| 2026-08-17 | Informe | **🟡 Los punteros al «inventario completo» — CERRADO: hoy hay UNA sede canónica, `6.1`, y las NUEVE remisiones apuntan allí.** La ficha contaba cuatro destinos (`4.6`, `6.1`, `A.3`+`6.1`, `4.3`+`6.1`); resolverlo era **fijar la sede y repuntar**, no elegir la más cómoda. **El hallazgo 🟠 del pase de auditoría iba justo aquí**: `A.3.7` conservaba un **inventario rival** sin remitir a `6.1`, y **`5.0` le había quitado el puntero en silencio**. Resuelto **sin borrar la tabla**: `A.3.7` queda como **volcado tabulado con enlace recíproco a `6.1`** | `822e4c5` |
| 2026-08-17 | Código | **🟠 El re-anclaje pendiente de `validacion.py` (`a8c20e9-sucio`) — CERRADO EJECUTÁNDOLO, no en prosa.** Los **seis artefactos** de `validacion.py` (los dos `*_validation_report.txt`, los dos `*_vocabulario_onehot.csv` y los dos `*_composicion_d3.csv`) llevan ya el sello **`ac36b88`**, **LIMPIO y sin sufijo `-sucio`** —se corrió sobre árbol limpio, que era el requisito—, con corridas `2026-08-17T20:42:19` (con selección) y `20:42:33` (sin selección); **`a8c20e9-sucio` ha desaparecido de los seis**, verificado en el ARTEFACTO y no en el script. **Cifras intactas**: `dos` 45.927 / 78,3336 %, `probe` 11.656 / 19,8806 %, `r2l` 995, `u2r` 52, total **58.630**, ratio 883,21; vocabulario one-hot **122** en ambas variantes (correcto: se mide sobre los `_original_*`, antes de la selección); D1 67.343 / D2 22.544 / 9.711 normales, drift (A) 37 vs (B) 25, outliers 4,78 %. **Ninguna `Resultados/metricas_*.csv` tocada: solo `commit` y `fecha`.** Auditoría `auditor-ml`: **APTO CON CAMBIOS**, los tres aplicados; **la frontera `validacion.py` → `config.py` NO se ensanchó** (`commit_actual()` en `:148` y `CATEGORIAS_ATAQUE` en `:457-458`/`:470`, **ningún uso produce ni altera un recuento**), sin fuga de datos y el drift T2 sigue publicado como **comparación** `delta = (A) − (B)` | `312c179` |
| 2026-08-17 | Código | **SEXTO caso del patrón «prosa que anuncia en presente algo ya resuelto» — el recuento del patrón es el dato.** A raíz de la auditoría del re-anclaje de `validacion.py`, tres restos de `Resultados/GUIA_RESULTADOS.md` declaraban **vivo** un pendiente ya cerrado: **§6.2 (`:627-628`)**, la entrada del 2026-08-17 de **§7 (`:750-751`)** —con su **referencia cruzada ROTA** al `[!todo]` de §2.4— y la **glosa de cierre de la entrada histórica del 2026-08-16 (`:764-769`)`**. Corregidos los tres. `PIPELINE.md:248-257` y `:309` quedan coherentes con el sello nuevo, sin `[!todo]` residual | `312c179` |
| 2026-08-17 | Código | **🟠 SEXTO re-anclaje de sello (`commit_agregador = 0276039-sucio`) — CERRADO EN PROSA, con el sello impreso INTACTO.** Los tres artefactos del agregador siguen llevando `0276039-sucio` **verificado en los tres**: el sello lo estampa `config.commit_actual()` y **no se reescribe a mano**, así que el re-anclaje va en el texto que lo lee. El `auditor-ml` lo dio por **correcto y sustantivo, no cosmético** | `822e4c5` |
| 2026-08-17 | Informe | **Hallazgo PROPIO, fuera de la auditoría: `6.1:65` seguía publicando que la banda de 4,8× «mide carga de máquina».** Esa afirmación **la retiró la Tanda 18 de `4.4` y `A.3` por FALSA** —las dos corridas de la banda no registran épocas—, pero **nadie había revisado `6.1`**. Corregida a **«magnitud observada sin causa atribuida»**. Es el **cuarto caso del mismo patrón**: se arregla una sede y la afirmación sobrevive en otra | `822e4c5` |
| 2026-08-17 | Código | **🟠 El «8 de 10» PAREADO — CERRADO: YA LO EMITE UN SCRIPT, y las cifras del artefacto COINCIDEN EXACTAMENTE con el conteo a mano que sustituyen.** `agregar_semillas.py` produce **`Resultados/comparaciones_pareadas.csv`** (13 filas + cabecera) con **tres comparaciones**: RF vs HGB en `f1_macro` y los **dos ejes de balanceo**. Cifras de la ejecución real: **8 de 10 en `122_sin_seleccion`** (RF pierde en las semillas **5** y **9**), **8 de 10 en `54`** (pierde en **3** y **5**), **16 de 20 global**, **`SMOTE vs nada` 40 de 40**, **`SMOTE vs class_weight` 23-17**, **cero empates**. Con esto **`5.2:107` deja de apoyar su formulación portante en un recuento a mano**, que era el agravante de la ficha: quince líneas más abajo la propia nota exigía ese criterio para el «13 de 98» | `98a0289` |
| 2026-08-17 | Código | **🟡 La palabra «determinista» FUERA de `PIPELINE.md` — CERRADA, con la salvedad escrita donde el generador la repone.** Corregida en **`agregar_semillas.py` (`:226`/`:245`)** —la sede que regenera `Resultados/dispersion_semillas.md`, artefacto citable y versionado— y en **`anomalias.py`**. **Las sedes legítimas quedaron INTACTAS, verificado**: `anomalias.py:190`, `program.py:310`/`:528`, `figura_nids_bloques.py:39` y `4.3:86`/`:92`, más las de «suciedad **indeterminada**» de `config.py`, que son otra cosa | `98a0289` |
| 2026-08-17 | Código | **El residuo de T22 — CERRADO SIN REESCRIBIR LA DECISIÓN, que era justo el ⛔ de la ficha.** Dos **notas fechadas** en `resumen-de-decisiones.md` registran la **reapertura autorizada por Francisco el 2026-08-17**; las líneas **`:633`** (título de la decisión), **`:636`** (cuerpo) y **`:1154`** (eco) quedan **INTACTAS y legibles**. Es la misma disciplina que se aplicó al «~17»: se añade nota, no se sobrescribe historia | `98a0289` |
| 2026-08-17 | Código | **Alta del CSV citable `comparaciones_pareadas.csv` en los CUATRO runbooks**: `Implementacion/PIPELINE.md`, `README.md`, `Resultados/GUIA_RESULTADOS.md` y `CLAUDE.md`. Es el barrido que en las Tandas 10, 15 y 16 se quedó corto: un artefacto nuevo sin entrada en el runbook es un artefacto que nadie sabe releer | `98a0289` |
| 2026-08-17 | Código | **Auditoría del ciclo: APTO CON CAMBIOS, 6 hallazgos, NINGUNO 🔴.** El `auditor-ml` confirmó que **el pareo es real por semilla** —no una comparación de medias disfrazada— y que **el 🔴 histórico (sd entre *folds* vendida como dispersión entre semillas) NO reapareció**. **Cinco hallazgos aplicados y verificados contra disco.** **Las cuatro tablas de métricas principales siguen con mtime del 9 de agosto: intactas** | `98a0289` |
| 2026-08-17 | — | **FALLO DE PROCESO (no de código) que merece quedar escrito: el primer pase de hallazgos reportó `done` con tres arreglos que solo existían en el `.py`.** Editó el **generador** y **no lo relanzó**, dejando los **artefactos citables con el texto viejo**. **Lección operativa: un `done ->` no prueba nada; en track Código con generadores hay que verificar el ARTEFACTO, no el script** | `98a0289` |
| 2026-08-17 | Informe | **TANDA 19 — cae el BLOQUEANTE DECLARADO DE LA FASE 5.** Cierra **cuatro fichas**: el **barrido de solapes del capítulo 2**, el **🟡 «determinista» de `PIPELINE.md`**, el **⛔ «~17»** y **T4**. Ficheros: `Implementacion/PIPELINE.md`, `resumen-de-decisiones.md`, `next-steps.md` y, en el vault, `2.1.1`, `2.2.2`, `2.2.3`, `2.3.2`, `5.2`, `5.4`. **Tres pases de auditoría, todos resueltos** (2 APTO, 2 APTO CON CAMBIOS aplicados). **Cero `[n]` nuevos o renumerados, cero cifras publicadas movidas, cero `fit`.** Censo contado contra disco: **74 filas, primer libre `[76]`** — coincide con `CLAUDE.md`. **Deja CUATRO fichas nuevas, ninguna bloqueante** | `b276f97` |
| 2026-08-17 | Informe | **El barrido de solapes del capítulo 2 — CERRADO, y era el bloqueante declarado de la Fase 5.** Su razón de ser, escrita desde el 2026-08-15: **recortar el capítulo 3 remitiendo a un capítulo 2 sin barrer es remitir a texto que también duplica.** Revisadas **las 12 notas que faltaban** (el barrido previo solo cubría `2.1.6` y `2.2.4`); **6 solapes corregidos con sede canónica fijada y remisión**, en **`2.1.1`, `2.2.2`, `2.2.3` y `2.3.2`**. **`2.3.3` no se tocó**: ya iba en la Tanda 18 (Axelsson realineado). Auditoría de **coherencia ENTRE notas**: los 6 recortes **siguen vivos en su sede** —el fallo propio de un recorte es la afirmación huérfana—, **wikilinks y anclas verificados** | `b276f97` |
| 2026-08-17 | Código | **🟡 `PIPELINE.md` «determinista» — CERRADA, y la auditoría cazó que la palabra SOBREVIVÍA al primer arreglo.** La ficha señalaba `:925`; el arreglo se aplicó en **`:945` y `:1379`**, y `:945` era **la frase titular en negrita, la que un tercero copiaría a la memoria**. Se cambió **la palabra, no el dato**: el **162/128**, la tabla, la conclusión y los factores quedan **intactos**. **La palabra sigue viva FUERA de `PIPELINE.md` y allí está PEOR, sin salvedad**: ficha nueva en `## Abiertas` | `b276f97` |
| 2026-08-17 | — | **⛔ El «~17» — CERRADO: las 7 ocurrencias aplicadas** (4 en `resumen-de-decisiones.md`, 3 en `next-steps.md`). **Sobraba el «~», no el número: el 17 es EXACTO.** Añadida la **nota fechada** (`resumen-de-decisiones.md:1388-1396`) registrando que se reescribió texto previo **por excepción expresa de Francisco del 2026-08-16** y que **la Decisión 3 sigue vigente para todo lo demás** — sin esa nota parecería una violación de su propia regla. **Falsos positivos `~170 MB` intactos**, verificado. **Recontado contra disco al cerrar: CERO «~17» en todo el árbol** | `b276f97` |
| 2026-08-17 | Código | **T4 · CERRADA — y se cerró VERIFICANDO la condición, no dándola por buena.** Lo exigido no era que `5.2`/`5.4` existieran sino que **CONSUMIERAN la banda**: contrastado **celda a celda** contra `dispersion_semillas.csv`, **la banda SÍ está genuinamente consumida**, y el **🔴 histórico *folds vs semillas* NO ha reaparecido** —era el error que T4 existe para evitar—. De los **5 hallazgos** de su verificación se aplicaron **3**: los punteros de `5.2:146` y `5.2:184`, y la banda y la media en `5.4`. Veredicto final **APTO** | `b276f97` |
| 2026-08-17 | Código | **`PIPELINE.md:596-611` — desambiguado un HOMÓNIMO que iba a morder.** El «8 de 10» de la sección de tiempos son **pares de tiempo de ENTRENAMIENTO intra-corrida**, y el «8 de 10» del capítulo 5 son **semillas en que RandomForest gana en `f1_macro`**: **dos recuentos distintos con el mismo aspecto**. Ahora lleva `[!warning]` explícito. **No es cosmética**: la formulación pareada del capítulo 5 tiene ficha 🟠 abierta justo por no estar emitida por script, y confundirla con la de tiempos habría dado por respaldada la que no lo está | `b276f97` |
| 2026-08-17 | Informe | **TANDA 18 — cierra T19 y limpia la afirmación falsa que la propia ficha sembraba.** Cuatro ficheros del vault, **cero código**: `4.4 …anomalías.md`, `3.2 Arquitectura del sistema.md`, `2.3.3 Límites y consideraciones éticas.md` y `Apéndices/A.3 Ficha del sistema.md`. **Cero `[n]` nuevos, cero `[CITA: …]` nuevos, cero cifras publicadas movidas.** Auditada en **tres pases por seis correctores**, con los hallazgos aplicados. Censo de citas **intacto: 74 filas, primer libre `[76]`** | `e1bda55` |
| 2026-08-17 | Informe | **T19 · CERRADA — `4.4` era la CUARTA y última sede, y la única que aún contradecía a `5.1`.** Su tabla publicaba **`5,0 s`** para IsolationForest cuando `5.1` ya publica **3,51 s de entrenamiento y 5,27 s de bloque**; la contradicción **la había creado el arreglo de la Tanda 17** al corregir un lado y no el otro. Tabla **verificada celda a celda** contra `Resultados/metricas_anomalias.csv`. Las otras tres sedes (`5.1:44-47`, `5.1:58`, `5.2:59`) se habían cerrado en la Tanda 17 (`9bcfe1f`) | `e1bda55` |
| 2026-08-17 | Informe | **🔴 de método: LA FICHA T19 ERA LA FUENTE DEL ERROR, no solo su registro.** El texto de `features.md:1015-1021` afirmaba que la banda de **4,8×** se da «**con el recuento de épocas idéntico**» y que el reparto «**conserva el orden de las ocho filas**». **Las dos son falsas, y las dos se habían PROPAGADO A LAS NOTAS** —`4.4` y `A.3:417-418` publicaban la primera— porque cada redactor las copió del registro sin recontarlas. **(a)** Las dos corridas de la banda (`38fdd4b` → `5516b60`) **no registran épocas**: `n_iter_total_grid` solo existe en `ac496cb` y `1163c90`, y `PIPELINE.md:923-929` ya lo declara por escrito. La banda pasa a **magnitud observada SIN causa atribuida**. **(b)** El orden se conserva **casi entero**: `IsolationForest` 122 **baja del 4.º al 6.º**, adelantada por las dos filas de `LocalOutlierFactor`. **(c)** Los **4,5 pp** son del **residual**, no de «cada tramo». **El texto de la ficha se corrigió al retirarla, y la MISMA afirmación se corrigió también en la ficha de T4, que sigue abierta y la repetía palabra por palabra** | `e1bda55` |
| 2026-08-17 | Informe | **Los otros tres hallazgos aplicados en la tanda.** **(1) 🟠 en `4.4`: equivalencia falsa con §5.1.2** que mezclaba el **AUC de validación (0,9918)** con el **AUC sobre D2 (0,923)** —son columnas distintas del mismo CSV, `auc_val` frente a `roc_auc`—; sustituida por una tabla que separa población y contenido de ataque y explica por qué la caída es esperable. **(2) 🟡 en `3.2`:** el FPR del baseline **se comparaba por variante solo en un lado**. **(3) 🟡 en `2.3.3`:** Axelsson **realineado con su sede canónica**, dentro del barrido de solapes del capítulo 2 —el punto 2 de la lista de cierre de la Tanda 12— | `e1bda55` |
| 2026-08-17 | Informe | **A.3 · segundo pase de auditoría: `A.3:417-418` repetía la MISMA afirmación falsa sobre las épocas** que se acababa de retirar de `4.4`. **Es el valor de auditar la tanda como unidad**: la nota no se había despachado por ese motivo y el fallo solo aparece al cruzarla con `4.4`. Corregido, y con la **salvedad obligatoria de que `ac496cb` no es reproducible desde git** ya declarada en `:429-431` | `e1bda55` |
| 2026-08-17 | Código | **T4 · DESBLOQUEADA (no cerrada).** Su única condición viva era que **`5.2`/`5.4` estuvieran escritos**, y lo están desde la **TANDA 17** (`9bcfe1f`, que cerró T11 con el capítulo 5 completo). El registro seguía dándola por bloqueada — **mismo patrón que ya ha mordido cuatro veces: una ficha sobrevive a su propio desbloqueo porque nadie la recuenta al cerrar**. Lo que queda es **verificar que la banda está consumida** en `5.2`/`5.4`, no solo que las notas existan | `e1bda55` |
| 2026-08-17 | — | **TANDA 17 — el capítulo 5 COMPLETO más el cierre de T10. Siete agentes de escritura en paralelo sobre ficheros disjuntos y TRES pases de auditoría.** Cierra **dos fichas**: **T11 · capítulo 5** (`5.0`–`5.4`, cinco notas redactadas a la vez) y **el bullet del «17» de T10**, que era el último vivo de esa ficha —**con lo cual T10 QUEDA CERRADA**—. **13 ficheros**: las cinco notas de `05 Evaluación/`, `4.2`, `99 Investigación/clasificadores-tabulares-y-arquitecturas-hibridas.md`, `EL_FUTURO.md`, `Guia_ML/` ×3, `Implementacion/app/baseline.py` y `firmas.py`. **413 inserciones.** Censo de citas **intacto: 74 filas, primer libre `[76]`** | `9bcfe1f` |
| 2026-08-17 | Informe | **🔴🔴 EL PRIMER PASE DE AUDITORÍA DEL CAPÍTULO 5 FUE NO APTO CON DOS ROJOS, Y LOS DOS ERAN CIFRAS FALSAS. Queda escrito porque son los dos errores más graves que ha cazado una auditoría en este proyecto.** **(1) `5.2` presentaba como «desviación típica a lo largo de las diez semillas» unos `±` que son la sd ENTRE LOS 5 *FOLDS* DE LA SEMILLA 42.** Es dispersión **intra-corrida** vendida como **inter-semilla**, y sostenía el argumento central del apartado: exactamente la confusión que **T4 existe para evitar**. **(2) `5.1` publicaba CUATRO TIEMPOS QUE NO EXISTEN EN NINGÚN ARTEFACTO** (5,04 / 28,34 / 16,42 / 40,56 s); los reales son **5,27 / 25,58 / 20,16 / 49,20**. De ahí salía el titular **«ocho veces menor»**, que era **×9,3 o ×13,9 según la columna**, y que **ya se había propagado a `5.4`**. **Ambos corregidos y VERIFICADOS CERRADOS en un segundo pase** | `9bcfe1f` |
| 2026-08-17 | Informe | **Cómo se cerraron los dos rojos — no con un parche, sino declarando lo que la cifra es.** En **`5.1`** se publican ahora **LOS DOS RATIOS con su porqué**: **×13,9 sobre el tiempo de entrenamiento** (3,51 s de IsolationForest frente a 48,93 s del Autoencoder) y **×9,3 sobre el bloque completo** (5,27 s frente a 49,20 s), explicando que difieren porque en el Autoencoder casi todo el bloque es entrenamiento mientras que en IsolationForest pesa también el puntuado. En **`5.2:145-146`** el `±` queda **declarado explícitamente**: es `f1_macro_cv_std`, la sd **entre los 5 *folds* de esa misma corrida**, dispersión **intra-corrida**, y la nota dice **que NO es la dispersión entre semillas** —que vive en `metricas_balanceo_semillas.csv` y **no se mezcla ahí** | `9bcfe1f` |
| 2026-08-17 | Informe | **Los otros hallazgos de los tres pases — 6 🟠 y 6 menores, APLICADOS.** El más ilustrativo, y el fallo típico de tanda paralela: **la rejilla C1-C7 estaba definida ENTERA DOS VECES, con C5 enunciado de dos maneras distintas**. Es el defecto que **solo se ve auditando la tanda como unidad**, no nota a nota —mismo patrón que el Kim et al. duplicado de la Tanda 12— | `9bcfe1f` |
| 2026-08-17 | Mixto | **El bullet del «17» — CERRADO, y CIERRA T10. La ficha mentía en DOS sitios, y ambos se descubrieron abriendo los ficheros en vez de fiarse de la lista.** Dato verificado contra disco: **17 tipos 0-day, 3.750 filas de D2**. **(1) `firmas.py:157` era en realidad `:174`.** **(2) Los supuestos «~17» de `.gitignore` y `README.md` eran `~170 MB`**: falsos positivos que **nadie había abierto** y que llevaban tiempo en la ficha. Era de **track MIXTO**, y por eso tocó `baseline.py` y `firmas.py` además de la prosa | `9bcfe1f` |
| 2026-08-17 | — | **⛔ ABIERTA · EL «~17» DE `resumen-de-decisiones.md` Y `next-steps.md` SIGUE SIN CORREGIR, Y FRANCISCO YA LO AUTORIZÓ. Es lo primero que hay que retomar.** Quedan **7 ocurrencias**: **4 en `resumen-de-decisiones.md`** (`:65`, `:153`, `:298`, `:299`) y **3 en `next-steps.md`**. **Francisco concedió el 2026-08-16 una EXCEPCIÓN PUNTUAL Y EXPRESA** para reescribir texto previo en ambos —preguntado con las alternativas sobre la mesa—, pese a que la **Decisión 3 de la Fase 0** solo autoriza añadir nota fechada en el primero y a que `next-steps.md` está **CONGELADO**. **El agente cayó por límite de API antes de escribir nada: ambos ficheros están INTACTOS, verificado contra `git status`.** **El alcance autorizado es SOLO el dato del «~17»**, nada más. **Lo que sobra es el «~» / «aproximadamente», NO el número: el 17 es EXACTO.** Al hacerlo, **dejar nota fechada en `resumen-de-decisiones.md`** registrando que se reescribió texto previo por autorización expresa y que la Decisión 3 sigue vigente para todo lo demás — sin esa nota, parecería una violación de su propia regla. **Ojo a los falsos positivos ya identificados: `~170 MB`** | `9bcfe1f` |
| 2026-08-17 | Informe | **🟡 ABIERTA · `5.4:42` atribuye a `[18]` Arp que el error es «endémico en seguridad», sin número de *pitfall*.** El problema es que **el propio capítulo se contradice**: `5.0` acaba de acotar que de Arp et al. este TFG **solo toma P5 por número**, así que `5.4` atribuye más de lo que el capítulo declara usar. **Se preguntó a Francisco y la respuesta no llegó**, así que **se toma la vía conservadora: se deja como está y se ficha. NO se fuerza una cita.** Al retomar: o se ancla a un *pitfall* concreto verificable, o se enuncia sin colgárselo a Arp | `9bcfe1f` |
| 2026-08-17 | Informe | **🟡 ABIERTA · TRES `[CITA: …]` VIVOS en la memoria, los primeros desde que el pase de la Tanda 16 los dejó a cero.** Están en **`5.0:160`, `5.1:86` y `5.4:78`**, los tres del capítulo 5 recién redactado. **Es lo correcto** —ningún redactor inventó un `[n]`— y quedan pendientes del **pase en serie del `researcher`**, que **ya no requiere petición explícita** de Francisco. Censo al cerrar: **74 filas, primer libre `[76]`** | `9bcfe1f` |
| 2026-08-17 | — | **HALLAZGO (no cierra ficha) · DOS FICHAS MUERTAS que aún figuraban ABIERTAS, detectadas contra disco.** **(1)** La de **`2.1.4:77` (LOF)** ya está resuelta: `2.1.4:76` cita **`[75]` Breunig** desde el pase de la Tanda 16. **(2)** El **punto 6 de las «seis afirmaciones desfasadas»** (`[6]` Goodfellow huérfana) también. **Es el mismo patrón que ya ha mordido tres veces en este fichero**: una ficha sobrevive a su propio arreglo porque nadie la recuenta al cerrar. Se registran aquí para que la próxima sesión las cierre en vez de redespacharlas | `9bcfe1f` |
| 2026-08-16 | — | **TANDA 16 — la primera tanda de track CÓDIGO desde la reapertura del 2026-08-06 en este bloque de tandas.** Ficheros: **15 modificados + 2 nuevos** — `Implementacion/app/validacion.py`, `Implementacion/app/config.py`, `Implementacion/PIPELINE.md`, `Resultados/GUIA_RESULTADOS.md`, `Obsidian_TFG_Vault/04 Implementación del sistema/` `4.2`, `4.3`, `4.5` y `4.6`, los dos `*_validation_report.txt`, los dos `*_vocabulario_onehot.csv` y `resumen-de-decisiones.md`; **nuevos**: `Resultados/specialized_nsl_kdd_composicion_d3.csv` y `Resultados/specialized_nsl_kdd_sin_seleccion_composicion_d3.csv`. **Cero `fit`, ninguna cifra publicada movida, cero `[n]` inventados.** **Regeneración confirmada como esperada y verificada línea a línea:** los `vocabulario_onehot.csv` cambian **8 líneas que son 4 filas reescritas SOLO en `commit,fecha`** —mediciones idénticas, 77→122, delta 45—; los reports cambian **16 líneas que son el bloque nuevo**; **drift 37/25 y 44/31, outliers 4,78 %/2,44 % y los tamaños quedan INTACTOS**. Incluye el arreglo del 🟡 de `specialized_nsl_kdd_validation_report.txt:20`, que imprimía `(fuente: <base_path>_composicion_d3.csv)` **sin expandir** (`validacion.py:1266`), y su **re-corrida antes del commit** —decisión de Francisco— para que **los seis artefactos no queden con un sello distinto al que la prosa acaba de publicar**. **La ficha que dejó señalada para Francisco —la frontera `validacion.py`→`config.py`— YA NO está abierta: Francisco la APROBÓ el mismo día**, preguntado con las dos alternativas sobre la mesa. **El alcance real de la tanda creció después de este registro**: incluye además el arreglo del literal `<base_path>`, la decisión de **dejar de citar marcas temporales en la prosa**, la unificación de la fuente del nombre del CSV y un pase de `Bibliografía.md`. Ficheros finales: **18 modificados + 2 nuevos** | `055e1b4` |
| 2026-08-16 | Código | **La ficha 🟠 «El reparto por categoría de D3 (45.927 / 11.656 / 995 / 52) NO lo emite ningún script» — CERRADA: ya lo emite.** `validacion.py` gana **`medir_composicion_d3()`**, que deriva todo de `value_counts()`/`len()` —**cero hardcodeo**—, con **guarda de cuadre que revienta si las categorías no suman el total** y **cero `fit`**. Emite **dos CSV nuevos versionados** (`con_seleccion` y `sin_seleccion`) con las cifras que hasta hoy eran **un recuento a mano**: **45.927 / 11.656 / 995 / 52**, total **58.630**, **DoS 78,3336 %** y `ratio_desbalance_max_min` **883,21**, con **procedencia estampada**. `PIPELINE.md` y `GUIA_RESULTADOS.md` actualizados y **`4.2`, `4.3`, `4.5` y `4.6` repuntadas al artefacto**. Era el **precedente exacto del «13 de 98»** (`9d4c26d`), y se salda igual: la cifra ya no depende de que alguien la contase bien una vez | `055e1b4` |
| 2026-08-16 | Código | **`4.6:13` — ACOTADA, y NO por la razón que la ficha preveía.** La ordenación dura («ningún número que llegue a la memoria procede de una ejecución manual») **se respetó** y la emisión la volvía cierta por el lado de D3, **pero seguía sin ser literalmente cierta por OTRO caso**: `4.2:104-110` declara que los porcentajes de D2 son «cociente directo de esos recuentos, no cifras leídas de ningún artefacto». Queda acotada **con esa excepción citada literal**, **sin prometer automatizaciones** que nadie ha hecho. El orden exigido por la ficha —emitir primero, acotar después— se cumplió | `055e1b4` |
| 2026-08-16 | Código | **EL PRIMER PASE DE `auditor-ml` FUE NO APTO, y esto queda escrito porque NO HABÍA CORRIDO ANTES DEL CORTE POR LÍMITE DE API.** Corrió después. **El código, las cifras y la ausencia de leakage eran correctos: lo que falló fue el BARRIDO DE DOCUMENTACIÓN** — `4.2:217-218`, `4.2:224` y `4.3:128` seguían publicando el sello **`fc1c6b4-sucio`** y fechas del **2026-08-11** **de artefactos que esa misma corrida había sobrescrito**: las dos notas que el ciclo editó, **repuntadas a medias**. **Tres rondas de corrección, y cada una introdujo un defecto nuevo que la siguiente auditoría cazó.** Veredicto final: los **4 puntos del segundo pase y los 3 del tercero**, aplicados y **verificados en disco línea a línea**. Es el mismo defecto de barrido corto de las Tandas 10 y 15, ahora sobre sellos de procedencia | `055e1b4` |
| 2026-08-16 | — | **HALLAZGO (no cierra ficha) · EL `.gitignore` NO TIENE FALLO, y conviene que quede registrado POR QUÉ, porque la duda va a volver.** Los dos CSV nuevos **DEBEN versionarse**. La frase de `CLAUDE.md` («modelos y CSV, no») es una **simplificación imprecisa**: el `.gitignore` real solo excluye `Resultados/*_processed_*.csv` y `*_original_*.csv` —los splits, regenerables y pesados—. **`composicion_d3.csv` no casa con ningún patrón**, igual que `metricas_*.csv`, `dispersion_semillas.csv` y `vocabulario_onehot.csv`, **que ya están versionados** (verificado por el hilo principal: **20+ CSV versionados en `Resultados/`**). Documentado en `validacion.py:1508-1511` | `055e1b4` |
| 2026-08-16 | Código | **🔴 F1 — LA RE-CORRIDA ROMPIÓ 17 CITAS DE PROCEDENCIA, y de ahí sale una DECISIÓN DE FONDO de Francisco. Es el hallazgo más importante de la tanda.** Al re-correr `validacion.py` para arreglar el 🟡 del `<base_path>`, los seis artefactos cambiaron su marca temporal, y **17 líneas en 5 ficheros seguían citando las muertas** (`PIPELINE.md`, `GUIA_RESULTADOS.md`, `resumen-de-decisiones.md`, `4.2`, `4.3`). **Dos de ellas decían «verificado en disco»**, y **`PIPELINE.md:291` PROPAGABA ACTIVAMENTE EL ERROR**: instruía a «copiar los segundos que trae ese fichero». Dictamen del `auditor-ml`: **NO APTO**. **Es exactamente la avería que la tanda venía a reparar, reaparecida por el propio arreglo.** ⛔ **DECISIÓN DE FRANCISCO (2026-08-16): la prosa del proyecto DEJA DE CITAR la marca temporal** y remite al campo del artefacto (`Fecha de la corrida:` en informes, columna `fecha` en CSV). **El `commit` SÍ se sigue citando**: identifica el estado del código y **no cambia al re-correr**. Motivo: copiar los segundos hacía que **cada re-corrida futura invalidase la memoria**. La instrucción de `PIPELINE.md:291` queda **DEROGADA** explícitamente. **Barrido final: CERO marcas temporales de corrida en todo el árbol `.md`** | `055e1b4` |
| 2026-08-16 | — | **DOS EXCEPCIONES RAZONADAS a la decisión de F1, que NO se tocaron y conviene que queden escritas para que nadie las «arregle» luego.** **(1)** Las filas de **corridas HISTÓRICAS** de la tabla canónica de `PIPELINE.md` (`fc1c6b4-sucio`, `df30cb2`, `00c3c3e-sucio`, `ddade37-sucio`, `6bb224c-sucio`): sus artefactos **ya no están en disco**, así que la marca temporal es ahí el **único identificador** de la invocación y **no puede caducar por re-corrida**. **(2)** `GUIA_RESULTADOS.md:23-24`, `:575-584`, `:602-603` y `:732-760`: varias pasadas de `agregar_semillas.py` **comparten commit y solo se distinguen por la hora**, así que ahí la marca **identifica, no decora**. **La regla de F1 aplica a lo que se puede re-correr, no a lo que ya es historia** | `055e1b4` |
| 2026-08-16 | Código | **🟡 F2 — el nombre del artefacto se componía en DOS sitios independientes: RESUELTO con fuente única.** `validacion.py` escribía el sufijo `_composicion_d3.csv` por duplicado, en la cabecera del informe y en la escritura del CSV. **Escenario de fallo concreto**: renombrar el artefacto en un sitio dejaba el informe **versionado** apuntando a un fichero inexistente, y **nada lo detectaba** —`_comprobar_tabla()` no cubre eso y el informe no se valida—. Nuevo helper **`_ruta_composicion_d3()`** (`validacion.py:1540-1550`) consumido por `:1278` y `:1574`. **Verificado no observable**: tras re-correr, la única diferencia en los seis artefactos es la marca temporal, **con los tamaños en bytes IDÉNTICOS** (9161, 9364, 492×2, 502×2) | `055e1b4` |
| 2026-08-16 | Código | **🟡 F3 — cifra atribuida al artefacto EQUIVOCADO: corregida.** `PIPELINE.md` presentaba **883,21:1** como cifra **del informe**, pero el informe imprime **`883.2:1`** —formatea con un decimal— y el **883,21** sale del **CSV** (columna `ratio_desbalance_max_min`). Reatribuido, coherente con `GUIA_RESULTADOS.md:190`, que ya lo tenía bien. Defecto **preexistente al arreglo**, cazado por el mismo pase | `055e1b4` |
| 2026-08-16 | Código | **La ficha 🟠 de la frontera `validacion.py` → `config.py` — CERRADA: Francisco APROBÓ la extensión.** Se le preguntó con las dos alternativas sobre la mesa —aprobarla, o revertirla duplicando la lista de categorías por copia—. **Razón que pesó: duplicar el vocabulario por copia es exactamente el problema que Q2 vino a resolver**, así que revertir habría comprado pureza de acoplamiento al precio de reintroducir la avería original. ⛔ **La dependencia cubre HOY TRES cosas: rutas, procedencia y el vocabulario de categorías.** **Lo que SIGUE SIN CUBRIR, y que ningún agente debe dar por extendido citando esta aprobación: cualquier lectura de `config.py` que PRODUZCA O ALTERE UN RECUENTO.** Los recuentos salen de `value_counts()` y `len()`, y esa frontera no la ha movido nadie. Registrado en `resumen-de-decisiones.md` y `CLAUDE.md` | `055e1b4` |
| 2026-08-16 | Informe | **⛔ CONTADOR GLOBAL DE CITAS — EL PRIMER `[n]` LIBRE PASA A SER EL `[76]`. Contado contra disco, no recordado.** `Bibliografía.md` pasa a **74 filas**: `[1]`–`[8]` y `[10]`–`[75]`. **`[9]` sigue QUEMADA.** Altas: **`[74]`** Goldschmidt y Chudá, «Network intrusion datasets: A survey, limitations, and recommendations», *Computers & Security* 156:104510, 2025, DOI `10.1016/j.cose.2025.104510`; **`[75]`** Breunig, Kriegel, Ng y Sander, «LOF: Identifying Density-Based Local Outliers», *ACM SIGMOD Record* 29(2):93-104, 2000, DOI `10.1145/335191.335388`. **Donde este fichero diga `[74]` como primer libre está DESFASADO.** Estampado ya en `CLAUDE.md` y `.claude/agents/leader.md`. **CERO `[CITA: …]` vivos en la memoria** | `055e1b4` |
| 2026-08-16 | Informe | **HALLAZGO DEL PASE DE BIBLIOGRAFÍA — las cifras del 23 %/16 % eran CORRECTAS, pero la ATRIBUCIÓN no, y son poblaciones distintas.** `4.2` colgaba el dato del marco «CORE A*/A 2020-2023». **Verificado *verbatim* en el artículo**: la frase («*prone to biased evaluations and selective reporting*») vive en **§5.5.4 «Other Observations»** y se mide sobre **los 89 datasets del *survey***. El marco CORE A*/A es de **§5.4 «Dataset Popularity»**, que analiza **45 artículos de congresos** y es de donde sale otro dato («NSL-KDD was used only three times»). Marcador corregido a **`[74, §5.5.4]`** y la frase **recolgada de la población correcta**. El hallazgo previo de la Tanda 15, que ya señalaba el marco mal colgado, **era correcto** | `055e1b4` |
| 2026-08-16 | Informe | **Las DOS reasignaciones de fuente que esperaban a Francisco — APROBADAS POR ÉL y EJECUTADAS.** **(1) LOF** (`2.1.4:76`): pasa de `[12]` Hastie a **`[75]` Breunig et al. (2000)**, porque **Hastie cap. 14 no trata LOF**; el uso de `[12]` en `2.1.4` baja de **×7 a ×6**, recontado. Mismo patrón que la reasignación del Isolation Forest a `[73]`. **(2) MAE/RMSE** (`2.1.5:114`): queda como **`[5, cap. 2]`** — el marcador decía «cap. 4» y esa contraposición está en el **cap. 2**. **Recuentos corregidos en la misma pasada**: `[23]` era `×3` y son **`×5`**; añadido el uso de `4.3` a `[17]` y `[18]`. **MARCADO SIN RESOLVER, no inventado**: `[5, cap. 2]` lleva **reserva de verificación** — el capítulo se establece por la estructura del libro, pero la ficha de O'Reilly devuelve **403** a todo acceso automático, así que **la página exacta no se establece** | `055e1b4` |
| 2026-08-16 | — | **PERMISOS QUE FRANCISCO CONCEDIÓ EL 2026-08-16, y que cambian cómo se despacha a partir de ahora.** **(1) El `researcher` tiene PERMISO PERMANENTE**: se despacha cuando el trabajo lo requiera, sin pedirlo cada vez. Sigue siendo **el único que escribe `Bibliografía.md`** y **siempre en serie**. **(2) Los commits NO se preguntan**: se commitea al cerrar cada tanda y se reporta después. **Lo que NO cambia: se sigue revisando el diff antes de commitear; si aparece algo que `.gitignore` debería excluir o un fichero que el trabajo no debía tocar, se PARA y se avisa; el `push` lo sigue lanzando Francisco; y el track Código sigue sin cerrarse sin `auditor-ml`** | `055e1b4` |
| 2026-08-16 | — | **TANDA 15 — avance de T10 (capítulo 4). AVANZA, NO CIERRA: T10 SIGUE ABIERTA.** Dos `redactor-tfg` en paralelo sobre ficheros **disjuntos**, un pase de `auditor-ml` de coherencia **ENTRE** las dos notas, y dos correctores en paralelo aplicando el dictamen. Ficheros: `Obsidian_TFG_Vault/04 Implementación del sistema/4.2 Base de datos utilizada.md` y `4.3 Preprocesamiento de los datasets.md`. **Dictamen: APTO CON CAMBIOS, 6 hallazgos, ninguno 🔴; 4 aplicados y 4 NO FORZADOS, registrados como abiertos.** **Cero fuga de datos, cero `[n]` inventados o renumerados, ninguna cifra publicada movida, ningún script ejecutado.** **El auditor RECONTÓ CONTRA DISCO las cifras de ambas notas y todas cuadran.** **Censo de citas INTACTO, contado contra disco: 72 filas, primer libre el `[74]`, `[9]` quemada**; sigue vivo **1 `[CITA: …]`** (Goldschmidt y Chudá, `4.2:62`) y **es correcto**. **De los 5 bullets de T10 quedan 4 hechos y UNO vivo, el del «17», de track MIXTO** (18 ocurrencias en 12 ficheros, **dos de código**: `baseline.py:12`, `firmas.py:157`) — **dejado fuera A PROPÓSITO, no por olvido** | `ba7a529` |
| 2026-08-16 | Informe | **El «~33 %» de DoS de `4.2` — CORREGIDO, y con los DOS denominadores publicados en vez de uno.** Era el defecto que la ficha describía desde el **2026-08-12**: un porcentaje sin decir sobre qué se calcula. Queda **58,1 % sobre los ataques de D2** y **33,1 % sobre D2 completo**, con **tabla de las cuatro categorías en ambos denominadores** y su procedencia declarada (`soporte_*` de `metricas_baseline.csv`). Publicar los dos, y no elegir uno, es lo que impide que el siguiente lector repita la confusión | `ba7a529` |
| 2026-08-16 | Informe | **`4.3` entera — HECHA: nueva `4.3.7 Preprocesado sin fuga de datos`, más el peso real del one-hot y la naturaleza de la poda.** La `4.3.7` contrasta **las cuatro transformaciones contra `program.py`** —no contra lo que la memoria decía que hacía— y cita `[17]` Kapoor y Narayanan y `[18]` Arp et al. (P3/P5). En `4.3.3`, el one-hot pesa **84/122 = 68,9 %** (`service` aporta **70** por sí sola). En `4.3.5`, **58 de las 60** características eliminadas por importancia son *dummies* y `service` pasa de **70 a 15**: la selección es, en la práctica, **un mecanismo de poda del one-hot de `service`**, que es justo lo que la ficha pedía demostrar | `ba7a529` |
| 2026-08-16 | Informe | **Los 4 hallazgos APLICADOS de la auditoría de la TANDA 15, y el primero es del tipo que SOLO se ve auditando las dos notas juntas.** **(1) CONTRADICCIÓN ENTRE NOTAS sobre el 78 % de DoS en D3:** `4.2` lo ponía en duda con un `[!todo]` **mientras `4.3.6` y `4.5` lo publican como cerrado** — dos partes del mismo capítulo afirmando cosas incompatibles. Resuelto declarándolo **derivable: 45.927/58.630 = 78,3 %**. **(2)** La **sobreafirmación de prevalencia** atribuida a `[17]` en `4.3.7`, bajada al nivel prudente que ya usa `5.0`. **(3) EL CENSO DE SEDES DEL *DATA SNOOPING*: la nota lo daba con DOS LISTAS DISTINTAS cuando en disco son DIEZ** (`resumen-de-decisiones.md:1271-1282`) — el mismo defecto de barrido corto que ya apareció en la Tanda 10. **(4)** La declaración de **sede única** frente a `5.0`, corregida | `ba7a529` |
| 2026-08-16 | — | **HALLAZGO (no cierra ficha) · LOS 4 NO FORZADOS DE LA TANDA 15 QUEDAN ABIERTOS, NO RESUELTOS POR INICIATIVA DEL AGENTE.** **(1) 🟠 track CÓDIGO:** el **reparto por categoría de D3 (45.927 / 11.656 / 995 / 52) no lo emite ningún script** y su CSV fuente **no está versionado** — un titular de la memoria salido de un **recuento a mano**, el **precedente exacto del «13 de 98»**; ficha propia abierta. **(2)** `5.0 Protocolo de evaluación.md` arrastra **la misma sobreafirmación** (`:149`) y **cuatro anclajes de línea caducados** (`:144-147`), **dos verificados** —`scaler.fit` en `program.py:332`, no `:316`; `rf.fit` en `:516`, no `:500`—: es fichero de **T11** y se anota dentro de ella. **(3)** Para el `researcher`: añadir `4.3` a los usos de `[17]` y `[18]` en `Bibliografía.md:120-121`; anotado dentro de T10 junto al alta de Goldschmidt y Chudá y el `[23] ×3 → ×5`. **(4)** `4.6:13` afirma que «ningún número que llegue a la memoria procede de una ejecución manual», **lo que (1) desmiente**; va atado a (1) y **no se corrige antes que él** | `ba7a529` |
| 2026-08-16 | — | **TANDA 14 — dos fichas distintas, y solo UNA cierra.** Ficheros: `Obsidian_TFG_Vault/04 Implementación del sistema/4.2 Base de datos utilizada.md` y `4.5 Entrenamiento del modelo de detección basado en firmas.md`. **(1) CERRADA**: la ficha «`4.5:39` es INEXACTO para KNN». **(2) AVANZADA, NO CERRADA: T10 · Capítulo 4** — hechos **2 de sus 5 bullets** (las tres particiones oficiales con la vacuna sobre KDDTest-21, y la 5.ª razón de «por qué NSL-KDD» con Goldschmidt y Chudá); **T10 SIGUE ABIERTA** con el «~33 %» de DoS, la nota de procedencia del «17» y `4.3` entera. **DOS pases de `auditor-ml`: NO APTO → corregido → APTO CON CAMBIOS → aplicado.** **Cero código, cero cómputo, cero corridas, ninguna cifra publicada movida, cero `[n]` inventados.** **Censo contado contra disco: INTACTO — 72 filas, primer libre el `[74]`, `[9]` sin tocar.** Queda **1 `[CITA: …]` vivo** (Goldschmidt y Chudá 2025, `4.2:62`), y es **correcto**: esa obra no está en `Bibliografía.md` y su alta es del `researcher` | `65484bb` |
| 2026-08-16 | Informe | **La ficha «`4.5:39` es INEXACTO para KNN» — CERRADA con las cifras exactas que ella misma exigía.** En **KNN** el `f1_macro` es **idéntico** entre `4.3.4` y `4.5` (**0,945349**), y en **HistGradientBoosting** la diferencia citada era **artefacto de redondeo** (**0,969377 vs 0,969391**, **1,4e-5**) | `65484bb` |
| 2026-08-16 | Informe | **EL PRIMER PASE DE `auditor-ml` FUE NO APTO, y queda escrito por qué: `4.5` daba una causa técnica DOBLEMENTE FALSA.** Decía «variabilidad de punto flotante entre **dos ejecuciones separadas** del mismo `StratifiedKFold`». **`firmas.py:133-135` construye UN ÚNICO `StratifiedKFold(random_state=42)` reutilizado en el mismo proceso** —no hay dos ejecuciones—, y **sí había configuración distinta**: el mini-experimento usa `max_iter=100` por defecto y la ganadora es `max_iter=300`. **La nota se contradecía con su propia tabla dos líneas antes** y, peor, **sugería no-determinismo en un pipeline que el TFG vende como reproducible**. Sustituida por la causa real | `65484bb` |
| 2026-08-16 | Informe | **Los otros cuatro hallazgos de los dos pases de auditoría — APLICADOS.** **(1)** «cuatro milésimas de punto porcentual» era en realidad **1,4**: magnitud corregida a **1,4e-5**. **(2)** El marco «CORE A*/A 2020-2023» estaba **mal colgado** del 23 %/16 %: pertenece a **otro dato de la misma revisión**. **(3)** `4.2:18` afirmaba **en presente** que no quedaban `[CITA:]` **habiendo tres**. **(4) RIESGO DE `[74]` DUPLICADO EVITADO: Tavallaee YA TENÍA `[23]`** en `Bibliografía.md:126`, así que dejarlo como `[CITA:]` habría provocado un alta redundante en el siguiente pase del `researcher`. **Los dos marcadores mapeados a `[23]`** | `65484bb` |
| 2026-08-16 | — | **TANDA 13 — el pase EN SERIE de citas del `researcher`, que cubre de una vez el capítulo 2 y el 3: la última dependencia declarada del track Informe sobre `Bibliografía.md`, LEVANTADA.** **36 marcadores `[CITA: …]` convertidos a `[n]`** en `2.1.1`, `2.1.3`, `2.1.4`, `2.1.5`, `2.2.4` y `3.5` (**34 del capítulo 2 + 2 del capítulo 3**): **30 MAPEADOS** a entradas existentes (`[5]` Géron ×20, `[12]` Hastie ×7) y **6 ALTAS NUEVAS, `[68]`–`[73]`**, todas con DOI. **27 de los 36 bajan CON localizador de capítulo**, cumpliendo la decisión de Francisco del 2026-08-15. Ficheros: `Obsidian_TFG_Vault/Bibliografía.md`, las seis notas citadas y `99 Investigación/Auditoría de Bibliografía.md`. **Cero código, cero cómputo, cero corridas, ninguna cifra publicada movida.** **NO procede `auditor-ml`**: no hay cifras de resultados en juego, es un pase de referencias. **Deja CUATRO fichas nuevas abiertas, y las cuatro esperan decisión de Francisco** — ninguna la forzó el agente | `df86968` |
| 2026-08-16 | Informe | **⛔ CONTADOR GLOBAL DE CITAS — EL PRIMER `[n]` LIBRE PASA A SER EL `[74]`. Contado contra disco el 2026-08-16, no recordado.** `Bibliografía.md` pasa a **72 filas**: `[1]`–`[8]` y `[10]`–`[73]`. **`[9]` sigue QUEMADA, no libre** (retirada sin renumerar, `396e283`). **Donde este fichero diga `[68]` o «66 entradas» está DESFASADO** — el número vale solo si se cuenta (`grep -oE '^\| *\[[0-9]+\]' Bibliografía.md`), y ya ha ido mal tres veces. *(`CLAUDE.md` y `.claude/agents/leader.md` también lo dicen mal; son andamiaje y los corrige el hilo principal.)* | `df86968` |
| 2026-08-16 | Informe | **La ficha «Pase EN SERIE del `researcher`: 33 `[CITA: …]` del capítulo 2 + 3 arreglos en `Bibliografía.md`» — CERRADA, y con 36 marcadores, no 33.** **Verificado: CERO `[CITA: …]` vivos en la memoria.** Los que quedan son **prosa sobre la convención** (`4.2` ×1, `Bibliografía.md` ×7) o **informe** (`99 Investigación/Reconstrucción…` ×11): **ninguno es marcador pendiente**. De sus tres arreglos, el **1 (`[6]` Goodfellow marcada huérfana EN FALSO en `Bibliografía.md:63`, `:75` y `:199`) queda HECHO** —las tres declaraciones retiradas, **7 ocurrencias verificadas en disco**— y el **2 (`[4]` Chio, «dónde se usa» apuntando a una imagen) también**, ya reanclado a `2.1.1 Introducción al ML`. **El arreglo 3 —corrección (6) de la Tanda 5, «Dónde se usa» de `[2]` y `[3]`— NO se cierra**: verificado el 2026-08-16, ambas filas siguen diciendo solo `1.2 Preliminares`, y vive en su ficha propia | `df86968` |
| 2026-08-16 | Informe | **El DESCUADRE DE CIFRAS «36 marcadores vs 33» — CERRADO, con la unidad y el número casando.** `Bibliografía.md:46-47` pasa a decir **«36 marcadores — 33 en las notas más los 3 de `EL_FUTURO.md`»**. Era el defecto que la ficha describía exactamente: las dos cifras eran defendibles bajo criterios distintos, pero **el texto literal no era cierto bajo ninguno de los dos** | `df86968` |
| 2026-08-16 | Informe | **Hallazgo 10 de la auditoría de la TANDA 12 — «Dónde se usa» desfasada en OCHO entradas: CERRADO, y el hallazgo sobreestimaba en una.** **7 de las 8 estaban desfasadas por el capítulo 3 y quedan recontadas; `[52]` era CORRECTA.** Se resolvió **donde estaba previsto** —dentro de este pase, para tocar `Bibliografía.md` **una sola vez y no dos**—, que era la razón declarada de aplazarlo. **Lo que NO cierra**: el mismo defecto de familia en `[2]` (Anderson) y `[3]` (Denning), que tiene ficha propia desde la Tanda 5 | `df86968` |
| 2026-08-16 | Informe | **REASIGNACIÓN DE FUENTE EJECUTADA — el Isolation Forest pasa de `[54]` Molnar a `[73]` Liu, Ting y Zhou (2008), DOI `10.1109/ICDM.2008.17` verificado.** Es el aviso que la auditoría de la Tanda 11 dejó **marcado y sin tocar**: atribuía el algoritmo a un libro de **interpretabilidad** en vez de a su fuente primaria. **Se ejecuta porque venía con ENCARGO ESCRITO EN LA PROPIA NOTA**, no por criterio del agente — el contraste con la ficha abierta de LOF/Breunig, donde no había encargo y por eso **no** se sustituyó, es justamente lo que hace defendible esta decisión. **Efecto lateral: `[54]` Molnar, con la edición sin fijar, ya NO bloquea ningún localizador del capítulo 2** | `df86968` |
| 2026-08-16 | — | **TANDA 12 · LA AUDITORÍA DE COHERENCIA — EJECUTADA, y con ella se levanta lo que bloqueaba el cierre de la tanda.** Era el punto 1 de los cuatro que este fichero listaba: la Tanda 12 se commiteó **parcial** en `669fd9f` **sin auditoría**. Dictamen: **APTO CON CAMBIOS, 10 hallazgos, ninguno 🔴**. **9 de los 10 aplicados** por **cuatro `redactor-tfg` en paralelo sobre ficheros disjuntos**: `03 Diseño del sistema/3.2 Arquitectura del sistema.md`, `3.3 Metodología de funcionamiento del sistema.md`, `3.5 Modelo de detección basado en firmas.md`, `3.6 Conclusiones del capítulo.md` y `02 Marco Teórico/2.3 Inteligencia Artificial/2.3.3 Límites y consideraciones éticas.md`. **Cero código, cero cómputo, cero corridas, ninguna cifra publicada movida, cero `[n]` inventados** — **censo contado contra disco, no recordado: `Bibliografía.md` sigue en 66 entradas y el primer libre sigue siendo el `[68]`.** **El hallazgo 10 NO se aplica aquí**: es de `Bibliografía.md`, fichero del `researcher`, y queda con ficha propia abierta. **NO cierra T9**: siguen vivos los puntos 2 y 4 del traspaso —el barrido de solapes del capítulo 2 y la comprobación de qué solapes de los 15 quedan sin aplicar— | `4210379` |
| 2026-08-16 | Informe | **Los tres hallazgos de fondo de la auditoría de la TANDA 12 — CORREGIDOS, y los tres son del tipo que solo se ve auditando la tanda como unidad.** **(1)** `3.2.2` insertaba la frase «no se repite aquí» **y a continuación repetía el argumento en una tabla**: el recorte enunciaba su propia regla y la incumplía en el párrafo siguiente. Reformulado al patrón **categoría/instancia**. **(2) LA TANDA PREVIA DE DES-DUPLICACIÓN HABÍA CREADO UNA DUPLICACIÓN NUEVA:** Kim et al. y su callout de verificación, **ya desarrollados en `2.2.4`**, aparecían reescritos en `3.2`. Unificados en **una sola sede**. Queda escrito porque es el riesgo propio de un pase de recorte: se des-duplica en un sitio y se siembra en otro. **(3)** `3.5` llamaba **«apoyo duro»** a un orden (**HistGradientBoosting 0,804 vs RandomForest 0,822**) que **`A.3` declara NO establecido** —bandas solapadas y la **semilla 42 de RandomForest cae fuera de su propia banda**—. Reescrito a la forma **pareada**: **RF gana en 8 de 10 semillas**, que es lo que el barrido sostiene | `4210379` |
| 2026-08-16 | Informe | **Punto 3 del traspaso — el ancla de `2.3.3` VERIFICADA, y era CORRECTA: no había nada que repuntar.** La decisión técnica de la TANDA 10 pieza A dejó `2.3.3:91` con **wikilink a nota** en vez de ancla, a reconsiderar **después de que T9 renumerase el capítulo 3**. Comprobado: **T9 NO renumeró `3.1`** —la renumeración fue **local a `3.3`**—, así que el destino del wikilink no se movió. **Se cierra el punto declarando que la condición no se dio**, no aplicando un cambio: la reconsideración estaba pendiente, el repunte nunca fue necesario | `4210379` |
| 2026-08-15 | — | **TANDA 11 — EL CAPÍTULO 2 QUEDA CERRADO ENTERO.** **Undécimo commit por tanda** bajo la Decisión 7, salvo que aquí son **dos commits**: `d31e20f` (la redacción y la creación de la figura) y `296de24` (el embebido de la figura y la auditoría aplicada). **12 ficheros tocados**: `02 Marco Teórico/` `2.1.1`–`2.1.6`, `2.2.1`, `2.2.2`, `2.2.4`, `2.2.5`, `2.3.1` y `Apéndices/A.2`, más `Implementacion/app/figura_nids_bloques.py` (**nuevo**) y su PNG en `assets/`. **Auditoría en DOS PASES PARALELOS** —coherencia conceptual y citas/cifras—, ambos **APTO CON CAMBIOS**, aplicados por **4 redactores sobre ficheros disjuntos**. **Cero cómputo sobre el dataset, cero corridas, ninguna cifra publicada movida, cero `[n]` inventados.** Lo que cierra va desglosado en las filas de abajo. **Deja abiertas DOS fichas nuevas** (el pase en serie del `researcher` y los pies de figura de los capítulos 4-5) y **desbloquea** la del recuento de `00 Índice TFG.md` | `d31e20f` + `296de24` |
| 2026-08-15 | Informe | **T8 · «Cita en el punto de la decisión — capítulo 2» — CERRADA.** Lo único que la mantenía abierta era **`2.1.5`**, que seguía siendo un stub en `estado: borrador`. **`2.1.5 Métricas` queda COMPLETADA al nivel de `A.2` por decisión de Francisco**: **17 bloques de fórmulas LaTeX**, la **frase cortada cerrada** y aparato de citas. Con ello **FPR, F1 y macro/weighted ya están definidos**, así que **las tres remisiones colgadas de `2.3.3:31`, `2.3.3:139` y `2.1.6:132` dejan de apuntar a contenido inexistente**. Las cargas de `2.2.3`/`2.2.4` (Tanda 4), `2.3.3` y `2.1.6` (Tanda 5) ya estaban verificadas contra disco: **esta era la última pieza** | `d31e20f` |
| 2026-08-15 | Informe | **Prosa de memoria en `2.1.1`–`2.1.4` y `2.2.1` — HECHA.** Pasan de **apuntes crudos** a texto de memoria: encabezados reales y aparato de citas. **`2.1.4` gana Isolation Forest, One-Class SVM y LOF**, que son exactamente los algoritmos de la etapa 1 del sistema y no estaban descritos en el marco teórico. **Con esto el capítulo 2 no tiene ninguna nota en apuntes** | `d31e20f` |
| 2026-08-15 | Informe | **La FIGURA del diagrama de bloques del NIDS — CREADA, COPIADA Y EMBEBIDA; con ella se retira el `> [!todo]` de `2.2.2` que arrastraba desde la TANDA 4.** Es el caso que este fichero ya había acotado bien: **no era «copiar y embeber» como las de `assets/`, porque la figura NO EXISTÍA**. Se genera con `Implementacion/app/figura_nids_bloques.py` —**reproducible, no un binario caído del cielo**—, se copia a `Obsidian_TFG_Vault/assets/` **byte-idéntica** y se embebe en `2.2.2` **con pie de figura**. Numerada **Figura 2.5** bajo el criterio fijado en esta misma tanda | `d31e20f` + `296de24` |
| 2026-08-15 | Informe | **T24 y T25 — CERRADAS las dos, y con ellas `[6]` (Goodfellow) DEJA DE ESTAR HUÉRFANA.** `2.1.4.3` la ancla con **`[6, cap. 6]`**, aplicando la decisión de Francisco del **2026-08-09** (anclar en el bloque de redes neuronales de `2.1.4`, **sin** afirmar que el modelo del TFG sea profundo). **Verificado por el hilo principal contra disco: 7 ocurrencias.** Cae también el localizador de página que la decisión del 2026-08-15 exigía a los 8 libros. **LO QUE NO CIERRA, y por eso se abre ficha del `researcher`: `Bibliografía.md:75`, `:63` y `:199` SIGUEN DECLARANDO `[6]` huérfana** — el disco desmiente al registro bibliográfico, y **solo el `researcher` toca ese fichero**. *(`CLAUDE.md` ya lo corrigió el hilo principal.)* | `d31e20f` |
| 2026-08-15 | Informe | **La ficha «Las 7 correcciones de la auditoría de la TANDA 5» — CERRADA ENTERA.** La **(1)** era exactamente la decisión sobre `2.1.5`, resuelta por la vía de **redactarla** (fila de T8, arriba). La **(5)** queda resuelta: **`2.1.6` ya no adelanta el `0,822`**, así que la política de «el capítulo 2 no anticipa resultados» se aplica sin excepción. Las (2), (3), (4) y (7) estaban hechas desde la Tanda 6. **De las siete sobrevive SOLO la (6)**, que es del **`researcher`** y **vive en su ficha hermana**, no aquí | `d31e20f` + `296de24` |
| 2026-08-15 | Informe | **Los 4 🔴 de la auditoría de la TANDA 11 — ENCONTRADOS Y CORREGIDOS, más 7 🟡 y 9 localizadores de página propagados a marcadores que habían quedado desnudos.** **(1) COLISIÓN LATENTE DE FIGURAS:** `2.1.1` numeraba «Figura 1.1–1.4» **dentro del capítulo 2** y la figura nueva era «Figura 2.1» → **al volcar al `.docx` habría habido dos «Figura 2.1»**, defecto que no se ve en Markdown y sí en el entregable. **(2) `2.2.4:74` afirmaba que `2.1.5` está «hoy en estado de borrador»**, falso desde esta misma tanda: un tribunal habría leído que una sección del propio TFG está sin acabar. **(3) `2.1.5` y `A.2` se atribuían mutuamente el mismo papel**, y `2.1.5` describía `A.2` como «cuatro tablas de resultados» que **no contiene**. **(4) Dos wikilinks rotos** introducidos en la tanda, uno de ellos **inventando un segundo nombre para `4.2`** | `296de24` |
| 2026-08-15 | — | **DECISIONES TÉCNICAS DELEGADAS en la TANDA 11 — reversibles, y se registran para no rediscutirlas.** **(a) Criterio de numeración de figuras: `Figura <capítulo>.<orden>`**, aplicado ya a `2.1.1` (2.1–2.4) y `2.2.2` (2.5). **(b) Reparto de sede `2.1.5` / `A.2`: `2.1.5` DEFINE Y JUSTIFICA, `A.2` INSTANCIA CON CIFRAS** — antes cada una remitía a la otra. **(c) `[4]` (Chio) se REANCLA en `2.1.1:22` en vez de darse de baja**, porque la afirmación que sostenía sigue viva. **(d) `[CITA: Molnar, cap. 8]` NO se toca pero se MARCA**: atribuye Isolation Forest a un libro de interpretabilidad cuando **la fuente original es Liu, Ting y Zhou (2008)** — **aviso para el `researcher`**, que es quien resuelve el marcador | `296de24` |
| 2026-08-15 | — | **HALLAZGO (no cierra ficha) · LO QUE SALIÓ LIMPIO, que era el riesgo declarado de reescribir 6 notas de golpe.** Se registra porque **un invariante que aguanta solo cuenta si queda escrito que se comprobó**: «híbrido» **no se redefine** —el callout de `2.2.3` sigue siendo sede única—; «semisupervisado (one-class)» **no recupera «no supervisado» como sinónimo**, y **`2.1.2.6` no redefine sino que RECONCILIA** la clasificación de los manuales con la **Decisión 8**; **cero `[n]` inventados** y **`[9]` no reaparece**; **ninguna cifra movida** y el «51» **no vuelve**; y **el capítulo 2 no anticipa ningún resultado** | `d31e20f` + `296de24` |
| 2026-08-15 | — | **TANDA 10 — dos piezas: `3.1.5 Modelo de amenaza` (pieza A) y el ANÁLISIS DE DATOS REPETIDOS del capítulo 3 (pieza B).** **Décimo commit por tanda** bajo la Decisión 7, salvo que aquí son **dos commits**, no uno: la pieza A se commiteó sola (`55ef3c6`) porque la sesión **murió por límite de API** antes de escribir la pieza B, y la B llegó en el ciclo siguiente (`3fadf13`). Ficheros: `Obsidian_TFG_Vault/03 Diseño del sistema/3.1 Requisitos del sistema.md`, `06 Conclusiones/6.1 Conclusiones.md`, `Apéndices/A.3 Ficha del sistema.md` y `99 Investigación/Datos repetidos en el capítulo 3.md` (**nuevo**). **Cero código, cero cómputo, cero corridas, ninguna cifra publicada movida, ni un `[n]` nuevo.** Lo que cierra va desglosado en las dos filas de abajo. **Deja TRES fichas nuevas abiertas** (los hallazgos laterales) y **una ampliación de T9**, que es quien ejecuta el recorte | `55ef3c6` + `3fadf13` |
| 2026-08-15 | Informe | **`3.1.5 Modelo de amenaza` — AÑADIDA a `3.1 Requisitos del sistema`, y con ella CERRADA la ficha 🟠 «`2.3.3:91` remite el modelo de amenaza CONCRETO a `3.1`, que está VACÍA».** Fija el adversario en las **seis dimensiones** (caja negra sin observación, solo emitir tráfico, solo inferencia, estático) y sostiene **por qué NO hay experimento adversario** con **propiedades verificables del NSL-KDD** —características derivadas y agregadas, ataque en espacio de características sin correspondencia en el espacio del problema—, **no con falta de tiempo**: es un resultado, no una excusa. **DESBLOQUEA EL CIERRE DEL CAPÍTULO 2**, que remitía **dos veces** (`2.3.3:11` y `:91`) el modelo de amenaza concreto a `3.1`. **Cierra los tres `[!todo]`** que declaraban ese hueco con idéntico texto en `6.1:75`, `A.3:52` y `A.3:647`. **CORRECCIÓN AL REGISTRO, que este fichero afirmó hasta hoy: `3.1` NO estaba vacía** —tenía `3.1.1`–`3.1.4` con prosa real—, así que lo hecho es **añadir una subsección**, no redactar la nota; la ficha describía mal su propio objeto. **DECISIÓN TÉCNICA DELEGADA Y REGISTRADA: `2.3.3:91` NO se repunta al ancla `3.1.5`** — se deja el wikilink a nota, que es la convención del vault, porque **T9 va a renumerar el capítulo 3**. **Se reconsidera tras T9**, y queda anotado dentro de su ficha | `55ef3c6` |
| 2026-08-15 | Informe | **El ANÁLISIS DE DATOS REPETIDOS del capítulo 3 — ENTREGADO: `Obsidian_TFG_Vault/99 Investigación/Datos repetidos en el capítulo 3.md`, 513 líneas.** Responde a la crítica del profesor sobre recortar y unificar «los primeros apartados del Capítulo 3». **ES ANÁLISIS, NO EJECUCIÓN: el recorte lo aplica T9**, y así queda anotado en su ficha. **15 solapes verificados con línea exacta**, cada uno con **recortar / unificar / remitir**, **sede canónica** y **la frase de remisión concreta** a insertar. **El barrido inicial que este fichero traía se quedaba corto: el *data snooping* está en 10 sitios, no 6** —faltaban `2.1.6:76-90`, `4.6:28-35`, `5.4:32` y `A.3:574-586`—, más un solape cap. 2 ↔ cap. 3 (`2.2.4.5` ↔ `3.2.2`) y uno interno (`3.2.1` ↔ `3.3.3`). **Cifra para el profesor: el capítulo 3 encoge ≈20 % en total y ≈25 % en `3.1`–`3.3`.** **Sección de repetición LEGÍTIMA, validada por el auditor, que NO se toca:** `3.4.1`↔`2.3.1`, la cadena `3.1.3`→`3.5.3`→`4.5` y los cierres de capítulo — decir qué repetición se conserva es tan parte de la respuesta como decir cuál se corta. `auditor-ml`: **APTO CON CAMBIOS**, 8 puntos, **ningún 🔴, todos aplicados**; y **los tres graves eran TRAMPAS PARA T9**, por eso quedan escritos: (1) el informe declaraba `4.3.6` «único sitio con los 17 tipos» y es **falso** —`A.1:99-106` los enumera—, con una instrucción que **habría roto una remisión buena**; (2) S2 y S7 ignoraban `2.1.6:132-140`; (3) S1 creaba una **segunda redacción** del *data snooping* contra `resumen-de-decisiones.md:316-323`. **DOS HUECOS DECLARADOS DENTRO DEL INFORME, no ocultos:** el barrido del capítulo 2 solo cubre `2.1.6` y `2.2.4` (ficha propia abierta), y los porcentajes son **estimación redondeada a la decena** —no hay script de conteo—; **decisión técnica registrada: se publican redondeados, y si algún día se cuenta con script, se sustituyen** | `3fadf13` |
| 2026-08-15 | — | **TANDA 9 — el pase EN SERIE del `researcher`, `[CITA: …]` → `[n]`: la dependencia declarada que bloqueaba el resto del track Informe, LEVANTADA.** **23 marcadores MAPEADOS** a entradas existentes y **13 resueltos con 10 ALTAS NUEVAS, `[58]`–`[67]`**, todas verificadas contra **Crossref o la web del editor**. Ficheros: `Obsidian_TFG_Vault/Bibliografía.md`, `4.2`, `5.0`, `6.1`, `6.2`, `A.3`, `EL_FUTURO.md` y `99 Investigación/`. **Cero código, cero cómputo, cero corridas, ninguna cifra publicada movida.** **Noveno commit por tanda** bajo la Decisión 7. `auditor-ml`: **APTO CON CAMBIOS, sin ningún 🔴**. **Y esta vez EL DESASTRE DE LA TANDA 6 NO SE REPRODUJO, y queda escrito porque era el riesgo entero del pase: el hilo principal verificó los invariantes POR SU CUENTA CONTRA DISCO, sin fiarse del parte** — comparó las altas de `Bibliografía.md` contra **todos** los `[n]` usados en las notas y **no hay ni una nota apuntando a una entrada inexistente**; **`[9]` sigue QUEMADA**; **`2.2.1:32` ya está repuntada a `[8]`**; y los `[CITA:` que quedan en `4.2` y en `Bibliografía.md` son **prosa sobre la conversión, no marcadores pendientes**. **Deja 5 residuos fichados, ninguno bloqueante**, más la reapertura declarada de la corrección (6) de la Tanda 5 | `e286cce` |
| 2026-08-15 | Informe | **La ficha «Reconciliar el contador de citas: convertir `[CITA: …]` a `[n]` y dar de alta en `Bibliografía.md`» (🟠) — CERRADA.** Abierta en el cierre de sesión del 2026-08-13 como **deuda garantizada del paralelismo**, era la última superviviente de aquellas tres altas. **Se cierra sobre conteo contra disco, no sobre el parte del agente.** **EL CONTADOR GLOBAL QUEDA ASÍ: 66 entradas, `[1]`–`[8]` y `[10]`–`[67]`, `[9]` quemada, PRIMER LIBRE EL `[68]`** — actualizado en el bloque de PRÓXIMOS PASOS, que es el único sitio de este fichero donde se mantiene esa cifra. **El rango se cuenta, no se recuerda** (`grep -oE '^\| *\[[0-9]+\]' Bibliografía.md`): **ha ido mal dos veces el mismo 2026-08-15**, y si se queda desfasado la próxima tanda arranca en el `[58]` y **machaca en silencio las diez altas de hoy**. **NO cierra dos cosas que arrastraba:** `[6]` (Goodfellow) **sigue huérfana** —depende de T24— y la **corrección (6) de la Tanda 5** sigue viva, con su omisión verificada | `e286cce` |
| 2026-08-15 | Informe | **Los 20 marcadores `[CITA: …]` de la TANDA 7 (`5.0`=5, `6.1`=7, `6.2`=8), los 7 de `A.3`, los 3 de `EL_FUTURO.md` y los 6 de `4.2` — LAS CUATRO FICHAS, CERRADAS.** Es el **inventario entero** que este fichero había ido reuniendo a trompicones —y que hasta el 2026-08-15 estaba **incompleto**: solo registraba los 6 de `4.2`—. Se resuelven **todas en el mismo pase en serie**, que era la condición que las cuatro fichas exigían por separado. **`EL_FUTURO.md` era además dependencia de T12**, porque `6.2` se redacta desde él: queda servida. **Cero `[n]` inventados por los redactores en toda la cadena de tandas paralelas** — el protocolo de citas se cumplió de punta a punta, que era su única prueba real | `e286cce` |
| 2026-08-15 | Informe | **La columna «Localizador por uso» de `Bibliografía.md` — CREADA, aplicando la decisión de Francisco del 2026-08-15.** **5 localizadores establecidos** y **5 MARCADOS COMO NO ESTABLECIBLES en vez de inventados**, que es **exactamente la disciplina acordada** —la misma que ya rige las 47 citas reconstruidas y las fuentes sin acceso institucional—. **Marcar lo que no se puede establecer es el resultado correcto, no una carencia.** **Lo que NO cubre, y tiene ficha propia:** el localizador casi **no ha bajado al texto** (solo `6.2:306` lo lleva), y la leyenda de `:58` promete una marca que solo existe en las filas nuevas | `e286cce` |
| 2026-08-15 | Informe | **El residuo (4) de la TANDA 7 — «`Bibliografía.md:153` dice “propuesta, no ejecutada” sobre algo YA ejecutado» — CERRADO, y eran TRES callouts, no uno.** Los tres afirmaban que una acción estaba solo propuesta cuando **el disco demuestra que ya se ejecutó**. Quedó **expresamente fuera de la Tanda 8** por ser fichero del `researcher`, y aquí se salda con el resto de su carga. **La ficha madre de los seis residuos SIGUE ABIERTA** por los dos que quedan: los números de línea de T25 desplazados y `[6]` huérfana | `e286cce` |
| 2026-08-15 | Informe | **La ficha de las figuras de `assets\` — CERRADA ENTERA, sus dos mitades: «copiar» (TANDA 7) y «embeber» (TANDA 8).** **Se cierra sobre un CONTEO CONTRA DISCO, no sobre una impresión.** Corrige además lo que el propio registro dejó a medias al cerrar la Tanda 8: **están embebidas las TRES KS, no dos** — `4.2:115` (`validacion_drift_ks.png`), `4.2:119` (`validacion_drift_ks_d2_normales.png`) y `4.2:121` (`validacion_drift_ks_comparativa.png`), así que la «tercera PNG» que se sospechaba sin destino **sí lo tenía**. **Barrido completo, que es la evidencia que cierra la ficha:** `Obsidian_TFG_Vault/assets/` tiene **35 ficheros**; los `![[…]]` de las notas de la memoria (excluida `99 Investigación/`, que no es memoria) embeben **23**; las **12 restantes son EXACTAMENTE las `*_122_sin_seleccion*`**, que `4.2:120` declara **deliberadamente no publicadas** —solo se publica la variante de 54—. Es decir: **no falta ninguna figura por embeber, y las 12 que quedan fuera NO deben embeberse, por decisión ya tomada.** **Con esto se retira del todo el cuello de `assets/` que bloqueaba T10 por el lado del binario** | `8976944` |
| 2026-08-15 | — | **TANDA 8 — las 5 correcciones 🔴 de la auditoría de la TANDA 7, más los residuos que caían en los mismos ficheros.** **SEIS ficheros del vault**, en serie. Proceso: **redactor → `auditor-ml` (`NO APTO`, 1 🔴 + 3 menores) → corrector → segunda auditoría (`APTO CON CAMBIOS`, cambios ya aplicados) → repunte final**. **Cero código, cero cómputo, cero corridas; ni un `[n]` nuevo, ninguna cifra publicada movida, ningún wikilink roto.** **Octavo commit por tanda** bajo la Decisión 7. Ficheros: `06 Conclusiones/6.1 Conclusiones.md`, `06 Conclusiones/6.2 Líneas futuras.md`, `Apéndices/A.3 Ficha del sistema.md`, `04 Implementación del sistema/4.2 Base de datos utilizada.md`, `00 Índice TFG.md` y `05 Evaluación/5.1 Resultados del modelo de detección de anomalías.md`. Lo que cierra va desglosado en las filas de abajo | `8976944` |
| 2026-08-15 | Informe | **Los 5 hallazgos 🔴 de la auditoría de la TANDA 7 — CERRADOS los cinco.** **(a)** `6.2`: `[!todo]` retirado y puesta la **procedencia real del 13,4 %**. **(b)** `6.1`: la salvedad de **no-proyección a prevalencia** se declara **una sola vez**, en el límite 2 de `6.1.4.1`, como instancia del enunciado de marco de `2.3.3:53`. **(c)** `6.1`: modelo de amenaza **repuntado de `3.1` a `2.3.3 §2.3.3.3` en las tres apariciones**, con `[!todo]` por el reenvío circular. **(d)** `6.1`: la fila **P8** reescrita con los **nombres reales de columna** (`metricas_firmas.csv` no tiene columna de FPR; en `metricas_anomalias.csv` se llama `fpr`, no `bin_fpr`). **(e / T21)** `6.1:65` y `:112`: se mide coste de **inferencia**, no de despliegue, y el KS repuntado a `4.2`. **DEJA VIVO, con ficha propia: la mitad de (c) que esta tanda NO resuelve** —`2.3.3:91` sigue remitiendo el modelo de amenaza concreto a `3.1`, que está vacía— y **la ampliación de (b)**, anotada dentro de **T11** | `8976944` |
| 2026-08-15 | Informe | **Tres de los seis residuos de la TANDA 7, absorbidos por estar en los mismos ficheros — CERRADOS.** (1) `4.2:117-118`: el `[!todo]` falso de las figuras **retirado** y **las dos KS embebidas** desde `assets/`, más el callout «Fuente numérica única» **acotado**. (2) `A.3`: remisión a `5.0` corregida, y `:48` y `:634` **repuntadas a `2.3.3`**. (3) **`5.0` dada de alta en `00 Índice TFG.md`** — **`:104` intacto, deliberadamente**: el recuento tiene ficha propia. Y de propina, `5.1:61` repuntada a `4.2`, que **cierra la cadena de remisión**. **La ficha madre de los seis residuos SIGUE ABIERTA** por los tres restantes: `Bibliografía.md:153` (del `researcher`, va en su pase en serie), los números de línea de T25 desplazados y `[6]` huérfana | `8976944` |
| 2026-08-15 | — | **HALLAZGO (no cierra ficha) · El 🔴 de la primera auditoría de la TANDA 8 justificó por sí solo todo el pase: `A.3` remitía el modelo de amenaza a `3.1` —nota que no contiene «amenaza» ni «adversario»— CONTRADICIENDO lo que `6.1` declaraba verificado EN ESA MISMA TANDA.** Dos notas de la misma tanda afirmando cosas incompatibles, cada una coherente leída por separado. **Es exactamente el fallo que solo se ve auditando la COHERENCIA ENTRE FICHEROS**, y es la razón por la que el andamiaje exige auditar la tanda como unidad y no nota a nota | `8976944` |
| 2026-08-15 | — | **DECISIÓN RAZONADA de la corrección (b), escrita aquí porque ACOTA T11.** Se corrigió **la afirmación de `6.1`** y **NO** se sembraron declaraciones de la salvedad por todo el capítulo 5. Motivo: `6.1:66` es una **metaafirmación sobre el documento**; sembrar la salvedad junto a cada cifra de precisión de `5.1`/`5.2`/`5.3` sería **cambio de contenido en notas bajo T11**, sin decisión de Francisco, y **obligaría igualmente a reescribir `6.1:66`**. Si Francisco quiere además la salvedad **inline**, eso es **T11** y está anotado dentro de su ficha | `8976944` |
| 2026-08-15 | — | **ANDAMIAJE · BUG CORREGIDO en `leader.md:196`: declaraba que el primer `[n]` libre era el `[11]` cuando es el `[58]`.** Verificado **contando `Bibliografía.md`**: **56 entradas**, `[1]`–`[8]` y `[10]`–`[57]`, con **`[9]` quemada** (retirada sin renumerar, `396e283`). **No es cosmético: `leader.md` es el agente que DESPACHA**, así que un redactor que leyera esa línea asignaba números **ya usados** — el solape silencioso de `[n]` que el protocolo de citas existe justo para evitar, reintroducido por el propio andamiaje. Mismo patrón estructural que el de la prohibición de autoría derogada que seguía viva en `leader.md` (2026-08-13): **la regla vieja gana cuando vive en el fichero que reparte el trabajo.** Aplicado por el hilo principal en `CLAUDE.md`, `.claude/agents/leader.md`, `.claude/agents/researcher.md` y `.claude/agents/redactor-tfg.md` | `75f90b7` |
| 2026-08-15 | — | **ANDAMIAJE · DECISIÓN NUEVA DE FRANCISCO (2026-08-15) — el LOCALIZADOR DE PÁGINA en el marcador de cita.** Razón de la decisión, en sus términos: **él genera el formato IEEE en Zotero**; de los agentes necesita **(1) la fuente** y **(2) el párrafo marcado que apunta a ella**. La (2) ya la cumplía el `[n]`; la (1) estaba a nivel de **obra** pero **no de página**, y en un libro de 800 páginas eso no es una referencia verificable. **Lo que cambia:** el marcador admite **localizador opcional en sintaxis IEEE nativa** (`[8, p. 45]`, `[5, cap. 1]`) que **NO consume número** del contador global —es el mismo `[n]`, no uno nuevo—; es **obligatorio solo en libros y documentos largos**: `[4]` Chio, `[5]` Géron, `[6]` Goodfellow, `[7]` Murphy, `[8]` Stallings, `[12]` Hastie y `[39]` Russell y Norvig. **DISCREPANCIA ARITMÉTICA A CUADRAR AL APLICAR, sin resolverla por iniciativa de nadie: la decisión dice «son 8» y la enumeración lista SIETE.** O falta una obra en la lista o el «8» es un desliz — mismo tipo de descuadre que arrastra T14 («siete verificaciones, 3+5»), y por eso se anota en vez de escoger. `Bibliografía.md` gana columna **«Localizador por uso»**, que **escribe solo el `researcher`**; y **la página que no se pueda establecer con honestidad se MARCA, no se inventa** — misma regla que ya rige las fuentes sin acceso institucional. Aplicado por el hilo principal en `CLAUDE.md`, `.claude/agents/leader.md`, `.claude/agents/researcher.md` y `.claude/agents/redactor-tfg.md` | `75f90b7` |
| 2026-08-15 | — | **TANDA 7 — `5.0` (T5), el `6.1.4` de `6.1` (T6), `6.2` entera (T12) y la mitad «copiar» de la ficha de figuras.** **SE COMMITEA CON DICTAMEN `NO APTO` Y 5 🔴 ABIERTOS**, por el precedente que Francisco ratificó en la **Tanda 5** y porque **el trabajo llevaba TRES cortes de API sin respaldo en git**. **Los 5 son TEXTUALES: no mueven ninguna cifra publicada ni tocan código**, y quedan **fichados** en `## Abiertas` como **TANDA 8, en serie**. **Séptimo commit por tanda** bajo la Decisión 7. **INCIDENTE, otra vez el mismo patrón y por eso queda escrito: los agentes que produjeron la tanda MURIERON POR LÍMITE DE API antes de reportar, y su trabajo apareció HUÉRFANO EN DISCO** — sin reporte, sin registro y sin commit. **La auditoría original murió también y hubo que rehacerla.** Se aplicó la regla derivada de la Tanda 5: **comprobar truncamiento antes que relanzar**. Resultado: **todo íntegro, cero truncamiento, cero `[n]` nuevos inventados**. **Cero código ejecutado, cero cómputo, cero corridas.** Lo que cierra va desglosado en las cuatro filas de abajo | `e50eb8b` |
| 2026-08-15 | Informe | **T5 · `5.0 Protocolo de evaluación` — CERRADA.** `Obsidian_TFG_Vault/05 Evaluación/5.0 Protocolo de evaluación.md`, **NUEVA, 191 líneas, completa y verificada íntegra en disco**. Cubre el encargo punto por punto: particiones y su función, lo congelado entre variantes, métricas obligatorias, prohibiciones explícitas y el vocabulario de Pineau et al. **Y lo que era el corazón del encargo, HECHO: el arreglo de C3/C6 se CUENTA**, con el caso concreto de la **columna `accuracy_D2` homónima**. Contar la corrección en vez de exhibir siete verdes es lo que separa la autocrítica de la autocomplacencia, y era la razón de ser de la ficha. **Deja vivo:** **5 `[CITA: …]`** y dos de los 5 🔴. **Resuelve además una precondición ajena:** el `> [!todo]` de `A.3` que esperaba a que `5.0` existiera — pero **el `[!todo]` sigue escrito en disco** y se retira en la ficha de residuos, no aquí | `e50eb8b` |
| 2026-08-15 | Informe | **T6 · «Límites de lo medible con NSL-KDD» — CERRADA.** Nuevo apartado **`6.1.4`** dentro de `Obsidian_TFG_Vault/06 Conclusiones/6.1 Conclusiones.md`, **+77 líneas**, **en el cuerpo y no en apéndice** como exigía la ficha —los apéndices no se leen y el argumento solo funciona si se ve—. Lleva **los seis límites** con su razón técnica y **la tabla P1-P10**. **Deja vivo:** **7 `[CITA: …]`** y **cuatro de los 5 🔴**, todos dentro de esta nota. **El más grave es el (e), y es de manual: la sección que declara cubrir el pitfall P9 lo COMETE**, afirmando que «se mide el coste de despliegue» cuando `A.3:174`, `2.3.3:46` y el propio `alcance_tiempo_s` dicen que solo se mide `predict`/`score`. **Se enlaza con T21**, que es su ficha natural | `e50eb8b` |
| 2026-08-15 | Informe | **T12 · `6.2 Líneas futuras` — CERRADA.** `Obsidian_TFG_Vault/06 Conclusiones/6.2 Líneas futuras.md` pasa de **placeholder de 688 B** —una de las tres notas vacías del recuento del vault— a **documento entero: +341/-8 líneas**, redactado desde `EL_FUTURO.md`. **Queda pendiente y NO es de un agente: la revisión final de Francisco**, que la decisión marco (b) le reserva expresamente sobre `6.2`. **Deja vivo:** **8 `[CITA: …]`** —el mayor recuento de la tanda— y el 🔴 **(a)**: un `[!todo]` que afirma que **ninguna columna publica el 13,4 %** cuando está en `Resultados/metricas_hibrido_calibracion.csv:3` (`d2_pct_unknown_entre_0day_det = 0,133564`) y **ya lo publican `5.3`, `5.4:39` y `6.1:85`** | `e50eb8b` |
| 2026-08-15 | Informe | **La MITAD «COPIAR» de la ficha de las figuras de `assets\` — CERRADA (la ficha sigue abierta por su otra mitad).** Tres PNG en `Obsidian_TFG_Vault/assets/`: `validacion_drift_ks.png` **re-copiada** —la que había era de una corrida anterior y **le faltaba el prefijo «(A)» en los rótulos**— más `validacion_drift_ks_comparativa.png` y `validacion_drift_ks_d2_normales.png`, **nuevas**. **Byte-idénticas por MD5** a `Resultados/figuras/`: no es una copia «parecida», está comprobada. **Copiar solo las tres del set de 54 es DELIBERADO y correcto** — `4.2:120` declara que solo se publica esa variante—, y se deja escrito para que nadie lo lea como un olvido. **Retira el cuello que bloqueaba T10 por el lado del binario.** **NO cierra la ficha:** la mitad **«embeber»** sigue viva y con ella el `> [!todo]` de la nota. **Deja un residuo fichado:** `4.2:117-118` sigue diciendo que las figuras «aún no se han copiado» | `e50eb8b` |
| 2026-08-15 | — | **TANDA 6 — reparación de las 47 citas colgantes + auditoría y corrección del arreglo del bloqueante de D2 + T13.** **SEIS agentes**, **dos pases de auditoría**, **ningún 🔴**. Lo que cierra va desglosado en las tres filas de abajo. Ficheros tocados: `EL_FUTURO.md`, `resumen-de-decisiones.md`, `Obsidian_TFG_Vault/Bibliografía.md`, `Obsidian_TFG_Vault/99 Investigación/Reconstrucción de las 47 citas colgantes.md` (**nuevo**) y **once notas del vault** (`02 Marco Teórico/2.1 Machine Learning/2.1.6 Metodologías y buenas prácticas.md`, `03 Diseño del sistema/3.3 Metodología de funcionamiento del sistema.md`, `04 Implementación del sistema/4.3`, `4.4`, `4.5`, `4.6`, `05 Evaluación/5.1`, `5.2`, `5.4`, `06 Conclusiones/6.1 Conclusiones.md`, `Apéndices/A.3 Ficha del sistema.md`), más **`CLAUDE.md`** (andamiaje: la cita `firmas.py:91-96` pasa a `firmas.py:100-108`, **verificado en disco**, porque divergía de `A.3:126`). **Cero código ejecutado, cero cómputo, ninguna cifra publicada movida.** **Sexto commit por tanda** bajo la Decisión 7. **Deja TRES fichas nuevas abiertas** —las 5 citas no reconstruidas, los 7 `[CITA: …]` de `A.3` y los 3 de `EL_FUTURO.md`— y **una ampliación de T14** | `c634367` |
| 2026-08-15 | Informe | **LAS 47 CITAS COLGANTES, REPARADAS — la ficha 🔴 queda CERRADA.** De los `[11]`–`[57]` que el pase interrumpido dejó apuntando a nada: **42 reconstruidos, verificados con DOI/URL y dados de alta en `Bibliografía.md`**; **5 NO reconstruibles, marcados como tales** (ficha propia abierta: los resuelve Francisco por criterio, retirando la afirmación o buscando fuente alternativa). Informe de trabajo en `Obsidian_TFG_Vault/99 Investigación/Reconstrucción de las 47 citas colgantes.md`. **CORRIGE UN DATO FALSO QUE ESTA FICHA AFIRMÓ HASTA HOY:** la ficha 🔴 decía que el pase había tocado **nueve notas fuera del capítulo 2** (`3.3`, `4.4`, `4.5`, `4.6`, `5.1`, `5.2`, `5.4`, `6.1`, `A.3`) y **es FALSO** — **los 47 `[n]` están SOLO en el capítulo 2**, verificado contra disco al cerrar. Aquello mandaba a verificar nueve notas que no tenían nada que verificar. **Riesgo declarado del encargo, comprobado:** `[2]` (Anderson 1980) y `[3]` (Denning 1987) **mapeados, no duplicados**, y **`[9]` sigue quemada** (retirada sin renumerar, `396e283`) | `c634367` |
| 2026-08-15 | Informe+Código | **ARREGLO DEL BLOQUEANTE DE D2 · AUDITADO, y la auditoría encontró que el arreglo VOLVÍA A COMETER EL ERROR QUE VENÍA A CORREGIR.** El parche commiteado en `059d5f3` declaraba **menos *data snooping* del que hubo**: enumeraba las decisiones contaminadas por D2 **omitiendo la más estructural de las tres**. O sea, el mismo defecto de la afirmación original —regla enunciada más estrecha que la realidad— reaparecido dentro de su propia corrección. **Corregido en 11 ficheros del vault** más **nota fechada en `resumen-de-decisiones.md`** (solo añadido, conforme a la Decisión 3). Un **retitulado a «Validación experimental»** se propagó completo: **cero punteros colgando en todo el repo, verificado**. **Dos pases de `auditor-ml`, ambos cerrados sin ningún 🔴**, que es lo que faltaba para poder cerrar: track Código no se cierra sin auditoría. Con esto queda cubierto también el **barrido** que la ficha dejaba pendiente sobre `5.1`, `3.x` y `A.3` | `c634367` |
| 2026-08-15 | Informe | **T13 · `EL_FUTURO.md` — CERRADA: las tres entradas nuevas y la anotación, escritas.** (1) **★ Vector de error de reconstrucción por característica** como entrada extra de la etapa 2 —la única idea del lote que podría ayudar al recall 0-day **conservando reglas legibles**—; (2) **salvaguarda de TabArena** sobre sobreajuste al conjunto de validación, pegada a la línea del *ensemble* de la etapa 1; (3) **bucle de generación automática de firmas de Hwang et al. 2007** como respuesta publicada al «¿y qué hago con un `unknown`?»; y (4) la **anotación (no reapertura)** de que el *target encoding* es incompatible con la opción A —no desmiente Q1/C, es **una razón más a favor de la opción B**. **Deja dos residuos con ficha:** los **3 `[CITA: …]`** del fichero y las **cifras de Hwang et al. 2007 sin verificar**, que se suman a **T14** | `c634367` |
| 2026-08-14 | — | **TANDA 5 (CIERRE DE LA FASE 4 del plan de cierre) — CUATRO NOTAS, un fichero cada una: la prosa de las 4 notas RESTANTES del capítulo 2. Con ella el capítulo 2 queda en 8 de 8.** Ficheros (**4**): `02 Marco Teórico/2.1 Machine Learning/2.1.6 Metodologías y buenas prácticas.md`, `02 Marco Teórico/2.3 Inteligencia Artificial/2.3.1 IA, ML y Deep Learning.md`, `2.3.2 La IA en ciberseguridad.md` y `2.3.3 Límites y consideraciones éticas.md`. **Cero código, cero cómputo, cero corridas, ninguna cifra publicada movida.** **Quinto commit por tanda** bajo la Decisión 7. `auditor-ml`: **APTO CON CAMBIOS**. **SE COMMITEA CON LAS 7 CORRECCIONES ABIERTAS, por decisión de Francisco**: el trabajo estaba escrito y **sin respaldo en git tras un corte por límite de sesión**, así que se prioriza preservarlo — las 7 quedan dadas de alta en `## Abiertas`, en **dos fichas**, y **los puntos 4, 5 y 7 son CROSS-FILE y ACOPLADOS: NO se paralelizan**, exigen un redactor **en serie** con las cuatro notas en contexto. **Lo que salió LIMPIO, que era el riesgo declarado de la tanda:** «híbrido» **no se redefine** (`2.3.1:11` y `2.3.2:55` remiten al callout canónico de `2.2.3:62-63`); «semisupervisado (one-class)» sin sinónimos contradictorios en las cuatro, coherente con `resumen-de-decisiones.md:463-467`; el «51» no aparece; **cero `[n]` nuevos** —el único es `[3]` en `2.3.2:36`, correctamente **mapeado** a Denning 1987, y `[9]` no reaparece—; todas las rutas y cifras verificadas contra disco. **La Decisión 4 NO está sobreaplicada** (comprobado contra `99 Investigación/`): el defecto es **el contrario**, faltan marcadores en `2.3.3` y `2.3.1`. **CIERRA la ficha de la prosa de las 8 notas (8 de 8). NO cierra T8**: su viñeta `2.3.3` queda hecha, pero `2.1.5` sigue siendo un stub sin tocar. **PROCEDE AHORA el pase EN SERIE del `researcher`** de `[CITA: …]` → `[n]`, dependencia declarada del final de cada fase | `7241cbd` |
| 2026-08-14 | Informe | **`2.1.6 Metodologías y buenas prácticas` — PROSA REDACTADA** desde su guion, y con ella la carga T8 de esta nota: **Chow 1970** como regla de rechazo óptima **sobre las posteriores verdaderas** —y que `predict_proba` de un RF no lo es— en el callout de `:95-98`, más **Arp et al.** (`:135`) y el **vocabulario de Pineau** (`:139`). Cierra su última sección, «Relación con otras notas». **Deja DOS de las 7 correcciones abiertas dentro de la nota**: la remisión en presente de `:132` a `2.1.5` (stub) y el adelanto de cifras de `:175` | `7241cbd` |
| 2026-08-14 | Informe | **`2.3.1 IA, ML y Deep Learning` — PROSA REDACTADA** desde su guion: el encaje IA ⊃ ML ⊃ DL. **No redefine «híbrido»**: `:11` remite al callout canónico de `2.2.3:62-63`, que es justo el riesgo que la tanda tenía declarado. Cierra su última sección, §2.3.1.5. **Deja abierta su parte de la corrección 4**: le faltan marcadores de reserva de la Decisión 4 | `7241cbd` |
| 2026-08-14 | Informe | **`2.3.2 La IA en ciberseguridad` — PROSA REDACTADA** desde su guion. **`:55` remite al callout canónico de «híbrido»** en vez de redefinirlo, y **`:36` usa `[3]` MAPEADO a Denning 1987 — no es un `[n]` nuevo**, que es la trampa exacta que el protocolo de citas existe para evitar. Cierra su última sección, §2.3.2.6. **Deja abierta la corrección 6**: `Bibliografía.md:29` tiene que actualizar «Dónde se usa» por ese nuevo uso de `[3]`, y **eso es pase del `researcher`, no del redactor** | `7241cbd` |
| 2026-08-14 | Informe | **`2.3.3 Límites y consideraciones éticas` — PROSA REDACTADA, y con ella la parte de `2.3.3` de T8**: **P9 y P10** y el marco del **modelo de amenaza**. Cierra su última sección, §2.3.3.8. **Es la nota que concentra 4 de las 7 correcciones abiertas** —las remisiones en presente de `:31` y `:139`, la «proyección a prevalencia realista» de `:50` que **no existe** en código, `Resultados/` ni notas, la atribución a **Arp** de `:85` que es de la línea **Pierazzi**, y la asimetría de la Decisión 4—, y además **prohíbe anticipar números** (`:11,34,142`) mientras `2.1.6:175` los anticipa | `7241cbd` |
| 2026-08-14 | Informe | **La ficha «La prosa de las 8 notas en guion del capítulo 2 no la encarga ninguna ficha» — CERRADA, 8 de 8.** Era **el mayor bloque de trabajo pendiente del TFG** y hasta el 2026-08-13 era **invisible en este fichero**. Se cierra en dos tandas del mismo día: la **Tanda 4** con el bloque `2.2` (`2.2.2`, `2.2.3`, `2.2.4`, `2.2.5`) y la **Tanda 5** con `2.1.6`, `2.3.1`, `2.3.2` y `2.3.3`. **Lo que NO cierra, y tiene ficha propia:** el `> [!todo]` del **diagrama de bloques del NIDS** en `2.2.2` —comparte el cuello de `assets/` que ya bloquea T10, porque el `redactor-tfg` no escribe binario—, las **7 correcciones de la Tanda 5** y **T8**. Con esto **la Fase 4 del plan de cierre queda cerrada** | `7241cbd` |
| 2026-08-14 | — | **HALLAZGO (no cierra ficha) · El agente que despachaba la TANDA 5 murió por LÍMITE DE SESIÓN DE LA API después de terminar la redacción y ANTES de reportar.** Se retomó en un segundo ciclo. **Ninguna nota quedó truncada** —verificado **explícitamente** por `auditor-ml`: las cuatro cierran su última sección (`2.1.6` «Relación con otras notas», `2.3.1` §2.3.1.5, `2.3.2` §2.3.2.6, `2.3.3` §2.3.3.8)—. Un pase de verificación dedicado murió además por un **529 del servidor**, y su cometido lo cubrió el propio `auditor-ml`. **Queda escrito porque el patrón SE VA A REPETIR: un agente que muere por límite deja el trabajo HECHO EN DISCO y NINGÚN reporte**, así que lo primero al retomar es **comprobar truncamiento, no relanzar** — relanzar sobre trabajo ya hecho lo duplica o lo pisa. **Es también la razón por la que Francisco decidió commitear con las 7 correcciones abiertas**: prosa escrita y sin respaldo en git es exactamente lo que un segundo corte se lleva por delante | `7241cbd` |
| 2026-08-14 | — | **TANDA 4 (arranque de la FASE 4 del plan de cierre) — CUATRO NOTAS EN PARALELO, un redactor por fichero: la prosa del bloque `2.2` COMPLETO.** Cubre **4 de las 8** notas en guion del capítulo 2, todas en `Obsidian_TFG_Vault/02 Marco Teórico/2.2 Ciberseguridad/`; lo que cierra va desglosado en las cuatro filas de abajo, más **dos filas de HALLAZGO** que no cierran ficha. **Cero código, cero cómputo, cero corridas, ninguna cifra publicada movida.** Proceso: **4 redactores en paralelo → auditoría de COHERENCIA ENTRE NOTAS → 3 correctores en paralelo → segunda auditoría → 1 corrección residual**; **dos pases de `auditor-ml`, ambos cerrados SIN NINGÚN 🔴**. Ficheros (**4**): `2.2.2 Sistemas de detección de intrusiones.md`, `2.2.3 Taxonomía de los IDS.md`, `2.2.4 Detección por firmas frente a detección por anomalías.md` y `2.2.5 Taxonomía de ataques y panorama de amenazas.md`. **Cuarto commit por tanda** bajo la Decisión 7. **Protocolo de citas respetado: CERO `[n]` nuevos y ningún `[n]` preexistente renumerado**; todas las citas nuevas quedan como `[CITA: …]`, pendientes del pase **en serie** del `researcher` al final de la fase. **Aviso que tiene que sobrevivir a ese pase: Anderson 1980 ya es `[2]` y Denning 1987 ya es `[3]` — hay que MAPEAR, no dar de alta.** **CIERRA PARCIALMENTE, no del todo:** la ficha de la prosa de las 8 notas queda en **4 de 8** y **T8** solo en su parte de `2.2.3`/`2.2.4`. **Vivos:** las **4 notas restantes** —`2.1.6`, `2.3.1`, `2.3.2` y `2.3.3`, esta con la carga T8 de P9/P10 y el modelo de amenaza—, que van en la **Tanda 5**, y el `> [!todo]` del **diagrama de bloques del NIDS** en `2.2.2` | `06eb63e` |
| 2026-08-14 | Informe | **`2.2.2 Sistemas de detección de intrusiones` — PROSA REDACTADA** desde su guion: definición, componentes, IDS frente a IPS y ubicación en la red. **Deja vivo un `> [!todo]` DENTRO de la nota**: falta el **diagrama de bloques del NIDS**, que va a `assets/` y por tanto comparte cuello con las figuras que ya bloquean T10 — el `redactor-tfg` no escribe binario | `06eb63e` |
| 2026-08-14 | Informe | **`2.2.3 Taxonomía de los IDS` — PROSA REDACTADA, y con ella la parte de `2.2.3` de T8.** Ejes de clasificación más la carga citada: **los cuatro sentidos de «híbrido»** en la literatura NSL-KDD y cuál usa el TFG —el **(a)**, anomalías + firmas—, que **Khraisat et al. 2019 NO taxonomiza lo híbrido**, y el **linaje ADAM 2001 / Tombini 2004**. **Fija en callout `[!important]` la DEFINICIÓN CANÓNICA de «híbrido»**, que es la que referencia el resto del capítulo: cualquier nota posterior remite a ella en vez de redefinirlo | `06eb63e` |
| 2026-08-14 | Informe | **`2.2.4 Detección por firmas frente a detección por anomalías` — PROSA REDACTADA, y con ella la parte de `2.2.4` de T8.** Comparativa de los dos paradigmas y justificación de la cascada. **APLICA LA DECISIÓN 8 de la Fase 0:** término canónico **«semisupervisado (one-class)»**, **sin reintroducir «no supervisado»** como si fuera término propio — el sinónimo se declara una sola vez y es en `3.4.1`. Con esto la Decisión 8 queda consumida donde tocaba: dentro de una nota ya encargada, sin ciclo propio | `06eb63e` |
| 2026-08-14 | Informe | **`2.2.5 Taxonomía de ataques y panorama de amenazas` — PROSA REDACTADA** desde su guion: las cuatro categorías `dos`/`probe`/`r2l`/`u2r` y el panorama de amenazas. **Escrita con las 40 etiquetas correctas** (`normal` + 39 tipos de ataque): **la cifra errónea «51» NO aparece en la nota**, que es justo el número que `CLAUDE.md` dejó marcado como falso | `06eb63e` |
| 2026-08-14 | Informe | **HALLAZGO (no cierra ficha) · El marcador de cautela aplicado DE MÁS — patrón INVERSO al habitual de este proyecto.** `2.2.3` marcaba como «**sin acceso al texto completo**» a **Khraisat 2019, Sommer y Paxson 2010 y ADAM 2001**, y **el disco lo desmentía**: `Obsidian_TFG_Vault/99 Investigación/arquitecturas-hibridas-en-la-literatura.md` registra los **tres como leídos íntegros**. Marcadores **retirados**. **La reserva de la Decisión 4 queda SOLO para Tombini 2004**, que sí se conoce por resumen. Merece quedar escrito porque la regla permanente del `redactor-tfg` (marcar dentro de la nota) se puede sobreaplicar, y una salvedad falsa **degrada gratis** una fuente que sí sostiene el texto | `06eb63e` |
| 2026-08-14 | Informe | **HALLAZGO (no cierra ficha) · Dos afirmaciones falsas cazadas por la auditoría de coherencia y CORREGIDAS dentro de la tanda.** (1) Una remisión a **`firmas_reglas.txt`, fichero que NO EXISTE**: el que hay en disco es **`firmas_reglas_54.txt`**, con la variante en el nombre — una ruta sin variante es incitable. (2) Un «**tres órdenes de magnitud**» que **en disco son 883:1, es decir 2,9** — la magnitud redondeada hacia arriba sin comprobar el dato. Ambas son del tipo que **solo se ve mirando las notas juntas y contra disco**, que es exactamente para lo que existe el pase de coherencia entre notas de una tanda paralela | `06eb63e` |
| 2026-08-14 | — | **TANDA 3 (Fase 3 del plan de cierre) — DOS FICHAS EN PARALELO, un track cada una, despachadas sobre ficheros disjuntos.** Lo que cierra va desglosado en las dos filas de abajo: el **alta de `A.3` en el índice** (Informe) y el **QUINTO re-anclaje de sello** (Código). **Cero cómputo, cero corridas, ninguna cifra publicada movida, ningún hash inventado** — `1cb5c26` está verificado con git. `auditor-ml`: **APTO** tras **dos pases**, con los hallazgos aplicados. Ficheros (**4**): `Implementacion/PIPELINE.md`, `Obsidian_TFG_Vault/00 Índice TFG.md`, `Obsidian_TFG_Vault/Apéndices/A.3 Ficha del sistema.md` y `Resultados/GUIA_RESULTADOS.md`. **Tercer commit por tanda** bajo la Decisión 7. **Queda ABIERTO y a criterio de Francisco, no despachado:** el callout «Punto actual» de `00 Índice TFG.md:8` no menciona `A.3`, pero está **fechado el 2026-07-16**, así que es **historial** y la recomendación fue **no tocarlo** | `cbdd084` |
| 2026-08-14 | Informe | **`A.3 Ficha del sistema` DADA DE ALTA en `00 Índice TFG.md`**, en el listado de apéndices (`:92-93`), **con el mismo formato que `A.1` y `A.2`**. Cierra la viñeta viva de la ficha «Residuos de `A.3`» y el pase en serie sobre el índice que la Tanda 2 dejó pendiente. En la misma pasada, **corregida la afirmación FALSA de `:101-102`**, que decía que `03 Desarrollo/` «contiene solo avisos de migración»: en disco la carpeta **existe y está VACÍA**, sin un solo `.md`. **La cifra «de 43 notas» de `:104` se dejó INTACTA a propósito** —se cuadra en la Fase 4, cuando haya movido el reparto redactadas/guion—, y el auditor confirmó además que **cuadra con disco**. **Lo que NO cierra:** el **borrado físico** de `03 Desarrollo/` sigue abierto —exige un agente con shell, que el `redactor-tfg` no tiene— y la ficha de `:104` sigue abierta por decisión | `cbdd084` |
| 2026-08-14 | Código | **QUINTO RE-ANCLAJE del proyecto: `6bb224c-sucio → 1cb5c26`.** Cierra la ficha homónima. Escrito en `Implementacion/PIPELINE.md` y `Obsidian_TFG_Vault/Apéndices/A.3 Ficha del sistema.md`; **hash verificado con git**, no copiado de una ficha. **El sello impreso DENTRO del artefacto NO se toca**, misma forma que los cuatro anteriores (`fc1c6b4-sucio → 9af842c`, `00c3c3e-sucio → 54d1349`, `df30cb2-sucio → 9ad971b`, `ddade37-sucio → 9d4c26d`): lo estampa `config.commit_actual()` y no puede llevar el hash del commit que lo versiona. **HALLAZGO DE AUDITORÍA, aplicado y que merece quedar escrito: el implementador había dejado FUERA `Resultados/GUIA_RESULTADOS.md`**, que según `resumen-de-decisiones.md:686-688` **forma parte de la unidad de un re-anclaje**. Sin ese arreglo, `PIPELINE.md` habría afirmado «no queda ningún re-anclaje pendiente» **mientras el runbook de `Resultados/` seguía diciendo que ese commit no existe** — exactamente el defecto reincidente del proyecto. Completado en `GUIA_RESULTADOS.md` en los **5 puntos** que declaraban pendiente la cuarta pasada, más la **cláusula que resuelve la contradicción sobre la pasada del FPR**. **El recuento inicial del implementador también estaba mal: 6 ocurrencias, no 8, y 2 de ellas eran sellos impresos que no se tocan.** Dos pases de `auditor-ml`, **APTO** tras aplicar hallazgos | `cbdd084` |
| 2026-08-14 | — | **FASE 2 DEL PLAN DE CIERRE, CERRADA: la Tanda 2 —`A.3` más la reconciliación del trabajo que quedó colgado de la sesión anterior— despachada.** Lo que cierra va desglosado en las filas de abajo: **T7**, la reconciliación de sellos con el **cuarto re-anclaje**, el **diagnóstico de la «ejecución colgada»** y el residuo de los **recuentos 94/4**, más **una fila de HALLAZGO** que no cierra ficha. **Cero cómputo, cero corridas, ninguna cifra publicada movida** y **ningún hash inventado**. `auditor-ml`: **APTO CON CAMBIOS**, **8 hallazgos, ninguno crítico, todos corregidos**. Ficheros: `Obsidian_TFG_Vault/Apéndices/A.3 Ficha del sistema.md` (**nuevo**), `Implementacion/PIPELINE.md` y `Resultados/GUIA_RESULTADOS.md`. **El commit arrastra además tres ficheros sin commitear de sesiones anteriores**, y hay que nombrarlos en su cuerpo para que no entren de tapadillo: `Implementacion/app/agregar_semillas.py`, `Resultados/dispersion_semillas.csv` y `Resultados/dispersion_semillas.md`. **Vivos y NO despachados:** `T25`, el alta de `A.3` en `00 Índice TFG.md`, los dos `> [!todo]` internos de `A.3` y el **quinto re-anclaje** (sello `6bb224c-sucio`) | `1cb5c26` |
| 2026-08-14 | Informe | **T7 · `A.3 Ficha del sistema` — CREADA.** `Obsidian_TFG_Vault/Apéndices/A.3 Ficha del sistema.md`, *model card* completa según Mitchell et al. 2019: particiones, semilla, configuraciones ganadoras, alcance de cada métrica, infraestructura de cómputo (i7-12700H, 34 GB RAM, Windows 11 Pro 10.0.26200, Python 3.11, 21 dependencias fijadas con `scikit-learn==1.7.1`) y la **tabla de dispersión de T4** pegada desde `Resultados/dispersion_semillas.md` (**198 filas**, `sd` muestral `ddof=1`) con `alcance` y `tabla_origen` rotulados, el **alcance declarado** —dispersión de los modelos sobre splits y set de características **FIJOS**, no «del sistema»— y las **tres salvedades del «13 de 98»**. Incluye el **encargo de la Decisión 2 de la Fase 0**: las **rutas absolutas hardcodeadas** declaradas como **límite conocido de reproducibilidad**, no disfrazadas de decisión de diseño. Checklist de Pineau: los **11 ítems FT**, declarados explícitamente como subconjunto del de 17. **El sello se cita como IMPRESO y pre-commit (`6bb224c-sucio`, `A.3:609-612`)**, pendiente del quinto re-anclaje — **quinto re-anclaje HECHO el 2026-08-14 en `cbdd084`**; `A.3:609-611` ya lo refleja. **No se vuelve a encargar `A.3`**: lo que queda vivo son sus residuos, con ficha propia en `## Abiertas` | `1cb5c26` |
| 2026-08-14 | Código | **Reconciliación de sellos y CUARTO RE-ANCLAJE del proyecto (`ddade37-sucio → 9d4c26d`), escrito en `Implementacion/PIPELINE.md` y `Resultados/GUIA_RESULTADOS.md`.** Verificado **con git**, no copiado de una ficha: `9d4c26d` es el commit de cierre de ese ciclo y `ddade37` el **inmediatamente anterior** al cambio. **Los tres ficheros llevaban dos días afirmando que el re-anclaje seguía pendiente «porque el commit de cierre no existe», cuando `features.md` ya identificaba `9d4c26d` seis veces**: la divergencia iba **al contrario** de la habitual —el registro tenía el dato y la prosa lo negaba—, y por eso queda escrito. **El sello impreso DENTRO de los artefactos NO se toca**, por la razón de siempre: lo estampa `config.commit_actual()` y no puede llevar el hash del commit que lo versiona. **Deja descendencia, con ficha abierta**: la cuarta pasada del agregador imprimió `6bb224c-sucio`, que exige un **quinto** re-anclaje cuando exista el commit de este ciclo | `1cb5c26` |
| 2026-08-14 | Código | **Diagnóstico de la «ejecución colgada» que reportó Francisco: NO hubo tal.** La **cuarta pasada del agregador SÍ completó**, cabecera `2026-08-14T15:15:13`. Lo que quedó desfasado fue la **prosa** de `PIPELINE.md` y `GUIA_RESULTADOS.md`, escrita a las **15:11**, **cuatro minutos antes**, y que por eso afirmaba que la cuarta regeneración estaba «prevista» y que el `.md` «todavía no lo lleva». **Artefactos verificados íntegros en disco: 198 filas, recuento 13/98, reparto por commit de origen 94/4, cero residuos `*_semilla*`.** Queda escrito porque el patrón se va a repetir: **una prosa escrita minutos antes de que termine la ejecución se lee después como una ejecución fallida** | `1cb5c26` |
| 2026-08-14 | Código | **La salvedad de procedencia de `dispersion_semillas.md` ya imprime los recuentos 94/4** — cierra la ficha 🟡 de los residuos de la automatización del «13 de 98». El `.md` enumeraba los dos commits de origen del titular sin decir cuántas celdas aporta cada uno; ahora lo emite el agregador (`_reparto_commits_titular_md()`, cuarta pasada): de las **98 celdas casadas**, `1163c90` aporta **94** (**13 fuera de banda**) y `274923d-sucio` aporta **4** (**ninguna fuera**). Importaba porque **`A.3` pega ese `.md`** y sin los recuentos el lector no puede dimensionar la salvedad | `1cb5c26` |
| 2026-08-14 | Código | **HALLAZGO (no cierra ficha) · `ddade37-sucio` nombra DOS invocaciones distintas del agregador, no una.** La versión que quedó **versionada en `9d4c26d`** tiene cabecera **`2026-08-13T20:13:37`**, no `19:54:48`: el mismo sello `-sucio` se imprimió en dos corridas del mismo árbol sucio. **Consecuencia práctica: un sello `-sucio` NO identifica una corrida, solo un estado del código** — para identificar la corrida hace falta la **cabecera con la marca de tiempo**, y por eso la tabla de corridas del agregador de `PIPELINE.md` va por marca de tiempo y no por sello. **Tiene que quedar escrito aquí**, o el próximo que compare dos artefactos con el mismo `-sucio` los dará por idénticos | `1cb5c26` |
| 2026-08-14 | — | **FASE 1 DEL PLAN DE CIERRE, CERRADA: la Tanda 1 —barrido de correcciones de una línea— despachada en DOS CICLOS EN PARALELO, uno por track.** Las **cinco fichas** que cierra van desglosadas en las cinco filas de abajo, más **dos filas de HALLAZGO** que no cierran ficha pero no pueden perderse. **Cero cómputo, cero corridas, ninguna cifra publicada movida:** las **nueve `metricas_*.csv` verificadas intactas**, y **ningún hash inventado**. Proceso: **tres pasadas de implementación y VARIAS de `auditor-ml`** —la del cuerpo de la tanda, **APTO CON CAMBIOS** aplicados, y las de la corrección del «más del doble» que se describe abajo, una de ellas **NO APTO** antes de quedar resuelta—. **El recuento se deja así a propósito, sin número cerrado: la tanda siguió recibiendo pasadas después de escrita esta fila.** **Es el PRIMER COMMIT POR TANDA bajo la Decisión 7** de la Fase 0 — las fichas que cierra van nombradas en el cuerpo del commit. Ficheros: `Implementacion/app/program.py`, `Implementacion/app/validacion.py`, `Resultados/GUIA_RESULTADOS.md`, `resumen-de-decisiones.md`, `Obsidian_TFG_Vault/04 Implementación del sistema/4.2 Base de datos utilizada.md` y `Obsidian_TFG_Vault/Apéndices/A.2 Métricas de desempeño.md`. **Aplicada de paso la Decisión 1 del FPR en sus sitios**: el rango viejo se sustituye por la **cifra por variante — 10,2 % en 54 y 8,5 % en 122** — en los **dos comentarios de `validacion.py`**, en `GUIA_RESULTADOS.md` (**bitácora §7 actualizada**) y en **`A.2:69`**. **Imprecisión detectada en la revisión del diff y CORREGIDA DENTRO DE LA MISMA TANDA, no ficha abierta:** al sustituir el «8-10 %» quedó «**más del doble**», que **vale para 54 (10,2 / 5 = 2,04×) pero NO para 122 (8,5 / 5 = 1,7×)**. **Eran TRES sitios, no dos:** `validacion.py:551`, `GUIA_RESULTADOS.md:221` y —el que sobrevivió al primer barrido— el **docstring de `detect_data_drift_normales()`**, `Implementacion/app/validacion.py:638-639`, que es **la afirmación operativa pegada a las dos cifras que la desmienten**. **Hicieron falta DOS pasadas de corrección**, con un dictamen **NO APTO** de `auditor-ml` en medio: la primera dejó fuera el tercer sitio **y** puso una formulación que tampoco era literal —«entre 1,7 y 2 veces», cuando **0,10174 / 0,05 = 2,0348×** se sale del intervalo por arriba—. **Formulación definitiva: se abandona el rango y se cita POR VARIANTE, ≈2,0× con 54 y ≈1,7× con 122**, que es lo que la Decisión 1 exige de todas formas. **LECCIÓN DEL BARRIDO, que va a volver a pasar y por eso queda escrita: la frase estaba PARTIDA POR EL SALTO DE LÍNEA** («…sale más\\n del doble…»), así que un `grep "más del doble"` **daba limpio siendo falso**. **Se busca por el fragmento más corto que no se parta, o en multilínea** — un barrido que sale vacío sobre una expresión de varias palabras no prueba nada por sí solo | `cd407b1` |
| 2026-08-14 | Código | **El `warnings.filterwarnings('ignore')` global, RETIRADO** — la quinta y última ficha de la migración de la deuda técnica de `next-steps.md` §3.2. Retirado de **`program.py:12`** y **`validacion.py:57`**. **`validacion.py:21` NO se tocó**: es un **comentario**, y llevaba meses mal apuntado en la propia ficha. El implementador retiró además **`import warnings`** de ambos scripts, ya sin uso, y el auditor verificó que **no queda ni una llamada a `warnings.` en todo `app/`**. Con esto la sección de la migración de §3.2 **queda sin fichas abiertas** | `cd407b1` |
| 2026-08-14 | Código | **`resumen-de-decisiones.md:820-821` ya no afirma en presente que el aviso de re-anclaje se mantiene.** Era el **punto 5 de la auditoría**, el único que quedó sin aplicar en `97e679b` por falta de permiso de escritura. Resuelta con **nota fechada que supera el aviso obsoleto**, la convención que el propio fichero ya usa. **PRIMERA APLICACIÓN DEL PERMISO ACOTADO** que Francisco concedió al `ml-implementador` ese mismo día (**Decisión 3 de la Fase 0**): auditado que la edición **SOLO AÑADE**, sin tocar una línea de texto histórico — que es exactamente la garantía por la que el permiso se acotó | `cd407b1` |
| 2026-08-14 | Informe | **Las dos imprecisiones de una línea de `4.2` — corregidas.** `4.2:105`: retirada la **acotación falsa del ranking a la variante de 54**. `4.2:120`: el rango de FPR pasa a la **cifra por variante (10,2 % en 54 · 8,5 % en 122)**, aplicando la Decisión 1. **El inventario de texto congelado o histórico que arrastra el rango viejo NO se toca** —es foto de su fecha— y se conserva escrito en `## Abiertas` para que nadie lo «corrija». Va **antes de T10**, como sus fichas hermanas | `cd407b1` |
| 2026-08-14 | Informe | **El sello de `4.2:145` ya no dice «pendiente de re-anclaje»: re-anclado a `9af842c`.** Era la **cuarta copia viva** del aviso —las otras tres se re-anclaron el 2026-08-12 en un ciclo track Código que no tocaba el vault—. **Hash verificado contra `.git/logs/HEAD`, no copiado de una ficha.** **El sello impreso DENTRO del artefacto se conserva literal, `fc1c6b4-sucio`**, por la misma razón que en `97e679b`: es salida de `config.commit_actual()` y no puede llevar el hash del commit que la versiona, que tiene que existir después. Va **antes de T10** | `cd407b1` |
| 2026-08-14 | Informe | **T20 · RESUELTA — y con ella queda DESBLOQUEADA T9.** Se resuelve **reformulando la viñeta `3.5` de T9**, que es donde vivía: el par **`68,7 s / 54,8 s` queda RETIRADO** y en su lugar va la formulación **anclada en `PIPELINE.md:493-498`**, que es el bloque citable. **Dejarlo escrito, porque es la dependencia que gobierna el orden del plan: T20 antes de T9** | `cd407b1` |
| 2026-08-14 | Informe | **HALLAZGO (no cierra ficha) · `5.3` NO publica la variante de 122, y dos agentes remitían a ella como respaldo del FPR por variante.** Sale de la **auditoría cruzada entre los dos tracks** de la tanda —el fallo que solo se ve mirando las dos ramas juntas—: el único «**8,5 %**» que hay hoy en `5.3` es el de **OneClassSVM en 54**, así que un lector siguiendo esa remisión habría **confirmado la cifra con el alcance equivocado**. Corregido **citando el artefacto**, no `5.3`. **`5.3` NO se tocó a propósito: añadirle la fila de 122 es CONTENIDO DE T11**, y ahí queda la decisión | `cd407b1` |
| 2026-08-14 | Informe | **HALLAZGO (no cierra ficha) · La trampa de las TRES lecturas de `0,084852`.** El mismo valor con **tres significados distintos**: (1) `bin_fpr` del **híbrido en 122**; (2) `fpr` del **Autoencoder en 122** —**el mismo por CONSTRUCCIÓN**, porque en una cascada la etapa 2 no puede crear ni corregir falsos positivos binarios—; y (3) `fpr` de **OneClassSVM en 54**, que coincide **POR AZAR** (ambas filas tienen exactamente `tn = 8887, fp = 824`). Tras esta tanda las tres quedan con **alcance explícito en el texto**. **Tiene que quedar escrito aquí**, o el próximo que lo mire «corregirá» una por otra creyendo que arregla una errata | `cd407b1` |
| 2026-08-14 | — | **FASE 0 DEL PLAN DE CIERRE, CERRADA: las OCHO decisiones que solo podía tomar Francisco, tomadas el 2026-08-14.** Era el **cuello de botella declarado del plan**. Las ocho van desglosadas en las ocho filas de abajo, todas de esta misma fecha. **Cero cómputo, cero código, cero corridas, ninguna cifra publicada movida:** esta fila y las ocho siguientes son **registro de decisiones**, no ejecución. **Efecto sobre la Fase 0:** pasa de EN CURSO a CERRADA, y su «Tanda 0» del bloque `PRÓXIMOS PASOS` **deja de existir**. **Lo único que hereda el hilo principal**, porque es andamiaje y no lo toca ningún agente: matizar `CLAUDE.md` §Git (**precondición de la Fase 4**), el permiso acotado en `.claude/agents/ml-implementador.md` y la regla de marcado en `.claude/agents/redactor-tfg.md` | `ff54553` |
| 2026-08-14 | Código | **Decisión 1 · El eje de balanceo de `4.3.4` NO se reabre: se DECLARA NO CONSTANTE.** Cierra la ficha «La decisión de balanceo de `4.3.4` no es constante entre semillas», que estaba **PENDIENTE DE DECISIÓN DE FRANCISCO**. **NO se toca `firmas.py` y no se mueve ninguna cifra publicada.** Se **consume en `5.4`/`4.3.4` (ficha T11)**, donde queda escrito el detalle. Verificado contra `Resultados/metricas_balanceo.csv` (16 filas, sello `1163c90`, 2026-08-09) qué ganó con la semilla 42 en el eje **SMOTE vs `class_weight`** —que solo aplica a DecisionTree y RandomForest—: 54-DecisionTree `class_weight` **0,9530 ± 0,0087** vs SMOTE **0,9350 ± 0,0165**; 54-RandomForest SMOTE **0,9736 ± 0,0079** vs `class_weight` **0,9715 ± 0,0147**; 122-DecisionTree `class_weight` **0,9568 ± 0,0118** vs SMOTE **0,9513 ± 0,0184**; 122-RandomForest SMOTE **0,9795 ± 0,0099** vs `class_weight` **0,9751 ± 0,0186**. **Con n=1 el reparto YA era 2-2** (DecisionTree para `class_weight`, RandomForest para SMOTE, en las dos variantes); a n=10 es **17 de 40 (42,5 %)**. **El barrido NO descubre que la decisión estuviera mal: confirma que ese eje nunca estuvo establecido.** **Los márgenes están dentro del ruido:** RandomForest-54 decide por **0,0021**, **~7 veces menos que su propia sd** (0,0079 y 0,0147) — es un **desempate arbitrario** y así se escribe. **ACOTACIÓN OBLIGATORIA:** el «no es constante» vale **solo** para SMOTE vs `class_weight`; **el eje SMOTE vs NADA (KNN e HistGradientBoosting) SÍ está establecido** —SMOTE gana en las **4 celdas**, y en HistGradientBoosting con holgura enorme: **0,9694 vs 0,8327** (54) y **0,9724 vs 0,8044** (122)—. Sin ella se entendería que todo `4.3.4` es arbitrario, **y no lo es**. **Configuración publicada, verificada en `firmas.py:146`** (`self.balanceo_ganador` alimenta el entrenamiento final), idéntica en las dos variantes: DecisionTree → `class_weight`; RandomForest, KNN e HistGradientBoosting → **SMOTE**. **Causa mecánica del 17 de 40, a citar al lado del recuento** (`firmas.py:40`, cabecera): cambiar la semilla cambia el `StratifiedKFold`, así que el ganador de `4.3.4` y la config del grid pueden cambiar con ella | `ff54553` |
| 2026-08-14 | Código | **Decisión 2 · NO se regeneran los splits — y en consecuencia la ficha de las RUTAS ABSOLUTAS se retira de `## Abiertas` sin ejecutarse.** Razón de los splits: son del **2026-07-05** y de ellos cuelga **todo lo publicado** (9 tablas, 20 `.joblib`, 39 figuras, 2.320 filas del barrido); regenerar obliga a re-correr el pipeline entero **más las 2 h 29 min del barrido** y **no aporta ningún número nuevo**. Efecto sobre la ficha «Rutas absolutas hardcodeadas en `program.py` y `validacion.py`» (🟠), que estaba **bloqueada por esta decisión**: **NO se ejecuta**. Es **cosmética de portabilidad**, no afecta a ningún resultado, y **tocar `program.py` sin re-correrlo dejaría código modificado no ejecutado, que es peor que la deuda**. **No se descarta: se declara como LÍMITE CONOCIDO en `A.3`**, y ese encargo queda escrito **dentro de T7**, que es quien escribe `A.3` | `ff54553` |
| 2026-08-14 | — | **Decisión 3 · Permiso de escritura del `ml-implementador` en `resumen-de-decisiones.md`: ACOTADO, no general.** Solo puede **AÑADIR nota fechada**; **NUNCA reescribir texto previo**. Razón: ese fichero es **el registro de decisiones**, y un permiso libre permitiría **reescribir historial sin que nadie lo vea**. La forma de **nota fechada** es la que el proyecto ya usa (`9af842c`, `419f4c7`). El **precedente del reparto que funciona es `c5ceca5`**: el implementador **redacta y verifica**, el **hilo principal aplica con Francisco delante**. **La aplicación del permiso en `.claude/agents/ml-implementador.md` es ANDAMIAJE y la hace el hilo principal**: aquí solo se registra la decisión. Desbloquea la ficha 🟠 de `resumen-de-decisiones.md:820-821` | `ff54553` |
| 2026-08-14 | — | **Decisión 4 · Acceso institucional: NO se cierra T14 como «no disponible». Los puntos quedan MARCADOS.** Decisión literal de Francisco: **quizá pueda encontrar esa información en otras fuentes; al revisar el informe completo, al final de todo, irá revisando esos puntos y verá de dónde sacar las citas**. **T14 sigue ABIERTA y cambia de naturaleza:** de «cerrar por criterio» pasa a **inventario de puntos a revisar por Francisco en la revisión final**. **Hallazgo verificado hoy en el vault: NINGUNA nota de la memoria cita hoy ninguna de esas fuentes** — el único hit fuera de `99 Investigación/` es «UNSW-NB15» en el **guion** de `2.3.2`, y es **coincidencia de cadena**; **`Kim et al. 2014` NO está en `3.2.2`**, esa cita es **trabajo pendiente de T9**. **Por tanto el marcado no se puede hacer ahora: las notas que citarán esas fuentes no están escritas**, y se convierte en **REGLA PERMANENTE del `redactor-tfg`**: toda nota que cite una de esas fuentes **nace con un marcador VISIBLE DENTRO de la nota** (`> [!warning] Verificación pendiente — sin acceso al texto completo`), **no solo anotado en `features.md`** — marcarlo solo en el registro no sirve, porque **Francisco revisará el informe, no el registro**. **El único que merece la pena reabrir si aparece acceso es `Kim et al. 2014`**, antagonista directo de `3.2.2` (mismo dataset, cascada en orden inverso) y hoy citado **por el abstract**; los otros seis **no sostienen ninguna afirmación**. **Discrepancia aritmética anotada, NO resuelta:** T14 declara «siete verificaciones — 3 degradadas + 5 cerradas», y **3+5 son ocho**; se cuadra **al ejecutar T14** | `ff54553` |
| 2026-08-14 | — | **Decisión 5 · Los tres `grill-me` (`2.1`, revisión del profesor, `1.4`) SALEN de la Fase 0 y quedan APLAZADOS a la Fase 6.** Instrucción literal de Francisco, **más fuerte que lo propuesto**: **se hacen TODAS las tareas de volcado de información al informe y, una vez TODO esté cerrado, revisa él el informe completo**. Razón adicional: **dos de los tres se alimentan de `mis-apuntes-del-informe.md`, que es incremental y sigue creciendo**; fijar hoy su alcance es decidir sobre un fichero que va a cambiar. **La Fase 6 va detrás de absolutamente todo, con `1.4` la ÚLTIMA.** **MATIZ QUE NO SE PIERDE:** el orden entre fases da igual **para Francisco**, pero **las dependencias técnicas siguen vigentes y no son negociables** — **T7 (`A.3`) antes de la revisión del profesor** (lo que el profesor recorte del cuerpo **se MUEVE** a `A.3`), **figuras de `assets\` antes de T10** (si no, T10 vuelca `4.2` con un `[!todo]` vivo), **T20 antes de T9**, y **la conversión de `[CITA: …]` a `[n]` al final de CADA fase**, no una sola vez al final del plan | `ff54553` |
| 2026-08-14 | Informe | **Decisión 6 · El título del TFG queda APLAZADO.** Los preliminares se redactan **al final** por decisión ya registrada, y **fijar el título antes de que existan el capítulo 2 y las conclusiones es fijarlo con menos información**. **Sigue siendo decisión de Francisco: un agente propone candidatos, no lo fija.** **No se pide lista de candidatos todavía** — se pedirá en la Fase 7, dentro de la ficha de Preliminares, que sigue abierta | `ff54553` |
| 2026-08-14 | — | **Decisión 7 · Granularidad del commit bajo despacho en paralelo: UN COMMIT POR TANDA**, nombrando **en el cuerpo** las fichas que cierra. Cierra la ficha homónima, que estaba **PENDIENTE DE DECISIÓN DE FRANCISCO**. Razón: **3-4 commits sobre el MISMO estado del árbol son granularidad ficticia** — no hay estados intermedios recuperables, así que `git log` prometería **una trazabilidad que no existe**. **Queda pendiente que el hilo principal matice `CLAUDE.md` §Git**: «un commit por tarea cerrada» → «**por tarea, o por tanda paralela nombrando sus fichas**». **Eso es PRECONDICIÓN de la Fase 4**: si no se aplica, **la regla vigente y la práctica divergen en silencio**, que es el defecto reincidente de este proyecto | `ff54553` |
| 2026-08-14 | Informe | **Decisión 8 · La divergencia de `resumen-de-decisiones.md:459` NO es decisión de contenido: es una INSTRUCCIÓN al redactor de `2.2.4`.** Cierra la ficha «`resumen-de-decisiones.md:459` · la divergencia "a corregir por Francisco al redactar"». Leída la línea, **el término canónico YA estaba fijado**: **«semisupervisado (one-class)»**, con **«no supervisado» admitido como sinónimo declarado UNA SOLA VEZ, en `3.4.1`**. Y **`2.2.4` es una de las 8 notas que se redactan en la Fase 4 de todas formas**, así que **no lleva ciclo propio: se resuelve dentro de una nota ya encargada**. La instrucción queda escrita **en la ficha de las 8 notas en guion**, que es donde la ve quien redacte. **Por qué se aplazó dos veces** (2026-08-09 y 2026-08-11): **se planteaba como decisión y no lo era** | `ff54553` |
| 2026-08-13 | Código | **Tarea B APLICADA · corregido el alcance del balanceo en el bullet Q6 de `resumen-de-decisiones.md`.** Cierra la ficha 🟠 abierta el 2026-08-13 (`resumen-de-decisiones.md:120`). El texto decía «*se corre solo sobre el set 54*» y era **falso contra disco**: `firmas.py:559` llama a `_experimento_balanceo()` **sin condicional de variante**, `Resultados/metricas_balanceo.csv` trae **16 filas = 8 por variante** (`54` y `122_sin_seleccion`) y `config.ALCANCE_BALANCEO` (`config.py:463-468`) es **agnóstico a la variante**. De paso se precisó el eje, que la fórmula corta dejaba impreciso: **SMOTE vs `class_weight` solo vale para DecisionTree y RandomForest; KNN e HistGradientBoosting comparan SMOTE contra NADA**, porque sklearn no les admite `class_weight` (`firmas.py:91-96`). El «4 algoritmos» sí era correcto. **CORRIGE UNA DESCRIPCIÓN, NO REABRE Q6:** sigue vigente que el balanceo **no se cruza** con el grid ni con el eje de selección (`firmas.py:249-255`). La edición la aplicó el **hilo principal con Francisco delante** —ningún agente escribe en ese fichero—, sobre el texto que el `ml-implementador` había redactado y verificado. Cero código, cero corridas, ninguna cifra publicada movida | `c5ceca5` |
| 2026-08-13 | Código | **Refactorización integral de `features.md`, 1.349 → 1.087 líneas**, con **excepción autorizada por Francisco** al invariante «se edita quirúrgicamente, nunca se reorganiza entero». **No es precedente** y el estado previo íntegro queda recuperable en `9d4c26d`. **10 fichas palimpsesto compactadas**, **5 cabeceras vacías retiradas** y `## Cerradas` compactada **conservando fecha, track, hash y evidencia**. **Verificación mecánica contra la versión anterior, que es lo que hace citable esta fila: 39 fichas abiertas antes y después, 50 filas cerradas antes y después, 173.360 → 133.230 bytes; y de los 39 hashes citados solo desaparece `9734f4b`**, que estaba en un párrafo que describía `validacion.py` como WIP incompleto y sin re-correr —estado superado— y cuyo hash principal `d9225be` sobrevive. Trabajo sin ficha propia (carril Intervención) | `6bfc779` |
| 2026-08-13 | Código | **Retirada de `leader.md` la prohibición DEROGADA de despachar `redactor-tfg` para la teoría `2.x` y el borrador de `6.2`.** Estaba derogada desde el **2026-08-06** (decisión marco (b)) y ya retirada de `CLAUDE.md` y de `redactor-tfg.md`, **pero no de `leader.md`; y como el leader es quien despacha, ganaba la regla vieja: ésa era la razón ESTRUCTURAL de que las 8 notas del capítulo 2 llevaran semanas en guion sin que nadie tuviera permiso de escribirlas.** En el mismo commit, la **política de despacho en paralelo** (decisión de Francisco del 2026-08-13): la unidad es el **FICHERO, no el tema**; nunca en paralelo dos agentes sobre la misma nota, `Bibliografía.md`, `features.md`, la asignación de `[n]` ni el pase de `auditor-ml`; **varios `auditor-ml` sí van en paralelo**, que son de solo lectura. **Protocolo de citas:** nadie inventa un `[n]` nuevo —contador global, hoy `[4]`, `[5]`, `[7]`, `[8]` y `[10]` en uso—, se escribe `[CITA: tema]` y la conversión es un pase posterior **en serie** del `researcher`; escrito en **`CLAUDE.md`**, que es lo que se inyecta a todos los agentes, y no solo en `leader.md`. Dos ítems nuevos en `auditor-ml.md` que no existían en `.claude/`: **ningún número de la memoria sale de un cálculo a mano** y **las nueve tablas publicadas son intocables, verificado por md5 antes y después**. `grill-me/SKILL.md` reescrito. **No se tocaron las 313 entradas de `permissions.allow`**, y merece quedar escrito por qué: un `deny` sobre `git commit`/`push` **rompería el skill `cierre`**, que es la vía sancionada; la barrera real es la lista `tools:` de cada agente, y solo `ml-implementador` y `ejecutor-experimentos` tienen Bash/PowerShell. Ficheros: `.claude/agents/leader.md`, `.claude/agents/redactor-tfg.md`, `.claude/agents/auditor-ml.md`, `.claude/skills/grill-me/SKILL.md`, `CLAUDE.md` | `0fb5f2b` |
| 2026-08-13 | Código | **El titular «13 de 98» ya SALE DEL ARTEFACTO: automatizado el recuento «fuera de banda» de la semilla 42.** Cuatro columnas nuevas en `agregar_semillas.py` —`valor_semilla_42`, `dentro_banda_42`, `distancia_fuera_banda_42`, `commit_semilla_42`—, **sección propia en el `.md`** y recuento por stdout. **El número manual RESISTE: 13 de 98, con 0 celdas sin casar**, así que **queda LEVANTADA la prohibición de citarlo**. Artefacto regenerado dos veces; **las nueve `metricas_*.csv` publicadas quedan con md5 IDÉNTICO antes y después** y **cero entrenamiento**. Dictamen de `auditor-ml`: **APTO CON CAMBIOS**, los cinco hallazgos altos aplicados y reverificados. **Las tres salvedades que se van con el `.md` y que T7 tiene que pegar en `A.3` están escritas en T7.** No cierra **T4** (falta el consumo de la banda) ni la **Tarea B**. Deja dos residuos con ficha propia: los recuentos **94/4** sin imprimir y el sello **`ddade37-sucio`** pendiente de re-anclaje. Ficheros: `Implementacion/app/agregar_semillas.py`, `Implementacion/PIPELINE.md`, `Resultados/GUIA_RESULTADOS.md`, `README.md`, `Resultados/dispersion_semillas.csv` y `.md` | `9d4c26d` |
| 2026-08-13 | Código | **Re-anclado en prosa el sello `commit_agregador = df30cb2-sucio` → `9ad971b`** en `Implementacion/PIPELINE.md` y `Resultados/GUIA_RESULTADOS.md` (tabla de corridas **y** prosa). **Tercer re-anclaje del proyecto**, tras `fc1c6b4-sucio → 9af842c` (`97e679b`) y `00c3c3e-sucio → 54d1349` (`ad62665`), y **con la misma forma**: **el sello impreso DENTRO del artefacto NO se toca** —lo estampa `config.commit_actual()` y no puede llevar el hash del commit que lo versiona, que tiene que existir después—. **Cero cómputo, cero artefactos regenerados, ninguna cifra publicada movida.** Acotados dos recuentos sin moverlos: **2.320 filas** en las nueve `metricas_*_semillas.csv` y **232 = 222 + 10** en las nueve publicadas. Dictamen de `auditor-ml`: **APTO CON CAMBIOS**, aplicado en la segunda pasada. **Superado para los dos artefactos de dispersión por su regeneración posterior** (`ddade37-sucio`, ficha propia abierta) | `ea35ce3` |
| 2026-08-13 | Código | **La parte de CÓMPUTO de T4 — barrido de 10 semillas CORRIDO y agregado. NO cierra T4**, que sigue abierta por el **consumo** del resultado (`A.3`/**T7** y `5.2`/`5.4`/**T11**). Trabajo sin ficha propia (carril Intervención dentro de T4). Corrió el **2026-08-12T22:09 → 2026-08-13T00:38**, **≈2 h 29 min**: **2.320 filas**, **20/20 celdas** (10 semillas × 2 variantes, `54` y `122_sin_seleccion`), sello **`df30cb2` único y limpio**. **Aislamiento intacto**, que es lo que el andamiaje existe para garantizar: nueve tablas publicadas, 20 `.joblib` y 39 figuras **sin tocar**, cero residuos `_semilla` en `Resultados/modelos/`, los **100 logs** de `Resultados/logs_barrido/` terminan en `COMPLETADO` sin tracebacks, y la propagación de `--semilla` verificada como **real y no cosmética**. **Agregador ejecutado** → `Resultados/dispersion_semillas.csv` y `.md`, **198 filas** (98 de calidad + 100 de dispersión de máquina), `sd` muestral `ddof=1`. **Bug corregido en el agregador, reincidencia del defecto que cerró T1:** `_tabla_md` no emitía `alcance` ni `tabla_origen`, así que rotulaba **`54 \| RandomForest`** tanto para el clasificador de firmas como para la cascada invertida; corregido y agregador re-ejecutado. **Tres pasadas de auditoría, la 2.ª NO APTO; veredicto final APTO.** **Los resultados, que es para lo que existía T4, están escritos en T11 y en T4**: el hueco RF vs HGB **no sobrevive** (orden no establecido), el hueco AE vs IsolationForest **sí aguanta**, el titular de firmas es el punto más favorable de once corridas, la 42 cae fuera de banda en **13 de 98** celdas, y la decisión de balanceo de `4.3.4` **no es constante** entre semillas. **Alcance de lo medido, a escribir así y no de otra manera:** dispersión **de los modelos sobre splits y set de características FIJOS** (`program.py` no está parametrizado), **no «dispersión del sistema»**. Ficheros: `Implementacion/app/agregar_semillas.py`, `Implementacion/PIPELINE.md`, `Resultados/GUIA_RESULTADOS.md`, `README.md` y `Resultados/verificacion_semilla_joblib.txt` (modificados); `Resultados/dispersion_semillas.csv` y `.md` y los **nueve `Resultados/metricas_*_semillas.csv`** (nuevos) | `9ad971b` |
| 2026-08-12 | Código | **El `.joblib` ausente ya da mensaje accionable en vez de traceback crudo — más tres correcciones del runbook del barrido.** Trabajo sin ficha propia (carril Intervención dentro de T4); Francisco lo mandó arreglar antes de lanzar. **Cero cambios de lógica, umbrales, métricas o escritura de tablas; ningún número publicado se mueve.** `app/hibrido.py:200-219` (`_cargar_joblib`) y `app/cascada_invertida.py:198-213` (`_cargar_joblib_firma`, **simetrizado con `_leer_umbral_conf`**) envuelven el `joblib.load` y relanzan `RuntimeError ... from None` con ruta, script previo, variante con su flag y semilla; **siguen abortando con exit ≠ 0 y escritura cero**. El caso «joblib **AUSENTE**» caía por debajo de las salvaguardas auditadas, que solo cubrían «joblib de **OTRA** semilla presente». **La cita falsa que merece quedar escrita:** `cascada_invertida.py:314` citaba `hibrido.py:301` como respaldo de **P-5**, y esa línea es **la regla τ**, otra decisión; reanclada **por símbolo** (`hibrido.py::_ensamblar_prediccion`). **Tres correcciones en el runbook de `PIPELINE.md`, las tres por afirmar en absoluto algo que el código no sostiene:** **paso 0 nuevo** —árbol limpio bajo `Implementacion/` antes de lanzar, porque `config.commit_actual()` sellaría `-sucio` y las 2.320 filas nacerían con un sello no recuperable desde git—; **salvedad al «abortan»** —la tabla de los cuatro detectores es la excepción: omite el detector con aviso y deja `metricas_hibrido_0day*` en **54 filas en vez de 72**—; y el **nombre de función equivocado**: la que gobierna los nombres de artefacto es **`config.sufijo_semilla()`** (`config.py:203-213`), que **con la 42 devuelve cadena vacía** —lo que hace verdadera la garantía de T4—, no `config.sufijo_de_semilla()`, que toma argumento y devuelve `"_semilla42"` (la usa el borrado del barrido). Verificado **ejecutando** las dos funciones. **Tres pasadas de `auditor-ml`, veredicto final APTO.** Cifras medidas que sustituyen a las que arrastraba T4: **65,2 GB libres** en C: y **2.320 filas** verificadas por dos vías | `91f2ed7` |
| 2026-08-12 | Código | **Re-anclaje del sello `00c3c3e-sucio` → `54d1349` y saneamiento del texto de T4.** Trabajo sin ficha propia (carril Intervención dentro de T4). Ficheros: `Implementacion/PIPELINE.md`, `features.md`. **Cero código de modelos, cero corridas, cero cifras publicadas movidas**; la aritmética 232 filas / 9 ficheros no cambia. **El sello impreso DENTRO de `Resultados/verificacion_semilla_joblib.txt` no se editó** —es salida de `config.commit_actual()`, misma razón que en `97e679b`—, con fila nueva en la tabla de corridas; verificado que `git diff 54d1349 -- Resultados/verificacion_semilla_joblib.txt` sale **vacío** y que `54d1349` es el único commit que ha tocado el fichero. Dictamen de `auditor-ml`: **APTO CON CAMBIOS, ningún 🔴**, los siete hallazgos aplicados. **El 🟠 que merece quedar escrito: el paso 2 del runbook exigía un VACÍO IMPOSIBLE** — `Get-ChildItem -Recurse ..\Resultados -Filter *_semilla*` casa con esa traza, que está versionada y es **permanente**, así que enseñaba al operador a ignorar la única comprobación que evita que la reanudación dé una celda por hecha. Ahora la excluye explícitamente, con el motivo al lado, **verificado ejecutándolo: sale vacío**. Los otros dos 🟠: el sello `00c3c3e-sucio` **nombra DOS corridas** (la verificación `--solo-verificar` con cero `fit` y el ensayo de humo a semilla 1, que sí hizo cuatro `fit`), declarado en la tabla; y `--solo-verificar` **reescribe la traza siempre** (`barrido_semillas.py:149-150`), así que en cuanto alguien siga el runbook las citas del sello dejan de describir el disco — añadido el aviso y cómo re-anclarlas. De los cuatro 🟡: el par **0,8605 / 0,8257 son *accuracies*** y se añadieron los `f1` reales **0,8716** y **0,8341** (`Resultados/metricas_anomalias.csv`, set 54), y **las cuatro cifras de la semilla 1 quedan marcadas como NO VERIFICABLES desde git** —su CSV se borró como residuo y nunca se commiteó: cero coincidencias de `0.8632\|0.8520\|0.8226\|0.8157` en el repo—, así que valen como indicio interno, **no como evidencia citable en la memoria** | `ad62665` |
| 2026-08-12 | Código | **Remate del ensayo de humo del barrido + RUNBOOK del barrido.** Trabajo sin ficha propia (carril Intervención dentro de T4); el andamiaje que esto remata se commiteó antes en `54d1349`. **Cero código de modelos tocado, cero cifras publicadas movidas.** Ficheros: `Implementacion/PIPELINE.md` (+152), `README.md` (+4), `resumen-de-decisiones.md` (+9). **Los tres puntos que quedaban PASAN, dos con reserva:** (1) la **salvaguarda de mezcla de semillas** aborta con exit 1 y escritura cero, pero con **traceback crudo** —arreglado luego en `91f2ed7`—; (2) la **reanudación no duplica filas**, probada por vía barata (10 corridas → 9 con 1 saltada; tablas en 1 y 18 filas tras relanzar, no en 2 y 36); (3) el **agregador aborta** con exit 1, mensaje claro y sin escritura parcial, pero por la guarda de **tabla inexistente** (`agregar_semillas.py:235`), **no** por la de «1 semilla de 10», que sigue sin ejercitarse. **Residuo del ensayo creado y borrado, verificado:** cuatro ficheros, y `Resultados/` queda idéntico al estado inicial (**107 ficheros, 20 `.joblib`, 39 figuras, 9 tablas publicadas**). Merece quedar escrito porque las `metricas_*_semillas.csv` **sí se versionan**: de haberse quedado, se colaban en el commit. **El runbook era el hueco de «dejarlo listo»: no existía uno autosuficiente** — faltaban el comando completo, el recuento total esperado de cada una de las nueve tablas y la comprobación **de CIERRE** de que la semilla 42 no se movió (la única existente era *preflight*, o sea antes y no después). Sección nueva «Runbook del barrido de semillas» en `Implementacion/PIPELINE.md`: seis pasos copiables, prerrequisitos redactados **como comprobaciones y no como afirmaciones sobre el disco**, tabla de los nueve totales con su derivación declarada, y qué teclear tras un corte. Puntero desde `README.md`. Dictamen de `auditor-ml`: **APTO CON CAMBIOS**, un 🟠 y cuatro 🟡, todos aplicados. **El 🟠: el runbook decía CUATRO recuentos y el lanzador exige CINCO** (las 5 filas de la cascada invertida, `barrido_semillas.py:107-109`), contradiciendo en silencio a la ficha contigua. El quinto hallazgo fue a `resumen-de-decisiones.md` con **nota fechada, sin reescribir el texto histórico**: D5 se declaraba cerrada con solo la tasa de la cascada y el agregador agrega **también `n_condenadas`** | `419f4c7` |
| 2026-08-12 | Código | **Andamiaje COMPLETO del barrido de semillas para T4 — los OCHO hallazgos aplicados, lanzador reanudable y agregador.** Trabajo sin ficha propia (carril Intervención dentro de T4). Contenido: `SEMILLAS_BARRIDO = [1..10]` en `config.py`; el agregador nuevo `Implementacion/app/agregar_semillas.py`; el lanzador **reanudable** `Implementacion/app/barrido_semillas.py`; `Resultados/figuras/*_semilla*` excluido en el `.gitignore` raíz; la traza `Resultados/verificacion_semilla_joblib.txt` (**20/20 `.joblib` publicados con `semilla = 42`**, verificado en disco); y la tabla «qué SÍ varía dentro de cada semilla» en `PIPELINE.md`, verificada línea a línea contra el código por el auditor. **DOS pasadas de `auditor-ml`, ambas APTO CON CAMBIOS, las once aplicadas.** El hallazgo más serio merece quedar escrito porque es el tipo de fallo que este proyecto ya ha sufrido: **`config.ALCANCE_BALANCEO` llevaba el literal «semilla 42» y lo escribía en la columna `alcance`**, así que el barrido habría producido **160 filas versionadas con una afirmación FALSA dentro del propio dato**, imposible de corregir sin re-correr. En la segunda pasada: `commit` → `commit_agregador`, `decisiones_no_constantes` como columna del CSV, el modo real de la traza parametrizado y una frase sin respaldo retirada. Cifras medidas: `Resultados/modelos` **481,33 MB** y el barrido **200 modelos ≈ 4,8 GB**, con lo que el 🟠 del espacio dejó de ser blocker. **El ensayo de humo quedó a medias** (el `ejecutor-experimentos` cayó con un 529 Overloaded tras `anomalias.py --semilla 1`) y dejó en disco **11 ficheros `_semilla1`** con `commit = 00c3c3e-sucio` **sin abrir ninguna de las nueve tablas publicadas**, que es lo que el andamiaje existe para garantizar; se **borraron el mismo 2026-08-12**, con OK de Francisco y antes de este commit. **La comprobación NO queda superada por ese borrado:** el paso 2 del runbook sigue exigiendo que `Get-ChildItem -Recurse ..\Resultados -Filter *_semilla*` salga **VACÍO** antes de lanzar, **con la exclusión de `verificacion_semilla_joblib.txt`** añadida en `ad62665` —esa traza casa con el patrón, está versionada y es permanente—, porque cualquier corrida interrumpida repone residuos | `54d1349` |
| 2026-08-12 | Código | **Andamiaje de semilla para T4 — el flag `--semilla N` y las nueve tablas `*_semillas.csv`**, con cómputo CERO. Trabajo sin ficha propia (carril Intervención dentro de T4). **Vía elegida:** flag CLI que llama a `config.fijar_semilla(N)` **antes de instanciar**; los consumidores ya leían `config.RANDOM_STATE` **por atributo**, así que mutar la global propaga **sin cambiar ninguna firma**. **Tres decisiones de diseño cerradas:** (1) **una tabla `*_semillas.csv` por cada tabla existente (9), no una común** — obligado, porque `guardar_metricas()` **aborta** si el conjunto de columnas difiere entre filas del mismo CSV, y una tabla común exigía **rediseñar T1**, que estaba prohibido; (2) **con semilla 42 el sufijo es cadena vacía**, así que una corrida por defecto es idéntica a la actual, y con semilla ≠ 42 **no se abre ninguna de las nueve tablas publicadas**; (3) **se incluyó `cascada_invertida.py`** —el encargo decía cuatro scripts, **son cinco**—: sin el flag, correrla bajo otra semilla **habría escrito en su tabla publicada**. **Límite del diseño:** `program.py` **no** está parametrizado, así que las 10 semillas miden dispersión **de los modelos sobre splits y set de características FIJOS**. Ficheros: `Implementacion/app/config.py`, `evaluacion.py`, `anomalias.py`, `firmas.py`, `baseline.py`, `hibrido.py`, `cascada_invertida.py` e `Implementacion/PIPELINE.md`. Dictamen de `auditor-ml`: **APTO CON CAMBIOS, ningún 🔴** — verificó que el **peor modo de fallo** (10 corridas con semilla 42 → dispersión cero, falso tranquilizador) **no puede darse**: no hay ni un `from config import RANDOM_STATE`, los ~15 usos son por atributo dentro de funciones y `fijar_semilla()` se llama en los **cinco `__main__`**. Sin leakage nuevo, sin rediseño de T1, y `config.py` **sigue sin imports del proyecto** (de lo que depende `validacion.py`) | `e611068` |
| 2026-08-12 | Código | **`PIPELINE.md` ya no está desalineado con su propia figura** (ficha abierta el 2026-08-01, «la acepta o la retira Francisco»). El árbol de ficheros generados lista ya **`transformers.joblib`** (`:53`) y **`selected_features.txt`** (`:30`), **distingue lo que existe por duplicado —uno por variante, `_transformers.joblib` incluido— de lo que no**, y **declara su alcance** (`:71-72`). **Corrección verificada en disco que la propia ficha traía mal:** `selected_features.txt` lo escribe **`program.py:531-535`**, no `:521`, y **no lleva prefijo de variante** — es la única excepción a la regla del prefijo. **Documentación pura:** ningún script de `app/` tocado, ninguna corrida, ninguna cifra publicada movida. Sale en el **clúster de cinco fichas de `PIPELINE.md`**; dictamen común en la fila de abajo | `97e679b` |
| 2026-08-12 | Código | **Re-anclado el sello `fc1c6b4-sucio` a su commit de cierre, `9af842c`** — la ficha que **no podía cerrarse hasta que el commit existiera**, y ya existe. Re-anclado en los **tres** documentos: `Implementacion/PIPELINE.md`, `Resultados/GUIA_RESULTADOS.md` y `resumen-de-decisiones.md`. **El implementador se dejó el tercero en la primera pasada y se completó en una segunda.** **El sello impreso DENTRO de los artefactos no se tocó** —sigue diciendo `fc1c6b4-sucio`— **y se dice por qué**: es una salida generada, no un texto editable; quien la edite a mano rompe la correspondencia con lo que imprimió `config.commit_actual()`. Corregido de paso el **anclaje frágil** `..._validation_report.txt:4-5`, que pasa a citarse **por el nombre del campo**. **Re-anclaje textual: cero corridas, cero artefactos regenerados, cero cifras alteradas.** **Residuos: `resumen-de-decisiones.md:820-821`** (punto 5 de la auditoría, sin permiso de escritura en aquella pasada) **y la copia viva del vault** (`4.2:145`, track Informe) — **dos fichas nuevas en `## Abiertas`**. **Dictamen de `auditor-ml` del clúster: APTO CON CAMBIOS, todo aplicado.** Encontró un **🟠 real**: `GUIA_RESULTADOS.md` afirmaba que las líneas de procedencia «no están en los ficheros que hay en disco» cuando **sí están** desde la corrida de las 20:53, **contradiciendo a su propia §3.2** — es la **variante INVERSA del defecto reincidente del proyecto**: no afirmar en presente lo que la corrida no respalda, sino **negar en presente lo que la corrida sí respalda**. Más **tres 🟡** de texto caducado, aplicados | `97e679b` |
| 2026-08-12 | Código | **`PIPELINE.md` ya no se contradice dentro del mismo recuadro de trazabilidad.** Retirada la frase falsa «**su commit de cierre todavía no existe**» —el commit existe y es `9af842c`—, que chocaba con la mitad verdadera del mismo recuadro («están commiteados»). **Y no era una, eran tres:** se retiraron además **dos recaídas gemelas del mismo recuadro**. Verificado en disco el 2026-08-12: **cero apariciones** de «todavía no existe» en `Implementacion/PIPELINE.md`. Era **texto vigente y engañoso, no historial** —no llevaba nota fechada que lo superase—, y por eso se **corrige**, no se anota. Sale en el clúster de cinco; dictamen en la fila de arriba | `97e679b` |
| 2026-08-12 | Código | **Las tres filas de la tabla de corridas de `PIPELINE.md` quedan ancladas a su commit.** Ya no dicen «*aún en el árbol de trabajo*»: **`1163c90` → `8fdc421`** (cierre de **T18**), **`274923d-sucio` → `b1f1df2`** (cierre de **T3**) y **`fc1c6b4-sucio` → `9af842c`** (cierre del ciclo de los siete residuos). Las dos primeras eran el 🟡 «caducadas» y la tercera es el re-anclaje: **las tres en la misma pasada**, como ordenaban sus punteros cruzados. Importa porque un tercero que leyera la columna concluía que **las cifras publicadas de T18 y de T3 no se pueden recuperar de git**, cuando sí se pueden. Las filas viven hoy en **`PIPELINE.md:369-371`**. Sale en el clúster de cinco | `97e679b` |
| 2026-08-12 | Código | **Glosa del sufijo `-sucio` escrita en la primera aparición de los dos ficheros.** Una línea en `Implementacion/PIPELINE.md` (glosa **`:186-190`**, colgando de la primera aparición **`:184`**) y en `Resultados/GUIA_RESULTADOS.md` (**`:104-106`**, bajo la fila `commit`/`fecha` de **`:102`**), describiendo la convención y **remitiendo a la tabla canónica**, que queda **INTACTA y no se duplica** —hoy en `PIPELINE.md:994` (encabezado) + `:1001-1005` (los tres valores)—. El hueco era **de orden de lectura**: el `-sucio` ya estaba documentado en `config.py`, `evaluacion.py` y esa tabla, pero a **≈800 líneas** de su primera aparición, y **sin ninguna explicación** en `GUIA_RESULTADOS.md`. **Queda fuera el vault**, donde el `-sucio` sigue sin glosarse: se cubre con la ficha nueva de `4.2:145`. Sale en el clúster de cinco | `97e679b` |
| 2026-08-12 | Informe | **`4.2` · la medición (B) del KS, la frase del FPR y el callout de trazabilidad.** Despachada en la **misma pasada** que la fila de abajo, como ordenaba el puntero cruzado de ambas: **un solo fichero tocado**, `Obsidian_TFG_Vault\04 Implementación del sistema\4.2 Base de datos utilizada.md`. La medición **(B)** entra **junto a (A)**, con tabla: **37/54 · 44/122** frente a **25/54 · 31/122**, y `src_bytes` **0,346 → 0,091**, `dst_bytes` **0,317 → 0,107**. La salvedad del `delta = (A) − (B)` queda **impresa como COMPARACIÓN y no como descomposición aditiva** —el KS es un supremo de diferencia de CDF y no es aditivo sobre una mezcla—. La frase del FPR queda **reanclada a (B)**, que es la que la sostiene: (A) compara contra un D2 que es 57 % ataques y los falsos positivos los generan las filas **normales**. Y el callout de trazabilidad cita **las dos variantes** con sus fechas (**20:53:27** / **20:53:46**) y el sello **`fc1c6b4-sucio` tal cual, sin inventar hash** — su re-anclaje tiene **ficha propia abierta**. Dictamen de `auditor-ml`: **APTO CON CAMBIOS** — sin leakage, sin cifras caducadas y **sin invadir T10, que sigue intacta**. **Residuos que deja:** las figuras de `assets\` (la de (A) es de una corrida anterior y las de (B) no están copiadas, con un `> [!todo]` vivo en la nota) y dos imprecisiones 🟡 de una línea (`:120` y `:105`) — **dos fichas nuevas en `## Abiertas`**; más el «~33 %» de DoS de `:72`, **anclado dentro de T10** | `7c0659f` |
| 2026-08-12 | Informe | **El vault ya no dice «mediana» donde el artefacto dice «media».** `4.2 Base de datos utilizada.md:107` afirmaba «la **mediana** de outliers en D1 es del 4,78 %» y era el **único** sitio del vault afectado tras el cierre del rótulo del 2026-08-11 (`84e3c8f`). Rótulo corregido a **media entre características**, con **4,78 %** (54) y **2,44 %** (122), **verificados contra los dos `*_validation_report.txt`** — no copiados de la ficha. Cerrada **antes de T10**, que era la condición: si T10 hubiera volcado `4.2` tal cual, el TFG publica un estadístico que **nadie ha calculado**. Sale en la misma pasada y bajo el mismo dictamen que la fila de arriba | `7c0659f` |
| 2026-08-11 | Código | **`commit` + `fecha` en el CSV de vocabulario y en la cabecera de los dos informes de validación** — la ficha que gobierna el **ciclo agrupado de los siete residuos** de `validacion.py`. Cerrada por la **opción A que aprobó Francisco**: `validacion.py` **importa `config.py`** (`:55`) y estampa `config.commit_actual()` (`:111`) en los **cuatro artefactos**. **Cruza una frontera que se documentaba como inexistente** —`program.py` y `validacion.py` no dependían de `config.py`—: registrado en `resumen-de-decisiones.md` que la decisión **CONSUME Q2 y EXTIENDE su alcance de rutas a procedencia**, y **explícitamente NO como permiso literal**, porque Q2 hablaba de rutas y `commit_actual()` no es una ruta. **`program.py` NO pasa a depender de `config.py`**; actualizadas en consecuencia la frase de independencia de `CLAUDE.md`, la cabecera de `config.py` y `PIPELINE.md`. Sello: **`fc1c6b4-sucio`**, fecha por invocación (54 → `20:53:27` · 122 → `20:53:46`), **pendiente de re-anclaje** al commit de cierre — **ficha propia abierta**, sin ningún hash inventado. **Hechos del ciclo, comunes a las siete filas:** **dos pasadas de `auditor-ml`, ambas APTO CON CAMBIOS, ambas aplicadas** —la primera con **seis afirmaciones falsas**, documentación escrita **en presente antes** de la corrida—. **Una sola corrida y ninguna cifra publicada se mueve:** diff de `Resultados/` contra `fc1c6b4` caracterizado, **cero diferencias fuera de las cuatro clases esperadas**; intactos `Integridad: APROBADA`, D1 67.343 / D2 22.544 / D3 58.630 / 9.711 normales (43,1 %), drift (A) 37 y 44 · (B) 25 y 31, outliers 4,78 % y 2,44 % con el rótulo «media entre características», **los 17 tipos 0-day byte a byte** (total 3.750, 16,63 %) y el one-hot 77→122 con desglose `service` +44 / `flag` +1 / `protocol_type` +0. Zanjado además: las **12 figuras son byte-idénticas** a HEAD (generación determinista), los **splits NO se regeneraron** (mtime del 2026-07-05) y **ningún `metricas_*.csv`** se tocó. **Dato que merece quedar escrito:** el defecto de afirmar en presente algo que la corrida no respalda **reapareció en un sitio nuevo en cada vuelta**, y se trató bien: **nota fechada que la supera, sin reescribir el texto histórico** | `9af842c` |
| 2026-08-11 | Código | **`PIPELINE.md` y `GUIA_RESULTADOS.md` al día — y el recuadro que MENTÍA ya no miente.** Era el 🟠 del grupo: `PIPELINE.md:141-146` atribuía los informes y las 12 figuras que hay en disco a la corrida `274923d`-sucio del **2026-08-10** «todos con marca de tiempo de esa re-corrida» y remataba «**hay que creerse este recuadro**» (`:152`) — pedía crédito explícito que no merecía. Reatribuido a la corrida del **2026-08-11** y puestos al día `Implementacion/PIPELINE.md:43-45,103-108,139-153` y `Resultados/GUIA_RESULTADOS.md:16,§3.2`, que además **ya listan el artefacto nuevo** `*_vocabulario_onehot.csv`. La tabla canónica del sello `commit` vive hoy en **`PIPELINE.md:994`** (encabezado) **+ `:1001-1005`** (los tres valores), **verificado en disco el 2026-08-12**. **La referencia se ha desplazado dos veces y esta fila deja la traza**: era `:879-888`, pasó a `:952-963` al cerrar este ciclo (2026-08-11) y el clúster de cinco fichas de `PIPELINE.md` del **2026-08-12** volvió a moverla ~40 líneas hasta `:994` + `:1001-1005`. Sale en el ciclo agrupado de los siete; dictamen y verificaciones, en la fila de arriba | `9af842c` |
| 2026-08-11 | Código | **El 77 del delta 77→122 ya se publica rotulado como RECONSTRUCCIÓN.** No es el vocabulario que el pipeline usó en su día: se **recuenta** desde los CSV `_original_*`, así que sin rótulo cualquiera podía leerlo como cifra registrada por `program.py`. El token `RECONSTRUIDO` va ahora **en consola y en el informe** (`validacion.py:977` y `:1230`), en las dos variantes. Cambio de rótulo, **no de cálculo**: el 77, el 122 y el 45 siguen **recontándose, cero literales**. Sale en el ciclo agrupado de los siete | `9af842c` |
| 2026-08-11 | Código | **Los recuentos del CSV de vocabulario one-hot ya son enteros.** `38.0 / 77.0 / 122.0 / 45.0` pasan a `38 / 77 / 122 / 45` en la fila `__total__` de los dos `*_vocabulario_onehot.csv`. Son recuentos: publicarlos como flotantes invitaba a leerlos como promedios. Sale en el ciclo agrupado de los siete | `9af842c` |
| 2026-08-11 | Código | **El encabezado «Recomendaciones:» ya no se imprime vacío.** Ahora solo se escribe **si hay alguna** (`validacion.py:1102`, `:1122`), con la condición documentada en el propio código. Efecto verificado en disco: la variante de **54 pierde el encabezado** —no tenía recomendaciones que dar— y es una de las cuatro clases de diferencia esperadas del diff. Un encabezado vacío en un artefacto publicado invitaba a pensar que se había perdido algo. Sale en el ciclo agrupado de los siete | `9af842c` |
| 2026-08-11 | Código | **Las constantes importadas de `program.py` ya son copia, no alias.** `validacion.py` envuelve en `list(...)` (`:156-157`, **antes `:100-101`: no citar más esas líneas**) `COLUMNAS_CATEGORICAS` y `COLUMNAS_NO_CARACTERISTICA`, igual que hace `program.py:65` con la canónica de `program.py:36-37`. Era **inerte hoy** —todos los usos son de lectura— pero una **mutación futura habría contaminado el one-hot real sin dejar rastro**. Arreglo de una línea, **sin re-correr nada obligado**. Sale en el ciclo agrupado de los siete | `9af842c` |
| 2026-08-11 | Código | **El comentario de la cabecera de `validacion.py` ya no miente, y el orden de import queda DECLARADO como requisito.** Decía que `program.py` no tiene efectos al importarse, cuando sí los tiene (`program.py:12`, `:16-23`, `:26-27`: `warnings.filterwarnings`, reconfiguración de `stdout`, `plt.style.use('default')` y `sns.set_palette`). Reescrito (`validacion.py:13-33`) enumerando los cuatro efectos y declarando la **consecuencia load-bearing**: el `import program` (`:33`) **debe quedar por encima** del bloque `plt.style.use` / `sns.set_palette` / `plt.rcParams`; movido por debajo, el `plt.style.use('default')` de `program.py` **borraría `figure.figsize`** y las 12 figuras cambiarían de tamaño **en silencio**. Documentado además que `import config` (`:55`), a diferencia de aquél, **no tiene efectos al importarse** —`ensure_dirs()` y `setup_utf8()` existen pero no se llaman a nivel de módulo—, así que su posición **no** es load-bearing. Sale en el ciclo agrupado de los siete | `9af842c` |
| 2026-08-11 | Código | **El 4,78 % / 2,44 % de outliers de D1 ya se publica como MEDIA, no como «mediana».** Se cambió el **nombre, no el cálculo**: `.mean()` sigue donde estaba (`validacion.py:978`, era `:968`) y **las cifras 4,78 % y 2,44 % siguen siendo válidas**. El rótulo del informe pasa a **«Outliers D1 (media entre características)»**, y corregidos `Resultados/GUIA_RESULTADOS.md` (`:117`, `:276-281`, `:379-381`, `:394`) e `Implementacion/PIPELINE.md:54-55`. **La verificación que importaba:** el auditor comprobó que **no se corrigió ninguna mediana legítima** por error — `cascada_invertida.py:296`, `PIPELINE.md:832,864-865,746` y `conf_mediana_argmax` **siguen intactas**. Re-corrido en las dos variantes (19:51-19:52): `git diff 6ae4554 -- Resultados/` da **una única línea cambiada por informe**, la del rótulo, y los dos `*_vocabulario_onehot.csv` **byte-idénticos**; todo lo demás igual —17 tipos 0-day, 3.750 (16,63 %), delta 77→122, KS (A: 37/54 y 44/122 · B: 25/54 y 31/122), conteos, `Integridad: APROBADA`—. Dictamen de `auditor-ml`: **APTO CON CAMBIOS**, ningún hallazgo 🔴, **ninguna cifra publicada cambia**. **Residuo que dejó:** el vault (`4.2:107`) seguía diciendo «mediana» — **cerrado en `7c0659f`** | `84e3c8f` |
| 2026-08-11 | Código | **`COLUMNAS_CATEGORICAS` y `COLUMNAS_NO_CARACTERISTICA` dejan de estar duplicadas por copia.** **Ejecutada, no aceptada como deuda** — decisión explícita de Francisco sobre la ficha que quedó pendiente de su criterio. Son ahora **constantes de módulo** en `program.py:36-37`, y `validacion.py` las **importa** (hoy en `validacion.py:156-157`, tras el arreglo del alias). **Camino elegido: `import program`** —fuente canónica, que es quien hace el one-hot— en vez de subirlas a `config.py`, que **sí habría violado** la restricción de `CLAUDE.md`: `program.py` y `validacion.py` no dependen de `config.py`. **La verificación que importaba:** el **orden** de la lista **no puede alterar ningún artefacto**, porque `program.py:310-311` fija `train_cols = sorted(set(D1) | set(D3))` y `:316` reindexa las tres matrices con esa lista — el orden final es **alfabético e independiente del one-hot**. Solo importa la **pertenencia**, corroborada por los CSV (38 numéricas + 39/84 dummies = 77/122) y por el contraste independiente del `.joblib`. **Sin import circular**, `argparse` bajo `__main__`, **cero `fit`**, y **los splits en disco NO se regeneraron porque no hacía falta**. Re-corrido con la ficha del rótulo (19:51-19:52), mismo diff de una línea por informe. Dictamen de `auditor-ml`: **APTO CON CAMBIOS**, ningún hallazgo 🔴. **Residuos que dejó, los dos ya cerrados:** el alias (compartía objeto lista) y el comentario falso del orden de import | `84e3c8f` |
| 2026-08-11 | Código | **`validacion.py:282` · La lista nominal de los 17 tipos 0-day ya se persiste en el informe.** Cerrada completando el WIP de `d9225be` **sin reescribir sus ~231 líneas**: el cambio queda confinado a `_save_report()` (`:1080-1142`). `_save_report()` ya escribe la lista nominal completa —**tipo, categoría, instancias, total y % de D2**— con **tres ramas de degradación**, así que los 0-day dejan de quedarse solo en consola, que era la deuda. **El 17 sigue siendo emergente, no una lista a mano** (`:340`), y el auditor verificó que **los 17 tipos coinciden uno a uno con `metricas_hibrido_0day.csv`**. Re-corrida en las **dos variantes**: `EXITCODE=0`, `Integridad: APROBADA`, **16 artefactos regenerados** en `Resultados/` (2026-08-11 19:28), **ningún `metricas_*.csv` y ningún `.joblib` tocados**. Con esto **queda desbloqueada la ficha del `4.2`**, que cita el informe que esta re-corrida regenera. Dictamen de `auditor-ml`: **APTO CON CAMBIOS** — los cambios salen como residuos, ninguno 🔴. Commit previo del WIP: `d9225be` | `6ae4554` |
| 2026-08-11 | Código | **`validacion.py:283` · El delta 77→122 del fix one-hot ya vive en un artefacto regenerable.** El parámetro `onehot` de `:991` **deja de ser *dead parameter***: ahora se lee y se escribe el delta **con desglose por columna categórica**, y nace el artefacto **`Resultados/specialized_nsl_kdd_vocabulario_onehot.csv`** (más su gemelo `_sin_seleccion_`), vía el helper nuevo y contiguo `_guardar_csv_vocabulario_onehot()` (`:1144-1201`). Las **~148 líneas** de `medir_vocabulario_onehot()` **no se reescribieron**. **Resultado que hay que leer bien: el delta sale 77→122 en las DOS variantes**, no 77→54 en la de 54 — **correcto por construcción y verificado en código**: el one-hot ocurre en `program.py:283`, `select_features()` se invoca **después** (`:1148-1150`) y los CSV `_original_*` se escriben **pre-one-hot** (`:650-652`). Queda **declarado en los dos informes**. **Cero literales**: el 17, el 77, el 122 y el 45 se **recuentan** (verificado por el auditor). Dictamen de `auditor-ml`: **APTO CON CAMBIOS**. Commit previo del WIP: `d9225be` | `6ae4554` |
| 2026-08-11 | Código | **`validacion.py:284` · Comparación de columnas D2/D3 por orden, re-corrida — y la incógnita se resuelve EN NEGATIVO.** Era la mitad que faltaba: el fix estaba en `d9225be` pero **nadie lo había corrido**, así que no se sabía si destapaba un desajuste real. **Ya se sabe: NO destapó ningún desajuste D2/D3.** Los CSV que deja `program.py` **ya estaban alineados posicionalmente en ambas variantes**; la comparación por conjunto **no ocultaba nada**. Es un **resultado, no un no-hallazgo**: la rama de diagnóstico «mismo conjunto, distinto orden» queda como red de seguridad, no como parche de un bug vivo. Verificado además por el auditor en la misma pasada: **cero `fit`**, salvedad del KS **impresa en ambos informes**, KS **coincidente con lo publicado** —(A) **37/54** y **44/122** · (B) **25/54** y **31/122**— y **alcance respetado**. Dictamen de `auditor-ml`: **APTO CON CAMBIOS**. Commit previo del WIP: `d9225be` | `6ae4554` |
| 2026-08-10 | Código | **T3 · Medición de la cascada invertida.** Script nuevo `Implementacion/app/cascada_invertida.py` (clase `NSLKDDInvertedCascadeMeasurer`): medición **contrafactual y fuera del sistema** que pasa las **9.711 filas normales de D2** por el clasificador de firmas **ya persistido** (`firma_RandomForest_<set>.joblib`) y cuenta cuántas condenaría con confianza ≥ `UMBRAL_CONF`. **Cero `fit`**, solo inferencia; y el umbral se lee de `hibrido_<set>.joblib::umbral_conf_elegido`, **nunca como literal** — si falta el descriptor, **aborta**. Resultados: variante **54 → 6.558 condenadas (67,53 %)**; variante **122 → 3.329 (34,28 %)**. Salida en `Resultados/metricas_cascada_invertida.csv` (**10 filas**, tabla propia: no toca ninguna de las cuatro principales) y dos figuras. **Matiz conceptual que impuso la auditoría y que manda al citar:** la fila `__global__` es una **cota inferior de falsos positivos irrecuperables**, **no** «el FPR de un sistema de firmas-primero» — en el sistema publicado `unknown` es alarma (decisión **P-5**, respaldada por símbolo: `hibrido.py::_ensamblar_prediccion`), así que lo que cae bajo umbral **no queda exonerado**. La lectura y los números viven en `Implementacion/PIPELINE.md`, sección «La cascada invertida (T3)». **No cierra `T9`**: solo la alimenta (viñeta `3.2.2`), y allí queda anotada la cifra con su salvedad. Dictamen de `auditor-ml`: **APTO** | `b1f1df2` |
| 2026-08-10 | Código | **T2 · KS de D1 contra los normales de D2.** Añadido en `Implementacion/app/validacion.py` **sin sustituir** el KS existente: ahora son **dos mediciones separadas y no intercambiables** — **(A)** D1 vs D2 completo: **37/54** y **44/122** características con drift; **(B)** D1 vs las **9.711 normales de D2**: **25/54** y **31/122**. `src_bytes` cae de **0,346 a 0,091** y `dst_bytes` de **0,317 a 0,107**. El `delta = (A) − (B)` se publica como **comparación, nunca como descomposición aditiva** —el KS es un supremo de diferencia de CDF y no es aditivo sobre una mezcla—, y la salvedad quedó **impresa en los dos informes de validación**. **Efecto colateral no previsto:** `validacion.py` **nunca se había corrido en la variante 122**; ahora sí, con informe nuevo (`Resultados/specialized_nsl_kdd_sin_seleccion_validation_report.txt`) y **6 figuras nuevas**. De paso aparecieron **dos cifras inventadas preexistentes** en `Resultados/GUIA_RESULTADOS.md` («34 features», «85 % de drift»), **con destino explícito a §4.2.1 y §5.1**: corregidas a **37** y **68,5 %** contra el artefacto real. Invariantes verificadas **cuatro veces** por `auditor-ml`: cero `fit`, cero recalibración, **D2 solo se reporta** (H-4/P-4 intactas); los **8 `metricas_*.csv` previos sin reescribir** (222 filas, `semilla = 42`, `commit = 1163c90`), y `CLAVE_UNICIDAD`, `_limpiar_variante_csv`, `comprobar_recuento()` y `COLUMNAS_MINIMAS` **sin tocar** — no hubo que re-correr el runbook. **No cierra `T11`**: solo la alimenta (`5.1`/`5.4`), donde quedan anotadas las cifras y la salvedad del `delta`. Dictamen de `auditor-ml`: **APTO** | `b1f1df2` |
| 2026-08-09 | — | **T0 · Retirada de la regla «lo escribe Francisco».** Aplicadas las dos velocidades de la decisión marco (b) del lote 2026-08-06, en **15 ficheros (+96 −92)**: `CLAUDE.md`, `features.md`, `.claude/agents/redactor-tfg.md`, el callout de las **8 notas** del capítulo 2, `resumen-de-decisiones.md:560`, el MOC `00 Índice TFG.md` (5 sitios) y la nota `2.2.1:52`. La ficha **subestimaba el alcance**, así que hubo que barrer **por contenido y no por la lista**: varias ubicaciones no llevaban el callout literal sino la misma regla escrita de otra forma («la redacción corresponde a Francisco», «✍ teoría (Francisco)»). **Decisión de Francisco tomada al cerrar: `2.1.4` NO queda exceptuada** — entra en la retirada completa de `2.x`, porque exceptuar una sola nota reintroduciría a mano la regla recién retirada del capítulo entero; **con eso T25 queda desbloqueada, y con ella T24**. **Deliberadamente sin tocar:** `next-steps.md:382,387,421`, congelado e historial del 2026-07-15; reescribirlo falsearía lo que se decidió entonces. **No es deuda pendiente.** **Residuo sin ficha, señalado y no tocado, PENDIENTE DE DECISIÓN DE FRANCISCO desde el 2026-08-09 y aplazado el 2026-08-11:** `resumen-de-decisiones.md:459` dice «queda como divergencia a corregir por Francisco al redactar» — roza la regla retirada pero **no es la misma cosa** (habla de una divergencia terminológica concreta en `2.2.4`, «detectores no supervisados», no de la autoría de un capítulo). Solo tiene **dos salidas: ficha propia en `## Abiertas` o descarte expreso**, y **plantearlo ANTES de repartir trabajo**, no al cerrar sesión, que es lo que lo ha aplazado dos veces. Las **2 notas de `99 Investigación/`** que dicen que `6.2` la redacta Francisco son trabajo de **T17**. **Fuera del alcance de T0 pero corregido en el mismo ciclo, con aprobación de Francisco:** `how-to-work.md:32` decía «no te fíes de la prosa de `next-steps.md`/bitácora» cuando desde el 2026-08-01 el registro operativo vivo es `features.md` | `d6dae35` |
| 2026-08-09 | Informe | **La línea de `4.2` en «lo escribe Francisco» quedó desfasada** (ficha abierta el 2026-08-01, marcada «la acepta o la retira Francisco»). Se retira de `## Abiertas` por absorción: **T0 la resolvió** y no le quedaba contenido propio. La prosa de `4.2` la redacta el `redactor-tfg` —el borrador de «Origen» y «Las 41 características» ya existía en la nota desde la decisión del 2026-07-21— y Francisco solo **revisa** el «por qué NSL-KDD». Su contenido restante lo cubre **T10**, que sigue abierta | `d6dae35` |
| 2026-08-09 | — | **Andamiaje · `how-to-work.md` §6 «How to» pasa a exigir recomendación de paso siguiente.** Dos viñetas nuevas (`:30-31`), justo debajo de «Pideme aprobación para cada step a ejecutar», a petición explícita de Francisco: (1) **nunca cerrar una respuesta con un menú de decisiones abiertas** para que elija a ciegas — se propone **un** paso concreto y se justifica por qué ese y no los otros candidatos; la aprobación por step **sigue siendo obligatoria**, recomendar no es ejecutar; (2) criterio de ordenación por defecto de esa recomendación: **qué desbloquea más por minuto de máquina** — lo barato que destraba varias fichas va antes que lo caro que no destraba nada. Intervención sin ficha previa en `## Abiertas`: un solo fichero tocado, +2 líneas | `e1be742` |
| 2026-08-09 | Código | **T18 · Rediseño de qué se publica en `alcance_tiempo_s`.** Los **cuatro defectos** que dejaron `0595a15` en `[PENDIENTE, NO APTO]` quedan resueltos, y con ellos el bucle de fondo: el CSV publica solo lo **estable** (qué tramos entran, cuáles no y el aviso de P9) y **todos los números viven en `PIPELINE.md`**, anclados a commits de git, editables sin re-correr. Las dos frases empíricas prohibidas —«las desviaciones observadas caben dentro de la dispersión entre corridas» y «un tramo de coste casi FIJO que no escala con el modelo»— estaban en **8/8 y 8/8 filas** y ahora salen **0/8 y 0/8**. Corrida final `1163c90`: **222 filas**, `commit` limpio, `semilla = 42`, **deriva de calidad cero** contra nueve anclas externas y sin fuga de datos. `PIPELINE.md` re-anclado a `1163c90` con todas las cifras reproducibles desde los CSV. **Efecto sobre otras fichas:** re-ancla **T20** (era falsa: 8 de 10 pares, no 4 de 4, y horquilla retirada) y refuerza **T19** (Hallazgo 7). Dictamen de `auditor-ml`: APTO. Commits previos: `ac496cb`, `1163c90` | `8fdc421` |
| 2026-08-09 | Código | **T22 · `n_iter_` del Autoencoder.** Cerrada **con la conclusión invertida respecto a lo que la ficha traía**: `n_iter_total_grid` queda registrado por fila y resulta **determinista** — **162** a 54 características y **128** a 122, idénticos en las dos corridas que lo registran (una de ellas no reproducible desde git). Con las épocas congeladas, el wall-clock del Autoencoder se mueve **1,29× y 3,63×** entre corridas: esa variación es **carga de máquina, no épocas**, que era justo lo que la ficha no podía decidir. El cociente s/época **no separa nada** al tener denominador fijo. Y el eje **54-vs-122 es indecidible con este diseño** sin medidas repetidas: eso es un **resultado**, no una tarea pendiente. Dictamen de `auditor-ml`: APTO. Sale con T18 (`ac496cb`, `1163c90`) | `8fdc421` |
| 2026-08-09 | Informe | **Auditar la bibliografía** (ficha abierta el 2026-08-01). Se retira de `## Abiertas` por absorción: **T15 la cubrió por completo** —cita completa y nivel declarado en las 10 entradas, `[9]` retirada, `[1]` sustituida, `[2]` y `[8]` completados con año y editorial— y no le quedaba contenido propio. Se resolvió en `396e283`; no genera trabajo nuevo más allá de los residuos **T23**-**T25** que ya dejó T15 | `396e283` |
| 2026-08-09 | — | **T15 · B1: auditoría de `Bibliografía.md` cerrada.** Las **10 entradas** con cita completa y **nivel declarado** (8 de nivel 1; `[2]` Anderson 1980 queda en **nivel 2** y no hay forma de subirlo). `[9]` **retirada sin renumerar** (copia no autorizada del mismo Stallings de `[8]`, y hoy además exige login); `[1]` **sustituida** por la nota de prensa oficial de INCIBE (**97.348 incidentes en 2024, +16,6 %**), y `[2]` y `[8]` completados con año y editorial. Formato migrado a **tabla de staging**. **0 entradas añadidas**: el volcado de las ≈40 fuentes es **T16** y va después de la redacción. Informe en `Obsidian_TFG_Vault/99 Investigación/Auditoría de Bibliografía.md`. Residuos dados de alta: **T23**, **T24**, **T25** | `396e283` |
| 2026-08-08 | Código | **T1 · Nivel 1: esquema de métricas.** Cerrada en su objetivo, con residuos anotados (`T18`-`T22`). Las **8 tablas regeneradas**, tres corridas del runbook completo; las publicadas son las de `5f98d88`, producidas por el código `5516b60`: `commit` limpio y `semilla = 42` en las **216 filas**, recuentos 8/8/2/2 y 16/36/144/6, **cero deriva en métricas de calidad**, sin leakage y sin valores imposibles. Esquema nuevo: `bin_accuracy` en `metricas_baseline.csv`, campo **`alcance` por fila** en las cuatro tablas (cierra C3 y C6 — `accuracy_D2` era columna homónima con dos alcances: 0,9683 en firmas, 0,7395 en baseline), columnas `semilla` y `commit`, conjunto mínimo obligatorio de columnas, `_limpiar_variante_csv` subido a `evaluacion.py` con `CLAVE_UNICIDAD` declarada (variante × algoritmo × alcance), y **tiempo de inferencia separado del de entrenamiento** con latencia por flujo y flujos/s. Además, no previsto en la ficha: **todos los cronómetros pasados de `time.time()` a `perf_counter`** (`time.time()` tiene ≈15,6 ms de resolución en Windows y publicaba `latencia_ms_por_flujo = 0.0` con caudal vacío en DecisionTree); **guarda única** para latencia, caudal y FPR — un valor no medible da **celda vacía, nunca `0.0`**; y `tiempo_s`, que significaba **tres cosas distintas según la tabla** sin que el dato lo dijera, ahora declara su `alcance_tiempo_s` por fila. **Hallazgo mayor:** el residual `tiempo_s − entrenamiento − inferencia` llegaba al **49 % en OneClassSVM-54** y estaba sin declarar; la etiqueta lo llamaba «figuras», que son décimas de segundo. Medido y cerrado con dos columnas nuevas en `metricas_anomalias.csv` (`tiempo_score_seleccion_s`, `tiempo_score_umbral_s`): el grueso es **el scoring repetido dentro de la selección de hiperparámetros** —el script pasa por el scorer 5-7× más filas eligiendo config que evaluando— y en OCSVM-54 ese tramo **iguala al propio ajuste**; no entraba en `tiempo_entrenamiento_s` porque no es `fit`. Declarado que **`latencia_ms_por_flujo` mide solo `predict`/`score`** sobre características ya calculadas y en memoria, sin captura ni extracción de features: sin esa frase, citar el caudal como capacidad operativa sería la *Lab-Only Evaluation* que denuncia P9 (la mitad que falta → `T21`). **Corrección de lo que esta ficha afirmaba mientras estuvo abierta:** era **falso** que «ningún resultado publicado cambia: solo cambia el esquema de columnas» — no cambia **ninguna métrica de calidad** (semilla 42, modelos y calibración OOF intactos), pero **las columnas de tiempo sí cambian de valor**, por el paso a `perf_counter` y por la varianza de máquina, y cambia el `alcance` de las 16 filas de `metricas_balanceo.csv`. Decisiones de diseño internas → `T17`. **Cuatro pasadas de `auditor-ml`**; dictamen sobre las tablas publicadas: T1 puede cerrarse en track Código. Commits: `077119e`, `38fdd4b`, `34bee30`, `5516b60`, `5f98d88` | `5f98d88` |
| 2026-08-01 | Código | Fin del «roadmap vivo»: `next-steps.md` ya no se anuncia como tal en ningún fichero. La frase de reparto sale del callout «Estado a 2026-07-16» de `CLAUDE.md:115-117` a párrafo propio fechado el 2026-08-01 (datar el congelado tres semanas antes era falso), mismo arreglo en `resumen-de-decisiones.md:4` + inciso de fecha sobre la casilla del 2026-07-21 (`:440-443`, registro original íntegro) + entrada de bitácora nueva (`:533-542`), y «Roadmap» → congelado en `README.md:26-28` y `Guia_ML\README.md:7-9`. El auditor corrige además el fondo: «§6 vigente como especificación técnica» era falso sin matiz — `next-steps.md:591-597` declara §6.5 (`hibrido.py`) superada por el grill H-1…H-7, y sin la salvedad un implementador podía calibrar `UMBRAL_CONF` con el método viejo y saltarse una decisión anti-leakage cerrada; la salvedad va en los cuatro ficheros. Dos pasadas de `auditor-ml` (la primera APTO CON CAMBIOS, 4 puntos aplicados), árbol ASCII de `README.md` intacto | `b5aec20` |
| 2026-08-01 | Código | Diagrama `01_pipeline_completo.mmd` al día: 15 correcciones verificadas contra `fichero:línea` — capa de modelos ya no es «no implementado», «51 ataques» → 40 etiquetas, la alineación one-hot es la **unión D1+D3** (y no «schema de D1», que documentaba el bug cerrado el 2026-07-05), alta del paso `select_features()` 122→54 y de las 4 aristas del protocolo anti-leakage (calibración OOF de `UMBRAL_CONF` con D3, D2 no ajusta nada). `.png` y `.svg` regenerados con `mermaid-cli` 11.16.0 `-s 3`; segunda auditoría sin rojos ni naranjas. Incluye `diagramas/README.md` y, en `CLAUDE.md`, la atribución del balanceo 4.3.4 a `firmas.py` (por algoritmo), no a `program.py` | `d88dada` |
| 2026-08-01 | Código | `CLAUDE.md` al día tras la absorción de `Implementacion/`: tabla de scripts de 2 a 8 (6 clases reales + `config.py` y `evaluacion.py` como módulos-librería), orden de ejecución y dependencias entre scripts, y en `## Git` que `Implementacion/` ya no lleva `.git` propio y la precedencia de su `.gitignore` anidado | `e3548ca` |
| 2026-08-01 | Código | Absorción del repo git anidado `Implementacion/`: retirado el gitlink huérfano y versionados los 22 ficheros de código (8 scripts de `app/`, 10 diagramas, `requirements.txt`, `PIPELINE.md`, `readme.md`, `.gitignore`) | `fb920b8` |
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
