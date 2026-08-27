# Las tareas de Kiko

Revisado el **2026-08-27** contra `Resultados\docx\REPASO_20260826-2123\` (extracción **vigente**: `.docx` con `mtime` 2026-08-26T19:46, Word no abierto).

Fichero hermano: `Lo que quedo fuera.md`, inventario de lo que se quedó en el vault. Los cruces se resumen en una frase dentro de cada tarea.

---

## HOY · Roto o mal

- [ ] **5.1** · Invertir la atribución en «D2 y D3 no se dividen…»: D3 entrena la etapa 2 y aporta las probabilidades out-of-fold; D2 es el conjunto de evaluación. `vault`

- [ ] **5.2** · Reescribir el párrafo de D1. Texto a aplicar en Word: «D1 es el conjunto de tráfico exclusivamente normal y se divide en dos particiones: D1_train (80 %), con la que se ajusta el detector de anomalías, y D1_val (20 %), sobre la que se fija el umbral por percentil 95. D1 no interviene por sí mismo en ningún ajuste: solo lo hacen sus dos particiones.» `Word`

- [ ] **T3** · Completar la entrada `[66]` de la lista bibliográfica y borrar el aviso «⚠️ INCOMPLETA». Entrada ya montada para pegar (versión leída de `Implementacion/requirements.txt`: scikit-learn 1.7.1): `Word`

  > scikit-learn developers, "sklearn.neighbors.LocalOutlierFactor", *scikit-learn 1.7.1 documentation*. [En línea]. Disponible en: https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.LocalOutlierFactor.html [Consultado: 27-ago-2026].

- [ ] **2.25** · Eliminar el Título 3 vacío que cierra el capítulo 2, inmediatamente antes del Título 1 «Diseño del sistema». `Word`

- [ ] **3.10** · Eliminar (o titular) el Título 3 vacío y los tres párrafos vacíos que siguen al pie «Tabla 3.1. Subconjuntos especializados». `Word`

- [ ] **A7 + A8** · **DECISIÓN APLICADA:** borrar el encabezado vacío «A.2. Métricas de desempeño» y su entrada del índice, y **regenerar el índice**. Consecuencias: resuelve uno de los tres rótulos de **R10**, y obliga a restituir el párrafo de `1.4 Estructura` (hallazgo 5 del cap. 1) **sin** «fórmulas de las métricas de desempeño». `Word` + `vault`

- [ ] **A15** · Encabezado de página del Apéndice A: lleva «Capítulo 6. Conclusiones» → corregir el salto de sección; comprobar en Word.

- [ ] **6.10** · Título 1 «Conclusiones» seguido del Título 2 «Conclusiones». Dos opciones: `Word`
  - **(recomendada)** renombrar el **Título 1** a «Capítulo 6. Conclusiones y líneas futuras»: es lo más fiel, porque el capítulo contiene `6.1 Conclusiones` y `6.2 Líneas futuras`, y el índice deja de repetir la palabra.
  - alternativa: dejar el Título 1 y renombrar el **Título 2** a «6.1. Balance del trabajo».

- [ ] **5.4** · Insertar en §5.0 el diccionario de códigos de decisión, tal cual: `vault`

  > Las decisiones de diseño se identifican con un código estable a lo largo de la memoria. **Q1/C** establece que el conjunto de características (54 o 122) no se fija a priori sino por experimento, y quedó resuelto en 54. **H-2** designa el Autoencoder como detector por defecto de la etapa 1. **H-3** designa RandomForest como clasificador de la etapa 2, fijo entre las dos variantes. **H-6** establece que la evaluación multiclase del híbrido se reporta como matriz 5×6 y desglosada por alcance, sin un número único.

  `Lo que quedo fuera.md` (cap. 3) excluye 5.4 por nombre, luego **ningún hallazgo la resuelve**. La alternativa —eliminar los códigos del cuerpo— es más cara y pierde trazabilidad.

- [ ] **2.10** · **Fundida en 2.11.** El estado del arte es exigible en un TFG, pero **no hace falta sección nueva**: §2.2.4.5 ya sitúa el trabajo frente a Tombini. Basta titular «Trabajos relacionados» el bloque existente que resuelve **2.11**. Coste bajo y cubre el riesgo ante el tribunal. `vault`

- [ ] **2.11** · Escribir los tres trabajos anunciados en «Situar este trabajo frente a esos tres casos permite precisar en qué se apoya y en qué se aparta». Sede: **§2.2.4**, justo tras esa frase. Los tres están identificados en `Lo que quedo fuera.md` (cap. 2): **Ji *et al.*, Kim *et al.* y Khraisat *et al.*** (incluida la crítica a Khraisat por no taxonomizar lo híbrido); el material está en la nota `2.2.4` del vault. Alternativa barata: reescribir la frase a «Situar este trabajo frente a Tombini permite precisar…». **Recomendado escribirlos**, porque ahí se resuelve de paso **2.10**. `vault`

- [ ] **2.12** · Restituir **una frase** en §2.2.3 que fije el sentido (a) al que apunta el inciso «dentro del sentido (a) fijado más arriba»: híbrido = combinación de detección por anomalías y por firmas en un mismo sistema, frente a los otros tres sentidos (híbrido de algoritmos, de fuentes de datos, de despliegue). Procede de la tabla de los cuatro sentidos de «híbrido» de `2.2.3.2` del vault, que no se volcó (`Lo que quedo fuera.md`, cap. 2). Alternativa: borrar el inciso. **Recomendado restituir**, porque el inciso se usa después. `vault`

- [ ] **2.14** · **Recomendación: corregir el anuncio de «cuatro tramos» a «dos tramos» y no escribir los que faltan.** Los ausentes son `2.3.2.3` (la cara ofensiva), `2.3.2.4` (*adversarial ML*) y `2.3.2.5` (el panorama de datasets), según `Lo que quedo fuera.md` (cap. 2); sede §2.3.2. Razón: **2.16** ya ordena *comprimir* el capítulo 2 y añadir tres apartados va en dirección contraria. Es un cambio de dos palabras que cierra la promesa incumplida. `Word`

- [ ] **6.9** · Declarar en **§6.1.1**, dentro del objetivo general, que la comparación contra «cada etapa por separado» **sí se hizo**: la **Tabla 5.2** mide la etapa 1 sola sobre D2 y la **Tabla 5.3** la etapa 2 sola sobre los ataques conocidos de D2. Basta nombrar esas dos tablas. Orden: cruza con el **hallazgo 1 del cap. 1** de `Lo que quedo fuera.md`, que sustituye la lista de objetivos entera — decidir ese hallazgo primero y 6.9 se absorbe. `vault`

- [ ] **6.12** · Cabecera de la Tabla 6.1 (Ctrl+F «Error metodológico»): la celda `[f1,c1]` está vacía → poner rótulo a la columna P1–P10. `Word`

- [ ] **4.16** · «permite medir la detección de ataques "0-day" por tipo» → comillas españolas «0-day». `Word`

- [ ] **5.18** · Crear la tabla de tiempos que el texto crítico reclama y hoy no existe. Rótulo: **«Tabla 5.14. Coste temporal e inferencia de los cuatro clasificadores de firmas»**. Sede: **§5.2**, junto al párrafo `p2373` («Junto al FPR conviene acotar la segunda cifra que invita a la sobrelectura: la velocidad»), **antes** del bloque de avisos que ya existe (`p2375`–`p2379`). El número `5.14` está libre: la última tabla del capítulo es hoy la 5.13 (pie en `p2359`). Cifras de `Resultados/metricas_firmas.csv`, semilla 42, con `n_inferencia` = 9.083 en las ocho filas: `vault`

  | Algoritmo | Set | Entren. (s) | Inferencia (s) | ms/flujo | flujos/s |
  |---|---:|---:|---:|---:|---:|
  | DecisionTree | 54 | 1,815 | 0,002 | 0,000238 | 4.196.350,2 |
  | RandomForest | 54 | 61,444 | 0,066 | 0,007232 | 138.276,6 |
  | KNN | 54 | 42,648 | 1,565 | 0,172337 | 5.802,6 |
  | HistGradientBoosting | 54 | 60,745 | 0,029 | 0,003234 | 309.248,5 |
  | DecisionTree | 122 | 2,301 | 0,004 | 0,000391 | 2.556.719,0 |
  | RandomForest | 122 | 51,097 | 0,031 | 0,003366 | 297.079,6 |
  | KNN | 122 | 68,557 | 2,528 | 0,278364 | 3.592,4 |
  | HistGradientBoosting | 122 | 122,82 | 0,098 | 0,0108 | 92.594,4 |

  **Por qué la tarea es real:** el cuerpo discute `latencia_ms_por_flujo` y `flujos_por_segundo` por su nombre de columna —y comenta la cifra de 4.196.350,2 flujos/s con latencia 0,000238 ms (DecisionTree, 54 características)—, pero **ninguna tabla publicada muestra esas dos columnas**.

  **Caveat obligatorio al pie de la tabla**, ya enunciado por el propio texto en `p2375`–`p2377`: estas dos columnas miden **solo** el `predict`/`score` sobre el vector ya construido y en memoria; **no** incluyen captura del tráfico, ensamblado de los paquetes en flujos ni extracción de las 41 características. Son **techo de inferencia en laboratorio, no capacidad operativa**.

  **Incoherencia que el propio texto confiesa (`p2379`):** `flujos_por_segundo` se calcula del tiempo sin redondear mientras que `tiempo_inferencia_s` se publica a tres decimales, de modo que la columna no se puede reconstruir dividiendo; hay que decidir entre publicar más decimales o retirar la columna — **recomendación: publicar `tiempo_inferencia_s` con más decimales**, que hace la tabla reconstruible y elimina la confesión de incoherencia.

- [ ] **T4** · Pegar los marcadores que faltan recorriendo el **Anexo C** de este fichero (~18 filas tras la poda del 2026-08-27), fila a fila por su fragmento literal, con el Word abierto. Cada marcador va **al final de la frase, antes del punto, y siempre a pelo**. `Word`

- [ ] **B2** · Dar formato IEEE a las entradas hoy en URL desnuda. Entradas ya montadas para pegar: `Word`
  - `[1]`: "Principales ciberataques en España en 2024", *ChannelPartner*. [En línea]. Disponible en: https://www.channelpartner.es/seguridad/principales-ciberataques-en-espana-en-2024/ [Consultado: 27-ago-2026].
  - `[10]`: Centro Criptológico Nacional, *Glosario de términos y abreviaturas*, CCN-STIC 401. [En línea]. Disponible en: https://www.ccn-cert.cni.es/publico/seriesCCN-STIC/series/400-Guias_Generales/401-glosario_abreviaturas/index.html [Consultado: 27-ago-2026].
  - `[11]`: M. Roesch, "Snort — Lightweight Intrusion Detection for Networks", en *Proc. 13th USENIX LISA*, Seattle, WA, 1999, pp. 229-238.
  - `[9]`: es solo un PDF del libro de Stallings, duplicado de `[8]`. **Verificado: `[9]` no se cita en ninguna parte del cuerpo**, así que **se borra la entrada y NO se renumera nada** — es el protocolo de «quemar» un número que el proyecto ya usa. **Sin miedo a la renumeración: no hay ninguna.**

- [ ] **B1** · Mantener la lista **intacta**, sin retirar ninguna obra, como pediste: la poda obligaría a renumerar. Única acción: **añadir la fila de Chow**, que falta (aparece una sola vez en el `.docx`, `p3012`, y cero veces citada en el cuerpo). Las obras del `.docx` sin cita en el cuerpo son **19** y están listadas en el **Anexo C**, de modo que B1 y el Anexo C ya no se contradicen. `vault` + `Word`
  - Aviso aparte, que no es orfandad: **`TabArena` se cita en el cuerpo (`p2610`) y NO tiene entrada en la lista de referencias** — cita sin respaldo bibliográfico.
  - Las obras huérfanas de `Bibliografía.md` del vault (Barbará, Grinsztajn, McElfresh, Shwartz-Ziv, Hollmann, Bergstra, Storkey, Micci-Barreca, Pargent, Hwang, Behrouz, *Model Cards*, CRISP-DM, Pendlebury) **no están en la lista del `.docx`**: buscarlas en Word no dará resultados.

- [ ] **X31** · **DECISIÓN APLICADA:** cambiar `[74]` por `[72]`. Cómo: Ctrl+F en Word sobre «ilustra la magnitud del problema sin medirla» y sustituir el número del corchete final, a pelo. Verificado: `[72]` es Goldschmidt y Chudá («Network intrusion datasets: A survey, limitations, and recommendations», 2025), que es de lo que habla la frase; `[74]` es Sharafaldin (CIC-IDS2017), correcto en su otra aparición del cap. 6. `Word`

- [ ] **A14** · Pendiente por decisión de Francisco, por si se añade el apéndice. Si algún día se decide retirar, lo que se borra son **las dos llamadas de `p2447` (§6.1.4)**; **no hay ningún encabezado `A.3` que quitar**, porque el apéndice no existe. `Word` + `vault`

- [ ] **A16** · **Sí aplica** (A5 decidió no numerar los cuatro bloques). Sustituir la leyenda por: «Tabla A.1. Características del dataset completo NSL-KDD, desglosadas en los cuatro bloques anteriores: básicas (1–9), de contenido (10–22), de tráfico basadas en tiempo (23–31) y de tráfico basadas en host (32–41).», y anunciar en «Cada registro del dataset describe una conexión TCP/IP resumida en 41 atributos» que la tabla va partida en cuatro bloques. `Word` + `vault`

- [ ] **4.15** · Figura 4.3 y su pie en la misma página; comprobar en Word.

- [ ] **5.28** · Tabla 5.11 y su pie en la misma página; comprobar en Word.

- [ ] **A11** · Unificar a mayúsculas `S0/S1/S2/S3` las menciones a los flags de conexión del apéndice; comprobar en Word.

- [ ] **A13** · Dar formato monoespaciado a «El pipeline (program.py) codifica las etiquetas en dos niveles», a la ruta `Resultados\specialized_nsl_kdd_mappings_and_info.txt` y a «los ficheros y_attack/y_category»; comprobar en Word.

> [!note] Punto a verificar, sin tarea abierta
> `[45]` (Kendall, base de datos de ataques del DARPA) está anclado en «sino la definición formal del espacio de salida del modelo» (`p0595`), que no parece corresponder a esa obra.

---

## Recorte

- [ ] **5.21** · El 13,4 % se explica siete veces → dejar la explicación en «Este 13,4 % no es un defecto de ejecución, sino el comportamiento que la teoría predice» y remitir desde las otras seis. La sede superviviente debe estar **en §5.3**, y el recorte va **antes** que los hallazgos 5 y 6 del cap. 5 de `Lo que quedo fuera.md`, que reponen contenido ahí. `vault`
  - «Lo que el 13,4 % cuantifica es la calidad del etiquetado de lo desconocido».
  - «Es la explicación teórica del 13,4 % de 0-day detectados».
  - «La consecuencia estámedida: de los 0-day que la etapa 1 sí detecta, solo el 13,4 % llegan a etiquetarse unknown».
  - «de los 0-day que la etapa 1 sí detecta, solo el 13,4 % se enruta a unknown».
  - «de estos 0-day detectados, solo el 13,4 % termina etiquetado como unknown».
  - «El 13 se cita con tres salvedades».

- [ ] **4.10** · El desbalance 883:1 se desarrolla **seis** veces → dejarlo en una y remitir desde las demás. `vault`
  - «un desbalance de ratio ≈ 883:1 entre DoS y U2R» (cap. 2, viñeta «Huella en el tráfico» de U2R).
  - «Este desbalance extremo (ratio ≈ 883:1 entre DoS y U2R) es lo que motiva el mini-experimento».
  - «supera a la minoritaria (u2r) en una proporción cercana a 883:1».
  - «La proporción entre la clase mayoritaria y la minoritaria es ≈ 883:1».
  - `p1285`, «La Tabla 4.8 recoge la distribución de D3 por categoría de ataque, con un desbalance de ≈ 883:1…».
  - Pie «Tabla 4.8. Distribución de D3 por categoría de ataque» (solo si se decide quitar la cifra del pie).

- [ ] **4.11** · La justificación del umbral p95 se repite tres veces → dejarla en un solo sitio y reducir el resto a mención escueta. La sede superviviente debe ser la que **enlace** con la explicación que el hallazgo 3 del cap. 5 de `Lo que quedo fuera.md` repone en §5.1 (por qué el p95 promete ≈5 % y se mide 10,2 %). `vault`
  - «El umbral se fija en el percentil 95 de la puntuación de anomalía sobre validación».
  - «El umbral se fija en el percentil 95 del score de anomalía sobre un subconjunto de validación reservado de D1».
  - «para D1_val es el fijado del umbral de decisión, que quedó como el percentil 95 del score».

- [ ] **5.22** · Dos viñetas casi calcadas → dejar una. `vault`
  - «El baseline también falla donde su CV prometía: su f1_macro cae de 0.909».
  - «El baseline también falla donde su validación cruzada prometía: su f1_macro se desploma de 0.909».

- [ ] **6.11** · El `[40]` García-Teodoro **se ancla en el capítulo 6 y ahí se queda** («firmas y anomalías no compiten, sino que se complementan», `p2417`, sede única). No hay recorte que hacer. `vault`

- [ ] **6.4** · **DECISIÓN APLICADA:** deduplicar dejando el desarrollo en el **capítulo 6** y reduciendo el del capítulo 2 a una mención con remisión; el `[50]` va una sola vez, junto al `[49]` del capítulo 6. Razón: en el cap. 6 el supuesto sostiene el límite «No hay adversario adaptativo (P10)» y la fila P10 de la Tabla 6.1; en el cap. 2 es enunciado de marco. `vault` + `Word`

- [ ] **T12** · **DECISIÓN APLICADA:** no fusionar. Conservar la **Tabla 3.1** como tabla de *función* y reconvertir la **Tabla 4.7** en tabla de *reparto por categoría con doble denominador*, remitiendo a 3.1 en vez de repetirla. Recoge así el hallazgo 2 del cap. 4 de `Lo que quedo fuera.md` (DoS 7.458, Probe 2.421, R2L 2.754, U2R 200, normal 9.711; porcentaje sobre D2 completo y sobre los 12.833 ataques, más las dos erratas de denominador). Aviso: cualquier movimiento en el capítulo 4 obliga a revisar que la serie `4.x` quede contigua y sin duplicados, arrastrando las llamadas de la prosa. `Word` + `vault`

- [ ] **3.6** · Dejar la confesión de *data snooping* en el **capítulo 3** (que ya lleva el `[49]`) y remitir desde el capítulo 6. Compatible con el hallazgo 7 del cap. 4 de `Lo que quedo fuera.md`, que pide que las cuatro sedes del cap. 4 remitan con una fórmula breve; ese hallazgo pide además revertir en `4.4` el «y D2 no interviene en ningún momento» a «en esta selección». `vault`

- [ ] **4.12** · «Ganadores por algoritmo: class_weight para DecisionTree; SMOTE para RandomForest, KNN y HistGradientBoosting» → borrar la tabulación y dejar solo la remisión a §4.3.4. `vault`

- [ ] **2.17** · La justificación one-class aparece tres veces → dejarla en una y remitir desde las otras dos. Ojo al hallazgo 3 del cap. 3 de `Lo que quedo fuera.md`, que repone `3.4.5` y sería una cuarta sede. `vault`
  - «Estos algoritmos se denominan semisupervisados (one-class)».
  - «se mencionan solo para delimitar por contraste el régimen semisupervisado (one-class)».
  - «La etapa 1 materializa este paradigma con detectores semisupervisados (one-class)».

- [ ] **R7** · «El tipo de ataque snmpgetattack (n = 178) lo fallan los cuatro detectores» repite «snmpgetattack es un punto ciego universal» → fundir en una, conservando el soporte n = 178. `vault`

- [ ] **R8** · «patrón dominante en la literatura» aparece tres veces → dejar la formulación completa en la primera y abreviar las otras dos. `vault`

- [ ] **R10** · El rótulo «Métricas de desempeño» se usa tres veces como encabezado (§5.1, §5.2 y A.2) → renombrar al menos dos. **A7 + A8 ya resuelve el de A.2 al borrarlo.** `Word` + `vault`

- [ ] **1.1** · Fundir los Título 2 «Motivación» y «Preliminares», consecutivos. Cruza con el hallazgo 4 del cap. 1 de `Lo que quedo fuera.md`: fundir primero, desarrollar los cinco desafíos después. `vault`

- [ ] **1.3** · Fundir «validando los resultados y midiendo la capacidad de detección de ataques desconocidos» y «Medir la capacidad de detección de ataques desconocidos y analizar críticamente los resultados» en un solo objetivo específico. **Decidir antes el hallazgo 1 del cap. 1** de `Lo que quedo fuera.md`, que sustituye la lista entera por nueve objetivos numerados: si se aplica, 1.3 se absorbe. `vault`

- [ ] **A9** · «véase 4.3 Preprocesamiento de los datasets §4.3.5» → «véase §4.3.5». `vault`

---

## Mejora

- [ ] **2.13** · Título 3 «IA, ML y DL», hoy al final del capítulo dentro de §2.3 → pasarlo al principio del capítulo 2, delante del Título 2 «Machine Learning». `vault`
- [ ] **2.15** · Título 3 «Etapas del Ciclo de vida de un proyecto de ML» y sus cinco hijos en Título 5 → bajar los hijos a Título 4; hoy §2.1.3 no tiene subentradas en el índice. `Word`
- [ ] **2.16** · Comprimir el Título 3 «Límites y consideraciones éticas», que desarrolla P9 y P10 con extensión de capítulo de resultados. **Orden obligado:** primero comprimir P9 y P10, después restituir lo que pide el hallazgo 8 del cap. 2 de `Lo que quedo fuera.md` (`2.3.3.6`, `2.3.3.8` y el bloque ético `2.3.3.4/5/7`). El saldo de longitud puede quedar neutro. `vault`
- [ ] **3.5** · «Para comprobar que el orden de la cascada fijado en §3.2.1 es el adecuado» y los dos párrafos siguientes → moverlos al capítulo 5, tras «Resultados del sistema híbrido». `vault`
- [ ] **4.7** · Reordenar los Título 3 del cuerpo a codificación → normalización → selección, el orden real del pipeline. `vault`
- [ ] **4.8** · «El conjunto D3, con el que se entrena el clasificador de firmas, está fuertemente desbalanceado» → añadir el aviso de que el eje SMOTE vs `class_weight` no queda establecido entre semillas (§5.2.4). `vault`
- [ ] **4.9** · «Tabla 4.6. Experimento H1: comparación del sistema híbrido completo sobre D2» → mover el experimento al capítulo 5 o marcarlo como adelanto. `vault`
- [ ] **5.5** · Sacar del cuerpo las rutas de artefacto, a apéndice o nota al pie. `vault`
  - «está en Resultados\selected_features.txt».
  - «se persisten en Resultados\specialized_nsl_kdd_mappings_and_info.txt».
  - «del autoencoder (Resultados/metricas_hibrido_0day.csv».
- [ ] **5.11** · §5.3 «Resultados del sistema híbrido» y §5.4 «Conclusiones del capítulo» no tienen ningún Título 3 dentro → titular sus apartados con estilo de encabezado. `Word`
- [ ] **5.12** · Partir en Discusión y Conclusiones el Título 2 «Conclusiones del capítulo» del capítulo 5. `vault`
- [ ] **5.13** · Unificar el nombre de los dos apartados de cierre: «Resultados finales» (§5.1) y «Comparación de los resultados de cada algoritmo» (§5.2). `vault`
- [ ] **5.15** · Unificar las referencias cruzadas, hoy en tres formatos: «§4.3.5», «(4.3.5)» y «en 3.3.2 y 5.4». `Word`
- [ ] **6.5** · «Tasa de falsos positivos condicionada por el drift» → añadir que el FPR debe leerse a prevalencia realista (`[73]`) y que la latencia publicada es techo de laboratorio. `vault`
- [ ] **6.6** · Apartado «Validación de la tesis del híbrido» → añadir el titular `f1_macro` 0,8223 con su banda [0,7779–0,8205] y que es el mejor de once corridas. `vault`
- [ ] **6.7** · «Clases minoritarias u2r y r2l. Con muy pocas muestras de entrenamiento» → desdoblar en dos limitaciones, una por clase. `vault`
- [ ] **1.2** · «Este último punto es precisamente el que motiva el presente trabajo.» → sacarlo de la lista y convertirlo en párrafo de cierre. Coordinar con el hallazgo 4 del cap. 1 de `Lo que quedo fuera.md`. `vault`

---

# Anexo C · Citas que faltan por pegar

Solo quedan las obras que **no aparecen citadas ni una vez** en el cuerpo del `.docx`. Contado el 2026-08-27: la lista de referencias tiene **75 entradas** (`[1]`–`[75]`), el cuerpo cita **56 números distintos**, y las **19 sin cita** son `[9]`, `[15]`, `[18]`, `[19]`, `[20]`, `[21]`, `[37]`, `[50]`, `[54]`, `[56]`, `[57]`, `[58]`, `[59]`, `[62]`, `[63]`, `[66]`, `[67]`, `[69]`, `[70]`. No hay ningún marcador citado en el cuerpo que carezca de entrada en la lista.

## Capítulo 2

| ☐ | Marcador | Obra | Buscar este texto |
|---|---|---|---|
| ☐ | `[15]` | Russell y Norvig | «los investigadores han perseguido enseñar a las computadoras a razonar» |
| ☐ | `[18]` | Jolliffe | «Reducción de dimensionalidad y visualización» |
| ☐ | `[19]` | Agrawal y Srikant | «Reglas de asociación, que busca encontrar coocurrencias frecuentes» |
| ☐ | `[20]` | Sutton y Barto | «Un agente aprende por interacción con un entorno» |
| ☐ | `[21]` | Kohavi | «los valores que el algoritmo no aprende de los datos— mediante validación cruzada» |
| ☐ | `[CITA: Shostack, Threat Modeling: Designing for Security, 2014]` | Shostack | «Un modelo de amenaza es la especificación explícita de las hipótesis sobre el adversario» (§2.3; **sin número en el `.docx`, no inventar uno**) |

## Capítulo 3

| ☐ | Marcador | Obra | Buscar este texto |
|---|---|---|---|
| ☐ | `[54]` | Molnar | «del árbol de decisión se extraen reglas legibles (mediante export_text)» |
| ☐ | `[56]` | Chow | «estimadas fuera de muestra (out-of-fold, mediante validación cruzada sobre D3)» |

## Capítulo 4

| ☐ | Marcador | Obra | Buscar este texto |
|---|---|---|---|
| ☐ | `[37]` | He y García | «un clasificador que nunca predijera u2r conservaría un accuracy superior al 99,9 %» |
| ☐ | `[57]` `[58]` `[62]` `[63]` | Harris · McKinney · Hunter · Waskom | filas de NumPy, Pandas, Matplotlib y Seaborn de la tabla de librerías |
| ☐ | `[59]` | Pedregosa | «Núcleo de ML: preprocesamiento (MinMaxScaler, LabelEncoder)» |
| ☐ | `[66]` | doc. scikit-learn | «LocalOutlierFactor se instancia con novelty=True» — depende de **T3** |
| ☐ | `[67]` | Sakurada y Yairi | «las conexiones anómalas se reconstruyen mal y producen un MSE alto» |
| ☐ | ⛔ sin obra | — | «Python es el lenguaje de referencia para el aprendizaje automático»: no hay obra que lo respalde → **atenuar a «uno de los lenguajes más extendidos» o retirar la afirmación** |
| ☐ | `[CITA: medición propia, artefacto de Resultados/]` | — | «≈4·10⁶ flujos/s a 54 características» → respaldar en **nota al pie** con el artefacto de `Resultados/` |

## Capítulo 5

| ☐ | Marcador | Obra | Buscar este texto |
|---|---|---|---|
| ☐ | `[69]` + `[70]` | Demšar · Dietterich | «Comparación pareada (semilla a semilla)» |

## Capítulo 6

| ☐ | Marcador | Obra | Buscar este texto |
|---|---|---|---|
| ☐ | `[50]` | Biggio y Roli | «Evaluar sobre un conjunto de tráfico fijo equivale a suponer un adversario estático», junto al `[49]` que ya está ahí — así lo decide **6.4** |

**Notas de aplicación**

1. Cada marcador va **al final de la frase, antes del punto, y siempre a pelo, sin localizador**.
2. `[37]` tenía otra fila anclada en «un weighted alto, porque el peso n_i de la clase mayoritaria domina la suma»; ese fragmento está en el `.docx` con mayúscula inicial («Un weighted alto…», `p0462`), así que para evitar un fallo de búsqueda se le ha dado la sede del capítulo 4.
3. `[9]` no lleva ancla: se resuelve **borrando la entrada**, en **B2**.

> [!note] Registro
> El 2026-08-27, por decisión de Francisco, se han **borrado las ~56 filas de los antiguos Anexos C y D** cuyas obras ya se citan al menos una vez en el informe: una obra ya citada no necesita repetirse. Los dos anexos quedan fundidos en este.
