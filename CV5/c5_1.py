def sum(n):
    return n + sum(n-1) if n > 1 else n

print(sum(5))