from c4_14 import inRange

def pohyb_krala(x1, y1, x2, y2):
    if (inRange(x1, y1, x2, y2) and not (x1 == x2 and y1 == y2) and
        (x2 in range(x1-1, x1+2) and y2 in range(y1-1, y1+2))):
        return True
    else:
        return False

print(pohyb_krala(8, 8, 8, 7))