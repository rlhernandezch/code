import os
import sys


def my_function(one,    two, 
                three,  four, 
                five,   six):
    print("Hello World",one,two,three,four,five,six)


def second_function():
    print("Second Function")


def fn_hello_name(p1='dummy'):
    print("Hello "+p1)


my_list=[1, 2,
         3, 4,
         5, 6]

my_function(1,2,3,4,5,6)
fn_hello_name()


check = False

if check is True:
    print("Is true")
else:
    print("Is false")

