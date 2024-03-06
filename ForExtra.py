lista_colores=["Rojo","Rosado","Verde","Celeste","Crema","Gris"]
mi_color="Dorado"
for color in lista_colores:
    print(color)
    if color==mi_color:
        print("Color encontrado")
        break
else:
    print(f"No he encontrado el color {mi_color}\n") 
#####
rango_largo=range(1,1000)
print(rango_largo)
for numero in rango_largo:
    print(numero)
    if numero==4:
        print(f"Encontrado el numero {numero}")
        break
else:
    print("No he encontrado el número indicado")    