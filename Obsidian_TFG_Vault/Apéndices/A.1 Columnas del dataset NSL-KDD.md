---
titulo: "Apéndice A.1 — Columnas del dataset NSL-KDD"
numero: "A.1"
estado: borrador
---

# A.1 Columnas del dataset NSL-KDD

Este apéndice recoge la relación completa de las **41 características** de cada conexión del NSL-KDD, más las **etiquetas** (tipo de ataque específico y categoría) tal como las maneja el pipeline de este trabajo. Es el detalle de referencia que complementa la vista por grupos de [[4.2 Base de datos utilizada]].

Cada registro del dataset describe una conexión TCP/IP resumida en 41 atributos, seguidos de la etiqueta de clase y un nivel de dificultad. Los 41 atributos se agrupan tradicionalmente en cuatro bloques: **básicos** (extraídos directamente de la cabecera de la conexión), **de contenido** (obtenidos inspeccionando el payload, orientados a ataques R2L/U2R que no se delatan por volumen), **de tráfico basados en tiempo** (estadísticas sobre una ventana de 2 segundos) y **de tráfico basados en host** (estadísticas sobre las últimas 100 conexiones al mismo destino).

## A.1.1 Características básicas (1–9)

| # | Nombre | Tipo | Descripción |
|---:|---|---|---|
| 1 | `duration` | Continua | Duración de la conexión en segundos. |
| 2 | `protocol_type` | Categórica | Protocolo de transporte: `tcp`, `udp` o `icmp`. |
| 3 | `service` | Categórica | Servicio de red del destino (`http`, `ftp`, `smtp`, `private`, `domain_u`…). ~70 valores. |
| 4 | `flag` | Categórica | Estado de la conexión al terminar (`SF`, `S0`, `REJ`, `RSTR`…). 11 valores. |
| 5 | `src_bytes` | Continua | Bytes enviados del origen al destino. |
| 6 | `dst_bytes` | Continua | Bytes enviados del destino al origen. |
| 7 | `land` | Binaria | 1 si origen y destino tienen la misma IP y puerto (indicio del ataque *land*). |
| 8 | `wrong_fragment` | Discreta | Número de fragmentos "erróneos" en la conexión. |
| 9 | `urgent` | Discreta | Número de paquetes con el bit *urgent* activado. |

## A.1.2 Características de contenido (10–22)

| # | Nombre | Tipo | Descripción |
|---:|---|---|---|
| 10 | `hot` | Discreta | Número de indicadores "sensibles" (accesos a directorios de sistema, ejecución de programas…). |
| 11 | `num_failed_logins` | Discreta | Intentos de inicio de sesión fallidos. |
| 12 | `logged_in` | Binaria | 1 si el inicio de sesión tuvo éxito. |
| 13 | `num_compromised` | Discreta | Número de condiciones "comprometidas" observadas. |
| 14 | `root_shell` | Binaria | 1 si se obtuvo una shell de *root*. |
| 15 | `su_attempted` | Discreta | 1 si se intentó el comando `su root`. |
| 16 | `num_root` | Discreta | Número de accesos u operaciones como *root*. |
| 17 | `num_file_creations` | Discreta | Operaciones de creación de ficheros. |
| 18 | `num_shells` | Discreta | Número de *shells* abiertas. |
| 19 | `num_access_files` | Discreta | Operaciones sobre ficheros de control de acceso. |
| 20 | `num_outbound_cmds` | Discreta | Comandos salientes en una sesión FTP. **Constante a 0** en todo el NSL-KDD (por eso el filtro de varianza la elimina, véase [[4.3 Preprocesamiento de los datasets]] §4.3.5). |
| 21 | `is_host_login` | Binaria | 1 si el login pertenece a la lista de *hosts* de acceso. |
| 22 | `is_guest_login` | Binaria | 1 si el inicio de sesión es de invitado (*guest*). |

## A.1.3 Características de tráfico basadas en tiempo (23–31)

> Calculadas sobre las conexiones de los **2 segundos** anteriores. Orientadas a detectar ataques de volumen (DoS) y de sondeo (Probe).

| # | Nombre | Tipo | Descripción |
|---:|---|---|---|
| 23 | `count` | Discreta | Conexiones al **mismo host destino** en la ventana. |
| 24 | `srv_count` | Discreta | Conexiones al **mismo servicio** en la ventana. |
| 25 | `serror_rate` | Continua | % de conexiones (mismo host) con error de tipo `SYN` (`s0`/`s1`/`s2`/`s3`). |
| 26 | `srv_serror_rate` | Continua | Ídem, referido al mismo servicio. |
| 27 | `rerror_rate` | Continua | % de conexiones (mismo host) con error `REJ`. |
| 28 | `srv_rerror_rate` | Continua | Ídem, referido al mismo servicio. |
| 29 | `same_srv_rate` | Continua | % de conexiones al mismo servicio. |
| 30 | `diff_srv_rate` | Continua | % de conexiones a servicios distintos. |
| 31 | `srv_diff_host_rate` | Continua | % de conexiones (mismo servicio) a hosts distintos. |

