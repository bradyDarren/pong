from turtle import Turtle

# constructor - creates scoreboard
class Scoreboard(Turtle): 
    def __init__(self, x_cor = 0, y_cor = 450, tint = "white"):
        super().__init__()
        self.p1_score = 0 
        self.p2_score = 0
        self.hideturtle()
        self.penup()
        self.tint = tint
        self.color(self.tint, self.tint)
        self.y_cor = y_cor
        self.x_cor = x_cor
        self.goto(x = self.x_cor,y = self.y_cor)
        self.net = []
        self.net_section() 
        self.update_scorboard()

# creates scoreboard - displays p1 and p2 current score.
    def update_scorboard(self):
        self.clear()
        self.write(f"{self.p1_score}          {self.p2_score}", move = False, align = "center", font = ("Times New Roman", 40, "normal"))

# # takes winning player for that set and increases that player score.  
    def increase_score(self, player):
        if player == 1:
            self.p1_score += 1
        elif player == 2:
            self.p2_score += 2
        self.update_scorboard()
    
# creates a single section of the net within the middle of the screen.
    def net_section(self):
        net_section = Turtle(shape="square")
        net_section.penup()
        net_section.color(self.tint,self.tint)
        net_section.shapesize(stretch_wid = 1.5, stretch_len = .25)
        net_section.goto(x=self.x_cor, y= self.y_cor)
        self.net.append(net_section)
    
# creates the entire net based on window size.
    def create_net(self, net_height):
        net_height = (net_height / 2) - 60
        while self.net[-1].ycor() > -net_height:
            self.net_section()
            self.y_cor -= 45



