#!/usr/bin/python

from tkinter import *
from tkinter import messagebox

top = Tk()
top.geometry("250x250+10+10")

def doMaths(vl1=E2.text,vl2=E3.text):
    messagebox.showinfo("Say hello", str(int(vl1)+int(vl2)) )


L1 = Label(top, text = "Physics")
L1.place (x = 10, y = 10)
E1 = Entry(top, bd = 5)
E1.place(x = 60, y = 10)
L2 = Label(top,text="Maths")
L2.place(x = 10, y = 50)
E2 = Entry(top, bd = 5)
E2.place(x = 60, y = 50)

L3 = Label(top,text = "Total")
L3.place(x = 10, y = 150)
E3 = Entry(top, bd = 5)
E3.place(x = 60, y = 150)


B = Button(top, text = "Add", command = doMaths )
B.place(x = 100, y = 100)

top.mainloop()