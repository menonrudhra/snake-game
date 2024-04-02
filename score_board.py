from turtle import Turtle

SCOREBOARD_FONT = ("Arial", 25, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            content = file.read()
            self.high_score = int(content)
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 270)
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(arg=f"Score = {self.score} High Score = {self.high_score}", align=ALIGNMENT, font=SCOREBOARD_FONT)

    def increase_score(self):
        self.score += 1
        self.display_score()

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
        with open("data.txt", "w") as file:
            file.write(str(self.high_score))
        self.score = 0
        self.display_score()
