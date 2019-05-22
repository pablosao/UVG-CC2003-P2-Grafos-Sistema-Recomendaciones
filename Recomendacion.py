#!/usr/bin/env python
# -*- coding: Windows-1252 -*-
# -*- coding: cp1252 -*-
# -*- coding: utf-8 -*-

"""
Created on Tue May 21 19:02:48 2019

@author: Pablo Sao
"""

from dbConnection import Connection
from readIni import read_ini
import os
import sys



database = read_ini("database.ini","neo4j")

path = 'scriptCreate.graph'
query = ''

if os.path.isfile(path):
    file = open(path,"r")
    if file.mode == "r":
        
        query = file.read()
    
print
try:
    ejec = Connection(str(database["bolt"]),str(database["user"]),str(database["password"]))

    ejec.createDB(query.encode('raw_unicode_escape').decode('utf-8'))
    
    #datos = ejec.greeting("Templado")
    
    ejec.close()
    
except Exception as e:
    print(str(e))


print("Termino")
'''
for record in datos:
    print(record[0]['titulo'] + ' - ' + record[1]['Lugar'])
'''