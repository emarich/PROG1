def hasConsecutiveLetters(word):
    count = 0
    i = 0
    while i < len(word) - 1:
        if (word[i] == word[i+1]):
            count += 1
            i += 2
        else:
            i += 1
    if (count == 3):
        return True
    else:
        return False

def findTripleConsecutiveLetters():
    word = "Mississippi"
    if (hasConsecutiveLetters(word)):
        print("\"" + word + "\" has 3 consecutive double letters.")
    else:
        print("\"" + word + "\" has not 3 consecutive double letters.")

findTripleConsecutiveLetters()