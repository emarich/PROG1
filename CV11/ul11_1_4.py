def f(ret1: str, ret2: str) -> bool:
    count = 0
    for ch in ret1:
        if (ret2.count(ch) > 0):
            count += 1
    
    return True if count == len(ret1) else False

print(f("adam", "dadadam"))