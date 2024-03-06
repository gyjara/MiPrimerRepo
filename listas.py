lista=[1,2,3,4,5,6,"Simon",[4,5],14]
print(type(lista))
print(lista)

print(lista[2])

for elemento in lista:
    print(elemento)


#añadiendo elementos en la lista
lista.append(10)
lista.append("Lucias")
lista.append([15,25,35,45,55,65,75])
print(lista)

#borrar elementos de la lista
lista.remove(4)
print(lista)
