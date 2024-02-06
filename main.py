from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.02)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) and ball.heading() < 180:
        if not ball.is_bouncing_paddle:
            ball.is_bouncing_paddle = True
            scoreboard.r_point()
            ball.bounce_x()
    elif (ball.distance(l_paddle) < 50 and ball.xcor() < -320) and ball.heading() > 180:
        if not ball.is_bouncing_paddle:
            ball.is_bouncing_paddle = True
            scoreboard.l_point()
            ball.bounce_x()
    else:
        ball.is_bouncing_paddle = False

    # Detect R paddle misses
    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset_position()

    # Detect L paddle misses
    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset_position()

    # Check if the game should end
    if scoreboard.l_score == 10:
        print("Left player wins!")
        game_is_on = False
    elif scoreboard.r_score == 10:
        print("Right player wins!")
        game_is_on = False

screen.exitonclick()
