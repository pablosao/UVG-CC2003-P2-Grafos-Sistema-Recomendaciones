#!/usr/bin/env python
# -*- coding: Windows-1252 -*-
# -*- coding: cp1252 -*-
# -*- coding: utf-8 -*-

"""
Created on Tue May 21 19:02:48 2019

@author: Pablo Sao
"""

import ControladorGrafo
from tkinter import *
 
window = Tk()
 
window.title("Recomendación Turistica".encode('raw_unicode_escape').decode('utf-8'))
 
window.geometry('350x200')
 
lbdata_base = Label(window, text="Crear Base de Datos")
 
lbdata_base.grid(column=0, row=0)
 
btcrea_db = Button(window, text="Crear", command=ControladorGrafo.CreateDataBase)
 
btcrea_db.grid(column=1, row=0)


lbrecomendacion = Label(window, text="Obtener Recomendacion")
 
lbrecomendacion.grid(column=0, row=1)
 
btobtiene_recomendacion = Button(window, text="Consultar", command=ControladorGrafo.FindMatch('Cálido'.encode('raw_unicode_escape').decode('utf-8'),
                           'QQ'.encode('raw_unicode_escape').decode('utf-8'),
                           'Aventura'.encode('raw_unicode_escape').decode('utf-8')
                           ,'Amigos/as'.encode('raw_unicode_escape').decode('utf-8')))
 
btobtiene_recomendacion.grid(column=1, row=1)


window.mainloop()

'''
#Forma de utilizar la creación de base de datos
ControladorGrafo.CreateDataBase()

# Forma de utilizar la busqueda de coincidencia
ControladorGrafo.FindMatch('Cálido'.encode('raw_unicode_escape').decode('utf-8'),
                           'QQ'.encode('raw_unicode_escape').decode('utf-8'),
                           'Aventura'.encode('raw_unicode_escape').decode('utf-8')
                           ,'Amigos/as'.encode('raw_unicode_escape').decode('utf-8'))
'''