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
        self.goto(self.xcor(), (self.ycor() + 20))
    
#     def move_down_1(self):
#         self.two_paddles[0].backward(20)

# # movement functions for the second paddle.
#     def move_up_2(self):
#         self.two_paddles[1].forward(20)
    
#     def move_down_2(self):
#         self.two_paddles[1].backward(20)