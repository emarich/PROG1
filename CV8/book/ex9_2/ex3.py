def avoids(word, forbiddenChars):
    for c in forbiddenChars:
        if (word.count(c) != 0):
            return False
    return True

file = open("C:\\Users\\emari\\Desktop\\projects\\PROG1\\CV8\\book\\ex9_2\\words.txt", "r")
count = 0

for word in file.read().split():
    if (avoids(word, "egl")):
        count += 1

print(count)