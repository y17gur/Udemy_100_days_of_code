# Step 2
# https://replit.com/@appbrewery/Day-7-Hangman-2-Start

import random

word_list = ["aardvark", "baboon", "camel"]
display = []

random_word = random.choice(word_list)

# Testing code
print(f'Pssst, the solution is {random_word}.')

# TODO-1: - Create an empty List called display.
# For each letter in the chosen_word, add a "_" to 'display'.
# So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
for i in random_word:
    display.append('_')

print(display)

guess = (input('Please guess a letter: ')).lower()

# TODO-2: - Loop through each position in the chosen_word;
# If the letter at that position matches 'guess' then reveal that letter in the display at that position.
# e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
for idx, i in enumerate(random_word):
    if i == guess:
        display[idx] = i

# TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
# Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.

print(display)
