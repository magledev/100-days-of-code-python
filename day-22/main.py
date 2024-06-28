# Pong game clone

from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Clone")
screen.tracer(0)

scoreboard = Scoreboard()
left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))
ball = Ball()

screen.listen()
screen.onkey(left_paddle.paddle_up, "w")
screen.onkey(left_paddle.paddle_down, "s")
screen.onkey(right_paddle.paddle_up, "Up")
screen.onkey(right_paddle.paddle_down, "Down")

game_is_live = True
while game_is_live:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with top and bottom of screen
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect if ball is out of bounds
    if ball.xcor() > 380:
        ball.reset_ball()
        scoreboard.left_point()

    if ball.xcor() < -380:
        ball.reset_ball()
        scoreboard.right_point()

screen.exitonclick()
