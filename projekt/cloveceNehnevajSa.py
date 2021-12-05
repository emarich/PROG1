import random

fieldChar = "◦"
homeChar = "■"

class Pawn:
    def __init__(self, playerChar):
        self.pos = {} # actual pawn position
        self.prevPos = {} # previous pawn position
        self.char = playerChar # representative character on the gamefield
        self.isStartHome = True # flag if pawn is in starting home field
        self.isField = False # flag if pawn is on gamefield (not on home fields)
        self.isFinalHome = False # flag if pawn is in final home field

    def putOnField(self, gamefield, pos, prevPos): # move pawn from starting home to gamefield
        self.pos = pos.copy()
        self.prevPos = prevPos.copy()
        gamefield.field[pos["x"]][pos["y"]] = self.char
        self.isStartHome = False
        self.isField = True

    def move(self, gamefield, nextPos, prevPos): # move pawn on field
        gamefield.field[self.pos["x"]][self.pos["y"]] = fieldChar
        self.prevPos = prevPos.copy()
        self.pos = nextPos.copy()
        gamefield.field[nextPos["x"]][nextPos["y"]] = self.char

    def moveToFinalHome(self, gamefield, nextPos): # move pawn to final home
        gamefield.field[self.pos["x"]][self.pos["y"]] = fieldChar
        self.pos = nextPos.copy()
        gamefield.field[nextPos["x"]][nextPos["y"]] = self.char
        self.isField = False
        self.isFinalHome = True

class Player:
    def __init__(self, playerNum, gamefield):
        self.pawns = []
        self.spawnPos = {} # position of starting field for the player
        self.prevSpawnPos = {}
        self.char = "" # representative character on the gamefield
        halfN = int((gamefield.n+1)/2) # half of the gamefield

        if (playerNum == 1):
            self.char = "A"
            self.spawnPos = {"x": 1, "y": halfN+1}
            self.prevSpawnPos = {"x": 1, "y": halfN}
        elif (playerNum == 2):
            self.char = "B"
            self.spawnPos = {"x": gamefield.n, "y": halfN-1}
            self.prevSpawnPos = {"x": gamefield.n, "y": halfN}

        for i in range(gamefield.homePerPlayerNum):
            self.pawns.append(Pawn(self.char))

class Gamefield:
    def __init__(self, n, field, homePositions) -> None:
        self.n = n
        self.field = field        
        self.homePositions = homePositions
        self.homePerPlayerNum = int(len(homePositions)/4)

# generate gamefield
def gensachovnicu(n):
    # generate 2d array
    gameField = [[" " for i in range(n+1)] for j in range(n+1)]
    homePositions = [] # positions of final home fields
    halfN = int((n+1)/2)

    for i in range(1, n+1):
        # add right and top numbers
        gameField[0][i] = (i-1)%10
        gameField[i][0] = (i-1)%10
        # add houses and fields for players 
        for k in range(1, n+1):
            if (((i == 1 or i == n) and (halfN-1 <= k <= halfN+1)) or # horizontal top or bottom
                ((halfN-1 <= i <= halfN+1) and (k == 1 or k == n)) or # vertical right or left
                ((1 < i < halfN or halfN < i < n) and (k == halfN-1 or k == halfN+1)) or # vertical midle
                ((i == halfN-1 or i ==halfN+1) and (1 < k < halfN or halfN < k < n))): # horizontal middle
                gameField[i][k] = fieldChar
            elif ((1 < i < n and k == halfN) or
                   (i == halfN and 1 < k < n)):
                gameField[i][k] = homeChar
                homePositions.append({"x": i, "y": k})
    gameField[halfN][halfN] = " " # center of gamefield is empty

    return Gamefield(n, gameField, homePositions)

# print gamefield
def tlacsachovnicu(gamefield):
    for row in gamefield.field:
        for elem in row:
            print(elem, end=" ") # print elements
        print()    
    print()

# random 6-side dice rolling (numbers from 1 to 6)
def rollDice():
    return random.randint(1, 6)

def canGoNextPos(gamefield, nextPos, prevPos): # check if pawn can go in nextPos position
    if (nextPos["x"] <= gamefield.n and nextPos["y"] <= gamefield.n and 
        nextPos != prevPos and
        gamefield.field[nextPos["x"]][nextPos["y"]] == fieldChar):
        return True
    return False

def canGoFinalHome(gamefield, nextPos):
    if (nextPos["x"] <= gamefield.n and nextPos["y"] <= gamefield.n and
        gamefield.field[nextPos["x"]][nextPos["y"]] == homeChar):
        return True
    return False

def moveToNextPos(gamefield, pos, prevPos):
    if (canGoNextPos(gamefield, {"x": pos["x"]+1, "y": pos["y"]}, prevPos)):
        prevPos = pos.copy()
        pos["x"] += 1
    elif (canGoNextPos(gamefield, {"x": pos["x"]-1, "y": pos["y"]}, prevPos)):
        prevPos = pos.copy()
        pos["x"] -= 1
    elif (canGoNextPos(gamefield, {"x": pos["x"], "y": pos["y"]+1}, prevPos)):
        prevPos = pos.copy()
        pos["y"] += 1
    elif (canGoNextPos(gamefield, {"x": pos["x"], "y": pos["y"]-1}, prevPos)):
        prevPos = pos.copy()
        pos["y"] -= 1
    return (pos, prevPos)

def moveToFinalHome(gamefield, pos, diceRoll):
    if (canGoFinalHome(gamefield, {"x": pos["x"]+1, "y": pos["y"]})):
        pos["x"] += diceRoll
    elif (canGoFinalHome(gamefield, {"x": pos["x"]-1, "y": pos["y"]})):
        pos["x"] -= diceRoll
    elif (canGoFinalHome(gamefield, {"x": pos["x"], "y": pos["y"]+1})):
        pos["y"] += diceRoll
    elif (canGoFinalHome(gamefield, {"x": pos["x"], "y": pos["y"]-1})):
        pos["y"] -= diceRoll
    return pos

def play1Player(gamefield):
    player1 = Player(1, gamefield)

    # put pawn on field
    pos = player1.spawnPos.copy()
    prevPos = {}
    player1.pawns[0].putOnField(gamefield, pos, prevPos)
    tlacsachovnicu(gamefield)
    onField = True

    while onField:
        diceRoll = rollDice()
        print("~~~~~ Hrac " + player1.char + " hodil " + str(diceRoll) + " ~~~~~")

        while diceRoll != 0:
            pos, prevPos = moveToNextPos(gamefield, pos, prevPos)

            if (pos == player1.spawnPos):
                if (diceRoll > gamefield.homePerPlayerNum):
                    print("~~~~~ Ak sa chces dostat do domceka, hod menej")
                    pos = player1.pawns[0].pos.copy()
                    prevPos = player1.pawns[0].prevPos.copy()
                    break
                pos = moveToFinalHome(gamefield, prevPos, diceRoll)
                onField = False
                break

            diceRoll -= 1

        if (onField):
            player1.pawns[0].move(gamefield, pos, prevPos)
        else:
            player1.pawns[0].moveToFinalHome(gamefield, pos)
        tlacsachovnicu(gamefield)


# main function
def main():
    print("Hraj Clovece, nehnevaj sa!\n")

    n = 9
    # while True:
    #     n = int(input("Zadaj velkost sachovnice (cislo ma byt neparne a >= 5): "))
    #     if (n >= 5 and n % 2 != 0):
    #         break

    # 1. part
    gamefield = gensachovnicu(n)
    #tlacsachovnicu(gamefield)
    # 2. part
    play1Player(gamefield)

main()