from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_input = screen.textinput(title="Make your bet", prompt="Which turtle will win the race (red/blue/green/yellow)")
if user_input:
    is_race_on = True


def setup_turtles():
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    turtles = []
    y_coordinate = -100
    for color in colors:
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(color)
        new_turtle.penup()
        new_turtle.goto(-235, y_coordinate)
        y_coordinate += 40

        turtles.append(new_turtle)
    return turtles


def race(some_turtles, racing):
    while racing:
        for a_turtle in some_turtles:
            if a_turtle.xcor() >= 225:
                racing = False
                if a_turtle.color()[0] == user_input:
                    print(f"Your turtle won! Your color was {user_input}")
                else:
                    print(f"Sorry, your turtle did not win. The {a_turtle.color()[0]} turtle did.")
                break
            a_turtle.forward(random.randint(0, 10))


our_turtles = setup_turtles()
race(our_turtles, is_race_on)
screen.exitonclick()
