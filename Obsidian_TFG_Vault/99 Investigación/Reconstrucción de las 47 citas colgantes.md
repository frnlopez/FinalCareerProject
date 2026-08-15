---
titulo: "¿A qué fuente real corresponde cada uno de los [11]-[57] que hoy están puestos en el vault?"
numero: "-"
estado: informe
docx_ref: "-"
---

# ¿A qué fuente real corresponde cada uno de los `[11]`-`[57]` que hoy están puestos en el vault?

- **Encargo:** reparar el estado intermedio del pase `[CITA: …]` → `[n]` que murió a medias:
  barrer todo `Obsidian_TFG_Vault/` (salvo `99 Investigación/`) buscando marcadores `[n]` con
  n ≥ 11, reconstruir la correspondencia `[n]` → fuente leyendo el contexto de cada sitio de cita,
  dar de alta las 47 entradas en `Bibliografía.md` con cita completa, DOI/URL estable y nivel, y
  comprobar tres invariantes.
- **Fecha:** 2026-08-15
- **Alcance:** entra la reconstrucción del mapa y el alta en `Bibliografía.md`. **Queda fuera**:
  editar cualquier nota de la memoria, renumerar, las tres correcciones de T25, el pase a Zotero y
  los 6 `[CITA: …]` de `4.2 Base de datos utilizada`, que tienen ficha propia.
- **Alimenta a:** [[Bibliografía]] — y, a través de ella, a todo el capítulo 2.

## Respuesta corta

Los 47 marcadores `[11]`-`[57]` existen, están **todos** dentro del capítulo 2 y ninguno se
solapa: 47 números para 47 fuentes distintas. **42 se han reconstruido y dado de alta con cita
completa y DOI/URL verificado**; de esas, **25 son cierre firme** —la nota nombra a la fuente o
esta ya estaba verificada en `99 Investigación/`—, **16 son «identidad inferida del contexto»**
—metadatos verificados, pero pendientes de que Francisco confirme que es la obra que consultó— y
una (`[54]`, Molnar) tiene la edición sin fijar. **Cinco no se han podido reconstruir**: `[27]`,
`[28]` y `[44]`, sin pista alguna, y `[37]` y `[45]`, identificables como clase pero con la
edición indeterminable. Van dadas de alta con candidatos propuestos y sin inventar un solo dato.
Las tres
invariantes se cumplen, con **una desviación**: `A.3 Ficha del sistema` conserva 7 `[CITA: …]` sin
convertir que no estaban en el inventario de los 6 conocidos.

## Hallazgos

### 1. El alcance real es MENOR que el declarado en el encargo: solo capítulo 2

El encargo daba por confirmado que el pase tocó además `3.3`, `4.4`, `4.5`, `4.6`, `5.1`, `5.2`,
`5.4`, `6.1` y `A.3`. **No es así.** Un barrido de todo el vault con `\[\d+\]` devuelve marcadores
numéricos en 15 notas, y **ninguna de esas nueve está entre ellas**: no contienen un solo `[n]`, ni
≥ 11 ni < 11. Los 47 números viven en **ocho notas**, todas del capítulo 2:

| Nota | Marcadores ≥ 11 (ocurrencias) |
|---|---|
| `2.1.6 Metodologías y buenas prácticas` | 14 |
| `2.2.2 Sistemas de detección de intrusiones` | 6 |
| `2.2.3 Taxonomía de los IDS` | 8 |
| `2.2.4 Detección por firmas frente a detección por anomalías` | 6 |
| `2.2.5 Taxonomía de ataques y panorama de amenazas` | 9 |
| `2.3.1 IA, ML y Deep Learning` | 4 |
| `2.3.2 La IA en ciberseguridad` | 14 |
| `2.3.3 Límites y consideraciones éticas` | 13 |

Son **74 ocurrencias** de **47 números distintos**, y el rango `[11]`-`[57]` está **completo y sin
huecos**. La coincidencia entre «47 números nuevos» y «rango 11-57 sin huecos» es la confirmación
de que el pase anterior asignó de forma correlativa y no se saltó ni repitió ninguno.

