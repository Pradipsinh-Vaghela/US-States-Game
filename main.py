import turtle
import time
from states_info import StatesInfo

screen = turtle.Screen()
screen.setup(height=500, width=700)
screen.title("U.S. States Game ")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
answered_states_list = []
states_info = StatesInfo()

game_is_on = True
while len(answered_states_list) < 50 :
    screen.update()
    answer_state = screen.textinput(title=f"{len(answered_states_list)}/50 States Correct",
                                    prompt="What's another state name?").title()

    # Check if the state previously answered
    if answer_state in answered_states_list:
        pass
    # Check is the answer state is correct or not
    elif states_info.check_state_name(answer_state):
        states_info.location(answer_state)
        answered_states_list.append(answer_state)
        time.sleep(0.5)
    elif answer_state == "Exit":
        break

# Generate State_to_learn.csv
states_info.missing_states_name(answered_states_list)
