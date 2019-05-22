# -*- coding: utf-8 -*-
"""
Created on Tue May 21 17:28:54 2019

Clase encargada de  realizar la conexión con la base de datos de neo4j

Referencia:
    <> https://neo4j-rest-client.readthedocs.io/en/latest/info.html
    <> https://neo4j.com/developer/python/
    
@author: Pablo Sao
"""
from neo4j import GraphDatabase

class Connection:
    
    def __init__(self, uri="", user="", password=""):
        self._driver = GraphDatabase.driver(uri, auth=(user, password))
       

    def close(self):
        self._driver.close()


    def greeting(self, message):
        with self._driver.session() as session:
            greeting = session.read_transaction(self._create_and_return_greeting, message)
            
            for record in greeting:
                print(record[0])


    def CreateDatabase(self,create_script):
        self._driver.session().write_transaction(self._createDataBase,create_script)
        

    @staticmethod
    def _create_and_return_greeting(tx, message):
        result = tx.run("match (:Clima {titulo: $message})--(turismo:Turismo) return turismo.Lugar ", message=message)
        return result


    @staticmethod
    def _createDataBase(tx,create_script):
        return tx.run(create_script)
