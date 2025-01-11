from turtle import Screen
from scoreboard import Scoreboard
from paddle import Paddles
from ball import Ball
import time  

# background setup 
window = Screen()
window.bgcolor("black")

#set window size & title
window.setup(width=800, height=600)
window_height = window.window_height()
window.title("PONG GAME")

# removes the automatic animation from our window.
window.tracer(0)

window.listen()

scoreboard = Scoreboard(window_height/2)
scoreboard.create_net()

paddle_1 = Paddles((-370,0))
paddle_2 = Paddles((370,0))

window.onkey(key = "Up", fun = paddle_1.move_up)
window.onkey(key = "Down", fun = paddle_1.move_down)

window.onkey(key = "a", fun = paddle_2.move_up)
window.onkey(key = "z", fun = paddle_2.move_down)

ball = Ball()
game_on = True
game_speed = .1

while game_on: 
    time.sleep(game_speed)
    window.update()
    # ball.ball_movement()

#     if ball.ycor() >= 290 or ball.ycor() <= -290:
#         ball.bounce_y()
    
#     if ball.distance(paddle_1) < 50 and ball.xcor() > 340 or ball.distance(paddle_2) < 50 and ball.xcor() < -340:
#         ball.bounce_x()

window.exitonclick()