# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 11:33:51 2020

@author: kevme
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5 import uic

#clase heredada de QMainWindow(Contructor de ventanas)
class Ventana(QDialog):
    # Metodo constructor de la clase
    def __init__(self):
        #iniciar el objeto QMainWindow
        QMainWindow.__init__(self)
        #Cargar la configuracion de archivo .ui en el objeto
        uic.loadUi("MainWindow.ui", self)
        
#Instancia para iniciar la aplicacion
app = QApplication(sys.argv)

#Crear un objeto de la clase
_ventana = Ventana()

#Mostrar ventana
_ventana.show()

#Ejecutar la aplicacion
app.exec()
