# librerias es librerias.py donde tengo todas mis funciones
# que voy a poder usar en distintos programas de python
# lib es el nombre local que voy a usar 
# en el archivo librerias.py la funcion se llama menu_func
# localmente se debe llamar => lib.menu_func
#
import librerias as lib

empleados = {
                "001" : ("Jose Luis", 25, True,  42333111, True,  433000.15),
                "002" : ("Pablo",     66, True,  15324567, False, 145000.00),
                "003" : ("Ana Maria", 32, False, 55001123, True,  675090.88)
            }
opc = 0
i   = len(empleados)
print("\n"*10)
usuario = "Administrador"
opciones = ["Agregar","Mostrar","Mostrar Activos","Salir"]
while True:
    opc = lib.menu("Ingreso de Empleados", opciones, 4 , 1, usuario)
    if opc==1:
        id = input(f"\n{i+1} Ingrese ID :")
        if len(id)<3:
            #hago el formateo de los ultimos 3 caracteres
            id = lib.formatear_id(id, 3)

        if id in empleados:
            print(f"\nEl ID {id} ya está ingresado !!!!")
            nombre = empleados[id][0].capitalize()
            edad   = empleados[id][1]
            sexo = "Masculino" if empleados[id][2] else "Femenino"
            dni = f"{empleados[id][3]:,}".replace(",", ".")
            estado = "En Actividad" if empleados[id][4] else ">> INACTIVO <<"
            sueldo = f"{empleados[id][5]:,.2f}"
            sueldo = sueldo.replace(",", "X").replace(".", ",").replace("X", ".")
            print(f"Nombre  : {nombre:20}\nEdad    : {edad:3}\nSexo    : {sexo:12}\nDNI     : {dni:15}\nSueldo  : {sueldo:15}\nEstado  : {estado}\n\n")

        else:
            i += 1
            info_empleado = lib.ingreso_empleado(id)
            empleados.update( info_empleado )
    elif opc==2:
        if len(empleados)==0:
            print("\nNo hay informacion cargada aun !!!!\n")
        else:
            print("\nEmpleados Ingresados : \n")
            print("ID:       Nombre         Edad      Sexo         DNI            Sueldo        Estado")
            for key, value in empleados.items():
                sueldo = f"{value[5]:,.2f}"
                #Reemplazar las comas por puntos y los puntos por comas
                sueldo = sueldo.replace(",", "X").replace(".", ",").replace("X", ".")

                dni = f"{value[3]:,}".replace(",", ".")
                nombre = value[0].capitalize()
                sexo = "Masculino" if value[2] else "Femenino"
                estado = "En Actividad" if value[4] else ">> INACTIVO <<"
                print(f"ID: {key:5} {nombre:15} {value[1]:3}   {sexo:12} {dni:15} {sueldo:15} {estado}")
            print("\n\n")
    elif opc==3:
        if len(empleados)==0:
            print("\nNo hay informacion cargada aun !!!!\n")
        else:
            print("\nEmpleados En Actividad : \n")
            print("ID:       Nombre         Edad      Sexo         DNI            Sueldo")
            for key, value in empleados.items():
                if value[4]:
                    sueldo = f"{value[5]:,.2f}"
                    #Reemplazar las comas por puntos y los puntos por comas
                    sueldo = sueldo.replace(",", "X").replace(".", ",").replace("X", ".")

                    dni = f"{value[3]:,}".replace(",", ".")
                    nombre = value[0].capitalize()
                    sexo = "Masculino" if value[2] else "Femenino"
                    print(f"ID: {key:5} {nombre:15} {value[1]:3}   {sexo:12} {dni:15} {sueldo:15}")
            print("\n\n")
    elif opc==4:
        print(f"\nHasta Pronto {usuario.capitalize()}\n")
        break
