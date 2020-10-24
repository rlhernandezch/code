#!/user/bin/python
import numpy as np

list = range(5)
it = iter(list)

x = np.fromiter(it, dtype = float)
print(x)


x2 = np.arange(5)
print(x2)


x3 = np.arange(5,dtype = float)
print(x)

#Start and stop parameters

