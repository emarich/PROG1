import turtle
import math
import random

# global variables - angles
fullCircle = 360
halfCircle = 180
quarterCircle = 90
# global variables - colors
leafGreen = "#2D5A27"
roseRed = "#FF033E"
scorpionGrassBlue = "#76A6FA"
sunflowerYellow = "#F6A90F"

# move the turtle to a position [x,y]
def moveTurtle(t, x, y):
    t.penup()
    t.goto((x, y))
    t.pendown()

# draw a circle
def polygon(t, len, n, angle):
    polAngle = fullCircle/n
    drawAngle = int(n / (fullCircle / angle))
    for i in range(drawAngle):
        t.forward(len)
        t.left(polAngle)

# draw a part of circle
def arc(t, r, angle):
    circumference = 2 * math.pi * r
    len = circumference / r
    n = int((circumference / len))
    polygon(t, len, n, angle)

def drawPetal(t, r, angle):
    arc(t, r, angle)
    t.left(halfCircle - angle)
    arc(t, r, angle)

def drawStem(t, r, turtleAngle):
    t.setheading((halfCircle + quarterCircle) - turtleAngle/16)
    arc(t, 550 - r, turtleAngle / 8)

def drawBase(t, r, petalAngle, turtleAngle):
    t.color(leafGreen)
    drawStem(t, r, turtleAngle)
    # leafs
    randAngle = random.randint(0, int(quarterCircle/4))
    t.setheading(quarterCircle + randAngle + int(petalAngle / 2))
    drawPetal(t, 300 - r, quarterCircle - petalAngle)
    t.setheading(int(petalAngle / 2) - randAngle)
    drawPetal(t, 300 - r, quarterCircle - petalAngle)

'''
petalAngle = an angle that defines part of the circle, which will be representing half of the petal/leaf
turtleAngle = turtle's rotation angle after drawing a petal
'''
def drawFlower(t, r, numPetals, petalAngle, turtleAngle):
    for i in range(numPetals):
        drawPetal(t, r, petalAngle)
        t.left(turtleAngle)

    drawBase(t, r, petalAngle, turtleAngle)

def main():
    t = turtle.Turtle()
    t.speed(0)
    r = 100 # general radius of arc circles

    moveTurtle(t, -200, 100)
    numPetals = 7
    t.color(roseRed)
    drawFlower(t, r, numPetals, fullCircle/numPetals, halfCircle)

    moveTurtle(t, 0, 100)
    numPetals = 10
    t.color(scorpionGrassBlue)
    drawFlower(t, r/2, numPetals, fullCircle/numPetals*2, fullCircle)

    moveTurtle(t, 200, 100)
    numPetals = 20
    t.color(sunflowerYellow)
    drawFlower(t, r*2, numPetals, fullCircle/numPetals, halfCircle)

    t.hideturtle()
    turtle.done()

main()