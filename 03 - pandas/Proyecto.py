# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 00:59:13 2019

@author: kevme
"""

#Proyecto primer bimestre
##Kevin Mendoza

###El presente proyecto de analisis de datos con python trata sobre lo siguiente,
###Se obtuvo un archivo csv que contiene datos de hombres en donde se puede
###encontrar su fecha de nacimiento, provncia y canton donde nacio, su edad,
###su estado civil, la cantidad de hijos que tiene esta persona, esos son los
###campos principales que se usaran, pero este archivo contienen mas campos.

###Para realizar este proyecto se usaran las siguientes librerías.

import pandas as pd
import numpy as np
import os
import sqlite3
import matplotlib.pyplot as plt


###El archivo csv se encuentra en la siguiente direccion, este se lo guardara
###en el siguiente path.
path = "D://kevin//poli//actualizacion//python//proyecto//proyecto.csv"

###Al dataframe de prueba se lo usara de la siguiente manera.
df_prueba = pd.read_csv(path,  encoding = 'unicode_escape',sep = ";")

###Como se explico anteriormente en la introduccion, se usaran los siguientes
###campos.
columnas = ['prov_insc','cant_insc','hijos_rec',
            'anio_nach','mes_nach','dia_nach',
            'edad_hom','est_civih']

###Se tendra un nuevo dataframe que usara las columnas definidas anteriormente.
df_prueba2 = pd.read_csv(path,  encoding = 'unicode_escape',sep = ";", usecols=columnas)

###Para continuar se guardara en un pickle, con la siguiente configuracion.
path_guardado_pickle = "D://kevin//poli//actualizacion//python//proyecto//proyecto.pickle"

df_prueba2.to_pickle(path_guardado_pickle)

df_pickle = pd.read_pickle(path_guardado_pickle)

df = df_pickle.iloc[1:1000,:].copy()

###y para finalizar y poder realizar el analisis se creara el xlsx del proyecto.
df.to_excel('D://kevin//poli//actualizacion//python//proyecto//mi_proyecto.xlsx')

###Para poder ver lo que contiene nuestro dataframe y poder continuar con el
###analiis, usaremos la siguiente linea.
df.head()

###Para poder observar en una tabla varios ejemplos se lo realiza de la 
###siguiente manera; por ejemplo: hombres con estado civil viudos
df[df.est_civih=='Viudo']


### Hombres con mas de tres hijos
df[df.hijos_rec > 3]

##Graficos
###grafico hijos
###El siguiente grafico se puede observar la cantidad de pesonas que no tienen
###hijos o que tienen 1 hijo, 2 hijo, etc.
fig = plt.figure(figsize=(10,6))

df.hijos_rec.value_counts().plot(kind='bar')
plt.title('Hijos')

plt.show()


###Grafico provincias
###El siguiente grafico se observar el numero de hombres que hay en cada provincia

fig = plt.figure(figsize=(10,5))

df.prov_insc.value_counts(normalize = True).plot(kind='bar')
plt.title('Provincias')

plt.show()


###Grafico viudos segun los anios
###En el siguiente grafico se puede ver el numero de hombres viudos segun los anios

fig = plt.figure(figsize=(15,6))

df.edad_hom[df.est_civih=='Viudo'].value_counts().plot(kind='bar')
plt.title('Numero de personas viudas segun los anios')

plt.show()


###Grafico solteras en cada provincia
###El siguiente grafico muestra el numero de solteros en cada provincia
fig = plt.figure(figsize=(15,6))

df.prov_insc[df.est_civih=='Soltero'].value_counts().plot(kind='bar')
plt.title('Personas solteras en cada provincia')

plt.show()


###Hombres viudos maypres a 60 anios
###El grafico a continuacion muestra a hombres viudos maypres a 60 anios
## tabla hombres mayores a 60 anios
mayores_60_anios = df[df.edad_hom > 60]
mayores_60_anios

fig = plt.figure(figsize=(15,6))

mayores_60_anios[df.est_civih=='Viudo'].plot(kind='bar')
plt.title('Hombres viudos mayores a 60 anios')

plt.show()


### Hombres solteros que nacieron en 1992
###El grafico a continuacion muestra a hombres solteros que nacieron en 1992
## tabla hombres mayores a 60 anios
anio_nacimiento = df[df.anio_nach == 1992]
anio_nacimiento

fig = plt.figure(figsize=(15,6))

anio_nacimiento[df.est_civih=='Soltero'].plot(kind='bar')
plt.title('Hombres solteros que nacieron en 1992')

plt.show()


df.groupby('est_civih').plot(kind = 'bar')
plt.ylabel('Total de hombres')

##Conclusiones

#1) Como se pudo observar en la practica python es una herramienta muy poderosa
#que nos ayuda en el analisis de datos.

#2) Python nos permite separar los datos si un archivo es muy grande de la
#siguiente manera df = df_pickle.iloc[1:1000,:].copy() para que de esta forma
#sea mas facil el trabajo.

#3) Los graficos que nos ofrece python nos ayuda a visualizar de una manera mas 
#dinamica los datos que se tengan en los archivos.




















