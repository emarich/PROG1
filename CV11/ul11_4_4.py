def biggestNumInMatrix(t: list(list())) -> list:
    biggest = {"num": t[0][0], "pos": [0, 0]}
    for i,n in enumerate(t):
        for j,k in enumerate(n):
            if (k > biggest["num"]):
                biggest["num"] = k
                biggest["pos"] = [i, j]
    return biggest["pos"]

t = [[2, 2, 3, 4]
    ,[4, 3, 2, 1]]
print(biggestNumInMatrix(t))