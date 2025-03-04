from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self._initialize_ball()
        self.x_move = 5
        self.y_move = 5
        self.move_speed = 0.075
        self.random_start_direction()

    def _initialize_ball(self):
        """Initialize the ball's appearance and position."""
        self.shape("circle")
        self.color("white")
        self.penup()

    def move(self):
        """Move the ball by updating its position based on x_move and y_move."""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def wall_bounce(self):
        """Reverse the ball's vertical direction when it hits the top or bottom wall."""
        self.y_move *= -1

    def paddle_bounce(self):
        """Reverse the ball's horizontal direction and increase speed when it hits a paddle.
        Also change the ball's color based on its speed."""
        self.x_move *= -1
        self.move_speed *= 0.95
        self._update_ball_color()

    def _update_ball_color(self):
        """Update the ball's color based on its current speed."""
        if self.move_speed < 0.025:
            self.color("red")
        elif self.move_speed < 0.05:
            self.color("yellow")
        else:
            self.color("white")

    def reset_pos(self):
        """Reset the ball's position, speed, and color to its initial state."""
        self.goto(0, 0)
        self.color("white")
        self.move_speed = 0.075
        self.random_start_direction()

    def random_start_direction(self):
        """Randomly set the ball's initial direction after a reset."""
        self.x_move = random.choice([10, -10])  # Randomly choose left or right
        self.y_move = random.choice([10, -10])  # Randomly choose up or down
