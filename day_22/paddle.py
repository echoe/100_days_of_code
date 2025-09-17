from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.pu()
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.goto(position)

    def paddle_up(self):
        self.setpos(self.xcor(),self.ycor()+20)

    def paddle_down(self):
        self.setpos(self.xcor(),self.ycor()-20)