#!/user/bin/python
import numpy as np

#x = np.zeros ((2,2), dtype = [('x','i4'),('y','i4')]
#print(x)


#convert list to ndarray
x = [1,2,3]
a = np.asarray(x)
print(a)


x = [1,2,3]
a1 = np.asarray(x, dtype = float)
print(a1)

#ndarray from tuple
x2 = (1,2,3)
a2 = np.asarray(x2)
print(a2)

#ndarray from list of tuples
x3 = [(1,2,3),(4,5)]
a3 = np.asarray(x3)
print(a3)

