import json
from urllib import request
url='https://my.api.mockaroo.com/personas.json?key=01221290'
respuesta=request.urlopen(url)
#print(respuesta.read())
contenido=respuesta.read()
#print(contenido)
json_obtenido=json.loads(contenido.decode('utf-8'))
#print(json_obtenido)
for persona in json_obtenido:
    print(f"Nombre: {persona['Nombres']}")
    print(f"Apellidos: {persona['Apellidos']}")
    print(f"Email: {persona['email']}")
    print("\n")


