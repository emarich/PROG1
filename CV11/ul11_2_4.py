def haveUniqChars(ret: str) -> bool:
    retSet = set(ret)
    return True if len(ret) == len(retSet) else False

def f(t: list) -> str:
    biggestUniq = {"bStr": "", "bSet": set()}
    for ret in t:
        if (haveUniqChars(ret)):
            if (len(biggestUniq["bSet"]) < len(set(ret))):
                biggestUniq["bStr"] = ret
                biggestUniq["bSet"] = set(ret)
    return biggestUniq["bStr"]

t = ["pes", "macka", "gekon", "ryba"]
print(f(t))