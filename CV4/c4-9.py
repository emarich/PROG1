def getMin(n):
    min = int(input('Enter number: '))
    for i in range(n-1):
        num = int(input('Enter number: '))
        if (min > num):
            min = num
    return min

print(getMin(4))