# -*- coding: utf-8 -*-
"""
Creado el 22 de mayo de 2016

Realiza la busqueda de todos los registros de una etiqueta (section) en un
archivo .ini

@author: pablo
@version: 1v2
"""
from configparser import ConfigParser
import os 

def read_ini(filename='', section=''):
    """ 
     Lee archivo .ini y retorna un diccionario con los valores de la seccion
    :param filename: nombre del archivo .ini
    :param section: sección que se desea leer dentro del archivo .ini
    :return: Diccionario con todos los valores de la seccion
    """
    
    conf = {}
    
    if os.path.isfile(filename):
        
        # Se parsea y lee el archivo .ini
        parser = ConfigParser()
        parser.read(filename)
     
        # se obtienen los valores de una sección
        
        if parser.has_section(section):
            items = parser.items(section)
            for item in items:
                conf[item[0]] = item[1]
        else:
            raise Exception('La sección {0} no fue encontrada en el archivo {1}'.format(section, filename))
     
    else:
        raise Exception('El archivo {0} no fue encontrado.'.format(filename))
     
        
    return conf