import math
import sys

#content =dir(math)
#print(content)

print("This is the name of the program:", sys.argv[0]) 
  
print("Argument List:", str(sys.argv)) 
numpars = len(sys.argv)

for x in range(0,numpars):
    print('Parameter number %d is: %s ', x, sys.argv[x] )
