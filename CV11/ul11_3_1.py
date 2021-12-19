def fun(n: int) -> list:
    t = list()
    sum = 0
    while True:
        num = int(input("Enter a number: "))
        t.append(num)
        sum += num
        if (sum > n):
            break
    return t

print(fun(5))