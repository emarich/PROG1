def f(ret1: str, ret2: str) -> bool:
    for ch in ret1:
        if (ret2.count(ch) > 0):
            return True
    return False

print(f("adam", "eva"))