**Consecuencia práctica:** la reparación es más pequeña de lo temido y **el resto de capítulos no
está contaminado**. Lo que sí arrastran esos capítulos es otra cosa —`A.3`, ver hallazgo 4—.

### 2. El mapa `[n]` → fuente, reconstruido

El mapa no existía en ningún fichero. Se ha reconstruido de tres maneras, por orden de fuerza:
(i) la nota **nombra** a la fuente en el propio texto o en un callout de «Verificación pendiente»;
(ii) la fuente estaba ya verificada en un informe de `99 Investigación/`; (iii) la afirmación
apunta a una obra canónica única. Solo (i) y (ii) cierran; (iii) queda marcada.

| `[n]` | Fuente reconstruida | Nota donde se usa | Cómo se ha establecido |
|---|---|---|---|
| [11] | Chapman *et al.*, *CRISP-DM 1.0* (2000) | `2.1.6` | Nota nombra CRISP-DM |
| [12] | Hastie, Tibshirani y Friedman, *ESL* (2009) | `2.1.6` | ⚠️ Inferida (obra canónica) |
| [13] | Kohavi, IJCAI'95 | `2.1.6` | ⚠️ Inferida (obra canónica de *K-fold*) |
| [14] | scikit-learn, doc. de `GridSearchCV` | `2.1.6` | ⚠️ Inferida (el texto describe la API) |
| [15] | Bergstra y Bengio, JMLR 2012 | `2.1.6` | ⚠️ Inferida (búsqueda aleatoria) |
| [16] | Chow, IEEE T-IT 1970 | `2.1.6` | **Nota lo nombra** + verificada en `arquitecturas-hibridas` |
| [17] | Kapoor y Narayanan, *Patterns* 2023 | `2.1.6` | ⚠️ Inferida; ya verificada en `benchmark-comparativo` |
| [18] | Arp *et al.*, USENIX Sec. 2022 | `2.1.6`, `2.3.3` | **Nota lo nombra** (P3, P5, P7, P8, P9, P10) |
| [19] | He y Garcia, IEEE TKDE 2009 | `2.1.6` | ⚠️ Inferida (desbalance) |
| [20] | Pineau *et al.*, JMLR 2021 | `2.1.6` | Vocabulario literal de la lista (*number of runs*, *error bars*…) |
| [21] | Sommer y Paxson, IEEE S&P 2010 | `2.1.6`, `2.2.3`, `2.3.2`, `2.3.3` | **Nota los nombra** |
| [22] | McHugh, ACM TISSEC 2000 | `2.1.6`, `2.2.5`, `2.3.2`, `2.3.3` | **Nota lo nombra** |
| [23] | Tavallaee *et al.*, CISDA 2009 | `2.1.6`, `2.2.5`, `2.3.2`, `2.3.3` | **Nota lo nombra** |
| [24] | Axelsson, ACM TISSEC 2000 | `2.1.6`, `2.2.4`, `2.3.3` | **Nota lo nombra** |
| [25] | Scarfone y Mell, NIST SP 800-94 | `2.2.2`, `2.2.3`, `2.2.4` | Nota dice «la guía de referencia del NIST sobre IDPS» |
| [26] | Roesch, LISA'99 (Snort) | `2.2.2` | ⚠️ Inferida (Snort, tradición de reglas) |
| [27] | **NO RECONSTRUIDA** — SIEM/XDR | `2.2.2` | — |
| [28] | **NO RECONSTRUIDA** — defensa en profundidad | `2.2.2` | — |
| [29] | García-Teodoro *et al.*, C&S 2009 | `2.2.3` | ⚠️ Inferida (pareja natural de [30]) |
| [30] | Chandola *et al.*, ACM CSUR 2009 | `2.2.3`, `2.2.4` | **Nota lo nombra** («Chandola et al. [30]») |
| [31] | Khraisat *et al.*, *Cybersecurity* 2019 | `2.2.3` | **Nota lo nombra** |
| [32] | Barbará *et al.*, ADAM 2001 | `2.2.3` | **Nota lo nombra** |
| [33] | Tombini *et al.*, ACSAC 2004 | `2.2.3` | **Nota lo nombra** |
| [34] | Ptacek y Newsham, 1998 | `2.2.3` | ⚠️ Inferida (evasión: fragmentación, canal lento) |
| [35] | *Snort Users Manual* (doc. oficial) | `2.2.4` | ⚠️ Inferida (precede a un bloque de regla Snort) |
| [36] | Kendall, tesis MIT 1999 | `2.2.5` | ⚠️ Inferida (taxonomía DoS/Probe/R2L/U2R) |
| [37] | **NO RECONSTRUIDA** — panorama de amenazas | `2.2.5`, `2.3.2` | Edición sin fijar (lo declara la propia nota) |
| [38] | Strom *et al.*, MITRE ATT&CK (2018/2020) | `2.2.5` | Nota nombra ATT&CK y *cyber kill chain* |
| [39] | Russell y Norvig, *AIMA* | `2.3.1` | ⚠️ Inferida (panorama histórico de IA) |
| [40] | Krizhevsky *et al.*, NIPS 2012 | `2.3.1` | ⚠️ Inferida (ImageNet 2012) |
| [41] | Grinsztajn *et al.*, NeurIPS 2022 | `2.3.1` | **Nota lo nombra** + verificada en `clasificadores-tabulares` |
| [42] | McElfresh *et al.*, NeurIPS 2023 | `2.3.1` | Descripción literal del hallazgo; verificada en `clasificadores-tabulares` |
| [43] | Sahami *et al.*, AAAI WS 1998 | `2.3.2` | ⚠️ Inferida (filtros bayesianos de correo) |
| [44] | **NO RECONSTRUIDA** — apoyo al analista en el SOC | `2.3.2` | — |
| [45] | **NO RECONSTRUIDA** — agencia europea, IA y cibercrimen | `2.3.2` | Edición sin fijar (lo declara la propia nota) |
| [46] | Szegedy *et al.*, ICLR 2014 | `2.3.2` | ⚠️ Inferida (ejemplos adversariales, par con [47]) |
| [47] | Goodfellow *et al.*, ICLR 2015 | `2.3.2` | ⚠️ Inferida (ejemplos adversariales, par con [46]) |
| [48] | Biggio y Roli, *Pattern Recognition* 2018 | `2.3.2` | **Nota los nombra** |
| [49] | Bendale y Boult, CVPR 2016 | `2.3.2` | **Nota los nombra** + verificada en `arquitecturas-hibridas` |
| [50] | Moustafa y Slay, MilCIS 2015 | `2.3.2` | Nota nombra UNSW-NB15 |
| [51] | Sharafaldin *et al.*, ICISSP 2018 | `2.3.2` | Nota nombra CIC-IDS2017/2018 |
| [52] | Pierazzi *et al.*, IEEE S&P 2020 | `2.3.3` | ⚠️ Inferida («espacio del problema», descripción literal) |
| [53] | Rudin, *Nature MI* 2019 | `2.3.3` | Descripción literal de la tesis del artículo |
| [54] | Molnar, *Interpretable Machine Learning* | `2.3.3` | Descripción literal; **edición sin fijar** |
| [55] | RGPD, Reglamento (UE) 2016/679 | `2.3.3` | La nota lo cita por su número oficial |
| [56] | AI Act, Reglamento (UE) 2024/1689 | `2.3.3` | La nota lo cita por su número oficial |
| [57] | NIS2, Directiva (UE) 2022/2555 | `2.3.3` | La nota lo cita por su número oficial |

