import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import nltk
import seaborn as sns

#path del csv creado
path_csv = "C://Users//kevme//Documents//GitHub//py-Mendoza-Puertas-Patricio-Kevin//04 - Scrapy//06-spider-items//arania_fybeca//arania_fybeca//spiders//tmp//productos-fybeca.csv"
df = pd.read_csv(path_csv,  encoding = 'unicode_escape',sep = ",")

# Ahorro por la compre con tarjeta fybeca
df['ahorro'] = df['precio_normal'] - df['precio_descuento']

ahorroCompra = df['ahorro'].sum()
descuentoTotal = df['ahorro'].max()
descuetoMinimo = df['ahorro'].min()

#ver calculo descuento Total
print("Precio con el descuento maximo : ",descuentoTotal)

#ver calculo descuento minimo
print('Precio con el descuento minimo : ', descuetoMinimo)

#Ahorro por la compra con tareta
print('Ahorro por compra con tarjeta : ', ahorroCompra)