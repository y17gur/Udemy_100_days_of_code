from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 9, "normal")


class States(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()

    def update_text(self, x, y, state):
        self.goto(x, y)
        self.write(state, False, ALIGNMENT, FONT)
