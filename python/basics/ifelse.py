#!/usr/bin/python

check=None

if check == False:
    print ("If")    
elif check == True:
    print("elif")
else:
    print("Else")

MyArray=[1,2,3,4,5,6,7]

#For loop
for item in MyArray:
    print(item)

run = True
current = 1

while run:
    if current == 100:
        run = False
    else:
        print(current)
        current += 1


if math.isclose(math.sqrt(2)**2,2, rel_tol=1e-09) == True:
    print("Se aproxima")
else:
    print("No se aproxima")
    
