def sumInput(n):
    num = int(input("Enter number: "))
    return num + sumInput(n-1) if n > 1 else num

print(sumInput(3))