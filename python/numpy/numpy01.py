#!/user/bin/python

import numpy as np
a = np.array([1,2,3])
print (a)

#Minimum dimensions
b = np.array([1,2,3,4,5], ndmin=2)
print(b)

#more than one dimensions
c = np.array([[1,2],[3,4]])
print(c)

#dtype parameter
d = np.array([1,2,3], dtype = complex)
print(d)
