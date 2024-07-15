lista_1 = [1, 2, 3, 4, 5]
lista_2 = lista_1
print (f"Lista 1 = {lista_1}")
lista_1.append(6)
print (f"Lista 1 = {lista_1}")
print (f"Lista 2 = {lista_2}")
lista_3 = lista_2.copy()
lista_3.append(6)
lista_3.append(8)
print (f"Lista 3 = {lista_3}")
print ("\n")

# tupla ()
tupla_1 = (1, 2, 3, 4, 5)
print (f"Tupla 1 = {tupla_1}")
print(type(tupla_1))
print ("\n")

# set
set_1 = {"valor1", "valor2", "valor3"}
print (f"Set 1 = {set_1}")
print(type(set_1))
print ("\n")

# Diccionario
empleados = {"nombre":"Sergio", "edad":56}
print("Empleado : ",empleados.get("nombre"))
print("Edad     : ",empleados.get("edad"))

productos = { 
            "779000000012345" : {"Nombre":"Arroz Gallo Oro", "Precio":3220}
            }
