def sumEvenIndex(list):
    sum = 0
    for i in range(len(list)):
        if (i != 0 and i % 2 == 0):
            sum += list[i]
    return sum

t = [1,2,3,1,1]
print(sumEvenIndex(t))