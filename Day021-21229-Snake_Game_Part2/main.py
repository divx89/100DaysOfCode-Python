from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

MARGIN = 10


# Setup the screen (600x400, Black color)
def setup_screen():
    """Setup the screen used for display purposes"""
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("My Snake Game")
    screen.tracer(0)
    return screen


def setup_listeners(some_screen, some_snake):
    """Setup the listeners for the snake"""
    some_screen.listen()
    some_screen.onkey(key="Up", fun=some_snake.up)
    some_screen.onkey(key="Down", fun=some_snake.down)
    some_screen.onkey(key="Left", fun=some_snake.left)
    some_screen.onkey(key="Right", fun=some_snake.right)


# Declare the snake and screen
theScreen = setup_screen()
canvas_size = (theScreen.window_width(), theScreen.window_height())
max_x = canvas_size[0] / 2 - MARGIN
max_y = canvas_size[1] / 2 - MARGIN

theSnake = Snake()
theFood = Food(canvas_size)
theScoreBoard = Scoreboard(canvas_size)
setup_listeners(theScreen, theSnake)

game_on = True

# Run the game
while game_on:
    # Update the screen in every iteration
    theScreen.update()
    # Wait a bit
    time.sleep(0.1)
    # Move the snake
    theSnake.move()
    # Check if snake head and food are touching
    if theSnake.head.distance(theFood) < 15:
        theFood.move()
        theSnake.extend()
        theScoreBoard.update_score()

    snake_x = theSnake.head.xcor()
    snake_y = theSnake.head.ycor()

    if snake_x > max_x or snake_x < -max_x or snake_y > max_y or snake_y < -max_y or theSnake.collided_with_tail():
        game_on = False
        theScoreBoard.game_over()

theScreen.exitonclick()
