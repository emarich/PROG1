def Towers2(n):
    return 2 * Towers2(n-1) + 1 if n > 1 else 1

print(Towers2(3))