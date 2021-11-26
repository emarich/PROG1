def has_duplicates(l: list):
    s = set(l)
    if (len(l) == len(s)):
        return False
    else:
        return True

l = [1,2,3,4,3]
#print(has_duplicates(l))