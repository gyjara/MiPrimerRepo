#Tabla de multiplicar con for
tabla=int(input("Que tabla quieres calcular? "))
print(f"Tabla de {tabla}")
#repetir mientras sea menor de 11
for contador in range(1,11):
    resultado=tabla*contador
    print(f"{tabla} por {contador} es = {resultado}")
print("Fin de la tabla \n")

###########################
#Ejemplo FOR con lista
print("Lista de nombres ")
nombres=["Mario","ESTHER","Rurth","Joel","Marcos","Noemí"]
for nombre in nombres:
    print(f"Hola, {nombre}")
    
####################################
#Mostrar nostrar numeros hasta al 100

for numero in range(101):
    print(numero)