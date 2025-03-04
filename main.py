from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard, ScreenDivider
import time

# Screen Setup
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

# Paddle Initialization
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# Ball Initialization
ball = Ball()

# Scoreboard Initialization
scoreboard = Scoreboard()
split_screen = ScreenDivider()

# Keybinds
screen.listen()
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

# Main
def main():
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(ball.move_speed)
        ball.move()


        # Detect Collision with Wall
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.wall_bounce()

        # Detect Collision with Right Paddle
        if ball.x_move > 0 and ball.xcor() > 320 and ball.distance(r_paddle) < 50:
            ball.paddle_bounce()

        # Detect Collision with Left Paddle
        if ball.x_move < 0 and ball.xcor() < -320 and ball.distance(l_paddle) < 50:
            ball.paddle_bounce()

        # Detect if Player Scores
        if ball.xcor() > 380:
            ball.reset_pos()
            scoreboard.l_point()
            if scoreboard.l_score == 10:  # Left player wins
                game_is_on = False
                scoreboard.display_winner("Left Player Wins!")

        if ball.xcor() < -380:
            ball.reset_pos()
            scoreboard.r_point()
            if scoreboard.r_score == 10:  # Right player wins
                game_is_on = False
                scoreboard.display_winner("Right Player Wins!")

    screen.exitonclick()

if __name__ == "__main__":
    main()
