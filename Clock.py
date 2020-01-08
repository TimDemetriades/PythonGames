# Simple Analog Clock

import turtle           # turtle module
wn = turtle.Screen()    # sets up screen window
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.title("Simple Analog Clock by Tim Demetriades")

# Create our drawing pen
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)            # animation speed (max)
pen.pensize(3)

def draw_clock(pen):    # function to draw clock using pen

    # Draws clock face
    pen.up()            # do not draw line
    pen.goto(0, 210)    # put turtle at the top
    pen.setheading(180) # and face it to the left
    pen.color("green")
    pen.pendown()       # begin drawing line
    pen.circle(210)     # create circle with radius 210

    # Draw the lines for the hours
    pen.penup()
    pen.goto(0,0)
    pen.setheading(90)

    for _ in range(12):
        pen.fd(190)     # puts pen right before circle
        pen.pendown()
        pen.fd(20)      # draws line to circle
        pen.penup()
        pen.goto(0,0)
        pen.rt(30)      #repeats every 30 degrees

draw_clock(pen)




wn.mainloop()   #keeps window from closing