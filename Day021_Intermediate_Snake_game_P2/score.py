from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.goto(0, 268)
        self.update_score()
        self.update_text()

    def update_score(self):
        self.clear()
        self.score += 1
        self.update_text()

    def update_text(self):
        self.write(f"Score: {self.score}", False, ALIGNMENT, FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER!", False, ALIGNMENT, FONT)
