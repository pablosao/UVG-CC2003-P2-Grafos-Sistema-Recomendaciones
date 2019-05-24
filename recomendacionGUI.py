# -*- coding: utf-8 -*-
"""
Created on Thu May 23 23:58:54 2019

@author: pablo
"""

import wx
import ControladorGrafo

class Mywin(wx.Frame): 
    
    
    
    def __init__(self, parent, title): 
        
        
        
                
        super(Mywin, self).__init__(parent, title = title,size = (320,370)) 
		
        panel = wx.Panel(self) 
        box = wx.BoxSizer(wx.VERTICAL) 
        
        #Texto Inicial
        self.label = wx.StaticText(panel,label = "Recomendacion" ,style = wx.ALIGN_CENTRE) 
        box.Add(self.label, 0 , wx.EXPAND |wx.ALIGN_CENTER_HORIZONTAL |wx.ALL, 20) 
        
        #Configuración ComboBox para selección de Clima
        lbtipo_clima = wx.StaticText(panel,label = "Escoja Clima",style = wx.ALIGN_CENTRE) 
        box.Add(lbtipo_clima,0,wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL,5) 
        
        
        # Creando información de ComboBox con datos de la base de datos
        self.TIPO_CLIMA = []
        
        query = "match (clima:Clima) return clima.titulo  order by clima.titulo"
        
        dato = ControladorGrafo.ExecQuery(query)
        
        for record in dato:
            self.TIPO_CLIMA.append(record[0])
        
        
        #self.TIPO_CLIMA = ['Templado', 'Húmedo', 'Frío', 'Lluvioso', 'Cálido'] 
        self.cbtipo_clima = wx.Choice(panel,choices = self.TIPO_CLIMA) 
        box.Add(self.cbtipo_clima,1,wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL,5) 
        
        #Configuración ComboBox para selección del Tipo de Viaje
        self.lbtipo_viaje = wx.StaticText(panel,label = "Tipo Viaje",style = wx.ALIGN_CENTRE) 
        box.Add(self.lbtipo_viaje,0,wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL,5) 
        
        
        # Creando información de ComboBox con datos de la base de datos
        self.TIPO_VIAJE = []
        
        query = "match (tViaje:Tipo_Viaje) return tViaje.titulo  order by tViaje.titulo"
        
        dato = ControladorGrafo.ExecQuery(query)
        
        for record in dato:
            self.TIPO_VIAJE.append(record[0])
        
        
        
        #self.TIPO_VIAJE = ['Amigos/as', 'Familia', 'Solo']
        self.cbtipo_viaje = wx.Choice(panel,choices = self.TIPO_VIAJE) 
        box.Add(self.cbtipo_viaje,1,wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL,5) 
        
        #Configuración ComboBox para selección del Tipo de Turismo
        self.lbtipo_turismo= wx.StaticText(panel,label = "Tipo Turismo",style = wx.ALIGN_CENTRE) 
        box.Add(self.lbtipo_turismo,0,wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL,5) 
        
        
        
        # Creando información de ComboBox con datos de la base de datos
        self.TIPO_TURISMO = []
        
        query = "match (tTurismo:Tipo_Turismo) return tTurismo.titulo  order by tTurismo.titulo"
        
        dato = ControladorGrafo.ExecQuery(query)
        
        for record in dato:
            self.TIPO_TURISMO.append(record[0])
                
        
        #self.TIPO_TURISMO = ['Aventura', 'Arqueológico', 'Ecoturismo']
        self.cbtipo_turismo = wx.Choice(panel,choices = self.TIPO_TURISMO) 
        box.Add(self.cbtipo_turismo,1,wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL,5)
        
        
        #Configuración ComboBox para selección de Presupuesto
        self.lbtipo_turismo= wx.StaticText(panel,label = "Tipo Presupuesto",style = wx.ALIGN_CENTRE) 
        box.Add(self.lbtipo_turismo,0,wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL,5) 
        
        PRESUPUESTO = ['Q', 'QQ', 'QQQ','QQQQ']
        self.cbpresupuesto = wx.Choice(panel,choices = PRESUPUESTO) 
        box.Add(self.cbpresupuesto,1,wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL,5)
        
        
        # Agregamos botón para consulta
        self.btconsulta = wx.Button(panel,-1,"Obtener Recomendación") 
        box.Add(self.btconsulta,0,wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL,5) 
        
        
        # Configuramos Eventos
        box.AddStretchSpacer() 
        
        self.cbpresupuesto.SetSelection(1)
        
        self.btconsulta.Bind(wx.EVT_BUTTON,self.getConsulta) 
        
        if(not self.cbtipo_clima.IsEmpty()):
            self.cbtipo_clima.SetSelection(0)
        
        if(not self.cbtipo_clima.IsEmpty()):
            self.cbtipo_viaje.SetSelection(0)
        
        if(not self.cbtipo_clima.IsEmpty()):
            self.cbtipo_turismo.SetSelection(0)
        
        
        
		
        panel.SetSizer(box) 
        self.Centre() 
        self.Show() 
    
    def getConsulta(self,event):
        
        control = True
        clima = ""
        tipo_viaje = ""
        tipo_turismo = ""
        presupuesto = ""
        
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

        if(control):
           print(clima)
        
        
    def OnCombo(self, event): 
        #self.label.SetLabel("You selected"+self.combo.GetValue()+" from Combobox") 
        self.label.SetLabel("You selected from Combobox") 
		
    def OnChoice(self,event): 
        self.label.SetLabel("You selected from Combobox") 
        #self.label.SetLabel("You selected "+ self.choice.GetString
        # (self.choice.GetSelection())+" from Choice") 
        

                             
app = wx.App() 
Mywin(None,  'Recomendación Turistica') 
app.MainLoop()
