def countNumbersDivadableBy5(n):
    sum = 0
    for i in range(n):
        num = input('Enter number: ')
        if (int(num) % 5 == 0):
            sum += 1
    return sum

print(countNumbersDivadableBy5(3))