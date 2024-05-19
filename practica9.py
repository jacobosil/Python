#pedirle al usuario su nombre y su edad y mostrarlo utilizando F-String

nombre = input("ingrese su nombre ")
edad = int(input("ingrese su edad "))

texto = f"la persona {nombre} tiene {edad} años de edad"

print("la persona " + nombre + " tiene ", edad , " años de edad")
print(f"la persona {nombre} tiene {edad} años de edad")
print(texto)
