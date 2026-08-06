# Pipeline de Implementación — H-NIDS NSL-KDD

> Los diagramas Mermaid viven como ficheros sueltos en [`diagramas/`](diagramas/) (fuente `.mmd` + PNG/SVG renderizados).
> Ver [`diagramas/README.md`](diagramas/README.md) para cómo editarlos/exportarlos.

## Diagrama completo del pipeline

![Pipeline completo](diagramas/01_pipeline_completo.svg)

> Fuente editable: [`diagramas/01_pipeline_completo.mmd`](diagramas/01_pipeline_completo.mmd)

---

## Mapeo de ataques (39 tipos de ataque → 5 categorías)

![Mapeo de ataques a 5 categorías](diagramas/02_mapeo_ataques.svg)

> Fuente editable: [`diagramas/02_mapeo_ataques.mmd`](diagramas/02_mapeo_ataques.mmd)

---

## Estructura de archivos generados

```
Resultados/
└── specialized_nsl_kdd_
    ├── original_D1_normal_for_anomaly.csv
    ├── original_D2_complete_test.csv
    ├── original_D3_known_attacks_for_signatures.csv
    │
    ├── processed_X_D1_normal_for_anomaly.csv          ← features D1 (escaladas)
    ├── processed_y_attack_D1_normal_for_anomaly.csv
    ├── processed_y_category_D1_normal_for_anomaly.csv
    │
    ├── processed_X_D2_complete_test.csv               ← features D2 (escaladas)
    ├── processed_y_attack_D2_complete_test.csv
    ├── processed_y_category_D2_complete_test.csv
    │
    ├── processed_X_D3_known_attacks_for_signatures.csv ← features D3 (escaladas)
    ├── processed_y_attack_D3_known_attacks_for_signatures.csv
    ├── processed_y_category_D3_known_attacks_for_signatures.csv
    │
    ├── mappings_and_info.txt                           ← mapeos LabelEncoder + scaler
    ├── usage_guide.txt                                 ← guía de uso con ejemplos
    └── validation_report.txt                          ← generado por validacion.py
```

---

## Runbook de reconstrucción de las tablas de métricas (esquema T1)

El esquema de las tablas de métricas cambió con la tarea **T1** (columnas `alcance`,
`semilla`, `commit`, `bin_accuracy`, tiempos separados de entrenamiento/inferencia). Un CSV
con el esquema anterior **no se mezcla**: `evaluacion.limpiar_variante_csv()` lo aparta como
`<nombre>.esquema-anterior.bak` y lo regenera. Para volver a tener las tablas completas hacen
falta **estas ocho invocaciones**, desde `Implementacion/app/` y con el venv `Imp` activado.

`hibrido.py` va **al final de cada variante**: consume los `.joblib` que dejan `anomalias.py` y
`firmas.py`, y aborta si no encuentra los de su variante.

```powershell
# --- Variante de 54 características (selección 4.3.5 aplicada, por defecto) ---
python anomalias.py
python firmas.py
python baseline.py
python hibrido.py

# --- Variante de 122 características (sin selección) ---
python anomalias.py --sin-seleccion
python firmas.py    --sin-seleccion
python baseline.py  --sin-seleccion
python hibrido.py   --sin-seleccion
```

Ningún número cambia respecto a lo publicado: la semilla es 42 en todo y T1 solo añade
columnas.

### Recuento esperado (comprobado por código, no a ojo)

| Tabla | Filas por variante | Total con las dos variantes |
|---|---|---|
| `metricas_anomalias.csv` | 4 (un detector por fila) | **8** |
| `metricas_firmas.csv` | 4 (un clasificador por fila) | **8** |
| `metricas_baseline.csv` | 1 (RF monolítico) | **2** |
| `metricas_hibrido.csv` | 1 (la cascada) | **2** |

Lo verifica `evaluacion.comprobar_recuento()` al final de cada corrida (contra
`evaluacion.FILAS_ESPERADAS_POR_VARIANTE`): si la variante que se acaba de correr no tiene
exactamente esas filas, **aborta**. Junto a ella, `evaluacion.comprobar_unicidad()` verifica la
clave `set_features × algoritmo × alcance`. Las cuatro tablas auxiliares
(`metricas_balanceo.csv`, `metricas_baseline_0day.csv`, `metricas_hibrido_0day.csv`,
`metricas_hibrido_calibracion.csv`) tienen otra granularidad de fila y no llevan recuento fijo,
pero sí `alcance` y procedencia (`evaluacion.COLUMNAS_MINIMAS_AUXILIARES`).

> Al terminar las ocho, si quedan ficheros `*.esquema-anterior.bak` en `Resultados/`, es que
> había tablas del esquema viejo: comprobar que la nueva trae todas las filas y borrarlos a mano.
> Un `.bak` no se versiona ni se cita.

### La columna `commit`: tres valores posibles

| Valor | Significado |
|---|---|
| `<hash>` | El código (`Implementacion/`) no tenía cambios sin commitear al correr. |
| `<hash>-sucio` | Había cambios sin commitear **en `Implementacion/`**. La fila no es reproducible desde ese hash tal cual. |
| `<hash>-suciedad_desconocida` | El hash es válido, pero el `git status` falló o agotó su timeout: no se pudo determinar si el código estaba limpio. |

El `-sucio` mira **solo `Implementacion/`**, no todo el árbol (`config._RUTA_SUCIEDAD`): los
propios scripts escriben figuras y CSV en `Resultados/`, que está versionado, así que un
`git status` completo daría `-sucio` siempre y la columna no discriminaría nada. Si git no está
disponible o el directorio no es un repositorio, el valor es `desconocido` (sin hash).

### Límite declarado: las cuatro tablas principales son de pase único (semilla 42)

Las cuatro tablas principales contienen **un solo pase, con la semilla 42**. La dispersión entre
semillas (tarea **T4**, 10 semillas) **no entra en ellas**: va a **tabla propia**, con clave de
unicidad que incluya `semilla`. Queda escrito aquí porque hoy T4 chocaría contra tres muros a la
vez y se descubriría en ejecución, no antes:

1. `evaluacion.limpiar_variante_csv()` borra por **variante**, no por clave: 10 semillas de la
   misma variante colapsarían a la última escrita.
2. `evaluacion.CLAVE_UNICIDAD` (`set_features × algoritmo × alcance`) **no incluye `semilla`**:
   dos semillas de la misma variante son un duplicado y `comprobar_unicidad()` **aborta**.
3. `evaluacion.FILAS_ESPERADAS_POR_VARIANTE` es fijo 4/4/1/1: 40 filas hacen **abortar** a
   `comprobar_recuento()`.

Los tres aborts **se conservan**: ninguna invocación legítima de la CLI actual los dispara y son
lo que hace comprobable el recuento del runbook. La dispersión de T4 entra como tabla nueva
en el anexo `A.3`.

---

## Decisión de diseño clave: ajuste del scaler

| Enfoque | Scaler ajustado en | Ventaja | Desventaja |
|---|---|---|---|
| ~~Anterior~~ | Solo D1 (normal) | Anomalías se "desbordan" del rango → más detectables | D3 mal escalado → firmas sesgadas |
| **Actual** | D1 + D3 (todo el train) | Escalado correcto para ambos modelos | Ninguna significativa |

El scaler se ajusta en `concat(D1, D3)` y se aplica igual a D2 (test), garantizando que ninguna división tenga ventaja artificial en el rango de valores.
