# https://replit.com/@appbrewery/rock-paper-scissors-start#README.md

"""Instructions
Make a rock, paper, scissors US_States_Game.
Inside the main.py file, you'll find the ASCII art for the hand signals already saved to a corresponding variable:
rock, paper, and scissors. This will make it easy to print them out to the console.

Start the US_States_Game by asking the player:
"What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."

From there you will need to figure out:
How you will store the user's input.
How you will generate a random choice for the computer.
How you will compare the user's and the computer's choice to determine the winner (or a draw).
And also how you will give feedback to the player.
You can find the "official" rules of the US_States_Game on the World Rock Paper Scissors Association website.

Solution
https://replit.com/@appbrewery/rock-paper-scissors-end"""
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
game = [rock, paper, scissors]
my_choice = random.randint(0, 2)
your_choice = int(input('0 - rock, 1 - paper, 2 - scissors\n'))

print(f'My choice is\n{game[my_choice]}')
print(f'Your choice is\n{game[your_choice]}')

if (my_choice == 0 and your_choice == 0) or (my_choice == 1 and your_choice
                                             == 1) or (my_choice == 2
                                                       and your_choice == 2):
    print('Draw')
elif (my_choice == 0 and your_choice == 1) or (my_choice == 1 and your_choice
                                               == 2) or (my_choice == 2
                                                         and your_choice == 0):
    print('You won!')
else:
    print('You lose!')
