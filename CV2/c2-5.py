def vypis(n):
    sum = 0
    for i in range(n):
        x = i+1
        sum += x*x
    return sum

print(vypis(3))