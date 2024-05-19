#funcion lambda (anonima)

sumar = lambda x: x + 10

resultado = sumar(5)
print(resultado)

multiplicar = lambda x,y: x * y
resultado = multiplicar(10,10)
print(resultado)

lista = [1,2,3,4,5]
numero = list(map(lambda x: x + 1, lista))
print(numero)

lista_pares = list(filter(lambda x: x % 2 == 0, numero))
print(lista_pares)