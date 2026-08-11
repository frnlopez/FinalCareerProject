import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import argparse
import warnings
import os
import sys
import joblib

# program.py es la FUENTE CANÓNICA de las columnas categóricas y de las que no
# son características: se importan, no se copian (antes estaban duplicadas por
# copia y un cambio allí rompía en silencio medir_vocabulario_onehot()).
# Esto NO introduce dependencia de config.py ni de evaluacion.py: validacion.py
# sigue sin importarlas, y program.py tampoco. No hay import circular
# (program.py no importa validacion.py) ni efectos al importar: todo su código
# ejecutable vive bajo `if __name__ == "__main__"`.
import program

warnings.filterwarnings('ignore')

# Forzar salida UTF-8 en consolas Windows: sin esto, los prints con emojis
# cascan con el códec cp1252 salvo que exista PYTHONIOENCODING=utf-8.
if sys.stdout.encoding and sys.stdout.encoding.lower().replace('-', '') != 'utf8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except (AttributeError, ValueError):
        # stdout no reconfigurable (p. ej. redirigido a un objeto sin reconfigure):
        # se continúa sin forzar el encoding
        pass

plt.style.use('default')
sns.set_palette("husl")
plt.rcParams['figure.figsize'] = (12, 8)


class NSLKDDValidator:
    """
    Valida las divisiones D1/D2/D3 generadas por NSLKDDPreprocessor (program.py).

    Espera los archivos con el prefijo devuelto por save_specialized_splits(), p.ej.:
        <base_path>_processed_X_D1_normal_for_anomaly.csv
        <base_path>_processed_X_D2_complete_test.csv
        <base_path>_processed_X_D3_known_attacks_for_signatures.csv
        ... (y sus correspondientes y_attack / y_category)
    """

    def __init__(self, base_path=r'C:\Users\francisco.lopez\KIKO_TFG\Working_Directory\Resultados\specialized_nsl_kdd'):
        self.base_path = base_path

        # Directorio de figuras: Resultados\figuras (mismo patrón que program.py).
        # Las figuras se guardan a disco en lugar de mostrarse (no bloquean la
        # ejecución y quedan listas para la memoria del TFG).
        self.figures_dir = os.path.join(os.path.dirname(base_path) or '.', 'figuras')

        # Sufijo de variante (H3): si se valida la variante sin selección
        # (base_path acabado en '_sin_seleccion'), las figuras llevan el mismo
        # sufijo para no pisar las de la variante por defecto.
        self.variant_suffix = ('_sin_seleccion'
                               if os.path.basename(base_path).endswith('_sin_seleccion')
                               else '')

        # D1: solo tráfico normal (entrenamiento anomalías)
        self.D1_X = None
        self.D1_y_category_original = None

        # D2: set de test completo (evaluación)
        self.D2_X = None
        self.D2_y_attack_original = None
        self.D2_y_category_original = None

        # Subconjunto NORMAL de D2 (tarea T2). D2 es 43 % normal + 57 % ataques, así
        # que el KS de D1 contra D2 COMPLETO mezcla dos cosas: el desplazamiento
        # entre particiones del tráfico legítimo y la simple presencia de ataques.
        # Para explicar el FPR hace falta el primero solo, y ese es este subconjunto.
        # NO sustituye a nada: los dos KS se calculan y se reportan por separado.
        self.D2_X_normal = None

        # D3: ataques conocidos (entrenamiento firmas)
        self.D3_X = None
        self.D3_y_attack_original = None
        self.D3_y_category_original = None

        self.feature_names = None

        # Tipos de ataque presentes en D2 y ausentes del entrenamiento (los
        # "0-day" del experimento). Se calculan en analyze_class_distribution()
        # SIEMPRE desde los datos —nunca desde una lista escrita a mano— y se
        # persisten en el informe (deuda menor de next-steps.md:277: hasta ahora
        # solo salían por consola).
        self.zero_day_df = None

    # Columnas categóricas del NSL-KDD y columnas que no son características.
    # NO se declaran aquí: se toman de program.py, que es quien realmente hace
    # el one-hot (las usa en 'self.categorical_columns' y en el descarte previo
    # a get_dummies). Así medir_vocabulario_onehot() reproduce por construcción
    # el one-hot real y no puede desincronizarse en silencio.
    COLUMNAS_CATEGORICAS = program.COLUMNAS_CATEGORICAS
    COLUMNAS_NO_CARACTERISTICA = program.COLUMNAS_NO_CARACTERISTICA

    # ─────────────────────────────────────────────────────────────────────────
    # Utilidades
    # ─────────────────────────────────────────────────────────────────────────

    def _save_figure(self, filename):
        """
        Guarda la figura matplotlib actual en Resultados/figuras y la cierra.
        Sustituye a plt.show() para que la validación no bloquee la ejecución.
        """
        os.makedirs(self.figures_dir, exist_ok=True)
        if self.variant_suffix:
            raiz, ext = os.path.splitext(filename)
            filename = f"{raiz}{self.variant_suffix}{ext}"
        figure_path = os.path.join(self.figures_dir, filename)
        plt.savefig(figure_path, dpi=300, bbox_inches='tight')
        plt.close()
        print(f"   ✓ Figura guardada en: {figure_path}")

    # ─────────────────────────────────────────────────────────────────────────
    # Carga de datos
    # ─────────────────────────────────────────────────────────────────────────

    def load_all_data(self):
        """Carga las tres divisiones procesadas generadas por program.py."""
        print("🔄 CARGANDO DIVISIONES D1 / D2 / D3...")
        print("=" * 60)
        try:
            bp = self.base_path

            # D1
            self.D1_X = pd.read_csv(f'{bp}_processed_X_D1_normal_for_anomaly.csv')
            D1_y_cat = pd.read_csv(f'{bp}_processed_y_category_D1_normal_for_anomaly.csv')
            self.D1_y_category_original = D1_y_cat['category_original'].values

            # D2
            self.D2_X = pd.read_csv(f'{bp}_processed_X_D2_complete_test.csv')
            D2_y_att = pd.read_csv(f'{bp}_processed_y_attack_D2_complete_test.csv')
            D2_y_cat = pd.read_csv(f'{bp}_processed_y_category_D2_complete_test.csv')
            self.D2_y_attack_original = D2_y_att['attack_original'].values
            self.D2_y_category_original = D2_y_cat['category_original'].values

            # D3
            self.D3_X = pd.read_csv(f'{bp}_processed_X_D3_known_attacks_for_signatures.csv')
            D3_y_att = pd.read_csv(f'{bp}_processed_y_attack_D3_known_attacks_for_signatures.csv')
            D3_y_cat = pd.read_csv(f'{bp}_processed_y_category_D3_known_attacks_for_signatures.csv')
            self.D3_y_attack_original = D3_y_att['attack_original'].values
            self.D3_y_category_original = D3_y_cat['category_original'].values

            self.feature_names = self.D1_X.columns.tolist()

            # Subconjunto NORMAL de D2 (T2): mismo tipo de tráfico que D1, otra
            # partición. Es el término de comparación que deja FUERA los ataques,
            # así que el KS calculado contra él mide el desplazamiento del propio
            # tráfico legítimo. No es un reparto de causas del KS contra D2
            # completo: son dos mediciones sobre dos poblaciones (ver el bloque de
            # cabecera de la sección 4).
            self.D2_X_normal = self.D2_X[self.D2_y_category_original == 'normal']

            print(f"   ✓ D1 (Normal):   {self.D1_X.shape[0]:>7,} × {self.D1_X.shape[1]}")
            print(f"   ✓ D2 (Test):     {self.D2_X.shape[0]:>7,} × {self.D2_X.shape[1]}")
            print(f"   ✓ D2 (solo normales de D2): {self.D2_X_normal.shape[0]:>7,} filas "
                  f"({self.D2_X_normal.shape[0] / self.D2_X.shape[0] * 100:.1f} % de D2)")
            print(f"   ✓ D3 (Ataques):  {self.D3_X.shape[0]:>7,} × {self.D3_X.shape[1]}")
            print(f"\n✅ {len(self.feature_names)} características cargadas correctamente")
            return True

        except FileNotFoundError as e:
            print(f"❌ Archivo no encontrado: {e}")
            print("   Ejecuta program.py primero para generar las divisiones procesadas.")
            return False
        except Exception as e:
            print(f"❌ Error al cargar datos: {e}")
            return False

    # ─────────────────────────────────────────────────────────────────────────
    # 1. Integridad
    # ─────────────────────────────────────────────────────────────────────────

    def validate_data_integrity(self):
        """
        Comprueba:
          - Dimensiones X/y consistentes en D2 y D3
          - Columnas alineadas entre D1, D2 y D3
          - Ausencia de nulos e infinitos
          - Pureza de D1 (solo 'normal') y D3 (sin 'normal')
          - Rangos de escalado razonables
        """
        print("\n🔍 VALIDACIÓN DE INTEGRIDAD")
        print("=" * 60)
        issues = []

        # 1. Dimensiones
        print("1. Dimensiones X / y:")
        for name, X, y in [
            ('D2', self.D2_X, self.D2_y_category_original),
            ('D3', self.D3_X, self.D3_y_category_original),
        ]:
            if len(X) != len(y):
                issues.append(f"{name}: X({len(X)}) ≠ y({len(y)})")
                print(f"   ❌ {name}: X({len(X):,}) ≠ y({len(y):,})")
            else:
                print(f"   ✓ {name}: {len(X):,} muestras consistentes")

        # 2. Alineación de columnas — POR ORDEN, no por conjunto
        # Deuda menor de next-steps.md:279: la comparación anterior era de
        # conjuntos, así que daba por buenas tres matrices con las mismas
        # columnas PERMUTADAS. Eso no es inocuo: los modelos consumen los CSV
        # como arrays posicionales (sklearn ignora los nombres), de modo que una
        # permutación entre D1/D2/D3 pasaría el chequeo y envenenaría la
        # inferencia en silencio. Se compara la lista ordenada y, cuando el
        # conjunto coincide pero el orden no, se dice exactamente eso.
        print("\n2. Alineación de columnas entre divisiones (conjunto Y orden):")
        cols_d1 = list(self.D1_X.columns)
        cols_d2 = list(self.D2_X.columns)
        cols_d3 = list(self.D3_X.columns)
        if cols_d1 == cols_d2 == cols_d3:
            print(f"   ✓ {len(self.feature_names)} columnas alineadas en D1 / D2 / D3 "
                  f"(mismo conjunto y mismo orden)")
        else:
            for nombre, cols in [('D2', cols_d2), ('D3', cols_d3)]:
                if cols == cols_d1:
                    continue
                diferencia = set(cols_d1).symmetric_difference(set(cols))
                if diferencia:
                    issues.append(f"Columnas D1 ≠ {nombre}: {diferencia}")
                    print(f"   ❌ Diferencias D1 ↔ {nombre}: {diferencia}")
                else:
                    # Mismo conjunto, distinto orden: justo lo que la comparación
                    # por conjunto ocultaba.
                    desordenadas = [(i, a, b) for i, (a, b) in enumerate(zip(cols_d1, cols))
                                    if a != b]
                    issues.append(f"Columnas D1 y {nombre}: mismo conjunto pero distinto "
                                  f"ORDEN ({len(desordenadas)} posiciones)")
                    print(f"   ❌ D1 y {nombre} tienen las mismas columnas en distinto ORDEN "
                          f"({len(desordenadas)} posiciones). Primeras 5:")
                    for i, a, b in desordenadas[:5]:
                        print(f"      posición {i}: D1='{a}'  {nombre}='{b}'")

        # 2b. Consistencia con los transformadores persistidos: las columnas de
        # los CSVs deben coincidir con 'feature_columns' del transformers.joblib
        # (tras la selección de características 4.3.5, esa clave contiene la
        # lista FINAL de features; no se asume ningún número fijo de columnas).
        transformers_path = f'{self.base_path}_transformers.joblib'
        if os.path.exists(transformers_path):
            try:
                transformers = joblib.load(transformers_path)
                expected_cols = transformers.get('feature_columns')
                if expected_cols is None:
                    print("   ℹ️  transformers.joblib sin clave 'feature_columns' — chequeo omitido")
                elif list(self.D1_X.columns) == list(expected_cols):
                    print(f"   ✓ Columnas de los CSVs coinciden con transformers.joblib ({len(expected_cols)} features)")
                else:
                    issues.append("Columnas de los CSVs ≠ 'feature_columns' de transformers.joblib")
                    print(f"   ❌ Columnas de los CSVs ({len(self.D1_X.columns)}) ≠ "
                          f"'feature_columns' de transformers.joblib ({len(expected_cols)})")
            except Exception as e:
                print(f"   ℹ️  No se pudo leer transformers.joblib ({e}) — chequeo omitido")
        else:
            print("   ℹ️  transformers.joblib no encontrado — chequeo de consistencia omitido")

        # 3. Nulos e infinitos
        print("\n3. Nulos e infinitos:")
        for name, X in [('D1', self.D1_X), ('D2', self.D2_X), ('D3', self.D3_X)]:
            nulls = X.isnull().sum().sum()
            infs = np.isinf(X.select_dtypes(include=[np.number])).sum().sum()
            if nulls > 0 or infs > 0:
                issues.append(f"{name}: {nulls} nulos, {infs} infinitos")
                print(f"   ❌ {name}: {nulls} nulos, {infs} infinitos")
            else:
                print(f"   ✓ {name}: sin nulos ni infinitos")

        # 4. Pureza de D1 (solo tráfico normal)
        print("\n4. Pureza de D1 (debe ser 100 % normal):")
        n_non_normal_d1 = np.sum(self.D1_y_category_original != 'normal')
        if n_non_normal_d1 > 0:
            issues.append(f"D1 contiene {n_non_normal_d1} instancias no-normales")
            print(f"   ❌ D1 contiene {n_non_normal_d1} instancias no-normales")
        else:
            print(f"   ✓ D1 = 100 % normal ({len(self.D1_X):,} instancias)")

        # 5. Pureza de D3 (solo ataques, sin normal)
        print("\n5. Pureza de D3 (debe ser 100 % ataques):")
        n_normal_d3 = np.sum(self.D3_y_category_original == 'normal')
        if n_normal_d3 > 0:
            issues.append(f"D3 contiene {n_normal_d3} instancias normales")
            print(f"   ❌ D3 contiene {n_normal_d3} instancias normales")
        else:
            print(f"   ✓ D3 = 100 % ataques ({len(self.D3_X):,} instancias)")

        # 6. Rangos de escalado
        print("\n6. Rangos de escalado:")
        for name, X in [('D1', self.D1_X), ('D2', self.D2_X), ('D3', self.D3_X)]:
            x_min = X.min().min()
            x_max = X.max().max()
            print(f"   {name}: [{x_min:.4f}, {x_max:.4f}]")

        # Resumen
        print("\n" + "=" * 60)
        if not issues:
            print("🎉 INTEGRIDAD APROBADA — sin problemas detectados")
        else:
            print(f"⚠️  {len(issues)} problema(s) encontrado(s):")
            for issue in issues:
                print(f"   ❌ {issue}")

        return len(issues) == 0, issues

    # ─────────────────────────────────────────────────────────────────────────
    # 2. Distribución de clases
    # ─────────────────────────────────────────────────────────────────────────

    def analyze_class_distribution(self):
        """
        Analiza la distribución de categorías de ataque en D2 y D3,
        y detecta ataques presentes en el test (D2) pero no vistos en entrenamiento (D3).
        """
        print("\n📊 ANÁLISIS DE DISTRIBUCIÓN DE CLASES")
        print("=" * 60)

        d2_cat = pd.Series(self.D2_y_category_original).value_counts()
        d3_cat = pd.Series(self.D3_y_category_original).value_counts()
        d3_att = pd.Series(self.D3_y_attack_original)
        d2_att = pd.Series(self.D2_y_attack_original)

        print("\n1. D2 — Set de Test Completo (categorías):")
        for cat, count in d2_cat.items():
            pct = count / len(self.D2_y_category_original) * 100
            print(f"   {cat.upper():<12}: {count:>6,}  ({pct:.2f}%)")

        print("\n2. D3 — Ataques Conocidos (categorías):")
        for cat, count in d3_cat.items():
            pct = count / len(self.D3_y_category_original) * 100
            print(f"   {cat.upper():<12}: {count:>6,}  ({pct:.2f}%)")

        d3_min = d3_cat.min()
        d3_max = d3_cat.max()
        ratio = d3_max / d3_min if d3_min > 0 else float('inf')
        print(f"\n   Ratio de desbalance en D3: {ratio:.1f}:1")
        if ratio > 100:
            print("   ⚠️  Alto desbalance — considera class_weight='balanced' en el modelo de firmas")

        # Ataques nuevos en D2 no vistos en D3 = los "0-day" del experimento.
        # Se derivan SIEMPRE de los datos (diferencia de conjuntos entre las
        # etiquetas de D2 y las de D3); no hay ninguna lista literal escrita a
        # mano ni ningún recuento fijado a priori. El resultado se guarda en
        # self.zero_day_df para que _save_report() lo persista en el informe
        # (next-steps.md:277: hasta ahora solo salía por consola).
        new_in_test = sorted(set(d2_att.unique()) - {'normal'} - set(d3_att.unique()))
        d2_cat_series = pd.Series(self.D2_y_category_original)
        filas = []
        for a in new_in_test:
            mascara = (d2_att == a).values
            categorias = d2_cat_series[mascara].unique().tolist()
            filas.append({
                'tipo': a,
                'categoria': '/'.join(sorted(categorias)),
                'instancias_en_D2': int(mascara.sum()),
            })
        self.zero_day_df = pd.DataFrame(
            filas, columns=['tipo', 'categoria', 'instancias_en_D2']
        )
        if not self.zero_day_df.empty:
            self.zero_day_df = self.zero_day_df.sort_values(
                'instancias_en_D2', ascending=False
            ).reset_index(drop=True)

        if new_in_test:
            n_inst = int(self.zero_day_df['instancias_en_D2'].sum())
            print(f"\n   ⚠️  {len(new_in_test)} tipo(s) de ataque NUEVOS en D2 (no vistos en D3) "
                  f"— {n_inst:,} instancias "
                  f"({n_inst / len(self.D2_y_attack_original) * 100:.2f} % de D2):")
            for _, fila in self.zero_day_df.iterrows():
                print(f"      → {fila['tipo']:<20} [{fila['categoria']}]  "
                      f"{fila['instancias_en_D2']:>5,} instancias en D2  "
                      f"(solo detectable por el modelo de anomalías)")
        else:
            print("\n   ✓ Todos los ataques de D2 están representados en D3")

        self._plot_class_distributions(d2_cat, d3_cat)
        return d2_cat, d3_cat

    def _plot_class_distributions(self, d2_counts, d3_counts):
        fig, axes = plt.subplots(1, 3, figsize=(18, 6))

        axes[0].bar(['normal'], [len(self.D1_X)], color='lightgreen', alpha=0.85, edgecolor='darkgreen')
        axes[0].set_title('D1 — Tráfico Normal\n(Entrenamiento Anomalías)')
        axes[0].set_ylabel('Instancias')

        colors_d2 = ['lightgreen' if c == 'normal' else 'lightcoral' for c in d2_counts.index]
        axes[1].bar(d2_counts.index, d2_counts.values, color=colors_d2, alpha=0.85, edgecolor='grey')
        axes[1].set_title('D2 — Test Completo\n(Evaluación H-NIDS)')
        axes[1].set_ylabel('Instancias')
        axes[1].tick_params(axis='x', rotation=30)

        axes[2].bar(d3_counts.index, d3_counts.values, color='lightcoral', alpha=0.85, edgecolor='grey')
        axes[2].set_title('D3 — Ataques Conocidos\n(Entrenamiento Firmas)')
        axes[2].set_ylabel('Instancias')
        axes[2].tick_params(axis='x', rotation=30)

        plt.tight_layout()
        self._save_figure('validacion_distribucion_clases.png')

    # ─────────────────────────────────────────────────────────────────────────
    # 3. Distribuciones de características
    # ─────────────────────────────────────────────────────────────────────────

    def analyze_feature_distributions(self):
        """
        Detecta características con varianza baja y alta correlación sobre el
        train completo (D1+D3) y compara distribuciones D1 (normal) vs D3
        (ataques) para identificar las más discriminantes para el modelo
        de firmas.
        """
        print("\n📈 ANÁLISIS DE DISTRIBUCIONES DE CARACTERÍSTICAS")
        print("=" * 60)

        # ⚠️ Varianza y correlación se calculan sobre el TRAIN COMPLETO (D1+D3),
        # NUNCA solo sobre D1: los dummies de service/flag exclusivos de tráfico
        # de ataque son todo-cero en D1 (solo normal) y aparecerían falsamente
        # como "varianza nula" (trampa documentada en next-steps.md §6.2).
        X_train_completo = pd.concat([self.D1_X, self.D3_X], axis=0)

        train_var = X_train_completo.var()
        low_var = train_var[train_var < 1e-8].index.tolist()
        if low_var:
            print(f"   ⚠️  {len(low_var)} características con varianza casi nula sobre D1+D3:")
            for f in low_var[:10]:
                print(f"      - {f}")
        else:
            print("   ✓ Todas las características tienen varianza suficiente sobre D1+D3")

        # Pares con alta correlación sobre D1+D3 (train completo)
        print("\n   Correlaciones altas (> 0.95) sobre D1+D3:")
        corr = X_train_completo.corr()
        high_corr = []
        for i in range(len(corr.columns)):
            for j in range(i + 1, len(corr.columns)):
                val = abs(corr.iloc[i, j])
                if val > 0.95:
                    high_corr.append((corr.columns[i], corr.columns[j], corr.iloc[i, j]))
        if high_corr:
            print(f"   ⚠️  {len(high_corr)} pares — top 5:")
            for f1, f2, v in sorted(high_corr, key=lambda x: abs(x[2]), reverse=True)[:5]:
                print(f"      {f1} ↔ {f2}: {v:.3f}")
        else:
            print("   ✓ Sin correlaciones extremas")

        # Características más discriminantes: mayor diferencia de medias D1 vs D3
        print("\n   Top 10 características más discriminantes (D1 Normal vs D3 Ataques):")
        mean_diff = (self.D3_X.mean() - self.D1_X.mean()).abs().sort_values(ascending=False)
        for feat, diff in mean_diff.head(10).items():
            mu_d1 = self.D1_X[feat].mean()
            mu_d3 = self.D3_X[feat].mean()
            print(f"      {feat:<40}  μ_D1={mu_d1:.3f}  μ_D3={mu_d3:.3f}  Δ={diff:.3f}")

        self._plot_feature_distributions(mean_diff)
        return {'low_variance': low_var, 'high_correlation': high_corr}

    def _plot_feature_distributions(self, mean_diff):
        top_feats = mean_diff.head(12).index.tolist()
        n_cols, n_rows = 4, 3
        fig, axes = plt.subplots(n_rows, n_cols, figsize=(20, 12))
        axes = axes.flatten()

        for i, feat in enumerate(top_feats):
            axes[i].hist(self.D1_X[feat], bins=40, alpha=0.6, label='D1 Normal', density=True, color='green')
            axes[i].hist(self.D3_X[feat], bins=40, alpha=0.6, label='D3 Ataques', density=True, color='red')
            axes[i].set_title(feat, fontsize=9)
            axes[i].legend(fontsize=7)

        for i in range(len(top_feats), len(axes)):
            axes[i].set_visible(False)

        plt.suptitle('D1 (Normal) vs D3 (Ataques) — Top características discriminantes', fontsize=12)
        plt.tight_layout()
        self._save_figure('validacion_discriminantes_d1_vs_d3.png')

    # ─────────────────────────────────────────────────────────────────────────
    # 4. Data drift D1 → D2 — DOS mediciones distintas, nunca intercambiables
    # ─────────────────────────────────────────────────────────────────────────
    # (A) detect_data_drift()           D1  vs  D2 COMPLETO  (normales + ataques)
    # (B) detect_data_drift_normales()  D1  vs  SOLO LAS FILAS NORMALES DE D2
    #
    # Por qué las dos y por qué separadas (tarea T2). (A) es la medición histórica
    # y se conserva intacta, pero NO sirve para explicar el FPR: D2 es 43 % normal
    # y 57 % ataques, así que buena parte de su drift es simplemente que en D2 hay
    # ataques y en D1 no. (B) compara tráfico legítimo contra tráfico legítimo, así
    # que lo que mide es el desplazamiento ENTRE PARTICIONES del propio tráfico
    # normal — que es lo que puede explicar por qué un umbral p95 ajustado sobre
    # D1_val (≈5 % de FPR prometido) rinde 8-10 % sobre D2.
    #
    # PRECISIÓN OBLIGATORIA AL CITARLO: es desplazamiento entre particiones, NO
    # deriva temporal. NSL-KDD no tiene marca de tiempo y la afirmación temporal no
    # se sostendría.
    #
    # SEGUNDA PRECISIÓN OBLIGATORIA — (A) y (B) NO SE RESTAN PARA REPARTIR CAUSAS.
    # El informe publica un `delta = (A) - (B)` y es una COMPARACIÓN de las dos
    # mediciones sobre las mismas características, nunca una descomposición: el
    # estadístico KS es un SUPREMO de diferencia entre funciones de distribución
    # acumulada y NO es aditivo sobre una mezcla de poblaciones. Con D2 = mezcla de
    # normales y ataques, KS(D1, D2) != KS(D1, D2_normales) + «aporte de los
    # ataques»: ese segundo sumando no existe como magnitud. Un delta grande dice
    # que la característica se comporta muy distinto bajo las dos poblaciones de
    # comparación, y hasta ahí llega. Escribirlo como atribución —«cuánto del drift
    # se debe a X y cuánto a Y»— es lo que este bloque prohíbe, porque de aquí sale
    # material para la redacción de 5.1/5.4.
    #
    # Las columnas de (B) llevan sufijo '_normales' y su figura y su sección del
    # informe llevan rótulo propio: las dos cifras NO deben poder confundirse.
    # ─────────────────────────────────────────────────────────────────────────

    def detect_data_drift(self):
        """
        (A) Compara distribuciones D1 (normal de entrenamiento) vs D2 COMPLETO
        (normales + ataques) usando el test de Kolmogorov-Smirnov.

        Drift alto indica que el test tiene perfiles muy distintos al baseline
        normal, lo que es esperable si contiene ataques — y precisamente por eso
        esta medición NO aísla el desplazamiento del tráfico legítimo: para eso
        está detect_data_drift_normales(), que es otra cifra y no la sustituye.
        """
        print("\n🌊 DETECCIÓN DE DRIFT (A) — D1 (Normal train) vs D2 COMPLETO "
              "(normales + ataques)")
        print("=" * 60)

        results = []
        for feat in self.feature_names:
            ks_stat, ks_p = stats.ks_2samp(
                self.D1_X[feat].values, self.D2_X[feat].values
            )
            results.append({
                'feature': feat,
                'ks_statistic': ks_stat,
                'ks_p_value': ks_p,
                'mean_d1': self.D1_X[feat].mean(),
                'mean_d2': self.D2_X[feat].mean(),
                'has_drift': ks_p < 0.01,
            })

        drift_df = pd.DataFrame(results)
        n_drift = drift_df['has_drift'].sum()
        total = len(drift_df)

        print(f"\n   Drift significativo (KS p < 0.01): {n_drift}/{total} características ({n_drift/total*100:.1f}%)")
        if n_drift > 0:
            print(f"\n   Top 10 por KS statistic:")
            top = drift_df.nlargest(10, 'ks_statistic')[['feature', 'ks_statistic', 'ks_p_value']]
            print(top.to_string(index=False, float_format='%.4f'))

        self._plot_drift(drift_df)
        return drift_df

    def detect_data_drift_normales(self):
        """
        (B) Compara D1 (todo normal) contra LAS FILAS NORMALES DE D2 con el mismo
        test de Kolmogorov-Smirnov y el mismo criterio (p < 0.01). Tarea T2.

        Es tráfico legítimo contra tráfico legítimo, así que el drift que sale aquí
        NO puede achacarse a la presencia de ataques en el test: es desplazamiento
        del propio tráfico normal ENTRE PARTICIONES (nunca «deriva temporal»:
        NSL-KDD no tiene marca de tiempo). Es la cifra que puede explicar por qué
        el umbral p95 fijado sobre D1_val promete ≈5 % de FPR y sobre D2 sale 8-10 %.

        NO sustituye a detect_data_drift(): son dos mediciones con dos poblaciones
        de comparación distintas y las dos se publican. Las columnas llevan sufijo
        '_normales' para que no se puedan confundir ni mezclar por accidente.

        Returns:
        --------
        pandas.DataFrame
            feature · ks_statistic_normales · ks_p_value_normales · mean_d1 ·
            mean_d2_normal · has_drift_normales
        """
        print("\n🌊 DETECCIÓN DE DRIFT (B) — D1 (Normal train) vs D2 SOLO NORMALES "
              "(tarea T2)")
        print("=" * 60)
        print(f"   Poblaciones comparadas: D1 = {len(self.D1_X):,} filas normales  vs  "
              f"D2-normal = {len(self.D2_X_normal):,} filas normales")
        print("   (esta cifra NO es la de (A): allí el término de comparación es D2")
        print("    COMPLETO y parte de su drift es la presencia de ataques)")

        results = []
        for feat in self.feature_names:
            ks_stat, ks_p = stats.ks_2samp(
                self.D1_X[feat].values, self.D2_X_normal[feat].values
            )
            results.append({
                'feature': feat,
                'ks_statistic_normales': ks_stat,
                'ks_p_value_normales': ks_p,
                'mean_d1': self.D1_X[feat].mean(),
                'mean_d2_normal': self.D2_X_normal[feat].mean(),
                'has_drift_normales': ks_p < 0.01,
            })

        drift_norm_df = pd.DataFrame(results)
        n_drift = drift_norm_df['has_drift_normales'].sum()
        total = len(drift_norm_df)

        print(f"\n   Drift significativo D1 vs D2-normales (KS p < 0.01): "
              f"{n_drift}/{total} características ({n_drift/total*100:.1f}%)")
        if n_drift > 0:
            print("\n   Top 10 por KS statistic (D1 vs D2-normales):")
            top = drift_norm_df.nlargest(10, 'ks_statistic_normales')[
                ['feature', 'ks_statistic_normales', 'ks_p_value_normales']
            ]
            print(top.to_string(index=False, float_format='%.4f'))

        self._plot_drift_normales(drift_norm_df)
        return drift_norm_df

    def _plot_drift(self, drift_df):
        fig, axes = plt.subplots(1, 2, figsize=(16, 6))

        top20 = drift_df.nlargest(20, 'ks_statistic')
        colors = ['red' if d else 'steelblue' for d in top20['has_drift']]
        axes[0].barh(range(len(top20)), top20['ks_statistic'], color=colors)
        axes[0].set_yticks(range(len(top20)))
        axes[0].set_yticklabels([f[:25] for f in top20['feature']], fontsize=8)
        axes[0].invert_yaxis()
        # Rótulo explícito de la población de comparación (T2): esta figura y la de
        # D2-solo-normales no deben poder confundirse al mirarlas en la memoria.
        axes[0].set_title('(A) Top 20 KS — D1 vs D2 COMPLETO (normales + ataques)\n'
                          '(rojo = drift significativo)')
        axes[0].set_xlabel('KS Statistic')

        axes[1].hist(drift_df['ks_p_value'], bins=30, alpha=0.75, edgecolor='black')
        axes[1].axvline(x=0.01, color='red', linestyle='--', label='p=0.01')
        axes[1].set_title('(A) Distribución de p-values — D1 vs D2 COMPLETO')
        axes[1].set_xlabel('p-value')
        axes[1].set_ylabel('Frecuencia')
        axes[1].legend()

        plt.tight_layout()
        self._save_figure('validacion_drift_ks.png')

    def _plot_drift_normales(self, drift_norm_df):
        """
        Figura propia del KS D1 vs D2-SOLO-NORMALES (T2), con nombre de archivo y
        títulos que la distinguen de validacion_drift_ks.png. Es la medición (B)
        por separado: mismo test y mismo criterio que (A) sobre otra población de
        comparación. No resta nada de (A) — ver la nota de no aditividad en la
        cabecera de la sección 4.
        """
        fig, axes = plt.subplots(1, 2, figsize=(16, 6))

        top20 = drift_norm_df.nlargest(20, 'ks_statistic_normales')
        colors = ['red' if d else 'steelblue' for d in top20['has_drift_normales']]
        axes[0].barh(range(len(top20)), top20['ks_statistic_normales'], color=colors)
        axes[0].set_yticks(range(len(top20)))
        axes[0].set_yticklabels([f[:25] for f in top20['feature']], fontsize=8)
        axes[0].invert_yaxis()
        axes[0].set_title('(B) Top 20 KS — D1 vs D2 SOLO NORMALES\n'
                          '(rojo = drift significativo)')
        axes[0].set_xlabel('KS Statistic')

        axes[1].hist(drift_norm_df['ks_p_value_normales'], bins=30, alpha=0.75,
                     edgecolor='black', color='darkseagreen')
        axes[1].axvline(x=0.01, color='red', linestyle='--', label='p=0.01')
        axes[1].set_title('(B) Distribución de p-values — D1 vs D2 SOLO NORMALES')
        axes[1].set_xlabel('p-value')
        axes[1].set_ylabel('Frecuencia')
        axes[1].legend()

        plt.tight_layout()
        self._save_figure('validacion_drift_ks_d2_normales.png')

    def _plot_drift_comparativa(self, drift_df, drift_norm_df):
        """
        Compara las DOS mediciones de KS característica a característica: las
        mismas features bajo las dos poblaciones de comparación, una barra al lado
        de la otra.

        NO es una descomposición del drift ni una atribución de causas. El KS es un
        supremo de diferencia de CDF y no es aditivo sobre una mezcla, así que
        KS(D1, D2) NO se reparte entre «lo que aporta el tráfico legítimo» y «lo
        que aportan los ataques» (ver la nota de la cabecera de la sección 4). Lo
        que la figura enseña es cuál de las dos mediciones es mayor en cada
        característica y por cuánto — que es también lo que dice el informe
        publicado: «las mismas características bajo las dos poblaciones ·
        delta = (A) - (B)».
        """
        comparada = drift_df[['feature', 'ks_statistic']].merge(
            drift_norm_df[['feature', 'ks_statistic_normales']], on='feature'
        )
        top = comparada.nlargest(20, 'ks_statistic')

        x = np.arange(len(top))
        w = 0.4
        fig, ax = plt.subplots(figsize=(15, 7))
        ax.bar(x - w / 2, top['ks_statistic'], w,
               label='(A) D1 vs D2 COMPLETO (normales + ataques)', color='steelblue')
        ax.bar(x + w / 2, top['ks_statistic_normales'], w,
               label='(B) D1 vs D2 SOLO NORMALES', color='darkseagreen')
        ax.set_xticks(x)
        ax.set_xticklabels([f[:22] for f in top['feature']], rotation=45,
                           ha='right', fontsize=8)
        ax.set_ylabel('KS Statistic')
        ax.set_title('Desplazamiento D1→D2 según la población de comparación\n'
                     '(top 20 por KS contra D2 completo · desplazamiento entre '
                     'particiones, NO deriva temporal)')
        ax.legend()
        plt.tight_layout()
        self._save_figure('validacion_drift_ks_comparativa.png')

    # ─────────────────────────────────────────────────────────────────────────
    # 5. Outliers
    # ─────────────────────────────────────────────────────────────────────────

    def analyze_outliers(self):
        """
        Detecta outliers por IQR en cada característica para las tres divisiones.
        Un alto porcentaje de outliers en D3 respecto a D1 es indicativo de
        características con buen poder discriminante.
        """
        print("\n🎯 ANÁLISIS DE OUTLIERS (IQR)")
        print("=" * 60)

        def iqr_outlier_pct(X):
            Q1 = X.quantile(0.25)
            Q3 = X.quantile(0.75)
            IQR = Q3 - Q1
            return ((X < Q1 - 1.5 * IQR) | (X > Q3 + 1.5 * IQR)).sum() / len(X) * 100

        summaries = {}
        for name, X in [('D1', self.D1_X), ('D2', self.D2_X), ('D3', self.D3_X)]:
            pct = iqr_outlier_pct(X)
            summaries[name] = pct
            worst_feat = pct.idxmax()
            print(f"   {name}: outliers promedio = {pct.mean():.2f}%  |  "
                  f"máximo en '{worst_feat}' ({pct.max():.1f}%)")

        self._plot_outliers(summaries)
        return summaries

    def _plot_outliers(self, summaries):
        top_feats = summaries['D1'].nlargest(15).index.tolist()
        fig, ax = plt.subplots(figsize=(14, 6))

        x = np.arange(len(top_feats))
        w = 0.25
        ax.bar(x - w, summaries['D1'][top_feats], w, label='D1 Normal', color='lightgreen', alpha=0.85)
        ax.bar(x,     summaries['D2'][top_feats], w, label='D2 Test',   color='steelblue',  alpha=0.85)
        ax.bar(x + w, summaries['D3'][top_feats], w, label='D3 Ataques', color='lightcoral', alpha=0.85)
        ax.set_xticks(x)
        ax.set_xticklabels([f[:18] for f in top_feats], rotation=45, ha='right', fontsize=8)
        ax.set_ylabel('% Outliers (IQR)')
        ax.set_title('Outliers por característica — Top 15 en D1')
        ax.legend()
        plt.tight_layout()
        self._save_figure('validacion_outliers_iqr.png')

    # ─────────────────────────────────────────────────────────────────────────
    # 6. Rango de escalado en D2 (informativo)
    # ─────────────────────────────────────────────────────────────────────────

    def check_d2_scaling_range(self):
        """
        Chequeo INFORMATIVO (no bloqueante): lista las características de D2
        con valores fuera de [0, 1] tras el escalado.

        Es ESPERABLE por diseño: el MinMaxScaler se ajusta solo sobre el train
        (D1+D3) y no se re-ajusta con D2 (hacerlo sería leakage), por lo que el
        test puede contener valores mayores que el máximo (o menores que el
        mínimo) visto en entrenamiento. Se reporta para vigilar su efecto en
        los modelos (p. ej. el FPR del autoencoder), no como error.

        Returns:
        --------
        pandas.DataFrame
            Columnas: feature, min_d2, max_d2 — solo las que salen de [0, 1],
            ordenadas por max_d2 descendente. Vacío si todas están en rango.
        """
        print("\n📏 RANGO DE D2 TRAS EL ESCALADO (chequeo informativo, no bloqueante)")
        print("=" * 60)

        maximos = self.D2_X.max()
        minimos = self.D2_X.min()
        fuera = self.D2_X.columns[(maximos > 1.0) | (minimos < 0.0)].tolist()

        resumen = pd.DataFrame({
            'feature': fuera,
            'min_d2': minimos[fuera].values,
            'max_d2': maximos[fuera].values,
        }).sort_values('max_d2', ascending=False).reset_index(drop=True)

        if fuera:
            print(f"   ℹ️  {len(fuera)} características de D2 fuera de [0, 1].")
            print("      Esperable por diseño: el scaler se ajustó en train (D1+D3)")
            print("      y no se re-ajusta con el test. Top 15 por valor máximo:")
            for _, row in resumen.head(15).iterrows():
                print(f"      - {row['feature']:<40} min={row['min_d2']:.4f}  max={row['max_d2']:.4f}")
            if len(resumen) > 15:
                print(f"      ... y {len(resumen) - 15} más (lista completa en el reporte de texto)")
        else:
            print("   ✓ Todas las características de D2 están dentro de [0, 1]")

        return resumen

    # ─────────────────────────────────────────────────────────────────────────
    # 7. Vocabulario del One-Hot: el delta 77 → 122 del fix del 2026-07-05
    # ─────────────────────────────────────────────────────────────────────────

    def medir_vocabulario_onehot(self):
        """
        RECOMPUTA el delta 77 → 122 del fix del one-hot (deuda de
        next-steps.md:278) contando las categorías reales de los CSV
        `_original_*` que dejó program.py. No hay ningún literal: las dos cifras
        salen de los datos de esta misma corrida.

        Qué se mide y por qué son dos números:
          - Vocabulario BUGGY (solo D1): antes del 2026-07-05 las columnas se
            alineaban contra D1, que es solo tráfico normal, así que las
            categorías de service/flag que únicamente aparecen en tráfico de
            ataque se descartaban al reindexar. Aquí se reconstruye contando las
            categorías presentes SOLO en D1.
          - Vocabulario ACTUAL (unión D1+D3): el que fija program.py:292-298.

        Este chequeo NO toca D2 ni ajusta nada: solo cuenta categorías (es la
        misma puerta de calidad de siempre, sin fit).

        Nota de variante: los CSV `_original_*` son idénticos en las dos
        variantes (54 y 122) porque la selección de características actúa
        después del one-hot; por eso esta medición da lo mismo en ambas, y el
        informe lo dice explícitamente.

        Returns:
        --------
        dict
            medido · n_numericas · dummies_solo_d1 · dummies_union ·
            total_solo_d1 · total_union · detalle (por columna categórica) ·
            total_union_transformers (contraste independiente) · motivo (si no
            se pudo medir)
        """
        print("\n🧬 VOCABULARIO DEL ONE-HOT — delta del fix de 2026-07-05 "
              "(D1 solo → unión D1+D3)")
        print("=" * 60)

        ruta_d1 = f'{self.base_path}_original_D1_normal_for_anomaly.csv'
        ruta_d3 = f'{self.base_path}_original_D3_known_attacks_for_signatures.csv'

        resultado = {
            'medido': False,
            'motivo': None,
            'n_numericas': None,
            'dummies_solo_d1': None,
            'dummies_union': None,
            'total_solo_d1': None,
            'total_union': None,
            'detalle': [],
            'total_union_transformers': None,
        }

        # Contraste independiente del 122: la lista completa post-one-hot que
        # program.py persiste en el joblib ('feature_columns_pre_seleccion').
        # Es otra medición del mismo número, por otra vía, y está disponible
        # también en la variante de 54 (donde los CSV procesados ya vienen
        # filtrados y no permitirían contarlo).
        transformers_path = f'{self.base_path}_transformers.joblib'
        if os.path.exists(transformers_path):
            try:
                pre = joblib.load(transformers_path).get('feature_columns_pre_seleccion')
                if pre is not None:
                    resultado['total_union_transformers'] = len(pre)
            except Exception as e:
                print(f"   ℹ️  No se pudo leer transformers.joblib ({e})")

        if not (os.path.exists(ruta_d1) and os.path.exists(ruta_d3)):
            resultado['motivo'] = ('no están en disco los CSV `_original_D1` / '
                                   '`_original_D3` que genera program.py')
            print(f"   ℹ️  Medición omitida: {resultado['motivo']}.")
            print("      El informe declarará el delta como VALOR HISTÓRICO con su procedencia.")
            return resultado

        try:
            cabecera = pd.read_csv(ruta_d1, nrows=0).columns.tolist()
            faltan = [c for c in self.COLUMNAS_CATEGORICAS if c not in cabecera]
            if faltan:
                resultado['motivo'] = f"faltan columnas categóricas en los CSV originales: {faltan}"
                print(f"   ℹ️  Medición omitida: {resultado['motivo']}.")
                return resultado

            d1_cat = pd.read_csv(ruta_d1, usecols=self.COLUMNAS_CATEGORICAS)
            d3_cat = pd.read_csv(ruta_d3, usecols=self.COLUMNAS_CATEGORICAS)

            # Numéricas = todo lo que no es categórico ni etiqueta. Es el mismo
            # criterio que aplica program.py antes del get_dummies.
            n_numericas = len([c for c in cabecera
                               if c not in self.COLUMNAS_CATEGORICAS
                               and c not in self.COLUMNAS_NO_CARACTERISTICA])

            detalle = []
            dummies_solo_d1 = 0
            dummies_union = 0
            for col in self.COLUMNAS_CATEGORICAS:
                cats_d1 = set(d1_cat[col].unique())
                cats_d3 = set(d3_cat[col].unique())
                n_d1 = len(cats_d1)
                n_union = len(cats_d1 | cats_d3)
                dummies_solo_d1 += n_d1
                dummies_union += n_union
                detalle.append({
                    'columna': col,
                    'categorias_en_D1': n_d1,
                    'categorias_union_D1_D3': n_union,
                    'recuperadas': n_union - n_d1,
                })

            resultado.update({
                'medido': True,
                'n_numericas': n_numericas,
                'dummies_solo_d1': dummies_solo_d1,
                'dummies_union': dummies_union,
                'total_solo_d1': n_numericas + dummies_solo_d1,
                'total_union': n_numericas + dummies_union,
                'detalle': detalle,
            })

            print(f"   Vocabulario BUGGY (alineado solo con D1): {resultado['total_solo_d1']} "
                  f"características = {n_numericas} numéricas + {dummies_solo_d1} dummies")
            print(f"   Vocabulario ACTUAL (unión D1+D3):         {resultado['total_union']} "
                  f"características = {n_numericas} numéricas + {dummies_union} dummies")
            print(f"   Δ = +{resultado['total_union'] - resultado['total_solo_d1']} características "
                  f"(+{dummies_union - dummies_solo_d1} dummies exclusivas de tráfico de ataque)")
            for d in detalle:
                print(f"      {d['columna']:<15} D1={d['categorias_en_D1']:>3}  "
                      f"unión={d['categorias_union_D1_D3']:>3}  "
                      f"(+{d['recuperadas']})")
            if resultado['total_union_transformers'] is not None:
                coincide = (resultado['total_union_transformers'] == resultado['total_union'])
                print(f"   {'✓' if coincide else '❌'} Contraste con transformers.joblib "
                      f"('feature_columns_pre_seleccion'): "
                      f"{resultado['total_union_transformers']} características")

        except Exception as e:
            resultado['medido'] = False
            resultado['motivo'] = f"error al leer los CSV originales: {e}"
            print(f"   ℹ️  Medición omitida: {resultado['motivo']}.")

        return resultado

    # ─────────────────────────────────────────────────────────────────────────
    # Reporte completo
    # ─────────────────────────────────────────────────────────────────────────

    def generate_validation_report(self):
        """Ejecuta toda la validación y guarda un reporte en texto."""
        print("\n📋 REPORTE COMPLETO DE VALIDACIÓN")
        print("=" * 60)

        integrity_ok, issues = self.validate_data_integrity()
        d2_dist, d3_dist = self.analyze_class_distribution()
        feat_analysis = self.analyze_feature_distributions()
        drift_df = self.detect_data_drift()
        # (B) el KS de T2, separado y sin sustituir al anterior.
        drift_norm_df = self.detect_data_drift_normales()
        self._plot_drift_comparativa(drift_df, drift_norm_df)
        outlier_summaries = self.analyze_outliers()
        d2_range_df = self.check_d2_scaling_range()
        # Delta 77 → 122 del fix del one-hot, recomputado desde los datos
        # (next-steps.md:278).
        onehot = self.medir_vocabulario_onehot()

        report = {
            'integrity_ok': integrity_ok,
            'issues': issues,
            'D1_size': len(self.D1_X),
            'D2_size': len(self.D2_X),
            'D2_normal_size': len(self.D2_X_normal),
            'D3_size': len(self.D3_X),
            'n_features': len(self.feature_names),
            # Clave HISTÓRICA (D1 vs D2 completo): no se renombra ni se cambia su
            # significado; la de T2 entra como clave NUEVA y explícita.
            'features_with_drift': int(drift_df['has_drift'].sum()),
            'features_with_drift_normales': int(drift_norm_df['has_drift_normales'].sum()),
            'avg_outlier_pct_D1': float(outlier_summaries['D1'].mean()),
            'low_variance_features': len(feat_analysis['low_variance']),
            'high_corr_pairs': len(feat_analysis['high_correlation']),
            'd2_features_fuera_rango': len(d2_range_df),
            # Recuento (nunca una lista fija) de los tipos 0-day de D2
            'n_zero_day_types': (0 if self.zero_day_df is None
                                 else int(len(self.zero_day_df))),
        }

        report_path = f'{self.base_path}_validation_report.txt'
        self._save_report(report, drift_df, d2_range_df, report_path,
                          drift_norm_df=drift_norm_df, onehot=onehot)

        print(f"\n{'✅' if integrity_ok else '❌'} Integridad: {'APROBADA' if integrity_ok else 'FALLA'}")
        print(f"🌊 Drift (A) D1 vs D2 COMPLETO:      {report['features_with_drift']}/{report['n_features']} características")
        print(f"🌊 Drift (B) D1 vs D2 SOLO NORMALES: {report['features_with_drift_normales']}/{report['n_features']} características")
        print(f"🕳️  Tipos 0-day en D2 (no vistos en D3): {report['n_zero_day_types']}")
        print(f"⚠️  Pares alta correlación: {report['high_corr_pairs']}")
        print(f"📄 Reporte guardado en: {report_path}")

        return report

    def _save_report(self, report, drift_df, d2_range_df, path, drift_norm_df=None,
                     onehot=None):
        with open(path, 'w', encoding='utf-8') as f:
            f.write("REPORTE DE VALIDACIÓN — DIVISIONES D1/D2/D3 NSL-KDD\n")
            f.write("=" * 60 + "\n\n")
            f.write(f"Integridad:       {'APROBADA' if report['integrity_ok'] else 'FALLA'}\n")
            f.write(f"D1 (Normal):      {report['D1_size']:,} instancias\n")
            f.write(f"D2 (Test):        {report['D2_size']:,} instancias\n")
            f.write(f"D2 solo normales: {report['D2_normal_size']:,} instancias "
                    f"({report['D2_normal_size'] / report['D2_size'] * 100:.1f} % de D2)\n")
            f.write(f"D3 (Ataques):     {report['D3_size']:,} instancias\n")
            f.write(f"Características:  {report['n_features']}\n")
            f.write(f"Drift (A) D1 vs D2 COMPLETO:      {report['features_with_drift']} características\n")
            f.write(f"Drift (B) D1 vs D2 SOLO NORMALES: {report['features_with_drift_normales']} características\n")
            # Rótulo explícito: `iqr_outlier_pct()` devuelve un porcentaje POR
            # CARACTERÍSTICA y aquí se publica su MEDIA entre características
            # (`.mean()`), no una mediana. La abreviatura anterior ("med.") era
            # ambigua y se documentó por error como mediana.
            f.write(f"Outliers D1 (media entre características): "
                    f"{report['avg_outlier_pct_D1']:.2f}%\n")
            f.write(f"Baja varianza (sobre D1+D3):    {report['low_variance_features']} características\n")
            f.write(f"Alta correlación (sobre D1+D3): {report['high_corr_pairs']} pares\n")
            f.write(f"D2 fuera de [0,1]: {report['d2_features_fuera_rango']} características (informativo)\n")

            if report['issues']:
                f.write("\nProblemas detectados:\n")
                for issue in report['issues']:
                    f.write(f"  ❌ {issue}\n")

            f.write("\nRecomendaciones:\n")
            if not report['integrity_ok']:
                f.write("  ❌ CRÍTICO: resolver problemas de integridad antes de entrenar\n")
            if report['high_corr_pairs'] > 0:
                f.write("  💡 Considera eliminar características con correlación > 0.95\n")
            if report['low_variance_features'] > 0:
                f.write("  💡 Considera eliminar características con varianza casi nula\n")
            if report['avg_outlier_pct_D1'] > 15:
                f.write("  ⚠️  Alto porcentaje de outliers en D1 — revisar preprocesamiento\n")

            # ── Las DOS mediciones de drift, cada una con su población de
            # comparación escrita en el propio rótulo (T2). No son intercambiables
            # y la (A) por sí sola NO explica el FPR.
            f.write("\n(A) Top 15 características con mayor drift — D1 vs D2 COMPLETO\n")
            f.write("    (D2 completo = normales + ataques: parte de este drift es\n")
            f.write("     simplemente que en D2 hay ataques y en D1 no)\n")
            top = drift_df.nlargest(15, 'ks_statistic')[
                ['feature', 'ks_statistic', 'ks_p_value', 'has_drift']
            ]
            f.write(top.to_string(index=False) + "\n")

            if drift_norm_df is not None:
                f.write("\n(B) Top 15 características con mayor drift — D1 vs D2 SOLO NORMALES\n")
                f.write("    (tráfico legítimo contra tráfico legítimo: DESPLAZAMIENTO ENTRE\n")
                f.write("     PARTICIONES, nunca 'deriva temporal' — NSL-KDD no tiene marca de\n")
                f.write("     tiempo. Es la medición que puede explicar el exceso de FPR sobre\n")
                f.write("     el ~5 % que promete el umbral p95 ajustado en D1_val)\n")
                top_n = drift_norm_df.nlargest(15, 'ks_statistic_normales')[
                    ['feature', 'ks_statistic_normales', 'ks_p_value_normales',
                     'has_drift_normales']
                ]
                f.write(top_n.to_string(index=False) + "\n")

                # Comparación directa de las dos KS sobre las mismas features. El
                # 'delta' es la diferencia entre DOS MEDICIONES, no un reparto de
                # causas: el KS no es aditivo sobre una mezcla de poblaciones y
                # (A) no se descompone en (B) más un «aporte de los ataques».
                # La salvedad se ESCRIBE EN EL ARTEFACTO, en las tres líneas de
                # rótulo de aquí abajo, y no solo en este comentario: el .txt se
                # lee suelto, sin el código ni la guía delante, y una columna
                # 'delta' sin aviso se lee como atribución. Si se toca el rótulo,
                # la salvedad se queda.
                f.write("\n(A) vs (B) — KS de las mismas características bajo las dos poblaciones\n")
                f.write("    (top 15 por KS contra D2 completo; delta = (A) - (B))\n")
                f.write("    OJO: 'delta' COMPARA las dos mediciones sobre las mismas\n")
                f.write("    características; NO es un reparto de causas. El estadístico KS\n")
                f.write("    es un supremo de diferencia de CDF y NO es aditivo sobre una\n")
                f.write("    mezcla de poblaciones: (A) no se descompone en (B) más un\n")
                f.write("    «aporte de los ataques».\n")
                comparada = drift_df[['feature', 'ks_statistic']].merge(
                    drift_norm_df[['feature', 'ks_statistic_normales']], on='feature'
                )
                comparada['delta'] = (comparada['ks_statistic']
                                      - comparada['ks_statistic_normales'])
                f.write(comparada.nlargest(15, 'ks_statistic').to_string(
                    index=False, float_format='%.4f') + "\n")

            # Chequeo informativo (no bloqueante) del rango de D2 tras el escalado
            f.write("\nCaracterísticas de D2 fuera de [0, 1] tras el escalado (INFORMATIVO):\n")
            f.write("Esperable por diseño: el scaler se ajusta solo en train (D1+D3) y no se\n")
            f.write("re-ajusta con el test (sería leakage). Vigilar su efecto en los modelos.\n")
            if d2_range_df.empty:
                f.write("  (ninguna — todo D2 dentro de [0, 1])\n")
            else:
                f.write(d2_range_df.to_string(index=False, float_format='%.4f') + "\n")

            # ── Los tipos 0-day de D2, NOMINALMENTE y no solo por recuento
            # (deuda menor de next-steps.md:277: hasta ahora solo salían por
            # consola y no quedaba constancia en ningún artefacto). La lista es
            # EMERGENTE: la calcula analyze_class_distribution() como diferencia
            # de conjuntos entre las etiquetas de D2 y las de D3, así que aquí no
            # se fija ningún nombre ni ninguna cifra a priori.
            f.write("\nTipos de ataque 0-day en D2 (presentes en D2, ausentes de D3): "
                    f"{report['n_zero_day_types']}\n")
            f.write("Derivados de los datos (etiquetas de D2 menos etiquetas de D3), nunca\n")
            f.write("de una lista escrita a mano. Solo el modelo de anomalías puede\n")
            f.write("detectarlos: el clasificador de firmas no ve ni una muestra suya en D3.\n")
            if self.zero_day_df is None:
                f.write("  (sin medir — analyze_class_distribution() no llegó a ejecutarse)\n")
            elif self.zero_day_df.empty:
                f.write("  (ninguno — todos los ataques de D2 están representados en D3)\n")
            else:
                f.write(self.zero_day_df.to_string(index=False) + "\n")
                n_inst_0day = int(self.zero_day_df['instancias_en_D2'].sum())
                f.write(f"  Total de instancias 0-day en D2: {n_inst_0day:,} "
                        f"({n_inst_0day / report['D2_size'] * 100:.2f} % de D2)\n")

            # ── Vocabulario del one-hot: el delta 77 → 122 del fix del
            # 2026-07-05, RECOMPUTADO por medir_vocabulario_onehot() a partir de
            # los CSV `_original_*`. Las dos cifras salen de los datos de esta
            # corrida: en este bloque no hay ningún literal 77 ni 122. Si los CSV
            # de origen no están en disco, se escribe el motivo y no se inventa
            # ninguna cifra.
            f.write("\nVocabulario del One-Hot — delta del fix del 2026-07-05\n")
            f.write("(vocabulario alineado solo con D1  →  vocabulario unión D1+D3)\n")
            if onehot is None:
                f.write("  (sin medir — no se recibió el resultado de "
                        "medir_vocabulario_onehot())\n")
            elif not onehot.get('medido'):
                f.write(f"  (sin medir — {onehot.get('motivo')})\n")
                f.write("  El delta se declara en el informe como VALOR HISTÓRICO, con su\n")
                f.write("  procedencia; no se reconstruye de memoria.\n")
            else:
                f.write(f"  Vocabulario BUGGY (alineado solo con D1): "
                        f"{onehot['total_solo_d1']} características = "
                        f"{onehot['n_numericas']} numéricas + "
                        f"{onehot['dummies_solo_d1']} dummies\n")
                f.write(f"  Vocabulario ACTUAL (unión D1+D3):         "
                        f"{onehot['total_union']} características = "
                        f"{onehot['n_numericas']} numéricas + "
                        f"{onehot['dummies_union']} dummies\n")
                f.write(f"  Delta = +{onehot['total_union'] - onehot['total_solo_d1']} "
                        f"características "
                        f"(+{onehot['dummies_union'] - onehot['dummies_solo_d1']} dummies "
                        f"exclusivas de tráfico de ataque)\n")
                f.write("  Desglose por columna categórica:\n")
                f.write(pd.DataFrame(onehot['detalle']).to_string(index=False) + "\n")
                f.write("  Nota de variante: los CSV `_original_*` son idénticos en las dos\n")
                f.write("  variantes (54 y 122) porque la selección de características actúa\n")
                f.write("  DESPUÉS del one-hot; por eso esta medición da lo mismo en ambas.\n")
            if onehot is not None and onehot.get('total_union_transformers') is not None:
                f.write(f"  Contraste independiente con "
                        f"`feature_columns_pre_seleccion` de transformers.joblib: "
                        f"{onehot['total_union_transformers']} características\n")

        # El vocabulario del one-hot va además a un CSV propio: hasta ahora la
        # cifra solo vivía en prosa y no había ningún artefacto en disco que la
        # respaldara.
        self._guardar_csv_vocabulario_onehot(onehot)

    def _guardar_csv_vocabulario_onehot(self, onehot):
        """
        Persiste en CSV la medición de medir_vocabulario_onehot(): una fila por
        columna categórica más una fila `__total__` con los agregados.

        Degrada igual que el método que lo mide: si no se pudo medir, se escribe
        una única fila con el `motivo` en lugar de omitir el artefacto o rellenar
        las celdas con cifras inventadas.
        """
        ruta = f'{self.base_path}_vocabulario_onehot.csv'
        variante = 'sin_seleccion' if self.variant_suffix else 'con_seleccion'
        columnas = ['variante', 'medido', 'motivo', 'columna', 'categorias_en_D1',
                    'categorias_union_D1_D3', 'recuperadas', 'n_numericas',
                    'total_solo_d1', 'total_union', 'delta_total',
                    'total_union_transformers']

        if onehot is None:
            onehot = {'medido': False,
                      'motivo': 'no se recibió el resultado de medir_vocabulario_onehot()',
                      'total_union_transformers': None}

        base_fila = {
            'variante': variante,
            'medido': bool(onehot.get('medido')),
            'motivo': onehot.get('motivo') or '',
            'total_union_transformers': onehot.get('total_union_transformers'),
        }

        filas = []
        if onehot.get('medido'):
            for d in onehot.get('detalle', []):
                fila = dict(base_fila)
                fila.update({
                    'columna': d['columna'],
                    'categorias_en_D1': d['categorias_en_D1'],
                    'categorias_union_D1_D3': d['categorias_union_D1_D3'],
                    'recuperadas': d['recuperadas'],
                })
                filas.append(fila)
            total = dict(base_fila)
            total.update({
                'columna': '__total__',
                'categorias_en_D1': onehot['dummies_solo_d1'],
                'categorias_union_D1_D3': onehot['dummies_union'],
                'recuperadas': onehot['dummies_union'] - onehot['dummies_solo_d1'],
                'n_numericas': onehot['n_numericas'],
                'total_solo_d1': onehot['total_solo_d1'],
                'total_union': onehot['total_union'],
                'delta_total': onehot['total_union'] - onehot['total_solo_d1'],
            })
            filas.append(total)
        else:
            fila = dict(base_fila)
            fila['columna'] = '__no_medido__'
            filas.append(fila)

        pd.DataFrame(filas, columns=columnas).to_csv(ruta, index=False)
        print(f"   ✓ Vocabulario del one-hot guardado en: {ruta}")


