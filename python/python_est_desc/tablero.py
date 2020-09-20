#!/usr/bin/python

#A,C,E,G: Negras  para Non
#A,C,E,G: Blancas para Par
#B,D,F,H: Blancas para Non
#B,D,F,H: Negras para Par


def fn_color_casilla(numero,letra):
    switch = {
        "A":1,
        "B":2,
        "C":3,
        "D":4,
        "E":5,
        "F":6,
        "G":7,
        "H":8,
    }
    vlNumLetra= switch.get(letra)
    
    if (vlNumLetra%2 == 0):
        if (numero%2 == 0):
            print("NEGRA")
        else:
            print("BLANCA")
    else:
        if (numero%2 == 0):
            print("BLANCA")
        else:
            print("NEGRA")


fn_color_casilla(1,"A")
        