#!/usr/bin/python
#basic object handling

def suma (x,y):
    return x+y

def buscapares (x):    
    if (x % 2 == 0):
        vlIsPair = True
    else:
        vlIsPair = False
    return vlIsPair


class Operaciones(object):
    def suma(self, x, y):
        self.resultado = x+y
        return self.resultado
#usando la funcion
print(suma(2,3))

#usando el objeto
operInstance = Operaciones()
print(operInstance.suma(2,7))


def saludar():
    nombre = str(input("Introduce Nombre: "))
    vlReturn=0

    if nombre:
        print ("Hola "+nombre)
        vlReturn = 1
    else:
        print("Hola")
        vlReturn = 0
    return vlReturn


if saludar():
    print ("option 1")
else:
    print ("option 2")

if buscapares(4):
    print("Es par")
else:
    print("Es non")




