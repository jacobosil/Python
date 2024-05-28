#encontrar el maximo valor en una lista de tuplas


tuplas = [(1,2),(3,4),(5,0),(6,8)]
maximo = max(tuplas, key = lambda x: x[0])
#print(maximo)

combinar = lambda nombre,apellido: nombre + " " + apellido
print(combinar("jose", "perez"))

iguales =  list(filter(lambda x: x[0] == x[1], tuplas))
print(iguales)

mayores = list(filter(lambda x: x[0] > x[1], tuplas))
print(mayores)

menores = list(filter(lambda x: x[0] < x[1], tuplas))
print(menores)