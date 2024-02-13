# Step 1
# https://replit.com/@appbrewery/Day-7-Hangman-1-Start#main.py

import random

word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
random_word = random.choice(word_list)

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = (input('Please guess a letter: ')).lower()

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for i in random_word:
    if i == guess:
        print(True)
    else:
        print(False)


