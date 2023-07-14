from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-275, 200)
        self.write(self.l_score, font=("impact", 32, "normal"))
        self.goto(275, 200)
        self.write(self.r_score, font=("impact", 32, "normal"))

    def left_score_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def right_score_point(self):
        self.r_score += 1
        self.update_scoreboard()
