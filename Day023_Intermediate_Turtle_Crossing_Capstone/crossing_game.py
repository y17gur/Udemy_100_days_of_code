import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


def setup_screen():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.title("Turtle Crossing Capstone")
    screen.tracer(0)
    return screen


def main():
    screen = setup_screen()
    car_manager = CarManager()
    scoreboard = Scoreboard()
    player = Player()
    game_is_on = True

    while game_is_on:
        time.sleep(car_manager.move_speed)
        screen.update()
        screen.listen()
        screen.onkeypress(player.move_forward, "Up")

        car_manager.create_cars()
        car_manager.move_left()

        if player.finish_line():
            scoreboard.update_score()
            player.reset_player()
            car_manager.speedup_cars()

        for one_car in car_manager.all_cars:
            if player.distance(one_car) < 20:
                scoreboard.game_over()
                game_is_on = False

    screen.exitonclick()


if __name__ == "__main__":
    main()
