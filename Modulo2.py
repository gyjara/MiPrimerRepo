
from random import randint as azar
from random import  *
continua="s"
while(continua=="s" or continua =="s"):
    lanzaDado=azar(1,6)
    print("Has sacado un "+str(lanzaDado))
    continua=input("Continuamos s/n? ")
print("Ya no tiro mas el dado, hasta luego ")