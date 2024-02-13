from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 1.2


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.move_speed = 0.1

    def create_cars(self):
        random_choice = random.randint(1, 10)
        if random_choice == 1:
            car = Turtle("square")
            car.color(random.choice(COLORS))
            car.shapesize(1, 2)
            car.penup()
            car.setheading(180)
            random_y = random.randrange(-250, 250, 20)
            car.goto(300, random_y)
            self.all_cars.append(car)

    def move_left(self):
        for car in self.all_cars:
            car.forward(STARTING_MOVE_DISTANCE)

    def speedup_cars(self):
        self.move_speed /= MOVE_INCREMENT
