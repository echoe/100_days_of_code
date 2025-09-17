from turtle import Turtle
import random
"""We take the food class from the snake game and modify it to taste"""

class Ball(Turtle):
    def __init__(self):
        """Creates a ball."""
        super().__init__()
        self.shape("round")
        self.pu()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("white")
        self.speed("fastest")
        self.refresh()
    
    def refresh(self):
        """Refreshes the ball to a new random place with random trajectory. Rounds to ensure this is on the grid."""
        random_x = round(random.randint(-4,4))*20
        random_y = random.randint(-4,4)*20
        headings = [45,135,225,315]
        self.seth(random.choice(headings))
        self.goto(random_x, random_y)

    def move(self):
        """move forward"""
        self.forward(20)

    def up_down_bounce(self):
        """Turn if you hit the wall and the ball is still in play"""
        if self.heading() == 45:
            self.seth(315)
        elif self.heading() == 315:
            self.seth(45)
        elif self.heading() == 135:
            self.seth(225)
        elif self.heading() == 225:
            self.seth(135)

    def left_bounce(self):
        """Turn if you hit a paddle"""
        if self.heading() == 135:
            self.seth(45)
        elif self.heading() == 225:
            self.seth(315)

    def right_bounce(self):
        """Turn if you hit a paddle"""
        if self.heading() == 45:
            self.seth(135)
        elif self.heading() == 315:
            self.seth(225)