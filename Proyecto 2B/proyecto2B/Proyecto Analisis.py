# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 00:59:13 2019

@author: kevme
"""

#Proyecto Segundo bimestre
##Kevin Mendoza

###El presente proyecto de analisis de datos con python trata sobre lo siguiente,
###Se obtuvo un archivo csv que contiene datos sobre jugadores de futbol de todo
###el mundo, el archivo csv se obtuvo realizando Scrapy a un link de descarga de 
###jugadores de la fifa. Los datos originales tenian muchas caracteristicas de
###los jugadores y para este proyecto se escogio las principales caracteristcas
###como son:

###full_name
###age
###height_cm
###weight_kgs
###positions
###positions
###potential
###value_euro
###finishing
###short_passing
###dribbling
###freekick_accuracy
###long_passing
###ball_control
###acceleration
###sprint_speed
###agility

###Estas caracteristicas se escogieron por ser las mas importantes para realizar
###un buen analisis.


###Para realizar este proyecto se usaran las siguientes librerías.

import pandas as pd
import numpy as np
import os
import sqlite3
import matplotlib.pyplot as plt


###El archivo csv se encuentra en la siguiente direccion, este se lo guardara
###en el siguiente path.
path = "C://Users//kevme//Documents//GitHub//py-Mendoza-Puertas-Patricio-Kevin//Proyecto 2B//proyecto2B//proyecto2B//spiders//fifa.csv"

###Al dataframe de prueba se lo usara de la siguiente manera.
df_prueba = pd.read_csv(path,  encoding = 'unicode_escape',sep = ";")

###Para continuar se guardara en un pickle, con la siguiente configuracion.
path_guardado_pickle = "C://Users//kevme//Documents//GitHub//py-Mendoza-Puertas-Patricio-Kevin//Proyecto 2B//proyecto2B//proyecto2B//spiders//fifa.pickle"

df_prueba.to_pickle(path_guardado_pickle)

df_pickle = pd.read_pickle(path_guardado_pickle)

###El archivo original se tienen mas de 15000 jugadores, para este proyecto se usaran
###solo los primeros 100. 
df = df_pickle.iloc[1:200,:].copy()

###y para finalizar y poder realizar el analisis se creara el xlsx del proyecto.
df.to_excel('C://Users//kevme//Documents//GitHub//py-Mendoza-Puertas-Patricio-Kevin//Proyecto 2B//proyecto2B//proyecto2B//spiders//mi_proyecto.xlsx')

###Para poder ver lo que contiene nuestro dataframe y poder continuar con el
###analiis, usaremos la siguiente linea.
df.head()

df

###Para poder observar en una tabla varios ejemplos se lo realiza de la 
###siguiente manera; por ejemplo: jugadores de futbol de Argentina
a=df[df.nationality=='Brazil']
a


### Jugadores menores de 25 años
df[df.age < 25 ]

##Graficos
###grafico Posiciones
###El siguiente grafico se puede observar la cantidad de jugadores en cada una
###de las posiciones
fig = plt.figure(figsize=(10,6))
df.nationality.value_counts().plot(kind='bar')
plt.title('nacionalidad')
plt.show()

###Potencial de los jugadores de Brazil
a.groupby('full_name').mean()["potential"].plot(kind='bar',stacked=True,
          title="Potencial de los jugadores")



###Jugadores con la mayor edad en cada pais.
df.groupby('nationality').mean()["age"].plot(kind='bar',stacked=True,
          title="Promedio de edad de los jugadores en cada pais")


###Variacion del potencial en cada posicion
jugadores = df.groupby(['positions'])['potential'].describe()
jugadores.plot(kind='line')


###Potecial de los jugadores segun la edad.
fig, ax1 = plt.subplots()
Potencial_edad = pd.read_excel('C://Users//kevme//Documents//GitHub//py-Mendoza-Puertas-Patricio-Kevin//Proyecto 2B//proyecto2B//proyecto2B//spiders//mi_proyecto.xlsx')
my_plot = df.plot("age", "potential", kind="scatter", ax=ax1)
ax1.set_xlabel("Edades")
ax1.tick_params(labelsize=16, pad=8)
fig.suptitle('Potencial de los jugadores segun la edad', fontsize=15)


### Porcentaje de jugadores por pais.
df['nationality'].value_counts().head(15).plot(kind = 'pie', cmap = 'Paired', autopct="%0.1f %% ")
plt.ylabel('')


###Potencial de los jugadores de Francia en cuanto a goles.
b=df[df.nationality=='France']
b
b.groupby('full_name').mean()["finishing"].plot(kind='bar',stacked=True)


### Porcentaje de jugadores por posicion en el campo.
b['positions'].value_counts().head(15).plot(kind = 'pie', cmap = 'Paired', autopct="%0.1f %% ")
plt.ylabel('')


### Potencial de los jugadores de Inglaterra en cuanto a control de balon.
c=df[df.nationality=='England']
c
c.groupby('full_name').mean()["ball_control"].plot(kind='bar',stacked=True)


### Edad de los jugaores de Inglaterra. 
c.groupby('full_name').mean()["age"].plot(kind='bar',stacked=True)

## Conclusiones

## 1) Como se pudo observar en la practica python es una herramienta muy poderosa
## que nos ayuda en el analisis de datos.

## 2) Python nos permite separar los datos si un archivo es muy grande de la
## siguiente manera df = df_pickle.iloc[1:200,:].copy() para que de esta forma
## sea mas facil el trabajo.

## 3) Los graficos que nos ofrece python nos ayuda a visualizar de una manera mas 
## dinamica los datos que se tengan en los archivos.




















