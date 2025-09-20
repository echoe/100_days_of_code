from turtle import Turtle
import random

class Food(Turtle):
    """Create food for the snake game.
    Food is created at a random place.
    Functions:
    -refresh: Refresh where the food is created. Only one food should be created at a time,
    as this can make two food items in the exact same spot.
    Food is spawned in a random square of the board."""
    def __init__(self):
        """Creates a food icon."""
        super().__init__()
        self.shape("circle")
        self.pu()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()
    
    def refresh(self):
        """Refreshes the food to a new place. Rounds to ensure this is on the grid."""
        random_x = round(random.randint(-13,13))*20
        random_y = random.randint(-13,13)*20
        self.goto(random_x, random_y)