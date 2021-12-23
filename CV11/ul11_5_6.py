def someIntervalIntersectingAll(t: list(list())) -> bool:
    newT = sorted(t, key=lambda i: i[1] - i[0])
    for i in range(1, len(t)):
        if not (newT[0][0] > newT[i][0] and newT[0][1] < newT[i][1]):
            return False
    return True

t = [[-1,5],[1,2],[0,6]]
print(someIntervalIntersectingAll(t))