# Ejercicios
#
# iris.data
#
# Lee desde archivo el conjunto de datos iris.data utiliza el método read_csv().
#
# Nombra a los atributos como se especifica en la información del conjunto de datos:
#
#   Attribute Information:
#    1. sepal length in cm
#    2. sepal width in cm
#    3. petal length in cm
#    4. petal width in cm
#    5. class:
#       -- Iris Setosa
#       -- Iris Versicolour
#       -- Iris Virginica
# Haz una gráfica con los datos como se hizo en el ejercicio de introducción utilizando el método plot().
#
# Imprime cual es el ancho y largo promedio del sépalo y pétalo.


# importe de librerias necesarias para la ejecucion
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# Lee desde archivo el conjunto de datos iris.data utiliza el método read_csv().
#  Nombra a los atributos como se especifica en la información del conjunto de datos:
#
#   Attribute Information:
#    1. sepal length in cm
#    2. sepal width in cm
#    3. petal length in cm
#    4. petal width in cm
#    5. class:
#       -- Iris Setosa
#       -- Iris Versicolour
#       -- Iris Virginica


# cambio de nombre en los headers, ademas de separaciones por coma
df2 = pd.read_csv('iris.data', sep=',', header=None,
 names=['sepal length in cm','sepal width in cm','petal length in cm','petal width in cm','class'])

# tipo de dato contenido en el dataset
df2.dtypes

# descripcion de los datos contenidos en el dataset
df2.describe()

# Haz una gráfica con los datos como se hizo en el ejercicio de
# introducción utilizando el método plot().
df2['class'].value_counts().plot(kind='pie')
plt.show()

# Imprime cual es el ancho y largo promedio del sépalo y pétalo.
df2['sepal length in cm'].mean()

df2['sepal width in cm'].mean()

df2['petal length in cm'].mean()
a
df2['petal width in cm'].mean()
