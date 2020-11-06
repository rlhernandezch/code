#!/usr/bin/python

from tkinter import *
from tkinter import messagebox


top = Tk()
def OpenWindow():
    NewWindow = Tk()
    NewWindow.geometry("250x250+10+10")   

    L1 = Label(NewWindow, text = "Physics")
    L1.place (x = 10, y = 10)
    E1 = Entry(NewWindow, bd = 5)
    E1.place(x = 60, y = 10)
    L2 = Label(NewWindow,text="Maths")
    L2.place(x = 10, y = 50)
    E2 = Entry(NewWindow, bd = 5)
    E2.place(x = 60, y = 50)

    L3 = Label(NewWindow,text = "Total")
    L3.place(x = 10, y = 150)
    E3 = Entry(NewWindow, bd = 5)
    E3.place(x = 60, y = 150)


    B = Button(NewWindow, text = "Add" )
    B.place(x = 100, y = 100)

    NewWindow.mainloop()
    

menubar = Menu(top)
file = Menu(menubar, tearoff=0)
file.add_command(label="New")
file.add_command(label="Open", command=OpenWindow)
file.add_command(label="Save")
file.add_command(label="Save as...")
file.add_command(label="Close")
file.add_separator()
file.add_command(label="Exit", command=top.quit)

menubar.add_cascade(label="File",menu=file)
edit = Menu(menubar, tearoff=0)
edit.add_command(label="Undo")

edit.add_separator()

edit.add_command(label="Cut")
edit.add_command(label="Copy")
edit.add_command(label="Paste")
edit.add_command(label="Delete")
edit.add_command(label="Select All")

menubar.add_cascade(label="Edit", menu=edit)
help = Menu(menubar, tearoff = 0)
help.add_command(label = "About")
menubar.add_cascade(label="Help", menu=help)

top.config(menu=menubar)
top.mainloop()
