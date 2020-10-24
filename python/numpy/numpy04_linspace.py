#!/user/bin/python
import numpy as np

x = np.linspace(10,20,5)

x2 = np.linspace(10,20,5,endpoint = False)
print(x2)


x3 = np.linspace(1,2,5,retstep = True)
print(x3)