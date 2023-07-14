from turtle import Turtle


class PaddleClass(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()

    def paddleup(self):
        new_y = self.ycor() + 20
        if new_y < 280:
            self.goto(self.xcor(), new_y)

    def paddledown(self):
        new_y = self.ycor() - 20
        if new_y > - 280:
            self.goto(self.xcor(), new_y)

