def f(strList: list) -> str:
    firstLetters = ""
    for ret in strList:
        firstLetters += ret[0]
    return firstLetters

sl = ["pes", "gekon", "ryba"]
print(f(sl))