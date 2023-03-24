import time
from turtle import Turtle


class Clock(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0, 280)

    def countdown(self):
        minutes = 10
        secs = 0
        while True:
            self.write(str(minutes).zfill(2) + ":" + str(secs).zfill(2), font=("arial", 20, "normal"))
            time.sleep(1)
            minutes -= 1
            if minutes == 0:
                break
