#escribir una frase e imprimir la longitud de la frase
#y buscar una palabra dentro de la frase, mostrar por pantalla los resultados

frase = input("ingrese una frase ")
print(len(frase))
print("hola" in frase)

if "hola" in frase: 
    print("si, la palabra esta en la frase")