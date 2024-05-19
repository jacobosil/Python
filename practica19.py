#pythonset

MiSet = {"alma", "fiesta", "caribe"}
print(MiSet)
print(type(MiSet))

# MiSet[0] = "roca" el set no se cambian los datos.
# print(MiSet)

# print(MiSet[0])  el set es desordenado es decir, no se puede referir por un indice

MiSet = {"alma", "fiesta", "caribe", "alma"}
print(MiSet) 

MiSet = {"alma", "fiesta", "caribe", True, 1, False, 0}
print(MiSet)
print(len(MiSet))

for item in MiSet:
    print(item)

if "fiesta" not in MiSet:
    print("la banana no esta")
else:
    print("si esta ")

MiSet.add("timon y pumba")  #le puedes agregar mas datos pero no cambiarlos
print(MiSet)

MiSet2 = {"fuego","playa"}

MiSet.update(MiSet2)
print(MiSet)

lista = ["karma","socio"]

MiSet.update(lista)
print(MiSet)

tupla = ("ganado", "vacas")
MiSet.update(tupla)
print(MiSet)

MiSet.remove("alma")
print(MiSet)

MiSet.pop()
print(MiSet)

MiSet.clear()
print(MiSet)

del MiSet
print(MiSet)