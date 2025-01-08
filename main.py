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

paddles = Paddles(xcord = -600, ycord= 0)

# key functions that enable paddle #1 to move up and down. 
window.onkey(key="Up",fun=paddles.move_up_1)
window.onkey(key="Down",fun=paddles.move_down_1)

# key functions that enable paddle #2 to move up and down. 
window.onkey(key="a",fun=paddles.move_up_2)
window.onkey(key="z",fun=paddles.move_down_2)


window.exitonclick()