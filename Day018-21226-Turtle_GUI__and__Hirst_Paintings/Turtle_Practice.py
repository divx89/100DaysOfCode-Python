import random
import turtle
from turtle import Turtle, Screen


def random_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


def make_square(some_turtle):
    """Move a turtle so that it creates a square of 100 units side length"""
    for i in range(4):
        some_turtle.forward(100)
        some_turtle.right(90)


def make_dashed_line(some_turtle):
    """Make a turtle create a dashed line"""
    some_turtle.penup()
    some_turtle.setposition(-300, 0)
    for i in range(50):
        some_turtle.pendown()
        some_turtle.forward(6)
        some_turtle.penup()
        some_turtle.forward(5)


def draw_different_shapes(some_turtle):
    colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue",
               "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
    some_turtle.penup()
    some_turtle.setposition(-50, 100)
    some_turtle.pendown()
    some_turtle.speed(5)
    for num_sides in range(3, 11):
        angle = 360 / num_sides
        some_turtle.pencolor(random_color())
        for side in range(num_sides):
            some_turtle.forward(100)
            some_turtle.right(angle)


def random_walk(some_turtle):
    some_turtle.shape("circle")
    some_turtle.pensize(10)
    directions = [0, 90, 180, 270]
    some_turtle.speed("fastest")
    for x in range(150):
        some_turtle.pencolor(random_color())
        some_turtle.forward(30)
        some_turtle.setheading(random.choice(directions))


def draw_spirograph(some_turtle):
    some_turtle.speed("fastest")

    heading = 0
    while heading <= 360:
        some_turtle.color(random_color())
        some_turtle.circle(100)
        heading += 5
        some_turtle.setheading(heading)


myTurtle = Turtle()
turtle.colormode(255)

# make_square(myTurtle)
# make_dashed_line(myTurtle)
# draw_different_shapes(myTurtle)
# random_walk(myTurtle)
draw_spirograph(myTurtle)

screen = Screen()
screen.exitonclick()
