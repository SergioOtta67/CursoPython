class Empleado():
    def __init__ ( self, 
                  legajo : str, 
                  nombre : str, 
                  edad : int, 
                  sexo : bool, 
                  dni : int, 
                  trabaja : bool, 
                  sueldo : float) -> None:
        self._legajo  = legajo
        self._nombre  = nombre
        self._edad    = edad
        self._sexo    = sexo
        self._dni     = dni
        self._trabaja = trabaja
        self._sueldo  = sueldo
        
    def mostrar_info(self) -> None:
        sexo_dato    = "Masculino" if self._sexo else "Femenino"
        estado       = "En Actividad" if self._trabaja else ">> INACTIVO <<"
        print(f"Legajo  : {self._legajo:5}\nNombre  : {self._nombre:20}\nEdad    : {self._edad:3}\nSexo    : {sexo_dato:12}\nDNI     : {self._dni:15}\nSueldo  : {self._sueldo:15}\nEstado  : {estado}\n\n")
        
    def mostrar_info_renglon(self) -> None:
        sexo_dato    = "Masculino" if self._sexo else "Femenino"
        estado       = "En Actividad" if self._trabaja else ">> INACTIVO <<"
        sueldo_info = f"{self._sueldo:,.2f}"
        #Reemplazar las comas por puntos y los puntos por comas
        sueldo_info = sueldo_info.replace(",", "X").replace(".", ",").replace("X", ".")
        print(f"ID: {self._legajo:5} {self._nombre:15} {self._edad:3}   {sexo_dato:12} {self._dni:15} {sueldo_info:15} {estado}")
        
    def mostrar_sueldo(self) -> float:
        return self._sueldo
    
    def subir_sueldo(self, porcentaje : float) -> float:
        self._sueldo *= 1 + (porcentaje/100)
    