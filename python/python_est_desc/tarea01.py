#!/usr/bin/python
import math

def fn_lee_real (x):
    if x >= 0:
        print("Positivo")
    else:
        print("Negativo")

def fn_lee_rango(x):
    if (x>=-5 and x<=5):
        print("Esta en rango")
    else:
        print("No esta en rango")

def fn_lee_x_y(x,y):
    if (x>0):
        if (y>0):
            print("Cuadrante I")
        else:
            print("Cuadrante IV")    
    else:
        if (y>0):
            print("Cuadrante II")
        else:
            print("Cuadrante III")
    
def fn_div_cociente (x,y):
    vlCoc=x/y
    vlResto=x % y
    return (vlCoc,vlResto)

def fn_cuad_perf(x):
    vlDecimales= math.sqrt(x)%1
    if (vlDecimales != 0):
        print("No es cuadrado perfecto")
    else:
        print("Cuadrado perfecto")


val1=int(input("Dame Valor 1:" ))
val2=int(input("Dame Valor 2:" ))
fn_lee_real(val1)
fn_lee_rango(val1)
fn_lee_x_y(1,1)
fn_lee_x_y(-1,1)
fn_lee_x_y(-1,-1)
fn_lee_x_y(1,-1)

val3=fn_div_cociente(val1,val2)
print ("Cociente:" +str(val3[0]) +" Resto:" +str(val3[1]))

fn_cuad_perf(8)
fn_cuad_perf(9)

#Punto 6
vlYr=[2000]
vlEsBiciesto = list(filter(lambda x: ( x%4==0 and x%100==0 and x%400==0), vlYr))
if vlEsBiciesto:
    print("Biciesto")
else:
    print("No Biciesto")



