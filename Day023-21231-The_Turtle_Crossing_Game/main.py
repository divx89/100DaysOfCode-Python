import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Setup the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Create the player and set a listener to control its movement
theTurtle = Player()
screen.listen()
screen.onkeypress(key="Up", fun=theTurtle.move_up)

# Create scoreboard and cars
score_board = Scoreboard()
traffic = CarManager()

game_is_on = True
while game_is_on:
    # Wait a while every iteration before updating the screen with new positions
    time.sleep(0.1)
    screen.update()

    # Create a new car if allowed
    traffic.add_car()

    # Make the traffic move
    traffic.move()

    # Remove the cars that have passed the left edge of the screen
    traffic.remove_exited_cars()

    # Reset player if level crossed
    if theTurtle.level_up():
        score_board.increase_level()
        traffic.increase_speed()
        theTurtle.reset_it()

    # Check if game over
    for car in traffic.cars:
        if car.distance(theTurtle) < 25:
            score_board.display_game_over()
            game_is_on = False

screen.exitonclick()
