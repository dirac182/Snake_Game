from turtle import *
from random import *
from food import Food
from scoreboard import *
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


game_on = True
game_start = True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    while game_start:
        scoreboard.scoreboard()
        game_start = False

    #Detect collision win food
    if snake.head.distance(food) < 20:
        scoreboard.incease_score()
        scoreboard.scoreboard()
        food.refresh()
        snake.extend()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() >300 or snake.head.ycor() < -300:
        scoreboard.reset()
        snake.reset()

    #detect collision with tail
    for snakes in snake.snakes[1:]:
        if snake.head.distance(snakes) < 10:
            scoreboard.reset()
            snake.reset()
    #if head collides with any segment in tail






screen.exitonclick()