#Programa solicita ingreso de usuario

import ControladorGrafo

#Condiciones
tclimas = ['Calido', 'Frio', 'Humedo', 'Lluvioso', 'Templado']
tpresupuesto = ['Q', 'QQ', 'QQQ', 'QQQQ']
tturismo = ['Agroturismo', 'Arqueologico', 'Aventura', 'Comunitario', 'Cultural', 'Deportivo', 'Ecoturismo', 'Etnoturismo', 'Gastronomico', 'Religioso']
tviaje = ['Amigos/as', 'Familiar', 'Solo']

def menu():

    #Menu Principal
    print('\tMenu')
    print('\n1. Crear Base de Datos')
    print('\n2. Consultar')

    #Ingreso usuario
    op1 = input('\nIngrese una opcion: ')

    if op1 == '1' :

        #Crea base de datos
        print('\nInicializando DB')
        ControlGrafo.CreateDataBase()
        print('\nDB creada')

    elif op1 == '2':

        #Llama def ingreso para ingresar los datos
        ingreso()

def ingreso ():

    #Ingreso de clima
    ingresoClima()
    ingresoPresupuesto()
    ingresoTurismo()
    ingresoViaje()

def ingresoClima():

    #Ingreso de clima
    ctr = 1
    print('\n\n\tTipo de clima')
    for field in tclimas:
        print ('\n' + ctr + '. ' + field)
        ctr +=1

    #Seleccionar clima    
    op2 = input('\nIngrese una opcion: ')

    if op2 == '1':
        climaSel = tclima[0]
    elif op2 == '2':
        climaSel = tclima[1]
    if op2 == '3':
        climaSel = tclima[2]
    elif op2 == '4':
        climaSel = tclima[3]
    elif op2 == '5':
        climaSel = tclima[4]
    elif:
        print ('\nERROR: Opcion ingresada no es valida')
        ingresoClima()

    return climaSel

def ingresoPresupuesto():

    #Ingreso Presupuesto
    ctr = 1
    print('\n\n\tPresupuesto')
    for field in tpresupuesto:
        print ('\n' + ctr + '. ' + field)
        ctr +=1

    #Seleccionar Presupuesto    
    op2 = input('\nIngrese una opcion: ')

    if op2 == '1':
        presuSel = tpresupuesto[0]
    elif op2 == '2':
        presuSel = tpresupuesto[1]
    elif op2 == '3':
        presuSel = tpresupuesto[2]
    elif op2 == '4':
        presuSel = tpresupuesto[3]
    elif:
        print ('\nERROR: Opcion ingresada no es valida')
        ingresoPresupuesto()

    return presuSel

def ingresoTurismo():

    #Ingreso Turismo
    ctr = 1
    print('\n\n\tTurismo')
    for field in tturismo:
        print ('\n' + ctr + '. ' + field)
        ctr +=1

    #Seleccionar turismo    
    op2 = input('\nIngrese una opcion: ')

    if op2 == '1':
        turiSel = tturismo[0]
    elif op2 == '2':
        turiSel = tturismo[1]
    elif op2 == '3':
        turiSel = tturismo[2]
    elif op2 == '4':
        turiSel = tturismo[3]
    elif op2 == '5':
        turiSel = tturismo[4]
    elif op2 == '6':
        turiSel = tturismo[5]
    elif op2 == '7':
        turiSel = tturismo[6]
    elif op2 == '8':
        turiSel = tturismo[7]
    elif op2 == '9':
        turiSel = tturismo[8]
    elif op2 == '10':
        turiSel = tturismo[9]
    elif:
        print ('\nERROR: Opcion ingresada no es valida')
        ingresoTurismo()

    return turiSel

def ingresoViaje():
    
    #Ingreso Viaje
    ctr = 1
    print('\n\n\tTurismo')
    for field in tviaje:
        print ('\n' + ctr + '. ' + field)
        ctr +=1
    #Seleccionar viaje    
    op2 = input('\nIngrese una opcion: ')

    if op2 == '1':
        viajeSel = tviaje[0]
    elif op2 == '2':
        viajeSel = tviaje[1]
    elif op2 == '3':
        viajeSel = tviaje[2]
    elif:
        print ('\nERROR: Opcion ingresada no es valida')
        ingresoTurismo()

    return viajeSel
