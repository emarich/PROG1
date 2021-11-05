def countSameNumSequnce():
    counter = 0
    isSeq = False
    prevNum = None

    while True:
        num = int(input("Enter number: "))

        if (num == 0):
            return counter

        if (prevNum == None):
            prevNum = num
            continue

        if (prevNum == num and not isSeq):
            counter += 1
            isSeq = True
        if (prevNum != num):
            isSeq = False

        prevNum = num

print(countSameNumSequnce())