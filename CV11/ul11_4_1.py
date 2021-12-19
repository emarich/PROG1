def findNumInMatrix(t: list(list()), x: int) -> bool:
    for n in t:
        for k in n:
            if (k == x):
                return True
    return False

t = [[2, 2, 3, 4]
    ,[4, 3, 2, 1]]
num = 0
print(findNumInMatrix(t, num))