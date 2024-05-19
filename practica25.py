#crear una lista, luego crear una funcion que reciba la lista y nos permita
#añadir nuevos datos a la lista, despues crear una funcion 
#que nos permita ver los datos, usar un bucle que consiga un menu para seleccionar
#la opcion de añadir datos y mostrar resultados y salir

lista = []

def añadirDatos(lista):
    dato = input("ingrese un nuevo dato ")
    lista.append(dato)
    
def mostrarDatos(lista):
    print("datos de la lista")
    if not lista:
        print("no hay datos")
    else:
        for dato in lista:
            print(dato)



def menu():
    while True:
        print("bienvenido al menu")
        print("1- añadir datos")
        print("2- mostrar resultado")
        print("3- salir")
        opcion = input("seleccione una opcion ")

        if opcion == "1":
            añadirDatos(lista)
        elif opcion == "2":
            mostrarDatos(lista)
        elif opcion == "3":
            print("saliendo del programa")
            break
        else:
            print("opcion no valida. seleccione del 1 al 3")

menu()

