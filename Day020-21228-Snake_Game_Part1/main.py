from turtle import Screen
from snake import Snake
import time


# Setup the screen (600x400, Black color)
def setup_screen():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("My Snake Game")
    screen.tracer(0)
    return screen


def setup_listeners(some_screen, some_snake):
    some_screen.listen()
    some_screen.onkey(key="Up", fun=some_snake.up)
    some_screen.onkey(key="Down", fun=some_snake.down)
    some_screen.onkey(key="Left", fun=some_snake.left)
    some_screen.onkey(key="Right", fun=some_snake.right)


# Declare the snake and screen
theSnake = Snake()
theScreen = setup_screen()
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

theScreen.exitonclick()
