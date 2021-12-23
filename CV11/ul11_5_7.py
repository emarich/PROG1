def have2IntervalsIntersection(t: list(list())) -> bool:
    for i in range(len(t)):
        for j in range(1, len(t)):
            if (max(t[i][0], t[j][0]) < min(t[i][1], t[j][1])):
                return True
    return False

t = [[1,2],[0,5],[6,7]]
print(have2IntervalsIntersection(t))