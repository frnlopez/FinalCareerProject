---
titulo: "Bibliografía"
numero: "-"
estado: borrador
docx_ref: "Desarrollo (referencias)"
---

# Bibliografía

> [!info] Tabla de *staging* — auditada el 2026-08-09 (T15)
> Este fichero **no es la bibliografía final**: es la tabla de trabajo desde la que Francisco hará
> el pase mecánico a Zotero en formato IEEE. Cada entrada lleva su **cita completa**, su **DOI o
> URL estable** y su **nivel de fiabilidad** a la vista, para que no se cuele una fuente de nivel
> 2-3 sosteniendo una afirmación fuerte.
>
> **Niveles:** **1** revisado por pares con DOI · norma o estándar · organismo oficial ·
> documentación oficial · libro con ISBN de editorial reconocida — cita sin reservas.
> **2** preprint, tesis, informe técnico de empresa, *white paper* — admisible declarando la
> reserva. **3** blog, prensa, web sin autor ni fecha, copia no autorizada — **no sostiene nada**.
>
> Informe de la auditoría: [[Auditoría de Bibliografía]].
> **La numeración no se reordena**: los `[n]` están usados en las notas. `[9]` queda retirada y su
> número **no se reutiliza**.

> [!danger] Reconstrucción de `[11]`-`[57]` — 2026-08-15
> Las 47 entradas de `[11]` a `[57]` se dieron de alta en un **pase de reparación**: los marcadores
> ya estaban puestos en las notas del capítulo 2 desde un pase anterior que murió antes de
> escribir aquí, de modo que la memoria arrastraba 47 referencias colgantes. El mapa `[n]` → fuente
> **no existía en ningún fichero** y se ha reconstruido leyendo el contexto de cada sitio de cita.
> Informe del pase: [[Reconstrucción de las 47 citas colgantes]].
>
> Por eso conviven tres grados de certeza, marcados **en la propia fila**:
> - **Sin marca** — la nota nombra a la fuente (autor, obra o pitfall) o la fuente ya estaba
>   verificada en `99 Investigación/`. Cita cerrada.
> - **⚠️ identidad inferida del contexto** — la obra es la candidata canónica para lo que el texto
>   afirma, y sus metadatos están verificados, **pero nadie ha confirmado que sea la que se
>   consultó**. Antes del pase a Zotero, Francisco debe confirmar cada una.
> - **⚠️ NO RECONSTRUIDA** — no se ha podido determinar la fuente. Son **cinco**: `[27]`, `[28]` y
>   `[44]`, sin pista alguna en el texto, y `[37]` y `[45]`, identificables como clase de documento
>   pero con la **edición indeterminable**. **No se ha inventado ninguna cita**: la fila lleva
>   candidatos propuestos y `—` en los campos que no se saben.
>
> **Ninguna de las 47 se ha puesto ni cambiado en las notas**: la numeración se toma como dada.

