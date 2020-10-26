#!/usr/bin/python

import tkinter as tk
from tkinter import messagebox


top = tk.Tk()
top.geometry("800x600")
top.title("Super ventana!")


def helloCallBack():
    msg = tk.messagebox.showinfo("Hello Python", "Hello world")
    

B = tk.Button(top, text = "Hello", command = helloCallBack)
B.place(x = 50, y = 50)

C = tk.Canvas(top, bg = "blue", height = 250, width = 300)

coord = 10,50,240,210
arc = C.create_arc(coord, start = 0, extent = 150,  fill = 'red')
line = C.create_line(10,10,200,200,fill = 'white')
C.pack()

ckBtnVar1 = tk.IntVar()
ckBtnVar2 = tk.IntVar()

D = tk.Checkbutton(top, text = "Music", variable = ckBtnVar1, onvalue = 1, offvalue = 0 , height = 5, width = 20)
E = tk.Checkbutton(top, text = "Gaming", variable = ckBtnVar2, onvalue = 1, offvalue = 0 , height = 5, width = 20)
#D.place(x= 100,y = 100)
D.pack()
E.pack()

L1 = tk.Label(top, text = "User Name")
L1.pack(side = tk.LEFT)
vlEntryText = tk.Text()
vlEntry01 = tk.Entry(top, bd= 5)
vlEntry01.pack(side = tk.RIGHT)


top.mainloop()
