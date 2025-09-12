import colorgram
from turtle import Turtle, Screen
import random
"""Making a Hirst Dots Picture, using a color palette from a jpg file from the internet.
Needs you to insert the FILENAME into this file to create the proper picture.
You may want to move the starting place of the drawing, depending on what you prefer."""
FILENAME = "YOUR_FILE_HERE"


# Pull the colors from the filename and convert them into the proper tuples for the turtle.
colors = colorgram.extract(FILENAME, 26)
colorslist = []
for color in colors:
    #Ignore the white and white-adjacent colors.
    if tuple(color.rgb)[0] > 240 and tuple(color.rgb)[1] > 240 and tuple(color.rgb)[2] > 240:
        pass
    else:
        colorslist.append(tuple(color.rgb))

#Set up the turtle to draw and the screen to be drawn on.
my_turtle = Turtle()
my_turtle.speed(0)
my_turtle.ht()
my_turtle.pu()
my_screen = Screen()
my_screen.colormode(255)

# Then, move the starting position and screen size to be able to see the entire grid.
# my_screen.screensize(1000,1000) This is an option if you want to do it.
# my_turtle.setheading(225)
# my_turtle.forward(300)
# my_turtle.setheading(0)
# You can also do it like this if you want.
# my_turtle.left(180)
# my_turtle.forward(200)
# my_turtle.left(90)
# my_turtle.forward(200)
# my_turtle.left(90)
# But this way does it based on whatever screen you are generating (it is still moved for taste, YMMV):
my_turtle.setheading(180)
my_turtle.forward(my_screen.window_width()/2 - 100)
my_turtle.setheading(270)
my_turtle.forward(my_screen.window_height()/2 - 100)
my_turtle.setheading(0)

def draw_dots_rectangle(x, y, dots, space):
    """Draw a rectangle of dots on a white background.
    x: number of dots in x axis
    y: number of dots in y axis
    dots: size of dots
    space: size of space between dots"""
    for _ in range(0, y):
        for __ in range(0,x):
            my_turtle.dot(dots,random.choice(colorslist))
            my_turtle.forward(space)
        my_turtle.left(90)
        my_turtle.forward(space)
        my_turtle.left(90)
        my_turtle.forward(space * x)
        my_turtle.left(180)

draw_dots_rectangle(10,10,20,50)
my_screen.exitonclick()