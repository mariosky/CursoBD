#seguir los pasos del tutorial para comprender el funcionamiento
#de pandas, al final de la primera parte cambiar el formato
#de la grafica para que sea barras.


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df = pd.read_csv('auto-mpg.data', sep='\s+')

# leemos los datos cargados
df

# insertamos headers como none
df = pd.read_csv('auto-mpg.data', sep='\s+', header=None)

# una nueva tabla con headers con nombres correctos
df2 = pd.read_csv('auto-mpg.data', sep='\s+', header=None,
 names=['mpg','cylinders','displacement','horsepower','weight','acceleration',
 'model_year','origin','car_name'])

# verificamos los tipos de datos contenidos en las columnas
df2.dtypes


#dentro de la columnas reemplazar los signos ? con na_values
df2 = pd.read_csv('auto-mpg.data', sep='\s+', header=None,
         names=['mpg','cylinders','displacement','horsepower','weight',
         'acceleration','model_year','origin','car_name'], na_values='?')



# renombrar y asignarr el tipo de dato a cada columna
df2 = pd.read_csv('auto-mpg.data', sep='\s+',
     header=None,  na_values='?', names=['mpg','cylinders','displacement','horsepower',
        'weight','acceleration','model_year','origin','car_name'],
     dtype={'mpg':'f4','cylinders':'i4','displacement':'f4',
        'horsepower':'f4','weight':'f4','acceleration':'f4',
        'model_year':'i4','origin':'category','car_name':'category'})


# describir el tipo de dato por columna dentro de la tabla
# count, mean, std, min, 25%, 50%, 75%, max.
df2.describe()

# esta columa solo contiene 3 valores diferentes, se infiere
# que es el pais de procedencia
df2['origin']

# cambiamos el 1, 2 y 3 por los paises de origen
df2["origin"].cat.categories = ["USA", "Japan", "Germany"]

# al volver a imprimir origin cambio de 1, 2 y 3 a nombre de paises
df2['origin']

# creacion de grafica en forma de barras
#en esta parte plot(kind='bar') podemos camvbiar el tipo de plot,
#ya sea utilizar, barras, pie, etc, para este ejemplo urilizaremos barras
df2['origin'].value_counts().plot(kind='bar')

# despliege de la grafica generada en el paso anterior
plt.show()