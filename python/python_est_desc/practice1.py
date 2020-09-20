#!/usr/bin/python
#basic object handling

def suma (x,y):
    return x+y

class Operaciones(object):
    def suma(self, x, y):
        self.resultado = x+y
        return self.resultado
#usando la funcion
print(suma(2,3))

#usando el objeto
operInstance = Operaciones()
print(operInstance.suma(2,7))




