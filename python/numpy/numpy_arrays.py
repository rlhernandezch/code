#!/user/bin/python
import numpy as np

a  = np.array([     [1,2,3],
                    [3,4,5],
                    [4,5,6]
                ]
                )
print("The array is")
print (a)
print ("Print items in second column")
print (a[...,1])

print ("Print items in second row")
print (a[1,...])

print ("Print items column 1 onwards")
print (a[...,1:])