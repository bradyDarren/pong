from turtle import Turtle
import random 

class Ball(Turtle):
    def __init__(self,shape = "square"):
        super().__init__(shape)
        self.color("white")
        self.shapesize(stretch_len = .75, stretch_wid = .75)
        self.penup() 
        self.ymove = 10
        self.xmove = 10
    
    def ball_movement(self):
        new_xcor = self.xcor() + self.xmove
        new_ycor = self.ycor() + self.ymove
        self.goto(new_xcor, new_ycor)

    def bounce_y(self):
        self.ymove *= -1

    def bounce_x(self):
        self.xmove*= -1
    
    