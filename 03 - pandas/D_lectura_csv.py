# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 08:21:11 2019

@author: kevme
"""

import pandas as pd
import os

# 1) JSON CSV HTML XML .....
# 2) Binary files -> (!#mf-.1234'120)
# 3) relational Databases

# Definir el path del archivo

path = "C://Users//kevme//Documents//GitHub//py-Mendoza-Puertas-Patricio-Kevin//03 - pandas//data//artwork_data.csv"

df1 = pd.read_csv(path, nrows = 10)

columnas = ['id','artist','title','medium','year','acquisitionYear','height','width','units']

df2 = pd.read_csv(path, nrows = 10, usecols = columnas)

df3 = pd.read_csv(path, nrows = 10, usecols = columnas, index_col = 'id')

# Para crear un pickle, que nos sirve para tener varias versiones guardadas
path_guardado = "C://Users//kevme//Documents//GitHub//py-Mendoza-Puertas-Patricio-Kevin//03 - pandas//data//artwork_data.csv"

df3.to_pickle(path_guardado) 

df4 = pd.read_pickle(path_guardado)








