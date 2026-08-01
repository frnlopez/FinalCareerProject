# H-NIDS con Machine Learning — TFG

Sistema **Híbrido de Detección de Intrusiones en Red** que combina detección por **anomalías**
(no supervisada) y detección por **firmas** (supervisada) en cascada, evaluado sobre el dataset
**NSL-KDD**.

La hipótesis del trabajo es el **ataque de día cero**: un clasificador supervisado monolítico
solo puede predecir clases que vio durante el entrenamiento, mientras que la etapa de anomalías
puede señalar como sospechoso un tipo de ataque que nunca ha visto. El repositorio incluye un
baseline de control precisamente para medir esa diferencia.

---

## Estructura

```
Working_Directory/
├── Implementacion/            Código Python del pipeline y los modelos
│   ├── app/                   Los 8 scripts (ver tabla)
│   ├── diagramas/             Diagramas Mermaid del pipeline (.mmd + .png/.svg)
│   ├── PIPELINE.md            Documentación del flujo de preprocesamiento
│   └── requirements.txt       Dependencias con versión fijada
├── Obsidian_TFG_Vault/        La memoria del TFG en Markdown (vault de Obsidian)
├── Resultados/                Métricas, figuras y reglas extraídas
├── Guia_ML/                   Notas de referencia de ML usadas durante el desarrollo
├── features.md                Registro vivo: tareas abiertas y cerradas
├── next-steps.md              Congelado. §1-§5 historial · §6 = especificación de cada
│                              script, salvo §6.5 (ver grill H-1…H-7 en decisiones)
├── resumen-de-decisiones.md   Registro de decisiones de diseño
├── EL_FUTURO.md               Líneas futuras respaldadas con datos
└── .claude/                   Arquitectura de agentes (ver más abajo)
```

---

## Entorno

Python **3.11**. Solo scikit-learn e imbalanced-learn: **no se usa TensorFlow ni Keras** — el
autoencoder está implementado como `MLPRegressor`.

```powershell
"C:\Python311\python.exe" -m venv Imp
.\Imp\Scripts\Activate.ps1
pip install -r Implementacion\requirements.txt
```

