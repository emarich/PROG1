# book page 61 - ex 6.5
def gcd(a, b):
    if (b == 0):
        return a
    else:
        r = a % b
        return gcd(b, r)

print(gcd(12,4))