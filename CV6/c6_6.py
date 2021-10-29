def countLargestNumber():
    sum = 1
    num = int(input("Enter number: "))
    largest = num

    while num != 0:
        num = int(input("Enter number: "))

        if (num == largest):
            sum += 1
        if (num > largest):
            sum = 1
            largest = num
    
    return sum

print(countLargestNumber())