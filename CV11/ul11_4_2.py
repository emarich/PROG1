def countNumInMatrix(t: list(list()), x: int) -> int:
    count = 0
    for n in t:
        for k in n:
            if (k == x):
                count += 1
    return count

t = [[2, 2, 3, 4]
    ,[4, 3, 2, 1]]
num = 2
print(countNumInMatrix(t, num))