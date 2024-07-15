#titulo     : nombre del menú
#opciones   : lista str de las opciones que se van a imprimir
#sale       : opcion para salir del menu
#tab        : para poner tabulacion 0:no 1:si
#return opc : es la opcion seleccionada por el usuario
def menu_opciones(titulo : str, opciones : list[str], sale : int, tab : int, usuario : str):
    print (f"MENU: {titulo} ** {usuario.capitalize()} **")
    print ("-"*(len(titulo)+len(usuario)+14))
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


empleados = {
                "001" : ("Jose Luis", 25, True,  42333111, True),
                "002" : ("Pablo",     66, True,  15324567, False),
                "003" : ("Ana Maria", 32, False, 55001123, True)
            }


opc = 0
i   = len(empleados)
while True:
    opc = menu_opciones("Ingreso Empleado", ["Agregar","Mostrar","Mostrar Activos","Salir"],4,1,"Administrador")
    if opc==1:
        id = input(f"\n{i+1} Ingrese ID :")
        if id in empleados:
            print(f"\nEl ID {id} ya fue ingresado\n")
        else:
            i += 1
            nombre = input("Nombre: ")
            edad = int(input("Edad: "))
            sexo = input("Sexo: ")
            sexo = True if sexo == "Masculino" else False
            dni  = int(input("DNI: "))
            trabaja = bool( input("Trabaja 0 (no) 1 (si) : ") )
            agregar_empleado = { id : (nombre, edad, sexo, dni, trabaja) }
            empleados.update( agregar_empleado )
    elif opc==2:
        if empleados=={}:
            print("\nNo hay informacion cargada aun !!!!\n")
        else:
            print("\nEmpleados Ingresados : ")
            for key, value in empleados.items():
                dni = f"{value[3]:,}".replace(",", ".")
                nombre = value[0].capitalize()
                sexo = "Masculino" if value[2] else "Femenino"
                estado = "En Actividad" if value[4] else "INACTIVO"
                print(f"ID: {key}\n\tNombre: {nombre}, Edad: {value[1]}, Sexo: {sexo}, DNI: {dni}, Estado: {estado}")
    elif opc==3:
        if empleados=={}:
            print("\nNo hay informacion cargada aun !!!!\n")
        else:
            print("\nEmpleados En Actividad : ")
            for key, value in empleados.items():
                if value[4]:
                    dni = f"{value[3]:,}".replace(",", ".")
                    nombre = value[0].capitalize()
                    sexo = "Masculino" if value[2] else "Femenino"
                    print(f"ID: {key}\n\tNombre: {nombre}, Edad: {value[1]}, Sexo: {sexo}, DNI: {dni}")
    elif opc==4:
        print("\nHasta Pronto\n")
        break
