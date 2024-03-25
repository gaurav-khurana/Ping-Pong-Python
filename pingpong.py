# PING PONG GAME
# Youtube @ freecodecamp.org; link - https://www.youtube.com/watch?v=XGf2GcyHPhc
import turtle
import os

win = turtle.Screen()
win.title("Ping Pong by Gaurav")  # set title on turtle window
win.bgcolor("blue")  # set background color
win.setup(width=800, height=600)
# on XY plane, so width is -400 0 +400 & heigth + 300 0 -300
win.tracer(0)

# SCORE
score_a = 0
score_b = 0

# PADDLE A
paddle_a = turtle.Turtle()  # create obj of Turtle class
paddle_a.speed(0)
# here speed is for the animation on the screen 0 - fastest, 10 - fast, 6 - normal, 3 - slow, 1 - slowest
paddle_a.shape("square")  # can be square, circle, triangle
# default shape size is 20 pixels by 20 pixels
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
# width 5 i.e. default wid 20 x 5 = 100 pixels; same with length
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350, 0)  # coordinates of paddle ie. X -350, Y 0

# PADDLE B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350, 0)

# BALL
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2  # dx is short for direction in plane x
ball.dy = 2
# above dx & dy gives ball direction to move to top right corner

# PEN
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()  # if pendown then we see a line being drawn in animation
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: 0 Player 2: 0", align="center",
          font=('Courier', 24, "normal"))

# FUNCTION


def paddle_a_up():
    y = paddle_a.ycor()  # ycor - to get y coordinates of paddle
    y += 20  # change y coordinate by this value
    paddle_a.sety(y)  # set value of y coordinate


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


def quit_game():  # bug - doesnt quit game directly
    pen.clear()
    pen.write("You have quit game the game. Thank you for playing",
              align="center", font=("Courier", 24, "normal"))
    turtle.done()  # stops turtle graphics and ends game


# KEYBOARD BINDING
win.listen()  # listen for key input on keyboard
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")
win.onkeypress(quit_game, "q")

# MAIN GAME LOOP
while True:
    win.update()  # performs sceen update to start entire loop again

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("afplay bounce.wav&")
        # afplay is to play sound from mac, soundfile should b in same folder as .py,
        # preferred format- .wav; add '&' at end of .wav i.e. ".wav&" to avoid hang during soundplay

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("afplay bounce.wav&")

    if ball.xcor() > 390:
        ball.goto(0, 0)
        os.system("afplay retro-power-down.wav&")
        ball.dx *= -1
        score_a += 1
        pen.clear()  # clear screen to recieve new write msg; or else will just overwrite on last msg
        pen.write(f"Gaurav: {score_a} Suraj: {score_b}", align="center",
                  font=('Courier', 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        os.system("afplay retro-power-down.wav&")
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f"Gaurav: {score_a} Suraj: {score_b}", align="center",
                  font=('Courier', 24, "normal"))

    # Paddle and Ball collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
        os.system("afplay bounce.wav&")

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
        os.system("afplay bounce.wav&")

    # Win condition
    if (score_a == 5):
        pen.clear()
        pen.write("Gaurav wins", align="center",
                  font=("Courier", 30, "normal"))
        turtle.done()

    if (score_b == 5):
        pen.clear()
        pen.write("Suraj wins", align="center",
                  font=("Courier", 30, "normal"))
        turtle.done()
