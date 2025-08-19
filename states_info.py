import pandas
from turtle import Turtle

class StatesInfo(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.speed(5)
        self.x_cor = 0
        self.y_cor = 0
        self.data = pandas.read_csv("50_states.csv")
        self.missing_states_list = []

    def check_state_name(self, answer_state):
        """Return TRUE if the answer_state name is match with any state in data.
        Take input as answer_state(str)"""
        for state in self.data["state"]:
            if answer_state == state:
                return True

    def location(self,answer_state):
        """Place the name of the answered_state to the map.
        Take input as answer_state(str)"""
        self.x_cor = self.data.x[self.data.state == answer_state]
        self.y_cor = self.data.y[self.data.state == answer_state]
        self.goto(int(self.x_cor.item()), int(self.y_cor.item()))
        self.write(arg=f"{answer_state}", align="center")

    def missing_states_name(self, answered_states):
        """Return .csv file of not answered states names.
        Take input as answered states(list)"""
        for state in self.data.state:
            if state not in answered_states:
                self.missing_states_list.append(state)

        missing_states_data = pandas.DataFrame(self.missing_states_list)
        missing_states_data.to_csv("States_to_learn.csv")
