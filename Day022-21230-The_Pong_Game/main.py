"""The Pong Game"""
import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from net import Net

WIDTH = 800
HEIGHT = 600
MARGIN = 50


def create_screen():
    """
    Create a screen for playing Pong.
    The screen will be black, and of a width > height
    """
    screen = Screen()
    screen.setup(width=WIDTH, height=HEIGHT)
    screen.bgcolor("black")
    screen.title("Pong")
    screen.tracer(0)

    Net()

    return screen


def setup_listeners(screen, paddle, l_r):
    """Setup the listeners to handle the movement of paddles on the screen"""
    screen.listen()
    screen.onkeypress(key=("Up" if l_r == "r" else "w"), fun=paddle.up)
    screen.onkeypress(key=("Down" if l_r == "r" else "s"), fun=paddle.down)


def touched(general, specific):
    """Find out if the ball has touched a paddle, either side or the ceiling or floor"""
    return_value = False

    if general == 'paddle':
        if theBall.distance(left_paddle) <= 50 and theBall.xcor() < -325:
            specific.append('left')
            return_value = True
        elif theBall.distance(right_paddle) <= 50 and theBall.xcor() > 325:
            specific.append('right')
            return_value = True
    elif general == 'side':
        if theBall.xcor() <= -380:
            specific.append('left')
            return_value = True
        elif theBall.xcor() >= 380:
            specific.append('right')
            return_value = True
    elif general == 'walls':
        return_value = theBall.ycor() > (HEIGHT / 2 - 10) or theBall.ycor() < -(HEIGHT / 2 - 10)

    return return_value


theTable = create_screen()

right_paddle = Paddle(position=(WIDTH / 2 - MARGIN, 0), max_y=HEIGHT / 2)
left_paddle = Paddle(position=(-(WIDTH / 2 - MARGIN), 0), max_y=HEIGHT / 2)
theBall = Ball()
theScore = Scoreboard((WIDTH, HEIGHT))

setup_listeners(theTable, right_paddle, "r")
setup_listeners(theTable, left_paddle, "l")

game_on = True
# The sleep time decides how fast we update the screen
# or how fast the bal moves. So, lower the sleep_time,
# faster the ball.
sleep_time = 0.1

while game_on:
    theTable.update()
    time.sleep(sleep_time)

    theBall.move()
    paddle_touched = []
    side_touched = []

    if touched(general='paddle', specific=paddle_touched):
        theScore.score(paddle_touched[0])
        theBall.bounce_off(item="paddles")
        sleep_time *= 0.98

    if touched(general="walls", specific=[]):
        theBall.bounce_off(item="walls")

    if touched(general="side", specific=side_touched):
        theScore.score(side_touched[0])
        sleep_time = 0.1
        theBall.reset_position()

theTable.exitonclick()
