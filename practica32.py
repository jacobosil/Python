#crear una clase llamada persona que tenga los atributos, nombre edad 
#y nacionalidad luego crear el metodo hablar que imprima un msj de estoy hablando
#despues crear una clase hija llamada empleado inicializarlo con los datos
#del padre y añadirle  trabajo y salario como atributo. Despues crear 
#otra clase hija que tenga los atributos del padre y agregar nota y universidad
#como atributos.

class Persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print("estoy hablando")

    def __str__(self) :
        return f"{self.nombre} tiene {self.edad} años de edad y es de nacionalidad {self.nacionalidad}"
        

class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad,trabajo,salario):
        super().__init__(nombre, edad, nacionalidad,)
        self.trabajo = trabajo
        self.salario = salario

    def hablar(self):
        print(f"{self.nombre} : estoy hablando desde el trabajo ({self.trabajo})")

    def __str__(self):
        return f"{self.nombre} tiene {self.edad} años de nacionalidad {self.nacionalidad} trabaja en {self.trabajo} y gana {self.salario}"



class estudiante(Persona):
    def __init__(self, nombre, edad, nacionalidad,nota,universidad):
        super().__init__(nombre, edad, nacionalidad)
        self.nota = nota
        self.universidad = universidad

    def hablar(self):
        print(f"{self.nombre} : estoy hablando desde {self.universidad}")

    def __str__(self):
        return f"{self.nombre} tiene {self.edad}  de nacionalidad {self.nacionalidad} su nota es {self.nota} y estudia en {self.universidad}"


P1 = Persona("Raul",20,"colombiana")
P1.hablar()
    
E2 = Empleado("MARTHA",18,"colombiana","secretaria","1 millon")
E2.hablar()

E3 = estudiante("maria",21,"Argentina",7,"UTN")
E3.hablar()

print(P1)
print(E2)
print(E3)