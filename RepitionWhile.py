#tabla de multiplicar
tabla=int(input("¿Qué tabla quieres calcular? "))
#creamos variable contador
contador=1
print(f"Tabla de {tabla}")
#repiticion
while (contador <= 11):
    resultado=tabla*contador   
    #mostrar la tabla
    print(f"{tabla} por {contador -1} es igual a {resultado} \n")
    
     #incremento el contador
    contador=contador+1
print("Fin de la tabla ")