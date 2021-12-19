def coutnZeroRows(t: list(list())) -> int:
    count = 0
    for n in t:
        rowSet = set(n)
        if (n[0] == 0 and len(rowSet) == 1):
            count += 1
    return count

t = [[2, 2, 3, 4]
    ,[4, 3, 2, 1]]
print(coutnZeroRows(t))