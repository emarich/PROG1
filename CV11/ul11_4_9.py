def colIBiggestSum(t: list(list())) -> int:
    sums = []
    for j in range(len(t[0])):
        sum = 0
        for i in range(len(t)):
            sum += t[i][j]
        sums.append(sum)

    return True if len(set(sums)) < len(sums) else False

t = [[2, 1, 2, 4]
    ,[2, 1, 2, 1]]
print(colIBiggestSum(t))