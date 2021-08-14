"""
Simple program to create an example of a Hirst style painting
The first few lines are commented, because they're only used once to
figure out which colors are used in an actual Hirst painting.
After that, we don't need them again.
They can be uncommented and the rgb_colors variable renamed to colors,
and the program will work just fine.
"""

# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     rgb_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))
#
# print(rgb_colors)
import random
import turtle
from turtle import Turtle, Screen

colors = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123),
          (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35),
          (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77),
          (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64),
          (107, 127, 153), (176, 192, 208), (168, 99, 102)]

myTurtle = Turtle()
turtle.colormode(255)
print(myTurtle.pos())

start_x = -250
start_y = -250

x = 0
while x < 10:
    myTurtle.penup()
    myTurtle.goto(start_x, start_y)
    myTurtle.pendown()

    y = 0
    while y < 10:
        myTurtle.dot(20, random.choice(colors))
        myTurtle.penup()
        myTurtle.forward(50)
        myTurtle.pendown()
        y += 1
    x += 1
    start_y += 50


screen = Screen()
screen.exitonclick()