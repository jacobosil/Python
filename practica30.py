#crear una clase llamada cancion con los atributos de titulo y autor
#se debe definir un constructor inicializando ambos, crear getters y setters
#de los atributos y luego usar los metodos e imprimir los resultados

class Cancion:
    def __init__(self,titulo,autor) :
        self.titulo = titulo
        self.autor = autor

    def get_titulo(self):
        return self.titulo
    
    def set_titulo(self,titulo):
        self.titulo = titulo

    def get_autor(self):
        return self.autor
    
    def set_autor(self,autor):
        self.autor = autor

T1 = Cancion("","")
print(T1.get_titulo())
print(T1.get_autor())

T1.set_autor("Michael Jackson")   
T1.set_titulo("Black or White")

print(T1.get_autor())
print(T1.get_titulo())
