def inRange(x1, y1, x2, y2):
    if ((x1 in range(1, 9)) and (y1 in range(1, 9)) 
        and (x2 in range(1, 9)) and (y2 in range(1, 9))):
        return True # if all of them are in between <1, 8>
    else:
        return False

def pohyb_veze(x1, y1, x2, y2):
    if (inRange(x1, y1, x2, y2) 
        and not (x1 == x2 and y1 == y2)
        and (x1 == x2 or y1 == y2)):
        return True
    else:
        return False

# print(pohyb_veze(1, 1, 1, 8))