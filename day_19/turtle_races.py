"""Bet on turtle races!"""
from turtle import Turtle, Screen #See stuff.
import random #Every turtle has a random speed.
# TODO: Create the screen.
# TODO: Make a random turtle.
# TODO: Give the turtle a random speed.
# TODO: Make the turtle move forwards.
# TODO: Make the player able to bet on turtles. Whole monetary system.
# TODO: Other stuff.

my_screen = Screen()
my_screen.colormode(255)


def random_turtle(start_position):
    """Create a random turtle with a random color. Outputs the turtle.
    Input: The start position of the turtle, so the turtles can all compete."""
    my_turtle = Turtle()
    my_turtle.shape("turtle")
    my_turtle.color((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    my_turtle.pu()
    my_turtle.backward(200)
    my_turtle.left(90)
    my_turtle.backward(200)
    my_turtle.forward(start_position)
    my_turtle.right(90)
    return my_turtle 

turtle_num = my_screen.textinput("How many turtles do you want to race?: ")
turtle_guess = my_screen.textinput(f"Which turtle do you think will win, numerically? Guess a number from 1 to {turtle_num}.")
list_of_turtles = []
for i in range(0, int(turtle_num)):
    list_of_turtles.append(random_turtle(i * 20))

print("And they're off!!!!")
race_happening = True
winner = ""
while race_happening:
    for turtle in list_of_turtles:
        turtle.forward(random.randint(1,10))
        # print(turtle.pos())
        if turtle.pos()[0] >= 320:
            winner = list_of_turtles.index(turtle)
            race_happening = False
            print(f"Turtle {winner} is the winner!")


if int(winner) == int(turtle_guess):
    print("You guessed right! You win!")
else:
    print("You were wrong. You lose!")

my_screen.exitonclick()