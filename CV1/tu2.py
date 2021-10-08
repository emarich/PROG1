import turtle

circle = 360
halfCircle = 180

def drawNPolygon(n):
    polAngle = circle/n
    for i in range(n):
        turtle.forward(100)
        turtle.left(polAngle)

print("Enter number:")
n = input()
drawNPolygon(int(n)) 

turtle.done()