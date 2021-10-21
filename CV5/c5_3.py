def countEvenNumbers(n):
    num = int(input("Enter number: "))
    if (num % 2 == 0):
        return 1 + countEvenNumbers(n-1) if n > 1 else 1
    else:
        return 0 + countEvenNumbers(n-1) if n > 1 else 0

print(countEvenNumbers(3))