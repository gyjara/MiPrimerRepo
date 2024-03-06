def calcular(num1,num2,operacion="sumar"):
    def sumar(num1,num2):
        return num1+num2
    def restar(num1,num2):
        return num1-num2
    def multiplicar(num1,num2):
        return num1*num2
    def dividir(num1,num2):
        return num1/num2
    if operacion=="sumar":
        print(f" La suma de {num1} +{num2} ={sumar(num1,num2)}")   
    elif operacion=="restar":
         print(f"La resta {num1} - {num2} ={restar(num1,num2)}")
    elif operacion=="multiplicar":
        print(f"La multiplicacion {num1}* {num2} ={multiplicar(num1,num2)}")
    elif operacion=="dividir":
        print(f"La divicion {num1} / {num2} ={dividir(num1,num2)}")
        
print(calcular(3,5,"sumar"))
print(calcular(17,5,"restar"))
print(calcular(3,5,"multiplicar"))
print(calcular(10,5,"dividir"))