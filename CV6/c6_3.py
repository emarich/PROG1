# returns x, when finds the largest number of 2^x < n
def fun(n):
    x = 0
    prod = 2

    if (n <= 1):
        return "wrong argument"

    while True:
        if (prod < n):
            prod *= 2
            x += 1
        else:
            return x

print(fun(10))