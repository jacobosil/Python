#diccionarios: se usasn para guardar datos con una clave y un valor 

diccionario = {
    "nombre": "jacobo",
    "apellido": "silva",
    "edad": 33,
    "nombre": "ramon",
    "colores": ["rojo","blanco","azul"]
}

print(diccionario)
print(type(diccionario))
print(diccionario["nombre"])

print(len(diccionario))
print(diccionario["colores"])

diccionario2 = dict(nombre = "pedro", apellido = "perez", edad = 30)
print(diccionario2)

buscar = diccionario2.get("nombre")
print(buscar)

conseguir = diccionario2.keys()
print(conseguir)

diccionario2["color"] = "blanco"
print(conseguir)

valores = diccionario2.values()
print(valores)

x = diccionario2.items()
print(x)

if "carpa" in diccionario2:
    print("si esta en el diccionario")
else : 
    print("no esta en el diccionario")

diccionario2.update({"nombre": "pepe"})
print(diccionario2)

diccionario2.pop("color")
print(diccionario2)

diccionario2.popitem()
print(diccionario2)

del diccionario2["apellido"]
print(diccionario2)

# diccionario2.clear()
# print(diccionario2)

for x in diccionario:
    print(x)

for x in diccionario.values():
    print(x)

for x in diccionario.keys():
    print(x)

for x,y in diccionario.items():
    print(x,y)

diccionario3 = diccionario.copy()
print(diccionario3)

