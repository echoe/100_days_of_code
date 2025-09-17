from turtle import Turtle
"""We take the snake from the snake game and modify it to taste"""
PLAYER_STARTING_POSITIONS = [(-200,0),(-200,20),(-200,40)]
COMPUTER_STARTING_POSITIONS = [(200,0),(200,20),(200,40)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Paddle:
    def __init__(self, player):
        """Create the paddle. The paddle will be made out of three segments because it looked better and you can use it
        for collision sometimes (I tried the stretch option but it was not working with collision well).
        player must be a string that is either 'player' or 'computer'."""
        self.segments = []
        self.player = player
        self.paddle = self.create_paddle()

    def create_paddle(self):
        if self.player == "player":
            for position in PLAYER_STARTING_POSITIONS:
                self.add_segment(position)
        elif self.player == "computer":
            for position in COMPUTER_STARTING_POSITIONS:
                self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.pu()
        new_segment.color("white")
        new_segment.goto(position)
        new_segment.seth(90)
        self.segments.append(new_segment) 

    def reset(self):
        """Reset position of paddles."""
        count = 0
        if self.player == "player":
            for position in PLAYER_STARTING_POSITIONS:
                self.segments[count].setposition(position)
                count += 1
        elif self.player == "computer":
            for position in COMPUTER_STARTING_POSITIONS:
                self.segments[count].setposition(position)
                count += 1

    def up(self):
        for segment in self.segments:
            segment.forward(40)

    def down(self):
        for segment in self.segments:
            segment.backward(40)

    def com_up(self):
        for segment in self.segments:
            segment.forward(10)

    def com_down(self):
        for segment in self.segments:
            segment.backward(10)