palabras=["Hola","mundo","Phyton"]
mayusculas=[]
for palabra in  palabras:
    mayusculas.append(palabra.upper())
print(palabras)
print(mayusculas)

print("*"*20)
mayusculas=[palabra.upper() for palabra in palabras]
print(mayusculas)

##############################
numeros=[2,4,7,8,9,10,34]
mayores_a_cinco=[numero for numero in numeros if numero>5]
print("\n Ejercicio 2")
print(mayores_a_cinco)
###################################

frase="Python es u lenguaje de programación"
vocales=[letra for letra in frase if letra in "aeiouAEIOU"]
print(frase)
print(vocales)
