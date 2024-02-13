# Step 5
# https://replit.com/@appbrewery/Day-7-Hangman-5-Start#main.py

# TODO-2: - Import the stages from hangman_art.py and make this error go away.
import random
from hangman_words import word_list
from hangman_art import stages, logo

# TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
display = []
blank = '_'
random_word = random.choice(word_list)
random_word_list = []
end_of_game = False
lives = 6

# TODO-3: - Import the logo from hangman_art.py and print it at the start of the US_States_Game.
print(logo)
print(f'Pssst, the solution is {random_word}.')

for i in random_word:
    random_word_list.append(i)
    display.append(blank)
print(f"{' '.join(display)}")

while not end_of_game:
    guess = (input('Please guess a letter: ')).lower()

    # TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
    if guess not in random_word:
        print(f"A letter {guess} is not in the word. You lose a life.")
        lives -= 1
        # TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    elif guess not in random_word_list and guess in random_word:
        print(f"You have already guessed a letter: {guess}")

    for idx, letter in enumerate(random_word):
        if letter == guess:
            display[idx] = letter
            if letter in random_word_list:
                random_word_list.remove(letter)
    print(f"{' '.join(display)}")
    print(stages[lives])

    if blank not in display and lives > 0:
        end_of_game = True
        print('You win')
    elif lives == 0:
        end_of_game = True
        print('You lose')
