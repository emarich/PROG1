def has_no_e(word):
    if (word.count("e") == 0):
        return True
    else:
        return False

file = open("C:\\Users\\emari\\Desktop\\projects\\PROG1\\CV8\\book\\ex9_2\\words.txt", "r")
for word in file.read().split():
    if (has_no_e(word)):
        print(word)