def getMatchInInterval(t: list(list()), x: int) -> list:
    for interval in t:
        if (x > interval[0] and x < interval[1]):
            return interval
    return None

t = [[1,2],[3,6],[4,7]]
print(getMatchInInterval(t, 5))