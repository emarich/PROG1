def getSecondMax(n):
    max = int(input('Enter number: '))
    secondMax = max

    for i in range(n-1):
        num = int(input('Enter number: '))
        if (num < max == secondMax):
            secondMax = num
        elif (secondMax < num < max):
            secondMax = num
        elif (num > max):
            secondMax = max
            max = num
            
    return secondMax

print(getSecondMax(4))