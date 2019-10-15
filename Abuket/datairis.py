import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


plantas = pd.read_csv('BaseDatos/iris.data', sep=',', header=None,
         names=['SepalLengthInCm','SepalWidthInCm','PetalLengthInCm','PetalWidthInCm','class'], na_values='?',
         dtype={'SepalLengthInCm':'f4','SepalWidthInCm':'f4','PetalLengthInCm':'f4',
        'petal width in cm':'f4','class':'category'})

plantas["class"].cat.categories = ["Iris Setosa", "Iris Versicolour", "Iris Virginica"]

promlargoS=(plantas.SepalLengthInCm.sum())/150
promlargoP=(plantas.PetalLengthInCm.sum())/150
promAnchoS=(plantas.SepalWidthInCm.sum())/150
promAnchoP=(plantas.PetalWidthInCm.sum())/150
plantas['class'].value_counts().plot(kind='pie')

print('Promedio Largo del Sepalo :', promlargoS)
print('Promedio Largo del Petalo :', promlargoP)
print('Promedio Ancho del Sepalo :', promAnchoS)
print('Promedio Ancho del Petalo :', promAnchoP)
plt.show()

