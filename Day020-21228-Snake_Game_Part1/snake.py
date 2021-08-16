from turtle import Turtle
MOVE_DISTANCE = 20
START_X = 0
START_Y = 0
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake(object):

    def __init__(self):
        self.snake = []
        self.make_snake()
        self.head = self.snake[0]

    def make_snake(self):
        x_pos = START_X
        for part_number in range(0, 3):
            snake_segment = Turtle(shape="square")
            snake_segment.color("white")
            snake_segment.penup()
            snake_segment.setposition(x_pos, START_Y)
            x_pos -= MOVE_DISTANCE
            self.snake.append(snake_segment)

    def move(self):
        # Move the nth segment to the (n-1)th segment's place.
        # The 0th segment moves forward
        # This effectively moves the snake, with each segment moving to the previous segment's
        # position, and the first segment moving forward
        for segment_num in range((len(self.snake) - 1), -1, -1):
            if segment_num != 0:
                self.snake[segment_num].goto(self.snake[segment_num - 1].pos())
            else:
                self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
