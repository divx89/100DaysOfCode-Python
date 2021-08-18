from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self, canvas_size):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.canvas_size = canvas_size
        self.write_score()

    def write_score(self):
        self.clear()
        self.goto(-(self.canvas_size[0] / 8), self.canvas_size[1] / 2 - 60)
        self.write(arg=self.l_score, align="center", font=("Courier", 40, "bold"))
        self.goto(self.canvas_size[0] / 8, self.canvas_size[1] / 2 - 60)
        self.write(arg=self.r_score, align="center", font=("Courier", 40, "bold"))

    def score(self, left_right):
        if left_right == 'left':
            self.l_score += 1
        else:
            self.r_score += 1
        self.write_score()
