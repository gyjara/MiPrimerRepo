Nombre_De_tu_tio_case="Romero"
print(Nombre_De_tu_tio_case)

#datos Compuestos
#creando una lista (se puede modificar)
lista=["Gisela Jara","Soy Jara",True,1.50]

#creando tupla (no se puede modificar)
tupla=["Gisela Jara","Soy Jara",True,1.50]

#esto es valido
lista[3]="Femenino"

#esto no es valido
#tupla[1]="mujer"
print(lista)

#creando un conjunto _(set) no se puede llamar a los elementos por indice y no almacena datos ordenados
conjunto={'Gisela Jara ',"Soy Jara",True,1.50}
print(conjunto)

#creando diccionario
diccionario={ "\n "
    'Nombre':"GISELA JARA",
    'canal':"Soy JARA",
    'Esta_emosionado':True,
    'altura':1.500,
    'Dato_duplicado':"Soy JARA"
}
print(diccionario)