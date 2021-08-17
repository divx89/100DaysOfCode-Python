from turtle import Turtle

ALIGNMENT = "center"
FONT = ("courier", 20, "normal")
MARGIN = 28


class Scoreboard(Turtle):

    def __init__(self, canvas_size):
        super().__init__()
        self.canvas_size = canvas_size
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0, ((canvas_size[1] / 2) - MARGIN))
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER", move=False, align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.update_scoreboard()
