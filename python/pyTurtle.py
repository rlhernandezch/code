#!/usr/bin/python

import sys
import turtle

print(sys.version)

window= turtle.Screen()
window.bgcolor("Wheat")
Brad = turtle.Turtle()

Brad.shape("turtle")
Brad.color("navyblue")

for i in range(0,36):
    Brad.forward(100)
    Brad.right(90)
    Brad.forward(100)
    Brad.right(90)
    Brad.forward(100)
    Brad.right(90)
    Brad.forward(100)
    Brad.right(100)

Brad.hideturtle()
window.exitonclick()
