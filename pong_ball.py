from turtle import Turtle
import random

class PongBall(Turtle):

    def __init__(self):
        super().__init__()
        ball_angle = random.choice(range(0, 360, 10))
        self.setheading(ball_angle)
        self.x_move = 8
        self.y_move = 8
        self.ball_speed = 0.1

    def place_pongball(self):
        self.color("white")
        self.shape("circle")
        self.penup()

    def initial_move(self):
        if self.heading() <= 134:
            new_x = self.xcor() + self.x_move
            new_y = self.ycor() + self.y_move
            self.goto(new_x, new_y)
        elif self.heading() <= 224:
            new_x = self.xcor() - self.x_move
            new_y = self.ycor() + self.y_move
            self.goto(new_x, new_y)
        elif self.heading() <= 314:
            new_x = self.xcor() - self.x_move
            new_y = self.ycor() - self.y_move
            self.goto(new_x, new_y)
        elif self.heading() <= 359:
            new_x = self.xcor() + self.x_move
            new_y = self.ycor() - self.y_move
            self.goto(new_x, new_y)

    def bounce_border(self):
        self.y_move *= -1

    def bounce_paddle(self):
        self.x_move *= -1

    def reset_ball(self):
        self.setpos(0, 0)
        self.bounce_paddle()
