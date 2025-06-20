from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 35, "bold")

class Scoreboard(Turtle):
    def __init__(self,position):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.setpos(position)
    def display_score(self,score):
        self.clear()
        self.write(arg=f"{score}", align=ALIGNMENT, font=FONT)
    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER !", align=ALIGNMENT, font=FONT)
    def display_line(self):
        self.setheading(270)
        # self.pensize(2)
        while self.ycor() > -300:
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)




