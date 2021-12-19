def biggestNumInMatrix(t: list(list())) -> int:
    biggest = t[0][0]
    for n in t:
        for k in n:
            if (k > biggest):
                biggest = k
    return biggest

t = [[2, 2, 3, 4]
    ,[4, 3, 2, 1]]
print(biggestNumInMatrix(t))