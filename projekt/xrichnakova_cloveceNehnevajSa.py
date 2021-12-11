import random

fieldChar = "*" # character representing normal field on gamefield
homeChar = "D" # character representing final home field on gamefield

class Pawn:
    def __init__(self):
        self.pos = {} # actual pawn position
        self.prevPos = {} # previous pawn position
        self.onField = False # flag if pawn is on gamefield (not on home fields)
        self.onFinalHome = False # flag if pawn is in final home field

class Player:
    def __init__(self, playerNum, gamefield):
        self.pawns = []
        self.spawnPos = {} # position of starting field for the player
        self.prevSpawnPos = {} # position before starting field
        self.char = " " # representative character on the gamefield
        halfN = int((gamefield.n+1)/2) # half of the gamefield

        if (playerNum == 1): # first player
            self.char = "A"
            self.spawnPos = {"x": 1, "y": halfN+1}
            self.prevSpawnPos = {"x": 1, "y": halfN}
        elif (playerNum == 2): # second player
            self.char = "B"
            self.spawnPos = {"x": gamefield.n, "y": halfN-1}
            self.prevSpawnPos = {"x": gamefield.n, "y": halfN}

        for i in range(getFinalHomeNum(gamefield.n)):
            self.pawns.append(Pawn())

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
    def __init__(self, n, field, finalHomesPos) -> None:
        self.n = n # size od field
        self.field = field # 2d array gamefield representation
        self.finalHomesPos = finalHomesPos # positions of final home fields

# generate gamefield
def gensachovnicu(n):
    # generate 2d array
    gameField = [[" " for i in range(n+1)] for j in range(n+1)]
    finalHomes = []
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
                finalHomes.append({"x": i, "y": k})
    gameField[halfN][halfN] = "X" # center of gamefield is empty

    return Gamefield(n, gameField, finalHomes)

# print gamefield
def tlacsachovnicu(gamefield):
    for row in gamefield.field:
        for elem in row:
            print(elem, end=" ") # print elements
        print()    
    print()

# returns number of homes for single player
def getFinalHomeNum(n):
    return int((n - 3)/2)

# random 6-side dice rolling (numbers from 1 to 6)
def rollDice():
    return random.randint(1, 6)

# when player rolls 6 on dice, rolls again then sum it up
def rollDiceAgain(player):
    sumRolls = 6
    while True:
        newDiceRoll = rollDice()
        sumRolls += newDiceRoll
        print(f"      Hrac {player.char} znovu hodil {newDiceRoll}")
        if (newDiceRoll != 6):
            return sumRolls

# if pawn is on field, return index of pawn, otherwise -1
def getPawnIndexOnField(player):
    for i, pawn in enumerate(player.pawns):
        if (pawn.onField):
            return i
    return -1


def getPawnIndexFromStartHome(player):
    for i, pawn in enumerate(player.pawns):
        if (pawn.onField == False and pawn.onFinalHome == False):
            return i


def changePlayer(playerNum, maxNumPlayers):
    return (playerNum % maxNumPlayers) + 1


def canGoNextPos(gamefield, nextPos, prevPos): # check if pawn can go in nextPos position
    if (1 <= nextPos["x"] <= gamefield.n and 1 <= nextPos["y"] <= gamefield.n and
        nextPos not in gamefield.finalHomesPos and         
        nextPos != prevPos and
        gamefield.field[nextPos["x"]][nextPos["y"]] in (fieldChar, "A", "B")):
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
    return pos, prevPos


def canGoFinalHome(gamefield, nextPos):
    if (1 <= nextPos["x"] <= gamefield.n and 1 <= nextPos["y"] <= gamefield.n and
        gamefield.field[nextPos["x"]][nextPos["y"]] == homeChar):
        return True
    return False


def moveToFinalHome(gamefield, pos, diceRoll):
    if (canGoFinalHome(gamefield, {"x": pos["x"]+diceRoll, "y": pos["y"]})):
        pos["x"] += diceRoll
        return True
    elif (canGoFinalHome(gamefield, {"x": pos["x"]-diceRoll, "y": pos["y"]})):
        pos["x"] -= diceRoll
        return True
    elif (canGoFinalHome(gamefield, {"x": pos["x"], "y": pos["y"]+diceRoll})):
        pos["y"] += diceRoll
        return True
    elif (canGoFinalHome(gamefield, {"x": pos["x"], "y": pos["y"]-diceRoll})):
        pos["y"] -= diceRoll
        return True
    return False


