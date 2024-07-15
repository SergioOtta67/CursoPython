inventario = ["manzana", "sandia", "banana"]
print (f"\nNuestro Inventario es : {inventario}")
fruta = input("\nIngresa una Fruta para agregar : ")
inventario.append(fruta)
print (f"\nNuestro Inventario Ahora es : {inventario}")
borrar = input("Ingresa una fruta para borrar : ")
inventario.remove(borrar) if borrar in inventario else print("Fruta no encontrada")
inventario.sort()
print (f"\nNuestro Inventario Ordenado es : {inventario}")

