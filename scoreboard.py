from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 280)
        self.pencolor("white")
        self.update()

    def update(self):
        self.clear()
        self.pendown()
        self.write(f"Score: {self.score}", align="center", font=("Courier", 10, "normal"))
        self.penup()

    def game_over(self):
        self.goto(0, 0)
        self.pendown()
        self.write("GAME OVER", align="center", font=("Courier", 20, "normal"))
        self.penup()
