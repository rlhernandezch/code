#!/usr/bin/python

from tkinter import *

def donothing():
    filewin = TopLevel(root)
    button = Button(filewin, text = "Do nothing button")
    button.pack()

root = Tk()
menubar = Menu(root)
filemenu = Menu(menubar, tearoff = 0)
