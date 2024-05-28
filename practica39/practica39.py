#from para importar algo especifico desde otro archivo

from practica39b import persona2 as p2


import practica39b as p39b
print(p39b.persona) 

print(p39b.persona["nombre"])
print(p39b.persona["edad"])
print(p39b.persona["nacionalidad"])

print(p39b.persona2)
print(p2)