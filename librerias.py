#titulo     : nombre del menú
#opciones   : lista str de las opciones que se van a imprimir
#sale       : opcion para salir del menu
#tab        : para poner tabulacion 0:no 1:si
#usuario    : nombre del usuario del menu
#return opc : es la opcion seleccionada por el usuario
#
#     SALIDA ESPERADA:::
#
#  MENU: Ingreso de Empleados ** Administrador **
#  ----------------------------------------------
#          1-Agregar
#          2-Mostrar
#          3-Mostrar Activos
#          4-Salir
#          Tu Opcion : 
def menu_func(titulo : str, opciones : list[str], sale : int, tab : int, usuario : str) -> int:
    mostrar = f"MENU: {titulo} ** {usuario.capitalize()} **"
    print (f"{mostrar}")
    print ("-"*(len(mostrar)))
    tope = len(opciones)
    for x in range(tope):
        if tab==1:
            print(f"\t{x+1}-{opciones[x]}")
        else:
            print(f"{x+1}-{opciones[x]}")
    opc = 0
    while True:
        opc = input("\tTu Opcion : ")
        if (opc.isdigit()): 
            opc = int(opc)
            if (opc>0 and opc<=sale):
                break
            elif (opc==0 or opc>sale):
                print("\nOpcion Incorrecta !!!!\n")
        else:
            print ("\nSeleccione solo numeros !!!!\n")
    return opc

def largo_dato(tipo_dato : int, dato_info : str) -> int:
    sale = len(dato_info)
    if tipo_dato==1 and len(dato_info)==0:
        sale = "Mi diccionario esta vacio"
    elif tipo_dato==2 and len(dato_info)==0:
        sale = "Mi lista esta vacia"
    elif tipo_dato==3 and len(dato_info)==0:
        sale = "Mi tupla esta vacia"
    elif tipo_dato==4 and len(dato_info)==0:
        sale = "Mi SET esta vacio"
    else:
        sale = f"Error en dato {dato_info} es del tipo {type(dato_info)}"
    return sale

def ingreso_empleado(id):
    nombre  = ""
    edad    = 0
    sexo    = ""
    dni     = 0
    trabaja = 9
    confirma = "N"
    largomax = 20
    while len(nombre)==0 or len(nombre) > largomax:
        nombre  =     input("Nombre   : ")
        if len(nombre)>largomax:
            nombre = nombre[:largomax]
            print(f"El nombre quedará : {nombre}")
            confirma = ""
            while confirma != "N" and confirma != "S":
                confirma = input("Confirma cortar el nombre ? S=SI N=NO : ")
            if confirma == "N":
                nombre = ""
    while edad < 1 or edad > 120:
        edad    = input("Edad     : ")
        if edad.isdigit(): 
            edad = int(edad) 
        else:
            edad = 0
            print ("Error en tipo de dato")
    while sexo != "Masculino" and sexo != "Femenino":
        sexo    =     input("Sexo     : ")
    sexo    = True if sexo == "Masculino" else False
    while dni <= 0 or dni >= 99000000:
        dni     = input("D.N.I.   : ")
        if dni.isdigit():
            dni = int(dni)
        else:
            dni = 0
            print ("Error en tipo de dato debe ser numerico > 0 y < 99.000.000")
    while trabaja < 0 or trabaja > 1:
        trabaja = input("Trabaja 0=NO 1=SI : ")
        if trabaja.isdigit():
            trabaja = int(trabaja)
        else:
            trabaja = 9
            print("Valor inválido")
    trabaja = bool(trabaja)
    agregar_empleado = { id : (nombre, edad, sexo, dni, trabaja) }
    return agregar_empleado
