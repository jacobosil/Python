#crear una clase llamada persona y dentro de ella el metodo init con dos
#parametros de nombre y edad despues crear un objeto para pasarle los datos
#e imprimirlos

class Person:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"{self.nombre}({self.edad})"
        


p1 = Person("raul", 20)

print(p1.nombre, p1.edad)
print(p1)