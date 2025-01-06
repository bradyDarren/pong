from turtle import Turtle
#tasks: 
# 1. create scoreboard to display player 1 and player 2 scores.
# 2. create the net that runs down the middle of the screen.

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
        # self.create_net()
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
    
# creates the net in the middle of the screen.
# """Reevaluate this function - questionable"""
    def net_section(self):
        net_section = Turtle(shape="square")
        net_section.penup()
        net_section.color(self.tint,self.tint)
        net_section.shapesize(stretch_wid = 1.5, stretch_len = .25)
        net_section.goto(x=self.x_cor, y= self.y_cor)
        self.net.append(net_section)
    
    # def create_net(self):
    #     while self.net[-1::].ycor() > 480:
    #         self.net_section()
    #         self.ycor -= 45

score = Scoreboard()
for _ in range(3):
    score.net_section()


