#!/usr/bin/python

import math

def fn_ncomb (x, y):
    resultado=math.factorial(x)/math.factorial(y)* math.factorial((x-y))
    return (math.trunc(resultado) )

val=fn_ncomb(5,3)

print(val)


val2=math.fmod(5,3)
print(val2)

x = int(input())

if x == 5:
    print('es cinco')
elif x > 0 and x < 10:
    print('mayor que cero menor que diez')
elif x < 0:
    print('menor que cero')
else:
    print('alguna otra opcion')

#funciones trigonometricas

>>> import math
>>> math.expm1(1)
1.718281828459045
>>> math.e
2.718281828459045
>>> math.e-1
1.718281828459045
>>> math.exp(1) -1
1.718281828459045
>>> math.exp(1)-1 == math.expm1(1)
True
>>> math.log(10,1000)
0.33333333333333337
>>> math.log(10,10)
1.0
>>> math.sin(80)
-0.9938886539233752
>>> math.cos(math.pi)
-1.0
>>> math.tan(math.pi/2)
1.633123935319537e+16
>>> math.acos(1)
0.0
>>> math.atan(1)
0.7853981633974483
>>> math.degrees(math.atan(1))
45.0
>>> math.cos(math.radians(60))
0.5000000000000001


math.hypot(3,4)

math.atan2(4,3)
