from turtle import Turtle

class ScoreBoard(Turtle):


    def __init__(self,position):
        super().__init__()
        self.position = position
        self.color("white")
        self.penup()
        self.hideturtle()


    def score_display(self,score):
        self.clear()
        self.goto(self.position)
        self.write(arg = str(score), align = "center", font = ("Courier",80,"bold"))
