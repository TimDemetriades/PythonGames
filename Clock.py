# Simple Analog Clock

import time
import turtle           # turtle module
wn = turtle.Screen()    # sets up screen window
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.title("Simple Analog Clock by Tim Demetriades")
wn.tracer(0)

# Create our drawing pen
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)            # animation speed (max)
pen.pensize(3)

def draw_clock(h, m, s, pen):    # function to draw clock using pen

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
        pen.rt(30)      # repeats every 30 degrees

    # Draw the hour hand
    pen.penup()
    pen.goto(0,0)
    pen.color("white")
    pen.setheading(90)  # set heading to straight up
    angle = (h / 12) * 360
    pen.rt(angle)
    pen.pendown()
    pen.fd(100)

    # Draw the minute hand
    pen.penup()
    pen.goto(0,0)
    pen.color("blue")
    pen.setheading(90)  # set heading to straight up
    angle = (m / 60) * 360
    pen.rt(angle)
    pen.pendown()
    pen.fd(180)

    # Draw the second hand
    pen.penup()
    pen.goto(0,0)
    pen.color("gold")
    pen.setheading(90)  # set heading to straight up
    angle = (s / 60) * 360
    pen.rt(angle)
    pen.pendown()
    pen.fd(50)

while True:
    h = int(time.strftime("%I"))    # gives string formatted time as int in hours from 0 to 12
    m = int(time.strftime("%M"))    # gives string formatted time as int in minutes from 0 to 60
    s = int(time.strftime("%S"))    # gives string formatted time as int in seconds from 0 to 60

    draw_clock(h, m, s, pen)
    wn.update()

    time.sleep(1)

    pen.clear()


wn.mainloop()   #keeps window from closing