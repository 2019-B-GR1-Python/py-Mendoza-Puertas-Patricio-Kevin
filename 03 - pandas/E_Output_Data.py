# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 07:57:52 2019

@author: kevme
"""

import pandas as pd
import numpy as np
import os
import sqlite3

path_guardado_bin = "C://Users//kevme//Documents//GitHub//py-Mendoza-Puertas-Patricio-Kevin//03 - pandas//data//artwork_data.csv"
df5 = pd.read_pickle(path_guardado_bin)

# para copiar solo una cierta seccion se hace lo siguiente
df = df5.iloc[49980:50019,:].copy()


# Tipos archivos
# JSON
# EXCEL
# SQL

##### EXCEL ####
path_guardado = "C://Users//kevme//Documents//GitHub//py-Mendoza-Puertas-Patricio-Kevin//03 - pandas//data//mi_df_multiple.xlsx"
df.to_excel('mi_df_completo.xlsx')
df.to_excel('mi_df_completo.xlsx', index = False)
columnas = ['artist','title','year']
df.to_excel(path_guardado, columns = columnas)

path_multiple = "C://Users//kevme//Documents//GitHub//py-Mendoza-Puertas-Patricio-Kevin//03 - pandas//data//mi_df_multiple.xlsx"
writer = pd.ExcelWriter(path_multiple,
                        engine = 'xlsxwriter')


df.to_excel(writer, sheet_name = 'Primera')
df.to_excel(writer, sheet_name = 'Segunda',
            index = False)
df.to_excel(writer, sheet_name = 'Tercera',
            columns = columnas)

writer.save


### Multiples hojas de trabajo ####

num_artistas = df['artist'].value_counts()


path_colores = "C://Users//kevme//Documents//GitHub//py-Mendoza-Puertas-Patricio-Kevin//03 - pandas//data//mi_df_clores.xlsx"
writer = pd.ExcelWriter(path_colores,
                        engine = 'xlsxwriter')

num_artistas.to_excel(writer, sheet_name = 'Artist')

hoja_artistas = writer.sheets['Artistas']

rango_celdas = 'B2:B{}'.format(len(num_artistas.index)+1)

formaro_artistas = {
        "type" : "2_color_scale",
        "min_value" : "10",
        "min_type" : "percentile",
        "max_value" : "99",
        "max_type" : "percentile"}

hoja_artistas.conditional_format(rango_celdas,
                                 formato_artistas)

writer.save()

import xlsxwriter

workbook = xlsxwriter.Workbook('chart_line.xlsx')
worksheet = workbook.add_worksheet()

# Add the worksheet data to be plotted.
hoja_artistas.conditional_format(rango_celdas,
                                 formato_artistas)

# Create a new chart object.
chart = workbook.add_chart({'type': 'line'})

# Add a series to the chart.
chart.add_series({
    'values': '=Sheet1!$B$2:$B$100',
    'marker': {
        'type': 'square',
        'size': 8,
        'border': {'color': 'black'},
        'fill':   {'color': 'red'},
    },
})
# Insert the chart into the worksheet.
worksheet.insert_chart('C1', chart)

workbook.close()






















