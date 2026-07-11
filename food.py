from turtle import Turtle
from random import randint
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.shapesize(0.5)
        self.speed("fastest")
        self.penup()
        self.refresh()

    def refresh(self):
        random_x = randint(-265, 265)
        random_y = randint(-265, 265)
        self.goto(random_x, random_y)

