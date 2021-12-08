import random

fieldChar = "◦"
homeChar = "■"

class Pawn:
    def __init__(self, playerChar):
        self.pos = {} # actual pawn position
        self.prevPos = {} # previous pawn position
        self.char = playerChar # representative character on the gamefield
        self.onField = False # flag if pawn is on gamefield (not on home fields)
        self.isFinalHome = False # flag if pawn is in final home field

class Player:
    def __init__(self, playerNum, gamefield):
        self.pawns = []
        self.spawnPos = {} # position of starting field for the player
        self.prevSpawnPos = {} # position before starting field
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

        for i in range(int((gamefield.n - 3)/2)):
            self.pawns.append(Pawn(self.char))

    def putOnField(self, gamefield, pawnNum): # move pawn from starting home to gamefield
        self.pawns[pawnNum].pos = self.spawnPos.copy()
        self.pawns[pawnNum].prevPos = self.prevSpawnPos.copy()
        gamefield.field[self.spawnPos["x"]][self.spawnPos["y"]] = self.char
        self.pawns[pawnNum].onField = True

    def move(self, gamefield, pawnNum, nextPos, prevPos): # move pawn on field
        gamefield.field[self.pawns[pawnNum].pos["x"]][self.pawns[pawnNum].pos["y"]] = fieldChar
        self.pawns[pawnNum].prevPos = prevPos.copy()
        self.pawns[pawnNum].pos = nextPos.copy()
        gamefield.field[nextPos["x"]][nextPos["y"]] = self.char

    def moveToFinalHome(self, gamefield, pawnNum, nextPos): # move pawn to final home
        gamefield.field[self.pawns[pawnNum].pos["x"]][self.pawns[pawnNum].pos["y"]] = fieldChar
        self.pawns[pawnNum].pos = nextPos.copy()
        gamefield.field[nextPos["x"]][nextPos["y"]] = self.char
        self.pawns[pawnNum].onField = False
        self.pawns[pawnNum].onFinalHome = True

class Gamefield:
    def __init__(self, n, field) -> None:
        self.n = n
        self.field = field

# generate gamefield
def gensachovnicu(n):
    # generate 2d array
    gameField = [[" " for i in range(n+1)] for j in range(n+1)]
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
    gameField[halfN][halfN] = " " # center of gamefield is empty

    return Gamefield(n, gameField)

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
    prevPos = player1.prevSpawnPos.copy()
    player1.putOnField(gamefield, 0)
    tlacsachovnicu(gamefield)

    onField = True

    while onField:
        diceRoll = rollDice()
        print("~~~~~ Hrac " + player1.char + " hodil " + str(diceRoll) + " ~~~~~")

        while diceRoll != 0:
            pos, prevPos = moveToNextPos(gamefield, pos, prevPos)

            if (pos == player1.spawnPos): # if pawn is before final home
                if (diceRoll > len(player1.pawns)):
                    print("~~~~~ Ak sa chcete dostat do domceka, hodte menej")
                    pos = player1.pawns[0].pos.copy()
                    prevPos = player1.pawns[0].prevPos.copy()
                    break
                pos = moveToFinalHome(gamefield, prevPos, diceRoll)
                onField = False
                break

            diceRoll -= 1

        if (onField):
            player1.move(gamefield, 0, pos, prevPos)
        else:
            player1.moveToFinalHome(gamefield, 0, pos)
            print("⊱ Gratulujem, hrac A je v domceku ⊰")
        tlacsachovnicu(gamefield)

def checkPawnOnField(player): # if pawn is on field, return index of pawn, otherwise -1
    onFieldFlags = [pawn.onField for pawn in player.pawn]
    if (True not in onFieldFlags):
        return -1
    else:
        return onFieldFlags.index(True)

def getPawnIndexFromStartHome(player):
    for pawn in player.pawns:
        if (pawn.onField == False and pawn.isFinalHome == False):
            return player.pawns.index(pawn)

def otherPlayerNum(playerNum):
    return (playerNum % 2) + 1

def rollDiceAgain():
    sum = 0
    while True:
        newDiceRoll = rollDice()
        sum += newDiceRoll
        if (newDiceRoll != 6):
            return sum


def play2Players(gamefield):
    player = {1: Player(1, gamefield), 2: Player(2, gamefield)}
    pos = {1: player[1].spawnPos.copy(), 2: player[2].spawnPos.copy()}
    prevPos = {1: player[1].prevSpawnPos.copy(), 2: player[2].prevSpawnPos.copy()}
    tlacsachovnicu(gamefield)

    noWinner = True
    playerNum = 1
    
    while noWinner:
        diceRoll = rollDice()
        print("~~~~~ Hrac " + player[playerNum].char + " hodil " + str(diceRoll) + " ~~~~~")

        pawnIndex = checkPawnOnField(player[playerNum])
        if (pawnIndex == -1): # no pawn on field
            if (diceRoll == 6):
                player[playerNum].putOnField(gamefield, getPawnIndexFromStartHome(player[playerNum]))
            playerNum = otherPlayerNum(playerNum)
            continue
        else:
            if (diceRoll == 6):
                diceRoll = rollDiceAgain()
            print("~~~~~ Hrac " + player[playerNum].char + " hodil " + str(diceRoll) + " ~~~~~")
            while diceRoll != 0:
                pos[playerNum], prevPos[playerNum] = moveToNextPos(gamefield, pos[playerNum], prevPos[playerNum])

                if (pos[playerNum] == player[playerNum].spawnPos): # if pawn is before final home
                    if (diceRoll > len(player[playerNum].pawns)):
                        print("~~~~~ Ak sa chcete dostat do domceka, hodte menej")
                        pos[playerNum] = player[playerNum].pawns[0].pos.copy()
                        prevPos[playerNum] = player[playerNum].pawns[0].prevPos.copy()
                        break
                    pos[playerNum] = moveToFinalHome(gamefield, prevPos[playerNum], diceRoll)
                    break

                diceRoll -= 1

            if (onField):
                player1.move(gamefield, 0, pos, prevPos)
            else:
                player1.moveToFinalHome(gamefield, 0, pos)
                print("⊱ Gratulujem, hrac A je v domceku ⊰")
            tlacsachovnicu(gamefield)


# main function
def main():
    print("\nHrajte Clovece, nehnevaj sa!\n")

    n = 9
    # while True:
    #     n = int(input("Zadaj velkost sachovnice (cislo ma byt neparne a >= 5): "))
    #     if (n >= 5 and n % 2 != 0):
    #         break
    showPart = 0
    while True:
        showPart = int(input("Ktora cast projektu sa ma spustit?\nZadajte\t1 pre cast 1\n\t2 pre cast 2\n\t3 pre cast 3\n> "))
        if (1 <= showPart <= 3):
            break

    gamefield = gensachovnicu(n)

    if (showPart == 1):
        tlacsachovnicu(gamefield)
    elif (showPart == 2):
        play1Player(gamefield)
    elif (showPart == 3):
        play2Players(gamefield)

main()