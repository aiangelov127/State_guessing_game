from turtle import Turtle, Screen
import pandas

data = pandas.read_csv("50_states.csv")


state_name = Turtle()
screen = Screen()
states_map = Turtle()

screen.title("US States Game")
screen.setup()
image = "blank_states_img.gif"
screen.addshape(image)
states_map.shape(image)

states_list = []
all_states = data.state.to_list()

while len(states_list) < 50:

    answer_state = screen.textinput(title=f"{len(states_list)} / 50 correct", prompt="Guess a state: ").title()

    if answer_state == "Exit":
        not_guessed_list = [state for state in data.state if state not in states_list]
        not_guessed = {
            "states": not_guessed_list
        }
        not_guessed_file = pandas.DataFrame(not_guessed)
        not_guessed_file.to_csv("not_guessed.csv")
        break


    if answer_state in all_states:
        correct_state = data[data.state == answer_state]
        states_list.append(answer_state)
        new_x = int(correct_state.x)
        new_y = int(correct_state.y)
        state_name.hideturtle()
        state_name.penup()
        state_name.goto(new_x, new_y)
        state_name.write(answer_state)
    print(f"{len(states_list)} / 50")


screen.mainloop()