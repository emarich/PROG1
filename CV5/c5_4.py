def getLargestNumber(n):
    num1 = int(input("Enter number: "))
    if (n > 1):
        num2 = getLargestNumber(n-1)
        return num1 if num1 >= num2 else num2
    else:
        return num1

print(getLargestNumber(3))