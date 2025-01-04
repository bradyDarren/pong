from turtle import Turtle
#tasks: 
# 1. create scoreboard to display player 1 and player 2 scores.
# 2. create the net that runs down the middle of the screen.

# constructor - creates scoreboard
class Scoreboard(Turtle): 
    def __init__(self, x_cor = 0, y_cor = 615, color = "white"):
        super.__init__(shape = "square")
        self.p1_score = 0 
        self.p2_score = 0
        self.color(color, color)
        self.goto(x = x_cor,y = y_cor)
        self.net = []
        self.create_net()
        self.update_scorboard()

# creates scoreboard - displays p1 and p2 current score.
    def update_scorboard(self):
        self.clear()
        self.write(f"{self.p1_score}          {self.p2_score}")

# takes winning player for that set and increases that player score.  
    def increase_score(self, player):
        if player == 1:
            self.p1_score += 1
        elif player == 2:
            self.p2_score += 2
    
# creates the net in the middle of the screen.
    def create_net(self):
        if self.net[-1::].ycor() > -y_cor:
            for _ in range(3):
                net_section = Turtle()
                net_section.color(self.color,self.color)
                net_section.goto(x=self.x_cor,y=self.y_cor)
                self.net.append(net_section)
                y_cor -= 20
            y_cor -= 60





