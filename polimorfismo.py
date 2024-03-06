class Animal:
    def hacer_sonido(sef):
        pass
class Perro(Animal):
    def hacer_sonido(sef):
        return "Gual"
class Gato(Animal):
    def hacer_sonido(sef):
        return "Mia"
def interactuar_con_animal(animal):
    return animal.hacer_sonido()

mi_perro=Perro()
mi_gato=Gato()

resultado_perro=interactuar_con_animal(mi_perro)
resultado_gato=interactuar_con_animal(mi_gato)

print(resultado_perro)
print(resultado_gato)