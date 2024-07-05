frase = input("\nIngresa una frase :")
palabra = input("Ingresa una palabra a buscar : ")

if palabra in frase:
    print("Palabra Encontrada")
else:
    print(f"No se encuentra la palabra {palabra}")