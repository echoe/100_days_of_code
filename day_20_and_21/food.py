from turtle import Turtle
import random

class Food(Turtle):
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