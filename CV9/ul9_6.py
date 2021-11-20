def countElementsOccuredOnce(list):
    s = set(list)
    sum = 0
    for n in s:
        if (list.count(n) == 1):
            sum += 1
    return sum

t = [1,1,2,3,3,4,5]
print(countElementsOccuredOnce(t))