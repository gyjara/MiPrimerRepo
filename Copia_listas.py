listas_original=[1,2,3,4]
lista_copia=listas_original
print(listas_original)
print(id(listas_original))
print(type(listas_original))
print(lista_copia)
print(id(lista_copia))
print(type(lista_copia))

listas_original.append(6)
print(listas_original)
print(lista_copia)
print(listas_original is lista_copia)
#con Copy
print("*"*25)
print("usando copy")
listas_copia02=listas_original.copy()
print(listas_original)
print(id(listas_original))
print(type(listas_original))
print(listas_copia02)
print(id(listas_copia02))
print(type(listas_copia02))

listas_original.append(7)
listas_copia02.append(9)
print(listas_original)
print(listas_copia02)
print(listas_original is listas_copia02)

#con slicing
print("*"*25)
print("usando slicing")
listas_copia03=listas_original[:]
print(listas_original)
print(id(listas_original))
print(type(listas_original))
print(listas_copia03)
print(id(listas_copia03))
print(type(listas_copia03))

#con método copy
import copy
print("*"*25)
print("usando método copy")
listas_copia04=copy.deepcopy(listas_original)
print(listas_original)
print(id(listas_original))
print(type(listas_original))
print(listas_copia04)
print(id(listas_copia04))
print(type(listas_copia04))
print(listas_original is listas_copia04)

#ejemplos varios
#asignacion directa
listas_original=[1,2,3,4]
lista_copia=listas_original
lista_copia[0]=100
print("*"*25)
print("Ejercicios: ")
print(listas_original)
print(lista_copia)
#metodo copy
lista_copia=listas_original.copy()
lista_copia[1]=200
print(listas_original)
print(lista_copia)

#slicing
lista_copia=listas_original[:]
lista_copia[2]=300
print(listas_original)
print(lista_copia)

#modulo copy
print("*"*25)
listas_original=[[1,2],[3,4]]
lista_copia=copy.deepcopy(listas_original)
lista_copia[0][1]=1000
print(listas_original)
print(lista_copia)