class Vehículo:
    def __init__(self,color,velocidadMaxima,marca):
        self.color=color
        self.velocidadMaxima=velocidadMaxima
        self.velocidad=0
        self.marca=marca
    def arrancar (self):
        print('Arancando')
    def acelerador(self):
        if self.velocidad==0:
            self.velocidad=10
        else:
            self.velocidad=self.velocidad+10
        print(f"Velocidad= {self.velocidad}")
    def frenar(self):
        if self.velocidad>0:
            self.velocidad=self.velocidad-10
        else:
            self.velocidad=0
        print(f"Velocidad= {self.velocidad}")
    def muestraEstado(self):
        print(f"Soy de la marca {self.marca},con el color {self.color} y con la velocidad maxima de {self.velocidadMaxima}")
        
peugeut=Vehículo('rojo',120,'Peugeot')
peugeut.arrancar()
peugeut.acelerador()
peugeut.acelerador()
peugeut.frenar()
peugeut.muestraEstado()


#####creando clases hijo
class Moto(Vehículo):
    def __init__(self, color, velocidadMaxima, marca,ruedas):
        super().__init__(color, velocidadMaxima, marca)
        self.ruedas=ruedas
        
    def muestraEstado(self):
        print(f"Soy de la marca {self.marca},con el color {self.color} y con la velocidad maxima de {self.velocidadMaxima} \n y tengo  {self.ruedas} ruedas")
      
Motomax=Moto('PINK',140,'Motomax',2)
Motomax.arrancar()
Motomax.acelerador()
Motomax.acelerador()
Motomax.frenar()
Motomax.muestraEstado()



class Coche(Vehículo):
    def __init__(self, color, velocidadMaxima, marca,ruedas):
        super().__init__(color, velocidadMaxima, marca)
        self.ruedas=ruedas
        
    def muestraEstado(self):
        print(f"Soy de la marca {self.marca},con el color {self.color} y con la velocidad maxima de {self.velocidadMaxima} \n y tengo  {self.ruedas} ruedas")
      

Chebrelet=Coche('PINK',140,'Chebrelet',4)
Chebrelet.arrancar()
Chebrelet.acelerador()
Chebrelet.acelerador()
Chebrelet.frenar()
Chebrelet.muestraEstado()
