def menu():
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("0. Salir")
    opcion = int(input("?_____ "))
    return opcion

def solicitaDatos():
    num1 = int(input("Dime el primer numero: "))
    num2 = int(input("Dime el segundo numero: "))
    return num1, num2

def operacion(operador, num1, num2):
    if operador == "Suma":
        resultado = num1 + num2
    elif operador == "Restar":
        resultado = num1 - num2
    elif operador == "Multiplicar":
        resultado = num1 * num2
    elif operador == "Dividir":
        if num2 != 0:
            resultado = num1 / num2
            return resultado
        else:
            return "No es posible dividir entre cero"

while True:
    opcion = menu()
    if opcion == 1:
        num1, num2 = solicitaDatos()
        print(f"La suma de {num1} + {num2} = {operacion('Suma', num1, num2)}")
    elif opcion == 2:
        num1, num2 = solicitaDatos()
        print(f"La resta de {num1} - {num2} = {operacion('Restar', num1, num2)}")
    elif opcion == 3:
        num1, num2 = solicitaDatos()
        print(f"La multiplicacion de {num1} * {num2} = {operacion('Multiplicar', num1, num2)}")
    elif opcion == 4:
        num1, num2 = solicitaDatos()
        result = operacion('Dividir', num1, num2)
        print(f"Division de {num1} / {num2} = {result}")
    elif opcion == 0:
        break
    else:
        print("Introduce una opcion válida ")
        print("\n")

print("Salimos")
