# eda_basico.py

"""
Análisis Exploratorio de Datos (EDA) Básico
Autor: Walter Manuel Lannot
Fecha: Abril 2025
Descripción: Script sencillo para cargar, explorar y visualizar datos básicos.
"""

# Librerías principales
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar datos
# Puedes cambiar 'datos.csv' por el nombre de tu archivo real
data = pd.read_csv('datos.csv')

# Información general
print("Primeras filas del dataset:")
print(data.head())

print("\nDescripción estadística:")
print(data.describe())

print("\nInformación general del dataset:")
print(data.info())

# Detección de valores nulos
print("\nValores nulos por columna:")
print(data.isnull().sum())

# Visualización simple
# Histograma de una variable numérica
plt.figure(figsize=(10,6))
sns.histplot(data['variable_numerica'], kde=True)
plt.title('Distribución de Variable Numérica')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.show()

# Gráfico de correlación entre variables numéricas
plt.figure(figsize=(10,8))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
plt.title('Matriz de Correlación')
plt.show()
