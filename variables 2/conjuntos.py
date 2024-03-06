#teoria de conjuntos
conjunto1={2,4,6,8}
conjunto2={2,6,8}

#verificando si es un subconjunto
#resultado=conjunto2.issubset(conjunto1)
resultado=conjunto2<=conjunto1

#verificar si es un super conjunto
resultado=conjunto2.issuperset(conjunto1)
resultado=conjunto2>conjunto1

print(resultado)
