from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_player_score = 0
        self.right_player_score = 0
        self.update_scores()

    def update_scores(self):
        self.clear()
        self.goto(-50, 250)
        self.write(self.left_player_score, align="left", font=("Arial", 30, "normal"))
        self.goto(50, 250)
        self.write(self.right_player_score, align="right", font=("Arial", 30, "normal"))

    def left_point(self):
        self.left_player_score += 1
        self.update_scores()

    def right_point(self):
        self.right_player_score += 1
        self.update_scores()
