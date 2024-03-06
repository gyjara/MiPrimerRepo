class Persona:
    contador=0  #variable clase
    def __init__(self,nombre):
        self.nombre=nombre
        Persona.contador+=1 #incrementa al crear objeto o instancia de clase

Persona1=Persona("Juan")
Persona1=Persona("Karla")
Persona1=Persona("Carlos")

#valor contador
print("Numero de persona : ",Persona.contador)