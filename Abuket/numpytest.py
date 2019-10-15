#Raul Madrigal Carrion

import numpy as np 
import pandas as pd 

auto_mpg = pd.read_csv('BaseDatos/auto-mpg.data', sep='\s+', header=None,
         names=['mpg','cylinders','displacement','horsepower','weight',
         'acceleration','model_year','origin','car_name'], na_values='?',
         dtype={'mpg':'f4','cylinders':'i4','displacement':'f4',
        'horsepower':'f4','weight':'f4','acceleration':'f4',
        'model_year':'i4','origin':'category','car_name':'category'})

auto_mpg["origin"].cat.categories = ["USA", "Japan", "Germany"]
#se comentaron lineas para hacer cada una de las pruebas individualmente

# print(auto_mpg.index)
# print(auto_mpg.columns) 
# print(auto_mpg.tail(3))
#print(auto_mpg.values) 
print(auto_mpg.sort_values(by=['origin','car_name']).tail)


