class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    # Obtener nombre
    @property
    def nombre(self):
        return self._nombre

    # Dar valor a nombre
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    # Obtener edad
    @property
    def edad(self):
        return self._edad

    # Dar valor a edad
    @edad.setter
    def edad(self, edad):
        if edad >= 0:
            self._edad = edad
        else:
            print('La edad no puede ser negativa')

# Obtener objeto, instanciar la clase
persona1 = Persona("Adrian", 34)
print(f"Nombre: {persona1.nombre}\t Edad: {persona1.edad}")

# Modificar nombre y edad
persona1.nombre = "Britani"
print("Nombre: ", persona1.nombre)

# Modificar edad (with validation)
persona1.edad = 30
print("Edad: ", persona1.edad)
