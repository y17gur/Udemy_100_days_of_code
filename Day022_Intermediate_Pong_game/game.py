from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from score import Score


class PongGame:
    def __init__(self):
        self.screen = Screen()
        self.screen_setup()
        self.create_dashed_line()
        self.paddle_right = Paddle(370, 5)
        self.paddle_left = Paddle(-379, 5)
        self.ball = Ball()
        self.score_right = Score(50, 270)
        self.score_left = Score(-50, 270)

        self.screen.listen()
        self.screen.onkeypress(self.paddle_right.up, "Up")
        self.screen.onkeypress(self.paddle_right.down, "Down")
        self.screen.onkeypress(self.paddle_left.up, "q")
        self.screen.onkeypress(self.paddle_left.down, "a")

    def screen_setup(self):
        self.screen.setup(width=800, height=610)
        self.screen.bgcolor("black")
        self.screen.title("Pong Game")
        self.screen.tracer(0)

    def create_dashed_line(self):
        line = Turtle()
        line.color("white")
        line.penup()
        line.goto(0, 290)
        line.setheading(270)
        line.pendown()

        for _ in range(30):
            line.forward(10)
            line.penup()
            line.forward(10)
            line.pendown()

    def run_game(self):
        game_on = True
        while game_on:
            self.screen.update()
            time.sleep(self.ball.move_speed)
            self.ball.move()

            # Collision detection
            if self.ball.ycor() > 289 or self.ball.ycor() < -279:
                self.ball.bounce_y()

            if (
                self.ball.distance(self.paddle_right) < 50
                and self.ball.xcor() > 340
            ):
                self.ball.bounce_x()
            elif (
                self.ball.distance(self.paddle_left) < 50
                and self.ball.xcor() < -350
            ):
                self.ball.bounce_x()
            elif self.ball.xcor() > 400:
                self.score_left.update_score()
                self.ball.reset_ball()
            elif self.ball.xcor() < -400:
                self.score_right.update_score()
                self.ball.reset_ball()


if __name__ == "__main__":
    pong_game = PongGame()
    pong_game.run_game()
    pong_game.screen.exitonclick()
