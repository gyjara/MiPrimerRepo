def esPar(numero):
    if numero%2==0:
        #print("El número es par")
        return True
    else:
        #print(f"El número {numero} es impar")
        return False
numero=int(input("Dime el número y te indico si es par o impar "))  
resultado=esPar(numero)  
if resultado:
    print(f"El numero {numero} es par") 
else:
    print(f"El numero {numero} es impar")