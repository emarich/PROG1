def countChar(ret: str, x: str) -> int:
    count = 0
    if (len(x) == 1):
        for ch in ret:
            if (ch == x): count += 1
    else:
        return (f"\"{x}\" is not a character")
    return count

print(countChar("adam", "a"))