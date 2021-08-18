from turtle import Turtle

SPEED = 20
MARGIN = 10
INIT_HEADING = 36
INIT_SPEED = 6


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        # self.speed(INIT_SPEED)
        self.setheading(INIT_HEADING)

    def move(self):
        self.forward(SPEED)

    def bounce_off(self, item="paddles"):
        self.setheading((180 if item in ["paddles", "sides"] else 360) - self.heading())

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_off(item="sides")
