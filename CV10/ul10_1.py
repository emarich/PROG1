def getMostTypedNumber():
    d = {}
    while True:
        inp = input("Enter a number: ")
        if (inp == "0"): return max(d, key=d.get)
        if inp in d:
            d[inp] += 1
        else:
            d[inp] = 1
    
    
print(getMostTypedNumber())