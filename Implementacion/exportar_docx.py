# -*- coding: utf-8 -*-
"""Volcado de las notas de la memoria (Obsidian) a un unico .docx con la
plantilla de estilos de Francisco.

ADVERTENCIA (restriccion dura, 2026-08-22): el volcado es destructivo respecto
al trabajo manual en Word; re-ejecutar revive lo borrado. El volcado es
UNIDIRECCIONAL y no hay volcado inverso: las notas del vault son la fuente y el
.docx es la salida. Si Francisco borra material en su documento de trabajo, este
script NO lo sabe, y una nueva corrida lo REVIVE en silencio, sin fallar y sin
conflicto visible. Por eso:
  * el script NUNCA escribe sobre el documento de trabajo de Francisco NI
    sobre las notas del vault (que son la FUENTE): TODO lo que escribe -el
    .docx, el Markdown intermedio y los dos .txt- vive bajo `Resultados/docx/`,
    y una sola puerta (validar_ruta_escritura) lo valida y aborta si no; la
    ruta se resuelve por realpath, asi que una junction dentro de esa carpeta
    tampoco cuela,
  * el nombre de salida va versionado con fecha-hora y commit, y si el destino
    ya existe se ABORTA salvo `--sobrescribir` explicito,
  * el destino no puede llamarse `Proyecto_Fin_de_Grado-FJLM-2026.doc(x)`
    ni coincidir con la plantilla ni con `TFG - Fran.docx`.
Cada corrida deja junto al .docx TRES ficheros de texto: un
`*_procedencia.txt` -con el LISTADO INTEGRO de los callouts borrados y
degradados, no solo su recuento-, un `*_estilos_plantilla.txt` con el censo de
estilos de la PLANTILLA y su numPr/numId, y un `*_estilos_docx.txt` con el censo
de pStyle del DOCUMENTO GENERADO (tablas, encabezados, colgantes). Son dos
censos distintos y no se confunden: uno describe la plantilla y el otro el
artefacto. Con ellos el diagnostico es comprobable sin abrir ningun ZIP. El
cuarto fichero es el Markdown unico intermedio.

POLITICA DE CALLOUTS (Francisco, 2026-08-22): degradar a prosa es el
COMPORTAMIENTO POR DEFECTO -el callout pierde la caja y conserva el texto- y se
BORRA unicamente el andamiaje declarado en ANDAMIAJE / ANDAMIAJE_TIPOS.
Lo que Francisco quiera conservar de una corrida nueva lo TRASLADA el a mano
comparando su documento con el .docx generado.

Pipeline: indice -> orden y jerarquia -> transformacion del Markdown de cada
nota -> Markdown unico intermedio -> pandoc --reference-doc -> post-proceso del
.docx (estilo de tabla y remapeo de los estilos que inyecta pandoc) -> recuento
estimado de paginas por capitulo + parte de callouts y de citas.

Python 3.11. Unica dependencia externa: el ejecutable de pandoc.
"""

import argparse
import datetime
import os
import re
import shutil
import subprocess
import sys
import zipfile

# --------------------------------------------------------------------------
# Rutas y constantes de configuracion
# --------------------------------------------------------------------------

RAIZ = r"C:\Users\francisco.lopez\KIKO_TFG\Working_Directory"
VAULT = os.path.join(RAIZ, "Obsidian_TFG_Vault")
ASSETS = os.path.join(VAULT, "assets")
PLANTILLA = os.path.join(RAIZ, "Plantilla-para-volcado.docx")
SALIDA_DIR = os.path.join(RAIZ, "Resultados", "docx")
PANDOC = r"C:\Users\francisco.lopez\AppData\Local\pandoc-portable\pandoc-3.6.3\pandoc.exe"

# Procedencia: se sella con el mismo mecanismo que el resto del proyecto
# (config.commit_actual()), sin duplicarlo por copia.
sys.path.insert(0, os.path.join(RAIZ, "Implementacion", "app"))
try:
    import config as _config
except Exception:                                    # pragma: no cover
    _config = None

# Carpetas del vault que NO son memoria
EXCLUIDAS = ("99 Investigaci", ".obsidian", "assets")
# Grupos del indice que no entran en el volcado
GRUPOS_FUERA = ("Bibliograf", "Totales")

# Ficheros que JAMAS pueden ser destino del volcado (documento de trabajo de
# Francisco, memoria historica y la propia plantilla).
DESTINOS_PROHIBIDOS = ("proyecto_fin_de_grado", "tfg - fran",
                       "plantilla-para-volcado")

# Niveles de encabezado que la plantilla numera automaticamente. NO es un
# comentario de confianza: comprobar_numeracion_plantilla() abre el ZIP de la
# plantilla, lista los estilos de encabezado con numPr y falla si no cuadra con
# esta constante. En el nivel 4 el numero escrito a mano SE CONSERVA porque el
# estilo no numera.
NIVELES_AUTONUMERADOS = (1, 2, 3, 5, 6, 7, 8, 9)

# Estimacion de paginas: A4, Normal 12 pt, interlineado 1,5, margenes 3 cm
# laterales y 2,5 cm superior/inferior, justificado -> ~425 palabras por pagina.
PALABRAS_POR_PAGINA = 425

# Nombres de estilo de la plantilla que el volcado necesita. Se resuelven por
# w:name contra la plantilla (nunca como literal en ingles): el .docx de
# Francisco los tiene en espanol, y 'caption' en minuscula.
ESTILO_PIE_FIGURA = ("Figura_Tabla_Ecuaci\u00f3n", "caption", "Caption")
ESTILO_TABLA = ("Table Grid", "Tabla con cuadr\u00edcula")
ESTILO_APENDICE_TITULO = ("Ap\u00e9ndice",)
ESTILO_APENDICE_N2 = ("T\u00edtulo 2 de Ap\u00e9ndice",)
ESTILO_APENDICE_N3 = ("T\u00edtulo 3 de Ap\u00e9ndice",)
ESTILO_LISTA = ("List Paragraph", "P\u00e1rrafo de lista")

# Estilos que pandoc INYECTA por su cuenta y que la plantilla no define. Sin
# remapear quedarian como pStyle colgante (Word cae al estilo por defecto).
# Compact = elementos de lista -> 'List Paragraph'; los otros dos son prosa
# corriente -> se les quita el pStyle y caen en Normal.
ESTILO_CODIGO = ("Código fuente", "Source Code")
REMAPEO_PSTYLE = {"Compact": ESTILO_LISTA, "FirstParagraph": None,
                  "BodyText": None, "Author": None, "Date": None,
                  "BlockText": None, "SourceCode": ESTILO_CODIGO}

# POLITICA DE CALLOUTS (decision de Francisco, 2026-08-22). La logica esta
# INVERTIDA respecto a las tres primeras pasadas del script: ya no hay lista de
# excepciones que se salvan del borrado.
#
#   * DEGRADAR A PROSA es el COMPORTAMIENTO POR DEFECTO: el callout pierde la
#     caja y conserva el texto. No hay que enumerarlo en ninguna parte.
#   * Se BORRA unicamente el ANDAMIAJE del vault, y la lista de abajo es la
#     UNICA lista enumerada que queda en el script.
#
# La antigua constante CALLOUTS_DEGRADAR (lista de excepciones que se salvaban)
# se ha ELIMINADO: con el defecto invertido seria codigo muerto y una segunda
# fuente de verdad sobre la misma decision. Consecuencia asumida y aceptada por
# Francisco: vuelve al documento el contenido de los callouts que las pasadas
# anteriores borraban; la poda la hace el a mano en Word.
#
# Andamiaje por TITULO (fragmento, comparado sin tildes):
ANDAMIAJE = ("Verificacion pendiente", "Trazabilidad")
# Andamiaje por TIPO de callout: un [!todo] es una tarea abierta del vault, no
# contenido de la memoria, sea cual sea su titulo.
ANDAMIAJE_TIPOS = ("todo",)

# Marcador de cita bibliografica: [12] o [8, p. 45] / [39, pp. 17-25] / [5, cap. 1]
RE_CITA = re.compile(r"\[(\d+)(?:\s*,\s*(?:pp?\.|cap\.)[^\]]*)?\]")


