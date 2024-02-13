# https://replit.com/@appbrewery/password-generator-start#README.md

"""Instructions
The program will ask:

How many letters would you like in your password?
How many symbols would you like?
How many numbers would you like?

The objective is to take the inputs from the user to these questions and then generate a random password.
Use your knowledge about Python lists and loops to complete the challenge.

Easy Version (Step 1)
Generate the password in sequence. If the user wants
4 letters
2 symbols and
3 numbers
then the password might look like this:
fgdx$*924
You can see that all the letters are together.
All the symbols are together and all the numbers follow each other as well. Try to solve this problem first.

Hard Version (Step 2)
When you've completed the easy version, you're ready to tackle the hard version.
In the advanced version of this project the final password does not follow a pattern.
So the example above might look like this:
x$d24g*f9
And every time you generate a password, the positions of the symbols, numbers, and letters are different.

Solution
https://replit.com/@appbrewery/password-generator-end"""

# Password Generator Project
import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

chosen_all = []
p_word = ''

for letter in range(nr_letters):
    letters_rand = random.choice(letters)
    chosen_all.append(letters_rand)

for symbol in range(nr_symbols):
    symbols_rand = random.choice(symbols)
    chosen_all.append(symbols_rand)

for number in range(nr_numbers):
    numbers_rand = random.choice(numbers)
    chosen_all.append(str(numbers_rand))

random.shuffle(chosen_all)

for i in chosen_all:
    p_word += i

print(f'Your PassWord is: {p_word}')
