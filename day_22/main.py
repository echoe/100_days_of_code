from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

#Create the playing field and set required settings
my_screen = Screen()
my_screen.setup(width=800, height=600)
my_screen.bgcolor("black")
my_screen.title("Ping, Pong, Ping, Pong")
my_screen.tracer(0)

#Make a paddle.
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

#Make a ball.
ball = Ball()

#Make a scoreboard.
scoreboard = Scoreboard()

#Move the paddle.
my_screen.listen()
my_screen.onkey(fun=r_paddle.paddle_up, key="Up")
my_screen.onkey(fun=r_paddle.paddle_down, key="Down")
my_screen.onkey(fun=l_paddle.paddle_up, key="w")
my_screen.onkey(fun=l_paddle.paddle_down, key="s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    my_screen.update()
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with paddle
    if ball.distance(r_paddle) < 40 and ball.xcor() > 320 or ball.distance(l_paddle) < 40 and ball.xcor() < -320:
        ball.bounce_x()

    #Detect ball miss
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset()
        scoreboard.r_point()

my_screen.exitonclick()