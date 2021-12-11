import turtle
import math

circleAngle = 360

def polygon(t, len, n, angle):
    polAngle = circleAngle/n
    drawAngle = int(n / (circleAngle/angle))
    for i in range(drawAngle):
        t.forward(len)
        t.left(polAngle)

def arc(t, r, angle):
    circumference = 2 * math.pi * r
    len = circumference/r
    n = int((circumference/len))
    polygon(t, len, n, angle)
    # check if radius is really r
    t.left(90)
    t.forward(r)
    turtle.done()

t = turtle.Turtle()
r = 100
angle = 90

arc(t, r, angle)