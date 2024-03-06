frase=input("Dígame una frase y te calculo cuanto tardarias si tuvieras que decirla: ")
palabras_separadas=frase.split(" ") #permite separar palabras
cantidad_de_palabras=len(palabras_separadas)

#en caso tarde mas de un minuto en decirlo, le decimos que pare un poco
if cantidad_de_palabras>12:
    print("Tampoco te pedí testamento")

#calculamos cuanto tardaria en decirlo las palabra y se lo decimos
print(f"Dijiste {cantidad_de_palabras} palabras, y tardarias {cantidad_de_palabras/2} segundos en decirlo")

#dalto tardaria
print(f"Dalto lo diria en {cantidad_de_palabras*100//2*1.3/10} segundos en decirlo")


                         