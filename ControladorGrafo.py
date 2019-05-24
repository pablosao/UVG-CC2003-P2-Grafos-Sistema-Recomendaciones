# -*- coding: utf-8 -*-
"""
Created on Thu May 23 15:55:26 2019

@author: pablo
"""
from dbConnection import Connection
from readIni import read_ini
import os


def CreateDataBase():
    
    database = read_ini("database.ini","neo4j")

    path = 'scriptCreate.graph'
    query = ''
    
    if os.path.isfile(path):
        file = open(path,"r")
        if file.mode == "r":
            
            query = file.read()
        
    try:
        ejec = Connection(str(database["bolt"]),str(database["user"]),str(database["password"]))
    
        ejec.createDB(query.encode('raw_unicode_escape').decode('utf-8'))
        
        #datos = ejec.greeting("Templado")
        
        '''
        for record in datos:
            print(record[0]['titulo'] + ' - ' + record[1]['Lugar'])
        '''
        
        ejec.close()
        
    except Exception as e:
        print(str(e))


def FindMatch(clima,presupuesto,tipo_turismo,tipo_viaje):
    
    query = 'match (clima:Clima)-[:TIENE_CLIMA]->(turismo:Turismo) '
    
    if(clima != ''):
        query += 'where clima.titulo = "{0}" '.format(clima)
        
        if(presupuesto != ''):
            query += 'AND '
    else:
        query += 'where '
        
    if(presupuesto != ''):
        query += 'turismo.Presupuesto = "{0}" '.format(presupuesto)
 
    
    query += 'match (tTurismo:Tipo_Turismo)--(turismo) ' 
    
    if(tipo_turismo != ''):
        query += 'where tTurismo.titulo = "{0}" '.format(tipo_turismo)
        
    query += 'match (cviaje:Tipo_Viaje)--(turismo) '
    
    if(tipo_viaje != ''):
        query += 'where cviaje.titulo = "{0}" '.format(tipo_viaje)

    query += ('match (municipio:Municipio)--(turismo) ' +
                'return municipio,cviaje,tTurismo,clima,turismo ')
                    
    print(query)
    


    
    
    
    
    
    
    
    