#!/usr/bin/python
#import regexp
import re

def fn_sum (x,y):
    return x+y

def fn_sub (x,y):
    return x-y

def fn_mul (x,y):
    return x*y

def fn_div (x,y):
    return x/y

def fn_menu():
    print ("Select Operation")
    print ("0. Exit")
    print ("1. Sum")
    print ("2. Rest")
    print ("3. Mult")
    print ("4. Div")
    
Keep = True

while Keep:
    fn_menu()
    choice = str(input("Enter Value:"))
    print ("Your choice is:"+str(choice))
    
    if choice != "0":
        num1= int(input("Enter first number:"))
        num2= int(input("Enter second number:"))

    if choice == "1":
        print(fn_sum(num1,num2))
    elif choice == '2':
        print(fn_sub(num1,num2))
    elif choice == '3':
        print(fn_mul(num1,num2))
    elif choice == '4':
        print(fn_div(num1,num2))
    elif choice == "0":
        Keep = False

    
