def countLocalMax():
    localMaxCount = 0
    prevNum = None
    num = None

    while True:
        nextNum = int(input("Enter number: "))

        if (nextNum == 0):
            return localMaxCount
        
        if (prevNum == None):
            prevNum = nextNum
            continue
        elif (num == None):
            num = nextNum
            continue
        else:
            if (prevNum < num > nextNum):
                localMaxCount += 1
            prevNum = num
            num = nextNum

print(countLocalMax())