# -*- coding: utf-8 -*-
"""
agregar_semillas.py — Agregador de la dispersión entre semillas (tarea T4).

Convierte las tablas del barrido (`metricas_*_semillas.csv`) en la tabla de
dispersión que cita el anexo `A.3` de la memoria: por cada combinación de
variante de características × algoritmo × alcance × métrica, el recuento `n`, la
media, la desviación típica MUESTRAL (ddof=1), el mínimo y el máximo, a 4
decimales.

POR QUÉ EXISTE: sin él la tabla de `A.3` saldría de cálculo manual sobre diez
filas por celda, y la regla del proyecto lo prohíbe. Emite además la misma tabla
ya formateada en Markdown (`dispersion_semillas.md`) para que T7 la pegue en el
anexo sin recalcular ni un número a mano.

Reglas de protocolo (invalidan el TFG si se rompen)
---------------------------------------------------
  * CERO `fit`. Este script solo lee CSV y calcula estadísticos descriptivos.
  * NO ABRE NINGUNA DE LAS NUEVE TABLAS PUBLICADAS. Lee exclusivamente sus
    homólogas `*_semillas.csv` (nombres derivados con
    `config.nombre_tabla_semillas()`), y las abre en modo lectura. Las cuatro
    principales y las cinco auxiliares de la semilla 42 no se tocan.
  * NO CONSUME `config.RANDOM_STATE`: las rutas se construyen a mano contra
    `config.RESULTADOS_DIR` en vez de con `config.ruta_tabla()`, que depende de la
    semilla global de la corrida. Este script no tiene semilla: agrega las de otros.
  * ABORTA si a alguna combinación le falta alguna de las semillas de
    `config.SEMILLAS_BARRIDO`. Una media de 7 puntos presentada como de 10 es peor
    que no tener tabla.
  * NO DECIDE NADA. No dice si dos intervalos se solapan ni calcula p-valores:
    emite `n`/media/sd/mín/máx y la lectura la escribe T11 en prosa (la renuncia
    al contraste estadístico —10 puntos sobre un único dataset— es una decisión ya
    tomada de la ficha T4, no una omisión de este script).

La semilla 42 NO entra en la agregación, y no porque se filtre aquí: es que no
está en `config.SEMILLAS_BARRIDO` ni escribe en estas tablas (ver el encabezado
de `config.py`). Es el TITULAR de 5.1-5.3, un punto independiente de la banda.

Procedencia: cada celda lleva DOS sellos y no uno —`commits_origen` (los commits de
las diez filas agregadas, que es el que vale para citar la banda) y `commit_agregador`
(el del agregador)—, y el script AVISA si una celda mezcla commits. También avisa, con el
reparto y sin abortar, si una celda no comparte la misma DECISIÓN en las diez
semillas (`balanceo`, `config_ganadora`): los folds pueden voltear el balanceo
ganador de 4.3.4, y una media sobre modelos con balanceos distintos hay que
declararla. Ese reparto va además en la COLUMNA `decisiones_no_constantes` de cada
celda del CSV, no solo en los avisos del `.md`: quien arme `A.3` desde la tabla ve
la mezcla en la misma fila que la media que la promedia.

Salidas
-------
  Resultados/dispersion_semillas.csv   una fila por (variante, algoritmo, alcance,
                                       métrica, bloque)
  Resultados/dispersion_semillas.md    la misma tabla formateada para `A.3`

Uso
---
  python app\\agregar_semillas.py
"""
import argparse
import os
from datetime import datetime

import numpy as np
import pandas as pd

import config
import evaluacion


