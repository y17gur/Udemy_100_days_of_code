# Step 4
# https://replit.com/@appbrewery/Day-7-Hangman-4-Start#main.py

import random

stages = ["""
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
""", """
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
""", """
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
""", """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""", """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""", """
  +---+
  |   |
  O   |
      |
      |
      |
=========
""", """
  +---+
  |   |
      |
      |
      |
      |
=========
"""]

word_list = ["aardvark", "baboon", "camel"]
display = []
blank = '_'
random_word = random.choice(word_list)
random_word_list = []
end_of_game = False
# TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
# Set 'lives' to equal 6.
lives = 6

# TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.

# Testing code
print(f'Pssst, the solution is {random_word}.')

for i in random_word:
    random_word_list.append(i)
    display.append(blank)
print(f"{' '.join(display)}")


while not end_of_game:
    guess = (input('Please guess a letter: ')).lower()

    # TODO-2: - If guess is not a letter in the chosen_word,
    # Then reduce 'lives' by 1.
    if guess not in random_word:
        lives -= 1
    elif guess not in random_word_list and guess in random_word:
        lives -= 1

    for idx, letter in enumerate(random_word):
        if letter == guess:
            display[idx] = letter
            if letter in random_word_list:
                random_word_list.remove(letter)
    print(f"{' '.join(display)}")
    print(stages[lives])

    if blank not in display and lives > 0:
        end_of_game = True
        print('You won')
    elif lives == 0:
        end_of_game = True
        print('You lose')
