import math

def in_bisect(words: list, w):
    lenght = len(words)
    halfLen = math.floor(lenght/2)

    if (lenght == 1):
        if (w != words[0]):
            return False
        else:
            return True
    
    if (w == words[halfLen]):
        return True
    elif (w > words[halfLen]):
        return in_bisect(words[halfLen:], w)
    elif (w < words[halfLen]):
        return in_bisect(words[:halfLen], w)

l = ["aha", "aligator", "barak", "byk", "cecilia", "gekon", "xylofon", "zase"]
#print(in_bisect(l, "mila"))