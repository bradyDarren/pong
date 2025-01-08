from turtle import Screen
from scoreboard import Scoreboard
from paddle import Paddles

# background setup 
window = Screen()
window.bgcolor("black")

#set window size & title
window.setup(width=1250, height=1000)
window_height = window.window_height()
window_width = window.window_width()
window.title("PONG GAME")

window.listen()

# scoreboard = Scoreboard()
# scoreboard.create_net(window_height)

paddle_one = Paddles(xcord = -600, ycord= 0)

window.onkey(key="Up",fun=paddle_one.move_up)
window.onkey(key="Down",fun=paddle_one.move_down)


window.exitonclick()