def isFinalHomeFull(player):
    for pawn in player.pawns:
        if (pawn.onFinalHome == False):
            return False
    return True


def play(maxPlayersNum, gamefield):
    player = {}
    pos = {}
    prevPos = {}
    noWinner = True
    countTurns = 0
    playerNum = 1

    for i in range(1, maxPlayersNum+1):
        player[i] = Player(i, gamefield)
    
    # if there is only 1 player, player will have only 1 pawn and it is put directly on field
    if (maxPlayersNum == 1):
        player[playerNum].pawns = [player[playerNum].pawns[0]]
        player[playerNum].putOnField(gamefield, 0)
        pos[playerNum] = player[playerNum].spawnPos.copy()
        prevPos[playerNum] = player[playerNum].prevSpawnPos.copy()

    tlacsachovnicu(gamefield)
    
    while noWinner:
        diceRoll = rollDice()
        print(f"~~~~~ Hrac {player[playerNum].char} hodil {diceRoll} ~~~~~")
        countTurns += 1

        pawnIndex = getPawnIndexOnField(player[playerNum])
        # no pawn on field
        if (pawnIndex == -1):
            if (diceRoll == 6): # if player rolled 6 on dice, put pawn on field
                player[playerNum].putOnField(gamefield, getPawnIndexFromStartHome(player[playerNum]))
                pos[playerNum] = player[playerNum].spawnPos.copy()
                prevPos[playerNum] = player[playerNum].prevSpawnPos.copy()
                tlacsachovnicu(gamefield)
            playerNum = changePlayer(playerNum, maxPlayersNum)
            continue
        # one pawn on field
        else:
            if (diceRoll == 6): # if player rolls 6 on dice, rolls again
                diceRoll = rollDiceAgain(player[playerNum])
                
            while diceRoll != 0:
                if (pos[playerNum] == player[playerNum].prevSpawnPos): # if pawn is before final home
                    if (diceRoll > getFinalHomeNum(gamefield.n)):
                        print("      Hod menej, aby si sa dostal do domceka")
                        pos[playerNum] = player[playerNum].pawns[pawnIndex].pos.copy()
                        prevPos[playerNum] = player[playerNum].pawns[pawnIndex].prevPos.copy()
                    elif (moveToFinalHome(gamefield, pos[playerNum], diceRoll)):
                        player[playerNum].moveToFinalHome(gamefield, pawnIndex, pos[playerNum])
                    break

                (pos[playerNum], prevPos[playerNum]) = moveToNextPos(gamefield, pos[playerNum], prevPos[playerNum]) # get next position of field for pawn

                diceRoll -= 1

            player[playerNum].move(gamefield, pawnIndex, pos[playerNum], prevPos[playerNum]) # move pawn to next field

            if (isFinalHomeFull(player[playerNum])):
                noWinner = False
            else:
                playerNum = changePlayer(playerNum, maxPlayersNum)
                
            tlacsachovnicu(gamefield)
            
    print(f"\n⋱⋰⋱⋰⋱ Gratulujem, hrac {player[playerNum].char} vyhral ⋰⋱⋰⋱⋰")
    print(f"      Trvalo to {countTurns} kol")


def main():
    print("\nHraj Clovece, nehnevaj sa!\n")

    # user enters size for gamefield
    n = 0
    while n % 2 == 0 or n < 5:
        try:
            n = int(input("Zadaj velkost sachovnice (cislo ma byt neparne a >= 5): "))
        except:
            print("Zadal si zly format.")

    # user enters number of players
    maxPlayersNum = None
    while maxPlayersNum not in (0, 1, 2):
        try:
            maxPlayersNum = int(input("Zadaj pocet hracov (1 alebo 2)(ak zadas 0, vypise sa iba sachovnica): "))
        except:
            print("\nZadal si zly format.")
    print()

    # generate gamefield
    gamefield = gensachovnicu(n)

    if (maxPlayersNum == 0):
        tlacsachovnicu(gamefield)
        return

    play(maxPlayersNum, gamefield)


main()