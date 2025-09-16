"""Let's play Snake!
I wrote this while testing if I could make this myself, without the walkthrough, on a plane. It's inaccurate :) But was a good experience."""

from turtle import Turtle, Screen
import time

mysnake = Turtle("square") # The game character
mybounds = Turtle() # The turtle that creates the bounds of the game.
screen = Screen()

#Draw the playfield. We'll do 160x160
mybounds.pu()
mybounds.right(90)
mybounds.forward(160)
mybounds.right(90)
mybounds.forward(160)
mybounds.pd()
for i in range(0,4):
    mybounds.right(90)
    mybounds.forward(320)
screen.tracer(0)

# Make the functions and onkey commands to move the snake.
def head_up():
    segments[0].seth(90)

def head_down():
    segments[0].seth(-90)

def head_left():
    segments[0].seth(180)

def head_right():
    segments[0].seth(0)

#Create snake segments.
starting_positions = [(0,0),(-20,0),(-40,0)]

segments = []

for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.pu()
    new_segment.color("black")
    new_segment.goto(position)
    segments.append(new_segment)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for seg_num in range(len(segments)-1,0,-1):
        segments[seg_num].goto(segments[seg_num-1].pos())
    segments[0].forward(20)
    if segments[0].pos()[0] > 160 or segments[0].pos()[0] < - 160 or segments[0].pos()[1] > 160 or segments[0].pos()[1] < - 160:
        print("Oh no, you crashed!")
        game_is_on = False
screen.exitonclick()