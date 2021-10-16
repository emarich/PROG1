from c4_14 import inRange

def rovnaka_farba(x1, y1, x2, y2):
    if (not inRange(x1, y1, x2, y2)):
        return False
    elif ((x1 % 2 and y1 % 2) or (not x1 % 2 and not y1 % 2)):
        if ((x2 % 2 and y2 % 2) or (not x2 % 2 and not y2 % 2)):
            # same color black
            return True
        else:
            return False
    elif ((x1 % 2 and not y1 % 2) or (not x1 % 2 and y1 % 2)):
        if ((x2 % 2 and not y2 % 2) or (not x2 % 2 and y2 % 2)):
            # same color white
            return True
        else:
            return False

print(rovnaka_farba(1, 1, 8, 8))