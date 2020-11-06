import sys
import turtle

# Funciones

# Habilitando 2 Turtles en paralelo

def TwoTurtles():
    window=turtle.Screen()
    window.bgcolor("Wheat")
    Brad=turtle.Turtle()
    Sam=turtle.Turtle()

    Brad.shape("turtle")
    Sam.color("navyblue")
    Sam.shape("turtle")
    Sam.color("navyblue")
    Sam.right(180)
    
    # Dibujando dos cuadrados
    #for i in range(0,4):
        #for j in range(0,90):
            #Sam.forward(1)
            #Brad.forward(1)
        
        #Brad.right(90)
        #Sam.left(90)

    # Dibujando dos circulos
    for k in range(0,90):    
        Sam.circle(90,4)
        Brad.circle(90,4)

    
    Sam.hideturtle()
    Brad.hideturtle()
    
    Angie=turtle.Turtle()
    Angie.color("red")
    Angie.shape("turtle")
    Angie.right(120)
    Angie.forward(157)
    
    Angie.left(120)
    Angie.forward(157)

    Angie.left(120)
    Angie.forward(157)
    
    Angie.left(150)
    Angie.forward(180)
    
    Angie.hideturtle()

    
    window.exitonclick()

# Main

print(sys.version)    
TwoTurtles()