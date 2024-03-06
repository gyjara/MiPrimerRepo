cadena1="Hola,soy, GIsela"
cadena2="Bienvenido "

resultado=cadena1.upper() # mayuscula
resultado=cadena1.lower() # letras minusculas
resultado=cadena1.capitalize() #primerra letra mayuscula

#buscamos una cadena en otra cadena, sino hay coincidencias devuelve -1
busqueda_find=cadena1.find("soy")

#buscamos una cadena en otra cadena, si no hay coincidencias lanza una excepcion
#busqueda_find=cadena1.index("9")


#si es numerico, devolvemos true, sino devolvemos falso
es_numero=cadena1.isnumeric()
#si es alfanumerico, devolvemos true
es_Alfanumerico=cadena1.isalpha()

#contamos las coincidencias de una cadena, dentro de otra cadena, devuelve la cantidad de coincidencias
contar_coincidencias=cadena1.count("e")
#contamos cuantos caracteres tiene una cadena
contar_caracteres=len(cadena1)

#verifiacmos si una cadena empieza con otra cadena dada, si es asi devuelve true
empieza_con=cadena1.startswith("Hola")

#Verificamos si una cadena termina con otra cadena dad, si es asi devuelve true
termina_con=cadena1.endswith("a")

#si el valos 1, se encuentra en la cadena original, remplaza el valor 1 por la misma el valor 2
cadena_nueva=cadena1.replace("la","lis")


#separar cadena con la que lo pasamos
cadena_Separada=cadena1.split(",")
print(cadena_Separada)

