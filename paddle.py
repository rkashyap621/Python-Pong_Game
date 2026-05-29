from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.position = position
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(self.position[0], self.position[1])

    def center_line(self):
        self.setheading(270)
        while self.ycor() > -600:
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)

    def paddle_up(self):
        new_pos = self.pos()[1] + 20
        self.goto(self.xcor(), new_pos)


    def paddle_down(self):
        new_pos = self.pos()[1] - 20
        self.goto(self.xcor(), new_pos)
