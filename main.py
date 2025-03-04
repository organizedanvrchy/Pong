from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard, ScreenDivider
import time

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PADDLE_POSITIONS = [(350, 0), (-350, 0)]
WINNING_SCORE = 10

# Screen Setup
def setup_screen():
    screen = Screen()
    screen.bgcolor("black")
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.title("Pong")
    screen.tracer(0)
    return screen

# Paddle Initialization
def setup_paddles():
    r_paddle = Paddle(PADDLE_POSITIONS[0])
    l_paddle = Paddle(PADDLE_POSITIONS[1])
    return r_paddle, l_paddle

# Keybinds
def setup_keybinds(screen, l_paddle, r_paddle):
    screen.listen()
    screen.onkey(l_paddle.up, "w")
    screen.onkey(l_paddle.down, "s")
    screen.onkey(r_paddle.up, "Up")
    screen.onkey(r_paddle.down, "Down")

# Detect Collisions
def detect_collisions(ball, r_paddle, l_paddle):
    # Detect Collision with Wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()

    # Detect Collision with Right Paddle
    if ball.x_move > 0 and ball.xcor() > 320 and ball.distance(r_paddle) < 50:
        ball.paddle_bounce()

    # Detect Collision with Left Paddle
    if ball.x_move < 0 and ball.xcor() < -320 and ball.distance(l_paddle) < 50:
        ball.paddle_bounce()

# Detect Scoring
def detect_scoring(ball, scoreboard):
    if ball.xcor() > 380:
        ball.reset_pos()
        scoreboard.l_point()
        return scoreboard.l_score == WINNING_SCORE, "Left Player Wins!"

    if ball.xcor() < -380:
        ball.reset_pos()
        scoreboard.r_point()
        return scoreboard.r_score == WINNING_SCORE, "Right Player Wins!"

    return False, ""

# Main Game Loop
def main_game_loop(screen, ball, r_paddle, l_paddle, scoreboard):
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(ball.move_speed)  # Use the ball's move_speed attribute
        ball.move()

        detect_collisions(ball, r_paddle, l_paddle)

        game_over, winner_message = detect_scoring(ball, scoreboard)
        if game_over:
            scoreboard.display_winner(winner_message)
            game_is_on = False

    screen.exitonclick()

# Main Function
def main():
    screen = setup_screen()
    r_paddle, l_paddle = setup_paddles()
    ball = Ball()
    scoreboard = Scoreboard()
    split_screen = ScreenDivider()

    setup_keybinds(screen, l_paddle, r_paddle)
    main_game_loop(screen, ball, r_paddle, l_paddle, scoreboard)

if __name__ == "__main__":
    main()
