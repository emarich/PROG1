def sumPositiveNumbers():
    sum = 0
    n = 1

    while True:
        n = int(input("Enter number: "))
        if (n <= 0):
            break
        sum += n
    
    return sum

print(sumPositiveNumbers())