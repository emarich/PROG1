def f(n: int) -> list:
    l = list()
    while True:
        num = int(input("Enter the number: "))
        l.append(num)

        if (len(set(l)) == n):
            break
    return l

print(f(3))