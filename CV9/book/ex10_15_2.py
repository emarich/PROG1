def cumsum(numbers):
    newList = []
    for i in range(len(numbers)):
        if (i != 0):
            newList.append(numbers[i] + newList[i-1])
        else:
            newList.append(numbers[i])
    return newList

t = [1, 2, 3]
print(cumsum(t))