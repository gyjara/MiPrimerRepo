#generadores
def impares():
    for numero in range(1,51,2):
        yield numero
generador=impares()
for numero in generador:
    print(numero)
print(generador)    