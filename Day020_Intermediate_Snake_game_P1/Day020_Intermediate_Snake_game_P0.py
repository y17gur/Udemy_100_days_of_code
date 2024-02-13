from turtle import Turtle, Screen
import random
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# x_position = 0
# for i in range(1, 3+1):
#     snake = Turtle(shape="square")
#     snake.penup()
#     snake.color("white")
#     snake.goto(x=x_position, y=0)
#     x_position += 20

segments = []
start_position = [(0, 0), (-20, 0), (-40, 0)]

for position in start_position:
    snake = Turtle(shape="square")
    snake.color("white")
    snake.penup()
    snake.goto(position)
    segments.append(snake)

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    # for seg in segments:
    #     seg.fd(20)
    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].fd(20)





screen.exitonclick()
