import time

def useAppend():
    words = []
    file = open("C:\\Users\\emari\\Desktop\\projects\\PROG1\\CV10\\book\\words.txt")
    for line in file:
        w = line.strip()
        words.append(w)
    return words

def useIdiom():
    words = []
    file = open("C:\\Users\\emari\\Desktop\\projects\\PROG1\\CV10\\book\\words.txt")
    for line in file:
        w = line.strip()
        words += [w]
    return words

startT = time.time()
words = useAppend()
durationT = time.time() - startT
print("Used append, duration time: " + str(durationT))

startT = time.time()
words = useIdiom()
durationT = time.time() - startT
print("Used idiom, duration time: " + str(durationT))

