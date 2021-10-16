from c4_14 import inRange

def pohyb_jazdca(x1, y1, x2, y2):
    if (inRange(x1, y1, x2, y2) and
        ((abs(x2 - x1) == 2 and abs(y2 - y1) == 1) or
        (abs(x2 - x1) == 1 and abs(y2 - y1) == 2))):
        return True
    else:
        return False

print(pohyb_jazdca(5, 4, 4, 3))