"""
e = even = True     e + e = e
o = odd = False     e + o = o
                    o + o = e
                    o + e = o      
                    (XNOR)
"""
def isSumInputEven(n):
    num = int(input("Enter number: "))
    if (num % 2 == 0):
        return not(True ^ isSumInputEven(n-1)) if n > 1 else True
    else:
        return not(False ^ isSumInputEven(n-1)) if n > 1 else False

print(isSumInputEven(3))