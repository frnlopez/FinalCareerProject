UNIVERSIDAD DE MÁLAGA

ESCUELA TÉCNICA SUPERIOR DE

INGENIERÍA DE TELECOMUNICACIÓN

TRABAJO FIN DE GRADO

SISTEMA HÍBRIDO DE DETECCIÓN DE INTRUSIONES EN RED BASADO EN MACHINE LEARNING

GRADO EN INGENIERÍA DE

SISTEMAS DE TELECOMUNICACIÓN

FRANCISCO JOSÉ LÓPEZ MORENO

MÁLAGA, 2026

[E.T.S. de Ingeniería de Telecomunicación, Universidad de Málaga]{.smallcaps}

**Título del Trabajo Fin de Grado**

Autor: Francisco José López Moreno

Tutor: Jorge Munilla Fajardo

Departamento: Ingeniería de Comunicaciones (IC)

Titulación: Grado en Ingeniería de Sistemas de Telecomunicación

Palabras clave: Palabras y frases claves que describen y caracterizan el tema del trabajo

**Resumen**

El resumen debe ser una breve descripción del contexto del proyecto, sus objetivos y los resultados obtenidos. Se recomienda que no exceda esta página.

[E.T.S. de Ingeniería de Telecomunicación, Universidad de Málaga]{.smallcaps}

**English version of the title**

Author: Francisco José López Moreno

Supervisor: Jorge Munilla Fajardo

Department: Ingeniería de Comunicaciones (IC)

Degree: Grado en Ingeniería de Sistemas de Telecomunicación

Keywords: English keywords

**Abstract**

The abstract should contain a brief description of the context of the project, the objectives and its main results.

Agradecimientos

Este apartado es opcional. En él se incluirían los agradecimientos personales y profesionales. Si no los hubiere, debe eliminarse esta página y la siguiente.

*En esta parte se coloca la*

*dedicatoria, si la hubiere\...*

# Contenido {#contenido .Título-de-TDC}

