from turtle import Turtle, Screen
import random

is_rase_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = None

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

while not user_bet:
    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win?")
    if user_bet not in colors:
        print("There is no such color!")
        user_bet = None


y_position = 80
for color in colors:
    race_turtle = Turtle(shape="turtle")
    race_turtle.penup()
    race_turtle.color(color)
    race_turtle.goto(x=-240, y=y_position)
    y_position -= 40
    all_turtles.append(race_turtle)

if user_bet:
    is_rase_on = True

while is_rase_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winner = turtle.pencolor()
            is_rase_on = False
            if winner == user_bet:
                print(f"You have won! The winner is {winner}!")
            else:
                print(f"You have lost! The winner is {winner}!")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