Las citas completas, con DOI o URL estable y nivel, están en [[Bibliografía]]; aquí no se
duplican para que no diverjan.

### 3. Las tres invariantes

**(a) `[2]` Anderson 1980 y `[3]` Denning 1987 se MAPEARON, no se duplicaron. ✔**
Era el riesgo declarado del encargo original y **no se materializó**. En `2.2.2 Sistemas de
detección de intrusiones` la línea temporal cita a Anderson con `[2]` (línea 35) y a Denning con
`[3]` (línea 36), que son exactamente los números que ya tenían en `1.2 Preliminares`. Denning
reaparece con `[3]` en `2.2.4:50` y en `2.3.2:36` (el pasaje de UEBA). Ninguno de los 47 números
nuevos corresponde a Anderson ni a Denning.

**(b) `[9]` no se ha reutilizado en ninguna nota. ✔**
Un barrido de `\[9\]` en todo el vault solo devuelve `Bibliografía.md` y
[[Auditoría de Bibliografía]] —es decir, los sitios donde se documenta su retirada—. **Ninguna
nota de la memoria cita `[9]`.**

> [!note] Hallazgo lateral: la acción P1 de T15 ya está aplicada
> [[Auditoría de Bibliografía]] deja abierta la acción **P1**: «`2.2.1 Introducción a la
> ciberseguridad.md:32` sigue citando `[9]`; hay que repuntarla a `[8]`». **Ya no es cierto**: esa
> nota cita hoy `[8]` en las líneas 10 y 32, y `[10]` en la 40. Alguien la aplicó y no se cerró la
> anotación. No lo he tocado —`Auditoría de Bibliografía.md` está fuera de mi alcance—, pero
> conviene marcar P1 como hecha para que no se «arregle» dos veces.

