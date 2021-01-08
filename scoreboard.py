from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 40, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score1 = 0
        self.score2 = 0
        self.color("white")
        self.penup()
        self.goto(0, 340)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"{self.score1} : {self.score2}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER!", align=ALIGNMENT, font=FONT)

    def increase_score_1(self):
        self.score1 += 1
        self.clear()
        self.update_scoreboard()

    def increase_score_2(self):
        self.score2 += 1
        self.clear()
        self.update_scoreboard()
