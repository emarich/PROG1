# resturns count of occurences, when entered number is larger than previous
def fun():
    sum = 0
    prevNum = int(input("Enter number: "))

    while True:
        if (prevNum == 0):
            return sum

        num = int(input("Enter number: "))

        if (num > prevNum):
            sum += 1
            
        prevNum = num

print(fun())   