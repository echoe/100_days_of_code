import turtle
import pandas
"""State guessing game!"""
IMAGE="blank_states_img.gif"
CSV="50_states.csv"
OUTPUT_FILE = "states_to_learn.csv"

screen = turtle.Screen()
screen.title("U.S. States Game")

screen.addshape(IMAGE)
turtle.shape(IMAGE)

data = pandas.read_csv(CSV)
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        states_to_learn = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(states_to_learn)
        new_data.to_csv(OUTPUT_FILE)
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.ht()
        t.pu()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state) # You can also do: state_data.state.item()