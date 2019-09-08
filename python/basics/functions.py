#!/usr/bin/python

def my_function (p1,p2,p3):
    print(p1)
    print(p2)
    print(p3)

def my_keywordarg(p1="someone",p2="unknown"):
    print("my name is ",p1, "and my age is ",p2)    


def print_list(*myarrayparam):
    for person in myarrayparam:
        print("This is", person)

def ret_value(p1,p2):
    vl1=p1+p2
    return vl1


my_function("Hello","World!",5)
my_keywordarg("Hello",None)
my_keywordarg(p2=40)

print_list("ric","iyas","mau","ricky")

MyVal1=ret_value(5,6)
MyVal2=ret_value(9,9)

print("My val1:",MyVal1,"My val2",MyVal2)