import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball

paddle_right = Paddle((350, 0))
paddle_left = Paddle((-350, 0))
ball = Ball()

screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Arcade")

screen.listen()
screen.onkey(paddle_right.move_paddle_up, "Up")
screen.onkey(paddle_right.move_paddle_down, "Down")
screen.onkey(paddle_left.move_paddle_up, "w")
screen.onkey(paddle_left.move_paddle_down, "s")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    ball.move()

    #detect collision with wall

    if not -285 < ball.ycor() < 285:
        ball.bounce_y()

    #detect collision with paddle
    if ball.distance(paddle_right) < 50 and ball.xcor() > 320 or ball.distance(paddle_left) < 50 and ball.xcor() < -320:
        print("collision")
        ball.bounce_x()

    if ball.xcor() > 370 or ball.xcor() < -370:
        ball.setpos(0,0)
        ball.bounce_x()

screen.exitonclick()