# ─────────────────────────────────────────────────────────────────────────────
# Funciones de uso directo
# ─────────────────────────────────────────────────────────────────────────────

def main(base_path=None):
    """
    Ejecuta la validación completa de las tres divisiones.

    Parameters:
    -----------
    base_path : str or None
        Prefijo de los archivos a validar. None → variante por defecto
        (con selección de características 4.3.5).
    """
    print("🔍 VALIDACIÓN D1/D2/D3 — NSL-KDD")
    print("=" * 60)

    if base_path is None:
        base_path = r"C:\Users\francisco.lopez\KIKO_TFG\Working_Directory\Resultados\specialized_nsl_kdd"
    validator = NSLKDDValidator(base_path)

    if validator.load_all_data():
        report = validator.generate_validation_report()
        status = '✅ DATOS LISTOS para entrenamiento' if report['integrity_ok'] else '❌ REVISAR problemas antes de continuar'
        print(f"\n🏁 {status}")
        return validator, report
    else:
        print("❌ No se pudieron cargar los datos. Ejecuta program.py primero.")
        return None, None


def quick_validation(base_path=None):
    """Validación rápida: solo integridad. Devuelve True si todo está bien."""
    if base_path is None:
        base_path = r"C:\Users\francisco.lopez\KIKO_TFG\Working_Directory\Resultados\specialized_nsl_kdd"
    validator = NSLKDDValidator(base_path)
    if validator.load_all_data():
        ok, _ = validator.validate_data_integrity()
        print(f"{'✅ Validación rápida exitosa' if ok else '❌ Problemas detectados — ejecuta generate_validation_report()'}")
        return ok
    return False


if __name__ == "__main__":
    # CLI (H3): con --sin-seleccion se valida la variante generada por
    # `program.py --sin-seleccion` (artefactos con sufijo '_sin_seleccion');
    # las figuras de esa variante llevan también el sufijo y no pisan las
    # de la variante por defecto.
    parser = argparse.ArgumentParser(
        description="Validación de las divisiones D1/D2/D3 generadas por program.py"
    )
    parser.add_argument(
        '--sin-seleccion', action='store_true',
        help="Valida la variante sin selección de características "
             "(artefactos con sufijo '_sin_seleccion')"
    )
    args = parser.parse_args()

    base = r"C:\Users\francisco.lopez\KIKO_TFG\Working_Directory\Resultados\specialized_nsl_kdd"
    if args.sin_seleccion:
        base += '_sin_seleccion'

    validator, report = main(base)
