# Pong

import turtle   #module for simple games and graphics

wn = turtle.Screen()    #captial S is important
wn.title("Pong by Tim Demetriades")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)    #stops window from updating, speeds up the game

#Main game loop
while True;
    wn.update() #everytime the loop runs it updates the screen
    