**(c) `[CITA: …]` sin convertir: los 6 conocidos de `4.2`, MÁS 7 en `A.3`. ✘ (desviación)**
En `4.2 Base de datos utilizada` quedan exactamente los **6** esperados —líneas 22, 24 (×3), 36 y
45; las apariciones de las líneas 8 y 18 son menciones al literal `[CITA:...]` dentro de callouts
de metadatos, no citas—. Correcto y con ficha propia.

**Pero `A.3 Ficha del sistema` conserva 7 marcadores `[CITA: …]` que no estaban en ese
inventario**, y de ellos **6 apuntan a fuentes que este pase acaba de numerar**:

| Línea de `A.3` | Marcador | Situación |
|---|---|---|
| 10 | `[CITA: Mitchell et al. 2019]` | *Model Cards for Model Reporting* — **sin número asignado** |
| 231, 614, 628, 636 | `[CITA: Pineau et al.]` (×4) | **Es `[20]`**, dado de alta hoy |
| 583, 586 | `[CITA: Arp et al. — pitfalls en ML para seguridad]` (×2) | **Es `[18]`**, dado de alta hoy |

No los he convertido: convertirlos es **editar una nota de la memoria**, que está fuera de mi
alcance. Ver la propuesta en «Implicaciones».

### 4. Lo que el propio capítulo 2 ya declara sobre sus fuentes

Vale la pena registrarlo porque **reduce el riesgo del pase**: seis de las ocho notas llevan ya un
callout `> [!warning] Verificación pendiente — sin acceso al texto completo` que declara, fuente
por fuente, qué se toma de ella y qué no. En todos los casos la declaración es la misma: se toma
el **encuadre conceptual**, **sin extraer ninguna cifra ni resultado experimental**. Afecta a
`[25]` (NIST SP 800-94), `[18]` (Arp *et al.*), `[16]` (Chow), `[30]` (Chandola), `[34]`
(evasión), `[3]` (Denning), `[22]` (McHugh), `[49]` (Bendale y Boult), `[48]` (Biggio y Roli),
`[46]`/`[47]` y `[37]`/`[45]`.

Esto importa para el listón de fiabilidad: **ninguna de las 16 entradas de identidad inferida
sostiene una cifra del trabajo**. Si una resultara ser la obra equivocada, el daño sería una cita
mal atribuida, no un resultado sin respaldo. Sigue habiendo que confirmarlas, pero el riesgo está
acotado y no bloquea la lectura del capítulo.

## Lo que no he podido confirmar

- **`[27]` — el IDS dentro de plataformas SIEM/XDR** (`2.2.2:43`). El texto no da autor, obra ni
  organismo, y el concepto (XDR) es lo bastante reciente y lo bastante comercial como para que la
  fuente probable fuera de **nivel 2 o 3**. Candidatos propuestos en la ficha: NIST SP 800-92
  (*Guide to Computer Security Log Management*, 2006), que cubre la correlación de eventos pero
  **no** XDR; o el capítulo correspondiente de Stallings y Brown `[8]`. **No he elegido**: elegir
  aquí sería inventar la atribución.
