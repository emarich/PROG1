def fun(k):
    sum = 0
    num = input("Enter number: ")
    sameNum = num

    while True:
        if (num == sameNum):
            sum += 1
            if (sum == k):
                return num
        else:
            sameNum = num
            sum = 1

        num = input("Enter number: ")

print(fun(2))