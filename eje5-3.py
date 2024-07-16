# librerias es librerias.py donde tengo todas mis funciones
# que voy a poder usar en distintos programas de python
# menu_ppal es el nombre local que voy a usar 
# en el archivo librerias.py la funcion se llama menu_func
# localmente se debe llamar => menu_ppal.menu_func
#
import librerias as menu_ppal


empleados = {
                "001" : ("Jose Luis", 25, True,  42333111, True),
                "002" : ("Pablo",     66, True,  15324567, False),
                "003" : ("Ana Maria", 32, False, 55001123, True)
            }
copia = []
print(f"\n\nlongitud de Copia : {menu_ppal.largo_dato(5, copia)}")

opc = 0
i   = len(empleados)
print("\n"*10)
usuario = "Administrador"
opciones = ["Agregar","Mostrar","Mostrar Activos","Salir"]
while True:
    opc = menu_ppal.menu_func("Ingreso de Empleados", opciones, 4 , 1, usuario)
    if opc==1:
        id = input(f"\n{i+1} Ingrese ID :")
        if id in empleados:
            print(f"\nEl ID {id} ya fue ingresado\n")
        else:
            i += 1
            info_empleado = menu_ppal.ingreso_empleado(id)
            empleados.update( info_empleado )
    elif opc==2:
        if len(empleados)==0:
            print("\nNo hay informacion cargada aun !!!!\n")
        else:
            print("\nEmpleados Ingresados : ")
            for key, value in empleados.items():
                dni = f"{value[3]:,}".replace(",", ".")
                nombre = value[0].capitalize()
                sexo = "Masculino" if value[2] else "Femenino"
                estado = "En Actividad" if value[4] else "INACTIVO"
                nada = " "*5
                print(f"ID: {key:10} Nombre: {nombre:20} Edad: {value[1]:3} {nada} Sexo: {sexo:15} DNI: {dni:15} Estado: {estado}")
    elif opc==3:
        if len(empleados)==0:
            print("\nNo hay informacion cargada aun !!!!\n")
        else:
            print("\nEmpleados En Actividad : ")
            for key, value in empleados.items():
                if value[4]:
                    dni = f"{value[3]:,}".replace(",", ".")
                    nombre = value[0].capitalize()
                    sexo = "Masculino" if value[2] else "Femenino"
                    nada = " "*5
                    print(f"ID: {key:10} Nombre: {nombre:20} Edad: {value[1]:3} {nada} Sexo: {sexo:15} DNI: {dni:15}")
    elif opc==4:
        print(f"\nHasta Pronto {usuario.capitalize()}\n")
        break