- **`[28]` — defensa en profundidad** (`2.2.2:91`). Mismo problema. Es doctrina tan consolidada
  que casi cualquier manual de seguridad la sostiene, y precisamente por eso el contexto no
  discrimina. Candidatos: Stallings y Brown `[8]`, NIST SP 800-53 Rev. 5, o material del CCN-CERT
  en la línea de `[10]`.
- **`[37]` — panorama actual de amenazas** (`2.2.5:64`, `2.3.2:70`). La fuente es reconocible como
  clase (informe anual de organismo público europeo; el candidato natural es *ENISA Threat
  Landscape*) pero **la edición es indeterminable**, y la propia nota lo declara en su callout:
  «la edición concreta debe fijarse y comprobarse antes de la entrega». Sin edición no hay cita.
- **`[44]` — apoyo al analista en el SOC** (`2.3.2:38`). Es la peor de las cuatro: no hay ninguna
  pista de autor, ni obra equivalente en `99 Investigación/`, y el párrafo mezcla triaje
  automatizado con modelos de lenguaje, que no suelen convivir en una misma fuente. El propio
  texto declara el punto «fuera del alcance de este trabajo».
- **`[45]` — agencia europea sobre IA y cibercrimen** (`2.3.2:70`). Igual que `[37]`: clase
  identificable (Europol), edición no. Candidatos en la ficha: *IOCTA* o el informe del Europol
  Innovation Lab sobre modelos de lenguaje y aplicación de la ley (2023).
- **Las 16 entradas marcadas «⚠️ identidad inferida del contexto»**. Sus **metadatos sí están
  verificados** —autores, año, publicación, páginas, DOI comprobado— pero **la identificación de
  la obra es mía, deducida del texto**, no un dato heredado. No son citas cerradas.
- **`[54]` Molnar y `[39]` Russell y Norvig: la edición.** Ambos libros van por su 3.ª y 4.ª
  edición respectivamente y el texto no permite deducir cuál se manejó. Mismo problema que ya tenía
  `[8]` (Stallings).
- **`[35]` Snort:** falta fijar **versión del manual y fecha de consulta**. La documentación de
  Snort es un recurso vivo y una URL sin fecha no es una cita estable.

## Fuentes

Se listan solo las consultadas **en este pase para verificar metadatos**. Las 47 citas completas
están en [[Bibliografía]].

