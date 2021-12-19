def haveUniqChars(ret: str) -> bool:
    retSet = set(ret)
    return True if len(ret) == len(retSet) else False

def f(t: list) -> int:
    countUniq = 0
    for ret in t:
        if (haveUniqChars(ret)):
            countUniq += 1
    return countUniq

t = ["pes", "macka", "gekon", "ryba"]
print(f(t))