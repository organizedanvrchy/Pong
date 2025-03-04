from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self._initialize_paddle()
        self.goto(position)

    def _initialize_paddle(self):
        """Initialize the paddle's appearance and properties."""
        self.shape("square")
        self.shapesize(5, 1, 0)  # Stretch the paddle to be 5x taller and 1x wider
        self.color("white")
        self.penup()

    def up(self):
        """Move the paddle upward by 40 units, but not beyond the top boundary."""
        if self.ycor() < 240:  # Prevent the paddle from moving off the screen
            new_y = self.ycor() + 40
            self.goto(self.xcor(), new_y)

    def down(self):
        """Move the paddle downward by 40 units, but not beyond the bottom boundary."""
        if self.ycor() > -240:  # Prevent the paddle from moving off the screen
            new_y = self.ycor() - 40
            self.goto(self.xcor(), new_y)
