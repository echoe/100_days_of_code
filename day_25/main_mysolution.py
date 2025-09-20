import turtle
import pandas
"""State guessing game! I added comments to explain what was happening after the fact."""
IMAGE="blank_states_img.gif"
CSV="50_states.csv"

# Create the turtle screen.
screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape(IMAGE)
turtle.shape(IMAGE)

#Create a dataframe from the 50 States CSV.
df = pandas.DataFrame(pandas.read_csv(CSV))

#Create a score, and then loop so you can guess multiple times.
score = 0
while score < 50:
    guess = turtle.textinput(f"{score}/50 States Correct", "What's another state name?").title()
    # print(guess.title())
    # print(df["state"])
    # print(df.loc[df["state"] == guess.title()])
    # Pull the row that corresponds to the typed state, converting the guess to title case.
    df_check = df.loc[df["state"] == guess]
    # If this is not an empty row, add the turtle.
    if not df_check.empty:
        score += 1
        statename_turtle = turtle.Turtle()
        statename_turtle.speed(0)
        statename_turtle.pu()
        statename_turtle.ht()
        state_pos = df_check.values.tolist() # We need these values to be a list so we can pull the x and y values cleanly.
        statename_turtle.goto(state_pos[0][1:3])
        statename_turtle.write(guess)
        df = df[df["state"] != guess] # Drop the state from the working dataframe so we can't guess it twice.
print("You win!")
screen.exitonclick()