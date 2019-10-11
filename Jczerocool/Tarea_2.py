
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np



# cambio de nombre en los headers, ademas de separaciones por coma
df2 = pd.read_csv('iris.data', sep=',', header=None,
 names=['sepal length in cm','sepal width in cm','petal length in cm','petal width in cm','class'])

# tipo de dato contenido en el dataset
df2.dtypes

df2.describe()

# df2['sepal length in cm'].value_counts().plot(kind='bar')
df2['class'].value_counts().plot(kind='pie')
plt.show()

df2['sepal length in cm'].value_counts()

# df2.plot.scatter(x='sepal length in cm', y='sepal width in cm',c='petal length in cm',cmap='viridis');
# plt.show()

df2['sepal length in cm'].mean()

df2['sepal width in cm'].mean()

df2['petal length in cm'].mean()
a
df2['petal width in cm'].mean()
