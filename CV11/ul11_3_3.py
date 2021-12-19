def f(n: int) -> list:
    l = list()
    smallest = int(input("Enter the number: "))
    biggest = smallest
    while True:
        num = int(input("Enter the number: "))
        l.append(num)

        if (num < smallest):
            smallest = num
        if (num > biggest):
            biggest = num
        if (biggest - smallest > n):
            break
    return l

print(f(5))