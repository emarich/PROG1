def findChar(ret: str, x: str) -> int:
    i = 0
    if (len(x) == 1):
        for i, ch in enumerate(ret):
            if (ch == x): return i
    else:
        return (f"\"{x}\" is not a character")
    return None

print(findChar("adam", "s"))