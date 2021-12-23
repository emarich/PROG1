def countMatchInInterval(t: list(list()), x: int) -> int:
    count = 0
    for interval in t:
        if (x > interval[0] and x < interval[1]):
            count += 1
    return count

t = [[1,2],[3,6],[4,7]]
print(countMatchInInterval(t, 6))