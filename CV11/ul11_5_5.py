def someIntervalContainAllIntervals(t: list(list())) -> bool:
    newT = sorted(t)
    for i in range(1, len(t)):
        if (not (newT[0][0] < newT[i][0] and newT[0][1] > newT[i][1])):
            return False
    return True

t = [[1,2],[3,5],[0,6]]
print(someIntervalContainAllIntervals(t))