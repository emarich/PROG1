def printSquareNumbers(n):
    x = 0
    while x < n:
        square = x ** 2
        if (square < n):
            if (x == 0):
                print(square, end="")
            else:
                print("," + str(square), end="")
            x += 1
        else:
            break

printSquareNumbers(10)