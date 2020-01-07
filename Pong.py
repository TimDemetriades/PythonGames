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

# Main game loop
while True:
    wn.update() #everytime the loop runs it updates the screen

