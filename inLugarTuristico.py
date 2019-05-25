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
   
        super(lugarTuristico, self).__init__(parent, title = title,size = (320,450))
        
        self.panel = wx.Panel(self) 
        box = wx.BoxSizer(wx.VERTICAL) 
        
        #Texto Inicial
        self.titulo = wx.StaticText(self.panel,label = "Recomendacion" ,style = wx.ALIGN_CENTRE) 
        box.Add(self.titulo, 0 , wx.EXPAND |wx.ALIGN_CENTER_HORIZONTAL |wx.ALL, 20) 
        
                
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
        
        
        
        # Creando información de ComboBox con datos de la base de datos
        self.TIPO_TURISMO = []
        
        query = "match (tTurismo:Tipo_Turismo) return tTurismo.titulo  order by tTurismo.titulo"
        
        dato = ControladorGrafo.ExecQuery(query)
        
        for record in dato:
            self.TIPO_TURISMO.append(record[0])
                
        
        #self.TIPO_TURISMO = ['Aventura', 'Arqueológico', 'Ecoturismo']
        self.cbtipo_turismo = wx.Choice(self.panel,choices = self.TIPO_TURISMO) 
        box.Add(self.cbtipo_turismo,1,wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL,5)
        
        
        #Configuración ComboBox para selección de Presupuesto
        self.lbtipo_turismo= wx.StaticText(self.panel,label = "Tipo Presupuesto",style = wx.ALIGN_CENTRE) 
        box.Add(self.lbtipo_turismo,0,wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL,5) 
        
        PRESUPUESTO = ['Q', 'QQ', 'QQQ','QQQQ']
        self.cbpresupuesto = wx.Choice(self.panel,choices = PRESUPUESTO) 
        box.Add(self.cbpresupuesto,1,wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL,5)
        
        #Agregando campo para ingreso del nombre del nuevo lugar
        
        self.lbnombre_nodo= wx.StaticText(self.panel,label = "Nombre Lugar Turistico",style = wx.ALIGN_CENTRE) 
        box.Add(self.lbnombre_nodo,0,wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL,5) 
        
        
        self.t1 = wx.TextCtrl(self.panel)
        box.Add(self.t1,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5) 
        
        
        
        # Agregamos botón para consulta
        self.btconsulta = wx.Button(self.panel,-1,"Obtener Recomendación") 
        box.Add(self.btconsulta,0,wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL,5) 
        
        
        # Configuramos Eventos
        box.AddStretchSpacer() 
        
        self.cbpresupuesto.SetSelection(1)
        
        self.btconsulta.Bind(wx.EVT_BUTTON,self.getConsulta) 
        
        if(not self.cbtipo_clima.IsEmpty()):
            self.cbtipo_clima.SetSelection(0)
        
        if(not self.cbtipo_viaje.IsEmpty()):
            self.cbtipo_viaje.SetSelection(0)
        
        if(not self.cbtipo_turismo.IsEmpty()):
            self.cbtipo_turismo.SetSelection(0)
		
        self.panel.SetSizer(box) 
        self.Centre() 
        self.Show() 
    
    def getConsulta(self,event):
        
        print("ingreso nodo")
        
        
   
        
        
app = wx.App() 
lugarTuristico(None,  'Ingreso de Lugar Turistico') 
app.MainLoop()
