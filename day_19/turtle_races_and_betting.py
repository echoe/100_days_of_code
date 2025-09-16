"""Bet on turtle races! I resolved all the official TODOs here, and the one I made (add monetary system and betting),
but I kind of want to recreate Quibble Race from UFO 50. Perhaps in the future I'll come back to this one.
The sugggested screen size also seems a little large for my screen somehow so I may change that as well."""
from turtle import Turtle, Screen #See stuff.
import random #Every turtle has a random speed.

my_screen = Screen()
my_screen.colormode(255)
my_screen.setup(height = 500,width = 400)


def random_turtle(start_position):
    """Create a random turtle with a random color. Outputs the turtle.
    Input: The start position of the turtle, so the turtles can all compete."""
    my_turtle = Turtle("turtle")
    my_turtle.color((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    my_turtle.pu()
    my_turtle.setpos(-190,-190 + start_position)
    return my_turtle 

#Set variables to use throughout the game.
money = 100
keep_playing = "y"

#Start the game.
while keep_playing == "y":
    turtle_num = int(my_screen.textinput(title="Turtle Number", prompt="How many turtles do you want to race?: "))
    turtle_guess = int(my_screen.textinput(title = "Turtle Choice", prompt=f"Which turtle do you think will win, numerically? Guess a number from 1 to {turtle_num}: "))
    bet_amount = int(my_screen.textinput(title="Bet on your racer!", prompt = f"How much would you like to bet? You have {money} dollars: "))
    while bet_amount > money:
        bet_amount = int(my_screen.textinput(title="Try again", prompt = f"You cannot bet more than {money} dollars. Please place a different bet: "))
    list_of_turtles = []
    for i in range(0, turtle_num):
        list_of_turtles.append(random_turtle(i * 20))

    print("And they're off!!!!")
    race_happening = True
    winner = ""
    while race_happening:
        for turtle in list_of_turtles:
            turtle.forward(random.randint(1,10))
            # print(turtle.pos())
            if turtle.pos()[0] >= 320:
                winner = int(list_of_turtles.index(turtle)) + 1
                race_happening = False
                print(f"Turtle {winner} is the winner!")

    result = "right"
    if winner == turtle_guess:
        print("You guessed right! You win!")
        money += bet_amount * (turtle_num - 1)
    else:
        result = "wrong"
        money -= bet_amount
    keep_playing = my_screen.textinput(title="Result", prompt=f"You were {result}! You have {money} dollars. Would you like to continue playing? Type y to continue. Type anything else to save your winnings.")

my_screen.textinput(f"You ended the game with {money} dollars! Type anything to quit.")
# Make sure to make the game exit on click only.
my_screen.exitonclick()