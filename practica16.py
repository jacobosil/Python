#crear una tuple y mostrarla

tupla = ("manzana", "banana", "naranja")
print(tupla)
print(type(tupla))
for x in tupla: 
    print(x)

tupla = ("yuka", "pera", "papa", "yuka")
print(tupla)

#no se pueden cambiar los datos dentro de una tupla
# tupla[0] = "mani"
# print(tupla)

print(tupla[1])
print(tupla[-1])

if "pera" in  tupla:
    print("si esta en la tupla")

#convertir la tupla a lista 

tupla2 = list(tupla)
print(type(tupla2))

tupla2[1] = "cereza"
print(tupla2)