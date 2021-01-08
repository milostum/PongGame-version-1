from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.goto(0, 0)
        self.angles = [15, 30, 45, 60, 120, 135, 150, 180, 225, 250]
        self.setheading(random.choice(self.angles))
        self.refresh()

    def move(self):
        self.forward(10)
        if self.ycor() > 400 or self.ycor() < -400:
            self.setheading(-self.heading())

    def refresh(self):
        self.goto(0, 0)
        self.setheading(random.choice(self.angles))
