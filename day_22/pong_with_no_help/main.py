"""Pong Game, written by me with no help
-First: we want to code up the paddles. 'Make a paddle appear on the screen.'
Then, 'Make the paddle move up and down'
Then, 'Make another paddle on the other side'
Then, 'Make a ball move across the screen with some physics'
Then, 'Make the ball detect collision on the edges of the screen'
Then, 'Make the ball detect collision on paddles'
Then, 'Make the score change when the ball passes a paddle, and reset the game to play again, until you get to 7'
Then, 'Make the other paddle move depending on where the ball is'
-We want to code up collision on the paddles
-We want to code up the scoreboard
-We want to code up the ball
-Then, finally, we code up the evil paddle.
THIS MOSTLY WORKS. TODO: Fix collision, by turning the paddle into three segments like the snake, and then checking each segment"""
from turtle import Turtle, Screen
from random import randint
from my_scoreboard import Scoreboard
from my_paddle import Paddle
from my_ball import Ball
import time

#Create the playing field and set required settings
my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("Ping, Pong, Ping, Pong")
my_screen.tracer(0)

# Pull in the required classes
scoreboard = Scoreboard()
my_paddle = Paddle("player")
computer_paddle = Paddle("computer")
ball = Ball()

# Deal with movement.
my_screen.listen() # now we're listening!
my_screen.onkey(fun=my_paddle.up, key="Up")
my_screen.onkey(fun=my_paddle.down, key="Down")

#The Game Logic is here!
game_is_on = True
while game_is_on:
    my_screen.update()
    time.sleep(0.1)
    ball.move()

    #Detect collision with top and bottom wall.
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.up_down_bounce()

    #Detect collision with ball and paddle.
    for segment in my_paddle.segments:
        if segment.distance(ball) < 15:
            ball.left_bounce()
            
    for segment in computer_paddle.segments:
        if segment.distance(ball) < 15:
            ball.right_bounce()

    #Move computer paddle slowly.
    if computer_paddle.segments[1].ycor() > ball.ycor():
        computer_paddle.com_down()
    elif computer_paddle.segments[1].ycor() < ball.ycor():
        computer_paddle.com_up()

    #Detect collision with back and front wall, and do scoring and ending the game.
    if ball.xcor() > 280:
        scoreboard.add_player_score()
        if scoreboard.player_score > 6:
            game_is_on = False
            scoreboard.game_over("win")
        time.sleep(1)
        my_paddle.reset()
        computer_paddle.reset()
        ball.refresh()
    if ball.xcor() < -280:
        scoreboard.add_computer_score()
        if scoreboard.computer_score > 6:
            game_is_on = False
            scoreboard.game_over("lose")
        time.sleep(1)
        my_paddle.reset()
        computer_paddle.reset()
        ball.refresh()

my_screen.exitonclick()