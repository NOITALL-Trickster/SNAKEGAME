from turtle import Turtle

SPEED = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.no_of_tails = 3
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for _ in range(0, self.no_of_tails):
            self.add_segment((-_*12, 0))

    def add_segment(self, pos_value):
        position = pos_value
        tim = Turtle()
        tim.penup()
        tim.goto(position)
        tim.shape("square")
        tim.shapesize(0.7)
        tim.color("white")
        self.segments.append(tim)

    def extend(self):
        self.add_segment(self.segments[-1].position())
        self.no_of_tails += 1

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            x_cor = self.segments[seg_num - 1].xcor()
            y_cor = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x_cor, y_cor)
        self.head.forward(SPEED)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

