diccionario={
    "nombre":"Gisela",
    "apellido":"Jara",
    "subs" :100000
}

#nos devuelve un objeto diccionario_item
claves=diccionario.keys()

#obteniendo un elemento con get() (si no encuentra nada en el programa continua)
valor_de_kasdks=diccionario.get("kasdks")
print("hola papa, el programa contitunua")

#elimina todo del diccionario
#  diccionario.clear()

#eliminandoi un elemento del diccionario
diccionario.pop("apellido")

#obteniendo un elemento diccionario items iterables
diccionario_iterable=diccionario.items()

print(diccionario_iterable)


