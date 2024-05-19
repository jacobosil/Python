#crear dos listas y pedirle al usuario que agregue tres elementos a cada una
#luego unir las dos listas y mostrar los elementos de la nueva lista

lista1 = []

dato = input("ingrese palabra ")
lista1.append(dato)

dato = input("ingrese palabra ")
lista1.append(dato)

dato = input("ingrese palabra ")
lista1.append(dato)

lista2 = []

dato = input("ingrese palabra ")
lista2.append(dato)

dato = input("ingrese palabra ")
lista2.append(dato)

dato = input("ingrese palabra ")
lista2.append(dato)

lista1.extend(lista2)
print(lista1)