[Capítulo 1. Introducción [1](#introducción)](#introducción)

[1.1. Motivación [1](#motivación)](#motivación)

[1.2. Preliminares [2](#preliminares)](#preliminares)

[1.3. Objetivo [3](#objetivo)](#objetivo)

[1.4. Estructura [4](#estructura)](#estructura)

[Capítulo 2. Marco Teórico [5](#marco-teórico)](#marco-teórico)

[2.1. Machine Learning [5](#machine-learning)](#machine-learning)

[2.1.1. Introducción al Machine Learning [5](#introducción-al-machine-learning)](#introducción-al-machine-learning)

[2.1.2. Tipos de ML [9](#tipos-de-ml)](#tipos-de-ml)

[2.1.3. Etapas del Ciclo de vida de un proyecto de ML [12](#etapas-del-ciclo-de-vida-de-un-proyecto-de-ml)](#etapas-del-ciclo-de-vida-de-un-proyecto-de-ml)

[2.1.4. Algoritmos de ML [14](#algoritmos-de-ml)](#algoritmos-de-ml)

[Algoritmos Supervisados [14](#_Toc236498676)](#_Toc236498676)

[Algoritmos no Supervisados [17](#_Toc236498677)](#_Toc236498677)

[2.1.5. Métricas de evaluación de modelos [18](#métricas-de-evaluación-de-modelos)](#métricas-de-evaluación-de-modelos)

[Para algoritmos de clasificación tenemos las siguientes métricas: [18](#_Toc236498679)](#_Toc236498679)

[2.2. Ciberseguridad [20](#ciberseguridad)](#ciberseguridad)

[2.2.1. Introducción a la ciberseguridad [20](#introducción-a-la-ciberseguridad)](#introducción-a-la-ciberseguridad)

[2.2.2. Sistemas de detección de intrusiones [23](#sistemas-de-detección-de-intrusiones)](#sistemas-de-detección-de-intrusiones)

[2.2.3. Taxonomía de los IDS [23](#taxonomía-de-los-ids)](#taxonomía-de-los-ids)

[2.2.4. Detección por firmas frente a detección por anomalías [23](#detección-por-firmas-frente-a-detección-por-anomalías)](#detección-por-firmas-frente-a-detección-por-anomalías)

[2.2.5. Taxonomía de ataques y panorama de amenazas [23](#taxonomía-de-ataques-y-panorama-de-amenazas)](#taxonomía-de-ataques-y-panorama-de-amenazas)

[2.3. Inteligencia Artificial [23](#inteligencia-artificial)](#inteligencia-artificial)

[2.3.1. IA, ML y Deep Learning [23](#ia-ml-y-dl)](#ia-ml-y-dl)

[2.3.2. La IA en Ciberseguridad [23](#la-ia-en-ciberseguridad)](#la-ia-en-ciberseguridad)

[2.3.3. Límites y consideraciones éticas [23](#límites-y-consideraciones-éticas)](#límites-y-consideraciones-éticas)

[Capítulo 3. Diseño del sistema [24](#diseño-del-sistema)](#diseño-del-sistema)

[3.1. Requisitos del sistema [24](#requisitos-del-sistema)](#requisitos-del-sistema)

[3.1.1. Requisitos funcionales [24](#requisitos-funcionales)](#requisitos-funcionales)

[3.1.2. Requisitos de datos [25](#requisitos-de-datos)](#requisitos-de-datos)

[3.1.3. Requisitos no funcionales [25](#requisitos-no-funcionales)](#requisitos-no-funcionales)

[3.1.4. Requisito de alcance [25](#requisito-de-alcance)](#requisito-de-alcance)

[3.2. Arquitectura del sistema [26](#arquitectura-del-sistema)](#arquitectura-del-sistema)

[3.2.1. Las dos etapas [26](#las-dos-etapas)](#las-dos-etapas)

[3.2.2. Por qué una cascada, y en este orden [27](#_Toc236498698)](#_Toc236498698)

[3.2.3. De dónde sale la capacidad de detectar lo desconocido [27](#_Toc236498699)](#_Toc236498699)

[3.3. Metodología de funcionamiento del sistema [28](#metodología-de-funcionamiento-del-sistema)](#metodología-de-funcionamiento-del-sistema)

[3.3.1. Diseño de los subconjuntos [28](#diseño-de-los-subconjuntos)](#diseño-de-los-subconjuntos)

[3.3.2. Donde se ajusta la normalización [29](#_Toc236498702)](#_Toc236498702)

[3.3.3. Recorrido de un flujo por la cascada [29](#_Toc236498703)](#_Toc236498703)

[3.3.4. Protocolo de evaluación común [30](#protocolo-de-evaluación-común)](#protocolo-de-evaluación-común)

[3.4. Modelo de detección de anomalías [31](#modelo-de-detección-de-anomalías)](#modelo-de-detección-de-anomalías)

[3.4.1. Planteamiento [31](#planteamiento)](#planteamiento)

[3.4.2. Algoritmos candidatos [31](#algoritmos-candidatos)](#algoritmos-candidatos)

[3.4.3. Diseño del umbral de decisión [32](#diseño-del-umbral-de-decisión)](#diseño-del-umbral-de-decisión)

[3.4.4. Papel en la cascada [33](#papel-en-la-cascada)](#papel-en-la-cascada)

[3.5. Modelo de detección basado en firmas [33](#modelo-de-detección-basado-en-firmas)](#modelo-de-detección-basado-en-firmas)

[3.5.1. Planteamiento [33](#planteamiento-1)](#planteamiento-1)

[3.5.2. Algoritmos candidatos [33](#algoritmos-candidatos-1)](#algoritmos-candidatos-1)

[3.5.3. Firmas interpretables [34](#firmas-interpretables)](#firmas-interpretables)

[3.5.4. Tratamiento del desbalance como decisión de diseño [34](#tratamiento-del-desbalance-como-decisión-de-diseño)](#tratamiento-del-desbalance-como-decisión-de-diseño)

[3.5.5. Papel en la cascada y salida "desconocido" [35](#papel-en-la-cascada-y-salida-desconocido)](#papel-en-la-cascada-y-salida-desconocido)

[3.6. Conclusiones del capítulo [36](#conclusiones-del-capítulo)](#conclusiones-del-capítulo)

[Capítulo 4. Implementación del sistema [38](#implementación-del-sistema)](#implementación-del-sistema)

[4.1. Tecnologías utilizadas [38](#tecnologías-utilizadas)](#tecnologías-utilizadas)

[4.1.1. Entorno y aplicaciones [38](#entorno-y-aplicaciones)](#entorno-y-aplicaciones)

[4.1.2. Lenguaje de programación [38](#lenguaje-de-programación)](#lenguaje-de-programación)

[4.1.3. Librerías de Python [39](#librerías-de-python)](#librerías-de-python)

[4.2. Base de datos utilizada [41](#base-de-datos-utilizada)](#base-de-datos-utilizada)

[4.2.1. Análisis previo de la base de datos [44](#análisis-previo-de-la-base-de-datos)](#análisis-previo-de-la-base-de-datos)

[4.3. Preprocesamiento de los datasets [49](#preprocesamiento-de-los-datasets)](#preprocesamiento-de-los-datasets)

[4.3.1. Adición y eliminación de etiquetas [50](#adición-y-eliminación-de-etiquetas)](#adición-y-eliminación-de-etiquetas)

[4.3.2. Normalización de variables numéricas [53](#normalización-de-variables-numéricas)](#normalización-de-variables-numéricas)

[4.3.3. Codificación de variables categóricas [55](#codificación-de-variables-categóricas)](#codificación-de-variables-categóricas)

[4.3.4. Equilibrio y balanceo de muestras [56](#equilibrio-y-balanceo-de-muestras)](#equilibrio-y-balanceo-de-muestras)

[4.3.5. Selección de características [59](#selección-de-características)](#selección-de-características)

[4.3.6. División del conjunto de datos [63](#división-del-conjunto-de-datos)](#división-del-conjunto-de-datos)

[4.4. Entrenamiento del modelo de detección de anomalías [66](#entrenamiento-del-modelo-de-detección-de-anomalías)](#entrenamiento-del-modelo-de-detección-de-anomalías)

[4.4.1. Protocolo de entrenamiento y validación [66](#protocolo-de-entrenamiento-y-validación)](#protocolo-de-entrenamiento-y-validación)

[4.4.2. Algoritmos y espacios de búsqueda [68](#algoritmos-y-espacios-de-búsqueda)](#algoritmos-y-espacios-de-búsqueda)

[4.4.3. Configuraciones ganadoras [69](#configuraciones-ganadoras)](#configuraciones-ganadoras)

[4.5. Entrenamiento del modelo de detección basado en firmas [70](#entrenamiento-del-modelo-de-detección-basado-en-firmas)](#entrenamiento-del-modelo-de-detección-basado-en-firmas)

[4.5.1. Protocolo de entrenamiento [71](#protocolo-de-entrenamiento)](#protocolo-de-entrenamiento)

[4.5.2. Algoritmos y espacios de búsqueda [72](#algoritmos-y-espacios-de-búsqueda-1)](#algoritmos-y-espacios-de-búsqueda-1)

[4.5.3. Configuraciones ganadoras [72](#configuraciones-ganadoras-1)](#configuraciones-ganadoras-1)

[4.5.4. Extracción de firmas legibles [73](#extracción-de-firmas-legibles)](#extracción-de-firmas-legibles)

[4.6. Conclusiones del capítulo [77](#conclusiones-del-capítulo-1)](#conclusiones-del-capítulo-1)

[4.6.1. Un pipeline reproducible de principio a fin [77](#un-pipeline-reproducible-de-principio-a-fin)](#un-pipeline-reproducible-de-principio-a-fin)

[4.6.2. Decisiones de preprocesado justificadas con datos, no por defecto [77](#decisiones-de-preprocesado-justificadas-con-datos-no-por-defecto)](#decisiones-de-preprocesado-justificadas-con-datos-no-por-defecto)

[4.6.3. La ausencia de fuga de información como principio transversal [78](#la-ausencia-de-fuga-de-información-como-principio-transversal)](#la-ausencia-de-fuga-de-información-como-principio-transversal)

[4.6.4. Comparación amplia bajo protocolo común [78](#comparación-amplia-bajo-protocolo-común)](#comparación-amplia-bajo-protocolo-común)

[Capítulo 5. Evaluación [79](#evaluación)](#evaluación)

[5.1. Resultados del modelo de detección de anomalías [79](#resultados-del-modelo-de-detección-de-anomalías)](#resultados-del-modelo-de-detección-de-anomalías)

[5.1.1. Matrices de confusión [80](#matrices-de-confusión)](#matrices-de-confusión)

[5.1.2. Métricas de desempeño [83](#métricas-de-desempeño)](#métricas-de-desempeño)

[5.1.3. Resultados finales [86](#resultados-finales)](#resultados-finales)

[5.2. Resultados del modelo de detección basado en firmas [87](#resultados-del-modelo-de-detección-basado-en-firmas)](#resultados-del-modelo-de-detección-basado-en-firmas)

[5.2.1. Matrices de confusión [87](#matrices-de-confusión-1)](#matrices-de-confusión-1)

[5.2.2. Métricas de desempeño [91](#métricas-de-desempeño-1)](#métricas-de-desempeño-1)

[5.2.3. Comparación de los resultados de cada algoritmo [93](#comparación-de-los-resultados-de-cada-algoritmo)](#comparación-de-los-resultados-de-cada-algoritmo)

[5.3. Resultados del sistema híbrido [94](#resultados-del-sistema-híbrido)](#resultados-del-sistema-híbrido)

[5.4. Conclusiones del capítulo [103](#conclusiones-del-capítulo-2)](#conclusiones-del-capítulo-2)

[Capítulo 6. Conclusiones [107](#conclusiones)](#conclusiones)

[6.1. Conclusiones [107](#conclusiones-1)](#conclusiones-1)

[6.1.1. Grado de cumplimiento de los objetivos [108](#grado-de-cumplimiento-de-los-objetivos)](#grado-de-cumplimiento-de-los-objetivos)

[6.1.2. Validación de la tesis del híbrido [109](#validación-de-la-tesis-del-híbrido)](#validación-de-la-tesis-del-híbrido)

[6.1.3. Limitaciones [109](#limitaciones)](#limitaciones)

[6.2. Líneas futuras [111](#líneas-futuras)](#líneas-futuras)

[Apéndice A. Columnas del dataset NSL-KDD [111](#columnas-del-dataset-nsl-kdd)](#columnas-del-dataset-nsl-kdd)

[A.1. Columnas del dataset NSL-KDD [111](#columnas-del-dataset-nsl-kdd-1)](#columnas-del-dataset-nsl-kdd-1)

[A.1.1. Características básicas (1--9) [112](#características-básicas-19)](#características-básicas-19)

[A.1.2. Características de contenido (10--22) [112](#características-de-contenido-1022)](#características-de-contenido-1022)

[A.1.3. Características de tráfico basadas en tiempo (23--31) [114](#características-de-tráfico-basadas-en-tiempo-2331)](#características-de-tráfico-basadas-en-tiempo-2331)

[A.1.4. Características de tráfico basadas en host (32--41) [114](#características-de-tráfico-basadas-en-host-3241)](#características-de-tráfico-basadas-en-host-3241)

[A.1.5. Etiquetas: tipos de ataque y categorías [115](#etiquetas-tipos-de-ataque-y-categorías)](#etiquetas-tipos-de-ataque-y-categorías)

[A.2. Métricas de desempeño [117](#métricas-de-desempeño-2)](#métricas-de-desempeño-2)

[Bibliografía [118](#_Toc236498770)](#_Toc236498770)

[Apéndice B. Nombre del apéndice A [120](#nombre-del-apéndice-a)](#nombre-del-apéndice-a)

[B.1. Este texto está escrito en estilo Título 7. Es el equivalente a Título 2 para los apéndices [120](#este-texto-está-escrito-en-estilo-título-7.-es-el-equivalente-a-título-2-para-los-apéndices)](#este-texto-está-escrito-en-estilo-título-7.-es-el-equivalente-a-título-2-para-los-apéndices)

[B.1.1. Este texto está escrito en estilo Título 8. Es el equivalente a Título 3 para los apéndices. [120](#este-texto-está-escrito-en-estilo-título-8.-es-el-equivalente-a-título-3-para-los-apéndices.)](#este-texto-está-escrito-en-estilo-título-8.-es-el-equivalente-a-título-3-para-los-apéndices.)

[Bibliografía [123](#_Toc236498774)](#_Toc236498774)

Lista de Acrónimos

**ML Machine Learning**

**IA Inteligencia Artificial**

**DL Deep Learning**

**IDS Intrusion Detection System**

**NIDS Network Intrusion Detection System**

**H-NIDS Hybrid Network Intrusion Detection System**

# Introducción

En este primer punto vamos a poner en contexto el proyecto. Primero, explicando un poco de historia del sistema que queremos construir en el mismo y como empezaron las primeras versiones de los Sistemas de Detección de Intrusiones (IDS), y como trabajan actualmente. Además de estructurar los objetivos generales y específicos del proyecto, y situarlos en cada uno de los capítulos que va a tener esta memoria.

## Motivación

La ciberseguridad y la inteligencia artificial (IA) dominan los titulares a diario. Ciberataques, nuevos modelos de IA, la capacidad de esta para transformar el mercado laboral y los puestos de trabajo actuales, son titulares a los que cada vez estamos más acostumbrados. En este contexto, la vulnerabilidad de los datos y de las infraestructuras se ha convertido en una de las mayores preocupaciones de las grandes empresas.

La posibilidad de sufrir estos problemas no se limita a grandes corporaciones únicamente, sino que cualquier institución puede verse afectada. El banco Santander, Telefónica, Iberdrola o la Universidad Complutense de Madrid son algunos de los grandes nombres españoles que han sufrido estas filtraciones de datos debidas a ciberataques **\[1\]**.

Todos estos motivos son los que han puesto la ciberseguridad, y por consecuente, la protección de datos, en el centro de prioridades para todos los profesionales informáticos.

Por otro lado, la IA ha tenido un crecimiento exponencial en los últimos años y el uso de esta se extiende a todos los ámbitos de la sociedad. De hecho, todas las grandes multinacionales están invirtiendo en esta tecnología y cada vez son más los puestos de trabajo que se están transformando debido a estas innovaciones, además de todas las nuevas innovaciones que presentan y la infinitud de aplicaciones que pueden llegar a tener en las organizaciones, ayudando a las mismas a centrar sus esfuerzos en tareas a más alto nivel.

En cuestión al objetivo de este proyecto, los Sistemas de Detección de Intrusiones en Red (NIDS) en general también se han visto beneficiados por esta nueva corriente. Se han creado algoritmos basados tanto en Machine Learning (ML) como en IA, que mejoran la capacidad de detección de ataques y a que cada vez sea más fácil detectar un ataque al producirse. Además, estos sistemas permiten relacionar un ataque actual con incidentes previos, haciendo posible el uso del método de resolución usado anteriormente.

De igual modo, estos algoritmos han sido fundamentales para la detección de ataques desconocidos, denominados **ataques 0-day**. Aunque estos algoritmos no son totalmente fiables, sus resultados son altamente prometedores.

## Preliminares

La historia de los IDS comienza con la creciente complejidad de las redes informáticas y la necesidad de proteger la información.

En la década de los 80 dos investigadores dieron los primeros fundamentos sobre la detección de intrusiones:

-   Fue primero James P. Anderson, en el 1980, quien publicó un informe titulado \"Computer Security Threat Monitoring and Surveillance\". En dicho documento se hablaba de como los patrones de uso del usuario y del sistema podían ser trackeados con el objetivo de detectar actividades maliciosas. Este informe se considera el punto de partida para los IDS **\[2\]**.

-   Posteriormente, Dorothy Denning, una investigadora americana, desarrolló el modelo IDES (Intrusion Detection Expert System) en el instituto SRI Internacional (Stanford Research Institute). IDES fue uno de los primeros prototipos de IDS, el cual se basaba en la monitorización del uso normal del usuario y del sistema, con el objetivo de detectar anomalías, clasificando dichas actividades anómalas como intrusiones **\[3\]**.

Años más tarde, en 1998, Martin Roesch creó **Snort**, un detector de intrusiones ligero y de código abierto, el cual podía realizar análisis de protocolos, búsqueda de contenido y coincidencia de patrones. Él fue quien popularizó la detección basada en firma, donde el NIDS busca patrones específicos (firmas) en el tráfico de red que se sabe que corresponden a ataques conocidos \[11\].

Además, se creó otro método más, el de detección basada en el estado. Este último monitorea las sesiones de red, con el objetivo de detectar anomalías en el flujo de comunicación. 

En el siglo XXI, todos estos sistemas se han convertido en esenciales de cara a la seguridad informática, pero a medida que evolucionan, también se encuentran desafíos a los que enfrentarse, como:

-   Evasión del IDS/NIDS -- el atacante conoce el mecanismo de detección y lo esquiva.

-   Volumen de datos -- miles de flujos por segundo, el detector debe decidir en tiempo real.

-   Falsos Positivos/Negativos -- un umbral demasiado permisivo deja pasar ataques; y uno demasiado estricto inunda al analista de falsas alarmas.

-   Integración con SIEM (Sistemas de Gestión de Información y Eventos de Seguridad).

-   IDS Híbridos y nuevas Tecnologías.

Este último punto es precisamente el que motiva el presente trabajo.

## Objetivo

***Objetivos generales***

Diseñar, implementar y evaluar un Sistema de Detección de Intrusiones Híbrido en Red (H-NIDS) basado en técnicas de aprendizaje automático, aplicado al conjunto de datos NSL-KDD.

Lo que el trabajo se propone demostrar es que si esa composición en cascada de dos modelos (explicados posteriormente) aportan algo medible frente a las alternativas obvias: cada etapa por separado o un clasificador monolítico.

***Objetivos específicos***

-   Estudiar los dos métodos principales en los que se basará este sistema, la Detección de Firmas para ataques conocidos y la Detección de Anomalías para ataques 0-day.

-   Revisar la estructura del dataset NSL-KDD, el cual va a usar el sistema, para su posterior preprocesamiento y estructuración con el uso de técnicas de ML.

-   Analizar los posibles algoritmos de ML a utilizar y sus diferentes aportaciones a los modelos a entrenar.

-   Entrenar los modelos de ML con los distintos subgrupos del dataset estructurado y validar los modelos entrenados.

-   Estudiar los resultados obtenidos tras la integración de ambas etapas, validando los resultados y midiendo la capacidad de detección de ataques desconocidos.

-   Contrastar el rendimiento del híbrido frente a un baseline monolítico de control.

## Estructura

Esta memoria describe paso a paso el proceso seguido: la preparación de fundamentos, el estudio de los procesos y técnicas utilizados, el diseño y la implementación de los modelos, y la evaluación final del sistema. Cada capítulo es un escalón hacia el objetivo final.

El Capítulo 1 consiste en la **Introducción**. En este capítulo se recorren los antecedentes históricos de los IDS, para entender de donde viene el problema. Su aportación consiste en delimitar la pregunta que el resto del trabajo debe responder.

E Capítulo 2, **Marco Teórico**, repasamos los conceptos básicos necesarios para la implementación. Estos conceptos se dividen en tres bloques, ML, IA y Ciberseguridad. Su aportación es justificar por qué la combinación de ambos paradigmas de detección es una vía razonable.

El Capítulo 3, **Diseño del sistema**, recoge los requisitos, la arquitectura en cascada, la metodología del funcionamiento y el diseño de las dos etapas del sistema. Su aportación es dejar cerradas todas las decisiones de diseño antes de la implementación.

El Capítulo 4, **Implementación del sistema**, detalla como se materializa el diseño. Describe las tecnologías utilizadas, el dataset NSL-KDD y su análisis previo. Su aportación es la trazabilidad: documenta cada paso con el detalle suficiente para que el sistema sea reproducible.

El Capítulo 5, **Evaluación**, presenta y analiza los resultados de los experimentos. Se fija primero el protocolo de evaluación, y se exponen los resultados tanto de los modelos por separado como del sistema híbrido.

Además, también se presenta el contraste con un **baseline monolítico de control** (un único clasificador multiclase entrenado sobre todo el tráfico, que nos permite afirmar o descartar que la arquitectura en cascada aporta una mejora o no) y el **análisis del *recall* de ataques desconocidos desagregado por tipo de ataque**, en lugar de una métrica global que oculte el comportamiento real frente a las categorías minoritarias. Su aportación es la evidencia.

El capítulo 6, **Conclusiones**, cierra el trabajo. Contrasta los resultados obtenidos con los objetivos del trabajo. Su aportación es el juicio final.

Por último, los **Apéndices** reúnen el material de consulta que apoya a los capítulos anteriores: se muestran datos que harían compleja la lectura del informe, además de no tener una aportación real durante la misma. Cierra la memoria la **Bibliografía**.

# Marco Teórico

## Machine Learning

### Introducción al Machine Learning

Desde los inicios de la era tecnológica, los investigadores han perseguido enseñar a las computadoras a razonar y tomar decisiones «inteligentes» de la misma manera que lo hacen los seres humanos, mediante la elaboración de generalizaciones y la extracción de conceptos a partir de conjuntos de información complejos sin instrucciones explícitas.

El ML se refiere a un aspecto de este objetivo, concretamente a los algoritmos y procesos que «aprenden» en el sentido de que son capaces de generalizar datos y experiencias pasadas para predecir resultados futuros. En esencia, el ML es un conjunto de técnicas matemáticas, implementadas en sistemas informáticos, que permiten un proceso de extracción de información, descubrimiento de patrones y obtención de inferencias a partir de datos.

El ML se enmarca dentro de la IA y guarda una relación estrecha con el DL, tal y como se ilustra en la Figura 1.1. El ML es uno de los caminos, aunque no el único, para construir sistemas de IA, y el DL es a su vez un subconjunto estricto del ML \[4\].

![](Resultados/docx/COMPARACION/media/media/image1.png)

Figura 1.1. Relación entre Inteligencia Artificial, Machine Learning y Deep Learning.

La diferencia entre la programación tradicional y el ML se ve clara en estos diagramas. Mientras que el primero debe definir unas reglas para evaluar, el otro aprende esas reglas a partir de datos y evaluaciones previas, para definir un sistema capaz de evaluar por sí mismo.

El proceso tradicional consiste en que el desarrollador escribe las reglas de decisión y, si no bastan, analiza los errores para corregirlas a mano \[Figura 1.2\].

![](Resultados/docx/COMPARACION/media/media/image2.png)

> Figura 1.2. Metodología en programación tradicional.

En el ML, tomamos datos de evaluaciones previas, entrenamos un algoritmo sobre ellos y lo evaluamos. Si el desempeño del modelo resultante no es satisfactorio, el propio entrenamiento del algoritmo es el que corrige \[Figura 1.3\].

![](Resultados/docx/COMPARACION/media/media/image3.png)

Figura 1.3. Metodología en ML.

Además, podríamos conseguir un modelo más completo haciendo que, una vez desplegado, aprendiera de los nuevos datos que está generando, es decir, de las nuevas evaluaciones que está haciendo a partir del algoritmo previamente entrenado \[Figura 1.4\]. \[5\]

![](Resultados/docx/COMPARACION/media/media/image4.png)

Figura 1.4. Metodología en ML con aprendizaje continuo.

La diferencia entre un algoritmo de ML y un modelo de ML consiste en que el algoritmo es el conjunto de instrucciones que dicen como aprender de los datos y el modelo es el producto que resulta de aplicar dicho algoritmo a un conjunto de datos.

Dichos datos no son más que la base del ML, la calidad del dato y la cantidad son imprescindibles. Dichos datasets de datos suelen llevar un preprocesamiento antes de pasar a usarlos; se limpian, transforman y dividen en subconjuntos de entrenamiento, validación y prueba.

### Tipos de ML

El ML se divide normalmente en tres tipos principales:

**Aprendizaje Supervisado**

En el aprendizaje supervisado el objetivo es aprender una correspondencia entre las entradas \"x\" y las salidas \"y\", dado un conjunto etiquetado de pares de entradas y salidas.

Dicho conjunto etiquetado de pares se denomina conjunto de entrenamiento. Las entradas \"x\" son llamadas características, atributos o covariables, y pueden ser desde datos básicos, como la altura y peso de una persona, hasta datos más complejos, como imágenes o gráficas. La forma de la salida y determina el tipo de tarea:

-   Cuando y es una variable categórica (por ejemplo, "ataque" o "normal"), la tarea es de clasificación.

-   Cuando y es un valor real (por ejemplo, el precio de una casa), la tarea es de regresión

Algunos de los algoritmos de aprendizaje supervisado más representativos son k-NN, la regresión logística y lineal, los arboles de decisión y las redes neuronales.

**Aprendizaje No Supervisado**

El otro enfoque es el de **aprendizaje no supervisado**, donde solo se nos proporcionan entradas y el objetivo es encontrar \"patrones interesantes\" en los datos. Esto a veces se denomina descubrimiento de conocimientos. Se trata de un problema peor definido, ya que no se nos dice qué tipo de patrones debemos buscar y no existe una métrica de error obvia que podamos utilizar (a diferencia del aprendizaje supervisado, en el que podemos comparar nuestra predicción de y para un x dado con el valor observado).

Bajo este paradigma, se agrupan tareas de naturaleza bastante distinta:

-   Agrupamiento (clustering), que busca particionar los datos en grupos internamente homogéneos (como por ejemplo K-Means).

-   Reducción de dimensionalidad y visualización, que busca proyectar los datos a un espacio de menos dimensión conservando su estructura (como por ejemplo PCA).

-   Reglas de asociación, que busca encontrar coocurrencias frecuentes entre variables (como por ejemplo Apriori).

-   Detección de anomalías y de novedades, que buscan identificar observaciones que se apartan del resto (como por ejemplo Isolation Forest).

**Reinforcement Learning o Aprendizaje por Refuerzo**

Un agente aprende por interacción con un entorno, guiado por recompensas y penalizaciones. A la vez, este agente aprende a hacer decisiones secuenciales.

Hay otros tipos, como el aprendizaje semi-supervisado (combina conjuntos de entradas y salidas, con solo entradas, para obtener un resultado mejor cuando no hay muchos datos de entrada con su salida correspondiente), o el aprendizaje auto-supervisado (donde el modelo genera sus propios conjuntos de etiquetas, sin supervisión humana). \[7\]

En el caso de este proyecto, la primera etapa (Anomalías) no se trata de aprendizaje no supervisado puro, ya que esa clasificación es razonable cuando el detector se entrena sobre un conjunto de datos mixto y sin etiquetar, pero en este caso, se entrena exclusivamente sobre el Split D1 (que más tarde se explicará que consiste únicamente en tráfico normal), la etiqueta de clase existe en el dataset original y se usa explícitamente para construir ese Split. El modelo nunca ve, durante el entrenamiento, ni un solo ejemplo de ataque ni tampoco de un conjunto mixto sin etiquetar, sino que solo ve una única clase.

Por consecuencia, se trata de un aprendizaje semisupervisado de una sola clase (one-class), y es el término que este trabajo adopta como canónico para los cuatros algoritmos utilizados en esta etapa (IsolationForest, OneClassSVM, LocalOutlierFactor y el autoencoder)

### Etapas del Ciclo de vida de un proyecto de ML

##### Comprensión y recolección de datos

La primera fase delimita el problema, reúne los datos y --antes de transformarlos\-- los comprende: naturaleza y distribución de cada atributo, proporción de valores faltantes, correlaciones entre variables y patrones o anomalías visibles.

##### Limpieza y preparación de datos

Sobre una copia del conjunto original, se corrigen o eliminan los valores atípicos, se tratan los faltantes y se escalan las características, de modo que su rango numérico no distorsione el aprendizaje de los algoritmos sensibles a la escala. Además, opcionalmente se seleccionan y construyen características, con el objetivo de discretizas variables continuas, descomponer las compuestas o agregar varias en una más informativa.

#####  Selección del tipo de modelo

Se exploran varios candidatos con configuración estándar para acotar el espacio de soluciones razonables, se compara por validación cruzada y se examina qué tipo de error comete cada uno.

La decisión no se toma con un único número: se contrastan la **media** de la métrica elegida entre particiones, su **desviación típica** ---un candidato algo peor pero mucho más estable puede ser preferible--- y el **tipo de error** cometido, que aporta la matriz de confusión

##### Entrenamiento del modelo y ajuste de hiperparámetros

Seleccionados los candidatos, el entrenamiento ajusta sus **hiperparámetros** ---los valores que el algoritmo no aprende de los datos--- mediante validación cruzada.

##### Evaluación del rendimiento

Medir su rendimiento sobre un conjunto que no ha intervenido en ninguna decisión previa, para estimar el error de generalización. Es la fase que da sentido a todo lo anterior \[5\].

### Algoritmos de ML

[]{#_Toc236498676 .anchor}Esta sección describe, a nivel de familia algorítmica, los métodos de aprendizaje automático que aparecen en el resto de la memoria.

**\
Algoritmos Supervisados**

-   **Arboles de decisión**

Un árbol de decisión es una estructura jerárquica de nodos de decisión que particiona el espacio de características mediante preguntas sucesivas sobre una variable, hasta llegar a una hoja que asigna una clase (árbol de clasificación) o un valor numérico (árbol de regresión). Su atractivo principal es la **interpretabilidad**: el camino desde la raíz hasta una hoja es, literalmente, la explicación de la predicción, lo que permite volcarlo en reglas legibles

-   **Bosques de decisión: Random Forest y Gradient Boosting**

Un **conjunto** (ensemble) combina varios clasificadores individuales en un modelo agregado que, en general, generaliza mejor que cualquiera de sus componentes por separado. Aplicado a árboles de decisión, el resultado se conoce como bosque de decisión (**decision forest**); las dos familias principales usadas en la práctica son los bosques aleatorios y los árboles potenciados por gradiente.

-   Random Forest

> Combina un número elevado de árboles de decisión ---típicamente entre decenas y miles---, cada uno entrenado sobre una muestra aleatoria de los datos y de las características. La predicción final se obtiene por voto mayoritario entre los árboles en clasificación, o por promedio en regresión. El muestreo aleatorio decorrelaciona los árboles individuales y reduce la varianza del conjunto respecto a un único árbol

-   Gradient Boosting

> Construye los árboles de forma secuencial: cada árbol nuevo se entrena para corregir los errores residuales del conjunto acumulado hasta ese punto, siguiendo la dirección de descenso del gradiente de una función de pérdida. El resultado suele ser más preciso que un bosque aleatorio a igualdad de número de árboles, a costa de un entrenamiento secuencial ---no paralelizable entre árboles--- y de mayor sensibilidad al sobreajuste si no se regulariza.
>
> **HistGradientBoosting** es una de las variantes de esta familia, la cual se caracteriza por acelerar el ajuste discretizando las características continuas en un número fijo de contenedores antes de construir los árboles.

-   K vecinos más cercanos (k-NN)

> El algoritmo de los k vecinos más cercanos es el ejemplo más conocido de **aprendizaje perezoso**: en lugar de estimar una función general durante el entrenamiento, se limita a almacenar todos los ejemplos de entrenamiento y pospone todo el cálculo al momento de clasificar.

**Algoritmos Semisupervisados de una clase (one-class)**

Un segundo grupo de algoritmos se entrena exclusivamente con ejemplos de una única clase ---en este trabajo, tráfico normal--- y aprende una caracterización de esa clase para poder señalar como anómalo cualquier ejemplo que no encaje en ella.

Estos algoritmos se denominan **semisupervisados (one-class)**: reciben una supervisión parcial ---la etiqueta «normal» está disponible y se usa para decidir con qué datos entrenar--- pero no observan ejemplos de la clase contraria durante el ajuste. No son, por tanto, algoritmos no supervisados en sentido estricto, aunque compartan con ellos el mecanismo interno de no usar etiquetas de clase en el criterio de optimización.

-   Isolation Forest

> Aísla cada punto mediante particiones aleatorias sucesivas del espacio de características, construyendo un conjunto de árboles de aislamiento (isolation trees). En cada árbol, se elige aleatoriamente una característica y un valor de corte dentro de su rango, hasta que el punto queda aislado en su propia hoja.
>
> La intuición es que los puntos **anómalos**, al ser escasos y diferentes del resto, quedan aislados con **pocas particiones** ---su camino desde la raíz hasta la hoja es corto---, mientras que los puntos normales, más densos y numerosos, requieren muchas más particiones para separarse del resto. La longitud media del camino de aislamiento a través del conjunto de árboles se convierte así en una puntuación de anomalía: cuanto más corto el camino, más anómalo el punto.

-   One-Class SVM

> One-Class SVM adapta el principio de las máquinas de vectores de soporte (*Support Vector Machines*) al aprendizaje con una sola clase. En lugar de buscar un hiperplano que separe dos clases, busca la **frontera** ---en el espacio transformado por un núcleo (*kernel*), típicamente el radial (RBF)--- que envuelve la región donde se concentra la clase normal, dejando fuera de ella la menor fracción posible de puntos de entrenamiento compatible con un margen de tolerancia fijado de antemano.

-   Local Outlier Factor

> Caracteriza la anomalía en términos de densidad local: compara la densidad de puntos alrededor de un ejemplo con la densidad alrededor de sus vecinos más cercanos. Un punto cuya densidad local es sensiblemente menor que la de su vecindario ---es decir, que está más aislado que sus propios vecinos--- recibe una puntuación LOF elevada y se considera anómalo.
>
> La ventaja de este enfoque frente a un criterio de densidad global es que detecta anomalías locales: un punto puede tener una densidad absoluta razonable y aun así resultar anómalo si su entorno inmediato es mucho más denso que él, algo que un umbral de densidad único no capturaría.

**Redes neuronales artificiales**

Una neurona artificial calcula una suma ponderada de sus entradas y le aplica una función de activación no lineal; organizadas en capas sucesivas ---entrada, una o varias ocultas y salida--- forman un perceptrón multicapa (*Multi-Layer Perceptron*, MLP). Es la no linealidad de la activación la que permite a la red aproximar relaciones que un modelo lineal no puede representar: sin ella, apilar capas equivaldría a una única transformación lineal. El entrenamiento consiste en minimizar una función de pérdida por descenso de gradiente, calculando los gradientes de todos los pesos mediante retropropagación.

Lo que este trabajo usa de esa familia es un componente concreto: un MLP empleado como **autoencoder**, que es el detector seleccionado para la etapa 1

**Algoritmos no supervisados**

Los algoritmos de agrupamiento (*clustering*) ---k-means y el agrupamiento jerárquico como exponentes principales--- agrupan puntos «cercanos» entre sí sin usar ninguna etiqueta. Este trabajo no los emplea y se mencionan solo para delimitar por contraste el régimen semisupervisado (one-class).

### Métricas de evaluación de modelos

-   Matriz de confusión

La **matriz de confusión** es el punto de partida de toda métrica de clasificación: no resume nada, solo cuenta. Enfrenta la clase real de cada muestra con la clase que el modelo predijo, de modo que cada fila representa una clase real y cada columna la clase prevista. En el caso binario, la matriz reduce el resultado a cuatro contadores:

-   **VP (verdadero positivo)**: un ataque correctamente señalado como ataque.

-   **VN (verdadero negativo)**: tráfico normal correctamente dejado pasar.

-   **FP (falso positivo)**: tráfico normal marcado por error como ataque ---la falsa alarma que satura al analista---.

-   **FN (falso negativo)**: un ataque que el sistema no detecta ---el fallo de mayor coste operativo en un NIDS---.

A partir de estos cuatro contadores de la matriz de confusión binaria se definen las métricas derivadas de uso más extendido.

-   **Precisión**: De todas las veces que el sistema levantó una alarma de ataque, qué proporción era correcta.

  --------------------------------------------------------------------------
  ![](Resultados/docx/COMPARACION/media/media/image5.png)            \(1\)
  ------------------------------------------------------------------ -------

  --------------------------------------------------------------------------

-   Exhaustividad (recall): de todos los ataques reales, qué proporción detectó el sistema.

  --------------------------------------------------------------------------
  ![](Resultados/docx/COMPARACION/media/media/image6.png)            \(2\)
  ------------------------------------------------------------------ -------

  --------------------------------------------------------------------------

-   Tasa de falsos positivos (FPR): de todo el tráfico normal, qué proporción se marcó por error como ataque. Es la contrapartida obligada del recall en un sistema de seguridad, porque cuantifica el coste de cada punto de detección ganado.

  --------------------------------------------------------------------------
  ![](Resultados/docx/COMPARACION/media/media/image7.png)            \(3\)
  ------------------------------------------------------------------ -------

  --------------------------------------------------------------------------

-   Exactitud (accuracy): la proporción de predicciones correctas sobre el total.

  --------------------------------------------------------------------------
  ![](Resultados/docx/COMPARACION/media/media/image8.png)            \(4\)
  ------------------------------------------------------------------ -------

  --------------------------------------------------------------------------

-   F1: la media armónica de precisión y recall.

  --------------------------------------------------------------------------
  ![](Resultados/docx/COMPARACION/media/media/image9.png)            \(5\)
  ------------------------------------------------------------------ -------

  --------------------------------------------------------------------------

Las métricas anteriores evalúan un clasificador en un **único umbral de decisión**. Pero casi todo clasificador ---los detectores de anomalías de este sistema, en particular--- no produce directamente una etiqueta, sino una puntuación continua que después se convierte en decisión binaria comparándola con un umbral. Cambiar ese umbral cambia recall y FPR simultáneamente, en sentidos opuestos: bajar el umbral captura más ataques (sube el recall) a costa de marcar más tráfico normal por error (sube el FPR).

Las **curvas de rendimiento** representan ese compromiso barriendo todos los umbrales posibles:

-   **Curva ROC** (*Receiver Operating Characteristic*)

> Enfrenta la TPR (recall) frente a la FPR en cada umbral. Su resumen numérico habitual es el **área bajo la curva** (AUC-ROC): un valor de 1 indica separación perfecta entre clases; 0,5 equivale a una decisión al azar.

-   **Curva precisión-recall** (PR)

> Enfrenta la precisión frente al recall en cada umbral, con su propia área bajo la curva (AUC-PR).

Ambas curvas son formas válidas de resumir un clasificador sin comprometerse a un umbral concreto, pero **no son igual de informativas en todos los contextos**. Cuando la clase positiva es minoritaria ---la situación habitual en detección de intrusiones, donde el tráfico normal domina numéricamente sobre el de ataque, y más aún dentro de las categorías de ataque menos frecuentes--- la curva ROC puede resultar engañosamente optimista: el término VN del denominador de la FPR es tan grande que un número considerable de falsos positivos apenas mueve la curva. La curva PR, al no involucrar los verdaderos negativos en ninguna de sus dos coordenadas, es sensible precisamente a lo que la ROC diluye, y por eso se considera **más informativa bajo desequilibrio fuerte de clases.**

## Ciberseguridad

### Introducción a la ciberseguridad

La seguridad Informática (Computer Security) es un fundamento esencial para la Ciberseguridad. Se define como la protección que se brinda a un sistema de información automatizado con el fin de alcanzar los objetivos aplicables de preservar la integridad, disponibilidad y confidencialidad de los recursos del sistema de información (incluye hardware, software, firmware, información/datos y telecomunicaciones). \[8\]

La **ciberseguridad** amplía ese foco al **ciberespacio**: el conjunto interconectado de redes y sistemas que hoy conforman la infraestructura digital, y no un único activo aislado. Se define como el conjunto de actuaciones orientadas a asegurar, en la medida de lo posible, las redes y los sistemas que constituyen el ciberespacio, mediante tres líneas de actuación:

-   **detectar** las intrusiones y hacerles frente,

-   **detectar, reaccionar y recuperarse** de los incidentes que se produzcan, y

-   **preservar** la confidencialidad, la disponibilidad y la integridad de la información. \[10\]

Esta definición nos introduce a tres objetivos clave que son el corazón de la Seguridad Informática (CIA: Confidence, Integrity and Aviability):

-   **Confidencialidad** : Este término abarca dos conceptos relacionados.

<!-- -->

-   Confidencialidad de los datos

Garantiza que la información privada o confidencial no se ponga a disposición ni se divulgue a personas no autorizadas.

-   Privacidad

Garantiza que las personas controlen o influyan en qué información relacionada con ellas se puede recopilar y almacenar, y quién y a quién se puede divulgar dicha información.

-   **Integridad** : Este término abarca dos conceptos relacionados.

<!-- -->

-   Integridad de los datos

> Garantiza que la información y los programas solo se modifiquen de la manera especificada y autorizada.

-   Integridad del sistema

> Garantiza que un sistema realice su función prevista sin impedimentos, libre de manipulaciones deliberadas o involuntarias no autorizadas del sistema.

-   **Disponibilidad**: garantiza que los sistemas funcionen con rapidez y que no se deniegue el servicio a los usuarios autorizados.

Hay algunos conceptos adicionales que se suelen añadir para presentar una imagen completa, algunos de ellos son la autenticidad y la responsabilidad. \[9\]

###  Sistemas de detección de intrusiones

Una **intrusión** es cualquier acción, intencionada o no, que compromete la confidencialidad, la integridad o la disponibilidad de un sistema de información o de sus datos. Caben ahí sucesos muy distintos ---el acceso no autorizado a una cuenta, la modificación silenciosa de un fichero de configuración, la saturación deliberada de un servicio--- con un rasgo operativo común: dejan **huella observable**, en los logs del equipo afectado o en el tráfico de la red.

Un **IDS** es el componente que explota esa huella. Se define como el software o dispositivo que monitoriza de forma continua los eventos que ocurren en un sistema o en una red, los analiza en busca de indicios de actividad que viole las políticas de seguridad, y **genera una alerta** dirigida al analista responsable.

Este sistema, por tanto, no impide el ataque: lo **hace visible**, y su valor se mide por cuánto de lo que ocurre consigue señalar y cuánto ruido introduce al hacerlo. El sistema de este trabajo encaja en esa definición: un H-NIDS que recibe **registros de conexiones de red** ---cada fila de NSL-KDD es una conexión ya resumida en un vector de características--- y emite para cada una un veredicto que separa el tráfico normal del intrusivo y, dentro de este, la familia de ataque cuando puede reconocerla.

En este trabajo, la **etapa de anomalías** hereda de Denning (quien aportó el modelo IDES, donde se construye un perfil estadístico del comportamiento normal de cada sujeto y se marca como sospechosa toda desviación significativa) la idea de modelar lo normal y señalar la desviación; la **etapa de firmas**, que produce reglas legibles extraídas de un árbol de decisión, entronca con la tradición de Snort (basado en un motor ligero que compara el tráfico contra un conjunto de reglas legibles), con la diferencia de que aquí las reglas no las escribe un analista sino que se **aprenden de los datos**.

**Componentes funcionales de un NIDS**

Con independencia del método de análisis que emplee, un NIDS se descompone en la misma cadena de bloques, representada en la Figura 2.5 junto con la frontera de alcance de este trabajo:

1.  **Sensor o captura.** Obtiene el tráfico del segmento vigilado, normalmente mediante un *tap* o un puerto espejo del conmutador. Determina la **visibilidad** del sistema: lo que no llega al sensor no es detectable, por buena que sea la etapa siguiente.

2.  **Extracción de características.** Reensambla los paquetes en conexiones o flujos y calcula, para cada uno, un conjunto de atributos: duración, protocolo, bytes intercambiados en cada sentido, banderas de la conexión y estadísticas agregadas sobre ventanas de conexiones recientes.

3.  **Motor de análisis.** Recibe el vector de características y emite un veredicto, ya sea comparándolo contra un conjunto de reglas, contrastándolo con un modelo de normalidad, o ambas cosas.

4.  **Generación de alertas.** Convierte el veredicto en un evento con contexto ---origen, destino, momento, tipo de actividad sospechosa y nivel de confianza--- apto para ser consumido por un humano o por una plataforma de correlación.

5.  **Consola del analista.** Presenta, agrupa y prioriza las alertas. Es el punto donde el compromiso entre detección y falsas alarmas se paga en tiempo de trabajo.

![](Resultados/docx/COMPARACION/media/media/image10.png)

Figura 1.5. Cadena de bloques funcionales de un NIDS.

### Taxonomía de los IDS

La literatura no usa una taxonomía única sino **varios ejes ortogonales**: describir un IDS consiste en fijar un valor por eje, no en asignarle una etiqueta. Se recorren cuatro ---fuente de datos, método de detección, modo de despliegue y momento del análisis.

-   **Fuentes de datos**

El primer eje atiende a **qué observa** el sensor, y es el que determina qué evidencias puede llegar a ver el sistema y cuáles le son estructuralmente inaccesibles. Se diferencia en este punto entre HIDS (host-based IDS) y NIDS (network-based IDS).

Los dos enfoques son **complementarios y no excluyentes**, cubren puntos ciegos distintos, y una arquitectura de defensa en profundidad suele desplegar ambos, pero, en el caso de este trabajo, el sistema es un NIDS, ya que el dataset empleado describe conexiones de red y no contiene ningún evento de host, log ni traza de llamadas al sistema.

-   **Método de detección**

El segundo eje clasifica los IDS según **cómo deciden** que algo es un ataque. Es la taxonomía más citada del área y la que enmarca el problema de este TFG. Se presentan aquí las tres casillas:

1.  **Detección por firmas** (*signature-based* o *misuse detection*): el sistema mantiene una descripción explícita de ataques conocidos ---patrones, reglas, secuencias--- y alerta cuando el tráfico observado la satisface. El conocimiento reside en el **modelo de lo malicioso**.

2.  **Detección por anomalías** (*anomaly-based*): el sistema construye un modelo de lo que se considera comportamiento normal y alerta ante desviaciones significativas respecto de ese perfil. El conocimiento reside en el **modelo de lo normal**.

3.  **Sistemas híbridos**: combinan ambos mecanismos dentro de un mismo sistema, buscando que las carencias de uno queden cubiertas por el otro.

-   **Modo de despliegue y momento del análisis**

El tercer eje describe **dónde se sitúa el sensor respecto del tráfico**, y determina si el sistema puede, además de detectar, actuar. Las dos casillas son:

-   **Despliegue en línea (*inline*)**: el tráfico atraviesa el sensor, que por tanto puede bloquearlo --- es la modalidad que convierte al detector en un **IPS**.

-   **Despliegue pasivo o por copia**: el sensor recibe una réplica del tráfico y solo observa; su respuesta se limita a generar alertas.

Se superpone un cuarto eje, el **momento del análisis**: **tiempo real**, cuando la decisión se emite mientras el tráfico circula, y **diferido** (*offline*), cuando se analizan registros ya capturados ---análisis forense y evaluación experimental de modelos---. Los dos ejes son independientes: un sensor pasivo puede analizar en tiempo real, mientras que uno en línea exige por definición hacerlo.

El sistema construido en este trabajo opera en modo **pasivo y en diferido**: clasifica registros ya capturados, sin intervenir en el tráfico ni en restricción de latencia.

### Detección por firmas frente a detección por anomalías

De los ejes de clasificación recogidos en el punto anterior, el **método de detección** merece tratamiento propio: es el que estructura por completo el diseño de este trabajo. Los dos paradigmas clásicos ---**firmas** y **anomalías**--- tienen fortalezas y debilidades aproximadamente inversas, y de esa comparación sale la justificación de la arquitectura híbrida en cascada que constituye la tesis de este trabajo.

**Detección de firmas**

La detección por firmas ---también denominada *misuse detection*--- parte de un principio directo: si un ataque ya es conocido, su manifestación en el tráfico de red puede describirse mediante un patrón, y detectarlo se reduce a **buscar coincidencias de ese patrón** en el tráfico observado. El conocimiento del analista de seguridad queda así codificado en una **base de firmas**, un catálogo de reglas que el motor de detección evalúa sobre cada paquete o flujo.

Entre sus principales propiedades se encuentran la alta precisión sobre lo que cubre, alertas explicables y bajo volumen de falsas alarmas. Frente a esto, el sistema arrastra una debilidad estructural, no corregible mediante mejor ingeniería de reglas, y como consecuencia de esto tiene la ceguera ante ataques 0-day (y también de variantes de ataques conocidos que se alejen lo suficiente del patrón codificado) y un coste de mantenimiento permanente, ya que debe estar actualizándose constantemente.

La **etapa 2** del H-NIDS es la versión en aprendizaje automático de este paradigma: en lugar de reglas escritas a mano, un clasificador supervisado entrenado con ataques etiquetados (D3).

**Detección por anomalías**

La detección por anomalías invierte el planteamiento. En lugar de describir los ataques, modela el comportamiento normal del sistema o de la red y alerta ante toda desviación estadísticamente significativa respecto de ese modelo. La formulación original del enfoque se debe a Denning, que propuso caracterizar el uso legítimo mediante perfiles estadísticos y tratar la desviación de dichos perfiles como indicio de intrusión.

La propiedad que lo hace atractivo se sigue de su definición: **no necesita conocer el ataque para detectarlo**. Un ataque nunca visto que se aparte del perfil de normalidad será señalado como anómalo exista o no una firma para él, lo que convierte a este paradigma en el único de los dos con capacidad estructural frente a los 0-day, y en el que no exige mantener un catálogo de amenazas.

El precio de dicha capacidad se paga en mayor tasa de falsos positivos, alertas menos explicables y sensibilidad a la deriva (drift) del tráfico normal.

La **etapa 1** materializa este paradigma con detectores semisupervisados (*one-class*) entrenados solo con tráfico normal (D1): el modelo ve únicamente la clase «normal» y aprende su frontera. El umbral se fija en el percentil 95 de la puntuación de anomalía sobre validación, lo que equivale a aceptar por diseño en torno a un 5 % de falsas alarmas a cambio de sensibilidad.

**La justificación del orden de la cascada** ---anomalías primero, firmas después--- es la siguiente:

1.  El clasificador de firmas nunca ha visto tráfico normal. Se entrena solo con ataques, porque su cometido es distinguir entre tipos de ataque. Si se le presentara tráfico legítimo, lo asignaría por fuerza a alguna categoría de ataque, con el consiguiente aluvión de falsas alarmas. Por tanto, no debe recibir tráfico normal directamente.

2.  El detector de anomalías sí sabe qué es lo normal, y es la única etapa capaz de reaccionar ante lo no catalogado. Es, pues, el filtro adecuado para la primera decisión.

3.  En consecuencia, la etapa de anomalías decide si un flujo es sospechoso, y solo lo sospechoso pasa a la etapa de firmas, que decide qué es.

4.  Cuando la etapa de firmas no alcanza confianza suficiente para asignar una categoría conocida, en lugar de forzar una etiqueta emite la salida unknown, que convierte el hallazgo del detector de anomalías en una alerta accionable de posible 0-day.

La cascada **anomalía → firmas** no es una combinación novedosa: es, dentro del sentido (a) fijado más arriba, uno de los patrones con más recorrido en la literatura de IDS híbridos, y sobre NSL-KDD en concreto existen trabajos que la adoptan, la invierten y la reformulan como conjunto paralelo. Situar este trabajo frente a esos tres casos permite precisar en qué se apoya y en qué se aparta.

### Taxonomía de ataques y panorama de amenazas

La taxonomía empleada procede de las campañas de evaluación de detección de intrusiones del MIT Lincoln Laboratory para DARPA (1998), reutilizada en la competición KDD Cup 99 y heredada por NSL-KDD. Su criterio de agrupación no es el mecanismo técnico concreto del ataque, sino el objetivo del atacante y la relación de privilegio que busca alterar. Ese criterio es el que hace que la taxonomía envejezca bien: los exploits caducan, los objetivos no.

En el conjunto de datos utilizado, la agrupación se materializa en cuatro categorías de ataque ---**dos**, **probe**, **r2l** y **u2r**--- más la clase **normal**. Cada una agrupa un subconjunto de los 39 tipos de ataque específicos presentes en el corpus; junto con **normal**, el codificador de etiquetas del pipeline maneja por tanto 40 etiquetas que se colapsan en las 5 clases del problema. El mapeo completo tipo → categoría es un artefacto del propio pipeline.

DoS -- Denial of Service

-   Definición: Agotar un recurso del sistema víctima ---ancho de banda, memoria, tabla de conexiones, tiempo de CPU--- hasta que deja de poder atender a usuarios legítimos. El atacante no busca acceso: busca **negar disponibilidad**, uno de los tres objetivos de la tríada CIA

-   Ejemplos en el dataset: neptune (inundación de segmentos SYN que satura la cola de conexiones semiabiertas), smurf (amplificación mediante peticiones ICMP a direcciones de difusión), back, teardrop, pod, land, y los tipos añadidos en el conjunto de test como apache2, mailbomb, processtable o udpstorm.

-   Huella en el tráfico: Es la más marcada de las cuatro: volúmenes y tasas de conexión muy por encima de lo habitual, gran número de conexiones semiabiertas ---reflejadas en el estado S0 de la característica flag--- y tasas de error SYN elevadas (serror_rate, srv_serror_rate).

Probe -- sondeo y reconocimiento

-   Definición: Recopilar información sobre la red objetivo ---máquinas activas, puertos abiertos, servicios y versiones, topología--- como **fase previa** a una intrusión. No causa daño directo, pero su presencia es un indicador temprano de alto valor.

-   Ejemplos en el dataset: nmap, portsweep, ipsweep, satan, y mscan y saint entre los tipos que solo aparecen en test.

-   Huella en el tráfico: Muchas conexiones **cortas y de escaso volumen** dirigidas a puertos distintos del mismo host (barrido de puertos) o al mismo puerto de hosts distintos (barrido de red), concentradas en una ventana temporal breve. Las características de ventana del dataset (count, srv_count, diff_srv_rate, dst_host_diff_srv_rate) están diseñadas precisamente para capturar este patrón, por lo que Probe también resulta relativamente visible.

R2L -- Remote to Local

-   Definición: Obtener acceso no autorizado como usuario local en una máquina sobre la que el atacante solo tiene conectividad de red, explotando credenciales débiles, servicios mal configurados o vulnerabilidades de aplicación.

-   Ejemplos en el dataset: guess_passwd (fuerza bruta o adivinación de contraseñas), warezclient y warezmaster, ftp_write, imap, phf, multihop, spy, y los tipos exclusivos de test snmpguess, snmpgetattack, named, sendmail, xlock, xsnoop y worm.

-   Huella en el tráfico: Aquí empieza la dificultad. Un R2L puede consistir en **una sola conexión** a un servicio legítimo, con volumen, duración y protocolo indistinguibles de los de un usuario real; lo que delata al ataque no está en la forma del flujo, sino en su **contenido**. Por eso la detección se apoya en las características de contenido del dataset (num_failed_logins, hot, logged_in, is_guest_login) más que en las estadísticas de ventana. Es una de las dos categorías estructuralmente más difíciles del problema.

U2R -- User to Root

-   Definición: Escalada de privilegios: un atacante que ya dispone de una cuenta de usuario sin privilegios en la máquina obtiene control de administrador, típicamente explotando un fallo de programación en un binario privilegiado.

-   Ejemplos en el dataset: buffer_overflow, rootkit, loadmodule, perl, y los tipos exclusivos de test httptunnel, ps, sqlattack y xterm.

-   Huella en el tráfico: Prácticamente nula. La escalada sucede **dentro del host**, mediante llamadas al sistema que un sensor de red no observa; lo único que llega al flujo son trazas indirectas (root_shell, su_attempted, num_root, num_file_creations). A esta invisibilidad se suma una **escasez extrema de muestras**: en el conjunto de ataques de entrenamiento (D3) U2R reúne exactamente **52 instancias**, frente a las decenas de miles de DoS, un desbalance de **ratio ≈ 883:1 entre DoS y U2R.** Es, por tanto, la clase minoritaria que condiciona toda la estrategia de evaluación: es la razón de que el trabajo vigile f1_macro y no la exactitud global

**Correspondencia con el espacio de salida del sistema.** Estas cuatro categorías más la normal **son exactamente las clases del problema** que resuelve el sistema: son las etiquetas del clasificador de firmas y las que estructuran el análisis de resultados en el capítulo de este trabajo de Evaluación. La taxonomía no es aquí un adorno teórico, sino la definición formal del espacio de salida del modelo.

## Inteligencia Artificial

El bloque anterior de este capítulo ha presentado el dominio de aplicación ---la ciberseguridad y los sistemas de detección de intrusiones--- y el bloque de aprendizaje automático ha introducido la disciplina que aporta las herramientas. Esta sección fija el **vocabulario** con el que se usarán ambas cosas en el resto de la memoria: qué se entiende por Inteligencia Artificial, qué relación guarda con el aprendizaje automático y con el aprendizaje profundo, y ---lo que aquí más importa--- **en qué punto exacto de esa jerarquía se sitúa el sistema desarrollado**.

La delimitación no es un preámbulo terminológico. En la literatura sobre detección de intrusiones, «IA» se emplea con frecuencia como etiqueta indistinta que cubre desde un árbol de decisión hasta un *transformer*, de modo que declarar la casilla propia es condición previa para que las comparaciones con trabajos previos signifiquen algo, igual que ocurría con el término «híbrido»

### IA, ML y DL

Los tres términos se usan a menudo como sinónimos, pero designan **conjuntos anidados**: cada uno es un subconjunto estricto del anterior. La relación ya se ilustró gráficamente en la Figura 1.1.

El punto que interesa retener es el **criterio de separación entre ML y DL**, porque es el que se aplicará después para situar el trabajo. No lo marca el uso de redes neuronales ---un perceptrón multicapa de una capa oculta es una red neuronal y no es aprendizaje profundo---, sino la **profundidad y el propósito**: se habla de DL cuando la jerarquía de capas es lo bastante honda como para que el aprendizaje de representaciones sea el mecanismo principal del modelo, y normalmente cuando esa arquitectura se entrena sobre datos no estructurados con infraestructura especializada.

Dicho criterio se sitúa en el **anillo intermedio**: es aprendizaje automático. Contiene un único componente neuronal ---un autoencoder implementado sobre MLPRegressor de scikit-learn--- que, por su tamaño y por el papel que desempeña, **no constituye una red profunda**.

### La IA en Ciberseguridad

Este apartado consiste en **qué hace el aprendizaje automático dentro de la ciberseguridad**, qué problemas resuelve bien, cuáles no, y qué le ocurre al propio modelo cuando el dominio de aplicación tiene, por definición, un adversario inteligente al otro lado.

El recorrido va en cuatro tramos: los **casos de uso defensivos**, el **problema de lo desconocido** como motivación de la arquitectura de este trabajo, la **cara ofensiva** ---tanto la IA al servicio del atacante como los ataques dirigidos contra los modelos--- y, por último, el **panorama de datasets públicos** que condiciona lo que hoy puede evaluarse en investigación de NIDS.

**Casos de uso defensivos**

El aprendizaje automático ha entrado en la práctica defensiva por aquellos problemas que comparten un mismo perfil: volumen de datos alto, variabilidad que desborda a las reglas escritas a mano y una etiqueta ---«malicioso» o «benigno»--- que puede aprenderse de ejemplos.

-   **Detección de intrusiones en red**

-   **Análisis de malware**

-   **Anti-phising y anti-spam**

-   **UEBA (User and Entity Behavior Analytics)**

De todos los problemas que el aprendizaje automático aborda en este dominio, hay uno que no es un problema de rendimiento sino de alcance, y es el que motiva la arquitectura de este trabajo: el ataque desconocido, o **0-day**.

1.  Un detector por firmas (o su equivalente aprendido, un clasificador supervisado) solo puede reconocer las clases que ha visto en el entrenamiento. Es una propiedad de su formulación, no una limitación de su calidad: se le pide elegir entre un conjunto cerrado de categorías.

2.  Un ataque nuevo no pertenece a ninguna de esas categorías. Presentado a un clasificador cerrado, no produce «ninguna de las anteriores»: produce la categoría conocida más parecida, que es una respuesta incorrecta emitida con la misma naturalidad que una correcta.

3.  Un detector de anomalías, en cambio, no necesita conocer el ataque: le basta con que se aparte del perfil de normalidad. Es el único de los dos que tiene capacidad estructural frente a lo no catalogado, al precio de no saber decir de qué ataque se trata.

### Límites y consideraciones éticas

Esta sección cierra el bloque desde el ángulo contrario: qué no puede hacer un detector basado en aprendizaje automático, qué no queda demostrado por una evaluación experimental y qué obligaciones ---técnicas, jurídicas y éticas--- acompañan a su uso.

El tratamiento es deliberadamente de marco teórico. Aquí se enuncian los límites como categoría conceptual, con su razón técnica y su respaldo bibliográfico; el inventario de los límites concretos de este trabajo, con sus cifras, corresponde a la discusión de resultados.

El hilo conductor lo aporta la revisión de Arp et al., que sistematiza **diez errores metodológicos recurrentes** (*pitfalls*) en la aplicación de aprendizaje automático a seguridad informática, agrupados por fase del flujo de trabajo. Su hallazgo, sobre una revisión de treinta artículos publicados en los cuatro congresos de referencia del área durante la década anterior, es que *«each paper suffers from at least three pitfalls».* Dos de esos diez errores ---**P9, Lab-Only Evaluation**, y **P10, Inappropriate Threat Model**--- son precisamente límites de la **evaluación experimental** como método, y por eso se desarrollan aquí y no en el capítulo de resultados.

**Evaluación de laboratorio frente a evaluación operativa (P9)**

El pitfall P9 de Arp et al., *Lab-Only Evaluation*, enuncia que un sistema de seguridad evaluado exclusivamente en condiciones de laboratorio **no ha demostrado nada sobre su comportamiento en producción**, por buenos que sean sus números. La distancia entre ambos escenarios no es de grado, sino de naturaleza, y se descompone en al menos cuatro factores independientes:

-   Prevalencia irreal de las clases.

-   Ausencia de coste de despliegue.

-   Datos estáticos frente a tráfico vivo.

-   Ausencia de bucle humano.

Este pitfall se sale del alcance de este trabajo debido a que este sistema se evalúa en diferido y sobre datos ya capturados.

**El modelo de amenaza como requisito metodológico (P10)**

El segundo límite de método es el pitfall P10, *Inappropriate Threat Model*: **un sistema de seguridad solo está definido cuando está definido el adversario frente al cual pretende protegerlo**. Sin esa definición, afirmar que un detector «funciona» carece de contenido verificable, porque no se ha dicho contra qué.

Un **modelo de amenaza** es la especificación explícita de las hipótesis sobre el adversario bajo las cuales se afirma que un sistema cumple su función. Se construye fijando un valor en cada una de estas dimensiones:

-   Activo protegido \-- ¿Qué se defiende y qué propiedad de seguridad?

-   Objetivo del adversario \-- ¿Qué quiere conseguir?

-   Conocimiento \-- ¿Qué sabe del defensor?

-   Capacidad \-- ¿Qué puede modificar, y con qué restricciones?

-   Momento de la acción \-- ¿Cuándo interviene?

-   Adaptatividad \-- ¿Reacciona al defensor?

**Por qué un trabajo de detección debe explicitarlo**

El razonamiento tiene tres pasos encadenados:

1.  **Toda evaluación asume un modelo de amenaza, se declare o no.** Medir un detector sobre un conjunto de tráfico fijo equivale a suponer un adversario que no modifica su comportamiento en respuesta a la defensa, es decir, **un adversario estático**. Ese supuesto está presente aunque nadie lo escriba.

2.  **Un supuesto no escrito se lee como una garantía que no se ha dado.** Si el trabajo no acota su adversario, el lector es libre de suponer el suyo ---por ejemplo, uno que conoce el modelo y adapta su tráfico--- y de concluir que los resultados son falsos. La cifra no cambia; lo que cambia es la afirmación que sostiene.

3.  **Explicitarlo convierte una vulnerabilidad argumental en un resultado delimitado.** «Este sistema detecta ataques» es una afirmación indefendible; «este sistema detecta, con este recall y este FPR, ataques de un adversario no adaptativo que desconoce el modelo» es una afirmación acotada, comprobable y honesta.

### 

# Diseño del sistema

## Requisitos del sistema

Dividimos los requisitos en funcionales y de alcance en base al objetivo del sistema, el cual es un sistema híbrido de detección de intrusiones en red (H-NIDS) que combine detección de anomalías y por firmas. Para ello el sistema debe reunir la principal característica de cada enfoque: por un lado, la capacidad de las anomalías para señalar lo nunca visto, y por el otro, la precisión de las firmas para clasificar la conocido.

### Requisitos funcionales

El sistema debe:

-   **Distinguir tráfico normal de tráfico sospechoso,** incluidos ataques cuya firma no ha visto nunca (ataques 0-day). Este es el requisito principal de anomalías, ya que un detector de firmas no puede cumplirlo.

-   **Clasificar los ataques conocidos** en las cuatro categorías canónicas del dataset NSL-KDD: denegación de servicio **(dos**), sondeo **(probe)**, acceso remoto no autorizado **(r2l)** y escalada de privilegios **(u2r).**

-   **Señalar como "desconocido" o "unknown"** aquel tráfico que detecta como sospechoso pero que no puede clasificar con confianza como ninguna categoría conocida. Esta salida es el reconocimiento explícito de un posible ataque nuevo.

### Requisitos de datos

-   El entrenamiento y validación del sistema se hace sobre el dataset NSL-KDD, separando el entrenamiento en dos subconjuntos, uno exclusivo de tráfico normal, que nos servirá para entrenar el modelo de anomalías, y otro con ataques conocidos, el cual utilizaremos para el modelo de detección por firmas.

-   La evaluación/validación del sistema debe ser realista: este proceso se realiza sobre el conjunto de validación completo, en el cual encontramos tanto tráfico normal como ataques (conocidos y desconocidos).

### Requisitos no funcionales

-   **Reproducibilidad:** todo resultado debe ser regenerable de forma determinista, para ello utilizamos una semilla global fija (*random_state = 42*) y versiones de librerías fijas. Ningún numero de la memoria procede de una ejecución manual irrepetible.

-   **Interpretabilidad de las firmas:** la etapa de detección por firmas debe poder producir reglas legibles, siguiendo la línea de un IDS clásico basado en reglas..

-   **Sin dependencias pesadas de Deep Learning:** el sistema se basa en las librerías *sickit-learn* y *imbalanced-learn* para el balanceo. Incluso el autoencoder se implementa mediante un perceptrón multicapa (MLPRegressor), lo que mantiene el proyecto ligero, portable y reproducible.

### Requisito de alcance

El objetivo del proyecto es investigar y experimentar, no entregar un único modelo. Por ello, cada modelo elegido se basa en la comparación de varios algoritmos bajo un protocolo idéntico (mismos datos, misma semilla y mismas métricas).

### Modelo de amenaza

Este apartado hace lo que la última sección del capítulo anterior deja pendiente: **instanciar el caso**, es decir, fijar un valor concreto en cada dimensión para *este* sistema y sostener por qué (para el pitfall P10).

-   Activo protegido \-- La red monitorizada: disponibilidad de sus servicios (dos), confidencialidad e integridad de los equipos accesibles desde ella (probe, r2l, u2r)

-   Objetivo del adversario \-- Comprometer la red por alguna de esas cuatro vías. **No** figura entre sus objetivos evadir al detector

-   Conocimiento \-- **Caja negra sin observación**: el adversario desconoce el modelo entrenado, sus características de entrada, su umbral de decisión y su arquitectura en cascada. Tampoco recibe información de si una conexión suya fue detectada.

-   Capacidad \-- Únicamente **emitir tráfico** hacia la red. No controla los datos de entrenamiento, no accede a la infraestructura del defensor y no altera el proceso de extracción de características.

-   Momento de la acción \-- Exclusivamente en **inferencia**. Se excluye por completo el **envenenamiento** del entrenamiento

-   Adaptatividad \-- **Estático**: repite su comportamiento con independencia de lo que haga la defensa

## Arquitectura del sistema

La arquitectura del H-NIDS consiste en una cascada de dos etapas: un detector de anomalías que clasifica un flujo es sospechoso o normal, seguido de un clasificador de firmas que, solo para dicho flujo sospechoso, lo asigna a una categoría de ataque conocida o lo marca como desconocido.

### Las dos etapas

![](Resultados/docx/COMPARACION/media/media/image11.png)

Figura 1.5. Flujo del proyecto

-   Etapa 1 -- Detector de anomalías.

Entrenado solo con tráfico normal, aprende un modelo de lo que es el comportamiento básico y marca como sospechoso todo lo que se desvíe de él por encima de un umbral. Actúa como un filtro binario normal / sospechoso.

-   Etapa 2 -- Clasificador de firmas.

Entrenado solo con ataques conocidos, recibe solo los flujos que la etapa 1 marcó como sospechosos y los clasifica en una de las cuatro categorías de ataque. Si su confianza en la predicción no alcanza un umbral (*UMBRAL_CONF*), marca el flujo como desconocido (candidato a 0-day).

## Metodología de funcionamiento del sistema

Esta sección consiste en describir como se organizan los datos en cada una de las etapas para que cada modelo aprenda lo que le corresponde, además de como recorre un flujo de red el sistema completo y bajo que protocolo se validan los modelos.

### Diseño de los subconjuntos

La arquitectura en cascada exige que cada modelo se entrene con datos distintos: anomalías con tráfico normal y firmas con ataques. Para ello, el tráfico de entrenamiento del NSL-KDD se divide en dos subconjuntos especializados y el test se reserva íntegro para evaluar:

+----------------------+----------------------------------------------------------------------------+-----------------------+
| SUBCONJUNTO          | CONTENIDO                                                                  | PROPÓSITO             |
+======================+============================================================================+=======================+
| D1                   | Solo tráfico normal del entrenamiento.                                     | Entrenar etapa 1.     |
+----------------------+----------------------------------------------------------------------------+-----------------------+
| D3                   | Solo ataques conocidos del entrenamiento.                                  | Entrenar etapa 2.     |
+----------------------+----------------------------------------------------------------------------+-----------------------+
| D2                   | Conjunto de test completo (que incluye tráfico normal y ataques, conocidos | Evaluar               |
|                      |                                                                            |                       |
|                      | y desconocidos).                                                           |                       |
+----------------------+----------------------------------------------------------------------------+-----------------------+

### 

Esta separación es lo que hace posible medir la detección de 0-day: al no re-particionar el test, D2 conserva los tipos de ataque que no aparecen en el entrenamiento (17 tipos), que son indetectables por la etapa de firmas y sirven para poner a prueba la etapa de anomalías.

Una decisión metodológica asociada a esta partición es que **todos los transformadores del preprocesado ---codificador, escalador y selector--- se ajustan únicamente sobre el tráfico de entrenamiento (D1+D3) y se aplican a D2 sin reajustarlos**, porque en un despliegue real no se conocen de antemano las categorías ni los rangos del tráfico futuro.

### Protocolo de evaluación común

Para que la comparación entre algoritmos sea igual, todos los modelos de una misma etapa se entrenan y evalúan bajo un mismo protocolo: mismos subconjuntos, misma semilla (*random_state = 42*), mismas métricas y particiones de validación cruzada (Cross-Validation). La regla transversal e inviolable es que el D2 (el test) no interviene jamás, ni en el entrenamiento, ni en la selección de modelos, ni en los umbrales, solo lo usamos para reportar los resultados finales.

## Modelo de detección de anomalías

Esta sección describe el diseño de la primera etapa de la cascada.

### Planteamiento

El detector de anomalías se plantea como un problema de aprendizaje de una sola clase (one class / semisupervisado): se entrena exclusivamente con el tráfico normal (D1) y aprende a como se comporta el mismo. En la evaluación, todo lo que se diferencie de dicho tráfico, se marcará como sospechoso.

La razón de este planteamiento es lo que diferencia este sistema: un detector que solo conoce el tráfico normal no depende de haber visto un ataque concreto para señalarlo. Así, un ataque nunca visto (0-day) es para este sistema simplemente un flujo que se desvía de lo normal, y por tanto detectable. Esta es la propiedad que un clasificador supervisado no puede tener.

### Algoritmos candidatos

Conforme al requisito de alcance del sistema planteado, se comparan varios algoritmos, los cuales son cuatro detectores de familias conceptualmente distintas, todos implementables en scikit-learn (librería de Python para ML núcleo del proyecto):

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **ALGORITMO**                                          **NOCIÓN DE ANOMALÍA**                           **Motivo de su inclusión**
  ---------------------------- -------------------------------------------------------------------------- -----------------------------------------------------------------
  Isolation Forest                           Aísla las anomalías por particiones aleatorias               Referencia rápida y robusta, sin problemas de escala

  OneClassSVM                          Aprende una frontera que encierra el comportamiento normal         Enfoque clásico de frontera; sensible al escalado

  LocalOutlierFactor                 Compara la densidad local de cada punto con la de sus vecinos        Perspectiva basada en densidad, complementaria a las anteriores

  Autoencoder (MLPRegressor)    Error de reconstrucción: reconstruye mal lo que no se parece a lo normal  Enfoque neuronal ligero, sin dependencias de DL pesadas
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------

La diversidad de familias (particiones, frontera, densidad, reconstrucción) es deliberada: permite comprobar qué noción de "anomalías" funciona mejor sobre este tráfico, y como se verá en los resultados, revela que los detectores son complementarios por tipo de ataque.

### Diseño del umbral de decisión

Cada detector produce puntuación continua de anomalía; convertirla en una decisión binaria normal /sospechoso requiere un **umbral**. El diseño de este umbral es una decisión clave en el sistema, porque no disponemos de ataques etiquetados para ajustarlo sin comprometer la evaluación. Resumo los puntos clave de esta decisión:

-   El umbral se fija en el percentil 95 del score de anomalía sobre un subconjunto de validación reservado de D1. Esto equivale a aceptar, por diseño, una 5% de los falsos positivos sobre tráfico normal similar al de entrenamiento.

-   Se aplica el mismo criterio a los cuatro algoritmos, para que la comparación sea homogénea.

-   El umbral nunca se ajusta mirando D2: hacerlo sería una fuga de información que invalidaría la evaluación.

### Papel en la cascada

En el sistema completo, este modelo de anomalías actúa como un filtro binartio de entrada: decide que flujos son sospechosos, y por construcción de la cascada, es quien toma la decisión normal / ataque. Los flujos que marca como sospechosos, y solo esos, son los que pasan a la siguiente etapa.

## Modelo de detección basado en firmas

Esta sección describe el diseño de la segunda etapa de la cascada.

### Planteamiento

La etapa de firmas se plantea como un problema de clasificación supervisada multiclase sobre los ataques conocidos (D3): dado un flujo ya marcado como sospechoso por la primera etapa, decide a cual de las cuatro categorías de ataque pertenene. No incluye la clase normal, porque distinguir entre flujo normal y ataque es responsabilidad de la etapa anterior; este clasificador solo sub-clasifica lo que ya se considera como sospechoso.

Esta etapa es el equivalente a lo que ya conocemos como las firmas de un IDS clásico, pero en lugar de reglas escritas a mano por un analista, aprende de los ejemplos de D3 los patrones que caracterizan a cada familia de ataque.

### Algoritmos candidatos

Se comparan cuatro clasificadores supervisados, todos de la librería ya mencionada anteriormente, *scikit-learn.*

  --------------------------------------------------------------------------------------------------------------------------------------------
  ALGORITMO               IDEA                                                   MOTIVO DE SU INCLUSIÓN
  ----------------------- ------------------------------------------------------ -------------------------------------------------------------
  DecisionTree            Reglas jerárquicas sobre umbrales de características   Máxima interpretabilidad: base para extraer firmas legibles

  RandomForest            Conjunto (ensemble) de árboles por bagging             Robusto y preciso en problemas tabulares multiclase

  KNN                     Clasificación por cercanía a los vecinos               Enfoque basado en distancia, sin modelo explícito

  HistGradientBoosting    Conjunto por boosting (rendimiento tipo XGBoost)       Alto rendimiento sin dependencias externas nuevas
  --------------------------------------------------------------------------------------------------------------------------------------------

### Firmas interpretables

Un requisito no funcional del sistema es la interpretabilidad de las firmas, es decir, que el modelo exponga la lógica con la que decide en términos que una persona pueda leer, verificar y auditar, en vez de emitir una puntuación opaca. Para cumplir con este objetivo, del árbol de decisión se extraen reglas legibles (mediante *export_text*), del tipo: "*si flag_s0 = 1 y serror_rate alta 🡪 **dos***". Estas reglas son la analogía directa con las firmas de un IDS tradicional y permiten que un analista entienda y audite por qué el sistema atribuye un ataque a una categoría. Aunque el clasificador finalmente seleccionado no sea el árbol, sus reglas se conservan como aportación interpretable al trabajo.

### Tratamiento del desbalance como decisión de diseño

D3, es decir, el dataset de entrenamiento de este modelo, está fuertemente desbalanceado. La categoría u2r apenas reúne unas decenas de muestras frente a las decenas de miles de dos. Entrenar sin más sobre ese reparto produciría un clasificador que ignora a las clases minoritarias.\
Por ello, el tratamiento del desbalance se aborda como una decisión de diseño explícita y guiada por datos:

🡪 Comparar el sobremuestreo sintético (SMOTE) frente al reponderado de clases (class_weight='balanced') y elegir, por algoritmo, el que mejor rinda en validación cruzada.

### Papel en la cascada y salida "desconocido"

En el sistema completo, esta etapa recibe únicamente los flujos que la etapa 1 ya marcó como sospechosos. Además de asignar categoría, incorpora el mecanismo que da al sistema su capacidad de señalar lo nuevo.

Si la **confianza** de la predicción (probabilidad máxima entre las categorías) no alcanza un umbral *UMBRAL_CONF*, el flujo se etiqueta como **desconocido** (candidato a 0-day) en vez de forzar una categoría. El diseño de este umbral de confianza (calibrado sin mirar el test \[D2\]) se desarrolla en la implementación del sistema híbrido.

El criterio para definir el *UMBRAL_CONF* es una decisión de diseño, con dos exigencias:

Primera, **no puede calibrarse mirando el test** (D2), hacerlo sería una fuga de información y, además, los 0-day no están en el entrenamiento, de modo que su detección solo puede medirse, nunca optimizarse.

Segunda, el umbral se fija sobre las **probabilidades del clasificador de firmas estimadas fuera de muestra** (*out-of-fold*, mediante validación cruzada sobre D3), que reflejan la confianza del modelo ante datos que no usó para ajustarse. Sobre esas probabilidades se aplica un regla de presupuesto, se elige el umbral más alto (el más agresivo marcando desconocido) cuyo coste en recall sobre las categorías conocidas se mantenga por debajo de una tolerancia pequeña. Un umbral más alto captura más candidatos a 0-day pero degrada la clasificación de lo conocido; la regla fija ese equilibrio del lado conservador. La calibración concreta (rango explorado, tolerancia y valor elegido) se desarrolla con su tabla de sensibilidad en puntos posteriores.

## Conclusiones del capítulo

Este capítulo ha definido qué sistema se construye y por qué antes de entrar en su implementación. Las decisiones de diseño que lo definen son las siguientes:

🡪 **Una arquitectura híbrida en cascada** (anomalías 🡪 firmas), y no un clasificador único, como respuesta al requisito diferenciador del sistema, que es detectar también ataques nunca vistos. El orden de las etapas está justificado, el clasificador no conoce la clase normal por lo que la etapa de anomalía debe filtrar previamente esta clase, y es de este orden del que sale la capacidad de señalar lo desconocido.

🡪 **Un diseño de datos en tres subconjuntos especializados** (D1 solo tráfico normal, D3 solo ataques, D2 test completo), que asigna a cada etapa exactamente el tráfico que necesita aprender y mantiene en el test los tipos de ataque ausente del entrenamiento, necesarios para poder medir la detección de 0-day.

🡪 **Un protocolo experimental común y una disciplina anti-leakage transversal**. Comparar varios algoritmos por etapa en igualdad de condiciones (misma semilla, mismos datos, mismas métricas), fijar en los umbrales sin mirar nunca el test, y ajustar la normalización solo sobre el entrenamiento. Es lo que hará creíbles y comparables los resultados.

🡪 **Dos modelos concebidos para roles distintos**. Un detector de anomalías *one-class* sobre tráfico normal, con umbral por percentil homogéneo entre los cuatro algoritmos candidatos; y un clasificador de firmas supervisado sobre los ataques conocidos, con extracción de reglas interpretables, tratamiento explícito del desbalance y una salida "desconocido" que materializa la detección de lo nuevo.

El capítulo fija un diseño en el que cada componente tiene una responsabilidad delimitada y cada decisión responde a un requisito o a una salvaguarda metodológica, no a una elección por defecto.

# Implementación del sistema

## Tecnologías utilizadas

Antes de detallar el pipeline, este apartado fija el entorno técnico sobr el que se ha desarrollado el sistema, es decir, las herramientas de trabajo, lenguaje de programación y las librerías empleadas con su función concreta. Todas las versiones de las librerías están fijadas en el correspondiente *requirements.txt.*

### Entorno y aplicaciones

El desarrollo se ha realizado sobre Windows 11, con el código Python en un entorno virtual creado con el intérprete de Python 3.11. Aislar las dependencias en un entorno virtual evita conflictos con otras instalaciones del sistema y permite congelar el conjunto exacto de librerías del proyecto.

Las aplicaciones utilizadas son:

-   Visual Studio Code -- editor de código para el desarrollo de los scripts de Python.

-   Git -- control de versiones del repositorio del proyecto.

-   Obsidian -- redacción y organización de las notas en formato Markdown que constituyen la fuente de esta memoria.

-   Microsoft Word -- maquetación del documento final y gestión de la bibliografía en formato IEEE.

### Lenguaje de programación

Todo el sistema está implementado en Python 3.11. La elección se justifica por tres motivos:

-   Ecosistema científico maduro: Python es el lenguaje de referencia para el aprendizaje automático, con librerías consolidadas (scikit-learn, pandas, numpy) que cubren todo el pipeline sin necesidad de herramientas externas.

-   Estabilidad de la versión: se optó por la 3.11 (no por la última publicada) por ser una versión estable y ampliamente soportada por el conjunto de librerías del proyecto, evitando incompatibilidades tempranas.

-   Reproducibilidad: fijando la versión del intérprete y las de las librerías se garantiza que los experimentos (en particular la selección de características por importancias de Random Forest, sensible a la versión de scikit-learn) produzcan los mismos resultados en cualquier ejecución.

### Librerías de Python

El proyecto depende de un conjunto reducido de librerías, todas con versión fijada en el fichero de configuración. La tabla siguiente recoge las librerías directas y papel en el pipeline. Además de estas, el fichero de config. fija con su versión exacta las dependencias transitivas (las que estas librerías arrastran de forma indirecta y que no se invocan desde el código), de modo que el entorno queda congelado completamente y no solo en sus componentes principales.

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Librería                Versión                 Función en el proyecto
  ----------------------- ----------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Numpy                   2.3.2                   Calculo numérico y operaciones vectorizadas; percentiles para el umbral p95 del detector de anomalías

  Pandas                  2.3.1                   Carga del dataset NSL-KDD y manipulación de los conjuntos D1/D2/D3 como DataFrames

  Scikit-learn            1.7.1                   Núcleo de ML: preprocesamiento (MinMaxScaler, LabelEncoder), los cuatro algoritmos de anomalías y los cuatro de firmas, GridSearchCV, StratifiedKFold, cross_val_predict y las métricas de evaluación

  Imbalanced-learn        0.14.2                  Tratamiento del desbalance de clases: SMOTE dentro de un Pipeline que lo aplica en cada fold del Cross-Validation (CV)

  Scipy                   1.16.0                  Estadísticas de la validación: test de Kolmogórov-Smirnov para el análisis de drift D1 🡪 D2

  Matplotlib              3.10.3                  Generación de todas las figuras (EDA, matrices de confusión, curvas ROC/PR)

  Seaborn                 0.13.2                  Visualizaciones estadísticas sobre matplotlib (distribuciones, mapas de calor)

  Joblib                  1.5.1                   Persistencia de los modelos entrenados y de los transformadores ajustados, para inferencia consistente

  pillow                  11.3.0                  Soporte de imágenes para el guardado de figuras
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Cabe destacar que el proyecto no depende de frameworks de Deep Learning como TensorFlow, Pytorch o Keras, el autoencoder del detector de anomalías se implementa con MLPRegressor de scikit-learn. Esto tiene como objetivo mantener el sistema ligero y sin dependencias pesadas.

## Base de datos utilizada

El sistema se ha desarrollado y evaluado sobre el dataset **NSL-KDD**, un conjunto de datos de referencia para la investigación en detección de intrusiones en red. Este apartado describe su origen, la naturaleza de sus características y las razones de su elección.

NSL-KDD es el último eslabón de una línea de herencia que se remonta a finales de los años noventa. Su punto de partida es el programa **DARPA 1998** del MIT Lincoln Laboratory, que generó varias semanas de tráfico de red simulado de una red militar con ataques inyectados de forma controlada. Ese tráfico bruto se transformó, para la competición **KDD Cup 1999**, en un conjunto de registros por conexión (cada fila resume una conexión TCP/IP mediante un vector de características), que se convirtió durante años en el banco de pruebas estándar de la detección de intrusiones \[enlace bibliografía: KDD Cup 99\].

El dataset KDD\'99 arrastraba, sin embargo, dos defectos bien documentados \[ enlace bibliografía: Tavallaee 2009\]. El primero era la **presencia masiva de registros duplicados** (del orden de tres cuartas partes de las conexiones, tanto en el train como en el test) que sesgaba a los clasificadores hacia los tipos de ataque más frecuentes (sobre todo los de denegación de servicio) e inflaba artificialmente las métricas de cualquier modelo. El segundo era la ausencia de un reparto de dificultad razonable entre entrenamiento y prueba. **NSL-KDD** (2009) es la revisión que corrige ambos: elimina los registros duplicados y reequilibra la dificultad, de modo que el rendimiento medido sobre él es mucho más representativo de la capacidad real de generalización de un modelo \[enlace bibliografía: Tavallaee 2009\]. La crítica original a la metodología de evaluación del DARPA/KDD se remonta a \[ enlace bibliografía: McHugh 2000\].

De esta herencia el trabajo aprovecha una propiedad concreta: usar los ficheros oficiales KDDTrain+.txt y KDDTest+.txt tal cual, sin re-particionar el test, preserva el hecho de que el conjunto de prueba contiene tipos de ataque ausentes del entrenamiento. Es exactamente lo que habilita el escenario 0-day que da sentido a la etapa de anomalías del sistema.

Cada conexión se describe mediante **41 características**, a las que el dataset añade la etiqueta del tipo de ataque y un índice de dificultad (level, ajeno al problema y descartado en el preprocesamiento). Las 41 características se agrupan en tres familias, según qué aspecto de la conexión capturan:

-   **Básicas** --- atributos de la propia conexión TCP/IP, extraíbles de sus cabeceras: duration, protocol_type, service, flag, src_bytes y dst_bytes.

-   **De contenido** --- obtenidas inspeccionando la carga útil, orientadas a detectar ataques que no alteran el patrón de tráfico sino su contenido (r2l, u2r): num_failed_logins, logged_in, root_shell.

-   **De tráfico** --- estadísticas calculadas sobre ventanas de conexiones (temporales y por host), que capturan el comportamiento agregado propio de los ataques de volumen (dos, probe): count, serror_rate, dst_host_same_srv_rate.

Esta correspondencia entre grupo de características y tipo de ataque detectable no es anecdótica: explica varios resultados del capítulo 5. Las categorías r2l y u2r, que dependen de las características de contenido, son sistemáticamente las más difíciles, y ataques como snmpgetattack resultan casi invisibles porque apenas se distinguen del tráfico normal en las características disponibles por conexión.

**¿Por qué se eligió NSL-KDD?**

La elección de NSL-KDD como base experimental responde a cuatro razones, asumida su contrapartida:

1.  **Estándar de facto con literatura abundante.** Es el dataset más utilizado en la investigación de NIDS con aprendizaje automático, lo que permite **comparar directamente** los resultados de este trabajo con los publicados \[CITA: Tavallaee 2009 + survey de datasets NIDS\].

2.  **Tamaño manejable.** Sus \~126.000 registros de entrenamiento permiten entrenar y comparar múltiples algoritmos en un equipo de sobremesa, sin GPU ni infraestructura distribuida.

3.  **Etiquetado completo por tipo de ataque**, no solo por categoría. Esta granularidad es la que hace posible medir el **recall de detección 0-day por tipo**, métrica central de la evaluación del sistema híbrido (véase [5.3 Resultados del sistema híbrido](file:///C:\Users\francisco.lopez\KIKO_TFG\Working_Directory\5.3%20Resultados%20del%20sistema%20híbrido)).

4.  **Contrapartida asumida:** el tráfico es **sintético y de 1998**, por lo que no refleja los protocolos ni las amenazas actuales. Es una limitación declarada del trabajo; la validación sobre datasets modernos queda recogida como línea futura (véase [6.2 Líneas futuras](file:///C:\Users\francisco.lopez\KIKO_TFG\Working_Directory\6.2%20Líneas%20futuras)).

### Análisis previo de la base de datos

Antes de entrenar ningún modelo se realizó un análisis exploratorio (EDA) de los datos y una validación sistemática de los tres subconjuntos de trabajo D1/D2/D3 (cuya construcción se detalla en [4.3 Preprocesamiento de los datasets](file:///C:\Users\francisco.lopez\KIKO_TFG\Working_Directory\4.3%20Preprocesamiento%20de%20los%20datasets) sección 4.3.6). El objetivo de este análisis es doble: caracterizar el dataset ---tamaños, reparto de clases, desbalance--- y detectar de antemano los fenómenos que condicionan el diseño del sistema: el desplazamiento de distribución entre entrenamiento y test, las características que mejor separan tráfico normal de ataque, y la presencia de tipos de ataque en el test que no existen en el entrenamiento. El EDA lo genera program.py; los chequeos cuantitativos, validacion.py.

Tamaño y reparto de los subconjuntos

Los tres subconjuntos, tras el preprocesamiento completo, quedan con las dimensiones siguientes (verificadas por el reporte de validación, integridad **APROBADA**):

  --------------------------------------------------------------------------------------------
  **Subconjunto**   **Contenido**                      **Instancias**    **Características**
  ----------------- ---------------------------------- ----------------- ---------------------
  D1                Solo tráfico normal (train)        67.343            54

  D2                Test completo (normal + ataques)   22.544            54

  D3                Solo ataques conocidos (train)     58.630            54
  --------------------------------------------------------------------------------------------

La figura del EDA resume, en un panel de nueve gráficos, el reparto de clases de cada subconjunto, la comparación de tamaños, los ataques predominantes y la cobertura de tipos entre train y test:

![](Resultados/docx/COMPARACION/media/media/image12.png)

De este panel se extraen las conclusiones que guían el resto del trabajo:

-   **D1 es puro** (una sola clase, normal), lo que lo hace apto para el aprendizaje de una sola clase (*one-class*) del detector de anomalías.

-   **D3 está fuertemente desbalanceado**: la categoría DoS domina (con neptune concentrando \~41.000 de las conexiones de ataque), mientras que U2R apenas reúne \~52 muestras. Este desbalance extremo (ratio ≈ 883:1 entre DoS y U2R) es lo que motiva el mini-experimento de balanceo de [4.3 Preprocesamiento de los datasets](file:///C:\Users\francisco.lopez\KIKO_TFG\Working_Directory\4.3%20Preprocesamiento%20de%20los%20datasets) sección 4.3.4 y el uso de f1_macro como métrica principal.

-   **El test no replica el reparto del entrenamiento**: en D3 la categoría DoS supone \~78 % de los ataques, pero en D2 baja a \~33 %, y R2L ---casi ausente en el train--- gana peso relativo en el test. Es un escenario deliberadamente exigente.

-   **Cobertura de tipos de ataque** (gráfico estrella): solo el \~52,5 % de los tipos de ataque del test son comunes a train y test; un \~42,5 % adicional aparece únicamente en el test. En términos de la clasificación por categorías del pipeline, **17 tipos de ataque presentes en D2 no existen en el entrenamiento** (enumerados en el [Apéndice A.1](file:///C:\Users\francisco.lopez\KIKO_TFG\Working_Directory\A.1%20Columnas%20del%20dataset%20NSL-KDD)). Estos \"0-day\" son indetectables por un modelo de firmas ---que solo conoce los ataques del train--- y constituyen el argumento central del sistema híbrido (véase [5.3 Resultados del sistema híbrido](file:///C:\Users\francisco.lopez\KIKO_TFG\Working_Directory\5.3%20Resultados%20del%20sistema%20híbrido)).

Una vista compacta del reparto de clases por subconjunto, que confirma visualmente la pureza de D1/D3 y el desbalance de D3, se obtiene también de validacion.py:

![](Resultados/docx/COMPARACION/media/media/image13.png)

Características discriminantes normal frente a ataque

Para orientar tanto la selección de características (sección 4.3.5) como la extracción de firmas interpretables (sección 4.5), validacion.py compara la distribución de cada característica entre D1 (normal) y D3 (ataque). La figura siguiente superpone los histogramas de las doce características más discriminantes (verde = normal, rojo = ataque):

![](Resultados/docx/COMPARACION/media/media/image14.png)

Cuanto menor es el solape entre ambas distribuciones, más informativa es la característica. Destacan:

-   **flag_S0** (conexión iniciada sin respuesta): prácticamente exclusiva del tráfico de ataque; es la firma natural de un SYN flood (neptune).

-   **flag_SF** y **logged_in**: concentradas en 1 para el tráfico normal y en 0 para los ataques.

-   **same_srv_rate**: cercana a 1 en el tráfico normal, dispersa hacia 0 en los ataques.

Estas mismas características reaparecen entre las reglas del árbol de decisión de la etapa de firmas ([4.5 Entrenamiento del modelo de detección basado en firmas](file:///C:\Users\francisco.lopez\KIKO_TFG\Working_Directory\4.5%20Entrenamiento%20del%20modelo%20de%20detección%20basado%20en%20firmas)).

Desplazamiento de distribución entre entrenamiento y test (drift)

Un sistema entrenado con tráfico normal debe enfrentarse en test a datos que se distribuyen de otra forma. Se cuantificó este desplazamiento mediante el test de Kolmogorov-Smirnov (KS) entre D1 y D2, característica a característica:

![](Resultados/docx/COMPARACION/media/media/image15.png)

37 de las 54 características (≈ 69 %) presentan drift estadísticamente significativo (KS con p \< 0,01). Encabezan el ranking src_bytes (KS = 0,346), dst_bytes (0,317) y dst_host_rerror_rate (0,298). Lejos de ser un problema, este desplazamiento es esperado y deseable: D2 mezcla ataques y tipos nunca vistos, y ese cambio de distribución es precisamente lo que el detector de anomalías debe captar. La existencia de este drift es también el motivo por el que la tasa de falsos positivos real del detector sobre D2 (\~8--10 %) supera la de diseño (\~5 % fijada sobre D1); se discute en \[\[5.1 Resultados del modelo de detección de anomalías\]\].

Valores atípicos (outliers)

Por último, se midió la proporción de valores atípicos (criterio del rango intercuartílico, IQR) por característica y subconjunto:

![](Resultados/docx/COMPARACION/media/media/image16.png)

La mediana de outliers en D1 es del 4,78 %. Las características donde D3 dispara los atípicos frente a D1 (src_bytes, dst_host_diff_srv_rate, dst_host_rerror_rate...) señalan comportamiento de ataque; los niveles no despreciables presentes también en D1 recuerdan que el propio tráfico normal tiene colas largas, un dato relevante a la hora de fijar el umbral del detector de anomalías por percentil (sección 4.4).

## Preprocesamiento de los datasets

Todo el preprocesamiento está implementado en la clase NSLKDDPreprocessor (Implementacion/app/program.py), que ejecuta un pipeline determinista (random_state=42) sobre los ficheros originales KDDTrain+.txt y KDDTest+.txt y genera como salida los artefactos specialized_nsl_kdd\_ de la carpeta Resultados\\. Los apartados siguientes describen cada transformación en el orden temático de la memoria; la validación posterior de los datos generados (integridad, distribuciones, drift) corre a cargo de validacion.py y su reporte se referencia donde procede.

### Adición y eliminación de etiquetas

El dataset NSL-KDD etiqueta cada conexión con su tipo específico de ataque. El vocabulario completo de etiquetas manejado por el pipeline consta de 40 valores: la etiqueta normal y 39 tipos de ataque. Trabajar directamente con 40 clases sería inviable para un clasificador con las muestras disponibles (varios tipos tienen menos de 20 instancias), por lo que el primer paso añade una etiqueta derivada, attack_category, que agrupa cada tipo en una de las cinco categorías canónicas de la literatura de NSL-KDD:

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Categoría               Descripción                                       Tipos agrupados
  ----------------------- ------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------
  Normal                  Tráfico legítimo                                  1 (normal)

  Dos                     Denegación de servicio                            10 (neptune, smurf, back, teardrop, pod, land, mailbomb, apache2, processtable, udpstorm)

  Probe                   Escaneo y reconocimiento                          6 (ipsweep, nmap, portsweep, satan, mscan, saint)

  R2l                     Acceso remoto no autorizado (*remote-to-local*)   15 (guess_passwd, warezclient, warezmaster, imap, ftp_write, multihop, phf, spy, sendmail, named, snmpgetattack, snmpguess, xlock, xsnoop, worm)

  U2r                     Escalada de privilegios (*user-to-root*)          8 (buffer_overflow, rootkit, loadmodule, perl, httptunnel, ps, sqlattack, xterm)
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

El mapeo (attack_mapping en program.py) cubre deliberadamente **también los tipos que solo aparecen en el conjunto de test**, de modo que toda fila de D2 recibe su categoría real aunque su tipo no exista en el entrenamiento; esta propiedad es la que después permite medir la detección de ataques \"0-day\" por tipo (véase [3.3 Metodología de funcionamiento del sistema](file:///C:\Users\francisco.lopez\KIKO_TFG\Working_Directory\3.3%20Metodología%20de%20funcionamiento%20del%20sistema)).

Sobre las etiquetas se ajustan dos LabelEncoder de scikit-learn: uno para los 40 tipos específicos y otro para las 5 categorías. Ambos se ajustan sobre el vocabulario completo del mapeo (no sobre los datos de un split concreto), lo que garantiza una codificación estable entre D1, D2 y D3. De las columnas de entrada se eliminan, antes de construir la matriz de características, las tres que no son variables predictoras: attack, attack_category (etiquetas) y level (índice de dificultad propio de NSL-KDD, ajeno al problema).

El ajuste de ambos codificadores sobre el vocabulario del mapeo ---y no sobre las etiquetas presentes en un split--- se implementa así (program.py, preprocess_specialized_splits):

Bloque de Código

all_attacks = sorted(self.attack_mapping.keys()) \# 40 tipos

all_categories = sorted(set(self.attack_mapping.values())) \# 5 categorías

self.label_encoder = LabelEncoder()

self.label_encoder.fit(all_attacks)

self.category_encoder = LabelEncoder()

self.category_encoder.fit(all_categories)

### Normalización de variables numéricas

Las 38 variables numéricas del dataset presentan escalas radicalmente distintas (desde tasas en \[0,1\] hasta contadores de bytes con valores de cientos de millones), lo que penalizaría a los algoritmos basados en distancias (KNN, OneClassSVM, LOF) y al autoencoder. Se aplica un MinMaxScaler con rango (0, 1) sobre la matriz completa post-codificación.

La decisión metodológica central de este apartado es dónde se ajusta el escalador:

-   El MinMaxScaler se ajusta sobre la concatenación D1+D3 (los 125.973 registros de entrenamiento: tráfico normal + ataques conocidos), de modo que los rangos característicos de los ataques queden representados en la normalización.

-   D2 (test) se transforma con ese mismo escalador, sin re-ajustarlo. Ajustar el escalador con datos de test (o con la unión train+test) filtraría información del conjunto de evaluación hacia el entrenamiento (data leakage): en un despliegue real, los mínimos y máximos del tráfico futuro no se conocen de antemano.

En el código, el ajuste sobre el train y la transformación sin re-ajuste quedan en dos pasos separados (program.py):

Bloque de código

\# Paso 3 --- el escalador se ajusta sobre la concatenación D1+D3 (todo el train):

X_train_all = pd.concat(

\[encoded\[D1_KEY\]\[\'X_enc\'\], encoded\[D3_KEY\]\[\'X_enc\'\]\], axis=0

)

self.scaler = MinMaxScaler()

self.scaler.fit(X_train_all)

\# \...

\# Paso 5 --- cada split, incluido D2, se transforma con ESE escalador, sin re-ajustar:

X_scaled = self.scaler.transform(data\[\'X_enc\'\])

Esta decisión tiene una consecuencia visible y asumida: como D2 contiene valores fuera de los rangos vistos en el entrenamiento, tras el escalado 4 características de D2 quedan fuera del intervalo \[0, 1\]:

  -----------------------------------------------------------------------
  Característica                      Máximo en D2 (escalado)
  ----------------------------------- -----------------------------------
  num_shells                          2,50

  num_file_creations                  2,33

  duration                            1,35

  hot                                 1,31
  -----------------------------------------------------------------------

El reporte de validación lo registra explícitamente como hallazgo informativo, no como fallo: es el comportamiento esperable por diseño cuando el escalador solo ve el train, y de hecho es una manifestación del drift entre train y test característico de NSL-KDD (el mismo reporte detecta drift significativo D1→D2 en 37 de las 54 características mediante el test de Kolmogórov-Smirnov).

### Codificación de variables categóricas

NSL-KDD contiene tres variables categóricas: protocol_type (3 valores), service (\~70 valores) y flag (11 valores). Se codifican mediante **One-Hot Encoding** (pd.get_dummies), generando una columna binaria por categoría observada.

El punto delicado es la **definición del vocabulario de categorías**, porque cada split ve subconjuntos distintos de servicios y flags. La regla implementada es:

-   **Vocabulario = unión de las categorías observadas en D1 y D3** (todo el entrenamiento), con orden determinista (ordenación alfabética).

-   Cada split se reindexa contra ese vocabulario: las columnas ausentes se rellenan a 0 y las categorías **exclusivas de D2 se descartan**.

La construcción del vocabulario como unión del train y el realineado de cada split se implementan así (program.py, paso 2):

Bloque de codigo

\# Vocabulario one-hot = UNIÓN de D1 y D3, orden determinista (sorted):

train_cols = sorted(set(encoded\[D1_KEY\]\[\'X_enc\'\].columns)

\| set(encoded\[D3_KEY\]\[\'X_enc\'\].columns))

self.feature_columns_after_encoding = train_cols

for name, data in encoded.items():

for col in self.feature_columns_after_encoding:

if col not in data\[\'X_enc\'\].columns:

data\[\'X_enc\'\]\[col\] = 0 \# ausente en este split → 0

data\[\'X_enc\'\] = data\[\'X_enc\'\]\[self.feature_columns_after_encoding\]

Esta regla corrige un defecto detectado en una versión anterior del pipeline, que construía el vocabulario **solo con D1** (tráfico normal). Como hay servicios y flags que solo aparecen en tráfico de ataque, aquel vocabulario perdía **45 columnas dummy exclusivas de D3** ---precisamente algunas de las señales más discriminantes para el clasificador de firmas---. La corrección (2026-07-05) elevó la dimensionalidad de **77 a 122 características** (38 numéricas + 84 dummies), y obligó a regenerar los CSV y a revalidarlos con validacion.py.

Conviene justificar por qué la exclusión de las categorías exclusivas de D2 **no es un error simétrico al anterior**:

1.  El vocabulario D1-solo mutilaba información **disponible en el entrenamiento**: era un defecto de implementación sin justificación metodológica.

2.  Las categorías que solo existen en el test, en cambio, **tampoco se conocerían en producción** en el momento de entrenar. Incluirlas equivaldría a construir el espacio de características mirando el futuro. Su exclusión no es *leakage* sino **realismo**: una conexión de D2 con un servicio nunca visto queda representada con todas sus dummies de servicio a cero, que es exactamente la información de la que dispondría el sistema desplegado.

### Equilibrio y balanceo de muestras

El conjunto D3, con el que se entrena el clasificador de firmas, está fuertemente desbalanceado (véase la distribución exacta en [4.3.6](#4.3.6_División_del_conjunto_de_datos)): la clase mayoritaria (dos) supera a la minoritaria (u2r) en una proporción cercana a 883:1. Antes de fijar una estrategia de balanceo por defecto, se realizó un **mini-experimento controlado** que compara, para cada algoritmo de la etapa de firmas, sus dos opciones disponibles:

-   **DecisionTree y RandomForest**: sobremuestreo sintético **SMOTE** frente a ponderación de clases class_weight=\'balanced\'.

-   **KNN y HistGradientBoosting**: estos algoritmos no admiten class_weight en scikit-learn, por lo que se compara **SMOTE frente a no balancear**.

El protocolo del experimento (implementado en firmas.py::\_experimento_balanceo) es idéntico para los cuatro algoritmos: **validación cruzada estratificada de 5 particiones** sobre D3 (StratifiedKFold(5, shuffle=True, random_state=42)), métrica **f1_macro** e hiperparámetros por defecto (el eje de balanceo no se cruza con el de hiperparámetros para aislar el efecto de cada variable). Un detalle metodológico es crítico: **SMOTE se aplica dentro de cada fold** de la validación cruzada, encapsulado en un Pipeline de imbalanced-learn. Sobremuestrear antes de particionar sería incorrecto: las muestras sintéticas se interpolan a partir de vecinos reales, de modo que los folds de validación contendrían puntos derivados de los folds de entrenamiento y la validación quedaría contaminada (estimaciones optimistas por *leakage*).

Esa garantía se materializa envolviendo el estimador en un ImbPipeline, de modo que cross_val_score aplica el sobremuestreo por fold (firmas.py):

Bloque de código

def \_envolver_balanceo(self, algo, base, balanceo):

if balanceo == \"SMOTE\":

return ImbPipeline(\[

(\"smote\", SMOTE(random_state=config.RANDOM_STATE, k_neighbors=self.K_SMOTE)),

(\"clf\", base),

\])

return base

\# \...

\# SMOTE va DENTRO del pipeline → cross_val_score lo aplica en cada fold (sin leakage):

scores = cross_val_score(est, self.X_D3, self.y_D3,

cv=self.cv, scoring=\"f1_macro\", n_jobs=-1)

Los resultados sobre el set primario de 54 características son:

  ---------------------------------------------------------------------------
  Algoritmo              Balanceo          F1_macro(CV)      Desv. Típica
  ---------------------- ----------------- ----------------- ----------------
  DecisionTree           SMOTE             0,9350            0,0165

  DecisionTree           Class_weight      **0,9530**        0,0087

  RandomForest           SMOTE             **0,9736**        0,0079

  RandomForest           Class_weight      0,9715            0,0147

  KNN                    SMOTE             **0,9453**        0,0058

  KNN                    Sin balanceo      0,9187            0,0252

  HistGradientBoosting   SMOTE             **0,9694**        0,0153

  HistGradientBoosting   Sin balanceo      0,8327            0,0657
  ---------------------------------------------------------------------------

Del experimento se extraen tres conclusiones:

1\. Ganadores por algoritmo: class_weight para DecisionTree; SMOTE para RandomForest, KNN y HistGradientBoosting. Cada algoritmo usa su ganador en el entrenamiento final de \[\[4.5 Entrenamiento del modelo de detección basado en firmas\|4.5\]\].

2\. El caso extremo es HistGradientBoosting: sin balanceo se desploma a 0,833 (con la mayor varianza entre folds, 0,066), y SMOTE lo recupera hasta 0,969. En los demás algoritmos el efecto existe pero es moderado, lo que confirma que el desbalanceo de D3 no puede ignorarse pero tampoco domina el problema.

3\. La variante de 122 características, repetida como control, arroja los mismos ganadores con valores muy próximos (DecisionTree/class_weight 0,957; RandomForest/SMOTE 0,980; KNN/SMOTE 0,952; HistGradientBoosting/SMOTE 0,972 frente a 0,804 sin balanceo), de modo que la conclusión es robusta al set de características.

### Selección de características

Tras la codificación one-hot, el espacio de entrada tiene 122 dimensiones, muchas de ellas redundantes o irrelevantes. La selección de características (implementada en program.py::select_features) se ejecuta **después del escalado**, se calcula **exclusivamente sobre D1+D3** (nunca sobre el test) y consta de dos pasos:

**Paso 1 --- filtros baratos (no supervisados):**

-   **Varianza ≈ 0** (umbral 10⁻⁸): elimina **1 característica**, num_outbound_cmds, constante en todo el entrenamiento. El cálculo se hace sobre D1+D3 deliberadamente: calculado solo sobre D1 (tráfico normal), este filtro habría eliminado justo los dummies exclusivos de ataque recuperados por el fix de 4.3.3, deshaciéndolo en silencio.

-   **Correlación \|r\| \> 0,95**: elimina **7 características** redundantes, conservando de cada par la de mayor varianza (con resolución en cadena cuando el representante de un par cae a su vez por correlación). Las eliminadas son serror_rate, srv_serror_rate, dst_host_serror_rate y dst_host_srv_serror_rate (toda la familia de tasas de error SYN, cuyo representante superviviente es flag_S0), rerror_rate y dst_host_srv_rerror_rate (representadas por srv_rerror_rate) y num_compromised (representada por num_root, \|r\| = 0,999).

**Paso 2 --- ranking supervisado de importancias:** sobre las 114 características restantes se entrena un RandomForestClassifier (100 árboles, class_weight=\'balanced\', semilla 42) con la etiqueta de categoría (5 clases) sobre D1+D3, y se conserva el conjunto mínimo de características cuya **importancia acumulada alcanza el 99,9 %**. Este umbral elimina **60 características** más ---en su inmensa mayoría dummies de servicios minoritarios con importancia individual inferior a 10⁻⁴--- y deja el set final en **54 características**. Las tres más importantes son src_bytes (0,091), dst_host_srv_count (0,075) y dst_bytes (0,066). El umbral, deliberadamente conservador, retiene señales minoritarias de baja importancia global pero potencialmente críticas frente a ataques poco representados (num_failed_logins, flag_REJ, flag_SH, num_shells).

En resumen: **122 → 54 características** (−1 varianza, −7 correlación, −60 importancia). El detalle completo, con el ranking de las 54 conservadas y el motivo de cada eliminación, está en Resultados\\selected_features.txt.

Los dos pasos ---filtros baratos y ranking supervisado--- se implementan en program.py::select_features:

Bloque de codigo

\# Base de cálculo: train completo D1+D3, nunca el test:

X_train = pd.concat(

\[processed_splits\[D1_KEY\]\[\'X\'\], processed_splits\[D3_KEY\]\[\'X\'\]\], axis=0

)

\# Paso 1 --- filtros no supervisados sobre D1+D3:

\# varianza \~0 + \|correlación\| \> 0.95 (se conserva la de mayor varianza)

\# \...

\# Paso 2 --- ranking supervisado: RF sobre y_category (5 clases):

rf = RandomForestClassifier(

n_estimators=100, random_state=42, class_weight=\'balanced\', n_jobs=-1

)

rf.fit(X_train\[restantes\], y_train)

importancias = pd.Series(rf.feature_importances\_, index=restantes).sort_values(ascending=False)

\# Top-N cuya importancia acumulada alcanza el umbral (0.999 → 99.9 %):

n_top = int((importancias.cumsum() \< importancia_acumulada).sum()) + 1

self.selected_features = \[f for f in features_iniciales if f in set(importancias.index\[:n_top\])\]

Validación experimental: 54 frente a 122 características (experimento H1)

La selección del paso 2 es **supervisada** y está alineada con el clasificador de firmas, pero el detector de anomalías se entrena de forma no supervisada y solo con tráfico normal: un ranking que favorece la separación normal-frente-a-ataque podría descartar características casi constantes en tráfico normal que fueran la única señal de un ataque nunca visto. Para no fijar el set de features a ciegas, ambos sets (54 y la variante sin selección de 122) se mantuvieron generables y **la decisión se delegó a un experimento con datos**: ejecutar el sistema híbrido completo (cascada Autoencoder → RandomForest, umbral de confianza 0,5; véase capítulo 5) sobre ambas variantes y comparar recall 0-day por tipo y f1_macro.

  ----------------------------------------------------------------------------------------------------------
  Métrica (cascada AE→RF sobre D2)                           54 features             122 features
  ---------------------------------------------------------- ----------------------- -----------------------
  Recall 0-day global (detector)                             0,771                   **0,785**

  FPR binaria                                                0,102                   **0,085**

  AUC-ROC del detector                                       0,929                   **0,947**

  f1_macro sobre ataques conocidos, end-to-end (n = 9.083)   **0,748**               0,655

  f1_macro a 5 clases (criterio conservador)                 **0,641**               0,583
  ----------------------------------------------------------------------------------------------------------

**Veredicto: se adopta el set de 54 características para ambas etapas del sistema.** La lectura honesta de la tabla tiene dos caras:

-   Las 122 características producen un **detector de anomalías marginalmente mejor** en la tarea binaria pura (domina en recall 0-day, FPR y AUC simultáneamente), confirmando el riesgo teórico que motivó el experimento: la selección supervisada \"ciega\" ligeramente al detector no supervisado. El efecto, sin embargo, es pequeño, y el desglose por tipo de ataque lo acota con precisión: el delta global es de **+55 detecciones** (2.890 → 2.945 sobre 3.750), de las que **36 corresponden a mailbomb** ---que con 122 características deja de estar completamente a cero (recall 0,00 → 0,123) pero sigue esencialmente fallado (36 de 293)--- y **20 a mscan** (0,980 → 1,000, ya casi saturado con 54); el resto de tipos se compensa entre sí (aportaciones netas ≈ 0, con retrocesos en sendmail y snmpguess).

-   La diferencia decisiva está en la **etapa de firmas**: con 122 características el f1_macro end-to-end sobre ataques conocidos cae \~9 puntos (0,748 → 0,655), porque el RandomForest sobreajusta a los dummies adicionales presentes en D3, que generalizan mal a D2.

Dado que el sistema completo es mejor con 54 en las métricas multiclase y prácticamente equivalente en 0-day, se elige el set de 54 para las dos etapas (opción homogénea, más simple y comparable). La configuración mixta ---122 para el detector de anomalías y 54 para las firmas--- es defendible a la vista de la tabla y queda registrada como línea de trabajo futuro.

### División del conjunto de datos

La arquitectura en cascada del H-NIDS (véase \[\[3.3 Metodología de funcionamiento del sistema\]\]) exige que cada etapa se entrene con datos distintos. En lugar de un split train/test convencional, el pipeline genera tres divisiones especializadas a partir de los conjuntos oficiales de NSL-KDD:

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Split             Contenido                                      Tamaño            Función
  ----------------- ---------------------------------------------- ----------------- --------------------------------------------------------------------------------------------------------------
  D1                Solo tráfico normal del train                  67.343            Entrenamiento del detector de anomalías: el modelo aprende exclusivamente cómo es el comportamiento legítimo

  D2                Conjunto de test completo (normal + ataques)   22.544            Evaluación realista de ambas etapas y del sistema híbrido; intocable durante el entrenamiento

  D3                Solo ataques del train                         58.630            Entrenamiento del clasificador de firmas y extracción de reglas de ataques conocidos
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

D1 y D3 particionan el train oficial (125.973 registros) sin solaparse; D2 es el test oficial íntegro, con 9.711 conexiones normales y 12.833 ataques.![](Resultados/docx/COMPARACION/media/media/image12.png)

Dos propiedades de esta división estructuran todos los experimentos posteriores:

-   D2 contiene ataques que no existen en el entrenamiento (escenario 0-day real). De los 12.833 ataques de D2, 3.750 (el 29,2 %) pertenecen a 17 tipos ausentes de D3: apache2, httptunnel, mailbomb, mscan, named, processtable, ps, saint, sendmail, snmpgetattack, snmpguess, sqlattack, udpstorm, worm, xlock, xsnoop y xterm. Es una característica de diseño de NSL-KDD que este trabajo explota deliberadamente: esos 17 tipos hacen de banco de pruebas de detección 0-day, la capacidad que justifica la etapa de anomalías del híbrido. En la evaluación del clasificador de firmas (5.2) esas filas se apartan (quedan 9.083 ataques de tipo conocido); en la evaluación del sistema completo (5.3) son la métrica protagonista.

-   D3 está extremadamente desbalanceado. Su distribución por categorías es:

  -----------------------------------------------------------------------
  Categoría               Instancias              \% de D3
  ----------------------- ----------------------- -----------------------
  Dos                     45.927                  78,3 %

  Probe                   11.656                  19,9 %

  R2l                     995                     1,7 %

  U2r                     52                      0,09 %
  -----------------------------------------------------------------------

La proporción entre la clase mayoritaria y la minoritaria es ≈ 883:1. Este desbalance es el que motiva el mini-experimento de balanceo de \[\[#4.3.4 Equilibrio y balanceo de muestras\|4.3.4\]\] y la elección sistemática de f1_macro (que pondera las cuatro clases por igual) como métrica de selección de modelos: con 52 muestras de u2r, un clasificador que ignorase por completo esa clase apenas perdería una milésima de accuracy.

![](Resultados/docx/COMPARACION/media/media/image13.png)

## Entrenamiento del modelo de detección de anomalías

La primera etapa del H-NIDS es un detector de anomalías **semisupervisado** (*one-class*, véase [3.4 Modelo de detección de anomalías](file:///C:\Users\francisco.lopez\KIKO_TFG\Working_Directory\3.4%20Modelo%20de%20detección%20de%20anomalías)): aprende un modelo del tráfico legítimo y marca como sospechosa cualquier conexión que se desvíe de él, sin haber visto jamás un ataque durante el entrenamiento. El entrenamiento está implementado en la clase NSLKDDAnomalyTrainer (Implementacion/app/anomalias.py), que compara **cuatro algoritmos bajo un protocolo idéntico** (mismos splits, misma semilla 42, mismo criterio de umbral y mismas métricas): IsolationForest, OneClassSVM (kernel RBF), LocalOutlierFactor y un autoencoder. Todo el proceso opera sobre el set primario de 54 características (decisión de [4.3.5](file:///C:\Users\francisco.lopez\KIKO_TFG\Working_Directory\4.3%20Preprocesamiento%20de%20los%20datasets#4.3.5 Selección de características)); el script es parametrizable para reproducir la variante de 122.

### Protocolo de entrenamiento y validación

El diseño experimental responde a una dificultad propia de la detección semisupervisada de anomalías: **¿cómo elegir hiperparámetros sin etiquetas de ataque y sin tocar el conjunto de test?** El protocolo adoptado es el siguiente:

1.  **Entrenamiento solo con tráfico normal.** D1 (67.343 conexiones normales) se divide en un 80 % de entrenamiento y un **20 % reservado como validación** (D1_val), con semilla 42. Los modelos se ajustan únicamente sobre la fracción de entrenamiento.

2.  **Score de anomalía unificado.** Cada algoritmo expone una puntuación continua donde **mayor valor = más anómalo**. Como en scikit-learn score_samples/decision_function siguen el convenio contrario (mayor = más normal), las puntuaciones de IsolationForest, LOF y OneClassSVM se niegan; el autoencoder usa directamente su error de reconstrucción. Este convenio común hace homogéneas la selección de configuraciones, la fijación del umbral y las curvas ROC/PR.

3.  **Selección de hiperparámetros por AUC-ROC sobre un conjunto de validación etiquetado** formado por D1_val (etiqueta 0, normal) más una **muestra aleatoria de 5.000 filas de D3** (etiqueta 1, ataque). Cada configuración del grid se entrena sobre D1 y se puntúa sobre este conjunto; gana la de mayor AUC-ROC. La elección es metodológicamente defendible porque el conjunto solo contiene **ataques conocidos del entrenamiento** ---información legítimamente disponible---, y **D2 no interviene en ningún momento**: ni los ataques del test ni, en particular, los 17 tipos 0-day influyen en la elección de configuraciones.

4.  **Umbral de decisión: percentil 95 del score sobre D1_val.** Fijado el modelo ganador, el umbral que separa \"normal\" de \"sospechoso\" se calcula como el percentil 95 de las puntuaciones del modelo sobre la validación (solo tráfico normal). El criterio es **idéntico para los cuatro algoritmos** y equivale a aceptar por diseño una tasa de falsos positivos aproximada del 5 % sobre tráfico normal similar al de entrenamiento (la tasa efectiva sobre D2 puede diferir por el drift train→test documentado en 4.3.2). Nunca se ajusta el umbral mirando D2.

La unificación del *score* del punto 2 ---lo que hace homogénea la comparación entre algoritmos--- se concentra en el método \_score, que niega las puntuaciones de scikit-learn (donde mayor = más normal) y emplea el error de reconstrucción para el autoencoder (anomalias.py):

Bloque de código

def \_score(self, algo, model, X):

\# Anomaly score unificado: MAYOR = MÁS ANÓMALO.

\# score_samples / decision_function de sklearn dan \"mayor = más normal\": se niegan.

if algo in (\"IsolationForest\", \"LocalOutlierFactor\"):

return -model.score_samples(X)

if algo == \"OneClassSVM\":

return -np.asarray(model.decision_function(X)).ravel()

if algo == \"Autoencoder\":

recon = model.predict(X)

return ((recon - X.values) 2).mean(axis=1) \# MSE de reconstrucción

### Algoritmos y espacios de búsqueda

Los grids son deliberadamente pequeños (decisión de alcance del proyecto: comparación amplia de algoritmos con búsquedas contenidas, no optimización exhaustiva de uno solo):

  -----------------------------------------------------------------------------------------------------------
  **Algoritmo**           **Espacio explorado**                                       **Configuraciones**
  ----------------------- ----------------------------------------------------------- -----------------------
  IsolationForest         n_estimators ∈ {100, 200, 300} × max_samples ∈ {0.5, 1.0}   6

  OneClassSVM (RBF)       nu ∈ {0.01, 0.05, 0.1} × gamma ∈ {\'scale\', 0.01, 0.1}     9

  LocalOutlierFactor      n_neighbors ∈ {10, 20, 35, 50}                              4

  Autoencoder (MLP)       hidden_layer_sizes ∈ {(64, 32, 64), (32, 16, 32)}           2
  -----------------------------------------------------------------------------------------------------------

Tres particularidades de implementación merecen documentarse:

-   **OneClassSVM se entrena con una submuestra reproducible de 20.000 filas** de D1 (semilla 42). Su coste de entrenamiento es O(n²) en memoria y tiempo, lo que hace inviable ajustar 9 configuraciones sobre las \~54.000 filas de entrenamiento; la submuestra es la concesión práctica estándar para este algoritmo y se declara como tal.

-   **LocalOutlierFactor se instancia con novelty=True**, requisito para poder puntuar datos no vistos (D2); en su modo por defecto LOF solo evalúa el propio conjunto de ajuste.

-   **El autoencoder se implementa sin frameworks de deep learning**, como un MLPRegressor de scikit-learn entrenado para reconstruir su propia entrada (fit(X, X)), con early_stopping=True (que reserva internamente un 10 % del entrenamiento para la parada temprana) y max_iter=300. Su score de anomalía es el **error cuadrático medio de reconstrucción** por muestra: el modelo aprende a comprimir y reconstruir tráfico normal, por lo que las conexiones anómalas se reconstruyen mal y producen un MSE alto. Esta decisión mantiene todo el proyecto dentro del ecosistema scikit-learn (sin TensorFlow/Keras) a cambio de renunciar a arquitecturas más sofisticadas.

### Configuraciones ganadoras

Resultado de la selección por AUC-ROC de validación sobre el set de 54 características:

  ------------------------------------------------------------------------------------------------------------------------------------
  **Algoritmo**        **Configuración ganadora**          **AUC-ROC (validación)**   **Umbral (p95 sobre D1_val)**   **Tiempo (s)**
  -------------------- ----------------------------------- -------------------------- ------------------------------- ----------------
  IsolationForest      n_estimators=100, max_samples=1.0   0,9918                     0,4406                          5,0

  OneClassSVM          nu=0.1, gamma=\'scale\'             0,9708                     19,1866                         28,3

  LocalOutlierFactor   n_neighbors=20                      0,9389                     2,1863                          16,4

  Autoencoder          hidden_layer_sizes=(64, 32, 64)     0,9864                     3,3·10⁻⁵                        40,6
  ------------------------------------------------------------------------------------------------------------------------------------

La columna *Tiempo* mide el proceso completo por algoritmo (búsqueda en rejilla, fijación del umbral, evaluación y generación de figuras), no solo el ajuste del modelo; sirve como comparación relativa de coste, no como tiempo de entrenamiento puro. Los umbrales no son comparables entre algoritmos (cada score vive en su propia escala: el del autoencoder es un MSE sobre datos normalizados, de ahí su magnitud de 10⁻⁵); lo comparable es el criterio (p95) con el que se fijan. En AUC de validación, IsolationForest y el autoencoder parten como los candidatos más fuertes, con OneClassSVM por detrás y LOF como el más débil; la confirmación (o no) de este orden sobre datos de test, con las matrices de confusión y las curvas ROC/PR sobre D2, se presenta en [5.1 Resultados del modelo de detección de anomalías](file:///C:\Users\francisco.lopez\KIKO_TFG\Working_Directory\5.1%20Resultados%20del%20modelo%20de%20detección%20de%20anomalías).

Cada modelo ganador se persiste en Resultados\\modelos\\anomalia\_\<algoritmo\>\_54.joblib junto con su umbral, su configuración y los metadatos del set de características, de modo que el sistema híbrido del capítulo 5 los carga tal cual, sin re-entrenar: las métricas del híbrido son trazables una a una a estos artefactos.

## Entrenamiento del modelo de detección basado en firmas

La segunda etapa del H-NIDS es un clasificador supervisado multiclase que, una vez la etapa de anomalías ha marcado una conexión como sospechosa, la atribuye a una categoría de ataque conocida. El entrenamiento está implementado en la clase NSLKDDSignatureTrainer (Implementacion/app/firmas.py), que compara cuatro algoritmos bajo protocolo idéntico: DecisionTree, RandomForest, KNN y HistGradientBoosting. Como en la etapa anterior, todo opera sobre el set primario de 54 características, con la variante de 122 disponible como control.

### Protocolo de entrenamiento

-   Datos de entrenamiento: exclusivamente D3 (58.630 ataques del train, 4 clases: dos/probe/r2l/u2r). Aquí no existe la clase normal: distinguir normal de ataque es responsabilidad de la etapa 1, y este clasificador solo sub-clasifica lo ya marcado como sospechoso.

-   Búsqueda de hiperparámetros: GridSearchCV con validación cruzada estratificada de 5 particiones (StratifiedKFold(5, shuffle=True, random_state=42)), la misma partición para los cuatro algoritmos.

-   Métrica de selección: f1_macro. La justificación es el desbalance descrito en \[\[4.3 Preprocesamiento de los datasets#4.3.6 División del conjunto de datos\|4.3.6\]\]: u2r supone el 0,09 % de D3 (52 muestras frente a 45.927 de dos). Con ese reparto, el accuracy \"miente\": un clasificador que nunca predijera u2r conservaría un accuracy superior al 99,9 %. La media macro de F1, al ponderar las cuatro clases por igual, obliga al modelo a rendir también en las minoritarias.

-   Balanceo: el ganador por algoritmo del mini-experimento de \[\[4.3 Preprocesamiento de los datasets#4.3.4 Equilibrio y balanceo de muestras\|4.3.4\]\] (class_weight=\'balanced\' para DecisionTree; SMOTE para el resto). Cuando el ganador es SMOTE, el sobremuestreo va encapsulado en un Pipeline de imbalanced-learn dentro de cada fold del GridSearchCV (los hiperparámetros se referencian con el prefijo clf\_\_), manteniendo la garantía anti-leakage del experimento original.

-   D2 es intocable durante todo el proceso: ni el balanceo ni los hiperparámetros ven una sola fila del test. La evaluación sobre D2 ---restringida a los ataques de tipo conocido (9.083 filas), con los 17 tipos 0-day apartados--- se presenta en \[\[5.2 Resultados del modelo de detección basado en firmas\]\].

### Algoritmos y espacios de búsqueda

  ------------------------------------------------------------------------------------------------------------------
  Algoritmo               Espacio explorado                                                  Combinaciones
  ----------------------- ------------------------------------------------------------------ -----------------------
  DecisionTree            max_depth ∈ {5, 10, 20, None} × min_samples_leaf ∈ {1, 5, 20}      12

  RandomForest            n_estimators ∈ {100, 300} × max_depth ∈ {10, None}                 4

  KNN                     n_neighbors ∈ {3, 5, 11} × weights ∈ {\'uniform\', \'distance\'}   6

  HistGradientBoosting    learning_rate ∈ {0.05, 0.1} × max_iter ∈ {100, 300}                4
  ------------------------------------------------------------------------------------------------------------------

### Configuraciones ganadoras

Resultado del GridSearchCV sobre el set de 54 características (el modelo final de cada algoritmo se re-ajusta sobre todo D3 con su mejor configuración):

  -------------------------------------------------------------------------------------------------------
  Algoritmo              Balanceo (4.3.4)            Configuración ganadora               f1_macro (CV)
  ---------------------- --------------------------- ------------------------------------ ---------------
  DecisionTree           class_weight=\'balanced\'   max_depth=10, min_samples_leaf=1     0,9533

  RandomForest           SMOTE                       n_estimators=300, max_depth=10       0,9798

  KNN                    SMOTE                       n_neighbors=5, weights=\'uniform\'   0,9453

  HistGradientBoosting   SMOTE                       learning_rate=0.1, max_iter=300      0,9694
  -------------------------------------------------------------------------------------------------------

Los valores de f1_macro en CV difieren marginalmente de los de la tabla de 4.3.4 porque aquel experimento usaba hiperparámetros por defecto (los dos ejes ---balanceo e hiperparámetros--- se exploraron por separado, no cruzados). En validación cruzada los cuatro algoritmos superan 0,94, con RandomForest en cabeza; la generalización real a D2, donde estas cifras se degradan de forma desigual, se analiza en 5.2. Cada modelo se persiste en Resultados\\modelos\\firma\_\<algoritmo\>\_54.joblib con su balanceo, configuración y metadatos, listo para ser cargado por el sistema híbrido.

### Extracción de firmas legibles

Un requisito de la componente \"basada en firmas\" de un IDS clásico es la interpretabilidad: las firmas deben poder leerse, auditarse y, llegado el caso, trasladarse a reglas de un motor convencional. Para ello, del mejor DecisionTree se extraen sus reglas de decisión con export_text (truncadas a profundidad 5 para legibilidad), publicadas íntegras en Resultados\\firmas_reglas_54.txt. Dos advertencias de lectura: los umbrales operan sobre los valores escalados a \[0, 1\] de 4.3.2 (un corte como src_bytes \<= 0.00 significa \"prácticamente cero bytes\", no exactamente cero), y para las variables dummy binarias el corte \> 0.50 equivale a \"la categoría está presente\".

La extracción se reduce a una llamada, tras recuperar el árbol subyacente (firmas.py, \_extraer_firmas):

python

dt = self.\_extraer_dt(self.resultados\[\"DecisionTree\"\]\[\"modelo\"\]) \# desenvuelve el ImbPipeline si hubo SMOTE

reglas = export_text(dt, feature_names=list(self.X_D3.columns), max_depth=5)

Se comentan a continuación cuatro reglas representativas del árbol, conectadas con el ataque que describen:

**Regla 1 --- inundación SYN (dos, familia neptune):**

logged_in \<= 0.50 ∧ flag_S0 \> 0.50 ∧ dst_host_rerror_rate \<= 0.00 → dos

(Camino simplificado para la lectura: el árbol incluye un corte intermedio redundante, dst_host_rerror_rate ≤ 0,02, subsumido por el posterior ≤ 0,00; hoja y clase idénticas a las de firmas_reglas_54.txt.)

Conexiones sin sesión iniciada cuyo flag TCP es S0 ---se envió el SYN inicial y el handshake jamás se completó--- y sin errores de rechazo en el host destino. Es la firma canónica de un SYN flood tipo neptune. Nótese que flag_S0 actúa aquí como representante de toda la familia de tasas de error SYN (serror_rate, srv_serror_rate...), absorbida por el filtro de correlación de 4.3.5: la regla del árbol es equivalente a la firma clásica \"tasa de errores SYN alta\" de la literatura.

**Regla 2 --- escaneo de puertos y servicios (probe):**

logged_in \<= 0.50 ∧ flag_S0 \<= 0.50 ∧ src_bytes \<= 0.00

∧ dst_host_rerror_rate ≈ 1.00 ∧ dst_host_diff_srv_rate \> 0.35 → probe

Conexiones sin carga útil (src_bytes ≈ 0), con la práctica totalidad de las conexiones al host destino terminadas en error de rechazo (REJ) y más de un tercio dirigidas a servicios distintos. Es el patrón de un escáner (satan, portsweep) sondeando muchos puertos de una máquina: la mayoría cerrados (de ahí los rechazos) y todos diferentes (de ahí la diversidad de servicios).

**Regla 3 --- acceso remoto vía cuenta de invitado (r2l):**

logged_in \> 0.50 ∧ dst_host_srv_count \<= 0.04 ∧ dst_bytes \> 0.00

∧ is_guest_login \> 0.50 → r2l

Sesión iniciada con éxito como invitado (is_guest_login), con transferencia de datos desde el servidor, contra un servicio poco frecuentado en ese host. Describe los ataques r2l de tipo warezclient/ftp_write: abuso de cuentas anónimas o de invitado (típicamente FTP) para obtener acceso remoto no autorizado. Que una única variable binaria concentre tanta capacidad discriminante ilustra el valor de los indicadores \"de contenido\" del NSL-KDD para la categoría r2l (is_guest_login es una de las 41 características originales del dataset, no una dummy del one-hot).

**Regla 4 --- escalada de privilegios (u2r):**

logged_in \> 0.50 ∧ dst_host_srv_count \> 0.04 ∧ src_bytes \<= 0.00

∧ dst_bytes \> 0.00 → u2r

Sesión legítima ya iniciada, sobre un servicio habitual del host, con un volumen saliente mínimo pero con respuesta del servidor: el perfil de una sesión interactiva de baja intensidad en la que un usuario local explota una vulnerabilidad (buffer_overflow y afines). Esta regla debe leerse con cautela: con solo 52 muestras de u2r en D3, las hojas que la sustentan son estadísticamente frágiles, coherente con el hecho de que u2r sea la clase más débil de toda la etapa de firmas.

En conjunto, el árbol reproduce de forma autónoma el conocimiento experto que un analista codificaría a mano en un IDS de firmas ---estados TCP anómalos, patrones de barrido, abuso de cuentas de invitado---, que es exactamente la propiedad que se buscaba de esta etapa: detección precisa y explicable de los ataques conocidos.

## Conclusiones del capítulo

Este capítulo ha materializado el diseño del capítulo 3 en un sistema reproducible: desde los ficheros crudos del NSL-KDD hasta los modelos entrenados y persistidos, listos para la evaluación del capítulo 5. Cierran el capítulo las siguientes ideas.

### Un pipeline reproducible de principio a fin

Toda la implementación está gobernada por un principio de reproducibilidad estricta: semilla global random_state = 42 en cada paso con aleatoriedad, versiones fijadas (pinning) en requirements.txt, y persistencia con joblib tanto de los transformadores del preprocesado (escalador, codificadores, lista de características) como de los modelos entrenados y sus umbrales. Ningún número que llegue a la memoria procede de una ejecución manual: todos se regeneran ejecutando los scripts (program.py, validacion.py, anomalias.py, firmas.py, hibrido.py), que depositan sus artefactos en Resultados\\. Esta trazabilidad ---cada cifra ligada a su fichero de origen--- es la que ha permitido auditar los resultados de forma sistemática.

### Decisiones de preprocesado justificadas con datos, no por defecto

El capítulo no se ha limitado a aplicar transformaciones estándar, sino que ha justificado cada decisión de preprocesado con su efecto medido:

\- La codificación one-hot se fijó con el vocabulario de la unión del entrenamiento (D1+D3), no solo del tráfico normal, corrigiendo una pérdida silenciosa de las señales dummy exclusivas de los ataques (77 → 122 características).

-   La normalización (MinMaxScaler) se ajusta solo sobre el train (D1+D3) y se aplica al test sin re-ajustar, una decisión anti-leakage cuya consecuencia visible ---4 características de D2 fuera de \[0,1\]--- se documenta como comportamiento esperado, no como fallo.

-   El balanceo (sección 4.3.4) no se dio por supuesto: un mini-experimento decidió, por algoritmo y con f1_macro en validación cruzada, entre SMOTE y class_weight=\'balanced\'.

-   La selección de características (sección 4.3.5) redujo de 122 a 54 características y resultó tener un doble efecto beneficioso ---menor dimensionalidad y mejor generalización del clasificador de firmas---, validado después por el experimento 54 vs 122 del capítulo 5.

### La ausencia de fuga de información como principio transversal

El hilo metodológico que recorre todo el capítulo es que D2 (el test) permanece intocable durante el entrenamiento y la selección de modelos, replicando las condiciones de un despliegue real: el escalador no lo ve, el umbral de anomalías se fija sobre validación de D1, los hiperparámetros de firmas se eligen por validación cruzada sobre D3, y SMOTE se aplica dentro de cada fold para no contaminar la validación. Esta disciplina es lo que hace creíbles ---y comparables--- los resultados del capítulo siguiente.

### Comparación amplia bajo protocolo común

Conforme al requisito de alcance del proyecto, cada etapa entrena y compara cuatro algoritmos bajo un protocolo idéntico (mismos splits, misma semilla, mismas métricas, rejillas de búsqueda pequeñas y documentadas): cuatro detectores de anomalías (sección 4.4) y cuatro clasificadores de firmas (sección 4.5). La comparación en igualdad de condiciones ---no la optimización exhaustiva de un solo modelo--- es la que sustenta las conclusiones del capítulo 5. De esta etapa quedan seleccionados el Autoencoder como detector y el RandomForest con SMOTE como clasificador de firmas, y extraídas además firmas interpretables del árbol de decisión (sección 4.5) que conectan las reglas aprendidas con los ataques reales que describen.

Con los modelos entrenados y persistidos, y las decisiones de preprocesado justificadas, el sistema queda listo para su evaluación integral sobre D2, que se aborda en \[\[5.1 Resultados del modelo de detección de anomalías el capítulo 5\]\].

# Evaluación

## Resultados del modelo de detección de anomalías

En esta sección se presentan los resultados de la etapa de detección de anomalías del sistema híbrido. Los cuatro algoritmos comparados ---IsolationForest, OneClassSVM, LocalOutlierFactor y Autoencoder (implementado mediante MLPRegressor, véase \[\[4.4 Entrenamiento del modelo de detección de anomalías\]\])--- se entrenaron exclusivamente con el tráfico normal de D1 y se evaluaron sobre el conjunto de test completo D2 (22.544 flujos: 9.711 normales y 12.833 ataques) como un problema binario normal frente a ataque. Todos los resultados de esta sección corresponden al conjunto primario de 54 características (decisión Q1/C, véase \[\[4.3 Preprocesamiento de los datasets\]\]); la variante de 122 características se retoma únicamente donde aporta información adicional, en \[\[5.3 Resultados del sistema híbrido\]\].

### Matrices de confusión

Las cuatro figuras siguientes muestran la matriz de confusión binaria de cada detector sobre D2, aplicando a cada uno su umbral de decisión calibrado como percentil 95 del score de anomalía sobre el 20 % de D1 reservado como validación.

![](Resultados/docx/COMPARACION/media/media/image17.png)\
![](Resultados/docx/COMPARACION/media/media/image18.png)![](Resultados/docx/COMPARACION/media/media/image19.png)\
![](Resultados/docx/COMPARACION/media/media/image20.png)

La lectura conjunta de las cuatro matrices se resume en la tabla siguiente:

  ----------------------------------------------------------------------------
  Detector             VN (tn)       FP            FN            VP (tp)
  -------------------- ------------- ------------- ------------- -------------
  IsolationForest      8.738         973           2.957         9.876

  OneClassSVM          8.887         824           4.021         8.812

  LocalOutlierFactor   8.153         1.558         7.071         5.762

  Autoencoder          8.723         988           2.158         10.675
  ----------------------------------------------------------------------------

Los casos extremos son ilustrativos:

-   Autoencoder presenta el menor número de falsos negativos (2.158 de 12.833 ataques, es decir, deja escapar el 16,8 % de los ataques) con un volumen de falsos positivos (988) prácticamente idéntico al de IsolationForest (973). Es la mejor combinación observada de sensibilidad y coste en falsas alarmas.

-   LocalOutlierFactor es el caso extremo negativo: falla 7.071 ataques (más de la mitad de los 12.833 presentes en D2) y, además, produce el mayor número de falsos positivos (1.558). Su noción de anomalía basada en densidad local no captura bien la separación normal/ataque en este espacio de características.

-   OneClassSVM es el más conservador: registra los falsos positivos más bajos (824), pero al precio de 4.021 falsos negativos, casi el doble que el Autoencoder.

### Métricas de desempeño

La tabla siguiente recoge las métricas completas de los cuatro detectores sobre D2 (conjunto de 54 características; positivo = ataque):

  -----------------------------------------------------------------------------------------
  Detector             AUC-ROC   AUC-PR   Precision   Recall   F1      FPR     Tiempo (s)
  -------------------- --------- -------- ----------- -------- ------- ------- ------------
  IsolationForest      0.923     0.918    0.910       0.770    0.834   0.100   5,04

  OneClassSVM          0.836     0.889    0.914       0.687    0.784   0.085   28,34

  LocalOutlierFactor   0.807     0.740    0.787       0.449    0.572   0.160   16,42

  Autoencoder          0.929     0.909    0.915       0.832    0.872   0.102   40,56
  -----------------------------------------------------------------------------------------

Las curvas ROC y precision-recall de los cuatro detectores permiten comparar su capacidad discriminante con independencia del umbral concreto:

![](Resultados/docx/COMPARACION/media/media/image21.png)

![](Resultados/docx/COMPARACION/media/media/image22.png)

Tres observaciones se desprenden de las curvas y de la tabla:

\- El Autoencoder e IsolationForest forman un primer grupo claramente destacado (AUC-ROC 0.929 y 0.923 respectivamente), con curvas ROC casi solapadas; en AUC-PR IsolationForest es incluso ligeramente superior (0.918 frente a 0.909). La diferencia práctica entre ambos la marca el punto de operación: al umbral p95, el Autoencoder convierte esa capacidad discriminante en 6,2 puntos más de recall (0.832 frente a 0.770) con un FPR equivalente.

\- OneClassSVM queda en un escalón intermedio (AUC-ROC 0.836) y LocalOutlierFactor es claramente el más débil en todas las métricas basadas en ranking (AUC-ROC 0.807, AUC-PR 0.740).

\- En coste computacional, IsolationForest es con diferencia el más rápido (5 s frente a los 40,6 s del Autoencoder), un factor a considerar si el criterio de despliegue priorizase la latencia de reentrenamiento sobre el recall.

### Resultados finales

El Autoencoder resulta el mejor detector de anomalías del estudio, con F1 = 0.872 y recall = 0.832 a un FPR del 10,2 %, y es el seleccionado como etapa 1 del sistema híbrido (decisión H-2). IsolationForest queda muy cerca (F1 = 0.834, AUC-ROC 0.923) y constituye una alternativa razonable con un coste de entrenamiento ocho veces menor; como se verá en \[\[5.3 Resultados del sistema híbrido\]\], además, su perfil de detección por tipo de ataque es parcialmente complementario al del Autoencoder. LocalOutlierFactor es claramente el más débil de los cuatro en este problema (recall 0.449 con el mayor FPR, 16 %), aunque ---adelantando un hallazgo de la evaluación 0-day--- conserva valor puntual sobre tipos de ataque concretos que los demás fallan.

El resultado de OneClassSVM debe contextualizarse: su coste de entrenamiento O(n²) hace inviable ajustarlo con el conjunto de entrenamiento completo (el 80 % de D1, \~53.900 filas, tras reservar la validación), por lo que se entrenó con una submuestra reproducible de 20.000 flujos normales extraída de ese conjunto (véase \[\[4.4 Entrenamiento del modelo de detección de anomalías\]\]). Su posición intermedia (F1 = 0.784, con el FPR más bajo del grupo, 8,5 %) se obtiene, por tanto, con menos datos de entrenamiento que el resto, lo que limita la comparación en igualdad de condiciones; aun así, es el trato computacionalmente honesto que un despliegue real le daría.

Dos conclusiones operativas cierran la sección:

1\. La elección del Autoencoder para la cascada se apoya en el mejor equilibrio recall/FPR al punto de operación fijado, no solo en el AUC global.

2\. El FPR efectivo de la etapa 1 (\~10 %) es el precio estructural que el sistema híbrido paga por su sensibilidad, y condiciona toda la evaluación de \[\[5.3 Resultados del sistema híbrido\]\].

## Resultados del modelo de detección basado en firmas

Esta sección evalúa la etapa de clasificación por firmas del sistema: los cuatro algoritmos supervisados ---DecisionTree, RandomForest, KNN y HistGradientBoosting--- entrenados sobre D3 (solo ataques de tipos conocidos, 4 clases: dos, probe, r2l, u2r) con el mejor esquema de balanceo por algoritmo (véase \[\[4.5 Entrenamiento del modelo de detección basado en firmas\]\]).

### Matrices de confusión

Las matrices de confusión multiclase (4 clases de ataque) de los cuatro clasificadores sobre los 9.083 flujos de tipos conocidos de D2 son las siguientes:![](Resultados/docx/COMPARACION/media/media/image23.png)

![](Resultados/docx/COMPARACION/media/media/image24.png)![](Resultados/docx/COMPARACION/media/media/image25.png)![](Resultados/docx/COMPARACION/media/media/image26.png)

El patrón común a las cuatro matrices es una diagonal muy marcada en dos y probe (las clases mayoritarias y con firmas más nítidas), una clase r2l mayoritariamente bien resuelta pero con fugas, y una clase u2r con soporte mínimo (37 muestras) donde se concentran los errores relativos de todos los modelos.

### Métricas de desempeño

La tabla siguiente compara los cuatro algoritmos en validación cruzada (StratifiedKFold(5) sobre D3) y sobre D2:

  -----------------------------------------------------------------------------------------------------
  **Algoritmo**          **Balanceo**   **f1_macro (CV, D3)**   **f1_macro (D2)**   **Accuracy (D2)**
  ---------------------- -------------- ----------------------- ------------------- -------------------
  DecisionTree           class_weight   0.953                   0.746               0.913

  **RandomForest**       SMOTE          0.980                   **0.822**           **0.968**

  KNN                    SMOTE          0.945                   0.769               0.956

  HistGradientBoosting   SMOTE          0.969                   0.804               0.958
  -----------------------------------------------------------------------------------------------------

La brecha sistemática entre el f1_macro de validación cruzada (0.945--0.980) y el de D2 (0.746--0.822) refleja el desplazamiento distribucional D3→D2 propio del NSL-KDD: los tipos de ataque son los mismos, pero sus instancias en el test no se distribuyen como en el train. Es una brecha de generalización esperable, no un fallo de los modelos, y justifica que la comparación entre algoritmos se haga sobre D2 y no sobre la CV.

El desglose por categoría (F1 sobre D2, con el soporte de cada clase) muestra dónde se decide realmente la comparación:

  -----------------------------------------------------------------------------------------------------------------
  **Algoritmo**          **F1 dos (n=5.741)**   **F1 probe (n=1.106)**   **F1 r2l (n=2.199)**   **F1 u2r (n=37)**
  ---------------------- ---------------------- ------------------------ ---------------------- -------------------
  DecisionTree           0.961                  0.749                    0.912                  0.361

  RandomForest           0.998                  0.902                    0.937                  0.452

  KNN                    0.993                  0.927                    0.911                  0.245

  HistGradientBoosting   0.995                  0.869                    0.921                  0.432
  -----------------------------------------------------------------------------------------------------------------

-   **dos y probe** están esencialmente resueltas por todos los modelos (F1 ≥ 0.96 en dos para todos; en probe destacan KNN y RandomForest).

-   **r2l** es el caso intermedio: F1 entre 0.90 y 0.94, con precisión muy alta (≥ 0.97 en todos) pero recall entre 0.84 y 0.89 --- una fracción de los ataques r2l del test escapa a las firmas aprendidas.

-   **u2r es el punto débil universal**: con solo 37 muestras en D2 (y \~52 en el train), ningún algoritmo supera F1 = 0.452 (RandomForest); en el conjunto de ambas variantes de características el F1 de u2r oscila entre 0.17 y 0.45. KNN ilustra el dilema del desbalanceo: alcanza el mayor recall de u2r (0.757) pero con precisión 0.146, es decir, a base de sobre-predecir la clase. Ni SMOTE ni class_weight compensan del todo un soporte tan reducido.

### Comparación de los resultados de cada algoritmo

Sobre el conjunto primario de 54 características, el mejor clasificador de firmas es **RandomForest con SMOTE** (f1_macro = 0.822 y accuracy = 0.968 sobre D2, mejor F1 en tres de las cuatro categorías), y es el seleccionado como **etapa 2 del sistema híbrido** (decisión H-3). HistGradientBoosting queda segundo (0.804), y DecisionTree, aun siendo el más interpretable y el más rápido (1,8 s), paga su simplicidad sobre todo en probe (F1 0.749).

La comparación entre las variantes de 54 y 122 características aporta el hallazgo más relevante de la sección:

  ----------------------------------------------------------------------------------
  **Algoritmo**          **f1_macro D2 (54)**   **f1_macro D2 (122)**   **Δ**
  ---------------------- ---------------------- ----------------------- ------------
  DecisionTree           0.746                  0.731                   −0.015

  **RandomForest**       **0.822**              0.696                   **−0.126**

  KNN                    0.769                  0.753                   −0.016

  HistGradientBoosting   0.804                  0.713                   −0.091
  ----------------------------------------------------------------------------------

Con las 122 características, RandomForest **cae de 0.822 a 0.696** y deja de ser el mejor algoritmo (lo supera KNN, que apenas se mueve: 0.769 → 0.753). La cadena causal es consistente con los artefactos (el paso intermedio ---la memorización vía dummies--- es interpretación registrada en el contrato de decisiones, no una medición directa):

1.  Con 122 características, la búsqueda de hiperparámetros de RF elige max_depth=None (frente a max_depth=10 en 54), es decir, árboles sin límite de profundidad.

2.  Esa configuración maximiza el f1_macro de CV sobre D3 (0.9795, prácticamente idéntico al 0.9798 de la variante de 54): **el sobreajuste es invisible en validación cruzada**, porque las variables *dummy* adicionales del one-hot permiten memorizar particularidades de D3 que también están en sus propios folds.

3.  Sobre D2, esas particularidades no se sostienen y el f1_macro se desploma 12,6 puntos, con r2l como principal víctima (recall 0.889 → 0.626).

En contraste, KNN ---que no construye reglas sobre variables individuales sino distancias globales--- es casi insensible al exceso de dimensiones. La conclusión es directa: **la selección de características de [4.3 Preprocesamiento de los datasets](file:///C:\Users\francisco.lopez\KIKO_TFG\Working_Directory\4.3%20Preprocesamiento%20de%20los%20datasets) (sección 4.3.5) no solo redujo la dimensionalidad, sino que mejoró la generalización D3→D2 del clasificador de firmas**, al eliminar los grados de libertad con los que RF sobreajustaba. Este resultado es una de las dos patas empíricas que cerraron la decisión Q1/C a favor del conjunto de 54 características (la otra, el recall 0-day, se analiza en [5.3 Resultados del sistema híbrido](file:///C:\Users\francisco.lopez\KIKO_TFG\Working_Directory\5.3%20Resultados%20del%20sistema%20híbrido)).

## Resultados del sistema híbrido

Esta sección evalúa el sistema completo: la cascada Autoencoder → RandomForest sobre el conjunto primario de 54 características, con umbral de confianza UMBRAL_CONF = 0.5 para el enrutado a la clase unknown. La etapa 1 (detector de anomalías de \[\[5.1 Resultados del modelo de detección de anomalías\]\]) decide si un flujo es sospechoso; la etapa 2 (clasificador de firmas de \[\[5.2 Resultados del modelo de detección basado en firmas\]\]) asigna a cada sospechoso una categoría de ataque o, si su confianza máxima no alcanza el umbral, la etiqueta unknown (candidato a 0-day). La evaluación se realiza sobre D2 completo (22.544 flujos), incluidos los 3.750 ataques de los 17 tipos ausentes del entrenamiento.

\## Evaluación binaria (normal vs ataque)

Sobre D2 completo, el sistema híbrido obtiene en la decisión binaria normal/ataque: recall = 0.832, precision = 0.915, F1 = 0.872 y FPR = 0.102 (accuracy 0.860; VN = 8.723, FP = 988, FN = 2.158, VP = 10.675).

Evaluación multiclase --- matriz 5×6 con \"desconocido\"

El artefacto primario de la evaluación multiclase es la matriz de confusión de 5 clases reales × 6 predichas (las cinco categorías más la columna unknown), sobre D2 completo: ![](Resultados/docx/COMPARACION/media/media/image27.png)

Las métricas por alcance de la cascada son:

\| Alcance \| Métrica \| Valor \|

\|\-\--\|\-\--\|\-\--:\|

\| Binario (D2 completo, n = 22.544) \| F1 / FPR \| 0.872 / 0.102 \|

\| Categorías conocidas end-to-end (n = 9.083) \| precision_macro / recall_macro / f1_macro \| 0.915 / 0.671 / 0.748 \|

\| 5 clases, criterio conservador (n = 22.544) \| f1_macro (unknown = error) \| 0.641 \|

Dos lecturas importantes:

\- El coste del filtro. Sobre los mismos 9.083 ataques de tipo conocido, el clasificador de firmas aislado alcanzaba f1_macro = 0.822 (sección 5.2); la cascada end-to-end obtiene 0.748. Esos \~7,4 puntos no son un fallo del clasificador, sino el precio estructural de la cascada: los ataques conocidos que la etapa 1 marca como normales nunca llegan a la etapa 2, y una pequeña fracción adicional se enruta a unknown por baja confianza. Es el intercambio deliberado del diseño: se sacrifica parte del rendimiento sobre lo conocido a cambio de la capacidad de detectar lo desconocido, que un clasificador de firmas puro no tiene.

\- El f1_macro a 5 clases \"conservador\" (0.641) cuenta todo unknown como error, incluidos los 0-day correctamente enrutados a esa clase; infravalora por tanto al sistema híbrido y se reporta únicamente porque es la única métrica formalmente comparable con el baseline monolítico (véase el último apartado).

\### Calibración del umbral de confianza

El UMBRAL_CONF se calibró sin tocar D2: sobre probabilidades out-of-fold (cross_val_predict, StratifiedKFold(5)) del clasificador de firmas en D3, con una regla de presupuesto: elegir el umbral más alto de {0.4, 0.5, 0.6} cuyo recall macro OOF de las clases conocidas no caiga más de τ = 2 puntos porcentuales respecto al clasificador sin umbral (recall macro OOF de referencia: 0.980). Las columnas de D2 de la tabla siguiente son puramente informativas (análisis de sensibilidad); en ningún caso intervinieron en la elección.

\| UMBRAL_CONF \| Recall macro OOF (conocidas) \| Falsos unknown OOF \| f1_macro-5 conservador (D2) \| Recall 0-day global (D2) \| % 0-day detectados → unknown (D2) \|

\|\-\--:\|\-\--:\|\-\--:\|\-\--:\|\-\--:\|\-\--:\|

\| 0.4 \| 0.975 \| 0,003 % \| 0.643 \| 0.771 \| 1,8 % \|

\| 0.5 (elegido) \| 0.965 \| 0,031 % \| 0.641 \| 0.771 \| 13,4 % \|

\| 0.6 \| 0.944 \| 0,089 % \| 0.592 \| 0.771 \| 34,0 % \|

Con la regla τ = 2 pp, el umbral 0.5 es el elegido: su caída OOF es de 1,5 pp (0.980 → 0.965), mientras que 0.6 cae 3,6 pp y queda descartado.

El dato más revelador de la tabla es precisamente ese enrutado: con el umbral elegido, solo el 13,4 % de los 0-day detectados acaba en unknown; el \~86 % restante recibe con confianza alta una etiqueta de categoría conocida. El RandomForest, entrenado solo con los tipos de D3, resulta sobre-confiado ante datos fuera de su distribución: asignar probabilidades altas a lo nunca visto es un comportamiento conocido de los clasificadores cerrados. Elevar el umbral mejora el enrutado (34 % a 0.6) pero al precio de triplicar los falsos unknown sobre conocidas. Superar esta limitación exige técnicas de open-set recognition en lugar de un umbral sobre predict_proba; se recoge como línea futura en \[\[6.2 Líneas futuras\]\] (documento de trabajo EL_FUTURO.md).

\## Análisis de ataques desconocidos (0-day)

D2 contiene 3.750 flujos de 17 tipos de ataque ausentes del entrenamiento. La tabla siguiente muestra el recall de detección (\"marcado como sospechoso\") por tipo, para el detector de la cascada (Autoencoder) y, con fines de análisis, para los otros tres detectores de la sección 5.1 aplicando el umbral persistido de cada uno. Conforme al caveat P-2, cada detector se reporta junto a su FPR binario: los recalls no son comparables en igualdad de condiciones, porque cada detector alarma con distinta frecuencia sobre tráfico normal.

\| Tipo 0-day \| n \| Autoencoder (FPR 10,2 %) \| IsolationForest (FPR 10,0 %) \| OneClassSVM (FPR 8,5 %) \| LOF (FPR 16,0 %) \|

\|\-\--\|\-\--:\|\-\--:\|\-\--:\|\-\--:\|\-\--:\|

\| apache2 \| 737 \| 0.997 \| 0.995 \| 0.969 \| 0.716 \|

\| mscan \| 996 \| 0.980 \| 0.955 \| 0.843 \| 0.260 \|

\| saint \| 319 \| 0.972 \| 0.991 \| 0.975 \| 0.398 \|

\| processtable \| 685 \| 1.000 \| 0.511 \| 0.073 \| 0.362 \|

\| httptunnel \| 133 \| 0.977 \| 0.842 \| 0.842 \| 0.248 \|

\| snmpguess \| 331 \| 0.018 \| 0.740 \| 0.012 \| 0.027 \|

\| mailbomb \| 293 \| 0.000 \| 0.010 \| 0.017 \| 0.823 \|

\| snmpgetattack \| 178 \| 0.000 \| 0.152 \| 0.062 \| 0.084 \|

\| named \| 17 \| 0.529 \| 0.353 \| 0.176 \| 0.412 \|

\| ps \| 15 \| 0.667 \| 0.133 \| 0.067 \| 0.667 \|

\| sendmail \| 14 \| 0.714 \| 0.286 \| 0.286 \| 0.714 \|

\| xterm \| 13 \| 0.846 \| 0.615 \| 0.692 \| 0.692 \|

\| xlock \| 9 \| 0.333 \| 0.111 \| 0.000 \| 0.333 \|

\| xsnoop \| 4 \| 0.750 \| 0.250 \| 0.500 \| 0.500 \|

\| sqlattack \| 2 \| 1.000 \| 1.000 \| 1.000 \| 1.000 \|

\| udpstorm \| 2 \| 0.000 \| 1.000 \| 0.000 \| 0.000 \|

\| worm \| 2 \| 0.000 \| 0.000 \| 0.000 \| 0.000 \|

\| Global \| 3.750 \| 0.771 \| 0.737 \| 0.551 \| 0.401 \|

Del desglose por tipo emergen tres hallazgos que el agregado global oculta:

1\. Complementariedad de los detectores: ningún algoritmo domina por tipo. El Autoencoder ---el mejor detector global--- tiene puntos ciegos totales que otros cubren bien: falla mailbomb por completo (recall 0.00 sobre 293 flujos) mientras LocalOutlierFactor, el peor detector global, lo detecta al 0.82; y falla snmpguess (0.018 sobre 331) mientras IsolationForest lo detecta al 0.74. Elegir el detector por su métrica global deja, por tanto, recall 0-day sobre la mesa; un ensemble de detectores es la línea futura número uno del proyecto (\[\[6.2 Líneas futuras\]\], EL_FUTURO.md).

2\. snmpgetattack (n = 178) es un punto ciego universal: los cuatro detectores lo fallan (recall máximo 0.152, de IsolationForest), y el resultado se repite en la variante de 122 características. La explicación apunta al límite de la representación por-flujo del NSL-KDD, no a los modelos: se trata de tráfico SNMP cuyas conexiones individuales apenas se distinguen del tráfico normal en las características disponibles. Ningún ajuste de los detectores actuales puede recuperarlo; requeriría características de secuencia o temporales.

3\. Los tipos 0-day de mayor volumen (apache2, mscan, saint, processtable, que suman 2.737 de los 3.750 flujos) son detectados por el Autoencoder con recalls entre 0.97 y 1.00, lo que sostiene el agregado global de 0.771.

Como se indicó en el apartado anterior, la detección (etapa 1) y el enrutado a unknown (etapa 2 + umbral) son problemas distintos: de estos 0-day detectados, solo el 13,4 % termina etiquetado como unknown.

\## Comparación con el baseline RF monolítico

La comparación central de esta sección ---y la tesis del trabajo--- enfrenta el sistema híbrido al patrón dominante en la literatura sobre NSL-KDD: un RandomForest monolítico entrenado sobre todo el train (D1+D3, 5 clases, class_weight=\'balanced\'; véase baseline.py) y evaluado sobre D2 completo.

\| Métrica \| Híbrido (AE → RF, 54) \| Baseline RF monolítico (54) \|

\|\-\--\|\-\--:\|\-\--:\|

\| Recall 0-day global \| 0.771 (2.890/3.750) \| 0.150 (561/3.750) \|

\| FPR binario \| 0.102 \| 0.027 \|

\| Recall binario (ataques) \| 0.832 \| 0.575 \|

\| f1_macro (CV sobre train) \| --- \| 0.909 \|

\| f1_macro 5 clases sobre D2 \| 0.641 (conservador, unknown = error) \| 0.472 \|

\| Recall r2l (D2) \| --- (véase nota) \| 0.004 \|

\| Recall u2r (D2) \| --- (véase nota) \| 0.010 \|

(Nota: el híbrido no produce un recall por clase a 5 clases directamente comparable ---sus errores incluyen el enrutado a unknown---; su rendimiento por categoría conocida se reportó como macro en el segundo apartado, y la comparación por clase puede leerse en las matrices de confusión.)

![](Resultados/docx/COMPARACION/media/media/image27.png)

![](Resultados/docx/COMPARACION/media/media/image28.png)\
\
Los resultados se resumen en cuatro puntos:

\- Detección 0-day, la métrica para la que se diseñó el híbrido: 0.771 frente a 0.150 --- una mejora de aproximadamente 5×. El desglose por tipo del baseline muestra que su detección 0-day es casi anecdótica: solo saint (0.987) se detecta bien ---presumiblemente por su parecido con tipos probe del train---, mientras mscan (0.151), apache2 (0.121) y prácticamente todo lo demás (incluidos processtable, snmpguess, mailbomb y snmpgetattack, todos con recall 0.000) resultan invisibles. Es la limitación estructural esperada: un clasificador supervisado cerrado no puede alarmar sobre patrones de los que no tiene ejemplos.

\- Caveat obligado (P-2): los dos sistemas no operan al mismo FPR. El híbrido alarma sobre el 10,2 % del tráfico normal; el baseline, solo sobre el 2,7 %. Parte de la ventaja 0-day del híbrido procede, sencillamente, de que alarma más. El recall 0-day no debe leerse aislado de esa columna. Dicho esto, la diferencia no se explica solo por el punto de operación: el desglose por tipo muestra que el baseline es estructuralmente incapaz de ver la mayoría de los tipos 0-day (recalls exactamente 0), no meramente menos sensible.

\- El baseline también falla donde su CV prometía: su f1_macro cae de 0.909 en validación cruzada sobre el train a 0.472 sobre D2, y las clases minoritarias colapsan pese a class_weight=\'balanced\': recall de r2l = 0.004 (12 de 2.754 ataques) y de u2r = 0.010 --- la clase normal, mayoritaria en su entrenamiento, absorbe esas categorías. El \"\~99 % de accuracy\" que la literatura obtiene con este patrón sobre particiones del train no sobrevive al test oficial del NSL-KDD.

\- Incluso en la métrica que perjudica al híbrido, este gana: el f1_macro a 5 clases conservador del híbrido (0.641), que como se argumentó (H-6) cuenta como error incluso los 0-day correctamente enrutados a unknown y por tanto lo infravalora, supera con claridad el 0.472 del baseline.

En conjunto, la comparación confirma la hipótesis que motivó la arquitectura: el clasificador monolítico es competitivo únicamente sobre los patrones que ya conoce, mientras que la cascada híbrida, a cambio de un FPR mayor y de un coste moderado sobre los ataques conocidos (0.822 → 0.748), aporta la capacidad ---esencialmente ausente en el baseline--- de detectar ataques nunca vistos.

## Conclusiones del capítulo

Este capítulo ha evaluado por separado las dos etapas del sistema y, después, el sistema híbrido completo frente al patrón dominante en la literatura sobre NSL-KDD. La lectura conjunta de los resultados permite extraer las conclusiones siguientes.

\## Sobre cada etapa por separado

Etapa 1 (anomalías). De los cuatro detectores comparados con idéntico protocolo (mismo umbral por percentil 95 sobre validación de D1, mismas métricas sobre D2), el Autoencoder es el mejor (F1 = 0.872, recall = 0.832 con FPR del 10,2 %), seguido de cerca por IsolationForest (F1 = 0.834) a un coste de entrenamiento ocho veces menor. LocalOutlierFactor es el más débil en conjunto y OneClassSVM queda en un escalón intermedio, condicionado por el submuestreo que exige su coste O(n²). La conclusión operativa es que el Autoencoder ofrece el mejor equilibrio recall/FPR en el punto de operación fijado, y por ello se selecciona como etapa 1 de la cascada.

Etapa 2 (firmas). Sobre los ataques de tipo conocido, el mejor clasificador es RandomForest con SMOTE (f1_macro = 0.822 sobre D2), seguido de HistGradientBoosting. Las categorías dos y probe están esencialmente resueltas por todos los algoritmos; r2l queda en un nivel intermedio; y u2r es el punto débil universal (F1 ≤ 0.452), un límite impuesto por su soporte mínimo (\~52 muestras de entrenamiento) que ni SMOTE ni el ajuste por coste (class_weight) compensan del todo. Esta etapa arrojó además un resultado metodológico relevante: la selección de características a 54 (sección 4.3.5) no solo redujo la dimensionalidad, sino que mejoró la generalización D3→D2 del clasificador, al eliminar los grados de libertad con los que RandomForest sobreajustaba las 122 características (caída de 0.822 a 0.696 con el conjunto completo, invisible en validación cruzada).

\## Sobre el sistema híbrido: la tesis del trabajo

La comparación central del capítulo enfrenta la cascada Autoencoder → RandomForest a un RandomForest monolítico ---el enfoque que \"todo el mundo acaba usando\" para este dataset--- y confirma la hipótesis que motivó la arquitectura:

\- En la métrica para la que el sistema se diseñó, la detección de ataques nunca vistos (0-day), el híbrido alcanza un recall global de 0.771 frente al 0.150 del baseline (≈ 5×). Y no es solo cuestión de sensibilidad: el desglose por tipo muestra que el baseline es estructuralmente incapaz de ver la mayoría de los tipos 0-day (recall exactamente 0 en processtable, snmpguess, mailbomb, snmpgetattack y otros), como corresponde a un clasificador supervisado cerrado.

\- El baseline también falla donde su validación cruzada prometía: su f1_macro se desploma de 0.909 (CV sobre el train) a 0.472 sobre D2, con las clases minoritarias colapsadas (recall r2l = 0.004, u2r = 0.010). El célebre \"\~99 % de accuracy\" de la literatura no sobrevive al test oficial del NSL-KDD.

\- Incluso en la métrica que penaliza al híbrido ---el f1_macro a 5 clases conservador, que cuenta como error los 0-day correctamente enrutados a unknown--- el sistema (0.641) supera con claridad al baseline (0.472).

\## Los caveats que acompañan a la tesis

Las conclusiones anteriores se sostienen, pero deben leerse con tres matices que este capítulo ha declarado explícitamente y que forman parte del rigor del análisis:

1\. Los dos sistemas no operan al mismo FPR (P-2). El híbrido alarma sobre el 10,2 % del tráfico normal; el baseline, solo sobre el 2,7 %. Parte de la ventaja 0-day procede de que el híbrido, sencillamente, alarma más. El recall 0-day nunca debe leerse aislado de su FPR --- de ahí que toda la tabla 0-day reporte ambos. Aun así, la incapacidad estructural del baseline (recalls exactamente 0) no se explica por el punto de operación.

2\. La cascada tiene un coste sobre lo conocido. El clasificador de firmas aislado lograba f1_macro = 0.822 sobre los ataques conocidos; la cascada end-to-end obtiene 0.748. Esos \~7,4 puntos son el precio estructural de filtrar por la etapa 1: es el intercambio deliberado de sacrificar rendimiento sobre lo conocido a cambio de la capacidad de ver lo desconocido.

3\. La evaluación binaria del híbrido coincide con la de la etapa 1 por construcción (H-5), no por mérito propio de la fusión: la aportación de la cascada no es binaria, sino convertir el \"sospechoso\" en una categoría accionable y separar lo conocido de los candidatos a 0-day.

\## Hallazgos que trascienden la comparación 54 vs 122

Más allá de cerrar la decisión sobre el conjunto de características (Q1/C, a favor de 54 para ambas etapas), la evaluación del híbrido destapó tres hallazgos que son, en realidad, las líneas futuras mejor fundamentadas del proyecto (recogidas en \[\[6.2 Líneas futuras\]\]):

\- Los detectores de anomalías son complementarios por tipo: ninguno domina. El Autoencoder falla mailbomb por completo (recall 0.00) mientras LocalOutlierFactor lo detecta al 0.82; falla snmpguess (0.018) mientras IsolationForest lo detecta al 0.74. Elegir un único detector por su AUC global deja recall 0-day sobre la mesa: un ensemble de detectores es la mejora número uno.

\- El RandomForest está sobre-confiado ante lo desconocido: de los 0-day que la etapa 1 sí detecta, solo el 13,4 % se enruta a unknown; el resto recibe con confianza alta una etiqueta conocida errónea. Superarlo exige reconocimiento de conjunto abierto (open-set) en lugar de un umbral sobre predict_proba.

\- snmpgetattack es un punto ciego universal (los cuatro detectores lo fallan, en ambos conjuntos de características): un límite de la representación por-flujo del NSL-KDD, no de los modelos, que ningún ajuste de estos puede recuperar.

En síntesis, el capítulo demuestra con datos que un enfoque híbrido orientado a la detección de lo desconocido aporta una capacidad que el clasificador monolítico ---competitivo solo sobre lo que ya conoce--- no tiene, y hace explícito el precio (más falsas alarmas, coste sobre lo conocido) al que se obtiene esa capacidad. Estas conclusiones se elevan al plano global del proyecto en \[\[6.1 Conclusiones\]\] y sus prolongaciones se detallan en \[\[6.2 Líneas futuras\]\].

# Conclusiones

## Conclusiones

Este trabajo se propuso implementar un sistema de detección de intrusiones híbrido en red (H-NIDS) que combinara detección por firmas y detección por anomalías, y evaluar con datos si esa combinación aporta algo frente al enfoque supervisado que domina la literatura sobre el NSL-KDD. Las conclusiones se ordenan según el grado de cumplimiento de los objetivos planteados en \[\[1.3 Objetivo\]\], para cerrar después con la validación de la tesis y sus limitaciones.

### Grado de cumplimiento de los objetivos

Objetivo general --- implementar un H-NIDS. Cumplido. El sistema se materializó como una cascada de dos etapas (detección de anomalías → clasificación por firmas), diseñada en el \[\[3.2 Arquitectura del sistema\|capítulo 3\]\], implementada en el \[\[4.1 Tecnologías utilizadas\|capítulo 4\]\] y evaluada de forma integral en el \[\[5.3 Resultados del sistema híbrido\|capítulo 5\]\].

Sobre los objetivos específicos:

\- Investigar los dos métodos (firmas y anomalías). Cumplido y ampliado más allá de lo mínimo: en lugar de un algoritmo por método, se compararon cuatro algoritmos por etapa bajo un protocolo idéntico (IsolationForest, OneClassSVM, LocalOutlierFactor y un autoencoder para anomalías; DecisionTree, RandomForest, KNN y HistGradientBoosting para firmas). De la etapa de firmas se extrajeron además reglas interpretables, en la línea de un IDS clásico.

\- Revisar y preprocesar el NSL-KDD. Cumplido. Se analizó la estructura del dataset (\[\[4.2 Base de datos utilizada\]\]) y se construyó un pipeline de preprocesamiento reproducible que corrigió un fallo de codificación one-hot, justificó la normalización anti-leakage y aplicó una selección de características (122 → 54) que, además de reducir la dimensionalidad, mejoró la generalización del clasificador de firmas.

\- Entrenar y validar los modelos. Cumplido. Ambas etapas se entrenaron con sus subconjuntos especializados (D1 solo normal, D3 solo ataques) bajo una disciplina anti-leakage estricta ---umbrales fijados sin ver el test, SMOTE dentro de cada fold, calibración por validación cruzada out-of-fold--- y se persistieron para inferencia reproducible.

\- Estudiar los resultados. Cumplido. El capítulo 5 evaluó cada etapa por separado y el sistema completo sobre el test oficial, con un análisis específico de la detección de ataques 0-day y una comparación honesta frente a un baseline monolítico.

### Validación de la tesis del híbrido

La hipótesis central del trabajo ---que un enfoque híbrido orientado a lo desconocido aporta una capacidad que un clasificador supervisado monolítico no tiene--- queda validada con datos. Frente a un RandomForest monolítico entrenado sobre todo el tráfico (el patrón que \"todo el mundo acaba usando\" para este dataset), el sistema híbrido multiplica por aproximadamente cinco la detección de ataques 0-day (recall global 0.771 frente a 0.150), y el desglose por tipo muestra que la diferencia no es solo de sensibilidad: el baseline es estructuralmente incapaz de ver la mayoría de los tipos nunca vistos, mientras la etapa de anomalías los detecta como desviaciones del tráfico normal. El baseline confirma además, con su desplome de f1_macro de 0.909 en validación cruzada a 0.472 sobre el test oficial, que el célebre \"\~99 % de accuracy\" de la literatura es un espejismo del propio conjunto de entrenamiento.

La conclusión de fondo es que firmas y anomalías no compiten, sino que se complementan: las firmas clasifican con precisión lo conocido; las anomalías cubren el punto ciego de las firmas ---lo nuevo---; y la cascada las combina sin que el clasificador de firmas condene tráfico legítimo. El precio de esa capacidad, que el trabajo declara abiertamente, es una tasa de falsas alarmas mayor y un coste moderado sobre la clasificación de los ataques ya conocidos.

### Limitaciones

El rigor del análisis exige reconocer las limitaciones del sistema, todas documentadas con datos a lo largo del capítulo 5:

\- Tasa de falsos positivos condicionada por el drift. El detector de anomalías opera a un FPR efectivo del \~10 % sobre el test, por encima del \~5 % de diseño, debido al desplazamiento distribucional entre el tráfico normal de entrenamiento y el de test propio del NSL-KDD. Buena parte de la ventaja 0-day del híbrido se obtiene, en efecto, alarmando más; ambas cifras deben leerse juntas.

\- Clases minoritarias u2r y r2l. Con muy pocas muestras de entrenamiento (del orden de decenas para u2r), ningún algoritmo ni técnica de balanceo (SMOTE, class_weight) logra un rendimiento sólido sobre ellas. Es el punto débil universal de la etapa de firmas.

\- Enrutado a \"desconocido\" limitado. De los 0-day que el sistema sí detecta, solo una fracción pequeña acaba correctamente etiquetada como desconocido; el clasificador de firmas, cerrado, tiende a asignar con confianza excesiva una categoría conocida a lo que nunca ha visto.

\- Tipos ciegos por el propio dataset. Algún tipo de ataque (snmpgetattack) resulta indetectable para los cuatro detectores: es un límite de la representación por-flujo del NSL-KDD, no de los modelos, que ningún ajuste de estos puede superar.

Estas limitaciones no invalidan la tesis ---se sostiene sobre la detección de 0-day, donde el híbrido gana con claridad---, pero delimitan con honestidad su alcance y son, en buena medida, el punto de partida de las líneas futuras del trabajo, que se desarrollan en \[\[6.2 Líneas futuras\]\].

## Líneas futuras

# 

###### Columnas del dataset NSL-KDD

####### Columnas del dataset NSL-KDD

Este apéndice recoge la relación completa de las 41 características de cada conexión del NSL-KDD, más las etiquetas (tipo de ataque específico y categoría) tal como las maneja el pipeline de este trabajo. Es el detalle de referencia que complementa la vista por grupos de \[\[4.2 Base de datos utilizada\]\].

Cada registro del dataset describe una conexión TCP/IP resumida en 41 atributos, seguidos de la etiqueta de clase y un nivel de dificultad. Los 41 atributos se agrupan tradicionalmente en cuatro bloques: básicos (extraídos directamente de la cabecera de la conexión), de contenido (obtenidos inspeccionando el payload, orientados a ataques R2L/U2R que no se delatan por volumen), de tráfico basados en tiempo (estadísticas sobre una ventana de 2 segundos) y de tráfico basados en host (estadísticas sobre las últimas 100 conexiones al mismo destino).

######## Características básicas (1--9)

  ---------------------------------------------------------------------------------------------------------------------------
  **\#**   **Nombre**       **Tipo**     **Descripción**
  -------- ---------------- ------------ ------------------------------------------------------------------------------------
  1        duration         Continua     Duración de la conexión en segundos.

  2        protocol_type    Categórica   Protocolo de transporte: tcp, udp o icmp.

  3        service          Categórica   Servicio de red del destino (http, ftp, smtp, private, domain_u...). \~70 valores.

  4        flag             Categórica   Estado de la conexión al terminar (SF, S0, REJ, RSTR...). 11 valores.

  5        src_bytes        Continua     Bytes enviados del origen al destino.

  6        dst_bytes        Continua     Bytes enviados del destino al origen.

  7        land             Binaria      1 si origen y destino tienen la misma IP y puerto (indicio del ataque *land*).

  8        wrong_fragment   Discreta     Número de fragmentos \"erróneos\" en la conexión.

  9        urgent           Discreta     Número de paquetes con el bit *urgent* activado.
  ---------------------------------------------------------------------------------------------------------------------------

######## Características de contenido (10--22)

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **\#**   **Nombre**           **Tipo**   **Descripción**
  -------- -------------------- ---------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  10       hot                  Discreta   Número de indicadores \"sensibles\" (accesos a directorios de sistema, ejecución de programas...).

  11       num_failed_logins    Discreta   Intentos de inicio de sesión fallidos.

  12       logged_in            Binaria    1 si el inicio de sesión tuvo éxito.

  13       num_compromised      Discreta   Número de condiciones \"comprometidas\" observadas.

  14       root_shell           Binaria    1 si se obtuvo una shell de *root*.

  15       su_attempted         Discreta   1 si se intentó el comando su root.

  16       num_root             Discreta   Número de accesos u operaciones como *root*.

  17       num_file_creations   Discreta   Operaciones de creación de ficheros.

  18       num_shells           Discreta   Número de *shells* abiertas.

  19       num_access_files     Discreta   Operaciones sobre ficheros de control de acceso.

  20       num_outbound_cmds    Discreta   Comandos salientes en una sesión FTP. **Constante a 0** en todo el NSL-KDD (por eso el filtro de varianza la elimina, véase [4.3 Preprocesamiento de los datasets](file:///C:\Users\francisco.lopez\KIKO_TFG\Working_Directory\4.3%20Preprocesamiento%20de%20los%20datasets) sección 4.3.5).

  21       is_host_login        Binaria    1 si el login pertenece a la lista de *hosts* de acceso.

  22       is_guest_login       Binaria    1 si el inicio de sesión es de invitado (*guest*).
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

######## Características de tráfico basadas en tiempo (23--31)

Calculadas sobre las conexiones de los 2 segundos anteriores. Orientadas a detectar ataques de volumen (DoS) y de sondeo (Probe).

  -------------------------------------------------------------------------------------------------------------
  **\#**   **Nombre**           **Tipo**   **Descripción**
  -------- -------------------- ---------- --------------------------------------------------------------------
  23       count                Discreta   Conexiones al **mismo host destino** en la ventana.

  24       srv_count            Discreta   Conexiones al **mismo servicio** en la ventana.

  25       serror_rate          Continua   \% de conexiones (mismo host) con error de tipo SYN (s0/s1/s2/s3).

  26       srv_serror_rate      Continua   Ídem, referido al mismo servicio.

  27       rerror_rate          Continua   \% de conexiones (mismo host) con error REJ.

  28       srv_rerror_rate      Continua   Ídem, referido al mismo servicio.

  29       same_srv_rate        Continua   \% de conexiones al mismo servicio.

  30       diff_srv_rate        Continua   \% de conexiones a servicios distintos.

  31       srv_diff_host_rate   Continua   \% de conexiones (mismo servicio) a hosts distintos.
  -------------------------------------------------------------------------------------------------------------

######## Características de tráfico basadas en host (32--41)

  ----------------------------------------------------------------------------------------------------
  **\#**   **Nombre**                    **Tipo**   **Descripción**
  -------- ----------------------------- ---------- --------------------------------------------------
  32       dst_host_count                Discreta   Conexiones al mismo host destino.

  33       dst_host_srv_count            Discreta   Conexiones al mismo servicio en el host destino.

  34       dst_host_same_srv_rate        Continua   \% de esas conexiones al mismo servicio.

  35       dst_host_diff_srv_rate        Continua   \% a servicios distintos.

  36       dst_host_same_src_port_rate   Continua   \% desde el mismo puerto origen.

  37       dst_host_srv_diff_host_rate   Continua   \% (mismo servicio) hacia hosts distintos.

  38       dst_host_serror_rate          Continua   \% con error SYN en el host destino.

  39       dst_host_srv_serror_rate      Continua   Ídem, por servicio.

  40       dst_host_rerror_rate          Continua   \% con error REJ en el host destino.

  41       dst_host_srv_rerror_rate      Continua   Ídem, por servicio.
  ----------------------------------------------------------------------------------------------------

######## Etiquetas: tipos de ataque y categorías

El pipeline (program.py) codifica las etiquetas en dos niveles: el tipo de ataque específico (40 valores, incluido normal) y su agrupación en 5 categorías. Los mapeos siguientes son los que produce el LabelEncoder y se persisten en Resultados\\specialized_nsl_kdd_mappings_and_info.txt; se reproducen aquí para poder interpretar las matrices de confusión y los ficheros y_attack/y_category del capítulo 5.

\### Codificación de categorías

\| Código \| Categoría \|

\|\-\--:\|\-\--\|

\| 0 \| DOS \|

\| 1 \| NORMAL \|

\| 2 \| PROBE \|

\| 3 \| R2L \|

\| 4 \| U2R \|

\### Tipos de ataque específicos agrupados por categoría

La tabla asigna cada uno de los 40 tipos a su categoría. Se marcan con ★ los 17 tipos que solo aparecen en el conjunto de test (D2) y no en el de entrenamiento --- los \"0-day\" del experimento, únicos detectables por la etapa de anomalías (véase \[\[5.3 Resultados del sistema híbrido\]\]).

\| Categoría \| Tipos de ataque \|

\|\-\--\|\-\--\|

\| NORMAL \| normal \|

\| DOS (Denial of Service) \| back, land, neptune, pod, smurf, teardrop, mailbomb ★, apache2 ★, processtable ★, udpstorm ★ \|

\| PROBE (sondeo/reconocimiento) \| ipsweep, nmap, portsweep, satan, mscan ★, saint ★ \|

\| R2L (Remote to Local) \| ftp_write, guess_passwd, imap, multihop, phf, spy, warezclient, warezmaster, sendmail ★, named ★, snmpgetattack ★, snmpguess ★, xlock ★, xsnoop ★, worm ★ \|

\| U2R (User to Root) \| buffer_overflow, loadmodule, perl, rootkit, httptunnel ★, ps ★, sqlattack ★, xterm ★ \|

####### Métricas de desempeño

####### 

[]{#_Toc236498770 .anchor}Bibliografía

1.  <https://www.channelpartner.es/seguridad/principales-ciberataques-en-espana-en-2024/>

2.  **\"Computer Security Threat Monitoring and Surveillance\"**. James P. Anderson Co.

3.  Denning, Dorothy E. (1987). **\"An Intrusion-Detection Model\"**. *IEEE Transactions on Software Engineering*, SE-13(2), 222-232

4.  Chio, C., & Freeman, D. (2018) Machine Learning & Security: Protecting Systems with Data and Algorithms. O\'Reilly Media.

5.  Geron, A. (2019). Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow (2nd Ed.). O\'Reilly Media.

6.  Goodfellow, I., Bengio, Y., & Courville, A. (2016). Deep Learning. MIT Press.

7.  Murphy, K. P. (2012). Machine Learning: A Probabilistic Perspective. MIT Press.

8.  \"Computer Security : Principles and Practice\" William Stallings

9.  <https://students.aiu.edu/submissions/profiles/resources/onlineBook/j5V2a3_Computer_Security_Principles.pdf>

10. <https://www.ccn-cert.cni.es/publico/seriesCCN-STIC/series/400-Guias_Generales/401-glosario_abreviaturas/index.html?n=189.html>

11. <https://www.usenix.org/legacy/publications/library/proceedings/lisa99/roesch.html>

###### Nombre del apéndice A

Este texto está escrito en estilo Normal. El texto del título del apéndice está escrito en estilo "Título 6".

Este texto está escrito con el estilo "Código fuente".

####### Este texto está escrito en estilo Título 7. Es el equivalente a Título 2 para los apéndices

Este texto está escrito en estilo Normal.

######## Este texto está escrito en estilo Título 8. Es el equivalente a Título 3 para los apéndices. 

Para introducir una Figura/Tabla en un apéndice, debe proceder igual que para hacerlo en un capítulo normal pero seleccionado el tipo "Figura en Apéndice" o "Tabla en Apéndice", esto hará que se numeren automáticamente con la letra del apéndice. A continuación se muestran dos ejemplos.

<figure>
<img src="Resultados/docx/COMPARACION/media/media/image29.emf" />
<figcaption><p>Figura en Apéndice A.1. Ejemplo de pie de figura en apéndice.</p></figcaption>
</figure>

  ----------------------- ----------------------- -----------------------
                                                  

                                                  
  ----------------------- ----------------------- -----------------------

  : Tabla en Apéndice A.1. Ejemplo de pie de tabla en apéndice.
