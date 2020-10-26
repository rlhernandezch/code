#!/usr/bin/python

from tkinter import *

root = Tk()
frame = Frame(root)
frame.pack()



bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )

redbutton = Button (frame, text = "Red", fg = "red")
redbutton.pack(side = LEFT)

greenbutton = Button (frame, text = "Green", fg = "green")
greenbutton.pack(side = LEFT)

bluebutton = Button (frame, text = "Blue", fg = "blue")
bluebutton.pack(side = LEFT)

blackbutton = Button (frame, text = "Black", fg = "black")
blackbutton.pack(side = BOTTOM)


upFrame = Frame(root)
upFrame.pack( side = TOP )
Lb1 = Listbox(upFrame)
Lb1.insert(1, 'option 1')
Lb1.insert(2, 'option 2')
Lb1.insert(3, 'option 3')
Lb1.insert(4, 'option 4')
Lb1.insert(5, 'option 5')

Lb1.pack()


root.mainloop()
