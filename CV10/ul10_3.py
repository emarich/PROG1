def isMatrix(a):
    if (type(a) == list):
        rowLen = len(a[0])
        for i in range(1, len(a)):
            if (rowLen != len(a[i])):
                return False
        return True
    return False

def printMatrix(a):
    for i in range(len(a)):
        print(*a[i])

def sumMatrixes(a, b):
    if (not isMatrix(a)):
        print(a)
        print("1. argument nie je matica")
        return
    elif (not isMatrix(b)):
        print(b)
        print("2. argument nie je matica")
        return
    if (len(a) != len(b) or
        len(a[0]) != len(b[0])):
        print("Zadane matice nie je mozne scitat")
        return

    sumMatrix = []

    for i in range(len(a)):
        sumMatrix.append([])
        for j in range(len(a[0])):
            sumMatrix[i].append(a[i][j] + b[i][j])

    printMatrix(sumMatrix)

a = [[1, 2]
    ,[3, 4]]
b = [[2, 2]
    ,[1, 1]]
#sumMatrixes(a, b)