#!/usr/bin/python

import tkinter as tk
from tkinter import messagebox


top = tk.Tk()
top.geometry("100x100")

def hello():
    messagebox.showinfo("Say hello", "Hello world")

B1 = tk.Button(top, text = "Say Hello", command = hello)
B1.place(x = 35, y = 50)
top.mainloop()