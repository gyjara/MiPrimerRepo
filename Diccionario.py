diccionario={'nombre':'Jose','apellidos': 'Ojeda',
             'tutoriales': ['Python','JavaScript','Php']}
print(diccionario)
print(type(diccionario))
print(diccionario['nombre'])
print(diccionario['tutoriales'])
print(diccionario['tutoriales'][0])
for clave in diccionario:
    print ("impreso en for" ,clave, ":",diccionario[clave])

#metodos de los diccionarios
persona=dict(nombre="Luis",apellidos="Ortega tiburcio",edad=34)
print(persona)
print(type(persona))

diccionario2=dict(zip('aeiou',[1,2,3,4,5]))
print(diccionario2)
print(type(diccionario2))

print(diccionario2.items())
print(diccionario2.keys())
print(diccionario2.values())

print(diccionario.get("nombre"))