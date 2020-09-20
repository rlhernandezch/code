#!/usr/bin/python
import math
import random
#random.random()
myval=random.choice([1,2,3,4])
print(myval)

S ='123456789'
#strings manipulation
vlStrLengh=len(S)
print (vlStrLengh)
print (S[-1])
print (S[-2])
print (S[0:4])

#error on inmutable objects
#S[1] = 'J'

vlList = list(S)

vlList[8]='J'
print(vlList)
#prints the list as a single string
print(''.join(vlList))

#byte array
B = bytearray(b'spam')
B.extend(b'eggs')
print(B)
B[1]='L'
print(B)
print(B.decode())

print(B.find('eg'))
print(B.replace('eg','fa'))
print(B.decode())
print(B.upper())
print(B.decode())
print(B.lower())
print(B.decode())

print(B.reverse())
print(B.decode())
print(B.reverse())
print(B.decode())

J=' aaa,bbb,ccc,ddd '
print(J)
print(J.split(','))
print(J.strip().split(','))
print(dir(J))



