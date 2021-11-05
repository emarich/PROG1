def fun():
    jump = None
    maxJump = jump 

    while True:
        num = int(input("Enter number: "))
        if (num == 0):
            return maxJump

        prevNum = num

        num = int(input("Enter number: "))
        if (num == 0):
            return maxJump

        jump = num - prevNum
        if (maxJump == None or maxJump < jump):
            maxJump = jump

print(fun())