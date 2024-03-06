#conjunto vacio
conjunto_vacio=set()

#conjunt con elementos
numeros={1,2,3,4,5,6,7,8,9}
letras=set(['a','b','c','d'])

print(conjunto_vacio)
print(numeros)
print(letras)

print('*'*30)
#Agregar elementos
frutas={'manzana','platano','naranja'}
print(frutas)
frutas.add('Piña')
print(frutas)

#Eliminar elemtos
frutas.remove('platano')
print(frutas)

#union de conjuntos
conjunto1={1,2,3}
conjunto2={3,4,5}
union=conjunto1| conjunto2
print(union)

#interseccion
interseccion=conjunto1& conjunto2
print(interseccion)

#diferencia
diferencia=conjunto1 - conjunto2
print(diferencia)


#diferencia semetrica
diferencia_semetrica=conjunto1 ^ conjunto2
print(diferencia_semetrica)

#pertenencia
if  3 in conjunto1:
    print("El 3 está en el conjunto 1")
else:
    print("El 3 no esta en el conjunto 1")
    
#longitud
longitud=len(conjunto1)
print(longitud)

#conversion listas y conjuntos
lista=[1,2,3,2,2,3,4,5,6,7,8,9,]
print(lista)
conjunto=set(lista)
print(lista)

lista_nueva=list(conjunto)
print(lista_nueva)