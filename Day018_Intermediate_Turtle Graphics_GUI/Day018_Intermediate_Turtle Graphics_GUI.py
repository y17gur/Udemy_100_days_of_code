import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
turtle.colormode(255)
directions = [0, 90, 180, 270]

tim.speed(20)

# colors = ["red", "green", "red", "dodger blue", "lime", "magenta", "blue violet", "indigo", "yellow", "orange",
#           "medium violet red", "dark slate blue", "hot pink", "salmon", "pale violet red", "purple", "royal blue",
#           "light sky blue"]

# tim.pensize(15)


# def draw(num):
#     tim.color(random.choice(colors))
#     for _ in range(num):
#         tim.forward(100)
#         tim.right(360/num)
#
#
# for i in range(3, 10):
#     draw(i)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


# for i in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

# for i in range(100):
#     tim.color(random_color())
#     tim.circle(100)
#     tim.setheading(tim.heading() + 10)

def draw_spirograph(size_of_gap):
    for i in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)








screen = Screen()
screen.exitonclick()
