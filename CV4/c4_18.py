from c4_14 import inRange, pohyb_veze
from c4_17 import pohyb_strelca

def pohyb_damy(x1, y1, x2, y2):
    if (inRange(x1, y1, x2, y2) and
        (pohyb_veze(x1, y1, x2, y2) or pohyb_strelca(x1, y1, x2, y2))):
        return True
    else:
        return False

print(pohyb_damy(5, 5, 5, 2))