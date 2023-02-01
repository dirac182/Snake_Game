from turtle import *
from food import Food


class Scoreboard():

    def __init__(self):

        self.score = 0
        self.board = Turtle()
        with open("data.txt", mode="r") as file:
            contents = file.read()
        self.high_score = int(contents)

    def scoreboard(self):

        self.board.clear()
        self.board.color('white')
        self.board.ht()
        self.board.penup()
        self.board.goto(0,250)
        self.board.write(f"Score: {self.score}  High Score: {self.high_score}",False,align="center", font=('courier',24,'normal'))


    def incease_score(self):

        self.score += 1
        if self.score >= self.high_score:
            self.high_score = self.score
        self.scoreboard()

    def reset(self):

        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.scoreboard()


    #def game_over(self):
    #    self.board.goto(0,0)
    #    self.board.write("Game Over", False, align="center", font=('courier', 24, 'normal'))





