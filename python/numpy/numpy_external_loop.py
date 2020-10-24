#!/user/bin/python
import numpy as np

a = np.arange(0,60,5)
a = a.reshape(3,4)

print('Original array is:')
print(a)
print('\n')

print ('Modified array is')
for x in np.nditer(a,flags = ['external_loop'], order = 'F'):
    print(x)

