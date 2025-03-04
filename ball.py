from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 5
        self.y_move = 5
        self.move_speed = 0.075
        self.random_start_direction()

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def wall_bounce(self):
        self.y_move *= -1

    def paddle_bounce(self):
        self.x_move *= -1
        self.move_speed *= 0.95

        # Change ball color based on speed
        if self.move_speed < 0.025:
            self.color("red")
        elif self.move_speed < 0.05:
            self.color("yellow")
        else:
            self.color("white")

    def reset_pos(self):
        self.goto(0, 0)
        self.color("white")
        self.move_speed = 0.075
        self.random_start_direction()

    def random_start_direction(self):
        self.x_move = random.choice([10, -10])  # Randomly choose left or right
        self.y_move = random.choice([10, -10])  # Randomly choose up or down
