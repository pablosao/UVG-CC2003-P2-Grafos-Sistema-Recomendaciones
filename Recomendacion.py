# -*- coding: utf-8 -*-
"""
Created on Tue May 21 19:02:48 2019

@author: Pablo Sao
"""

from dbConnection import Connection
from readIni import read_ini

database = read_ini("database.ini","neo4j")

try:
    ejec = Connection(str(database["bolt"]),str(database["user"]),str(database["password"]))

    datos = ejec.greeting("Templado")
    
    ejec.close()
    
except:
    print("Ocurrio un problema")



for record in datos:
    print(record[0]['titulo'] + ' - ' + record[1]['Lugar'])
