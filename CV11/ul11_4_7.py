def checkNotSameNumCol(t: list(list())) -> bool:
    same = False
    for j in range(len(t[0])):
        for i in range(len(t)-1):
            if (t[i][j] == t[i+1][j]):
                same = False
                break
            else:
                same = True
        if (same):
            return same
    return same

t = [[2, 1, 2, 4]
    ,[2, 1, 2, 1]]
print(checkNotSameNumCol(t))