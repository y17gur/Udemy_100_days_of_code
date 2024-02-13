import random
from hangman_words import word_list
from hangman_art import stages, logo

display = []
blank = '_'
random_word = random.choice(word_list)
end_of_game = False
lives = 6

print(logo)
print(f'Pssst, the solution is {random_word}.')

for i in random_word:
    display.append(blank)
print(f"{' '.join(display)}")

while not end_of_game:
    guess = (input('Please guess a letter: ')).lower()
    print("\n" * 100)  # simulate a clear effect

    if guess not in random_word:
        print(f"A letter {guess} is not in the word. You lose a life.")
        lives -= 1
    elif guess in display:
        print(f"You have already guessed a letter: {guess}")

    for idx, letter in enumerate(random_word):
        if letter == guess:
            display[idx] = letter

    print(f"{' '.join(display)}")
    print(stages[lives])

    if blank not in display and lives > 0:
        end_of_game = True
        print('You win')
    elif lives == 0:
        end_of_game = True
        print('You lose')
