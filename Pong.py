# Pong

import turtle   #module for simple games and graphics

wn = turtle.Screen()    #captial S is important
wn.title("Pong by Tim Demetriades")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)    #stops window from updating, speeds up the game

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
ball.penup()    
ball.goto(0, 0)  # x and y coordinates

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

