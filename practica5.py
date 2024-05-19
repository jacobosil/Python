#si la persona tiene una nota mayor o igual a 90 se imprimira la letra A
#y asi sucesivamente hasta la letra E que es mayor o igual a 50
#si tiene una nota inferior recibira la letra F

nota = int(input("ingrese la nota "))

if nota >= 90: 
    print("A")
elif nota >= 80:
    print("B")
elif nota >= 70:
    print("C")
elif nota >= 60:
    print("D")
elif nota >= 50:
    print("E")
else: 
    print("F")