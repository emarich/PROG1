# book page 49 - ex 5.6
import turtle

angle = 60
t = turtle.Turtle()
t.speed(0)

def koch(x):
    if (x > 10):
        newX = x/3
        koch(newX)
        t.left(angle)
        koch(newX)
        t.right(2*angle)
        koch(newX)
        t.left(angle)
        koch(newX)
    else:
        t.forward(x)

def snowflake(n):
    for i in range(3):
        koch(n)
        t.right(2*angle)

snowflake(200)
t.done()