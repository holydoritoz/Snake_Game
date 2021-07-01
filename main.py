from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time



screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title('My snake game')
screen.tracer(0)


snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    #Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    #Detect collision with wall.
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        game_is_on = False
        score.game_over()

    for any_segment in snake.snake_body[1:]:
        if snake.head.distance(any_segment) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()


