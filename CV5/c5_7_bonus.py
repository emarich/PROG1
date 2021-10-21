def Towers2(n):
    return Towers2(n-1) + Towers2(1) + Towers2(n-1) if n > 1 else 1

print(Towers2(3))