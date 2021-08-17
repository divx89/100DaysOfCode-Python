from turtle import Turtle

MOVE_DISTANCE = 10
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
        """Create a snake, initially of 3 segments"""
        x_pos = START_X
        for part_number in range(0, 3):
            self.add_segment((x_pos, START_Y))
            x_pos -= MOVE_DISTANCE

    def add_segment(self, position):
        snake_segment = Turtle(shape="square")
        snake_segment.color("white")
        snake_segment.penup()
        snake_segment.setposition(position[0], position[1])
        snake_segment.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.snake.append(snake_segment)

    def move(self):
        """Move a snake so that it follows its head"""
        # Move the nth segment to the (n-1)th segment's place.
        # The 0th segment moves forward
        # This effectively moves the snake, with each segment moving to the previous segment's
        # position, and the first segment moving forward
        for segment_num in range((len(self.snake) - 1), -1, -1):
            if segment_num != 0:
                self.snake[segment_num].goto(self.snake[segment_num - 1].pos())
            else:
                self.head.forward(MOVE_DISTANCE)

    def extend(self):
        """Extend the snake by a segment, at a certain position"""
        self.add_segment(position=self.snake[-1].position())

    def collided_with_tail(self):
        """Find out if a snake's head collided with any of its other segments"""
        did_it_collide = False
        for segment in self.snake[1:]:
            if self.head.position() != segment.position():
                continue
            did_it_collide = True
            break
        return did_it_collide

    def up(self):
        """Turn the snake's head up if feasible"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Turn the snake's head down if feasible"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Turn the snake's head left if feasible"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Turn the snake's head right if feasible"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
