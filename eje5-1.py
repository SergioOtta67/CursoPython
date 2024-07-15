inventario = ["Manzana", "Sandia", "Banana"]
print (f"\nNuestro Inventario Inicial es : {inventario}\n\n")

opc = 0;
while (opc != 4):
    print ("\tOpciones:","---------","1-Agregar","2-Eliminar","3-Mostrar","4-Salir", sep="\n\t")
    opc = input("\tTu Opcion : ")
    if (opc.isdigit): 
        opc = int(opc)
    if opc==1:
        fruta = input("\nIngresa una Fruta para agregar : ").capitalize()
        if fruta not in inventario:
            inventario.append(fruta) 
            inventario.sort()
        else:
            print(f"la fruta '{fruta}' ya está en el inventario")
    elif opc == 2:
        borrar = input("Ingresa una fruta para borrar : ").capitalize()
        inventario.remove(borrar) if borrar in inventario else print("Fruta no encontrada")
    elif opc == 3:
        print ("\nNuestro Inventario Ordenado es :", *inventario, sep="\n")
        print("\n")
    elif opc == 4:
        print ("\n\nHasta Pronto")
    else:
        opc = ""
        print("\n\nOpción Erronea")
