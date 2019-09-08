#!/usr/bin/python
import math 
import random

#To import a specific element from a module
#from dummod import myvar
#print(myvar)
#print (dummod.a,dummod.b,dummod.c,dummod.d)
#Print options from a module
#print(dir(dummod))

#Use module directly without import
#exec (open('dummod.py').read())
print(math.pi)

print(random.random())
print(random.choice([1,2,3,4]))

S='MyString'
vl = list(S)
print(vl)

for i in vl:
    print(i)

print(S.find('My'))
print(S.replace('String','Cadena'))
print(S.upper())
print(S.isalnum())

vlPipeVar = 'a|b|c|d|e'



