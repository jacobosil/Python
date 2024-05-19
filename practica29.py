#crear una clase llamada perro que tenga un nombre, una edad,una raza y energia
#crear el constructor con la energia fijada en 1000 , luego crear un metodo
#pasear que le reste 250 de energia. Imprimir los resultados.

class Perro:
    def __init__(self,nombre,edad,raza):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        self.energia = 1000

    def pasear(self):
        if self.energia >= 250:
            self.energia -= 250
            print(f"{self.nombre} ha paseado y ahora tiene {self.energia} de energia")
        else:
            print(f"{self.nombre} esta demasiado cansado")

    def __str__(self):
        return f"Mi perro {P1.nombre} tiene {P1.edad} años y su raza es {P1.raza}. Tiene {P1.energia} puntos de energia"
        

P1 = Perro("Flofy", 5, "Dogo")
print(P1)
P1.pasear()
print(P1.energia)

P1.pasear()
P1.pasear()
P1.pasear()
P1.pasear()
        