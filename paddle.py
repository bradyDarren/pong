from turtle import Turtle

# set inital coordinates of paddle
# adjust this to inherit the Turtle Class and remove the create_paddles method.
class Paddles(Turtle):
    def __init__(self, coordinates):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len = .5, stretch_wid = 5)
        self.penup()
        self.goto(coordinates)

# movement functions for the first paddle.
    def move_up_1(self):
        move_to = self.ycor() + 20
        self.goto(self.xcor(), move_to)
    
    def move_down_1(self):
        move_to = self.ycor() - 20
        self.goto(self.xcor(), move_to)
