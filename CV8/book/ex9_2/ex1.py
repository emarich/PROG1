file = open("C:\\Users\\emari\\Desktop\\projects\\PROG1\\CV8\\book\\ex9_2\\words.txt", "r")
for word in file.read().split():
    if (len(word) > 20):
        print(word)