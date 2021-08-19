from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.reset_it()

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def level_up(self):
        return self.ycor() >= FINISH_LINE_Y

    def reset_it(self):
        self.hideturtle()
        self.penup()
        self.color("black")
        self.setheading(90)
        self.goto(STARTING_POSITION)
        self.showturtle()
