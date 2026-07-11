import time
from turtle import Screen, Turtle

from scoreboard import Scoreboard
from snake import Snake
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
game_is_on = True

# Wall
wall_painter = Turtle()
wall_painter.pencolor("gray")
wall_painter.penup()
wall_painter.goto(-280,-280)
wall_painter.pendown()
for _ in range(4):
    wall_painter.forward(560)
    wall_painter.left(90)
wall_painter.hideturtle()

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


screen.update()

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Eat Food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.score += 1
        scoreboard.update()
    # Detect off Screen
    if snake.head.xcor() > 270 or snake.head.xcor() < -270 or snake.head.ycor() < -270 or snake.head.ycor() > 270:
        game_is_on = False
        scoreboard.game_over()
    # Detect Tail Collision
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
