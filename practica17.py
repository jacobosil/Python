#crear un tupla y añadir nuevo dato a una nueva lista que se formo de la tupla
#añadir 2 datos a la tuplay luego remover el dato en la posicion 0

tupla1 = ("carro", "pero", "casa", "comida")
# del tupla1[0]
# print(tupla1)
lista = list(tupla1)
lista.append("gato")
print(lista)
print(tupla1)

del lista[0]
print(lista)

for objeto in tupla1:           #for para recorer la tupla
    print(objeto)

if "pepe" in tupla1:            #if para buscar en la dupla
    print("si esta en la lista")
else:
    print("no esta en la lista")