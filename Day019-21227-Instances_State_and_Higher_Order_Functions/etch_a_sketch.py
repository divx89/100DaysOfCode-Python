from turtle import Turtle, Screen

myTurtle = Turtle()
screen = Screen()


def move_forward():
    myTurtle.forward(10)


def move_backward():
    myTurtle.backward(10)


def counter_clockwise():
    myTurtle.left(5)


def clockwise():
    myTurtle.right(5)


def reset_turtle():
    myTurtle.reset()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=reset_turtle)
screen.exitonclick()
