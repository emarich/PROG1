def fun(n: int) -> list:
    t = list()
    while True:
        num = int(input("Enter a number: "))
        if (num in t):
            break
        else:
            t.append(num)
    return t

print(fun(5))