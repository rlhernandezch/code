#!/usr/bin/python
import math

#uso de filter, map y reduce
import math
from functools import reduce

def sumaresta (x=0,y=0):
    suma=x+y
    resta=x-y
    return (suma, resta)

def suma(*args):
    return sum(args)

def sumcuad(*datos):
    total = 0 
    for d in datos:
        total += d**2
    return total

lsuma = lambda x,y: x+y

val=sumaresta(3,2)
print("Suma: " +str(val[0]) )
print("Resta: " +str(val[1]) )

val=sumaresta()
print("Suma: " +str(val[0]) )
print("Resta: " +str(val[1]) )



print( suma(1,2,3,4,5,6,7,8,9) )

print( sumcuad(1,2,3,4,5,6,7,8,9) )

cuadrado = lambda x: x**2
print( cuadrado(4) )
print( lsuma(3,2)  )

data = [1,2,3,4,5,6,7,8,9,10]
filtered_data = list(filter(lambda x: (x*2>0), data))
print (data)
print (filtered_data)

maped_data = list(map(lambda x: x*2,data))
print (maped_data)


reduced_data = reduce(lambda x,y: x+y, data)
print ( reduced_data )

print(math.sqrt(8))
print(math.sqrt(8)%1)