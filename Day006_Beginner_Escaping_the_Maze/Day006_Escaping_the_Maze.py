"""
https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

def turn_around():
    turn_left()
    turn_left()
    
    
def turn_right():
    turn_left()
    turn_left()
    turn_left()
   
   
def jump_over():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
   
# 1
for i in range(6):
    jump_over()
# 2
while not at_goal():
    jump_over()

# 3
front_is_clear(), wall_in_front(), at_goal()

def jump_infront_wall():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if front_is_clear():
        move()
    else:
        jump_infront_wall()

# 4
# front_is_clear(), right_is_clear(), wall_in_front(), wall_on_right(), at_goal()

while not at_goal():
    if front_is_clear() and wall_on_right():
        move()
    elif right_is_clear():
        turn_right()
        move()
    else:
        while not front_is_clear():
            turn_left()

# 5

#front_is_clear() right_is_clear() wall_in_front() wall_on_right() move() turn_left()
while front_is_clear():
    move()
turn_left()

while not at_goal():
    if front_is_clear() and wall_on_right():
        move()
    elif wall_in_front() and not wall_on_right():
        turn_right()
        move()
    elif right_is_clear():
        turn_right()
        move()
    elif not front_is_clear():
        turn_left()
    else:
        move()


# teacher
while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
"""
