def sumNumbers(n):
    sum = 0
    for i in range(n):
        num = int(input('Enter number: '))
        sum += num
    return sum

print(sumNumbers(3))