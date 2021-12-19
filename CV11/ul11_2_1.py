def f(strList: list) -> str:
    for ret in strList:
        if (ret.find("a") != -1):
            return ret
    return None

sl = ["pes", "gekon"]
print(f(sl))