def countLargestSequence():
    sum = 1
    largestSum = sum
    num = int(input("Enter number: "))
    sameNum = num

    while num != 0:
        num = int(input("Enter number: "))
        
        if (num == sameNum):
            sum += 1
        else:
            if (largestSum < sum):
                largestSum = sum
            sum = 1
            sameNum = num
    
    return largestSum

print(countLargestSequence())