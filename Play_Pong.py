# Jackson J
# 5.20.2020
# freeCodeCamp.org is a great YouTube channel that teaches code to people, whether they are beginners or not
# The idea to recreate this game was given to me by a friend, and the code is inspired by that channel
from turtle import *
from random import *
from time import sleep

window = Screen()
window.title("Throwback PONG")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# Creating Players and Ball

# Player 1
player1 = Turtle()
player1.speed(0)
player1.shape("square")
player1.shapesize(stretch_wid=5, stretch_len=1)
player1.color("white")
player1.penup()
player1.goto(-350, 0)


def player1_up():
    if player1.ycor() < 250:
        y = player1.ycor()
        y += 20
        player1.sety(y)


def player1_down():
    if player1.ycor() > -250:
        y = player1.ycor()
        y -= 20
        player1.sety(y)


# Player 2
player2 = Turtle()
player2.speed(0)
player2.shape("square")
player2.shapesize(stretch_wid=5, stretch_len=1)
player2.color("white")
player2.penup()
player2.goto(350, 0)


def player2_up():
    if player2.ycor() < 250:
        y = player2.ycor()
        y += 20
        player2.sety(y)


def player2_down():
    if player2.ycor() > -250:
        y = player2.ycor()
        y -= 20
        player2.sety(y)


window.listen()
window.onkeypress(player1_up, "w")
window.onkeypress(player1_down, "s")
window.onkeypress(player2_up, "Up")
window.onkeypress(player2_down, "Down")

# Ball
ball = Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)

dir_ = randint(1, 12)
if dir_ <= 3:
    ball.dx = .5
    ball.dy = .5
if 3 < dir_ < 7:
    ball.dx = -.5
    ball.dy = .5
if 6 < dir_ < 10:
    ball.dx = .5
    ball.dy = -.5
if dir_ >= 10:
    ball.dx = -.5
    ball.dy = -.5

# Creating the scoreboard
score_board = Turtle()
score_board.speed(0)
score_board.color("white")
score_board.penup()
score_board.hideturtle()
score_board.goto(0, 260)
score_board.write("Player 1: 0  Player 2: 0", align="center", font=("Courier", 24, "bold"))
player1_score = 0
player2_score = 0

# Continuing
cont = Turtle()
cont.speed(0)
cont.color("green")
cont.penup()
cont.hideturtle()
cont.goto(0, 0)


def continue_():
    return "a"


this = window.onkeypress(continue_(), "b")

# Main Game Loop
while player1_score != 10 or player2_score != 10:
    window.update()

    # Ball Movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Checking the Window Border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    dir_ = randint(1, 6)
    if ball.xcor() < -380 or ball.xcor() > 380:
        if ball.xcor() < -380:
            player2_score += 1
        else:
            player1_score += 1

        score_board.clear()
        score_board.write(f"Player 1: {player1_score}  Player 2: {player2_score}", align="center", font=("Courier", 24, "bold"))

        cont.write("CONTINUING IN: 3", align="center", font=("Courier", 24, "bold"))
        sleep(1)
        cont.clear()
        cont.write("CONTINUING IN: 2", align="center", font=("Courier", 24, "bold"))
        sleep(1)
        cont.clear()
        cont.write("CONTINUING IN: 1", align="center", font=("Courier", 24, "bold"))
        sleep(1)
        cont.clear()

        ball.goto(0, 0)
        if dir_ < 4:
            ball.dx *= -1
        else:
            ball.dx *= -1
            ball.dy *= -1

    # Collision between Ball and Paddle
    if -345 <= ball.xcor() <= -340 and \
            (player1.ycor() - 50 < ball.ycor() < player1.ycor() + 50):
        ball.setx(-340)
        ball.dx *= -1

    if 345 >= ball.xcor() >= 340 and \
            (player2.ycor() - 50 < ball.ycor() < player2.ycor() + 50):
        ball.setx(340)
        ball.dx *= -1
