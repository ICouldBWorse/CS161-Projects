# Dustin Erickson
# 10-9-2021
# This program takes two inputs, the number of sides for a polygon and the fill color. It calculates the angle and it initiates Turtle. It then
# uses turtle to print a shape with the given number of sides and the color. It can also exit when the screen is clicked. With larger shapes
# it will print off screen because the length of the lines is too large.

import turtle           #imports the turtle modules

sides = int(input("Input the number of sides of the polygon: "))            #asks for an input for number of sides
color = input("Enter a fill color: ")           #asks for a fill color
angle = 360 / sides             #calculates the angle between lines
length = 50             #variable for the length of the lines
screen = turtle.getscreen()         #initiates turtle screen
t = turtle.Turtle()             #initiates turtle variable

t.pen(pencolor=color, fillcolor=color)      #sets the pen color and fill color to the input
t.begin_fill()          #begins the fill for the shape
for a in range(0,sides):            #for loop that prints the shape for the number of sides given
    t.fd(length)            #draws sides
    t.lt(angle)             #turns the turtle
t.end_fill()            #ends the fill
screen.exitonclick()        #fun thing I found that allows you to exit Turtle with just a click


#Sources: https://stackoverflow.com/questions/6234798/turtle-graphics-how-do-i-control-when-the-window-closes
