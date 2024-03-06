texto="Esto es un texto para el ejemplo que vamos a realizar"
#indica empieza y termina con
print("La cadena enpieza con: ",texto.startswith("Esto"))
print("La cadena enpieza con: ",texto.endswith("Esto"))

#Alinear caracteres centrado
print(texto.center(80," "))
longitudCadena=len(texto)
print(longitudCadena)


#añadir caracteres a la derecha y izquierda
print(texto.ljust(80," ")) #Izquierda
print(texto.rjust(80," ")) #derecha