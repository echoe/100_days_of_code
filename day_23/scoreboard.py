FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.ht()
        self.color("black")
        self.score = -1 #This is so it is turned to 0 on the first update
        self.goto(-200,240)
        self.update()

    def update(self):
        """Updates the scoreboard."""
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align="left", font=FONT)

    def game_over(self):
        """Shows game over."""
        self.goto(0,0)
        self.write(f"Game Over", align="center", font=FONT)