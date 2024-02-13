from game_data import data
from art import vs, logo
import random


def get_random_person():
    return random.choice(data)


def game_choices(choice_1, choice_2):
    print(f"Compare A: {choice_1['name']}, {choice_1['description']} from {choice_1['country']}.")
    print(vs)
    print(f"Against B: {choice_2['name']}, {choice_2['description']} from {choice_2['country']}.")

    answer_chosen = False
    while not answer_chosen:
        answer_chosen = answer_entered(choice_1, choice_2)
    return answer_chosen


def answer_entered(choice_1, choice_2):
    answer = input("Who has more followers? Type 'A' or 'B': ")
    if answer == 'a' or answer == 'A':
        answer_chosen = choice_1
    elif answer == 'b' or answer == 'B':
        answer_chosen = choice_2
    else:
        print("Wrong! Type 'A' or 'B': ")
        answer_chosen = False
    return answer_chosen


def play_game():
    print(logo)
    level = 1
    lose = False
    while not lose:
        choice_1 = get_random_person()
        choice_2 = get_random_person()
        if choice_1 == choice_2:
            choice_2 = get_random_person()
        # print(choice_1['follower_count'])
        # print(choice_2['follower_count'])
        user_choice = game_choices(choice_1, choice_2)

        if choice_1['follower_count'] == user_choice['follower_count'] and \
                choice_1['follower_count'] > choice_2['follower_count']:
            print(f"You are write! Current score is {level}")
        elif choice_2['follower_count'] == user_choice['follower_count'] and \
                choice_2['follower_count'] > choice_1['follower_count']:
            print(f"You are write! Current score is {level}")
        else:
            lose = True
            print(f"Sorry that's wrong! Final score: {level-1}")
        level += 1


play_game()
