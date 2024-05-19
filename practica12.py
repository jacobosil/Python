#crear una lista de 3 elementos, añadir dos elementos, ordenarlos alfabeticamente
#insertar en la posicion 2 un nuevo elemento, verificar si tomate esta en la lista
#y mostrar la longitud y los elementos de la lista

Lista = ["cama", "auto", "tomate" ]

Lista.append("vida")
Lista.append("rubia")
Lista.sort()

Lista.insert(2, "naranja")
if "tomate" in Lista:
    print("si esta en la lista")

print(len(Lista))

print(Lista)

