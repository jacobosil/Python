#crear una tupla de 3 elementos, pasarlo a una lista,  borrar el elemento en la 
#posicion 2 e imprimir la longitud de la tupla y recorer con un for la tupla

tupla1 = ("alma","mora", "cosa")
lista = list(tupla1)

del lista[2]
print(lista)

print(len(tupla1))

for cama in tupla1:
    print(cama)