COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle
from random import choice, randint

class CarManager:
    def __init__(self):
        self.the_cars = []

    def create_car(self):
        """Create a new random car."""
        new_car = Turtle("square")
        new_car.color(choice(COLORS))
        new_car.resizemode("user")
        new_car.pu()
        new_car.seth(180)
        new_car.shapesize(1,2)
        new_car.goto(240,randint(-150,250))
        self.the_cars.append(new_car)
    
    def move_cars(self):
        """Move the cars across the screen on every refresh."""
        for car in self.the_cars:
            car.forward(5)

    def collision(self,player):
        """If the provided turtle object collides with any car, return True. Else, return False."""
        myresult = False
        for car in self.the_cars:
            if car.distance(player) < 20:
                myresult = True
        return myresult