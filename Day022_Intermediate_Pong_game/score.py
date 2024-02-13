from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class Score(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x, y)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"{self.score}", False, ALIGNMENT, FONT)
        self.score += 1
