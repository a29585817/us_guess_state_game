import turtle
import pandas as pd


screen = turtle.Screen()
screen.title("U.S State Games")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pd.read_csv("50_states.csv")
state = data["state"].tolist()
game_over = True
guessed_states = []



while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)} / 50 states", prompt="What's another state's name.").title()

    if answer_state == "Exit":
        new_data = pd.DataFrame([x for x in state if x not in guessed_states])
        new_data.to_csv("states_to_learn")
        break

    if answer_state in state:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())
