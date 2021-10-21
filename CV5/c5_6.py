def  test_prvociselnosti(a):
    for i in range(2, a):
        if (delitelnost(a, i)):
            return False
    return True

def delitelnost(a, d):
    return True if a % d == 0 else False

def sumPrimeNumbers(n):
    if (test_prvociselnosti(n)):
        return n + sumPrimeNumbers(n-1) if n > 2 else n
    else:
        return sumPrimeNumbers(n-1)

print(sumPrimeNumbers(3))