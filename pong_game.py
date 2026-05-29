from turtle import Screen
from paddle import Paddle
from pong_ball import PongBall
from score_board import ScoreBoard
import time

def game_over():
    global is_game_on
    is_game_on = False

screen = Screen()
screen.setup(width=1000, height=1000)
width = screen.window_width()
height = screen.window_height()
screen.bgcolor("black")
screen.tracer(0)

is_game_on = True
paddle_bat_1 = Paddle((480,0))
paddle_bat_2 = Paddle((-480,0))
pong_center = Paddle((0,510))
pong_center.center_line()
ball = PongBall()
ball.place_pongball()
P1_Board = ScoreBoard((200,380))
P2_Board = ScoreBoard((-200,380))
Player_1_Score = 0
Player_2_Score = 0


while is_game_on:
    screen.update()
    screen.listen()
    time.sleep(ball.ball_speed)
    screen.onkey(game_over, "space")
    screen.onkey(paddle_bat_1.paddle_up, "i")
    screen.onkey(paddle_bat_2.paddle_up, "w")
    screen.onkey(paddle_bat_1.paddle_down, "m")
    screen.onkey(paddle_bat_2.paddle_down, "s")
    P1_Board.score_display(Player_1_Score)
    P2_Board.score_display(Player_2_Score)
    ball.initial_move()

    if ball.ycor() > height/2 - 20 or ball.ycor() < (-1*(height/2)) + 20:
        ball.bounce_border()
        # ball.ball_speed += 0.1

    if ball.distance(paddle_bat_1) < 60 and ball.xcor() >440 or ball.distance(paddle_bat_2) < 50 and ball.xcor() <-440 :
        ball.bounce_paddle()
        # ball.ball_speed += 0.1

    if ball.xcor()> 460 :
        ball.reset_ball()
        Player_2_Score += 1


    elif ball.xcor()< -460 :
        ball.reset_ball()
        Player_1_Score += 1

screen.exitonclick()
