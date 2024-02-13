from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_pos=0, y_pos=0):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.penup()
        self.goto(x_pos, y_pos)

    def up(self):
        if self.ycor() < 240:
            self.sety(self.ycor() + 25)

    def down(self):
        if self.ycor() > -240:
            self.sety(self.ycor() - 25)

