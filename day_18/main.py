from turtle import Turtle, Screen
from random import randint
"""I really love how this course breaks stuff into digestable chunks and need to remember to do this myself.
IE: first you draw a square with turtle, then you expand from there. simple to harder.
The course expects you to make a list and pull from it but I would much rather 
just pull random integers, so I did that instead, first. Course eventually got there :)"""

tim = Turtle()
tim.shape("triangle")
tim.color("black")
screen = Screen()
screen.colormode(255)
def square():
    for turn in range(0,4):
        tim.right(90)
        tim.forward(100)

def dotted_line(dots, dot_length):
    """Draw a dotted line.
    Dots: The number of dots in your dotted line.
    Dot length: the size of each 'dot' in the line."""
    for _ in range(dots):
        tim.down()
        tim.forward(dot_length)
        tim.up()
        tim.forward(dot_length)

def draw_polygon(sides, length):
    """Draw a polygon.
    Sides: The number of sides.
    Length: The length of each side.
    All things drawn with random colors."""
    for _ in range(sides):
        tim.forward(length)
        tim.right(360/sides)

def random_walk(step_size, steps, random_color=True):
    """Take a random walk.
    step_size: the size of each step forwards.
    steps: The number of steps in the walk.
    random_color: Boolean, whether or not you want a random color on each step."""
    for _ in range(0,steps):
        if random_color:
            tim.color((randint(0,255),randint(0,255),randint(0,255)))
        tim.right(randint(0,4)*90)
        tim.forward(step_size)
    
def spirograph(circle_radius, gap, random_color = True):
    """Draws a spirograph.
    circle_radius: radius of each circle
    gap: size of the gap between each circle
    random_color: whether or not you want to have a random color on each circle"""
    for _ in range(0,int(360/gap)):
        if random_color:
            tim.color((randint(0,255),randint(0,255),randint(0,255)))        
        tim.circle(circle_radius)
        tim.left(gap)



tim.speed(0)
tim.ht()
# tim.width(10)

# square()
# dotted_line(50,10)
# for _ in range(3,11):
#     tim.color((randint(0,255),randint(0,255),randint(0,255)))
#     draw_polygon(_,100)
# random_walk(15,200)
spirograph(100,5)
#Needs to be at the bottom to keep the turtle drawing window open
screen.exitonclick()