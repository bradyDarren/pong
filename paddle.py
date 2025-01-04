from turtle import Turtle

# set inital coordinates of paddle
class Paddles: 
    def __init__(self, xcord, ycord, color = "white", paddle_shape = "square", heading = 90):
        self.xcord = xcord 
        self.ycord = ycord
        self.paddle_shape = paddle_shape
        self.color = color
        self.heading = heading
        self.two_paddles = []
        self.create_paddle()

    
    def create_paddle(self):
        paddle = Turtle(self.paddle_shape)
        paddle.setheading(self.heading)
        paddle.goto(x = self.xcord, y = self.ycord)
        paddle.penup()
        paddle.color(self.color, self.color)
        paddle.shapesize(stretch_len = .5, stretch_wid = 4)
    
    def move_up(self, player):
        self.two_paddles[player - 1].forward(10)
    
    def move_down(self, player):
        self.two_paddles[player - 1].backward(10)