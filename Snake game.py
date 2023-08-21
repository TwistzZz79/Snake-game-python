from turtle import Screen,Turtle
from Snake import Snake
import time
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600,height = 600)

screen.bgcolor("black")

screen.tracer(0)
screen.title("My Snake Game")


snake = Snake()
food = Food()
scoreboard=ScoreBoard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")

screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    #eat function
    if snake.head.distance(food)<30:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    
    #check to see if snake hit the wall
    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()>290 or snake.head.ycor()<-290:
        game_is_on=False
        scoreboard.game_over()
        
    #check to see if snake hit it self
    for segment in snake.segments[1:]:
        
        if snake.head.distance(segment)<10:
            game_is_on=False
            scoreboard.game_over()
        
    
    
screen.exitonclick()