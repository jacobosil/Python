#def significa funciones

def saludo():
     print("Hello World")

def nombre(name):
     print("su nombre es", name)
nombre("jacobo")

def nombreCompleto(nombre,apellido):
     print("bienvenido", nombre,apellido)
nombreCompleto("jacobo", "silva")

def mostrar(frutas):
     for x in frutas:
          print(x)

frutas = ["banana","limon","pera"]
mostrar(frutas)

def multiplicacion(numero):
     return 5 * numero



print(multiplicacion(3))

resultado = multiplicacion(10)
print(resultado)
    