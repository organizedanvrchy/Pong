from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 230)
        self.write(self.l_score, align="center", font=("Courier", 40, "bold"))
        self.goto(100, 230)
        self.write(self.r_score, align="center", font=("Courier", 40, "bold"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def display_winner(self, winner_text):
        self.goto(0, 0)
        self.write(winner_text, align="center", font=("Courier", 36, "bold"))

class ScreenDivider(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.draw_split_line()

    def draw_split_line(self):
        self.goto(0, 300)  # Start from the top
        self.setheading(270)  # Point downward
        self.pendown()
        self.width(2)  # Adjust line thickness if needed
        for _ in range(30):  # Dashed line
            self.forward(10)
            self.penup()
            self.forward(10)
            self.pendown()
