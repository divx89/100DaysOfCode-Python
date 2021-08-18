from turtle import Turtle

WIDTH_STRETCH = 5
HEADING = {"UP": 20, "DOWN": -20}


class Paddle(Turtle):

    def __init__(self, position, max_y):
        super().__init__()
        self.max_y = max_y
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=WIDTH_STRETCH, stretch_len=1)
        self.goto(position)
        self.speed(7)
        self.length = 10 * WIDTH_STRETCH

    def move(self, heading):
        self.goto(self.xcor(), self.ycor() + heading)

    def up(self):
        if self.ycor() < self.max_y - self.length:
            self.move(HEADING["UP"])

    def down(self):
        if self.ycor() > -self.max_y + self.length:
            self.move(HEADING["DOWN"])