## A.1.4 Características de tráfico basadas en host (32–41)

> Calculadas sobre las **últimas 100 conexiones** al mismo host destino. Capturan patrones de ataque lentos, que escapan a la ventana de 2 segundos.

| # | Nombre | Tipo | Descripción |
|---:|---|---|---|
| 32 | `dst_host_count` | Discreta | Conexiones al mismo host destino. |
| 33 | `dst_host_srv_count` | Discreta | Conexiones al mismo servicio en el host destino. |
| 34 | `dst_host_same_srv_rate` | Continua | % de esas conexiones al mismo servicio. |
| 35 | `dst_host_diff_srv_rate` | Continua | % a servicios distintos. |
| 36 | `dst_host_same_src_port_rate` | Continua | % desde el mismo puerto origen. |
| 37 | `dst_host_srv_diff_host_rate` | Continua | % (mismo servicio) hacia hosts distintos. |
| 38 | `dst_host_serror_rate` | Continua | % con error `SYN` en el host destino. |
| 39 | `dst_host_srv_serror_rate` | Continua | Ídem, por servicio. |
| 40 | `dst_host_rerror_rate` | Continua | % con error `REJ` en el host destino. |
| 41 | `dst_host_srv_rerror_rate` | Continua | Ídem, por servicio. |

> [!note] Etiquetas del registro
> Además de las 41 características, cada fila del NSL-KDD trae una etiqueta con el **nombre del ataque** (o `normal`) y un campo numérico de **dificultad** (proporción de clasificadores del estudio original que acertaron esa fila). El campo de dificultad no se usa como característica en este trabajo.

---

## A.1.5 Etiquetas: tipos de ataque y categorías

El pipeline (`program.py`) codifica las etiquetas en dos niveles: el **tipo de ataque específico** (40 valores, incluido `normal`) y su agrupación en **5 categorías**. Los mapeos siguientes son los que produce el `LabelEncoder` y se persisten en `Resultados\specialized_nsl_kdd_mappings_and_info.txt`; se reproducen aquí para poder interpretar las matrices de confusión y los ficheros `y_attack`/`y_category` del capítulo 5.

### Codificación de categorías

| Código | Categoría |
|---:|---|
| 0 | DOS |
| 1 | NORMAL |
| 2 | PROBE |
| 3 | R2L |
| 4 | U2R |

### Tipos de ataque específicos agrupados por categoría

La tabla asigna cada uno de los 40 tipos a su categoría. Se marcan con **★** los **17 tipos que solo aparecen en el conjunto de test (D2) y no en el de entrenamiento** — los "0-day" del experimento, únicos detectables por la etapa de anomalías (véase [[5.3 Resultados del sistema híbrido]]).

| Categoría | Tipos de ataque |
|---|---|
| **NORMAL** | `normal` |
| **DOS** (Denial of Service) | `back`, `land`, `neptune`, `pod`, `smurf`, `teardrop`, `mailbomb` ★, `apache2` ★, `processtable` ★, `udpstorm` ★ |
| **PROBE** (sondeo/reconocimiento) | `ipsweep`, `nmap`, `portsweep`, `satan`, `mscan` ★, `saint` ★ |
| **R2L** (Remote to Local) | `ftp_write`, `guess_passwd`, `imap`, `multihop`, `phf`, `spy`, `warezclient`, `warezmaster`, `sendmail` ★, `named` ★, `snmpgetattack` ★, `snmpguess` ★, `xlock` ★, `xsnoop` ★, `worm` ★ |
| **U2R** (User to Root) | `buffer_overflow`, `loadmodule`, `perl`, `rootkit`, `httptunnel` ★, `ps` ★, `sqlattack` ★, `xterm` ★ |

> [!info] Trazabilidad
> Mapeos de etiquetas: `Resultados\specialized_nsl_kdd_mappings_and_info.txt` (secciones 1–3). La relación de las 17 clases exclusivas de D2 la calcula y lista `validacion.py`. La descripción de las 41 características procede de la documentación original del KDD Cup 1999 (Lee y Stolfo) heredada por el NSL-KDD; véase la parte teórica en [[4.2 Base de datos utilizada]].