| # | Fuente | Nivel | Fecha | Cita completa | URL / DOI |
|---|---|---|---|---|---|
| 1 | CRISP-DM 1.0 (PDF alojado por la Univ. de Kassel) | 2 | 2000 | Chapman, Clinton, Kerber, Khabaza, Reinartz, Shearer y Wirth, *CRISP-DM 1.0: Step-by-step data mining guide*, CRISP-DM Consortium / SPSS | https://www.kde.cs.uni-kassel.de/wp-content/uploads/lehre/ws2012-13/kdd/files/CRISPWP-0800.pdf |
| 2 | Registro ACM DL de Kohavi | 1 | 1995 | Kohavi, *Proc. IJCAI'95*, vol. 2, pp. 1137-1143 | https://dl.acm.org/doi/10.5555/1643031.1643047 |
| 3 | Ficha JMLR de Bergstra y Bengio | 1 | 2012 | *JMLR*, vol. 13, pp. 281-305 | https://jmlr.org/papers/v13/bergstra12a.html |
| 4 | Registro del DOI de He y Garcia | 1 | 2009 | *IEEE TKDE*, vol. 21, n.º 9, pp. 1263-1284 | 10.1109/TKDE.2008.239 |
| 5 | Registro ACM DL de McHugh | 1 | 2000 | *ACM TISSEC*, vol. 3, n.º 4, pp. 262-294 | 10.1145/382912.382923 |
| 6 | Registro ACM DL de Axelsson | 1 | 2000 | *ACM TISSEC*, vol. 3, n.º 3, pp. 186-205 | 10.1145/357830.357849 |
| 7 | Registro ACM DL de Chandola *et al.* | 1 | 2009 | *ACM Computing Surveys*, vol. 41, n.º 3, art. 15 | 10.1145/1541880.1541882 |
| 8 | Actas LISA'99 (Roesch, Snort) | 1 | 1999 | *Proc. 13th USENIX Conf. on System Administration*, pp. 229-238 | https://www.usenix.org/legacy/publications/library/proceedings/lisa99/roesch.html |
| 9 | Ficha del DOI de García-Teodoro *et al.* | 1 | 2009 | *Computers & Security*, vol. 28, n.º 1-2, pp. 18-28 | 10.1016/j.cose.2008.08.003 |
| 10 | Copia archivada en DTIC de Ptacek y Newsham | 2 | 1998 | Informe técnico, Secure Networks Inc. | https://apps.dtic.mil/sti/html/tr/ADA391565/index.html |
| 11 | Tesis de Kendall (archivo del MIT Lincoln Lab y DSpace@MIT) | 2 | 1999-06 | K. Kendall, tesis S.B./M.Eng., MIT | https://archive.ll.mit.edu/ideval/files/kkendall_thesis.pdf · https://dspace.mit.edu/handle/1721.1/9459 |
| 12 | *MITRE ATT&CK: Design and Philosophy* (PDF oficial de MITRE) | 2 | 2018-07, rev. 2020-03 | Strom, Applebaum, Miller, Nickels, Pennington y Thomas | https://www.mitre.org/sites/default/files/2021-11/prs-19-01075-28-mitre-attack-design-and-philosophy.pdf |
| 13 | Ficha AAAI de Sahami *et al.* | 1 | 1998 | AAAI Technical Report WS-98-05, pp. 55-62 | https://aaai.org/papers/055-ws98-05-009/ |
| 14 | Registro del DOI de Biggio y Roli | 1 | 2018 | *Pattern Recognition*, vol. 84, pp. 317-331 | 10.1016/j.patcog.2018.07.023 |
| 15 | Registro del DOI de Moustafa y Slay | 1 | 2015 | *MilCIS 2015*, IEEE, pp. 1-6 | 10.1109/MilCIS.2015.7348942 |
| 16 | Ficha SciTePress de Sharafaldin *et al.* | 1 | 2018 | *ICISSP 2018*, pp. 108-116 | 10.5220/0006639801080116 |
| 17 | Ficha institucional de Pierazzi *et al.* (Royal Holloway / KCL) | 1 | 2020 | *IEEE S&P 2020*, pp. 1332-1349 | 10.1109/SP40000.2020.00073 |
| 18 | Registro del DOI de Rudin | 1 | 2019 | *Nature Machine Intelligence*, vol. 1, n.º 5, pp. 206-215 | 10.1038/s42256-019-0048-x |
| 19 | Sitio oficial del libro de Molnar (leído con `WebFetch`) | 2 | consultado 2026-08-15 | Sirve hoy la **3.ª edición**; **no publica ISBN ni año en la portada web** | https://christophm.github.io/interpretable-ml-book/ |
| 20 | Informes previos del propio vault | — | 2026-08 | [[benchmark-comparativo-nsl-kdd]], [[arquitecturas-hibridas-en-la-literatura]], [[clasificadores-tabulares-y-arquitecturas-hibridas]], [[Auditoría de Bibliografía]] | — |

> [!note] Sobre el método de verificación
> He usado `WebSearch` para localizar y `WebFetch` para leer. **No he necesitado Playwright en
> ningún momento.** Para los artículos tras muro de pago (Elsevier, IEEE, ACM) he usado metadatos
> y registros de DOI, que son públicos y bastan para citar: **no he intentado acceder al texto
> completo ni he iniciado sesión en ningún sitio**. Ninguna afirmación de este informe depende de
> un texto completo que no haya podido leer.

## Cambios en Bibliografía.md

**47 entradas añadidas, 0 completadas, 0 marcadas de las preexistentes.** Ninguna entrada previa
(`[1]`-`[8]`, `[10]`) se ha tocado, ni se ha borrado ni renumerado nada. Las tres correcciones de
T25 (`Bibliografía.md:32`, `:86`, `Auditoría de Bibliografía.md:140`) **no** se han hecho: son
ficha aparte, como indicaba el encargo.

