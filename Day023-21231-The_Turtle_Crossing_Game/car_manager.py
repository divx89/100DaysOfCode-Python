from turtle import Turtle
import random

INIT_SPEED = 5
SPEED_INCREMENT = 10
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class CarManager:

    def __init__(self):
        self.cars = []
        self.speed = INIT_SPEED

    def add_car(self):
        if random.randint(1, 6) == 3:
            new_car = Turtle()
            new_car.penup()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.goto(320, random.randint(-250, 250))
            self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.backward(self.speed)

    def increase_speed(self):
        self.speed += SPEED_INCREMENT

    def remove_exited_cars(self):
        self.cars = [car for car in self.cars if car.xcor() > -320]
