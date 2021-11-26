def startOfInterval(elem):
    return elem[0]

def checkIntervalsIntersections(t: list):
    if (len(t) == 1): return True

    commonInterval = t[0]

    for i in range(1, len(t)):
        if (range(max(commonInterval[0], t[i][0]), min(commonInterval[1], t[i][1]))):
            commonInterval = [max(commonInterval[0], t[i][0]), min(commonInterval[1], t[i][1])]
        else:
            return False
    print("Spolocny prienik intervalov je " + str(commonInterval))
    return True


#t = [[1,6], [0,10], [2, 7], [5, 13]]
t = [[1,6], [0,10], [2, 5], [9, 13]]
#t = [[19, 20], [18, 21]]
print(checkIntervalsIntersections(t))