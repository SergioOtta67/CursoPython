dni = []
i = 0
tope = 5
while (i < tope):
    valor_dni = int(input(f"{i+1} Ingrese DNI :"))
    if valor_dni in dni:
        print(f"El DNI {valor_dni} ya fue ingresado")
    else:
        dni.append(valor_dni)
        i += 1
dni.sort()
print(f"La lista de DNI es {dni}")
