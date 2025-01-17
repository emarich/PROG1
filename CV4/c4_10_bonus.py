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

while(True):
    try:
        n = input("How many numbers do you want to enter?\n(type \'e\' for end)\n> ")
        if (n == 'e'):
            break 
        print(str(getSecondMax(int(n))) + "\n")
    except ValueError as e:
        print("\nInvalid input.\n")
    except KeyboardInterrupt as e:
        break