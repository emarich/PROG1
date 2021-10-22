# book page 61 - ex 6.4
def is_power(a, b):
    if (a < b or b == 0):
        return False
    if (b == 1 or a == b):
        return True
    else:
        return ((a % b == 0 and is_power(a/b, b)))

print(is_power(30,2))