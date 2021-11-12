def uses_only(word, usedChars):
    wordLen = len(word)
    sumUsedChars = 0
    for c in usedChars:
        wordCount = word.count(c)
        if (wordCount == 0):
            return False
        sumUsedChars += wordCount
    if (sumUsedChars == wordLen):
        return True
    else:
        False

file = open("C:\\Users\\emari\\Desktop\\projects\\PROG1\\CV8\\book\\ex9_2\\words.txt", "r")
count = 0
usedChars = "anb"
for word in file.read().split():
    if (uses_only(word, usedChars)):
        print("Word \"" + word + "\" is only using this chars \"" + usedChars + "\"")