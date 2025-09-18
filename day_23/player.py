STARTING_POSITION = (0, -200)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        """Create a turtle at the bottom of the screen, oriented towards the top of the screen."""
        super().__init__()
        self.shape("turtle")
        self.seth(90)
        self.pu()
        self.goto(STARTING_POSITION)
    def move_up(self):
        self.forward(MOVE_DISTANCE)
    def goal(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
    def reset(self):
        self.goto(STARTING_POSITION)