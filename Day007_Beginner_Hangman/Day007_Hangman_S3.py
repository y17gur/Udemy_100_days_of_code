# Step 3
# https://replit.com/@appbrewery/Day-7-Hangman-3-Start#main.py

import random

word_list = ["aardvark", "baboon", "camel"]
display = []
blank = '_'
random_word = random.choice(word_list)
end_of_game = False

# Testing code
print(f'Pssst, the solution is {random_word}.')

for i in random_word:
    display.append(blank)
print(display)

# TODO-1: - Use a while loop to let the user guess again.
# The loop should only stop once the user has guessed all the letters in the chosen_word
# and 'display' has no more blanks ("_"). Then you can tell the user they've won.

while not end_of_game:
    guess = (input('Please guess a letter: ')).lower()

    for idx, i in enumerate(random_word):
        if i == guess:
            display[idx] = i
    print(display)

    if blank not in display:
        end_of_game = True
        print('You won')
