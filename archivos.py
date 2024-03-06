#guardar datos en archivos
#abrimos archivos
escritura=open("archivo.txt","w")
escritura.write("Esto se escribe en el archivo \n y esto en la linea siguiente \n  \t\t y estro en otra linea tabulado")
escritura.close()

#lectura de fichero
lectura=open("archivo.txt","r")
#leemos una linea 
leelinea=lectura.readline()
print("Leyendo una linea \n" +leelinea)
lectura.close()

#leemos todo el fichero
lectura=open("archivo.txt","r")
leetodo=lectura.read()
print("Leemos todo \n"+leetodo)
lectura.close()
