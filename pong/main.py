import turtle

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("light blue")
wn.setup(width = 800, height = 600)
wn.tracer(0)

#Paddle A
paddleA = turtle.Turtle()
paddleA.speed(0)
paddleA.shape("square")
paddleA.color("white")
paddleA.shapesize(5, 1)
paddleA.penup()
paddleA.goto(-350, 0)
#Paddle B
paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.shape("square")
paddleB.color("white")
paddleB.shapesize(5, 1)
paddleB.penup()
paddleB.goto(350, 0)
#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = 0.2
#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)

#Score
scoreA = 0
scoreB = 0
pen.write("Player A: 0   Player B: 0", align="center", font=24)
#Moving paddle
def paddleA_up():
    y = paddleA.ycor()
    y += 20
    paddleA.sety(y)

def paddleA_down():
    y = paddleA.ycor()
    y -= 20
    paddleA.sety(y)
def paddleB_up():
    y = paddleB.ycor()
    y += 20
    paddleB.sety(y)

def paddleB_down():
    y = paddleB.ycor()
    y -= 20
    paddleB.sety(y)
#Keyboard binding
wn.listen()
wn.onkeypress(paddleA_up, "w ")
wn.onkeypress(paddleA_down, "s")
wn.onkeypress(paddleB_up, "Up")
wn.onkeypress(paddleB_down, "Down")

#Main game
while True:
    wn.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreA += 1
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(scoreA, scoreB), align="center", font=24)
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreB += 1
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(scoreA, scoreB), align="center", font=24)
    #Paddle and ball
    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddleB.ycor() + 40 and ball.ycor() > paddleB.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
    if ball.xcor() < -340 and ball.xcor() > -350 and (
            ball.ycor() < paddleA.ycor() + 40 and ball.ycor() > paddleA.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
