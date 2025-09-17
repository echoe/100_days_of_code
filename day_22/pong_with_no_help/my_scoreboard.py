"""we take this scoreboard from the snake game and modify it to taste"""
from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.player_score = 0
        self.computer_score = 0
        self.pu()
        self.ht()
        self.setpos(y=270,x =0)
        self.update_scoreboard()
    
    def add_player_score(self):
        self.player_score += 1
        self.update_scoreboard()

    def add_computer_score(self):
        self.computer_score += 1
        self.update_scoreboard()        

    def update_scoreboard(self):
        self.clear()
        self.write(f"{self.player_score}        {self.computer_score}", False, align=ALIGNMENT, font=FONT)

    def game_over(self, win):
        """Writes whether you won or lost to the game screen."""
        self.goto(0,0)
        self.write(f"You {win}!", False, align=ALIGNMENT, font=FONT)