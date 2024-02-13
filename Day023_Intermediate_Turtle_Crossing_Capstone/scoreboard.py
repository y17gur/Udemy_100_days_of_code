from turtle import Turtle

ALIGNMENT = "left"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-290, 260)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Level: {self.score}", False, ALIGNMENT, FONT)
        self.score += 1

    def game_over(self):
        self.goto(-50, 0)
        self.write(f"GAME OVER!", False, ALIGNMENT, FONT)
