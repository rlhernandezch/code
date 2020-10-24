#!/user/bin/python
import numpy as np
#default base is 10
a = np.logspace(1.0,2.0, num = 10)
print(a)

print("Ejemplo 2")
a2 = np.logspace(1,10,num = 10, base = 2)
print (a2)


#INDEXING & SLICING

print ("INDEXING & SLICING")
a3 = np.arange(10)
s = slice(2,7,2)
print (a[s])


a4 = np.arange(10)
print (a4[2:5])

print("multiarray")
a5 = np.array([     [1,2,3],
                    [3,4,5],
                    [4,5,6]
                ]
                )
print("para a5")
print(a5)
print("para a5[1:]")
print(a5[1:])
print("para a5[2:]")
print(a5[2:])
print("para a5[0:0]")
print(a5[0:1],a5[2:])