def colIBiggestSum(t: list(list())) -> int:
    biggest = {"colI": 0, "sum": None}
    for j in range(len(t[0])):
        sum = 0
        for i in range(len(t)):
            sum += t[i][j]
        if (biggest["sum"] == None or biggest["sum"] < sum):
            biggest["colI"] = j
            biggest["sum"] = sum
    return biggest["colI"]

t = [[2, 1, 2, 4]
    ,[2, 1, 2, 1]]
print(colIBiggestSum(t))