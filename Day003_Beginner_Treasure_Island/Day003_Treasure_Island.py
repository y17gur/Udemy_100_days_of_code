# https://replit.com/@appbrewery/treasure-island-start?v=1#README.md

""" Instructions
Make your own "Choose Your Own Adventure" US_States_Game. Use conditionals such as if, else, and elif statements to lay out the
logic and the story's path in your program.
To write your code according to my story, you can use this flow chart from draw.io to help you.

However, I think the fun part is writing your own story 😊

Solution
https://replit.com/@appbrewery/treasure-island-end#main.py """

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

# Write your code below this line 👇
left_right = input('left or right? ').lower()
if left_right == 'right':
    print('Fall into a hole. Game Over.')
elif left_right == 'left':
    swim_wait = input('swim or wait? ').lower()
    if swim_wait == 'swim':
        print('Attacked by trout. Game Over.')
    elif swim_wait == 'wait':
        door = input('Which door? Red/Blue/Yellow ').lower()
        if door == 'red':
            print('Burned by fire. Game Over.')
        elif door == 'blue':
            print('Eaten by beasts. Game Over.')
        elif door == 'yellow':
            print('You Win!')
        else:
            print('Game Over.')
    else:
        print('Game Over.')
else:
    print('Game Over.')