def _sin_tildes(texto):
    """Normaliza el texto para comparar titulos sin depender de tildes."""
    tabla = {
        "\u00e1": "a", "\u00e9": "e", "\u00ed": "i", "\u00f3": "o", "\u00fa": "u",
        "\u00c1": "A", "\u00c9": "E", "\u00cd": "I", "\u00d3": "O", "\u00da": "U",
        "\u00f1": "n", "\u00d1": "N", "\u00fc": "u", "\u00ab": '"', "\u00bb": '"',
        "\u2014": "-", "\u2013": "-", "\u2019": "'", "\u201c": '"', "\u201d": '"',
    }
    return "".join(tabla.get(c, c) for c in texto)


def citas_en(texto):
    """Lista de numeros de cita [n] presentes en el texto."""
    return RE_CITA.findall(texto)


class ExportadorDocx:
    """Vuelca las notas de la memoria a un unico .docx aplicando la plantilla."""

    def __init__(self, capitulos=None, salida=None, pandoc=None, plantilla=None,
                 sobrescribir=False, conservar_numeros_apendice=True):
        self.capitulos = capitulos          # None = memoria completa
        self.pandoc = pandoc or PANDOC
        self.plantilla = plantilla or PLANTILLA
        self.sobrescribir = sobrescribir
        self.conservar_numeros_apendice = conservar_numeros_apendice
        self.commit = self._commit()
        self.estilos = {}              # w:name -> (styleId, tiene_numPr)
        self.estilos_crudos = {}       # styleId -> dict con numPr/numId/basedOn
        self.ruta_censo_docx = None    # censo de pStyle del .docx GENERADO
        self.callouts = []             # parte integro: todos los callouts vistos
        self.callouts_borrados = 0
        self.callouts_degradados = 0
        self.citas_md = []             # [n] presentes en el Markdown intermedio
        self.avisos = []               # se inicializa ANTES de _censo_notas()
        self.ruta_censo_estilos = None  # censo de estilos junto al artefacto
        self.paginas = []              # [(capitulo, palabras_prosa, palabras_bruto)]
        self.salida = salida or self._nombre_versionado()
        self.indice = self._localizar_indice()
        self.notas_disco = self._censo_notas()

    # ------------------------------------------------------- procedencia
    @staticmethod
    def _commit():
        """Hash del commit via config.commit_actual(), sin duplicar mecanismo."""
        if _config is None:
            return "commit_desconocido"
        try:
            return _config.commit_actual()
        except Exception:
            return "commit_desconocido"

    def _nombre_versionado(self):
        """Nombre de salida versionado: nunca pisa una corrida anterior."""
        sello = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        alcance = "completa" if not self.capitulos else \
            "cap" + "-".join(_sin_tildes(c).replace(" ", "") for c in self.capitulos)
        return os.path.join(SALIDA_DIR, "memoria_%s_%s_%s.docx"
                            % (alcance, sello, self.commit))

    def validar_ruta_escritura(self, ruta, extensiones, que):
        """Puerta unica de escritura: carpeta, enlaces, extension y existencia.

        La aplican TODOS los ficheros que el volcado escribe, no solo el .docx:
        el Markdown intermedio de --md-intermedio tambien, o una ruta dentro de
        `Obsidian_TFG_Vault/` sobrescribiria una NOTA del vault, que es la fuente
        del volcado y queda intacta por restriccion dura.

        Se resuelve por realpath, no abspath: una junction o un symlink dentro
        de Resultados/docx/ que apuntara al documento de trabajo pasaria el
        filtro de carpeta con abspath.
        """
        destino = os.path.realpath(os.path.abspath(ruta))
        carpeta = os.path.normcase(os.path.dirname(destino))
        raiz_ok = os.path.normcase(os.path.realpath(os.path.abspath(SALIDA_DIR)))
        if not (carpeta == raiz_ok or carpeta.startswith(raiz_ok + os.sep)):
            raise SystemExit(
                "%s fuera de Resultados/docx/: %s\n(ruta real tras resolver "
                "enlaces: %s)\nEl volcado NUNCA escribe fuera de "
                "Resultados/docx/: ni sobre el documento de trabajo de "
                "Francisco ni sobre las notas del vault, que son la FUENTE "
                "(el volcado es destructivo respecto al trabajo manual en "
                "Word; re-ejecutar revive lo borrado)."
                % (que, ruta, destino))
        base = _sin_tildes(os.path.basename(destino)).lower()
        for prohibido in DESTINOS_PROHIBIDOS:
            if prohibido in base:
                raise SystemExit(
                    "%s prohibido (%s): es un documento que Francisco edita a "
                    "mano. Elige otro nombre bajo Resultados/docx/."
                    % (que, os.path.basename(destino)))
        if not base.endswith(tuple(extensiones)):
            raise SystemExit(
                "%s con extension inesperada (%s): se esperaba %s."
                % (que, os.path.basename(destino), " o ".join(extensiones)))
        if os.path.exists(destino) and not self.sobrescribir:
            raise SystemExit(
                "el %s ya existe y no se pisa sin permiso explicito:\n  %s\n"
                "Usa --sobrescribir si de verdad quieres reemplazar esa corrida."
                % (que, destino))
        return destino

    def validar_destino(self, md_intermedio=None):
        """El .docx y el Markdown intermedio viven bajo Resultados/docx/."""
        self.validar_ruta_escritura(self.salida, (".docx",), "destino")
        if md_intermedio:
            self.validar_ruta_escritura(md_intermedio, (".md", ".markdown"),
                                        "markdown intermedio")

    # ---------------------------------------------------------------- disco
    def _localizar_indice(self):
        """Localiza la nota de indice sin depender de tildes en el nombre."""
        for nombre in sorted(os.listdir(VAULT)):
            if nombre.startswith("00 ") and nombre.endswith(".md"):
                return os.path.join(VAULT, nombre)
        raise SystemExit("No se encuentra la nota de indice en el vault.")

    def _censo_notas(self):
        """Mapa basename (sin .md) -> ruta absoluta, solo notas de memoria."""
        censo = {}
        for base, dirs, ficheros in os.walk(VAULT):
            dirs[:] = [d for d in dirs if not d.startswith(EXCLUIDAS)]
            if any(x in base for x in EXCLUIDAS):
                continue
            for fichero in ficheros:
                if not fichero.endswith(".md"):
                    continue
                clave = fichero[:-3]
                ruta = os.path.join(base, fichero)
                if clave in censo:
                    # el indice enlaza por basename: con dos notas homonimas en
                    # carpetas distintas, el wikilink es AMBIGUO y el volcado
                    # elegiria una en silencio. Se avisa en vez de callar.
                    self.avisos.append(
                        "AMBIGUEDAD: dos notas con el mismo nombre '%s'; el "
                        "volcado usa '%s' e IGNORA '%s'. Renombra una o el "
                        "wikilink del indice no tiene destino unico."
                        % (clave, censo[clave], ruta))
                    continue
                censo[clave] = ruta
        return censo

    # ------------------------------------------------- estilos y plantilla
    def cargar_estilos_plantilla(self):
        """Lee styles.xml de la plantilla: w:name -> (styleId, tiene_numPr)."""
        if not os.path.isfile(self.plantilla):
            raise SystemExit("No se encuentra la plantilla en: " + self.plantilla)
        with zipfile.ZipFile(self.plantilla) as z:
            xml = z.read("word/styles.xml").decode("utf-8", "replace")
        patron = r'<w:style [^>]*w:styleId="([^"]+)"[^>]*>(.*?)</w:style>'
        crudos = {}      # styleId -> dict(nombre, propio, numId, ilvl, basedOn)
        for m in re.finditer(patron, xml, re.S):
            cuerpo = m.group(2)
            nombre = re.search(r'<w:name w:val="([^"]*)"', cuerpo)
            base = re.search(r'<w:basedOn w:val="([^"]*)"', cuerpo)
            num = re.search(r'<w:numId w:val="([^"]*)"', cuerpo)
            ilvl = re.search(r'<w:ilvl w:val="([^"]*)"', cuerpo)
            crudos[m.group(1)] = {
                "nombre": nombre.group(1) if nombre else None,
                "propio": "<w:numPr" in cuerpo,
                "numId": num.group(1) if num else None,
                "ilvl": ilvl.group(1) if ilvl else None,
                "basedOn": base.group(1) if base else None,
            }

        def numera(sid, visto=()):
            """(numera, numId, styleId de origen): numPr propio o HEREDADO."""
            if sid not in crudos or sid in visto:
                return (False, None, None)
            d = crudos[sid]
            if d["propio"]:
                return (True, d["numId"], sid)
            if d["basedOn"]:
                return numera(d["basedOn"], visto + (sid,))
            return (False, None, None)

        self.estilos_crudos = crudos
        for sid, d in crudos.items():
            hay, numid, origen = numera(sid)
            d["numera"] = hay
            d["numId_efectivo"] = numid
            d["numId_origen"] = origen
            if d["nombre"]:
                self.estilos[d["nombre"]] = (sid, hay)
        return self.estilos

    def estilo(self, candidatos, para=""):
        """Nombre REAL del primer candidato que existe en la plantilla.

        Devuelve None y deja aviso si ninguno existe: no se emiten literales
        en ingles sin comprobar (mismo trato que 'Table Grid').
        """
        indice = dict((k.lower(), k) for k in self.estilos)
        for cand in candidatos:
            if cand in self.estilos:
                return cand
            if cand.lower() in indice:
                return indice[cand.lower()]
        self.avisos.append(
            "la plantilla no expone ningun estilo de %s (%s): el volcado deja "
            "esos parrafos en Normal" % (para or "este uso", ", ".join(candidatos)))
        return None

    def estilo_numera(self, nombre):
        """True si el estilo de la plantilla trae numeracion automatica."""
        return bool(nombre) and self.estilos.get(nombre, ("", False))[1]

    def comprobar_numeracion_plantilla(self):
        """Falla si los encabezados numerados de la plantilla no cuadran con
        NIVELES_AUTONUMERADOS. Analogo a comprobar_tdc_plantilla()."""
        numerados = []
        for nivel in range(1, 10):
            nombre = self.estilo(("heading %d" % nivel, "Heading %d" % nivel,
                                  "T\u00edtulo %d" % nivel),
                                 para="encabezado de nivel %d" % nivel)
            if nombre and self.estilo_numera(nombre):
                numerados.append(nivel)
        if tuple(numerados) != tuple(NIVELES_AUTONUMERADOS):
            raise SystemExit(
                "la plantilla numera los niveles %s y la constante "
                "NIVELES_AUTONUMERADOS dice %s: el volcado borraria (o "
                "duplicaria) numeros de titulo. Revisa la plantilla o la "
                "constante antes de volcar." % (tuple(numerados),
                                                tuple(NIVELES_AUTONUMERADOS)))
        return tuple(numerados)

    def _numeraciones_plantilla(self):
        """numId -> [(ilvl, lvlText)] leidos de word/numbering.xml.

        Sin esto, la afirmacion «'Titulo 2 de Apendice' numera con numId 5
        (Apendice %1.)» no es comprobable por nadie que no sepa abrir el ZIP.
        """
        with zipfile.ZipFile(self.plantilla) as z:
            if "word/numbering.xml" not in z.namelist():
                return {}, {}
            xml = z.read("word/numbering.xml").decode("utf-8", "replace")
        abstractos = {}
        for m in re.finditer(r'<w:abstractNum [^>]*w:abstractNumId="([^"]+)"'
                             r'[^>]*>(.*?)</w:abstractNum>', xml, re.S):
            niveles = []
            for lvl in re.finditer(r'<w:lvl [^>]*w:ilvl="([^"]+)"[^>]*>(.*?)</w:lvl>',
                                   m.group(2), re.S):
                txt = re.search(r'<w:lvlText w:val="([^"]*)"', lvl.group(2))
                niveles.append((lvl.group(1), txt.group(1) if txt else ""))
            abstractos[m.group(1)] = niveles
        nums = {}
        for m in re.finditer(r'<w:num [^>]*w:numId="([^"]+)"[^>]*>(.*?)</w:num>',
                             xml, re.S):
            ab = re.search(r'<w:abstractNumId w:val="([^"]*)"', m.group(2))
            nums[m.group(1)] = ab.group(1) if ab else None
        return nums, abstractos

    def escribir_censo_plantilla(self, ruta):
        """Vuelca a texto el censo de estilos de la plantilla con su numPr/numId.

        Existe para que el diagnostico de numeracion sea AUDITABLE sin abrir el
        ZIP: quien solo pueda leer texto debe poder comprobar (a) que existen los
        estilos que el script usa por nombre y (b) que 'Titulo 3 de Apendice'
        hereda el numId del cuerpo, que es lo unico que justifica conservar el
        numero escrito a mano en los apartados A.x.y.
        """
        nums, abstractos = self._numeraciones_plantilla()

        def pinta_num(numid):
            if not numid:
                return "-"
            niveles = abstractos.get(nums.get(numid), [])
            if not niveles:
                return "numId %s (sin lvlText legible)" % numid
            muestra = "; ".join("ilvl %s -> '%s'" % (i, t) for i, t in niveles[:4])
            return "numId %s [%s]" % (numid, muestra)

        usados = [("pie de figura", ESTILO_PIE_FIGURA),
                  ("tabla", ESTILO_TABLA),
                  ("titulo de apendice / sin numerar", ESTILO_APENDICE_TITULO),
                  ("apendice nivel 2", ESTILO_APENDICE_N2),
                  ("apendice nivel 3", ESTILO_APENDICE_N3),
                  ("elementos de lista", ESTILO_LISTA),
                  ("codigo fuente", ESTILO_CODIGO)]
        # por la MISMA puerta que el .docx y el Markdown intermedio: derivar la
        # ruta de self.salida no basta. Si el .docx no existe pero este .txt si,
        # sin la puerta se pisaria una corrida anterior sin --sobrescribir y sin
        # aviso.
        ruta = self.validar_ruta_escritura(
            ruta, (".txt",), "censo de estilos de la plantilla")
        with open(ruta, "w", encoding="utf-8") as fh:
            fh.write("censo de estilos de la plantilla de volcado\n")
            fh.write("plantilla: %s\n" % self.plantilla)
            fh.write("commit: %s\n" % self.commit)
            fh.write("fecha: %s\n"
                     % datetime.datetime.now().isoformat(timespec="seconds"))
            fh.write("estilos declarados en word/styles.xml: %d\n"
                     % len(self.estilos_crudos))
            fh.write("\n== (1) ESTILOS QUE EL VOLCADO USA POR NOMBRE ==\n")
            fh.write("   (se resuelven por w:name; el script nunca emite el "
                     "literal en ingles sin comprobarlo)\n")
            for para, candidatos in usados:
                nombre = None
                indice = dict((k.lower(), k) for k in self.estilos)
                for cand in candidatos:
                    if cand in self.estilos:
                        nombre = cand
                        break
                    if cand.lower() in indice:
                        nombre = indice[cand.lower()]
                        break
                if nombre is None:
                    fh.write("  [FALTA] %-34s candidatos: %s\n"
                             % (para, ", ".join(candidatos)))
                    continue
                sid = self.estilos[nombre][0]
                d = self.estilos_crudos.get(sid, {})
                fh.write("  [OK]    %-34s w:name='%s'  styleId='%s'  "
                         "numera=%s  %s\n"
                         % (para, nombre, sid, "si" if d.get("numera") else "no",
                            pinta_num(d.get("numId_efectivo"))))
            fh.write("\n== (2) ENCABEZADOS Y ESTILOS CON NUMERACION ==\n")
            fh.write("   numera=si significa numPr propio o HEREDADO por "
                     "basedOn; 'origen' es el styleId del que trae el numPr\n")
            filas = []
            for sid, d in self.estilos_crudos.items():
                if not d.get("numera"):
                    continue
                filas.append((d.get("nombre") or "(sin w:name)", sid, d))
            for nombre, sid, d in sorted(filas):
                propio = "propio" if d.get("propio") else \
                    "heredado de '%s'" % (d.get("numId_origen") or "?")
                fh.write("  %-32s styleId='%s'  %-24s %s\n"
                         % (nombre, sid, propio,
                            pinta_num(d.get("numId_efectivo"))))
            fh.write("\n== (3) DIAGNOSTICO DE LOS APARTADOS A.x.y ==\n")
            for para, candidatos in (("apendice nivel 2", ESTILO_APENDICE_N2),
                                     ("apendice nivel 3", ESTILO_APENDICE_N3)):
                nombre = candidatos[0]
                if nombre not in self.estilos:
                    fh.write("  %s: el estilo '%s' NO existe en la plantilla\n"
                             % (para, nombre))
                    continue
                sid = self.estilos[nombre][0]
                d = self.estilos_crudos.get(sid, {})
                fh.write("  '%s' -> styleId '%s', numera=%s, numPr %s, %s\n"
                         % (nombre, sid, "si" if d.get("numera") else "no",
                            "propio" if d.get("propio") else "heredado de '%s'"
                            % (d.get("numId_origen") or "?"),
                            pinta_num(d.get("numId_efectivo"))))
            fh.write("  Lectura: si el numId efectivo del nivel 3 de apendice "
                     "coincide con el de los encabezados del CUERPO, Word "
                     "numeraria A.x.y con la serie de los capitulos; por eso el "
                     "volcado CONSERVA el numero escrito a mano (conservar="
                     "%s).\n" % self.conservar_numeros_apendice)
            fh.write("\n== (4) NIVELES DE ENCABEZADO AUTONUMERADOS ==\n")
            for nivel in range(1, 10):
                nombre = None
                for cand in ("heading %d" % nivel, "Heading %d" % nivel,
                             "Título %d" % nivel):
                    indice = dict((k.lower(), k) for k in self.estilos)
                    if cand.lower() in indice:
                        nombre = indice[cand.lower()]
                        break
                if nombre is None:
                    fh.write("  nivel %d: sin estilo en la plantilla\n" % nivel)
                    continue
                sid = self.estilos[nombre][0]
                d = self.estilos_crudos.get(sid, {})
                fh.write("  nivel %d: '%s' (styleId '%s') numera=%s  %s\n"
                         % (nivel, nombre, sid, "si" if d.get("numera") else "no",
                            pinta_num(d.get("numId_efectivo"))))
            fh.write("  NIVELES_AUTONUMERADOS declarado en el script: %s\n"
                     % (NIVELES_AUTONUMERADOS,))
        return ruta

    def comprobar_tdc_plantilla(self):
        """Informa de si la plantilla ya trae una tabla de contenido."""
        with zipfile.ZipFile(self.plantilla) as z:
            doc = z.read("word/document.xml").decode("utf-8", "replace")
        return "TOC" in doc and "instrText" in doc

    # --------------------------------------------------------------- indice
    def leer_indice(self):
        """Devuelve [(capitulo, subgrupo, nivel_base, ruta)] en orden del indice.

        nivel_base es el nivel de encabezado que le corresponde al H1 de la
        nota: 2 si cuelga de un grupo '##', 3 si cuelga de un subgrupo '###'.
        El subgrupo NO es solo un desplazamiento de nivel: construir_markdown()
        emite su propio encabezado, o el capitulo 2 quedaria con 14 notas en
        Titulo 3 colgando de un Titulo 1 (numeracion tipo 2.0.1).
        """
        entradas = []
        capitulo = None
        subgrupo = None
        with open(self.indice, encoding="utf-8") as fh:
            lineas = fh.read().splitlines()
        for linea in lineas:
            m2 = re.match(r"^## +(.*\S)\s*$", linea)
            m3 = re.match(r"^### +(.*\S)\s*$", linea)
            if m2:
                capitulo, subgrupo = m2.group(1), None
                continue
            if m3:
                subgrupo = m3.group(1)
                continue
            mb = re.match(r"^- +\[\[([^\]|]+)(?:\|([^\]]+))?\]\]", linea)
            if not mb or capitulo is None:
                continue
            if any(capitulo.startswith(g) for g in GRUPOS_FUERA):
                continue
            destino = mb.group(1).split("/")[-1].strip()
            ruta = self.notas_disco.get(destino)
            if ruta is None:
                self.avisos.append("nota del indice sin fichero en disco: " + destino)
                continue
            entradas.append((capitulo, subgrupo, 3 if subgrupo else 2, ruta))
        return entradas

    @staticmethod
    def clave_capitulo(titulo):
        """'3. Diseno del sistema' -> '3'; 'Apendices' -> 'Apendices'."""
        m = re.match(r"^(\d+)\.", titulo)
        return m.group(1) if m else _sin_tildes(titulo.strip())

    @staticmethod
    def contexto_capitulo(titulo):
        """'cuerpo' para los capitulos 1-6; 'apendice' / 'preliminar' si no."""
        clave = ExportadorDocx.clave_capitulo(titulo)
        if clave.isdigit():
            return "cuerpo"
        if clave.lower().startswith("apendice"):
            return "apendice"
        return "preliminar"

    # -------------------------------------------------- transformaciones MD
    @staticmethod
    def quitar_frontmatter(texto):
        """Elimina el bloque YAML de cabecera SOLO si es frontmatter real.

        Exigir 'clave: valor' en la primera linea evita comerse contenido en una
        nota que empiece por una regla horizontal '---'.
        """
        m = re.match(r"^---[ \t]*\r?\n([A-Za-z_][\w.-]*[ \t]*:[^\n]*\r?\n"
                     r"(?:[^\n]*\r?\n)*?)---[ \t]*\r?\n", texto)
        if m:
            return texto[m.end():]
        return texto

    def procesar_callouts(self, texto, nota):
        """Degrada a prosa TODO callout y borra solo el andamiaje declarado.

        Deja parte INTEGRO de cada callout (nota, titulo, si trae [n], accion) y
        marca en rojo cualquier borrado que se llevaria una cita: ningun [n]
        puede caer por la via del borrado.

        La deteccion NO ancla el '>' en la columna 0. Anclarlo dejaba a los
        callouts INDENTADOS (los que van dentro de un elemento de lista) fuera
        de TODO el procesado: no se borraban, no se degradaban, no se contaban y
        no se auditaban, y entraban en el .docx con la sintaxis Obsidian cruda
        visible ('> [!info] Trazabilidad - ...'). Eran cinco en la memoria
        completa, tres de ellos `Trazabilidad`, que es andamiaje. La indentacion
        puede ser con espacios O CON TABULADOR: los dos casos existen en disco.
        """
        salida = []
        lineas = texto.split("\n")
        i = 0
        nombre_nota = os.path.basename(nota)[:-3]
        while i < len(lineas):
            m = re.match(r"^[ \t]*> *\[!(\w+)\][-+]? *(.*)$", lineas[i])
            if not m:
                salida.append(lineas[i])
                i += 1
                continue
            tipo, titulo = m.group(1), m.group(2).strip()
            cuerpo = []
            j = i + 1
            while j < len(lineas) and lineas[j].lstrip(" \t").startswith(">"):
                cuerpo.append(re.sub(r"^[ \t]*> ?", "", lineas[j]))
                j += 1
            citas = citas_en("\n".join([titulo] + cuerpo))
            andamiaje = self._es_andamiaje(tipo, titulo)
            degradar = not andamiaje
            self.callouts.append({
                "nota": nombre_nota, "tipo": tipo, "titulo": titulo,
                "citas": citas, "andamiaje": andamiaje,
                "indentado": bool(re.match(r"^[ \t]+", lineas[i])),
                "accion": "degradado" if degradar else "borrado",
            })
            if degradar:
                salida.append("")
                if titulo:
                    salida.append("**" + titulo + "**")
                    salida.append("")
                salida.extend(cuerpo)
                salida.append("")
                self.callouts_degradados += 1
            else:
                self.callouts_borrados += 1
            i = j
        return "\n".join(salida)

    def comprobar_citas_en_callouts(self, md):
        """Aborta si un callout borrado se lleva una cita que NO sobrevive.

        La invariante es que ninguna entrada [n] desaparezca del volcado. Un
        callout borrado que citaba [18] no rompe nada si [18] sigue citada en
        otro sitio del Markdown final; si es la unica sede, se aborta y lo
        decide Francisco (sacar el titulo de ANDAMIAJE o mover la cita).

        RED DE SEGURIDAD DE LA LISTA DE ANDAMIAJE (decision de Francisco,
        2026-08-22). Desde que degradar es el defecto, la unica via por la que
        se pierde contenido es un anadido a ANDAMIAJE / ANDAMIAJE_TIPOS, asi
        que esta comprobacion pasa a guardar precisamente esa lista: si un
        futuro anadido se lleva la unica sede de una cita, la corrida ABORTA y
        el mensaje senala la lista. Deliberadamente NO hay detector semantico
        de «salvedad metodologica»: seria fragil y cubriria dos veces el mismo
        riesgo (decision explicita de Francisco de no construirlo).
        """
        vivas = set(citas_en(md))
        perdidas = []
        for c in self.callouts:
            if c["accion"] != "borrado" or not c["citas"]:
                continue
            huerfanas = sorted(set(c["citas"]) - vivas, key=int)
            if huerfanas:
                perdidas.append((c, huerfanas))
            else:
                self.avisos.append(
                    "callout borrado con citas que SI sobreviven en otra sede: "
                    "%s | [!%s] %s | %s" % (c["nota"], c["tipo"], c["titulo"],
                                            ", ".join("[%s]" % n for n in c["citas"])))
        if not perdidas:
            return
        detalle = "\n".join(
            "  [ROJO] %s | [!%s] %s | unica sede de: %s"
            % (c["nota"], c["tipo"], c["titulo"], ", ".join("[%s]" % n for n in h))
            for c, h in perdidas)
        raise SystemExit(
            "el volcado perderia entradas de cita por el borrado de callouts "
            "de ANDAMIAJE:\n" + detalle + "\nSaca esos titulos de ANDAMIAJE / "
            "ANDAMIAJE_TIPOS (con lo que se degradaran a prosa, que es el "
            "defecto) o mueve la cita a la prosa, antes de volcar.")

    @staticmethod
    def _es_andamiaje(tipo, titulo):
        """True si el callout es andamiaje del vault y por tanto se BORRA.

        Es la unica via de borrado que queda: todo lo demas se degrada a prosa.
        Se decide por el TIPO ([!todo] = tarea abierta del vault) o por un
        fragmento del TITULO, comparado sin tildes.
        """
        if tipo.lower() in ANDAMIAJE_TIPOS:
            return True
        t = _sin_tildes(titulo)
        return any(a in t for a in ANDAMIAJE)

    @staticmethod
    def resolver_wikilinks(texto):
        """Quita el vinculo y deja la frase en texto plano (alias si existe).

        Los destinos de apendice se remiten como 'el apendice A.3', no como el
        titulo de la nota.
        """
        def rep(m):
            destino, alias = m.group(1), m.group(2)
            hoja = destino.split("/")[-1].strip()
            ma = re.match(r"^(A\.\d+(?:\.\d+)*)", hoja)
            if ma:
                return "el ap\u00e9ndice " + ma.group(1)
            if alias:
                return alias.strip()
            return hoja

        texto = re.sub(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]", rep, texto)
        # remisiones a apendices ya escritas en prosa
        texto = re.sub(r"\b([Ll])a secci[o\u00f3]n (A\.\d)",
                       "\\1l ap\u00e9ndice \\2", texto)
        texto = re.sub(r"\bsecci[o\u00f3]n (A\.\d)", "ap\u00e9ndice \\1", texto)
        # y las duplicaciones que la sustitucion pueda dejar
        texto = re.sub(r"(?:la secci[o\u00f3]n|el ap[e\u00e9]ndice)\s+"
                       r"el ap[e\u00e9]ndice", "el ap\u00e9ndice", texto)
        texto = re.sub(r"\bel\s+el ap[e\u00e9]ndice", "el ap\u00e9ndice", texto)
        return texto

    def resolver_embebidos(self, texto):
        """![[x.png]] -> imagen contra assets/; el pie siguiente al pie de figura."""
        estilo_pie = self.estilo(ESTILO_PIE_FIGURA, para="pie de figura")
        lineas = texto.split("\n")
        salida = []
        k = 0
        while k < len(lineas):
            m = re.match(r"^!\[\[([^\]]+)\]\]\s*$", lineas[k].strip())
            if not m:
                salida.append(lineas[k])
                k += 1
                continue
            fichero = m.group(1).split("|")[0].strip()
            if not os.path.isfile(os.path.join(ASSETS, fichero)):
                self.avisos.append("embebido sin fichero en assets/: " + fichero)
            ruta = os.path.join(ASSETS, fichero).replace("\\", "/")
            salida.append("![](%s)" % ruta)
            salida.append("")
            p = k + 1
            while p < len(lineas) and lineas[p].strip() == "":
                p += 1
            if p < len(lineas) and re.match(r"^\**Figura", lineas[p].strip()):
                if estilo_pie:
                    salida.append('::: {custom-style="%s"}' % estilo_pie)
                    salida.append(lineas[p].strip())
                    salida.append(":::")
                else:
                    salida.append(lineas[p].strip())
                salida.append("")
                k = p + 1
            else:
                k = k + 1
        return "\n".join(salida)

    @staticmethod
    def quitar_numero(titulo):
        """Quita el numero escrito a mano al inicio del titulo del encabezado."""
        return re.sub(r"^(?:\d+(?:\.\d+)*|[A-Z]\.\d+(?:\.\d+)*)\.?\s+", "", titulo)

    # ------------------------------------------------------- encabezados
    def emitir_encabezado(self, nivel, titulo, contexto):
        """Lineas de Markdown para un encabezado del nivel y contexto dados.

        - cuerpo: '#'*nivel hasta 6; por encima, div con el estilo real de la
          plantilla ('heading 7'..'heading 9'), resuelto por w:name.
        - apendice: estilos propios de la plantilla ('Apendice',
          'Titulo 2 de Apendice', 'Titulo 3 de Apendice'), o el 'Titulo 1'
          autonumerado se comeria la letra de A.1/A.2/A.3.
        - preliminar: sin numeracion (Resumen y Abstract no llevan numero).
        """
        titulo = titulo.strip()
        if contexto == "apendice":
            if nivel <= 1:
                estilo = self.estilo(ESTILO_APENDICE_TITULO, para="titulo de apendice")
                return self._div(estilo, titulo, "# " + titulo)
            if nivel == 2:
                estilo = self.estilo(ESTILO_APENDICE_N2, para="apendice nivel 2")
                if self.estilo_numera(estilo):
                    titulo = self.quitar_numero(titulo)
                return self._div(estilo, titulo, "## " + titulo)
            if nivel == 3:
                estilo = self.estilo(ESTILO_APENDICE_N3, para="apendice nivel 3")
                if self.estilo_numera(estilo) and not self.conservar_numeros_apendice:
                    titulo = self.quitar_numero(titulo)
                elif self.estilo_numera(estilo):
                    aviso = ("DEFECTO DE LA PLANTILLA: 'Titulo 3 de Apendice' "
                             "hereda la numeracion del cuerpo (numId del "
                             "capitulo), no la del apendice; el volcado "
                             "CONSERVA el numero a mano de los apartados A.x.y "
                             "para que el desajuste se vea. --numerar-apendice-n3 "
                             "lo quita.")
                    if aviso not in self.avisos:
                        self.avisos.append(aviso)
                return self._div(estilo, titulo, "### " + titulo)
            # nivel 4+: 'Titulo 4' no numera; el numero escrito a mano se queda
            return ["#" * min(nivel, 6) + " " + titulo]
        if contexto == "preliminar":
            estilo = self.estilo(ESTILO_APENDICE_TITULO, para="titulo sin numerar")
            if nivel <= 2:
                return self._div(estilo, titulo, "# " + titulo)
            return ["", "**" + titulo + "**", ""]
        # cuerpo de la memoria
        if nivel <= 6:
            if nivel in NIVELES_AUTONUMERADOS:
                titulo = self.quitar_numero(titulo)
            return ["#" * nivel + " " + titulo]
        estilo = self.estilo(("heading %d" % nivel, "Heading %d" % nivel,
                              "T\u00edtulo %d" % nivel),
                             para="encabezado de nivel %d" % nivel)
        if self.estilo_numera(estilo):
            titulo = self.quitar_numero(titulo)
        return self._div(estilo, titulo, "###### " + titulo)

    @staticmethod
    def _div(estilo, titulo, respaldo):
        """Div con custom-style, o el respaldo si el estilo no existe."""
        if not estilo:
            return [respaldo]
        return ["", '::: {custom-style="%s"}' % estilo, titulo, ":::", ""]

    def desplazar_encabezados(self, texto, nivel_base, contexto):
        """Sube los encabezados de la nota al nivel que le toca en la memoria."""
        desfase = nivel_base - 1
        salida = []
        en_codigo = False
        for linea in texto.split("\n"):
            if linea.lstrip().startswith("```"):
                en_codigo = not en_codigo
                salida.append(linea)
                continue
            m = re.match(r"^(#{1,6}) +(.*)$", linea)
            if m and not en_codigo:
                nivel = min(len(m.group(1)) + desfase, 9)
                salida.extend(self.emitir_encabezado(nivel, m.group(2), contexto))
            else:
                salida.append(linea)
        return "\n".join(salida)

    # ------------------------------------------------------------ recuentos
    @staticmethod
    def palabras_prosa(texto):
        """(palabras de prosa, palabras en bruto) del Markdown transformado.

        El bruto cuenta TODO —pipes de tabla, ':::' de los divs, rutas de
        imagen y el contenido de los bloques de codigo—, asi que infla el
        recuento. La estimacion de paginas usa la prosa.
        """
        bruto = len(texto.split())
        limpio = []
        en_codigo = False
        for linea in texto.split("\n"):
            if linea.lstrip().startswith("```"):
                en_codigo = not en_codigo
                continue
            if en_codigo:
                continue
            s = linea.strip()
            if s.startswith(":::") or s.startswith("|") or s.startswith("!["):
                continue
            limpio.append(re.sub(r"^#+\s*", "", linea))
        return len(" ".join(limpio).split()), bruto

    # ---------------------------------------------------------------- monta
    def construir_markdown(self):
        """Concatena todas las notas seleccionadas en un unico Markdown."""
        entradas = self.leer_indice()
        bloques = []
        capitulo_previo = None
        subgrupo_previo = None
        prosa_cap = 0
        bruto_cap = 0
        for capitulo, subgrupo, nivel_base, ruta in entradas:
            clave = self.clave_capitulo(capitulo)
            if self.capitulos and clave not in self.capitulos:
                continue
            contexto = self.contexto_capitulo(capitulo)
            if capitulo != capitulo_previo:
                if capitulo_previo is not None:
                    self.paginas.append((capitulo_previo, prosa_cap, bruto_cap))
                    prosa_cap = bruto_cap = 0
                if contexto != "preliminar":
                    bloques.append("\n".join(
                        self.emitir_encabezado(1, capitulo, contexto)) + "\n")
                capitulo_previo = capitulo
                subgrupo_previo = None
            if subgrupo and subgrupo != subgrupo_previo:
                # el subgrupo del indice ES jerarquia: sin este encabezado las
                # notas quedan en Titulo 3 colgando de un Titulo 1
                bloques.append("\n".join(
                    self.emitir_encabezado(2, subgrupo, contexto)) + "\n")
                subgrupo_previo = subgrupo
            with open(ruta, encoding="utf-8") as fh:
                crudo = fh.read()
            if "```mermaid" in crudo:
                self.avisos.append(
                    "ANDAMIAJE: %s trae un bloque ```mermaid; Word lo publicara "
                    "como codigo fuente tal cual (no se borra por decision del "
                    "script)" % os.path.basename(ruta)[:-3])
            texto = self.quitar_frontmatter(crudo)
            texto = self.procesar_callouts(texto, ruta)
            # ORDEN OBLIGATORIO: los embebidos ANTES de los wikilinks. Al
            # reves, la regex de wikilinks se come el '[[x.png]]' de
            # '![[x.png]]' y deja '!x.png': la imagen se pierde en silencio.
            texto = self.resolver_embebidos(texto)
            texto = self.resolver_wikilinks(texto)
            texto = self.desplazar_encabezados(texto, nivel_base, contexto)
            texto = re.sub(r"\n{3,}", "\n\n", texto).strip()
            prosa, bruto = self.palabras_prosa(texto)
            prosa_cap += prosa
            bruto_cap += bruto
            self.citas_md.extend(citas_en(texto))
            bloques.append(texto + "\n")
        if capitulo_previo is not None:
            self.paginas.append((capitulo_previo, prosa_cap, bruto_cap))
        if not bloques:
            raise SystemExit("Ninguna nota seleccionada: revisa --capitulos.")
        md = "\n\n".join(bloques)
        self.comprobar_citas_en_callouts(md)
        return md

    # -------------------------------------------------------------- pandoc
    def ejecutar_pandoc(self, md_path):
        """Convierte el Markdown intermedio a .docx con la plantilla."""
        if not os.path.isfile(self.pandoc):
            raise SystemExit("No se encuentra pandoc en: " + self.pandoc)
        if not os.path.isfile(self.plantilla):
            raise SystemExit("No se encuentra la plantilla en: " + self.plantilla)
        carpeta = os.path.dirname(self.salida)
        if carpeta:
            os.makedirs(carpeta, exist_ok=True)
        formato = ("markdown+pipe_tables+tex_math_dollars+fenced_divs"
                   "+bracketed_spans+implicit_figures")
        cmd = [self.pandoc, md_path, "--from", formato, "--to", "docx",
               "--reference-doc", self.plantilla, "--resource-path", ASSETS,
               "--output", self.salida]
        proc = subprocess.run(cmd, capture_output=True, text=True)
        if proc.returncode != 0:
            raise SystemExit("pandoc fallo:\n" + (proc.stderr or ""))
        if proc.stderr and proc.stderr.strip():
            self.avisos.append("pandoc: " + proc.stderr.strip().replace("\n", " | "))

    # --------------------------------------------------- post-proceso docx
    def postprocesar_docx(self):
        """Estilo de tabla + remapeo de los pStyle que inyecta pandoc.

        Devuelve (n_tablas, {pStyle inyectado: veces remapeadas}).
        """
        with zipfile.ZipFile(self.salida) as z:
            nombres = z.namelist()
            datos = dict((n, z.read(n)) for n in nombres)
        doc = datos["word/document.xml"].decode("utf-8")
        n_tablas = doc.count("<w:tbl>")

        nombre_tabla = self.estilo(ESTILO_TABLA, para="tabla")
        if nombre_tabla:
            style_id = self.estilos[nombre_tabla][0]
            ref = '<w:tblStyle w:val="%s"/>' % style_id
            doc = re.sub(r'<w:tblStyle w:val="[^"]*"\s*/>', ref, doc)
            doc = doc.replace("<w:tblPr>", "<w:tblPr>" + ref)
            doc = doc.replace(ref + ref, ref)

        remapeos = {}
        for inyectado, candidatos in REMAPEO_PSTYLE.items():
            patron = re.compile(r'<w:pStyle w:val="%s"\s*/>' % inyectado)
            veces = len(patron.findall(doc))
            if not veces:
                continue
            destino = ""
            if candidatos:
                nombre = self.estilo(candidatos, para="estilo de " + inyectado)
                if nombre:
                    destino = '<w:pStyle w:val="%s"/>' % self.estilos[nombre][0]
            doc = patron.sub(destino, doc)
            remapeos[inyectado] = veces
        datos["word/document.xml"] = doc.encode("utf-8")
        tmp = self.salida + ".tmp"
        with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as z:
            for n in nombres:
                z.writestr(n, datos[n])
        shutil.move(tmp, self.salida)
        return n_tablas, remapeos

    def auditar_docx(self):
        """Lee el .docx GENERADO: citas [n], estilos de parrafo e imagenes."""
        with zipfile.ZipFile(self.salida) as z:
            doc = z.read("word/document.xml").decode("utf-8", "replace")
            # las imagenes DEL VOLCADO son las que referencia el cuerpo: la
            # plantilla trae media propia (logos de encabezado) que no cuenta
            imagenes = len(re.findall(r"<a:blip", doc))
        texto = re.sub(r"<[^>]+>", "", re.sub(r"</w:p>", "\n", doc))
        estilos = {}
        for sid in re.findall(r'<w:pStyle w:val="([^"]+)"', doc):
            estilos[sid] = estilos.get(sid, 0) + 1
        return {"citas": citas_en(texto), "estilos": estilos,
                "imagenes": imagenes,
                "colgantes": sorted(set(
                    sid for sid in estilos
                    if sid not in [v[0] for v in self.estilos.values()]))}

    def escribir_censo_docx(self, auditoria, n_tablas, remapeos):
        """Persiste el censo de pStyle del .docx GENERADO junto al artefacto.

        No confundir con `*_estilos_plantilla.txt`, que censa la PLANTILLA: son
        dos cosas distintas. Este fichero censa el DOCUMENTO producido, y existe
        porque `auditar_docx()` calculaba ese diccionario y solo lo imprimia por
        consola: las cifras de tablas y de encabezados del .docx no eran
        comprobables sin descomprimir el ZIP, y quien audita no tiene
        descompresion. Con esto se leen en texto plano.
        """
        ruta = self.validar_ruta_escritura(
            os.path.splitext(self.salida)[0] + "_estilos_docx.txt",
            (".txt",), "censo de estilos del .docx")
        inversa = dict((sid, nombre) for nombre, (sid, _n)
                       in self.estilos.items())
        with open(ruta, "w", encoding="utf-8") as fh:
            fh.write("censo del .docx GENERADO (no de la plantilla)\n")
            fh.write("docx: %s\n" % os.path.basename(self.salida))
            fh.write("commit: %s\n" % self.commit)
            fh.write("fecha: %s\n"
                     % datetime.datetime.now().isoformat(timespec="seconds"))
            fh.write("capitulos: %s\n" % (",".join(self.capitulos)
                                          if self.capitulos
                                          else "memoria completa"))
            fh.write("\n== RECUENTOS DEL DOCUMENTO ==\n")
            fh.write("  tablas (<w:tbl>): %d\n" % n_tablas)
            fh.write("  imagenes (<a:blip>): %d\n" % auditoria["imagenes"])
            fh.write("  marcadores de cita [n]: %d (%d entradas distintas)\n"
                     % (len(auditoria["citas"]), len(set(auditoria["citas"]))))
            fh.write("  pStyle inyectados por pandoc y remapeados: %s\n"
                     % (remapeos or "ninguno"))
            fh.write("\n== ESTILOS DE PARRAFO (w:pStyle) DEL DOCUMENTO ==\n")
            fh.write("   columnas: veces | styleId | w:name en la plantilla\n")
            for sid, veces in sorted(auditoria["estilos"].items(),
                                     key=lambda kv: (-kv[1], kv[0])):
                fh.write("  %6d  %-28s %s\n"
                         % (veces, sid, inversa.get(sid, "(NO en la plantilla)")))
            fh.write("\n== ESTILOS COLGANTES (en el .docx, no en la plantilla) ==\n")
            if not auditoria["colgantes"]:
                fh.write("   (ninguno)\n")
            for sid in auditoria["colgantes"]:
                fh.write("  - %s\n" % sid)
            fh.write("\nADVERTENCIA: el volcado es destructivo respecto al "
                     "trabajo manual en Word; re-ejecutar revive lo borrado.\n")
        return ruta

    # -------------------------------------------------------------- informe
    def informar(self, auditoria):
        """Recuento de paginas, parte de callouts, citas y avisos."""
        print("")
        print("=== Recuento estimado de paginas (%d palabras/pagina de prosa) ==="
              % PALABRAS_POR_PAGINA)
        print("  (prosa = sin bloques de codigo, filas de tabla, divs ':::' ni "
              "rutas de imagen; el bruto se muestra al lado y esta inflado)")
        total_p = total_b = 0
        for capitulo, prosa, bruto in self.paginas:
            total_p += prosa
            total_b += bruto
            print("  %-32s prosa %7d  ~%6.1f pag.   bruto %7d"
                  % (capitulo, prosa, prosa / float(PALABRAS_POR_PAGINA), bruto))
        print("  %-32s prosa %7d  ~%6.1f pag.   bruto %7d"
              % ("TOTAL", total_p, total_p / float(PALABRAS_POR_PAGINA), total_b))

        print("")
        print("=== Callouts ===")
        print("  vistos: %d   borrados: %d   degradados a prosa: %d"
              % (len(self.callouts), self.callouts_borrados,
                 self.callouts_degradados))
        print("  (politica 2026-08-22: degradar es el DEFECTO; se borra solo el "
              "andamiaje de ANDAMIAJE / ANDAMIAJE_TIPOS)")
        print("  de ellos, INDENTADOS (dentro de un elemento de lista): %d"
              % sum(1 for c in self.callouts if c.get("indentado")))
        borrados = [c for c in self.callouts if c["accion"] == "borrado"]
        if borrados:
            print("")
            print("  LISTADO INTEGRO DE CALLOUTS BORRADOS "
                  "(nota | titulo | citas | andamiaje):")
            for c in borrados:
                print("   - %-34s %-52s %-10s %s"
                      % (c["nota"][:34], ("[!%s] %s" % (c["tipo"], c["titulo"]))[:52],
                         ", ".join("[%s]" % n for n in c["citas"]) or "sin citas",
                         "andamiaje" if c["andamiaje"] else "CONTENIDO"))

        print("")
        print("=== Citas [n] ===")
        print("  en el Markdown intermedio: %d marcadores, %d entradas distintas"
              % (len(self.citas_md), len(set(self.citas_md))))
        print("  en el .docx generado:      %d marcadores, %d entradas distintas"
              % (len(auditoria["citas"]), len(set(auditoria["citas"]))))
        perdidas = sorted(set(self.citas_md) - set(auditoria["citas"]), key=int)
        if perdidas:
            print("  [ROJO] entradas que no llegan al .docx: "
                  + ", ".join("[%s]" % n for n in perdidas))

        if auditoria["colgantes"]:
            self.avisos.append("estilos de parrafo en el .docx que la plantilla "
                               "no define: " + ", ".join(auditoria["colgantes"]))
        if self.avisos:
            print("")
            print("=== Avisos ===")
            for aviso in self.avisos:
                print("  - " + aviso)

    def escribir_procedencia(self, auditoria, md_path):
        """Sella la procedencia de la corrida junto al artefacto."""
        # por la MISMA puerta que el resto (ver escribir_censo_plantilla)
        ruta = self.validar_ruta_escritura(
            os.path.splitext(self.salida)[0] + "_procedencia.txt",
            (".txt",), "parte de procedencia")
        with open(ruta, "w", encoding="utf-8") as fh:
            fh.write("volcado del vault al .docx\n")
            fh.write("commit: %s\n" % self.commit)
            fh.write("fecha: %s\n" % datetime.datetime.now().isoformat(timespec="seconds"))
            fh.write("capitulos: %s\n" % (",".join(self.capitulos) if self.capitulos
                                          else "memoria completa"))
            fh.write("plantilla: %s\n" % self.plantilla)
            fh.write("pandoc: %s\n" % self.pandoc)
            fh.write("markdown intermedio: %s\n" % md_path)
            fh.write("citas [n] en el .docx: %d (%d distintas)\n"
                     % (len(auditoria["citas"]), len(set(auditoria["citas"]))))
            fh.write("imagenes embebidas: %d\n" % auditoria["imagenes"])
            fh.write("callouts: %d vistos, %d borrados, %d degradados\n"
                     % (len(self.callouts), self.callouts_borrados,
                        self.callouts_degradados))
            fh.write("censo de estilos de la plantilla: %s\n"
                     % os.path.basename(self.ruta_censo_estilos or "-"))
            fh.write("censo de estilos del .docx generado: %s\n"
                     % os.path.basename(self.ruta_censo_docx or "-"))
            fh.write("politica de callouts: degradar a prosa es el DEFECTO; se "
                     "borra solo el andamiaje (ANDAMIAJE / ANDAMIAJE_TIPOS)\n")
            # El recuento de paginas por capitulo tambien se PERSISTE: si vive
            # solo en la consola, ninguna cifra de paginas que se cite en
            # PIPELINE.md es comprobable por quien solo pueda leer texto plano.
            fh.write("\n== RECUENTO ESTIMADO DE PAGINAS (%d palabras/pagina de "
                     "prosa) ==\n" % PALABRAS_POR_PAGINA)
            fh.write("   MIDE: prosa. NO MIDE: bloques de codigo, filas de "
                     "tabla, divs ':::' ni rutas de imagen, que en Word SI "
                     "ocupan pagina. Es por tanto una INFRAESTIMACION del "
                     "grosor del documento, no la longitud de la memoria.\n")
            fh.write("   columnas: capitulo | palabras de prosa | paginas "
                     "estimadas | palabras en bruto (inflado)\n")
            total_p = total_b = 0
            for capitulo, prosa, bruto in self.paginas:
                total_p += prosa
                total_b += bruto
                fh.write("  %-32s %7d  ~%6.1f pag.  bruto %7d\n"
                         % (capitulo, prosa,
                            prosa / float(PALABRAS_POR_PAGINA), bruto))
            fh.write("  %-32s %7d  ~%6.1f pag.  bruto %7d\n"
                     % ("TOTAL", total_p,
                        total_p / float(PALABRAS_POR_PAGINA), total_b))
            fh.write("  callouts indentados detectados (dentro de un elemento "
                     "de lista): %d\n"
                     % sum(1 for c in self.callouts if c.get("indentado")))
            # El RECUENTO no dice QUE contenido quedo fuera. Sin este listado,
            # saber que se perdio exigiria capturar la consola de la corrida.
            fh.write("\n== CALLOUTS BORRADOS (contenido que NO entra en el "
                     ".docx) ==\n")
            fh.write("   columnas: nota | [!tipo] titulo | citas | clase\n")
            borrados = [c for c in self.callouts if c["accion"] == "borrado"]
            if not borrados:
                fh.write("   (ninguno)\n")
            for c in borrados:
                fh.write("  - %s | [!%s] %s | %s | %s\n"
                         % (c["nota"], c["tipo"], c["titulo"],
                            ", ".join("[%s]" % n for n in c["citas"])
                            or "sin citas",
                            "andamiaje" if c["andamiaje"] else "CONTENIDO"))
            fh.write("\n== CALLOUTS DEGRADADOS A PROSA (el texto entra, la caja "
                     "no) ==\n")
            degradados = [c for c in self.callouts if c["accion"] == "degradado"]
            if not degradados:
                fh.write("   (ninguno)\n")
            for c in degradados:
                fh.write("  - %s | [!%s] %s | %s\n"
                         % (c["nota"], c["tipo"], c["titulo"],
                            ", ".join("[%s]" % n for n in c["citas"])
                            or "sin citas"))
            if self.avisos:
                fh.write("\n== AVISOS DE LA CORRIDA ==\n")
                for aviso in self.avisos:
                    fh.write("  - %s\n" % aviso)
            fh.write("\nADVERTENCIA: el volcado es destructivo respecto al "
                     "trabajo manual en Word; re-ejecutar revive lo borrado.\n")
        return ruta

    # ----------------------------------------------------------------- run
    def ejecutar(self, md_intermedio=None):
        """Genera el Markdown unico, lo convierte y emite el informe."""
        print("ADVERTENCIA: el volcado es destructivo respecto al trabajo "
              "manual en Word; re-ejecutar revive lo borrado.")
        self.cargar_estilos_plantilla()
        self.comprobar_numeracion_plantilla()
        self.validar_destino(md_intermedio=md_intermedio)
        os.makedirs(SALIDA_DIR, exist_ok=True)
        # el censo de estilos se deja JUNTO al artefacto para que el diagnostico
        # de numeracion sea comprobable sin abrir el ZIP de la plantilla
        self.ruta_censo_estilos = self.escribir_censo_plantilla(
            os.path.splitext(self.salida)[0] + "_estilos_plantilla.txt")
        print("censo de estilos de la plantilla: " + self.ruta_censo_estilos)
        md = self.construir_markdown()
        md_path = md_intermedio or os.path.splitext(self.salida)[0] + ".md"
        carpeta = os.path.dirname(md_path)
        if carpeta:
            os.makedirs(carpeta, exist_ok=True)
        with open(md_path, "w", encoding="utf-8") as fh:
            fh.write(md)
        self.ejecutar_pandoc(md_path)
        n_tablas, remapeos = self.postprocesar_docx()
        auditoria = self.auditar_docx()
        self.ruta_censo_docx = self.escribir_censo_docx(
            auditoria, n_tablas, remapeos)
        print("censo de estilos del .docx generado: " + self.ruta_censo_docx)
        print("docx generado: " + self.salida)
        print("markdown intermedio: " + md_path)
        print("commit: " + self.commit)
        print("tablas con estilo de cuadricula: %d" % n_tablas)
        print("pStyle inyectados por pandoc y remapeados: %s"
              % (remapeos or "ninguno"))
        print("imagenes embebidas en el .docx: %d" % auditoria["imagenes"])
        print("la plantilla trae TDC propia: %s"
              % ("si" if self.comprobar_tdc_plantilla() else "no"))
        self.informar(auditoria)
        print("procedencia: " + self.escribir_procedencia(auditoria, md_path))


