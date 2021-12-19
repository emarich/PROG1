def getChars(ret: str) -> list:
    chars = set()
    for ch in ret:
        chars.add(ch)
    return list(chars)

print(getChars("adam"))