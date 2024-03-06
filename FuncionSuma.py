def suma(num1,num2):
    resultado=num1+num2
    return resultado
num1=int(input("Dime el primer numero "))
num2=int(input("Dime el segundo numero"))
#lloamada a la funcion
resultado=suma(num1,num2)
#mostramos el resultado
print(f"La suma de {num1} + {num2} ={resultado}")