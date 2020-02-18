import pandas as pd


###El archivo csv se encuentra en la siguiente direccion, este se lo guardara
###en el siguiente path.
path = "C://Users//kevme//Documents//GitHub//py-Mendoza-Puertas-Patricio-Kevin//04 - Scrapy//06-spider-items//arania_fybeca//arania_fybeca//spiders//tmp//productos-fybeca.csv"

###Al dataframe de prueba se lo usara de la siguiente manera.
df_prueba = pd.read_csv(path,  encoding = 'unicode_escape',sep = ",")

###Para continuar se guardara en un pickle, con la siguiente configuracion.
path_guardado_pickle = "C://Users//kevme//Documents//GitHub//py-Mendoza-Puertas-Patricio-Kevin//04 - Scrapy//06-spider-items//arania_fybeca//arania_fybeca//spiders//tmp//a.pickle"

df_prueba.to_pickle(path_guardado_pickle)

df_pickle = pd.read_pickle(path_guardado_pickle)

###El archivo original se tienen mas de 15000 jugadores, para este proyecto se usaran
###solo los primeros 100. 
df = df_pickle.iloc[1:200,:].copy()

###y para finalizar y poder realizar el analisis se creara el xlsx del proyecto.
df.to_excel('C://Users//kevme//Documents//GitHub//py-Mendoza-Puertas-Patricio-Kevin//04 - Scrapy//06-spider-items//arania_fybeca//arania_fybeca//spiders//tmp//mi_proyecto.xlsx')

###Para poder ver lo que contiene nuestro dataframe y poder continuar con el
###analiis, usaremos la siguiente linea.
df.head()

df


#compra con tarjeta y sin tarjeta
df.loc[df.index[-1] + 1] = df.sum()
print (df)

