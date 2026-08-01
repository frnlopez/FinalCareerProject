# Proyecto

# Lo primero es crear y activar un entorno virtual

# Usamos python3.11 ya que es una versión muy estable (la última versión es la 3.13.5)


"C:\Python311\python.exe" -m venv Imp
source Imp/Scripts/activate



# De este modo instalamos las librerías todas a la vez
pip install -r requirements.txt



# Descripción del código actual por partes --- 25/07/2025 16:50

# Funcionalidades

1. Descarga y Carga del dataset

https://github.com/Jehuty4949/NSL_KDD

Descargamos archivos KDDTrain+.txt & KDDTest+.txt

Asignación automática de los 41 nombres de características


2. Analisis Exploratorio (EDA)
Dimensiones de los datasets
Información general y estadísticas descriptivas
Verificación de valores nulos
Análisis de columnas categóricas
Distribución de ataques con visualizaciones
Mapeo a las 4 categorías principales (DoS, Probe, R2L, U2R)


3. Preprocesamiento Completo:

Separación de características y variable objetivo
One-Hot Encoding para columnas categóricas
Escalado con MinMaxScaler o StandardScaler
Codificación de etiquetas con LabelEncoder
Manejo de inconsistencias entre conjuntos de entrenamiento y prueba