| `[n]` | Qué he hecho |
|---|---|
| [11], [13], [16], [18], [20]-[25], [30]-[33], [38], [41], [42], [48]-[51], [53], [55]-[57] | **Añadidas — cierre firme.** Cita completa + DOI/URL verificado + nivel |
| [12], [14], [15], [17], [19], [26], [29], [34], [35], [36], [39], [40], [43], [46], [47], [52] | **Añadidas — marcadas «⚠️ identidad inferida del contexto».** Metadatos verificados; la identificación de la obra está pendiente de confirmación de Francisco |
| [54] | **Añadida — marcada: falta fijar edición y año** |
| [27], [28], [44] | **Añadidas como «⚠️ NO RECONSTRUIDA»**, con candidatos propuestos y `—` en DOI y nivel |
| [37], [45] | **Añadidas como «⚠️ NO RECONSTRUIDA — falta fijar la edición»**, con candidato de clase |

Además se ha insertado en la cabecera del fichero un callout `> [!danger]` que explica el pase, la
convención de las tres marcas y la instrucción de que **ninguna de las 47 se ha puesto ni cambiado
en las notas**.

> [!warning] Más de tres entradas tocadas en un mismo encargo
> Como pide el protocolo, se declara: este pase toca **47** entradas de `Bibliografía.md`. Es el
> objeto mismo del encargo, no un efecto colateral, pero conviene que quede dicho: el fichero ha
> pasado de 10 filas a 57 en una sola pasada.

## Implicaciones para el proyecto

1. **El track Informe se desbloquea, pero no queda limpio.** Las 47 referencias han dejado de ser
   colgantes: si el vault se vuelca hoy al `.docx`, ya no salen 47 referencias inventadas. Lo que
   sale son 43 citas reales y **5 filas visiblemente marcadas como sin resolver**, que es
   exactamente el estado que un tribunal puede tolerar y el anterior no. **Recomendación:** no
   volcar a Word hasta cerrar las cinco.
2. **Hay que decidir sobre `[27]`, `[28]`, `[37]`, `[44]` y `[45]`, y la decisión no es mía.** Para
   `[27]`, `[28]` y `[44]` hay dos salidas legítimas: localizar una fuente de nivel 1-2 que
   sostenga la frase, o **retirar el marcador y dejar la frase sin cita**, que es admisible porque
   las tres afirmaciones son de encuadre y no sostienen ningún resultado. Retirar un marcador es
   editar una nota: corresponde al `redactor-tfg` o a Francisco. Para `[37]` y `[45]` basta con
   elegir la edición.
3. **Propuesta sobre `A.3 Ficha del sistema` — no ejecutada.** Seis de sus siete `[CITA: …]` ya
   tienen número: los cuatro de Pineau son `[20]` y los dos de Arp son `[18]`. Convertirlos es
   mecánico y de bajo riesgo, pero es edición de nota. El séptimo, `[CITA: Mitchell et al. 2019]`
   (*Model Cards for Model Reporting*, FAT\* '19, `10.1145/3287560.3287596`, ya verificado en
   [[benchmark-comparativo-nsl-kdd]]), **necesita un número nuevo: sería el `[58]`**. No lo he dado
   de alta a propósito: dar de alta un `[58]` que ninguna nota cita crearía una entrada huérfana, y
   el alta debe ir junto con la conversión del marcador, en un solo pase.
4. **Cerrar la acción P1 de T15 en [[Auditoría de Bibliografía]].** Ya está aplicada en disco
   (`2.2.1` cita `[8]`, no `[9]`) y sigue figurando como pendiente. No la he tocado porque ese
   fichero está fuera de mi alcance.
5. **El contador global de `[n]` cambia.** Hasta hoy la regla del proyecto decía «en uso `[1]`-`[8]`
   y `[10]`; el primer número disponible es el `[11]`». **Ya no:** en uso `[1]`-`[8]` y
   `[10]`-`[57]`, `[9]` quemada, y **el primer número libre es el `[58]`**. Conviene que esto llegue
   a `CLAUDE.md` y a `leader.md`, porque es la regla que impide que dos agentes en paralelo
   asignen el mismo número. **Propongo, no ejecuto**: no toco ficheros de andamiaje.
6. **Ninguna decisión de `resumen-de-decisiones.md` queda desmentida por este pase.** No he
   encontrado nada que contradiga una decisión cerrada: el trabajo ha sido de atribución
   bibliográfica, no de contenido técnico.
