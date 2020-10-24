#/user/bin/python

print('List example:')
myList = [1,2,3,'abc']
print (myList)
myList.append('mau')
print (myList[0:0])
print (myList[0:1])
print (myList[0:2])
print (myList[0:3])

print('Tuple example')
myToup = (1, 2, 2, 2, 3, 'abc')
print (myToup[0:0])
print (myToup[0:1])
print (myToup[0:2])
print (myToup[0:3])
print (myToup.count(2))
print (len(myToup))

print ("Example Dictionary")

dict = {'Name': 'Ricardo',
        'Age': 41,
        'DOB' : '08/jul/1979'
        }
print(dict['Name'])
dict['POB'] = 'Alvarado'
print(dict['POB'])
del dict['Name']
print(dict)