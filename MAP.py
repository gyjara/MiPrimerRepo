#Funcion Map
lista=[23,34,7,5,9,1,76,24,68]
print("el cuadrado de los numeros es:",list(map((lambda valor:valor*valor),lista)))


#Funcion Filter
print(list(filter((lambda valor: valor % 2==0),lista)))


#funcion reduce
import functools
print(str(functools.reduce((lambda X, resultado: X+ resultado),lista)))


#MAY( funcion, secuencia)

numeros=[1,2,3,4,5,6]
cuadrados=list(map(lambda x:x**2,numeros))
print("ejemplo de MAP AL CUADRADO \n",numeros)
print(cuadrados,"\n" ,"-"*60)

#sin map
cuadrado=[]
for numero in numeros:
    cuadrados.append(numero**2)
print(numeros)
print(cuadrados)