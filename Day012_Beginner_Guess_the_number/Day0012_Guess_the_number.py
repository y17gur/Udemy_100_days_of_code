"""
Number Guessing Game Objectives:
# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
"""
from art import logo
import random


EASY = 10
HARD = 5


def check(answ, guess):
    if guess < answ:
        print("Too low.")
        guessed = False
    elif guess > answ:
        print("Too high.")
        guessed = False
    else:
        print(f"You got it! The answer was {answ}.")
        guessed = True
    return guessed


def choose_level():
    level_entered = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level_entered == 'easy':
        lvl_chosen = EASY
    elif level_entered == 'hard':
        lvl_chosen = HARD
    else:
        print("Wrong! Type 'easy' or 'hard': ")
        lvl_chosen = False
    return lvl_chosen


def user_answer():
    your_guess = 0
    while your_guess not in range(1, 101):
        your_guess = input("Make a guess: ")
        try:
            your_guess = int(your_guess)
        except ValueError:
            print('Entered value is not integer')
        if your_guess not in range(1, 101):
            print('Enter a number between 1 and 100.')

    return your_guess


def play_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1, 100)
    # print(answer)
    level_chosen = False
    guessed = False
    while not level_chosen:
        level_chosen = choose_level()
    if level_chosen == EASY:
        lives_amount = EASY
    else:
        lives_amount = HARD

    print(f'lives_amount - {lives_amount}')
    while lives_amount > 0 and guessed is False:

        your_guess = user_answer()

        guessed = check(answer, your_guess)
        lives_amount -= 1
        if lives_amount > 0 and guessed is False:
            print('Guess again')
            print(f"You have {lives_amount} attempts remaining to guess the number.")
        elif lives_amount == 0 and guessed is False:
            print("You've run out of guesses, you lose.")


print(logo)
play_game()
