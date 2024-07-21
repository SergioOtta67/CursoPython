class Persona:
    def __init__(self, 
                 nombre: str, 
                 edad: int, 
                 sexo: bool, 
                 dni: int) -> None:
        self._nombre = nombre
        self._edad   = edad
        self._sexo   = sexo
        self._dni    = dni

    def mostrar_info_persona(self) -> None:
        sexo_dato = "Masculino" if self._sexo else "Femenino"
        dni = f"{self._dni:,}".replace(",", ".")
        print(f"Nombre  : {self._nombre:20}\nEdad    : {self._edad:3}\nSexo    : {sexo_dato:12}\nDNI     : {dni:15}\n")

class Empleado(Persona):
    def __init__ ( self, 
                  legajo : str, 
                  nombre : str, 
                  edad : int, 
                  sexo : bool, 
                  dni : int, 
                  trabaja : bool, 
                  sueldo : float) -> None:
        super().__init__(nombre, edad, sexo, dni)
        self._legajo  = legajo
        self._trabaja = trabaja
        self._sueldo  = sueldo
        
    def mostrar_info(self) -> None:
        sexo_dato    = "Masculino" if self._sexo else "Femenino"
        estado       = "En Actividad" if self._trabaja else ">> INACTIVO <<"
        sueldo_info  = f"{self._sueldo:,.2f}"
        sueldo_info  = sueldo_info.replace(",", "X").replace(".", ",").replace("X", ".")
        dni = f"{self._dni:,}".replace(",", ".")
        print(f"Legajo  : {self._legajo:5}\nNombre  : {self._nombre:20}\nEdad    : {self._edad:3}\nSexo    : {sexo_dato:12}\nDNI     : {dni:15}\nSueldo  : {sueldo_info:15}\nEstado  : {estado}\n\n")
        
    def mostrar_info_renglon(self) -> None:
        sexo_dato    = "Masculino" if self._sexo else "Femenino"
        estado       = "En Actividad" if self._trabaja else ">> INACTIVO <<"
        sueldo_info  = f"{self._sueldo:,.2f}"
        sueldo_info  = sueldo_info.replace(",", "X").replace(".", ",").replace("X", ".")
        sueldo_info  = "***************" + sueldo_info
        dni = f"{self._dni:,}".replace(",", ".")
        #Reemplazar las comas por puntos y los puntos por comas
        print(f"  {self._legajo}     {self._nombre:15} {self._edad:3}   {sexo_dato:12} {dni:15} {sueldo_info[-15:]}    {estado}")
        
    def mostrar_sueldo(self) -> float:
        return self._sueldo
    
    def subir_sueldo(self, porcentaje : float) -> float:
        self._sueldo *= 1 + (porcentaje/100)
    
empleados_lista =   [
                ("001", "Jose Luis", 25, True,  42333111, True,     433000.15),
                ("002", "Pablo",     66, True,  15324567, False,    145000.00),
                ("003", "Ana Maria", 32, False, 55001123, True,     675090.88)
                    ]

print("\nEmpleados En Actividad : \n")

espacio  = " "
milista = []
#print(f"Legajo    Nombre         Edad      Sexo         DNI {espacio*13} Sueldo {espacio*9} Estado")
for value in empleados_lista:
    #if value[5]:
        miempleado = Empleado(value[0], value[1], value[2], value[3], value[4], value[5], value[6])
        #miempleado.mostrar_info_renglon()
        milista.append(miempleado)
print("\n\n")
largo = len(milista)
#print(f"el largo es : {largo}")
print("\nInformación de los empleados en la lista:")
print(f"Legajo    Nombre         Edad      Sexo         DNI {espacio*13} Sueldo {espacio*9} Estado")
for empleado in milista:
    empleado.mostrar_info_renglon()
print("\n\nInformación de las personas en la lista:")
for lapersona in milista:
    lapersona.mostrar_info_persona()
