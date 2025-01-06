from turtle import Screen
from scoreboard import Scoreboard

# background setup 
window = Screen()
window.bgcolor("black")
window.setup(width=1250, height=1000)
window_height = window.window_height()
window_width = window.window_width()
window.title("PONG GAME")


scoreboard = Scoreboard()
scoreboard.create_net(window_height)




window.exitonclick()