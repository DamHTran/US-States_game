import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

pen = turtle.Turtle()
pen.penup()
pen.hideturtle()


screen.tracer(0)

# Import data
data = pandas.read_csv("50_states.csv")
# check match answer and write state
guessed_states = []
while len(guessed_states) < 50:
    screen.update()
    answer = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?")
    answer = answer.title()
    if answer in data["state"].unique():
        index = data[data["state"] == answer].index
        print(index)
        pen.goto(int(data["x"][index]), int(data["y"][index]))
        pen.write(answer)
        guessed_states.append(answer)
    elif answer == "Exit":
        # states_to_learn.csv
        states_to_learn = []
        for state in data["state"]:
            if state not in guessed_states:
                states_to_learn.append(state)
        df = pandas.DataFrame(states_to_learn)
        df.to_csv("States_to_learn.csv")
        break
    else:
        print("This is not a state")



