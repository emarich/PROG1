from c4_14 import inRange

def pohyb_strelca(x1, y1, x2, y2):
    if (inRange(x1, y1, x2, y2) and
        abs(x2 - x1) == abs(y2 - y1)):
        return True
    else:
        return False

# print(pohyb_strelca(5, 3, 1, 7))