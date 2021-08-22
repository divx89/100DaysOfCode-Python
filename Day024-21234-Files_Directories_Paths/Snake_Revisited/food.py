from turtle import Turtle
import random

MARGIN = 20


class Food(Turtle):

    def __init__(self, canvas_size):
        """
        Initialize a Food object.
        PARAMETER:
          canvas_size (tuple of 2 integers): Width and Height of the canvas
        """
        super().__init__()
        self.shape("circle")
        self.penup()
        # Make the food particle half the normal size
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        # Remove the animation on movement of the food particle
        self.speed("fastest")
        self.canvas_size = canvas_size
        self.move()

    def move(self):
        # Place the particle at a random location on the canvas
        max_x = int(self.canvas_size[0] / 2) - MARGIN
        max_y = int(self.canvas_size[1] / 2) - MARGIN
        self.goto(random.randint(-max_x, max_x), random.randint(-max_y, max_y))
