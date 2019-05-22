# -*- coding: utf-8 -*-
"""
Created on Tue May 21 19:02:48 2019

@author: Pablo Sao
"""

from dbConnection import Connection
from readIni import read_ini

database = read_ini("database.ini","neo4j")


ejec = Connection(str(database["bolt"]),str(database["user"]),str(database["password"]))
ejec.print_greeting("Templado")

