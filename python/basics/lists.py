#!/usr/bin/python
#Arrays
MyArray=["MOVIES","GAMES","PYTHON","FOOD"]
print(["MOVIES","GAMES","PYTHON","FOOD"][3])

#Dicctionaries
MyDic={"name":"Ricardo","age":40,"hobby":"Gamming"}
print(MyDic["hobby"])

M = ['cc','bb','aa']
print ("Antes de ordenar")
print(M)
M.sort()
print ("Despues de ordenar")
print(M)



__NList = [ [1,2,3],
            [4,5,6],
            [7,8,9]]

print(__NList)
print(__NList[1][1])



__MyRecord = {'name': {'first':'John','last': 'Smith'},
                'jobs': ['dev','mrg'],
                'age':40.5
                }

print(__MyRecord['name']['first'])
print(__MyRecord['jobs'])
print(__MyRecord['jobs'][-1])

__MyRecord['jobs'].append('Project Leader')
print(__MyRecord['jobs'])



for c in 'my string':
    print(c.upper())    