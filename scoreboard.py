from turtle import Turtle

class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("my_text.txt") as data:
            self.highscore = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0,260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align="center", font = ("Cartier", 24, "normal"))
        
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("my_text.txt", mode= "w") as data:
                data.write(f"{self.highscore}")
        self.score=0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()