def getMatchInInterval(t: list(list()), x: int) -> list(list()):
    matchedIntervals = []
    for interval in t:
        if (x > interval[0] and x < interval[1]):
            matchedIntervals.append(interval)
    return matchedIntervals

t = [[1,2],[3,6],[4,7]]
print(getMatchInInterval(t, 5))