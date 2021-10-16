import turtle
from typing import Match

def square():
    for i in range(4):
        turtle.forward(100)
        turtle.left(90)
    turtle.done()

def triangle():
    for i in range(3):
        turtle.forward(100)
        turtle.left(120)
    turtle.done()

def menu():
    char = input("Enter \'s\' for square or \'t\' for triangle: ")
    match char:
        case 's':
            square()
        case 't':
            triangle()
        case _:
            print('Zadali ste neplatny vstup.')

menu()