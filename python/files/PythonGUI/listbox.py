#!/usr/bin/python 

from tkinter import *

top = Tk()

Lb1 = Listbox(top)
Lb1.insert(1, 'option 1')
Lb1.insert(2, 'option 2')
Lb1.insert(3, 'option 3')
Lb1.insert(4, 'option 4')
Lb1.insert(5, 'option 5')

Lb1.pack()
top.mainloop()