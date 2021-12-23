def intervalsWithNoIntersections(t: list(list())) -> list(list()):
    intervals = []
    for i in range(len(t)):
        isInInterval = False
        for j in range(i+1, len(t)):
            if (max(t[i][0], t[j][0]) < min(t[i][1], t[j][1])):
                isInInterval = True
                break
        if (not isInInterval):
            intervals.append(t[i])
    return intervals

t = [[1,2],[0,5],[6,7]]
print(intervalsWithNoIntersections(t))