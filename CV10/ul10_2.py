# book 10.4 from section 10.15
def chop(l: list):
    l.remove(l[0])
    l.remove(l[-1])
    return None

l = [1, 2, 3, 4]
chop(l)
print(l)