#usuario nos da el numero del mes y nosotros los pasamos en letras
def dameMes(num):
    meses={
        1:"Enero",
        2:"Febrero",
        3:"Marzo",
        4:"Abril",
        5:"Mayo",
        6:"Junio",
        7:"Julio",
        8:"Agosto",
        9:"Septiembre",
        10:"Octubre",
        11:"Noviembre",
        12:"Diciembre"
    }
    return meses.get(num,"Mes no valido")
mes=int(input("Introduccion un numero de 1 al  12 para saber el mes: "))
print(dameMes(mes))