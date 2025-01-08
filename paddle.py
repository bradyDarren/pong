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
        self.create_paddles()

    def create_paddles(self):
        for paddle in range (2):
            paddle = Turtle(self.paddle_shape)
            paddle.penup()
            paddle.setheading(self.heading)
            paddle.color(self.color, self.color)
            paddle.shapesize(stretch_len = 4, stretch_wid = .5)
            if len(self.two_paddles) != 1:
                paddle.goto(x = -self.xcord, y = self.ycord)
            else:
                paddle.goto(x = self.xcord, y = self.ycord)
            self.two_paddles.append(paddle)

# figure out how to take an input of the player playing and respond using the keystroke.
    def move_up_1(self):
        self.two_paddles[0].forward(20)
    
    def move_down_1(self):
        self.two_paddles[0].backward(20)
    
    def move_up_2(self):
        self.two_paddles[1].forward(20)
    
    def move_down_2(self):
        self.two_paddles[1].backward(20)