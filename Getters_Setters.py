class persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    # Obtener nombre
    def get_nombre(self):
        return self._nombre

    # Dar valor a nombre
    def set_nombre(self, nombre):
        self._nombre = nombre

    # Obtener edad
    def get_edad(self):
        return self._edad

    # Dar valor a edad
    def set_edad(self, edad):
        if edad >= 0:
            self._edad = edad
        else:
            print('La edad no puede ser negativa')

# Obtener objeto, instanciar la clase
persona1 = persona("Adrian", 34)
print(f"Nombre: ", persona1.get_nombre()+ "\t Edad:", persona1.get_edad())
persona1.set_nombre("Britani")


#PERSONA1:_NOMBRE="Jose"
print("Nombre: ",persona1.get_nombre())
persona1.set_edad(30)
print("Edad: ",persona1.get_edad())