class AgregadorSemillas:
    """
    Agrega las tablas del barrido de semillas en una tabla de dispersión.

    Una clase por script, como el resto del pipeline. No entrena, no dibuja y no
    escribe en ninguna tabla publicada: lee los `*_semillas.csv`, comprueba que
    cada combinación esté completa y emite CSV + Markdown.
    """

    # --- QUÉ MÉTRICAS SE AGREGAN (decisión de Francisco, 2026-08-12) -----------
    # Lista CERRADA por tabla. No se agrega "todo lo numérico" a propósito: en
    # estas tablas conviven columnas de D2 con columnas del train (`f1_macro_cv`,
    # `auc_val`), recuentos enteros (tn/fp/fn/tp, n_test) y texto; una media de
    # todas ellas produciría una tabla que invita a citar cifras de selección de
    # hiperparámetros como si fuesen resultados. Cada entrada declara además de
    # qué columna sale el nombre del algoritmo y qué filas se filtran.
    #
    # `umbral` (anomalías) y `umbral_conf_elegido` (híbrido) NO son métricas sobre
    # D2 y se agregan igualmente porque son justo lo que el barrido pone a prueba:
    # el p95 se recalcula en cada semilla (el split 80/20 de D1 cambia) y el
    # UMBRAL_CONF se recalibra por OOF. Su alcance propio ya viaja en las tablas
    # de origen (config.ALCANCE_SELECCION / la columna `alcance`).
    ESPECIFICACION = (
        {
            "tabla": "metricas_anomalias.csv",
            "columna_algoritmo": "algoritmo",
            "filtro": None,
            "metricas": ("roc_auc", "pr_auc", "f1", "fpr", "umbral"),
            "con_tiempos": True,
        },
        {
            "tabla": "metricas_firmas.csv",
            "columna_algoritmo": "algoritmo",
            "filtro": None,
            "metricas": ("f1_macro", "accuracy_D2", "recall_macro", "f1_u2r"),
            "con_tiempos": True,
        },
        {
            "tabla": "metricas_baseline.csv",
            "columna_algoritmo": "algoritmo",
            "filtro": None,
            "metricas": ("bin_accuracy", "bin_fpr", "f1_macro",
                         "recall_0day_global"),
            "con_tiempos": True,
        },
        {
            "tabla": "metricas_hibrido.csv",
            "columna_algoritmo": "algoritmo",
            "filtro": None,
            "metricas": ("bin_recall", "bin_fpr", "bin_accuracy",
                         "conocida_f1_macro", "recall_0day_global",
                         "fpr_cascada", "umbral_conf_elegido"),
            "con_tiempos": True,
        },
        {
            # AUXILIAR y con otra granularidad de fila: no tiene columna
            # 'algoritmo' (el modelo medido viaja en 'firma') y sus cinco filas por
            # (variante, semilla) son los cuatro buckets del argmax + '__global__'.
            # Se agrega SOLO la fila agregada, que es la que se cita.
            #
            # SE AGREGAN LAS DOS COLUMNAS, y 'n_condenadas' no es redundante aunque
            # sea 'tasa_condena' × 'n_normales_d2' con denominador constante (las
            # 9.711 normales de D2): PIPELINE.md y config.ALCANCE_CASCADA_INVERTIDA
            # declaran que LO CITABLE es 'n_condenadas', y con solo la tasa a 4
            # decimales T7/T11 tendrían que multiplicar por 9.711 a mano —cálculo
            # manual, prohibido en este proyecto— perdiendo ~1 flujo de resolución.
            # Es un entero: agregarlo es gratis y sin pérdida.
            "tabla": "metricas_cascada_invertida.csv",
            "columna_algoritmo": "firma",
            "filtro": ("categoria_asignada", "__global__"),
            "metricas": ("n_condenadas", "tasa_condena"),
            "con_tiempos": False,
        },
    )

    # --- LAS COLUMNAS DE TIEMPO VAN EN BLOQUE APARTE (decisión de Francisco) ---
    # No entran en la tabla de calidad. Motivo, y hay que escribirlo al lado de la
    # cifra: son wall-clock en una máquina no dedicada. El dato de T1 lo mide —el
    # Autoencoder de 54 fue de 37,71 s a 181,91 s entre dos corridas, 4,8×, con
    # calidad IDÉNTICA AL BIT y con el recuento de épocas determinista (162 en 54,
    # 128 en 122; cierre de T22)—, así que la sd de estas columnas mide carga de
    # máquina y no algoritmo. Se emiten porque documentan esa dispersión, no como
    # resultado.
    #
    # 'alcance_tiempo_s' queda FUERA de esta tupla aunque la decisión la enumere
    # entre las seis columnas de tiempo: es PROSA (el texto de
    # config.ALCANCE_TIEMPO_S_*), no un número, y no admite media ni sd. Se
    # comprueba en su lugar que sea CONSTANTE dentro de cada combinación: si dos
    # semillas de la misma celda declarasen alcances distintos, la celda estaría
    # mezclando dos magnitudes y el aviso lo deja a la vista.
    COLUMNAS_TIEMPO = ("tiempo_s", "tiempo_entrenamiento_s",
                       "tiempo_inferencia_s", "latencia_ms_por_flujo",
                       "flujos_por_segundo")

    RAZON_BLOQUE_MAQUINA = (
        "wall-clock en máquina no dedicada: su sd mide CARGA DE MÁQUINA y no el "
        "algoritmo. Medido en T1: el Autoencoder de 54 features pasó de 37,71 s a "
        "181,91 s entre dos corridas (4,8x) con calidad idéntica al bit y con el "
        "recuento de épocas determinista (162 en 54 y 128 en 122). No es una "
        "propiedad del algoritmo y no se cita como resultado."
    )

    # --- DECISIONES QUE PUEDEN VOLTEAR ENTRE SEMILLAS -------------------------
    # Columnas que NO son métricas: son la DECISIÓN que tomó cada corrida. Se
    # comprueba que sean constantes dentro de cada celda y, si no lo son, se avisa
    # CON EL REPARTO (sin abortar). Motivo: los folds del StratifiedKFold mueven el
    # balanceo ganador de 4.3.4 y el best_params_ del GridSearchCV, y el balanceo
    # por algoritmo es una decisión CERRADA tomada con n=1 (firmas.py:97-105).
    # Sin este aviso, A.3 publicaría la media de 'f1_macro' de RandomForest sobre
    # diez modelos entrenados con DOS esquemas de balanceo distintos sin decirlo.
    #
    # AVISO Y NO ABORTO, a propósito: que la decisión voltee en 3 de 10 semillas no
    # es un error del barrido — es un HALLAZGO para 5.4 (la fragilidad de una
    # decisión tomada con una sola corrida), y abortar lo escondería.
    COLUMNAS_CONSTANCIA = ("balanceo", "config_ganadora")

    BLOQUE_CALIDAD = "calidad"
    BLOQUE_MAQUINA = "dispersion_de_maquina"

    # Columna de procedencia de las filas de ORIGEN. No es la del agregador: ver
    # _commits_de_celda().
    COLUMNA_COMMIT = "commit"

    # Clave de agrupación. Es la CLAVE_UNICIDAD de las tablas de métricas (sin
    # `semilla`, que es justo el eje sobre el que se agrega): así cada celda de la
    # tabla de dispersión corresponde exactamente a una fila de la tabla publicada
    # de la semilla 42, y el titular se puede poner al lado de su banda.
    CLAVE_AGRUPACION = ("set_features", "algoritmo", "alcance")

    DECIMALES = 4

    NOMBRE_CSV = "dispersion_semillas.csv"
    NOMBRE_MD = "dispersion_semillas.md"

    def __init__(self, semillas=None):
        # Las diez semillas esperadas salen de config (lista cerrada, con sus
        # aserciones). El parámetro existe para poder auditar un barrido parcial a
        # mano, NO para publicar: el defecto es la lista completa.
        self.semillas = sorted(config.SEMILLAS_BARRIDO if semillas is None
                               else semillas)
        self.filas = []        # filas de la tabla de dispersión
        self.avisos = []       # avisos no fatales, se imprimen y van al .md
        self.commit = None     # commit del AGREGADOR (no el de las filas de origen)
        self.fecha = None
        # Todos los commits vistos en las filas agregadas, para la cabecera del .md.
        self.commits_vistos = set()

    # ------------------------------------------------------------------
    # 1. Lectura de una tabla del barrido
    # ------------------------------------------------------------------
    def _ruta_tabla_semillas(self, nombre_publicado):
        """
        Ruta de la tabla del BARRIDO correspondiente a una tabla publicada.

        No se usa config.ruta_tabla() a propósito: esa función decide por la
        semilla GLOBAL de la corrida y este script no tiene semilla. Aquí el
        desvío es incondicional, así que es imposible que una ejecución de este
        agregador acabe leyendo —y mucho menos escribiendo— una tabla publicada.
        """
        return os.path.join(config.RESULTADOS_DIR,
                            config.nombre_tabla_semillas(nombre_publicado))

    def _leer(self, spec):
        """Lee y filtra una tabla del barrido. Aborta si no existe o está incompleta."""
        ruta = self._ruta_tabla_semillas(spec["tabla"])
        if not os.path.exists(ruta):
            raise RuntimeError(
                "No existe {}. El barrido de las {} semillas no se ha corrido (o "
                "no ha llegado a esta tabla): lánzalo con "
                "'python app\\barrido_semillas.py' antes de agregar.".format(
                    ruta, len(self.semillas)))
        df = pd.read_csv(ruta)

        # Columna 'algoritmo' unificada: en las cuatro principales ya se llama así;
        # en la tabla de la cascada invertida el modelo medido viaja en 'firma'.
        col_algo = spec["columna_algoritmo"]
        if col_algo not in df.columns:
            raise RuntimeError(
                "{} no trae la columna '{}': no se puede identificar el "
                "algoritmo de cada fila.".format(ruta, col_algo))
        if col_algo != "algoritmo":
            df = df.copy()
            df["algoritmo"] = df[col_algo].astype(str)

        if spec["filtro"] is not None:
            columna, valor = spec["filtro"]
            if columna not in df.columns:
                raise RuntimeError(
                    "{} no trae la columna '{}' del filtro declarado.".format(
                        ruta, columna))
            df = df[df[columna].astype(str) == str(valor)]

        faltan = [c for c in self.CLAVE_AGRUPACION + ("semilla",)
                  if c not in df.columns]
        if faltan:
            raise RuntimeError(
                "{} no trae las columnas {}: es de otro esquema y no se puede "
                "agregar.".format(ruta, faltan))
        return df, ruta

    # ------------------------------------------------------------------
    # 2. Comprobación de completitud — el abort que exige la decisión D6
    # ------------------------------------------------------------------
    def _comprobar_completitud(self, df, ruta):
        """
        Cada combinación (variante, algoritmo, alcance) debe traer EXACTAMENTE una
        fila por cada semilla esperada. Aborta si falta alguna, si sobra una
        semilla ajena a la lista o si alguna aparece repetida.

        Es el requisito central del agregador: publicar una media de 7 semillas
        rotulada como de 10 sería una cifra falsa dentro del anexo A.3, y nadie la
        detectaría releyendo la tabla.
        """
        esperadas = set(self.semillas)
        problemas = []
        for clave, grupo in df.groupby(list(self.CLAVE_AGRUPACION), dropna=False):
            presentes = [int(s) for s in grupo["semilla"].tolist()]
            conjunto = set(presentes)
            if len(presentes) != len(conjunto):
                repetidas = sorted(s for s in conjunto
                                   if presentes.count(s) > 1)
                problemas.append("{} → semillas REPETIDAS {}".format(
                    clave, repetidas))
                continue
            if conjunto != esperadas:
                problemas.append("{} → faltan {} · sobran {}".format(
                    clave, sorted(esperadas - conjunto),
                    sorted(conjunto - esperadas)))
        if problemas:
            raise RuntimeError(
                "{}: el barrido está INCOMPLETO y no se agrega. Se esperaban las "
                "semillas {} en cada combinación {}. Problemas:\n     - {}\n"
                "   Relanza 'python app\\barrido_semillas.py' (es reanudable: "
                "salta lo que ya está) y vuelve a agregar.".format(
                    os.path.basename(ruta), self.semillas,
                    list(self.CLAVE_AGRUPACION), "\n     - ".join(problemas))
            )

    # ------------------------------------------------------------------
    # 3. Estadísticos de una celda
    # ------------------------------------------------------------------
    def _estadisticos(self, valores):
        """
        n, media, sd MUESTRAL (ddof=1), mín y máx de una serie, a 4 decimales.

        ddof=1 y no ddof=0: las diez semillas son una MUESTRA de las infinitas
        inicializaciones posibles, no la población entera. numpy usa ddof=0 por
        defecto (que subestima), así que se pasa explícito. Con n=10 la diferencia
        es un factor sqrt(10/9) = 1,054 sobre la sd — pequeño, pero es la
        definición correcta y la que se declara en A.3.
        """
        serie = pd.to_numeric(pd.Series(valores), errors="coerce").dropna()
        n = int(len(serie))
        if n == 0:
            return None
        arr = serie.to_numpy(dtype=float)
        # Con n=1 la sd muestral no está definida (división por n-1 = 0): celda
        # vacía en lugar de un 0,0 que se leería como "dispersión nula medida".
        sd = float(np.std(arr, ddof=1)) if n > 1 else float("nan")
        return {
            "n": n,
            "media": round(float(arr.mean()), self.DECIMALES),
            "sd": (round(sd, self.DECIMALES) if sd == sd else float("nan")),
            "min": round(float(arr.min()), self.DECIMALES),
            "max": round(float(arr.max()), self.DECIMALES),
        }

    def _agregar_metrica(self, spec, grupo, clave, metrica, bloque,
                         commits_origen="", decisiones_no_constantes=""):
        """Añade una fila de dispersión para una métrica de una combinación."""
        if metrica not in grupo.columns:
            if bloque == self.BLOQUE_CALIDAD:
                raise RuntimeError(
                    "{}: la columna '{}' no existe y es una de las métricas de "
                    "calidad declaradas para esta tabla.".format(
                        spec["tabla"], metrica))
            self.avisos.append("{}: sin columna '{}' (bloque de máquina); se "
                               "omite.".format(spec["tabla"], metrica))
            return

        est = self._estadisticos(grupo[metrica])
        if est is None or est["n"] != len(self.semillas):
            observados = 0 if est is None else est["n"]
            mensaje = ("{} · {} · métrica '{}': {} valores numéricos de {} "
                       "semillas (celdas vacías o no numéricas)".format(
                           spec["tabla"], clave, metrica, observados,
                           len(self.semillas)))
            if bloque == self.BLOQUE_CALIDAD:
                # Mismo criterio que la completitud de filas: una media de menos
                # puntos de los que declara no se publica.
                raise RuntimeError(
                    mensaje + ". No se publica una media incompleta como si "
                    "fuese de {} semillas.".format(len(self.semillas)))
            self.avisos.append(mensaje + "; se emite con la n real.")
            if est is None:
                return

        set_features, algoritmo, alcance = clave
        self.filas.append({
            "tabla_origen": config.nombre_tabla_semillas(spec["tabla"]),
            "bloque": bloque,
            "set_features": set_features,
            "algoritmo": algoritmo,
            "metrica": metrica,
            "n": est["n"],
            "media": est["media"],
            "sd": est["sd"],
            "min": est["min"],
            "max": est["max"],
            "semillas": " ".join(str(s) for s in self.semillas),
            # El alcance de la fila de origen viaja con la cifra agregada: sin él,
            # un 'f1_macro' de firmas y uno de baseline se leerían como la misma
            # medida (es exactamente el defecto que cerró T1).
            "alcance": alcance,
            "nota_bloque": ("" if bloque == self.BLOQUE_CALIDAD
                            else self.RAZON_BLOQUE_MAQUINA),
            # DOS columnas de procedencia y no una, porque son dos cosas distintas
            # y confundirlas es publicar una banda sellada con un commit que no
            # produjo ninguno de sus puntos (regla de procedencia de
            # evaluacion.py:100-105):
            #   'commits_origen' = los commits de las 10 filas que se agregan. Es
            #                      el que vale para citar la banda. Con un barrido
            #                      reanudable a lo largo de días una celda puede
            #                      mezclar commits —basta que cambie el sufijo
            #                      '-sucio'—, y entonces esta celda lo dice.
            #   'commit_agregador' = el del AGREGADOR, es decir con qué versión de
            #                      ESTE script se calcularon media/sd. No dice nada
            #                      sobre con qué código se produjeron los puntos.
            #
            # SE LLAMA 'commit_agregador' Y NO 'commit' (renombrado el 2026-08-12):
            # en las nueve 'metricas_*.csv' la columna 'commit' significa «el código
            # que produjo esta fila», y aquí significaría «el del agregador, que no
            # produjo ninguno de los diez puntos». Es el homónimo con dos
            # significados que prohíbe la regla de config.py:326-332, y esta tabla no
            # pasa por guardar_metricas()/validar_esquema_minimo(), así que no hay
            # red que lo detecte. El nombre distinto ES la red.
            # EL REPARTO DE UNA DECISIÓN NO CONSTANTE ES COLUMNA, no solo aviso
            # (decisión del 2026-08-12): antes «SMOTE en 7 · class_weight en 3» solo
            # iba a stdout y a la sección «Avisos» del .md, así que quien armase A.3
            # desde el CSV —que es lo natural: es la tabla— vería la media sin
            # enterarse de que promedia modelos con dos balanceos distintos. Justo en
            # la celda cuya media los mezcla. Vacío = la decisión fue la misma en las
            # diez semillas.
            "decisiones_no_constantes": decisiones_no_constantes,
            "commits_origen": commits_origen,
            "commit_agregador": self.commit,
            "fecha": self.fecha,
        })

    # ------------------------------------------------------------------
    # 4. Agregación de una tabla
    # ------------------------------------------------------------------
    def _agregar_tabla(self, spec):
        df, ruta = self._leer(spec)
        self._comprobar_completitud(df, ruta)
        n_celdas = 0
        for clave, grupo in df.groupby(list(self.CLAVE_AGRUPACION), dropna=False):
            self._comprobar_alcance_tiempo_constante(spec, grupo, clave)
            decisiones = self._comprobar_decisiones_constantes(spec, grupo, clave)
            commits = self._commits_de_celda(spec, grupo, clave)
            for metrica in spec["metricas"]:
                self._agregar_metrica(spec, grupo, clave, metrica,
                                      self.BLOQUE_CALIDAD, commits, decisiones)
            if spec["con_tiempos"]:
                for metrica in self.COLUMNAS_TIEMPO:
                    self._agregar_metrica(spec, grupo, clave, metrica,
                                          self.BLOQUE_MAQUINA, commits, decisiones)
            n_celdas += 1
        print("   {}: {} combinaciones × {} semillas".format(
            os.path.basename(ruta), n_celdas, len(self.semillas)))

    def _comprobar_alcance_tiempo_constante(self, spec, grupo, clave):
        """
        'alcance_tiempo_s' es texto: no se agrega, se verifica que sea el MISMO en
        las diez filas de la celda. Si dos semillas declarasen alcances distintos,
        el bloque de máquina de esa celda estaría promediando dos magnitudes
        diferentes (es el defecto que T1 cerró en el dato) y el aviso lo saca a la
        luz sin abortar: la tabla de calidad no depende de esta columna.
        """
        if not spec["con_tiempos"] or "alcance_tiempo_s" not in grupo.columns:
            return
        distintos = grupo["alcance_tiempo_s"].astype(str).nunique()
        if distintos > 1:
            self.avisos.append(
                "{} · {}: la columna 'alcance_tiempo_s' toma {} valores distintos "
                "entre semillas; las columnas de tiempo de esa celda no miden lo "
                "mismo.".format(spec["tabla"], clave, distintos))

    def _comprobar_decisiones_constantes(self, spec, grupo, clave):
        """
        Comprueba que las columnas de DECISIÓN (COLUMNAS_CONSTANCIA) sean las mismas
        en las diez semillas de la celda, y AVISA con el reparto si no lo son.

        Mismo patrón que _comprobar_alcance_tiempo_constante() y por el mismo
        motivo —una celda que promedia dos cosas distintas sin decirlo—, pero aquí
        lo que puede voltear no es un texto de alcance: es el balanceo ganador de
        4.3.4 o el best_params_ del GridSearchCV, las dos decisiones que dependen de
        los folds. No aborta (ver el comentario de COLUMNAS_CONSTANCIA): el reparto
        es material de 5.4, no un fallo del barrido.

        Devuelve el reparto ya formateado para la columna
        'decisiones_no_constantes' del CSV ('' si todas fueron constantes), para que
        el aviso no viva solo en el .md: ver el comentario de esa columna en
        _agregar_metrica().
        """
        repartos = []
        for columna in self.COLUMNAS_CONSTANCIA:
            if columna not in grupo.columns:
                continue
            valores = grupo[columna].astype(str)
            reparto = valores.value_counts()
            if len(reparto) <= 1:
                continue
            detalle = " · ".join(
                "{} en {} semilla(s)".format(valor, int(veces))
                for valor, veces in reparto.items())
            # Sin comas: este texto viaja como VALOR dentro del CSV (misma regla que
            # los textos de alcance de config.py).
            repartos.append("{}: {}".format(columna, detalle))
            self.avisos.append(
                "{} · {}: la columna de DECISIÓN '{}' NO es constante entre las {} "
                "semillas ({}). La media de esta celda promedia modelos con "
                "decisiones distintas: hay que declararlo al citarla (material de "
                "5.4, no un error).".format(
                    spec["tabla"], clave, columna, len(self.semillas), detalle))
        return " | ".join(repartos)

    def _commits_de_celda(self, spec, grupo, clave):
        """
        Conjunto DISTINTO de commits de las filas que se agregan en esta celda, ya
        formateado para la columna 'commits_origen'. Avisa si hay más de uno.

        POR QUÉ NO BASTA EL COMMIT DEL AGREGADOR (que es lo que hacía la versión
        anterior de este script): el barrido es reanudable y puede correrse a lo
        largo de días, así que una celda puede mezclar commits —basta que cambie el
        sufijo '-sucio'—. Sellar la banda con el commit del agregador publicaría en
        A.3 diez puntos rotulados con un commit que no produjo ninguno de ellos, y
        el lector no tendría forma de detectarlo. La regla de procedencia del
        proyecto (evaluacion.py:100-105) pide lo contrario: que el dato viaje con el
        código que lo produjo.
        """
        if self.COLUMNA_COMMIT not in grupo.columns:
            self.avisos.append(
                "{} · {}: sin columna '{}'; la celda queda SIN procedencia de "
                "origen.".format(spec["tabla"], clave, self.COLUMNA_COMMIT))
            return ""
        commits = sorted(set(grupo[self.COLUMNA_COMMIT].astype(str)))
        self.commits_vistos.update(commits)
        if len(commits) > 1:
            self.avisos.append(
                "{} · {}: las {} semillas de esta celda se produjeron con {} "
                "commits distintos ({}). La banda NO sale de una sola versión del "
                "código y hay que decirlo al citarla.".format(
                    spec["tabla"], clave, len(self.semillas), len(commits),
                    ", ".join(commits)))
        return " ".join(commits)

    # ------------------------------------------------------------------
    # 5. Salidas
    # ------------------------------------------------------------------
    def _escribir_csv(self):
        ruta = os.path.join(config.RESULTADOS_DIR, self.NOMBRE_CSV)
        df = pd.DataFrame(self.filas)
        # Orden estable y legible: primero la calidad, después la máquina, y
        # dentro por tabla de origen / variante / algoritmo / métrica. Sin esto el
        # orden lo decidiría el groupby y el fichero diffearía sin motivo.
        df["_orden_bloque"] = (df["bloque"] == self.BLOQUE_MAQUINA).astype(int)
        df = df.sort_values(
            ["_orden_bloque", "tabla_origen", "set_features", "algoritmo",
             "metrica"]
        ).drop(columns=["_orden_bloque"])
        df.to_csv(ruta, index=False)
        print("   Tabla de dispersión (CSV): {}".format(ruta))
        return ruta

    def _tabla_md(self, df_bloque):
        """Una tabla Markdown por bloque, ya formateada a 4 decimales."""
        lineas = ["| Variante | Algoritmo | Métrica | n | Media | sd | Mín | Máx |",
                  "|---|---|---|---:|---:|---:|---:|---:|"]
        for _, f in df_bloque.iterrows():
            def fmt(valor):
                return ("—" if valor != valor
                        else "{:.4f}".format(float(valor)))
            lineas.append("| {} | {} | `{}` | {} | {} | {} | {} | {} |".format(
                f["set_features"], f["algoritmo"], f["metrica"], int(f["n"]),
                fmt(f["media"]), fmt(f["sd"]), fmt(f["min"]), fmt(f["max"])))
        return "\n".join(lineas)

    def _escribir_md(self):
        ruta = os.path.join(config.RESULTADOS_DIR, self.NOMBRE_MD)
        df = pd.DataFrame(self.filas)
        partes = [
            "# Dispersión entre semillas (tarea T4)",
            "",
            "> Generado por `Implementacion/app/agregar_semillas.py`. **No se "
            "edita a mano**: se regenera corriendo el agregador.",
            # DOS sellos y no uno: el del agregador NO es el de las filas. Ver el
            # comentario de 'commits_origen' en _agregar_metrica().
            "> Commit del **agregador** (columna `commit_agregador` del CSV: con qué "
            "versión de `agregar_semillas.py` se calcularon media y sd): `{}` · "
            "Fecha: {}".format(self.commit, self.fecha),
            "> Commit(s) de las **filas agregadas** (con qué versión del código se "
            "produjeron los puntos de las bandas): {}. La columna "
            "`commits_origen` del CSV lo da por celda; si aquí hay más de uno, el "
            "bloque de avisos dice en qué celdas.".format(
                ", ".join("`{}`".format(c)
                          for c in sorted(self.commits_vistos))
                or "_ninguno: las tablas de origen no traen columna `commit`_"),
            "> Semillas agregadas ({}): {}.".format(
                len(self.semillas),
                ", ".join(str(s) for s in self.semillas)),
            "",
            "La **semilla 42 no está aquí**, y es deliberado: es el titular de "
            "5.1-5.3 y un punto **independiente** de esta banda, no uno de sus "
            "sumandos (razón completa en el encabezado de `config.py`). Al citar, "
            "el titular va al lado de la banda, nunca dentro de ella.",
            "",
            "Lo que **sí varía** entre estas corridas y lo que **no** está "
            "declarado en `Implementacion/PIPELINE.md`, subsección «El andamiaje "
            "de la semilla»: varían el split 80/20 de D1 (y con él el umbral "
            "p95), la muestra de 5.000 de D3, la submuestra de 20.000 de "
            "OneClassSVM, los folds del CV y la inicialización de los modelos; "
            "**no** varían los splits D1/D2/D3 ni la selección de las 54 "
            "características, porque `program.py` no está parametrizado por "
            "semilla.",
            "",
            "`sd` es la desviación típica **muestral** (`ddof=1`). **Sin "
            "p-valor**: 10 puntos sobre un único dataset no sostienen un "
            "contraste, y la renuncia se declara (ficha T4).",
            "",
            "Las tablas de abajo son la vista legible. El CSV "
            "(`dispersion_semillas.csv`) trae por celda tres columnas que aquí no "
            "caben y que hay que mirar antes de citar una banda: `commits_origen`, "
            "`commit_agregador` y `decisiones_no_constantes` (el reparto del "
            "`balanceo`/`config_ganadora` cuando no fue el mismo en las diez "
            "semillas; vacío = lo fue).",
            "",
            "## Calidad",
            "",
        ]
        calidad = df[df["bloque"] == self.BLOQUE_CALIDAD].sort_values(
            ["tabla_origen", "set_features", "algoritmo", "metrica"])
        partes.append(self._tabla_md(calidad))

        maquina = df[df["bloque"] == self.BLOQUE_MAQUINA].sort_values(
            ["tabla_origen", "set_features", "algoritmo", "metrica"])
        if len(maquina) > 0:
            partes += [
                "",
                "## Dispersión de máquina (NO es calidad y NO se cita como "
                "resultado)",
                "",
                "Bloque aparte a propósito: {}".format(
                    self.RAZON_BLOQUE_MAQUINA),
                "",
                self._tabla_md(maquina),
            ]

        if self.avisos:
            partes += ["", "## Avisos de la agregación", ""]
            partes += ["- {}".format(a) for a in self.avisos]

        partes.append("")
        with open(ruta, "w", encoding="utf-8") as f:
            f.write("\n".join(partes))
        print("   Tabla de dispersión (Markdown para A.3): {}".format(ruta))
        return ruta

    # ------------------------------------------------------------------
    # Orquestación
    # ------------------------------------------------------------------
    def ejecutar(self):
        config.setup_utf8()
        config.ensure_dirs()
        self.commit = config.commit_actual()
        self.fecha = datetime.now().isoformat(timespec="seconds")

        print("=" * 70)
        print("AGREGACIÓN DE LA DISPERSIÓN ENTRE SEMILLAS (T4)")
        print("=" * 70)
        print("   Semillas esperadas ({}): {}".format(
            len(self.semillas), self.semillas))
        print("   La semilla {} NO entra (es el titular publicado, punto "
              "independiente de la banda)".format(config.SEMILLA_POR_DEFECTO))
        print("   Tablas leídas: SOLO las '*{}.csv' — ninguna de las nueve "
              "publicadas se abre".format(config.SUFIJO_TABLA_SEMILLAS))
        print("-" * 70)

        for spec in self.ESPECIFICACION:
            self._agregar_tabla(spec)

        if not self.filas:
            raise RuntimeError(
                "No se agregó ninguna celda: revisa las tablas del barrido.")

        print("-" * 70)
        self._escribir_csv()
        self._escribir_md()
        for aviso in self.avisos:
            print("   [aviso] {}".format(aviso))
        print("=" * 70)
        print("AGREGACIÓN COMPLETADA: {} filas ({} de calidad · {} de "
              "máquina)".format(
                  len(self.filas),
                  sum(1 for f in self.filas
                      if f["bloque"] == self.BLOQUE_CALIDAD),
                  sum(1 for f in self.filas
                      if f["bloque"] == self.BLOQUE_MAQUINA)))
        print("=" * 70)
        return self.filas


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Agrega las tablas del barrido de semillas "
                    "('metricas_*_semillas.csv') en la tabla de dispersión de "
                    "A.3: n, media, sd muestral, mín y máx. No entrena nada y no "
                    "abre ninguna de las nueve tablas publicadas."
    )
    parser.add_argument(
        "--semillas", type=int, nargs="+", default=None,
        help="Semillas que se esperan en cada combinación (por defecto las {} de "
             "config.SEMILLAS_BARRIDO: {}). Solo para auditar un barrido parcial "
             "a mano: lo que se publica en A.3 se agrega con la lista "
             "completa.".format(len(config.SEMILLAS_BARRIDO),
                                config.SEMILLAS_BARRIDO),
    )
    args = parser.parse_args()

    # Referencia explícita para que quede claro que este script NO redefine el
    # esquema: la clave de agrupación es la CLAVE_UNICIDAD de evaluacion.py sin
    # `semilla`, que es el eje sobre el que se agrega.
    assert AgregadorSemillas.CLAVE_AGRUPACION == evaluacion.CLAVE_UNICIDAD, (
        "La clave de agrupación debe seguir siendo evaluacion.CLAVE_UNICIDAD")

    AgregadorSemillas(semillas=args.semillas).ejecutar()
