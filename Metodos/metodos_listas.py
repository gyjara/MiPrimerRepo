#creando una lista con list()
lista=list(["hola","gisela",25,8,7,8,True])

#devuelve la cantidad de elementos  de la lista
cantidad_elementos=len(lista)

#Agregando un elemento a lista
lista.append("Jara")

#agregando una elemento a la lista en un indice específico
lista.insert(2,"mi mamá")

#agregamos varios elementos a la lista
lista.extend(["a","b","c"])

#eliminando un elemento de la lista por su indice
print(len(lista))
lista.pop(0)   # -1 PARA ELIMINAR EL ULTIMO DE LA LISTA

#REMOVIENDO UN ELEMENTO DE LA LISTA POR SU VALOR    
lista.remove(12)

#ORDENA DE FORMA ACENDENTE LA LISTA SI SOLO TUVIERA LISTA NUMERICO
lista.sort()




#ELIMANDO TODOS LOS ELEMENTOS DE LA LISTA
#lista.clear()
print(lista)