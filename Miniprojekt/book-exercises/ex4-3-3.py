import turtle

circle = 360

def polygon(t, len, n):
    polAngle = circle/n
    for i in range(n):
        t.forward(len)
        t.left(polAngle)
    turtle.done()

t = turtle.Turtle()
len = 100
n = 5

polygon(t, len, int(n))