from turtle import Turtle
from random import randrange, randint

class BallClass(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.y_move = 10
        self.x_move = 10

    def reset(self):
        self.goto(0, 0)
        self.rebound()

    def move(self):
        new_y = self.ycor() + self.y_move
        new_x = self.xcor() + self.x_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def rebound(self):
        self.x_move *= -1
