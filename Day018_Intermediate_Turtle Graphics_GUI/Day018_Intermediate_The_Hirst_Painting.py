import turtle
from turtle import Turtle, Screen
import random

# import colorgram
#
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)


# print(rgb_colors)

color_list = [(213, 131, 110), (3, 14, 31), (51, 27, 19), (18, 104, 155), (149, 81, 43), (240, 212, 74), (212, 88, 67), (164, 162, 36), (153, 10, 28), (154, 64, 101), (177, 136, 157), (203, 76, 105), (93, 8, 21), (13, 64, 34), (14, 93, 56), (13, 175, 213), (3, 63, 142), (19, 133, 85), (153, 28, 20), (14, 207, 200), (146, 225, 214), (123, 191, 155), (124, 169, 191), (107, 219, 229), (221, 177, 208), (82, 134, 176)]
tim = Turtle()
tim.speed(20)
tim.penup()
tim.hideturtle()
turtle.colormode(255)

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = Screen()
screen.exitonclick()
