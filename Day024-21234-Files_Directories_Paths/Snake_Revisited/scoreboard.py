from turtle import Turtle

ALIGNMENT = "center"
FONT = ("courier", 20, "normal")
MARGIN = 28


class Scoreboard(Turtle):

    def __init__(self, canvas_size):
        super().__init__()
        self.canvas_size = canvas_size
        self.score = 0
        self.high_score = self.read_write_high_score('r')
        self.high_score = int(self.high_score) if self.high_score != '' else 0
        self.penup()
        self.color("white")
        self.goto(0, ((canvas_size[1] / 2) - MARGIN))
        self.update_scoreboard()
        self.hideturtle()

    def read_write_high_score(self, read_write='r'):
        with open(file="data.txt", mode=read_write) as data:
            if read_write == 'r':
                high_score = data.read()
                return high_score
            else:
                data.write(str(self.high_score))
                return None

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        self.high_score = self.score if self.score > self.high_score else self.high_score
        self.read_write_high_score('w')
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg=f"GAME OVER", move=False, align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.update_scoreboard()
