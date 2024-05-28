#crear una clase que se inicie con la marca y el modelo y tenga un metodo
#que imprima un mensaje que diga estoy conduciendo

class Auto:
    def __init__(self,marca,modelo) :
        self.marca = marca
        self.modelo = modelo

    def mensaje(self):
        print("estoy conduciendo")
        