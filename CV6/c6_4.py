def getPositionOfLargestNumber():
    i = 1
    pos = i
    largestNum = None

    while True:
        inpt = int(input("Enter number: "))
        
        if (largestNum == None or inpt > largestNum):
            largestNum = inpt
            pos = i

        if (inpt == 0):
            return pos

        i += 1


print(getPositionOfLargestNumber())