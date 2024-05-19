#crearla superClase padre y madre, luego crear la clase hija que
#realice una herencia multiple de ambos, colocar dos atributos
#para cada clase y un metodo distinto. Mostrar todo


class Padre:
    def __init__(self,ojos, pelo):
        self.ojos = ojos
        self.pelo = pelo
    def correr(self):
        print("40km")
    def __str__(self):
        return f"el padre tiene los ojos de color {self.ojos} y el pelo de color {self.pelo}"
        


class Madre:
    def __init__(self,culo,piernas):
        self.culo = culo
        self.piernas = piernas
    def cocinar(self):
        print("comida española")
    def __str__(self):
        return f"la madre tiene el trasero {self.culo} y piernas {self.piernas}" 
        


class Hija(Padre,Madre):
    def __init__(self, ojos, pelo,culo,piernas, piel,estatura):
        Padre.__init__(self,ojos, pelo)
        Madre.__init__(self,culo,piernas)
        self.piel = piel
        self.estatura = estatura
    def atleta(self):
        print("Hace Crossfit")
    def __str__(self):
        return f"y la hija heredo ambos rasgos: " + Padre.__str__(self) + " " +  Madre.__str__(self) 

padre = Padre("azules","marron")
madre = Madre("redondo","largas")
hija = Hija("azules","marron","redondo", "largas","color humilde","180cm")

print(padre)
print(madre)
print(hija)

    

        


    