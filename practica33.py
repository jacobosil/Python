#crear una clase llamada auto que tenga como atributos: 
#puertas,ventanas, tipo de motor, marca y modelo luego crear 
#tres clases hijas que tengan atributos adicionales como:
#tipo de traccion, autonomia y todo terreno
#crear el metodo acelerar para el auto deportivo, el metodo conducir 
#en terreno dificil para auto todo terreno, el metodo cargar
#bateria para el auto electrico. deben tener un print que exprese dicho metodo
#crear el metodo str sobre la clase auto.

class Auto:
    def __init__(self, puertas, ventanas, tipo_de_motor, marca, modelo) :
        self.puertas = puertas
        self.ventanas = ventanas
        self.tipo_de_motor = tipo_de_motor
        self.marca = marca
        self.modelo  = modelo
    def __str__(self):
        return f"El auto tiene {self.puertas} puertas y {self.ventanas} ventanas su tipo de motor es {self.tipo_de_motor} y de la marca alemana {self.marca} modelo {self.modelo}"
        

class AutoDeportivo(Auto):
    def __init__(self, puertas, ventanas, tipo_de_motor, marca, modelo, tipo_de_traccion):
        super().__init__(puertas, ventanas, tipo_de_motor, marca, modelo)
        self.tipo_de_traccion = tipo_de_traccion
    def acelerar(self):
        print("estoy acelerando")
        



class AutoTodoTerreno(Auto):
    def __init__(self, puertas, ventanas, tipo_de_motor, marca, modelo, todo_terreno):
        super().__init__(puertas, ventanas, tipo_de_motor, marca, modelo) 
        self.todo_terreno = todo_terreno
    def conducir(self):
        print("conduciendo en terreno dificil")


class AutoElectrico(Auto):
    def __init__(self, puertas, ventanas, tipo_de_motor, marca, modelo, autonomia):
        super().__init__(puertas, ventanas, tipo_de_motor, marca, modelo)
        self.autonomia = autonomia
    def cargar(self):
        print("cargar bateria")


deportivo = AutoDeportivo(5,4,"gasolina","ferrari","f8","trasera")
print("Auto deportivo:")
print("marca: ", deportivo.marca)
print("modelo: ", deportivo.modelo)
print("traccion: ", deportivo.tipo_de_traccion)
print("Tipo de motor: ", deportivo.tipo_de_motor)
print("ventanas: ", deportivo.ventanas)
print("Puertas: ", deportivo.puertas)
print()
todo_terreno = AutoTodoTerreno(4,4,"Diesel", "Jeep","Commander",True)
print("Auto todo terreno:")
print("Marca: ", todo_terreno.marca)
print("Modelo: ", todo_terreno.modelo)
print("Es todo terreno: ", todo_terreno.todo_terreno)
print("Tipo de motor: ", todo_terreno.tipo_de_motor)
print("Ventanas: ", todo_terreno.ventanas)
print("Puertas: ", todo_terreno.puertas)
print()
electrico = AutoElectrico(4,4,"electrico","tesla","model S",400)
print("Auto electrico:")
print("Marca: ", electrico.marca)
print("Modelo: ", electrico.modelo)
print("Autonomia: ", electrico.autonomia)
print("Tipo de motor: ", electrico.tipo_de_motor)
print("Ventanas: ", electrico.ventanas)
print("Puertas: ", electrico.puertas)

print()

auto = Auto(2,3,"20 cilindros","BMW","M3")
print(auto)