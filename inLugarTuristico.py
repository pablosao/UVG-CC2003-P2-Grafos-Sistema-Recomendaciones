# -*- coding: utf-8 -*-
"""
Created on Fri May 24 20:30:36 2019

Referencia: http://zetcode.com/wxpython/menustoolbars/
@author: pablo
"""


import wx
import ControladorGrafo

class lugarTuristico(wx.Frame): 
        
    def __init__(self, parent, title): 
   
        super(lugarTuristico, self).__init__(parent, title = title,size = (320,500))
        
        self.panel = wx.Panel(self) 
        box = wx.BoxSizer(wx.VERTICAL) 
        
        #Texto Inicial
        self.titulo = wx.StaticText(self.panel,label = "Crear Nodo" ,style = wx.ALIGN_CENTRE) 
        box.Add(self.titulo, 0 , wx.EXPAND |wx.ALIGN_CENTER_HORIZONTAL |wx.ALL, 20) 
        
        
        #--------------------------------------------------------------------------
        
        #Configuración ComboBox para selección de Municipio
        lbmunicipio = wx.StaticText(self.panel,label = "Seleccione Municipio",style = wx.ALIGN_CENTRE) 
        box.Add(lbmunicipio,0,wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL,5) 
        
         # Creando información de ComboBox con datos de la base de datos
        self.MUNICIPIO = []
        
        query = "match (municipio:Municipio) return municipio.titulo order by municipio.titulo"
        
        dato = ControladorGrafo.ExecQuery(query)
        
        for record in dato:
            self.MUNICIPIO.append(record[0])
                
        
        self.cbmunicipio = wx.Choice(self.panel,choices = self.MUNICIPIO) 
        box.Add(self.cbmunicipio,1,wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL,5)
        
        
        #--------------------------------------------------------------------------
        
        
        
        #Configuración ComboBox para selección de Clima
        lbtipo_clima = wx.StaticText(self.panel,label = "Escoja Clima",style = wx.ALIGN_CENTRE) 
        box.Add(lbtipo_clima,0,wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL,5) 
        
        
        # Creando información de ComboBox con datos de la base de datos
        self.TIPO_CLIMA = []
        
        
        query = "match (clima:Clima) return clima.titulo  order by clima.titulo"
        
        dato = ControladorGrafo.ExecQuery(query)
        
        for record in dato:
            self.TIPO_CLIMA.append(record[0])
        
        
        #self.TIPO_CLIMA = ['Templado', 'Húmedo', 'Frío', 'Lluvioso', 'Cálido'] 
        self.cbtipo_clima = wx.Choice(self.panel,choices = self.TIPO_CLIMA) 
        box.Add(self.cbtipo_clima,1,wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL,5) 
        
        #Configuración ComboBox para selección del Tipo de Viaje
        self.lbtipo_viaje = wx.StaticText(self.panel,label = "Tipo Viaje",style = wx.ALIGN_CENTRE) 
        box.Add(self.lbtipo_viaje,0,wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL,5) 
        
        
        
        #--------------------------------------------------------------------------
        
        
        
        # Creando información de ComboBox con datos de la base de datos
        self.TIPO_VIAJE = []
        
        query = "match (tViaje:Tipo_Viaje) return tViaje.titulo  order by tViaje.titulo"
        
        dato = ControladorGrafo.ExecQuery(query)
        
        for record in dato:
            self.TIPO_VIAJE.append(record[0])
        
        
        
        #self.TIPO_VIAJE = ['Amigos/as', 'Familia', 'Solo']
        self.cbtipo_viaje = wx.Choice(self.panel,choices = self.TIPO_VIAJE) 
        box.Add(self.cbtipo_viaje,1,wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL,5) 
        
        #Configuración ComboBox para selección del Tipo de Turismo
        self.lbtipo_turismo= wx.StaticText(self.panel,label = "Tipo Turismo",style = wx.ALIGN_CENTRE) 
        box.Add(self.lbtipo_turismo,0,wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL,5) 
        
        
        #--------------------------------------------------------------------------
        
        # Creando información de ComboBox con datos de la base de datos
        self.TIPO_TURISMO = []
        
        query = "match (tTurismo:Tipo_Turismo) return tTurismo.titulo  order by tTurismo.titulo"
        
        dato = ControladorGrafo.ExecQuery(query)
        
        for record in dato:
            self.TIPO_TURISMO.append(record[0])
                
        
        #self.TIPO_TURISMO = ['Aventura', 'Arqueológico', 'Ecoturismo']
        self.cbtipo_turismo = wx.Choice(self.panel,choices = self.TIPO_TURISMO) 
        box.Add(self.cbtipo_turismo,1,wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL,5)
        
        
        #--------------------------------------------------------------------------
        
        #Configuración ComboBox para selección de Presupuesto
        self.lbtipo_turismo= wx.StaticText(self.panel,label = "Tipo Presupuesto",style = wx.ALIGN_CENTRE) 
        box.Add(self.lbtipo_turismo,0,wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL,5) 
        
        PRESUPUESTO = ['Q', 'QQ', 'QQQ','QQQQ']
        self.cbpresupuesto = wx.Choice(self.panel,choices = PRESUPUESTO) 
        box.Add(self.cbpresupuesto,1,wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL,5)
        
        #Agregando campo para ingreso del nombre del nuevo lugar
        
        self.lbnombre_nodo= wx.StaticText(self.panel,label = "Nombre Lugar Turistico",style = wx.ALIGN_CENTRE) 
        box.Add(self.lbnombre_nodo,0,wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL,5) 
        
        
        self.tblugar_turistico = wx.TextCtrl(self.panel)
        box.Add(self.tblugar_turistico,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5) 
        
        
        #--------------------------------------------------------------------------
        
        # Agregamos botón para consulta
        self.btconsulta = wx.Button(self.panel,-1,"Crear Nodo") 
        box.Add(self.btconsulta,0,wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL,5) 
        
        
        # Configuramos Eventos
        box.AddStretchSpacer() 
        
        self.cbpresupuesto.SetSelection(1)
        
        self.btconsulta.Bind(wx.EVT_BUTTON,self.createNode) 
        
        if(not self.cbtipo_clima.IsEmpty()):
            self.cbtipo_clima.SetSelection(0)
        
        if(not self.cbtipo_viaje.IsEmpty()):
            self.cbtipo_viaje.SetSelection(0)
        
        if(not self.cbtipo_turismo.IsEmpty()):
            self.cbtipo_turismo.SetSelection(0)
        
        if(not self.cbmunicipio.IsEmpty()):
            self.cbmunicipio.SetSelection(0)
		
        self.panel.SetSizer(box) 
        self.Centre() 
        self.Show() 
    
    def createNode(self,event):
        
        control = True
        clima = ""
        tipo_viaje = ""
        tipo_turismo = ""
        presupuesto = ""
        nombre_nodo = ""
        
        #print(self.TIPO_CLIMA[self.cbtipo_clima.GetSelection()])
        if(self.cbtipo_clima.GetSelection() < 0 and control):
            control = control and False
            wx.MessageBox('Debe seleccionar un Tipo de Clima', 'Falta Información', wx.OK | wx.ICON_INFORMATION)
        else:
            clima =  self.cbtipo_clima.GetString(self.cbtipo_clima.GetSelection())
            
        if(self.cbtipo_viaje.GetSelection() < 0 and control):
            control = control and False
            wx.MessageBox('Debe seleccionar un Tipo de Viaje', 'Falta Información', wx.OK | wx.ICON_INFORMATION)
        else:
            tipo_viaje =  self.cbtipo_viaje.GetString(self.cbtipo_viaje.GetSelection())
            
        if(self.cbtipo_turismo.GetSelection() < 0 and control):
            control = control and False
            wx.MessageBox('Debe seleccionar un Tipo de Turismo', 'Falta Información', wx.OK | wx.ICON_INFORMATION)
        else:
            tipo_turismo = self.cbtipo_turismo.GetString(self.cbtipo_turismo.GetSelection())
        
        if(self.cbpresupuesto.GetSelection() < 0 and control):
            control = control and False
            wx.MessageBox('Debe seleccionar un Presupuesto', 'Falta Información', wx.OK | wx.ICON_INFORMATION)
        else:
            presupuesto = self.cbpresupuesto.GetString(self.cbpresupuesto.GetSelection())
        
        if(self.tblugar_turistico.GetValue() == ""):
            control = control and False
            wx.MessageBox('Debe seleccionar un el Nombre del Nodo', 'Falta Información', wx.OK | wx.ICON_INFORMATION)
        else:
            nombre_nodo = self.tblugar_turistico.GetValue()
        
        if(control):
            print("ingreso nodo")
            
            # Verificamos si existe el nódo
            query = 'match (turismo:Turismo) where turismo.Lugar =~ "(?i).*{0}.*" return turismo.Lugar'.format(nombre_nodo)
            
            datos = ControladorGrafo.ExecQuery(query)
            
            coincidencias = 0
            for record in datos:
                if(record[0] != ""):
                    coincidencias += 1
            
            if(coincidencias == 0):
                
                
                #creamos nódo
                nodo = nombre_nodo.replace(" ","").upper()
                
                query = 'CREATE (%s:Turismo {Lugar: "%s", Presupuesto: "%s"})' % (nodo,nombre_nodo,presupuesto)
                ControladorGrafo.ExecQuery(query)
                
                
                query = 'match (turismo:Turismo) where turismo.Lugar = "{0}" return id(turismo)'.format(nombre_nodo)
                datos = ControladorGrafo.ExecQuery(query)
                
                idNewNode = -1
                for record in datos:
                    if(idNewNode == -1):
                        idNewNode = record[0]
                
                #Se crea relación con clima
                query = 'MATCH (clima:Clima {titulo: "%s"}),(turismo:Turismo) WHERE id(turismo) = %d create (clima)-[:TIENE_CLIMA {roles:["Clima Lugar"]}]->(turismo) RETURN * ' % (clima,idNewNode) 
                
                ControladorGrafo.ExecQuery(query)
                
                
                #Se crea relación con tipo de viaje
                query = 'MATCH (tViaje:Tipo_Viaje {titulo: "%s"}),(turismo:Turismo) WHERE id(turismo) = %d create (tViaje)-[:CATEGORIA_VIAJE {roles:["Categoria Viaje"]}]->(turismo) RETURN * ' % (tipo_viaje,idNewNode)
                                
                ControladorGrafo.ExecQuery(query)
                
                
                
                self.tblugar_turistico.SetValue("") 
                
                wx.MessageBox('Se a creado el Lugar turistico y sus relaciones.', 'Creación de Nodo', wx.OK | wx.ICON_INFORMATION)
                
            else:
                wx.MessageBox('El nodo ya existe', 'Creación de Nodo', wx.OK | wx.ICON_INFORMATION)

"""
app = wx.App() 
lugarTuristico(None,  'Ingreso de Lugar Turistico') 
app.MainLoop()
"""