def saludo(veces:int):
    if veces > 0:
        for x in range(veces):
            print("\tBienvenido al Programa !!!")
    print("\n")

def saludar_personas(nombre : list[str] | None=""):
    for i in range(len(nombre)):
        nombre[i] = nombre[i].capitalize()
        print(f"\tBienvenido al Programa {nombre[i]} !!!")
    return nombre

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

nombre  = ["Administrador","juan", "pedro", "luis", "Ana", "Jose"]

#print(*nombre,"\n")
#saludar_personas(nombre)
#print(*nombre)
dni = []
opc = 0
i = 0
veces = 0
saludo(veces)
while (opc != 3):
#    print ("\tOpciones:","---------","1-Agregar","2-Mostrar","3-Salir", sep="\n\t")
#    opc = input("\tTu Opcion : ")
#    if (opc.isdigit()): 
#        opc = int(opc)
        opc = menu_opciones("Ingreso de DNI", ["Agregar","Mostrar","Salir"],3,1,nombre[0])
        if opc==1:
            i += 1
            valor_dni = int(input(f"\n{i} Ingrese DNI :"))
            if valor_dni in dni:
                print(f"\nEl DNI {valor_dni} ya fue ingresado\n")
            else:
                dni.append(valor_dni)
                dni.sort()
        elif opc==2:
            if dni==[]:
                print("\nNo hay informacion cargada aun !!!!\n")
            else:
                print("\nDNI Ingresados : ",*dni,sep="\n\t")
        elif opc==3:
            print("\nHasta Pronto\n")
