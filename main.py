import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

paddle_right = Paddle((350, 0))
paddle_left = Paddle((-350, 0))
division = Scoreboard((0,300))
division.display_line()
ball = Ball()
scoreboard_left = Scoreboard((-180,250))
scoreboard_right = Scoreboard((180,250))


screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Arcade")

screen.listen()
screen.onkeypress(paddle_right.move_paddle_up, "Up")
screen.onkeypress(paddle_right.move_paddle_down, "Down")
screen.onkeypress(paddle_left.move_paddle_up, "w")
screen.onkeypress(paddle_left.move_paddle_down, "s")

is_game_on = True
right_player_points = 0
left_player_points = 0

sleep_time = 0.1
while is_game_on:
    screen.update()
    time.sleep(sleep_time)
    scoreboard_left.display_score(left_player_points)
    scoreboard_right.display_score(right_player_points)
    ball.move()

    #detect collision with wall(up and down to bounce)

    if not -285 < ball.ycor() < 285:
        ball.bounce_y()

    #detect collision with paddle
    if ball.distance(paddle_right) < 60 and ball.xcor() > 320 or ball.distance(paddle_left) < 60 and ball.xcor() < -320:
        print("collision")
        ball.bounce_x()

    #when right paddle misses
    if ball.xcor() > 370:
        ball.reset_position()
        left_player_points += 1
        sleep_time *= 0.9

    #when left paddle misses
    if ball.xcor() < -370:
        ball.reset_position()
        right_player_points += 1
        sleep_time *= 0.9



screen.exitonclick()