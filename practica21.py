#DICCIONARIOS ANIDADOS

Familia = {
    "hijo1": {
        "nombre": "pepe",
        "edad": 15,
    },
    "hijo2": {
        "nombre": "raul",
        "edad": 20,
    },
    "hijo3": {
        "nombre": "roberto",
        "edad": 19,
    }
}
print(Familia)
print(Familia["hijo2"]["nombre"])

for clavePadre,valorPadre in Familia.items():
    print(clavePadre)
    for claveHijo,valorHijo in valorPadre.items():
        print(claveHijo,valorHijo)