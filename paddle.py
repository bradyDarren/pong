from turtle import Turtle

# set inital coordinates of paddle
class Paddle: 
    def __init__(self, paddle_shape = "square", xcord, ycord, color = "white"):
        self.xcord = xcord 
        self.ycord = ycord
        self.paddle_shape = paddle_shape
        self.color = color
        self.segments = []
    
    def create_paddle(self):
        for i in range(4):
            paddle_segment = Turtle(shape=self.paddle_shape)
            paddle_segment.penup()
            

