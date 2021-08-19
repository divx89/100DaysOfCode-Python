from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 0
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(-215, 260)
        self.increase_level()

    def increase_level(self):
        self.level += 1
        self.clear()
        self.write(arg=f"Level: {self.level}", align="center", font=FONT)

    def display_game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align="center", font=FONT)
