ingreso_mensual=100000 
gasto_mesual=3000

#if anidados elif 
if ingreso_mensual>1000:
    if ingreso_mensual-gasto_mesual<0:
        print("estas en deficit")
    elif ingreso_mensual-gasto_mesual>3000:
        print("bien estas bien")
    else:
        print("Estas gastando una banda, hayque ver si te alcanza") 
elif ingreso_mensual>1000:
    print("Estas bien en Latinoamerica")
else:
    print("sos pobre")