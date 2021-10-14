import turtle
import math

fullCircle = 360
halfCircle = 180

def moveTurtleX(t, x):
    t.penup()
    t.goto((x, 0))
    t.pendown()

def polygon(t, len, n, angle):
    polAngle = fullCircle/n
    drawAngle = int(n / (fullCircle/angle))
    for i in range(drawAngle):
        t.forward(len)
        t.left(polAngle)

def arc(t, r, angle):
    circumference = 2 * math.pi * r
    len = circumference/r
    n = int((circumference/len))
    polygon(t, len, n, angle)

def drawPetal(t, r, angle):
    arc(t, r, angle)
    t.left(halfCircle-angle)
    arc(t, r, angle)

def drawFlower(numPetals, r, petalAngle, turtleAngle):
    for i in range(numPetals):
        drawPetal(t, r, petalAngle)
        t.left(turtleAngle)

t = turtle.Turtle() # turtle
t.speed(100)
r = 100 # radius of circles in petals

moveTurtleX(t, -150)
numPetals = 7
drawFlower(numPetals, r, fullCircle/numPetals, halfCircle)

moveTurtleX(t, 0)
numPetals = 10
drawFlower(numPetals, r/2, fullCircle/numPetals*2, fullCircle)

moveTurtleX(t, 150)
numPetals = 20
drawFlower(numPetals, r*2, fullCircle/numPetals, halfCircle)

t.hideturtle()
turtle.done()