from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
screen.listen()


# w = forwards
def move_forwards():
    tim.forward(10)


# s = backwards
def move_backwards():
    tim.back(10)


# a = counter_clockwise
def move_counter_clockwise():
    tim.left(15)


# d = clockwise
def move_clockwise():
    tim.right(15)


# c = clear_all
def clear_all():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_counter_clockwise)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="c", fun=clear_all)
screen.exitonclick()
