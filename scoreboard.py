from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highest_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()     # here we are clearing the turtle graphic
        self.write(f"score:{self.score}  highest score:{self.highest_score}", align="center", font=("arial", 24, "normal"))

    def increase_score(self):
        self.score += 10
        self.clear()      # here we are clearing the turtle graphic
        self.update_scoreboard()

    def game_reset(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", align="center", font=("arial", 24, "normal"))
