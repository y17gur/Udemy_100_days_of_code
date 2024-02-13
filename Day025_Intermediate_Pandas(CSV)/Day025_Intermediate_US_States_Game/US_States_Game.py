import turtle
import pandas
from write_states import States

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
score = States()


data = pandas.read_csv("50_states.csv")
answers = []
missing_states = []
total_states = 50
game_on = True

# while game_on:
#     answer_state = screen.textinput(title=f"Guess the State ({len(answers)}/{total_states})",
#                                     prompt="What's the state's name?").title()
#
#     if answer_state == 'Exit':
#         break
#     if answer_state in data['state'].tolist():
#         entered_state_data = data[data['state'] == answer_state]
#         x_value = entered_state_data['x'].values[0]
#         y_value = entered_state_data['y'].values[0]
#         score.update_text(x_value, y_value, answer_state)
#         answers.append(answer_state)
#     if len(answers) == total_states:
#         game_on = False

while game_on:
    answer_state = screen.textinput(
        title=f"Guess the State ({len(answers)}/{total_states})",
        prompt="What's the state's name?"
    ).title()

    if answer_state == 'Exit':
        break

    if answer_state in data['state'].tolist():
        x_value, y_value = data[data['state'] == answer_state][['x', 'y']].values[0]
        score.update_text(x_value, y_value, answer_state)
        answers.append(answer_state)

    game_on = len(answers) != total_states


missing_states = list(set(data['state'].tolist()) - set(answers))
new_data = pandas.DataFrame(sorted(missing_states))
new_data.to_csv("states_to_learn.scv")


# def get_mouse_click_coordinates(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coordinates)
# turtle.mainloop()

