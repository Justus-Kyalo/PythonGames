import turtle
wn=turtle.Screen()
wn.title("pong game by @remmy")
wn.bgcolor ("black")
wn.setup(width=600,height=800)
wn.tracer(0)

paddle_a=turtle.Turtle()
paddle_a.speed(0)
paddle_a.color("white")
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.goto(-350,0)
paddle_a.penup()

paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.color("white")
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=6,stretch_len=1)
paddle_b.goto(350,0)
paddle_b.penup()

ball=turtle.Turtle()
ball.speed(0)
ball.color("white")
ball.shape("square")
ball.goto(0,0)
ball.penup()
ball.dx=2
ball.dy=-2
#pen
pen=turtle.Turtle()
pen.color("white")
pen.speed(0)
pen.goto(0,260)
pen.penup()
pen.hideturtle()
pen.write("player A:0 player B:0",align="center", font=( "courier",24,"normal"))
#functions to move the paddles

def paddle_a_up():
    y=paddle_a.ycor()
    y+=20
    paddle_a.sety(y)

def paddle_a_down():
    y=paddle_a.ycor()
    y-=20
    paddle_a.sety(y)

def paddle_b_up():
    y=paddle_b.ycor()
    y+=20
    paddle_b.sety(y)

def paddle_b_down():
    y=paddle_b.ycor()
    y-=20
    paddle_b.sety(y)
    #key binding calling the functions
wn.listen()
wn.onkeypress(paddle_a_up(),"w")
wn.onkeypress(paddle_a_down(),"s")
wn.onkeypress(paddle_b_up(),"Up")
wn.onkeypress(paddle_b_down(),"Down")

while True:
    wn.update()
ball.sety(ball.ycor()+ball.dy)
ball.setx(ball.xcor()+ball.dx)

if ball.ycor>290:
    ball.sety(290)
    ball.dy*=-1
if ball.ycor>-290:
    ball.sety(-290)
    ball.dy*=-1
if ball.xcor()>390:
   ball.goto(0,0)
   ball.dx*=-1
   score_a+=1
   pen.clear()
   pen.write("player A:0 player B:0", align="center", font=(
   "courier", 24, "normal"))

if ball.xcor()>-390:
   ball.goto(0,0)
   ball.dx*=-1
   score_b+=1
   pen.clear()
   pen.write("player A:0 player B:0", align="center", font=(
   "courier", 24, "normal"))
if (ball.xcor()>340 and ball.xcor()<350 )and (ball.ycor()<paddle_b.ycor()+40 and ball.ycor()>paddle_b.ycor()-40):
   ball.setxcor(340)
   ball.dx*=-1

if (ball.xcor() <340 and ball.xcor() < -350) and (ball.ycor() >paddle_a.ycor()+40 and ball.ycor() > paddle_b.ycor()-40):
    ball.setxcor(-340)
    ball.dx *= -1
