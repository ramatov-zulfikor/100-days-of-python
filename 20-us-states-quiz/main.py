import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

all_states = data["state"].to_list()
guessed_states = []
missing_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 Guess the State",
                                    prompt="What's another state's name").lower().title()

    if answer_state == "Exit":
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        states_to_learn = pandas.DataFrame(missing_states).to_csv("states_to_learn.csv")
        break
    if answer_state in data["state"].to_list():
        guessed_states.append(answer_state)
        guessed_state = data[data.state == answer_state]
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        new_x = int(guessed_state.x)
        new_y = int(guessed_state.y)
        t.goto(new_x, new_y)
        t.write(answer_state, align="center", font=("Courier", 14, "normal"))
