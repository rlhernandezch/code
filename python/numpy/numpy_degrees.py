#!/user/bin/python
import numpy as np

a = np.array([0,30,45,60,90])

print('Array containing sine values')
sin = np.sin(a*np.pi/180)
print(sin)
print('\n')


print('Compute sins inverse of angles. Returnes values are in radians.')
inv = np.arcsin(sin)
print(inv)
print('\n')

print('Check result by converting to degrees:')
print (np.degrees(inv))
print('\n')

print ('Arcos and arctan functions behave similarly:')
cos = np.cos(a*np.pi/180)
print(cos)
print('\n')


print ('Inverse of cos:')
inv = np.arccos(cos)
print('\n')

print('In degrees:')
print(np.degrees(inv))
print('\n')

print('Tan function:')
tan = np.tan(a*np.pi/180)
print(tan)
print('\n')

print('Inverse of tan')
inv = np.arctan(tan)
print(inv)
print('\n')