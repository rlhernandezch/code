#!/usr/bin/python

import random
import os

CurDirectory = os.getcwd()

def myFunction (p1,p2,p3):
    print(p1 +" "+ p2 +" "+ p3)

def fn_sum_val(p1,p2):
    return p1+p2

filename = CurDirectory+'/'+'list.txt'

with open(filename) as fp:
    mylin = fp.readline()
    while mylin:
        print(mylin)
        mylin = fp.readline()
