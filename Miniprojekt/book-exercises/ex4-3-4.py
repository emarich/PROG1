import turtle
import math

circleAngle = 360

def polygon(t, len, n):
    polAngle = circleAngle/n
    for i in range(n):
        t.forward(len)
        t.left(polAngle)

def circle(t, r):
    circumference = 2 * math.pi * r
    len = circumference/r
    n = int(circumference/len)
    polygon(t, len, n)
    # check if radius is really r
    t.left(90)
    t.forward(r)
    turtle.done()

t = turtle.Turtle()
r = 100

circle(t, r)

