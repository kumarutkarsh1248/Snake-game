from turtle import Screen
from time import sleep
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("turtle snake game")
screen.tracer(0)

food = Food()

scoreboard = Scoreboard()

initial_snake_grid = 20
snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    sleep(0.2)
    snake.move()

    # detect collision with the food
    if snake.head.distance(food) < 30:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.game_reset()
        snake.snake_reset()

    # detection collision with its own body
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.game_reset()
            snake.snake_reset()



screen.exitonclick()