El dataset **no está en el repositorio**. Descarga `KDDTrain+.txt` y `KDDTest+.txt` de
[Jehuty4949/NSL_KDD](https://github.com/Jehuty4949/NSL_KDD) y colócalos en
`Working_Directory/Archivos dataset/`.

---

## Los scripts

Se ejecutan en este orden. Todos aceptan `--sin-seleccion` para trabajar con las **122**
características del one-hot en lugar de las **54** seleccionadas, que es lo predeterminado.

| # | Script | Qué hace |
|---|---|---|
| 1 | `program.py` | Carga NSL-KDD, análisis exploratorio, one-hot de `protocol_type`/`service`/`flag`, escalado, codificación de etiquetas, balanceo y selección de características. Genera los splits **D1/D2/D3** y sus metadatos |
| 2 | `validacion.py` | Valida lo generado: integridad y alineación de columnas, pureza de D1 y D3, distribuciones, correlaciones, drift KS de D1→D2 y outliers. Emite un informe con veredicto **APROBADA / FALLA** |
| 3 | `anomalias.py` | **Etapa 1.** Compara cuatro detectores no supervisados entrenados solo con tráfico normal: IsolationForest, OneClassSVM, LocalOutlierFactor (`novelty=True`) y un autoencoder `MLPRegressor`. Score unificado (mayor = más anómalo) y umbral en el percentil 95 |
| 4 | `firmas.py` | **Etapa 2.** Clasificador multiclase de ataques conocidos sobre D3 (dos/probe/r2l/u2r). Compara DecisionTree, RandomForest, KNN e HistGradientBoosting con `GridSearchCV` y `f1_macro`, e incluye el experimento de balanceo SMOTE frente a `class_weight` |
| 5 | `baseline.py` | **Control.** Un único RandomForest monolítico de 5 clases sobre todo el train. No forma parte del híbrido: existe para contrastar su recall de día cero con el de la cascada |
| 6 | `hibrido.py` | **El sistema.** Encadena las dos etapas ya entrenadas y las evalúa de extremo a extremo sobre D2. No reentrena: carga los `.joblib`. Lo sospechoso pasa a firmas; si la confianza máxima queda por debajo del umbral, se etiqueta `unknown` (posible 0-day) |
| — | `config.py` | Configuración central: rutas, semilla y convenciones de clase, compartidas por los scripts de modelos |
| — | `evaluacion.py` | Módulo común de métricas y figuras: evaluación binaria, multiclase y de 0-day por tipo, matrices de confusión y curvas ROC/PR |

```powershell
cd Implementacion
python app\program.py            # y después validacion, anomalias, firmas, baseline, hibrido
python app\program.py --sin-seleccion
```

### Los tres splits

| Split | Contenido | Uso |
|---|---|---|
| **D1** | Solo tráfico normal del train | Entrenar la etapa de anomalías |
| **D2** | Set de test completo | Evaluación final. **Intocable** para ajustar nada |
| **D3** | Solo ataques conocidos del train | Entrenar la etapa de firmas |

---

## Reglas de protocolo

No son estilo: romperlas invalida los resultados.

- **D2 nunca se usa** para elegir hiperparámetros, umbrales, escalado, selección de
  características ni balanceo. Solo para reportar.
- El **umbral de anomalías** sale del percentil 95 sobre el 20 % de validación de D1, que es
  solo tráfico normal.
- **SMOTE se aplica dentro de cada fold** de la validación cruzada (vía `ImbPipeline`), nunca
  antes del split.
- **`random_state=42`** en absolutamente todo: splits, modelos y submuestreos.
- Los cuatro algoritmos de cada etapa se comparan bajo el **mismo split, la misma semilla y las
  mismas métricas**.

---

## Qué no está en el repositorio

Se versiona el texto plano; queda fuera el binario pesado que se puede reproducir. Sin estas
exclusiones el repositorio pesaría 1,1 GB y GitHub rechazaría el envío.

| Excluido | Peso | Cómo se recupera |
|---|---|---|
| `Implementacion/Imp/` | 423 MB | `python -m venv` + `requirements.txt` |
| `Resultados/modelos/*.joblib` | 482 MB | Reejecutando los scripts 3, 4 y 5 |
| Splits procesados (`*_processed_*.csv`) | ~170 MB | Reejecutando `program.py` |
| `Archivos dataset/` | 22 MB | Descarga desde el repositorio de NSL-KDD |
| `*.doc`, `*.docx` | 10 MB | Volcado final de la memoria; la fuente es el vault |

Sí están versionados los `metricas_*.csv`, las figuras y las reglas extraídas: son los
**resultados citados en la memoria** y deben quedar congelados junto al código que los produjo.

---

## Arquitectura de agentes

El repositorio incluye un andamiaje de agentes para Claude Code en `.claude/`. Cada mensaje pasa
por un hook de entrada que lo enruta al agente `leader`, que lo clasifica en un **carril**
(Consulta · Intervención · Tarea · Investigación) y un **track** (Código · Informe) y despacha.

| Agente | Rol |
|---|---|
| `leader` | Orquestador. Clasifica y despacha. No escribe nada |
| `ml-implementador` | Escribe el código Python |
| `ejecutor-experimentos` | Ejecuta los scripts y reporta las métricas |
| `auditor-ml` | Revisión adversaria. Obligatoria antes de cerrar cualquier cambio de código |
| `redactor-tfg` | Redacta las notas de la memoria en el vault |
| `researcher` | Investiga fuera del repositorio y verifica la fiabilidad de las fuentes citadas. Único que edita `Bibliografía.md` |
| `cronista` | Mantiene `features.md` |

Ningún agente ejecuta `git` de escritura: el commit lo hace el skill `cierre`, en hilo
principal y preguntando siempre.

---

## Ramas

Se trabaja en **`develop`**. `main` se actualiza solo en hitos: cierre de capítulo, entrega,
defensa.
