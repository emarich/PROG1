import turtle
import math

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
def moveTurtle(turtle, x, y):
    turtle.penup()
    turtle.goto((x, y))
    turtle.pendown()

def polygon(turtle, len, n, angle):
    polAngle = fullCircle/n
    drawAngle = int(n / (fullCircle / angle))
    for i in range(drawAngle):
        turtle.forward(len)
        turtle.left(polAngle)

# draw a part of a circle
def arc(turtle, radius, angle):
    circumference = 2 * math.pi * radius
    len = circumference / radius
    n = int((circumference / len))
    polygon(turtle, len, n, angle)

def drawPetal(turtle, radius, angle):
    arc(turtle, radius, angle)
    turtle.left(halfCircle - angle)
    arc(turtle, radius, angle)

'''
turtle = an instance of the turtle
radius = radius of circle, which will be representing half of the petal
numPetals = number of petals
petalAngle = an angle that defines part of the circle, which will be representing half of the petal
turtleAngle = turtle's rotation angle after drawing a petal
color = color of the turtle pen, default colo is black
'''
def drawFlower(turtle, radius, numPetals, petalAngle, turtleAngle, color="black"):
    turtle.color(color)
    for i in range(numPetals):
        drawPetal(turtle, radius, petalAngle)
        turtle.left(turtleAngle)

def drawStem(turtle, radius, stemAngle, color=leafGreen):
    turtle.color(color)
    turtle.setheading((halfCircle + quarterCircle) - stemAngle/2)
    arc(turtle, radius, stemAngle)

'''
turtle = an instance of the turtle
radius = radius of circle, which will be representing half of the leaf
turtleAngle = turtle's rotation angle after drawing a leaf
leafAngle = an angle that defines part of the circle, which will be representing half of the leaf
'''
def drawLeafs(turtle, radius, turtleAngle, leafAngle, color=leafGreen):
    turtle.color(color)
    turtle.setheading(turtleAngle)
    drawPetal(turtle, radius, leafAngle)
    turtle.setheading(halfCircle - turtleAngle - (leafAngle*0.8))
    drawPetal(turtle, radius, leafAngle)

def main():
    t = turtle.Turtle()
    t.speed(0)

    # flower 1
    moveTurtle(t, -200, 100)
    numPetals = 7
    drawFlower(t, 100, numPetals, fullCircle/numPetals, halfCircle, roseRed)
    drawStem(t, 130, 90)
    drawLeafs(t, 130, 10, 30)

    # flower 2
    moveTurtle(t, 0, 100)
    numPetals = 10
    drawFlower(t, 50, numPetals, fullCircle/numPetals*2, fullCircle, scorpionGrassBlue)
    drawStem(t, 450, 40)
    drawLeafs(t, 500, 65, 15)

    # flower 3
    moveTurtle(t, 200, 100)
    numPetals = 20
    drawFlower(t, 200, numPetals, fullCircle/numPetals, halfCircle, sunflowerYellow)
    drawStem(t, 250, 40)
    drawLeafs(t, 100, 20, 80)

    t.hideturtle()
    turtle.done()

main()