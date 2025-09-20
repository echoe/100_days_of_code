from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")
FILENAME = "data.txt"

class Scoreboard(Turtle):
    """Keep score for the snake game.
    Variables:
    -score: The score you've achieved in the snake game.
    -high_score: The high score.
    Functions:
    -add_score: Add a score to the score variable, and update the scoreboard.
    -update_scoreboard: Write details of the score to the scoreboard. Called by other methods.
    -reset: Check for a high score. Write it into a file if there isn't one.Then reset the scoreboard to the start of the game so the player can play again."""
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        with open(FILENAME,"r") as data: # Change this location if you are running elsewhere, haha. My 
            self.high_score = int(data.read())
        self.pu()
        self.ht()
        self.setpos(y=270,x =0)
        self.update_scoreboard()
    
    def add_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.score} High Score = {self.high_score}", False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(FILENAME,"w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()