print ("\n")
edad = float(input("\nIngresa tu edad :"))

if edad < 0: 
    print (f"\nTu edad es incorrecta")
elif edad >= 18:
    print(f"tu edad {edad} es correcta")
else:
    print ("Eres menor de edad")
