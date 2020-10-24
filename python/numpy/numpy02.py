#!/user/bin/python
import numpy as np

dt = np.dtype(np.int32)
dt2 = np.dtype('i4')
dt3 = np.dtype('>i4')
print(dt)
print(dt2)
print(dt3)

dt4 = np.dtype([('age',np.int8)])
print(dt4)

dt5 = np.dtype([('age',np.int8)])
a = np.array([(10,),(20,),(30,)], dtype =dt)
print (a)

#file name can be used to access content of  age column 

dt5 = np.dtype([('age',np.int8)])
a2 = np.array([(10,),(20,),(30,)], dtype = dt5)
print (a2['age'])

student = np.dtype([('name','S20'),('age','i1'),('marks','f4')])
print (student)


a3 = np.array([[1,2,3],[4,5,6]])
print (a3.shape)
b3 = a3.reshape(3,2)
print(b3.shape)

#an array of evenly spaced numbers
a4 = np.arange(24)
print(a4)

b4 = a4.reshape(2,4,3)
print(b4)