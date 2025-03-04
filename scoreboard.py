from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self._initialize_scoreboard()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def _initialize_scoreboard(self):
        """Initialize the scoreboard's appearance and properties."""
        self.color("white")
        self.penup()
        self.hideturtle()

    def update_scoreboard(self):
        """Update the scoreboard with the current scores."""
        self.clear()
        self._display_score(-100, 230, self.l_score)  # Left player score
        self._display_score(100, 230, self.r_score)  # Right player score

    def _display_score(self, x, y, score):
        """Display a score at the specified position."""
        self.goto(x, y)
        self.write(score, align="center", font=("Courier", 40, "bold"))

    def l_point(self):
        """Increase the left player's score and update the scoreboard."""
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        """Increase the right player's score and update the scoreboard."""
        self.r_score += 1
        self.update_scoreboard()

    def display_winner(self, winner_text):
        """Display the winner's message on the screen."""
        self.goto(0, 0)
        self.write(winner_text, align="center", font=("Courier", 36, "bold"))


class ScreenDivider(Turtle):
    def __init__(self):
        super().__init__()
        self._initialize_divider()
        self.draw_split_line()

    def _initialize_divider(self):
        """Initialize the screen divider's appearance and properties."""
        self.color("white")
        self.penup()
        self.hideturtle()
        self.width(2)  # Set line thickness

    def draw_split_line(self):
        """Draw a dashed line to divide the screen."""
        self.goto(0, 300)  # Start from the top
        self.setheading(270)  # Point downward
        self.pendown()
        for _ in range(30):  # Draw a dashed line
            self.forward(10)
            self.penup()
            self.forward(10)
            self.pendown()
