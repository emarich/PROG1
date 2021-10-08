import turtle

def square(t):
    for i in range(4):
        turtle.forward(100)
        turtle.right(90)
    turtle.done()

t = turtle.Turtle()
square(t)