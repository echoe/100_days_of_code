from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time

MOVE_INCREMENT = 0.9

screen = Screen()
screen.setup(width=600,height=600)
screen.tracer(0)

#Handle the cars.
car_manager = CarManager()

#Handle the player - instantiate it, then create the screen.
player = Player()
screen.listen()
screen.onkey(fun=player.move_up, key="Up")

#Handle the scoreboard.
scoreboard = Scoreboard()

is_game_on = True
count = 0
faster = 1
while is_game_on == True:
    count += 1
    if count % 6 == 0:
        car_manager.create_car()
    if car_manager.collision(player):
        scoreboard.game_over()
        is_game_on = False
    if player.goal():
        scoreboard.update()
        player.reset()
        faster *= MOVE_INCREMENT
    time.sleep(0.1 * faster)
    car_manager.move_cars()
    screen.update()
#Show game over screen.
screen.exitonclick()