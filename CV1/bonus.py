import turtle

line = 100
angle90 = 90
angle45 = 45

def sqrt(n: int):
    hyp = line

    for i in range(n-1):
        turtle.forward(hyp)
        turtle.left(angle90)
        turtle.forward(line)
        pos = turtle.pos()

        turtle.home()
        hyp = turtle.distance(pos)
        turtle.setheading(turtle.towards(pos))
        
    turtle.forward(hyp)
    turtle.left(angle90)
    turtle.forward(line)

    print("Square root of " + str(n) + " is " + str(hyp/100))

print("SQUARE ROOT")
print("Enter number:")
n = input()
sqrt(int(n))

turtle.done()