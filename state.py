from turtle import Turtle
import pandas as pd


data = pd.read_csv("50_states.csv")
state_x = data["x"]
state_y = data["y"]
state_name = data["state"]
state_dic = {}
for state in range(len(state_name)):
    state_dic[state_name[state]] = [state_x[state], state_y[state]]

class Correct(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def write_state(self, state):
        self.color("black")
        self.goto(state_dic[state][0], state_dic[state][1])
        self.write(arg=state, move=False, align="center"
                   , font=("Courier", 15, "normal"))




