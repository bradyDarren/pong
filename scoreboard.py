from turtle import Turtle

x_cor = 0
y_cor = 615
color = "white"

# constructor - creates scoreboard
class Scoreboard(Turtle): 
    def __init__(self):
        super.__init__(shape = "square")
        self.p1_score = 0 
        self.p2_score = 0
        self.color(color, color)
        self.goto(x= x_cor,y= y_cor)
        self.net = []
        self.create_net()
        self.update_scorboard()

# creates scoreboard - displays p1 and p2 current score.
    def update_scorboard(self):
        self.clear()
        self.write()
        


# creates the net in the middle of the screen.
    def create_net(self):
        while self.net[-1::].ycor() > -y_cor:
            net_section = Turtle()
            net_section.color(color,color)
            net_section.goto(x=x_cor,y=y_cor)





