#!/usr/bin/python
#practica 6

maxnums=20

def fn_evalua_primo(i):
    j = 2
    while (j <= (i/j)):
        if not(i%j): 
            print (i, "No es Primo")
            break
        j = j+1
    if ( j > i/j) : print (i, "Es Primo")
   

def fn_evalua_par_non(x):
    if (x%2 == 0):
        print(x," es par")
    else:
        print(x," es non")

vlLista=[]
for i in range(0,maxnums):
    vlVal=int(input("Introduce el valor para %2d: " %(i)))
    vlLista.append(vlVal)

for i in range(0,maxnums):  
    fn_evalua_par_non(vlLista[i])
    fn_evalua_primo(vlLista[i])