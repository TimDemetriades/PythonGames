# Pong

import turtle   #module for simple games and graphics
import winsound #module for playing sounds from files in windows

wn = turtle.Screen()    #captial S is important
wn.title("Pong by Tim Demetriades")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)    #stops window from updating, speeds up the game

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()  #turtle = module , Turtle = class (in turtle module)
paddle_a.speed(0)   # speed of animation, set to max
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)    #makes width 20x5 and length 20*1
paddle_a.penup()    
paddle_a.goto(-350, 0)  # x and y coordinates

# Paddle B
paddle_b = turtle.Turtle()  #turtle = module , Turtle = class (in turtle module)
paddle_b.speed(0)   # speed of animation, set to max
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)    #makes width 20x5 and length 20*1
paddle_b.penup()    
paddle_b.goto(350, 0)  # x and y coordinates

# Ball
ball = turtle.Turtle()  #turtle = module , Turtle = class (in turtle module)
ball.speed(0)   # speed of animation, set to max
ball.shape("square")
ball.color("white")
ball.penup()    #Prevents lines on screen
ball.goto(0, 0)  # x and y coordinates
ball.dx = 0.1 # change in x
ball.dy = 0.1 # change in y

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Comic Sans MS", 24, "normal"))

# Function
def paddle_a_up():
    y = paddle_a.ycor() #paddle_a = name of object , ycor = method from turtle module that returns y cordinate
    y += 20 # move y 20 up
    paddle_a.sety(y)    # moves paddle to new y coordinate

def paddle_a_down():
    y = paddle_a.ycor() #paddle_a = name of object , ycor = method from turtle module that returns y cordinate
    y -= 20 # move y 20 up
    paddle_a.sety(y)    # moves paddle to new y coordinate

def paddle_b_up():
    y = paddle_b.ycor() #paddle_b = name of object , ycor = method from turtle module that returns y cordinate
    y += 20 # move y 20 up
    paddle_b.sety(y)    # moves paddle to new y coordinate

def paddle_b_down():
    y = paddle_b.ycor() #paddle_b = name of object , ycor = method from turtle module that returns y cordinate
    y -= 20 # move y 20 up
    paddle_b.sety(y)    # moves paddle to new y coordinate

# Keyboard binding
wn.listen() # Listens for keyboard inputs
wn.onkeypress(paddle_a_up, "w") # When user presses lowercase w key, calls function paddle_a_up
wn.onkeypress(paddle_a_down, "s") # When user presses lowercase w key, calls function paddle_a_down
wn.onkeypress(paddle_b_up, "Up") # When user presses lowercase w key, calls function paddle_b_up
wn.onkeypress(paddle_b_down, "Down") # When user presses lowercase w key, calls function paddle_b_down

# Main game loop
while True:
    wn.update() #everytime the loop runs it updates the screen

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)    # Moves ball right
    ball.sety(ball.ycor() + ball.dy)    # Moves ball up

    # Border checking
    if ball.ycor() > 290:   # if y coordinate is 300 (half screen height) - 10 (half ball height)
        ball.sety(290)      # keep ball at 290
        ball.dy *= -1       # and reverse direction
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)    # adds sound when bouncing off stuff, async lets it happen w/out pausing game

    if ball.ycor() < -290:  # if y coordinate is -300 (half screen height) - -10 (half ball height)
        ball.sety(-290)     # keep ball at -290
        ball.dy *= -1       # and reverse direction
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:   # if x cooridnate is 400 (half screen width) - 10 (half ball width)
        ball.goto(0, 0)     # put ball back at center
        ball.dx *= -1       # and reverse direction
        score_a += 1        # increase score by one
        pen.clear()         # clear score pen
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Comic Sans MS", 24, "normal"))

    if ball.xcor() < -390:  # if x cooridnate is -400 (half screen width) - -10 (half ball width)
        ball.goto(0, 0)     # put ball back at center
        ball.dx *= -1       # and reverse direction
        score_b += 1        # increase score by one
        pen.clear()         # clear score pen
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Comic Sans MS", 24, "normal"))

    # Paddle and ball collisions
    if (ball.xcor() > 350 - 10 and ball.xcor() < 350) and (ball.ycor()) < paddle_b.ycor() + (50 - 10) and ball.ycor() > paddle_b.ycor() - (50 - 10):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor()) < paddle_a.ycor() + (50 - 10) and ball.ycor() > paddle_a.ycor() - (50 - 10):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
   