def _consola_utf8():
    """Evita UnicodeEncodeError al imprimir el informe en consolas cp1252.

    Los titulos de callout y las notas llevan tildes, comillas tipograficas y
    el signo menos U+2212. En Windows la consola arranca en cp1252 y el
    informe reventaba DESPUES de generar el .docx, dejando la impresion de
    que el volcado habia fallado cuando no lo habia hecho.
    """
    for flujo in (sys.stdout, sys.stderr):
        try:
            flujo.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass


def main(argv=None):
    _consola_utf8()
    parser = argparse.ArgumentParser(
        description="Volcado de las notas del vault a un unico .docx. "
                    "El volcado es destructivo respecto al trabajo manual en "
                    "Word: re-ejecutar revive lo borrado.")
    parser.add_argument("--capitulos", default=None,
                        help="claves separadas por comas: '3', '1,2,3' o "
                             "'Apendices'. Si se omite, memoria completa.")
    parser.add_argument("--salida", default=None,
                        help="ruta del .docx de salida. Obligatoriamente bajo "
                             "Resultados/docx/. Por defecto, nombre versionado.")
    parser.add_argument("--sobrescribir", action="store_true",
                        help="permite pisar un .docx de salida ya existente")
    parser.add_argument("--numerar-apendice-n3", action="store_true",
                        help="quita el numero a mano en los apartados A.x.y "
                             "(por defecto se conserva: el estilo 'Titulo 3 de "
                             "Apendice' hereda la numeracion del cuerpo)")
    parser.add_argument("--pandoc", default=None, help="ruta al ejecutable pandoc")
    parser.add_argument("--plantilla", default=None, help="ruta al .docx plantilla")
    parser.add_argument("--md-intermedio", default=None,
                        help="ruta del Markdown unico intermedio. Igual que la "
                             "salida, obligatoriamente bajo Resultados/docx/: "
                             "el volcado no escribe dentro del vault.")
    args = parser.parse_args(argv)
    capitulos = None
    if args.capitulos:
        capitulos = [c.strip() for c in args.capitulos.split(",") if c.strip()]
    exportador = ExportadorDocx(
        capitulos=capitulos, salida=args.salida, pandoc=args.pandoc,
        plantilla=args.plantilla, sobrescribir=args.sobrescribir,
        conservar_numeros_apendice=not args.numerar_apendice_n3)
    exportador.ejecutar(md_intermedio=args.md_intermedio)
    return 0


if __name__ == "__main__":
    sys.exit(main())
