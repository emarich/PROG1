import turtle

def square(t, len):
    for i in range(4):
        turtle.forward(len)
        turtle.right(90)
    turtle.done()

t = turtle.Turtle()
len = 100
square(t, len)