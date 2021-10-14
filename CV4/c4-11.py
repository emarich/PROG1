def delitelnost(a, d):
    return True if a % d == 0 else False

a = 12
for i in range(1, a + 1):
    if (delitelnost(a, i)):
        print(i, end=", " if i != a else "")