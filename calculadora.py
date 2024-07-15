#Calculadora
print ("\n")
num_1 = float(input("Ingresa El Primer  Numero :"))
num_2 = float(input("Ingresa El Segundo Numero :"))
print("\nOperaciones Disponibles")
print("\t1-Sumar Ambos numeros")
print("\t2-Restar Numeros")
print("\t3-Multiplicar Numeros")
print("\t4-Dividir numeros")
print("\t5-Division entera")
opcion = int(input("\tTu opcion : "))
if  opcion == 1:
    texto = "La suma : "
    operacion = "+"
    resultado = num_1 + num_2
elif opcion == 2:
    texto = "La resta : "
    operacion = "-"
    resultado = num_1 - num_2
elif opcion == 3:
    texto = "La multiplicacion : "
    operacion = "*"
    resultado = num_1 * num_2
elif opcion == 4:
    if (num_2 != 0):
        texto = "La division : "
        operacion = "/"
        resultado = num_1 / num_2
    else:
        texto = "No se puede dividir por cero"
        resultado = "Error => division por cero"
        operacion = ""
elif opcion == 5:
    if (num_2 != 0):
        texto = "La division : "
        operacion = "//"
        resultado = num_1 // num_2
    else:
        texto = "No se puede dividir por cero"
        resultado = "Error => division por cero"
        operacion = ""
else:
    texto = "ERROR en opcion"
    resultado = ""

if resultado != "": 
    print (f"\n\n{texto} {num_1} {operacion} {num_2} = {resultado}")
else:
    print (f"\n\n{texto}")