| `[n]` | Cita completa | DOI / URL estable | Nivel | Dónde se usa |
|---|---|---|---|---|
| [1] | Instituto Nacional de Ciberseguridad (INCIBE), «INCIBE presenta su balance de ciberseguridad 2024 con más de 97.000 incidentes gestionados», nota de prensa, 20 de marzo de 2025. **Dato citado:** 97.348 incidentes gestionados en 2024, un 16,6 % más que en 2023; 65.808 (67,6 %) afectaron a la ciudadanía y 31.540 (32,4 %) a empresas; 7.470 intrusiones o intentos de acceso no autorizado; 42.136 casos de *malware*, de ellos 357 de *ransomware* | https://www.incibe.es/incibe/sala-de-prensa/incibe-presenta-su-balance-de-ciberseguridad-2024-con-mas-de-97000-incidentes | **1** | `1.1 Motivación` |
| [2] | J. P. Anderson, *Computer Security Threat Monitoring and Surveillance*. Fort Washington, PA: James P. Anderson Co. (Box 42, Fort Washington, PA 19034), contrato 79F296400, 26 de febrero de 1980 (revisado el 15 de abril de 1980) | http://csrc.nist.gov/publications/history/ande80.pdf | **2** | `1.2 Preliminares` |
| [3] | D. E. Denning, «An Intrusion-Detection Model», *IEEE Transactions on Software Engineering*, vol. SE-13, n.º 2, pp. 222-232, feb. 1987 | 10.1109/TSE.1987.232894 | **1** | `1.2 Preliminares` |
| [4] | C. Chio y D. Freeman, *Machine Learning and Security: Protecting Systems with Data and Algorithms*, 1.ª ed. Sebastopol, CA: O'Reilly Media, 2018, 383 pp. ISBN 978-1-4919-7990-7 | ISBN 978-1-4919-7990-7 (sin DOI; sitio oficial del libro: https://mlsec.net/) | **1** | `2.1.1 Introducción al ML` |
| [5] | A. Géron, *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow: Concepts, Tools, and Techniques to Build Intelligent Systems*, 2.ª ed. Sebastopol, CA: O'Reilly Media, 2019. ISBN 978-1-492-03264-9 | https://www.oreilly.com/library/view/hands-on-machine-learning/9781492032632/ | **1** | `2.1.1 Introducción al ML`, `2.1.3 Ciclo de vida de un proyecto ML` |
| [6] | I. Goodfellow, Y. Bengio y A. Courville, *Deep Learning*. Cambridge, MA: MIT Press, 2016. ISBN 978-0-262-03561-3 | https://www.deeplearningbook.org/ | **1** | `2.1.2 Tipos de ML` |
| [7] | K. P. Murphy, *Machine Learning: A Probabilistic Perspective*. Cambridge, MA: MIT Press, 2012. ISBN 978-0-262-01802-9 | https://dl.acm.org/doi/book/10.5555/2380985 | **1** | `2.1.2 Tipos de ML` |
| [8] | W. Stallings y L. Brown, *Computer Security: Principles and Practice*, 4.ª ed. Pearson, 2018. ISBN 978-0-13-479410-5 | https://www.pearson.com/en-us/subject-catalog/p/computer-security-principles-and-practice/P200000010333 | **1** | `2.2.1 Introducción a la ciberseguridad` (definición de *Computer Security* y conceptos añadidos) |
| ~~[9]~~ | **RETIRADA el 2026-08-09 — fundida en [8]** (baja autorizada por Francisco el 2026-08-06) | — | ~~3~~ | ver aviso |
| [10] | Centro Criptológico Nacional (CCN-CERT), *Guía de Seguridad de las TIC CCN-STIC-401: Glosario y Abreviaturas*, entrada «ciberseguridad» | https://www.ccn-cert.cni.es/publico/seriesCCN-STIC/series/400-Guias_Generales/401-glosario_abreviaturas/index.html?n=189.html | **1** | `2.2.1 Introducción a la ciberseguridad` |
| [11] | P. Chapman, J. Clinton, R. Kerber, T. Khabaza, T. Reinartz, C. Shearer y R. Wirth, *CRISP-DM 1.0: Step-by-step data mining guide*. CRISP-DM Consortium / SPSS Inc., 2000 | https://www.kde.cs.uni-kassel.de/wp-content/uploads/lehre/ws2012-13/kdd/files/CRISPWP-0800.pdf | **2** | `2.1.6 Metodologías y buenas prácticas` (2.1.6.1, las seis fases) |
| [12] | T. Hastie, R. Tibshirani y J. Friedman, *The Elements of Statistical Learning: Data Mining, Inference, and Prediction*, 2.ª ed. Nueva York: Springer, 2009. ISBN 978-0-387-84857-0 · ⚠️ **identidad inferida del contexto** | 10.1007/978-0-387-84858-7 · https://hastie.su.domains/ElemStatLearn/ | **1** | `2.1.6` (2.1.6.2, error de generalización sobre datos no vistos) |
| [13] | R. Kohavi, «A Study of Cross-Validation and Bootstrap for Accuracy Estimation and Model Selection», en *Proc. 14th International Joint Conference on Artificial Intelligence (IJCAI'95)*, vol. 2, Morgan Kaufmann, 1995, pp. 1137-1143 | https://dl.acm.org/doi/10.5555/1643031.1643047 | **1** | `2.1.6` (2.1.6.3, validación cruzada K-fold) |
| [14] | scikit-learn, «`sklearn.model_selection.GridSearchCV`» — documentación oficial · ⚠️ **identidad inferida del contexto** (alternativa: F. Pedregosa *et al.*, «Scikit-learn: Machine Learning in Python», *JMLR*, vol. 12, pp. 2825-2830, 2011) | https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html | **1** | `2.1.6` (2.1.6.4, búsqueda exhaustiva en rejilla) |
| [15] | J. Bergstra e Y. Bengio, «Random Search for Hyper-Parameter Optimization», *Journal of Machine Learning Research*, vol. 13, pp. 281-305, 2012 | https://jmlr.org/papers/v13/bergstra12a.html | **1** | `2.1.6` (2.1.6.4, alternativa a la rejilla) |
| [16] | C. K. Chow, «On optimum recognition error and reject tradeoff», *IEEE Transactions on Information Theory*, vol. 16, n.º 1, pp. 41-46, ene. 1970 | 10.1109/TIT.1970.1054406 | **1** | `2.1.6` (2.1.6.4, regla de rechazo óptima) |
| [17] | S. Kapoor y A. Narayanan, «Leakage and the reproducibility crisis in machine-learning-based science», *Patterns*, vol. 4, n.º 9, art. 100804, 2023 · ⚠️ **identidad inferida del contexto** | 10.1016/j.patter.2023.100804 | **1** | `2.1.6` (2.1.6.5, fuga de información) |
| [18] | D. Arp, E. Quiring, F. Pendlebury, A. Warnecke, F. Pierazzi, C. Wressnegger, L. Cavallaro y K. Rieck, «Dos and Don'ts of Machine Learning in Computer Security», en *31st USENIX Security Symposium*, USENIX Association, 2022, pp. 3971-3988 | https://www.usenix.org/conference/usenixsecurity22/presentation/arp · preprint arXiv:2010.09470 | **1** | `2.1.6` (2.1.6.2, 2.1.6.5, 2.1.6.6), `2.3.3 Límites y consideraciones éticas` (P9, P10) |
| [19] | H. He y E. A. Garcia, «Learning from Imbalanced Data», *IEEE Transactions on Knowledge and Data Engineering*, vol. 21, n.º 9, pp. 1263-1284, sept. 2009 · ⚠️ **identidad inferida del contexto** | 10.1109/TKDE.2008.239 | **1** | `2.1.6` (2.1.6.6, aprendizaje con clases desequilibradas) |
| [20] | J. Pineau, P. Vincent-Lamarre, K. Sinha, V. Larivière, A. Beygelzimer, F. d'Alché-Buc, E. Fox y H. Larochelle, «Improving Reproducibility in Machine Learning Research (A Report from the NeurIPS 2019 Reproducibility Program)», *Journal of Machine Learning Research*, vol. 22, n.º 164, pp. 1-20, 2021 | https://www.jmlr.org/papers/v22/20-303.html | **1** | `2.1.6` (2.1.6.7, lista de comprobación de reproducibilidad), `A.3 Ficha del sistema` (como `[CITA: Pineau et al.]`) |
| [21] | R. Sommer y V. Paxson, «Outside the Closed World: On Using Machine Learning for Network Intrusion Detection», en *2010 IEEE Symposium on Security and Privacy*, Oakland, CA, 2010, pp. 305-316. Premio *Test of Time* IEEE S&P 2020 | 10.1109/SP.2010.25 | **1** | `2.1.6` (2.1.6.8 y definición de *semantic gap*), `2.2.3 Taxonomía de los IDS`, `2.3.2 La IA en ciberseguridad`, `2.3.3 Límites y consideraciones éticas` |
| [22] | J. McHugh, «Testing Intrusion Detection Systems: A Critique of the 1998 and 1999 DARPA Intrusion Detection System Evaluations as Performed by Lincoln Laboratory», *ACM Transactions on Information and System Security*, vol. 3, n.º 4, pp. 262-294, nov. 2000 | 10.1145/382912.382923 | **1** | `2.1.6` (2.1.6.8), `2.2.5 Taxonomía de ataques…`, `2.3.2`, `2.3.3` |
| [23] | M. Tavallaee, E. Bagheri, W. Lu y A. A. Ghorbani, «A Detailed Analysis of the KDD CUP 99 Data Set», en *Proc. 2nd IEEE Symposium on Computational Intelligence for Security and Defense Applications (CISDA)*, Ottawa, 2009, pp. 1-6 | 10.1109/CISDA.2009.5356528 · https://www.ee.torontomu.ca/~bagheri/papers/cisda.pdf | **1** | `2.1.6` (2.1.6.8), `2.2.5`, `2.3.2`, `2.3.3` |
| [24] | S. Axelsson, «The base-rate fallacy and the difficulty of intrusion detection», *ACM Transactions on Information and System Security*, vol. 3, n.º 3, pp. 186-205, ago. 2000 | 10.1145/357830.357849 | **1** | `2.1.6` (2.1.6.6), `2.2.4 Detección por firmas frente a…`, `2.3.3` |
| [25] | K. Scarfone y P. Mell, *Guide to Intrusion Detection and Prevention Systems (IDPS)*, NIST Special Publication 800-94. Gaithersburg, MD: National Institute of Standards and Technology, feb. 2007 | 10.6028/NIST.SP.800-94 | **1** | `2.2.2 Sistemas de detección de intrusiones` (2.2.2.1 y 2.2.2.3), `2.2.3`, `2.2.4` |
| [26] | M. Roesch, «Snort — Lightweight Intrusion Detection for Networks», en *Proc. 13th USENIX Conference on System Administration (LISA'99)*, Seattle, WA, 7-12 nov. 1999, USENIX Association, pp. 229-238 · ⚠️ **identidad inferida del contexto** | https://www.usenix.org/legacy/publications/library/proceedings/lisa99/roesch.html | **1** | `2.2.2` (2.2.2.2, generación *open source* basada en reglas) |
| [27] | ⚠️ **NO RECONSTRUIDA** — sostiene «el IDS como productor de eventos dentro de plataformas SIEM/XDR» en `2.2.2:43`. Candidatos propuestos, **ninguno confirmado**: K. Kent y M. Souppaya, *Guide to Computer Security Log Management*, NIST SP 800-92, 2006 (10.6028/NIST.SP.800-92); o el capítulo de correlación de eventos de Stallings y Brown [8]. **Decide Francisco** | — | — | `2.2.2` (2.2.2.2, actualidad) |
| [28] | ⚠️ **NO RECONSTRUIDA** — sostiene el principio de **defensa en profundidad** en `2.2.2:91`. Candidatos propuestos, **ninguno confirmado**: W. Stallings y L. Brown [8] (cap. 1); NIST SP 800-53 Rev. 5, *Security and Privacy Controls for Information Systems and Organizations*, 2020 (10.6028/NIST.SP.800-53r5); o material del CCN-CERT. **Decide Francisco** | — | — | `2.2.2` (2.2.2.5, defensa en profundidad) |
| [29] | P. García-Teodoro, J. Díaz-Verdejo, G. Maciá-Fernández y E. Vázquez, «Anomaly-based network intrusion detection: Techniques, systems and challenges», *Computers & Security*, vol. 28, n.º 1-2, pp. 18-28, feb. 2009 · ⚠️ **identidad inferida del contexto** | 10.1016/j.cose.2008.08.003 | **1** | `2.2.3` (2.2.3.2, modelo de lo normal) |
| [30] | V. Chandola, A. Banerjee y V. Kumar, «Anomaly detection: A survey», *ACM Computing Surveys*, vol. 41, n.º 3, art. 15, pp. 1-58, jul. 2009 | 10.1145/1541880.1541882 | **1** | `2.2.3` (2.2.3.2), `2.2.4` (deriva del perfil normal) |
| [31] | A. Khraisat, I. Gondal, P. Vamplew y J. Kamruzzaman, «Survey of intrusion detection systems: techniques, datasets and challenges», *Cybersecurity*, vol. 2, art. 20, 2019 | 10.1186/s42400-019-0038-7 | **1** | `2.2.3` (2.2.3.3, SIDS/AIDS y el párrafo único sobre híbridos) |
| [32] | D. Barbará, J. Couto, S. Jajodia y N. Wu, «ADAM: a testbed for exploring the use of data mining in intrusion detection», *ACM SIGMOD Record*, vol. 30, n.º 4, pp. 15-24, dic. 2001 | 10.1145/604264.604268 | **1** | `2.2.3` (antecedentes de la combinación anomalías + firmas) |
| [33] | E. Tombini, H. Debar, L. Mé y M. Ducassé, «A serial combination of anomaly and misuse IDSes applied to HTTP traffic», en *20th Annual Computer Security Applications Conference (ACSAC)*, IEEE, 2004, pp. 428-437 | 10.1109/CSAC.2004.4 | **1** | `2.2.3` (antecedentes de la cascada en serie) |
| [34] | T. H. Ptacek y T. N. Newsham, *Insertion, Evasion, and Denial of Service: Eluding Network Intrusion Detection*, informe técnico. Calgary: Secure Networks Inc., ene. 1998 · ⚠️ **identidad inferida del contexto** | https://apps.dtic.mil/sti/html/tr/ADA391565/index.html (copia archivada en DTIC) | **2** | `2.2.3` (2.2.3.4, técnicas de evasión) |
| [35] | Cisco / Snort Project, *Snort Users Manual* — sección «Writing Snort Rules» (documentación oficial) · ⚠️ **identidad inferida del contexto**; **falta fijar versión y fecha de consulta** | https://docs.snort.org/rules/ | **1** | `2.2.4` (2.2.4.1, ejemplo de regla) |
| [36] | K. Kendall, *A Database of Computer Attacks for the Evaluation of Intrusion Detection Systems*, tesis de máster (S.B./M.Eng.), Massachusetts Institute of Technology, jun. 1999 · ⚠️ **identidad inferida del contexto** (alternativa: R. Lippmann *et al.*, «Evaluating intrusion detection systems: the 1998 DARPA off-line intrusion detection evaluation», *DISCEX'00*, 2000, 10.1109/DISCEX.2000.821506) | https://archive.ll.mit.edu/ideval/files/kkendall_thesis.pdf · https://dspace.mit.edu/handle/1721.1/9459 | **2** | `2.2.5` (2.2.5.1, origen de las cuatro categorías) |
| [37] | ⚠️ **NO RECONSTRUIDA — falta fijar la edición.** Informe anual de panorama de amenazas de organismo público europeo. Candidato propuesto: ENISA, *ENISA Threat Landscape* (edición **por determinar**). El propio texto declara en `2.2.5:73-77` que la edición debe fijarse antes de la entrega y que no se cita ninguna cifra de ella. **Decide Francisco** | https://www.enisa.europa.eu/topics/cyber-threats/threats-and-trends (índice de la serie) | — | `2.2.5` (2.2.5.3), `2.3.2` (2.3.2.3) |
| [38] | B. E. Strom, A. Applebaum, D. P. Miller, K. C. Nickels, A. G. Pennington y C. B. Thomas, *MITRE ATT&CK®: Design and Philosophy*, informe técnico MITRE, jul. 2018 (rev. marzo 2020) · ⚠️ **identidad inferida del contexto** | https://www.mitre.org/sites/default/files/2021-11/prs-19-01075-28-mitre-attack-design-and-philosophy.pdf · matriz: https://attack.mitre.org/ | **2** | `2.2.5` (2.2.5.4, marco moderno de descripción de adversarios) |
| [39] | S. J. Russell y P. Norvig, *Artificial Intelligence: A Modern Approach*, 4.ª ed. Hoboken, NJ: Pearson, 2021. ISBN 978-0-13-461099-3 · ⚠️ **identidad inferida del contexto**; **falta confirmar la edición que maneja el autor** | https://aima.cs.berkeley.edu/ | **1** | `2.3.1 IA, ML y Deep Learning` (2.3.1.2, recorrido histórico) |
| [40] | A. Krizhevsky, I. Sutskever y G. E. Hinton, «ImageNet Classification with Deep Convolutional Neural Networks», en *Advances in Neural Information Processing Systems 25 (NIPS 2012)*, pp. 1097-1105 · ⚠️ **identidad inferida del contexto** | https://papers.nips.cc/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html · versión CACM: 10.1145/3065386 | **1** | `2.3.1` (2.3.1.2, ImageNet 2012) |
| [41] | L. Grinsztajn, E. Oyallon y G. Varoquaux, «Why do tree-based models still outperform deep learning on tabular data?», en *Advances in Neural Information Processing Systems 35 (NeurIPS 2022)*, Datasets and Benchmarks Track, 2022 | https://proceedings.neurips.cc/paper_files/paper/2022/file/0378c7692da36807bdec87ab043cdadc-Paper-Datasets_and_Benchmarks.pdf · preprint 10.48550/arXiv.2207.08815 | **1** | `2.3.1` (2.3.1.3, datos tabulares) |
| [42] | D. McElfresh, S. Khandagale, J. Valverde, V. Prasad C., G. Ramakrishnan, M. Goldblum y C. White, «When Do Neural Nets Outperform Boosted Trees on Tabular Data?», en *Advances in Neural Information Processing Systems 36 (NeurIPS 2023)*, Datasets and Benchmarks Track, 2023 | https://proceedings.neurips.cc/paper_files/paper/2023/hash/f06d5ebd4ff40b40dd97e30cee632123-Abstract-Datasets_and_Benchmarks.html | **1** | `2.3.1` (2.3.1.3, encaje con NSL-KDD) |
| [43] | M. Sahami, S. Dumais, D. Heckerman y E. Horvitz, «A Bayesian Approach to Filtering Junk E-Mail», en *Learning for Text Categorization: Papers from the 1998 AAAI Workshop*, AAAI Technical Report WS-98-05, 1998, pp. 55-62 · ⚠️ **identidad inferida del contexto** | https://aaai.org/papers/055-ws98-05-009/ · https://cdn.aaai.org/Workshops/1998/WS-98-05/WS98-05-009.pdf | **1** | `2.3.2` (2.3.2.1, filtros bayesianos anti-spam) |
| [44] | ⚠️ **NO RECONSTRUIDA** — sostiene el párrafo «Apoyo al analista en el SOC» (triaje, agrupación de alertas y modelos de lenguaje como asistentes) en `2.3.2:38`. **No hay ninguna pista de autor en el texto ni fuente equivalente en `99 Investigación/`.** El propio texto declara el punto fuera de alcance. **Decide Francisco**: o se localiza una revisión de nivel 1 sobre automatización del triaje en SOC, o se retira el marcador y la frase se deja sin cita | — | — | `2.3.2` (2.3.2.1, SOC) |
| [45] | ⚠️ **NO RECONSTRUIDA — falta fijar la edición.** Informe de agencia europea de aplicación de la ley sobre IA y cibercrimen. Candidatos propuestos: Europol, *Internet Organised Crime Threat Assessment (IOCTA)* (edición por determinar); o Europol Innovation Lab, *ChatGPT: The impact of Large Language Models on Law Enforcement*, 2023. El callout de `2.3.2:109` ya declara que la edición debe fijarse antes del pase a Zotero. **Decide Francisco** | https://www.europol.europa.eu/publications-events/publications | — | `2.3.2` (2.3.2.3, descenso de la barrera de entrada) |
| [46] | C. Szegedy, W. Zaremba, I. Sutskever, J. Bruna, D. Erhan, I. Goodfellow y R. Fergus, «Intriguing properties of neural networks», en *2nd International Conference on Learning Representations (ICLR 2014)*, 2014 · ⚠️ **identidad inferida del contexto** | https://arxiv.org/abs/1312.6199 · 10.48550/arXiv.1312.6199 | **1** | `2.3.2` (2.3.2.4, evasión / ejemplos adversariales) |
| [47] | I. J. Goodfellow, J. Shlens y C. Szegedy, «Explaining and Harnessing Adversarial Examples», en *3rd International Conference on Learning Representations (ICLR 2015)*, 2015 · ⚠️ **identidad inferida del contexto** | https://arxiv.org/abs/1412.6572 · 10.48550/arXiv.1412.6572 | **1** | `2.3.2` (2.3.2.4, evasión / ejemplos adversariales) |
| [48] | B. Biggio y F. Roli, «Wild patterns: Ten years after the rise of adversarial machine learning», *Pattern Recognition*, vol. 84, pp. 317-331, dic. 2018 | 10.1016/j.patcog.2018.07.023 | **1** | `2.3.2` (2.3.2.4, evasión y envenenamiento) |
| [49] | A. Bendale y T. E. Boult, «Towards Open Set Deep Networks» (OpenMax), en *2016 IEEE Conference on Computer Vision and Pattern Recognition (CVPR)*, 2016, pp. 1563-1572 | 10.1109/CVPR.2016.173 | **1** | `2.3.2` (2.3.2.5, reconocimiento de conjunto abierto) |
| [50] | N. Moustafa y J. Slay, «UNSW-NB15: a comprehensive data set for network intrusion detection systems (UNSW-NB15 network data set)», en *2015 Military Communications and Information Systems Conference (MilCIS)*, Canberra, 10-12 nov. 2015, IEEE, pp. 1-6 | 10.1109/MilCIS.2015.7348942 · https://research.unsw.edu.au/projects/unsw-nb15-dataset | **1** | `2.3.2` (tabla de datasets) |
| [51] | I. Sharafaldin, A. Habibi Lashkari y A. A. Ghorbani, «Toward Generating a New Intrusion Detection Dataset and Intrusion Traffic Characterization», en *Proc. 4th International Conference on Information Systems Security and Privacy (ICISSP)*, Funchal, 22-24 ene. 2018, SciTePress, pp. 108-116 | 10.5220/0006639801080116 · https://www.unb.ca/cic/datasets/ids-2017.html | **1** | `2.3.2` (tabla de datasets, CIC-IDS2017/2018) |
| [52] | F. Pierazzi, F. Pendlebury, J. Cortellazzi y L. Cavallaro, «Intriguing Properties of Adversarial ML Attacks in the Problem Space», en *2020 IEEE Symposium on Security and Privacy (S&P)*, 2020, pp. 1332-1349 · ⚠️ **identidad inferida del contexto** (el texto la describe como «la línea de trabajo sobre aprendizaje automático adversario en el espacio del problema») | 10.1109/SP40000.2020.00073 · preprint arXiv:1911.02142 | **1** | `2.3.3` (espacio de características frente a espacio del problema) |
| [53] | C. Rudin, «Stop explaining black box machine learning models for high stakes decisions and use interpretable models instead», *Nature Machine Intelligence*, vol. 1, n.º 5, pp. 206-215, 2019 | 10.1038/s42256-019-0048-x | **1** | `2.3.3` (interpretabilidad frente a explicación *a posteriori*) |
| [54] | C. Molnar, *Interpretable Machine Learning: A Guide for Making Black Box Models Explainable*. Edición del autor · ⚠️ **falta fijar la edición y el año**: la web oficial sirve hoy (consultada 2026-08-15) la **3.ª edición**; la más citada en la literatura es la 2.ª (2022) | https://christophm.github.io/interpretable-ml-book/ | **2** | `2.3.3` (sistematización del ML interpretable) |
| [55] | Parlamento Europeo y Consejo de la Unión Europea, *Reglamento (UE) 2016/679, de 27 de abril de 2016, relativo a la protección de las personas físicas en lo que respecta al tratamiento de datos personales y a la libre circulación de estos datos (RGPD)*, DOUE L 119, 4 de mayo de 2016, pp. 1-88 | http://data.europa.eu/eli/reg/2016/679/oj | **1** | `2.3.3` (2.3.3.5, marco normativo) |
| [56] | Parlamento Europeo y Consejo de la Unión Europea, *Reglamento (UE) 2024/1689, de 13 de junio de 2024, por el que se establecen normas armonizadas en materia de inteligencia artificial (Reglamento de Inteligencia Artificial)*, DOUE serie L, 12 de julio de 2024 | http://data.europa.eu/eli/reg/2024/1689/oj | **1** | `2.3.3` (2.3.3.5, marco normativo) |
| [57] | Parlamento Europeo y Consejo de la Unión Europea, *Directiva (UE) 2022/2555, de 14 de diciembre de 2022, relativa a las medidas destinadas a garantizar un elevado nivel común de ciberseguridad en toda la Unión (Directiva SRI 2 / NIS2)*, DOUE L 333, 27 de diciembre de 2022, pp. 80-152 | http://data.europa.eu/eli/dir/2022/2555/oj | **1** | `2.3.3` (2.3.3.5, marco normativo) |

## Avisos y reservas por entrada

> [!warning] [9] — retirada de la numeración, fundida en [8]
> Era `students.aiu.edu/.../j5V2a3_Computer_Security_Principles.pdf`: **copia no autorizada del
> mismo libro de Stallings que ya es [8]**, alojada en un dominio de terceros, sin garantía de
> integridad → **nivel 3**. Comprobado el 2026-08-09: el enlace **ya ni siquiera resuelve en
> abierto** (302 a `aiu.edu/securelogin.html`), así que tampoco era una URL estable.
> **Su número no se reutiliza** para no romper los `[n]` de las notas.
> **Acción pendiente, NO ejecutada por el researcher:** `2.2.1 Introducción a la
> ciberseguridad.md:32` sigue citando `[9]`; hay que **repuntarla a `[8]`**. Es una edición en una
> nota de la memoria y corresponde al `redactor-tfg` o a Francisco.

> [!warning] [8] — edición sin confirmar
> El libro se citaba **sin autor completo, sin año y sin editorial**. Completado con los
> metadatos verificados de la 4.ª edición (Pearson, 2018, ISBN 978-0-13-479410-5), que es la más
> difundida. **Existe una 5.ª edición: Pearson, 2023, ISBN impreso 978-0-13-809167-5**
> (e-book 978-0-13-809171-2). La definición citada en `2.2.1` (la de *computer security* tomada
> del NIST) aparece en el capítulo 1 de **todas** las ediciones, así que el texto no permite
> deducir cuál se usó, y la copia de [9] ya no es accesible para comprobarlo.
> **Francisco debe confirmar la edición que tiene delante antes del pase a Zotero.**
> Coautor añadido: **Lawrie Brown**, que faltaba.

> [!note] [2] — nivel 2, y qué sostiene exactamente
> Es un **informe técnico de empresa** (James P. Anderson Co.), no una publicación revisada por
> pares: **nivel 2**. Se cita como **fuente primaria histórica** y la copia enlazada la aloja el
> **NIST CSRC**, lo que da garantía de integridad. Portada verificada el 2026-08-09: título,
> contrato 79F296400, 26-02-1980 y revisión de 15-04-1980.
> **Reserva:** la frase de `1.2 Preliminares` «este informe se considera el punto de partida para
> los IDS» es una afirmación *sobre* el informe, que el propio informe no puede sostener.
> Necesita un aval de nivel 1 (una revisión del área). **Propuesta, no ejecutada.**

> [!note] [1] — sustituida (baja autorizada el 2026-08-06)
> Antes era `channelpartner.es` (**prensa sectorial, nivel 3**) sosteniendo una cifra de
> ciberataques. Sustituida por la **nota de prensa oficial de INCIBE** sobre el *Balance de
> ciberseguridad 2024* (nivel 1), con el dato exacto ya recogido en la tabla.
> **Reserva importante:** INCIBE da la **magnitud del fenómeno**, no los **nombres propios**
> (Santander, Telefónica, Iberdrola, UCM) que hoy aparecen en `1.1 Motivación:12`. Con esta
> fuente, la frase debe reformularse hacia la cifra agregada. **Propuesta, no ejecutada:** es
> edición de una nota de la memoria.

> [!note] [10] — organismo oficial, URL con protección anti-bot
> Nivel 1 por emisor (Centro Criptológico Nacional). El 2026-08-09 la URL devuelve **403/503 a
> cualquier acceso automático** (`ccn-cert.cni.es` filtra herramientas), igual que el espejo
> docente de la UPM. **No es un enlace roto**: es verificable a mano desde un navegador.
> **Sin verificar:** la **versión y la fecha** de la guía. Antes del pase a Zotero conviene citar
> la guía completa («CCN-STIC-401 Glosario y Abreviaturas», con su versión) en lugar del
> enlace profundo al término, que es frágil.

> [!warning] [6] — posible atribución equivocada, detectada de paso
> En `2.1.2 Tipos de ML.md:30` y `:64` se atribuyen a **Goodfellow et al.** dos listas
> (k-NN / regresión lineal / SVM / árboles / redes neuronales, y K-Means / DBSCAN / HCA /
> One-class SVM / Isolation Forest / PCA / Kernel PCA / LLE / t-SNE / Apriori / **Eclat**). Esas
> listas son las del **capítulo 1 de Géron [5]**; *Deep Learning* no trata Eclat, Apriori ni
> Isolation Forest. **Propuesta, no ejecutada:** repuntar esas dos citas a `[5]`. No es una baja
> de bibliografía, es una corrección de puntero en una nota de la memoria.
