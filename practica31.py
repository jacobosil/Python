#crear una clase persona con los atributos de nombre y apellido luego crear
#un metodo para imprimir ambos 

class persona():
    def __init__(self,nombre,apellido) :
        self.nombre = nombre
        self.apellido = apellido

    def imprimirDatos(self):
        print(self.nombre,self.apellido)
    
class estudiante(persona):
    #pass
    def __init__(self, nombre, apellido,escuela, edad):
        super().__init__(nombre, apellido)
        self.escuela = escuela
        self.edad = edad

    def imprimirDatos(self):
        super().imprimirDatos()
        print(self.escuela,self.edad)

N1 = persona("Ramon", "Perez")

N1.imprimirDatos()

E1 = estudiante("luis","rama","high", 15)
E1.imprimirDatos()        



