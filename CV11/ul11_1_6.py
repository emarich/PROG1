def getAllUniqueChars(ret: str) -> list:
    uniqChars = set()
    for ch in ret:
        if (ret.count(ch) == 1):
            uniqChars.add(ch)
    return list(uniqChars)

print(getAllUniqueChars("adam"))