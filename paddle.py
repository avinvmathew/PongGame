from turtle import Turtle, Screen

# from main import paddle_right

rectangle_shape = (
    (-10, 10),  # Top-left
    (10, 10),   # Top-right
    (10, -90),  # Bottom-right
    (-10, -90)  # Bottom-left
)

screen = Screen()
screen.register_shape("rectangle", rectangle_shape)

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.count = 0
        self.penup()
        self.shape("rectangle")
        self.color("white")
        self.setheading(90)
        self.setpos(position)

    def move_paddle_up(self):
        if self.ycor() < 290:
            self.forward(20)
    def move_paddle_down(self):
        if self.ycor() > -200:
            self.backward(20)

        



