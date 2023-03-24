import turtle
import pandas
from clock import Clock

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
while True:
    screen.update()
    answer = screen.textinput(title="Guess the State", prompt="What's another state's name?")
    answer = answer.title()
    clock = Clock()
    clock.countdown()
    if answer in data["state"].unique():
        index = data[data["state"] == answer].index
        print(index)
        pen.goto(int(data["x"][index]), int(data["y"][index]))
        pen.write(answer)
    else:
        print("no")
        break



screen.exitonclick()