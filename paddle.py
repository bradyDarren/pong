from turtle import Turtle

# set inital coordinates of paddle
class Paddle: 
    def __init__(self, xcord, ycord, color = "white", paddle_shape = "square"):
        self.xcord = xcord 
        self.ycord = ycord
        self.paddle_shape = paddle_shape
        self.color = color
        self.segments = []
    
    def create_paddle(self):
        for i in range(4):
            paddle_segment = Turtle(shape=self.paddle_shape)
            paddle_segment.penup()
            paddle_segment.color(self.color, self.color)
            paddle_segment.goto(x = self.xcord, y = self.ycord + (20 * i))
            self.segments.append(paddle_segment)


