from turtle import Screen, Turtle
from paddle import PaddleClass
from ball import BallClass
from score import ScoreBoard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Ping Pong")
screen.tracer(0)

player1 = PaddleClass()
player2 = PaddleClass()
ball = BallClass()
scoredisplay = ScoreBoard()

player1.goto(-380, 0)
player2.goto(380, 0)

screen.listen()

screen.onkeypress(player1.paddleup, "w")
screen.onkeypress(player1.paddledown, "s")
screen.onkeypress(player2.paddleup, "Up")
screen.onkeypress(player2.paddledown, "Down")

game_active = True
while game_active:
    screen.update()
    ball.move()
    time.sleep(0.05)

    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce()

    if ball.distance(player2) < 35 and ball.xcor() > 340 or ball.distance(player1) < 35 and ball.xcor() < -340:
        ball.rebound()

    if ball.xcor() > 390:
        ball.reset()
        scoredisplay.left_score_point()

    if ball.xcor() < -390:
        ball.reset()
        scoredisplay.right_score_point()

    if scoredisplay.l_score > 5 or scoredisplay.r_score > 5:
        game_active = False

screen.exitonclick()