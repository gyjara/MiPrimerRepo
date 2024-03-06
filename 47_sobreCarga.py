class MiNumero:
    def __init__(self,valor):
        self.valor=valor
    def __add__(self,other):
        if isinstance(other,MiNumero):
            return MiNumero(self.valor+other.valor)
        elif isinstance(other,(int,float)):
            return MiNumero(self.valor+other)
        else:
            raise TypeError("Operacion no reportada")
    def __str__(self):
        return str(self.valor)

numero1=MiNumero(5)
numero2=MiNumero(10)
resultado1=numero1+numero2
resultado2=numero1+5
print(resultado1)
print(resultado2)
texto="Hola"
resultado3=numero1,texto
print(resultado3)
    

class Persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
    def __eq__(self, other):
        if isinstance(other,Persona):
            return self.nombre==other.nombre and self.edad==other.edad
        return False
    def __str__(self):
        return f"Nombre:{self.nombre},Edad:{self.edad}" 
persona1=Persona("Juan",30)
persona2=Persona("Jaun",30)
print(persona1)
print(persona2)
        
        