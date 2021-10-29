def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def getFibonacciIndex(x):
    fibIndex = -1
    fib = 0

    while fib <= x:
        fibIndex += 1
        fib = fibonacci(fibIndex)
        if (fib == x):
            return fibIndex

    return -1 

print(getFibonacciIndex(8))