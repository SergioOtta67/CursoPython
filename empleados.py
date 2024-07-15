legajo  = [11, 21, 31, 41, 51]
nombre  = ["Juan", "Pedro", "Luis", "Ana", "Jose"]
edad    = [50, 43, 28, 33, 21]
sexo    = ["Masculino", "Masculino", "Masculino", "Masculino", "Femenino", "Masculino"]
dni     = [12340111, 56780123, 90120433, 34560334, 78909001]
trabaja = [0, 1, 1, 1, 1]

# empresa = dict(zip(id, nombre))
i = 0
empleado = [0,1,2,3,4]
empleados_empresa = {}
while i < 5:
        empleado[i] = (legajo[i], nombre[i], edad[i], sexo[i], dni[i], trabaja[i])
        empleados_empresa = dict.update ({legajo[i] : (nombre[i], edad[i], sexo[i], dni[i], trabaja[i])})
        i = i + 1

i = 0
while i < 5:
        print(f"Empleado {i+1} : ",empleado[i])
        i = i + 1

print ("\n\n")
print(f" Empleados Empresa :\n{empleado}", sep="\n")
# legajo = int(input("Legajo a buscar :"))
buscar = legajo.index(int(input("Legajo a buscar :")))
encuentro = empleado[buscar]
print(f"Empleado ID = {buscar} sus valores son {encuentro}\n\n")
print (f"Empleados Empresa :\n{empleados_empresa.items()}", sep="\n")