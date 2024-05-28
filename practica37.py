#crear una tupla e iterar y guardar en una variable usando el metodo iter

frutas = ("fresa","melon","uva")
#print(type(frutas))

iterador = iter(frutas)
print(next(iterador))
print(next(iterador))
print(next(iterador))

palabra = "banana"
iterador2 = iter(palabra) 
print(next(iterador2))
print(next(iterador2))
print(next(iterador2))
print(next(iterador2))
print(next(iterador2))
print(next(iterador2))

for x in frutas:
    print(x)

for x in palabra:
    print(x)