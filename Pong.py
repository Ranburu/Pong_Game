import turtle


wn = turtle.Screen()
wn.title("Pong by Ranburu")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer()

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_len=1, stretch_wid=5)
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_len=1, stretch_wid=5)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))


# Functions
def pause():
    pause = turtle.Turtle()
    pause.speed(0)
    pause.shape("square")
    pause.shapesize(stretch_len=1, stretch_wid=3)
    pause.color("white")
    pause.penup()
    pause.goto(10, 0)


def puddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def puddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def puddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def puddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Keyboard binding
wn.listen()
wn.onkeypress(puddle_a_up, "w")
wn.onkeypress(puddle_a_down, "s")
wn.onkeypress(puddle_b_up, "Up")
wn.onkeypress(puddle_b_down, "Down")

# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy *= -1

    if ball.xcor() > 380:
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    if ball.xcor() < -390:
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    # Checking paddle border
    if paddle_a.ycor() > 245:
        paddle_a.sety(245)

    if paddle_a.ycor() < -240:
        paddle_a.sety(-240)

    if paddle_b.ycor() > 245:
        paddle_b.sety(245)

    if paddle_b.ycor() < -240:
        paddle_b.sety(-240)

    # Paddle and ball collisions
    if (ball.xcor() > 330 and ball.xcor() < 340) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(330)
        ball.dx *= -1
    if (ball.xcor() < -330 and ball.xcor() > -340) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-330)
        ball.dx *= -1