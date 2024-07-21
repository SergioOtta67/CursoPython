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
