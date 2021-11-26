from ul10_3 import isMatrix, printMatrix

def multiplyMatrixes(a, b):
    if (not isMatrix(a)):
        print(a)
        print("1. argument nie je matica")
        return
    elif (not isMatrix(b)):
        print(b)
        print("2. argument nie je matica")
        return
    if (len(a[0]) != len(b)):
        print("Zadane matice nie je mozne scitat")
        return

    multMatrix = [[]]
    for i in range(len(a)):
        multMatrix.append([])
        for k in range(len(b[i])):
            multiplyRowCol = 0
            for j in range(len(b)):
                multiplyRowCol += a[i][j] * b[j][k]
            multMatrix[i].append(multiplyRowCol)

    printMatrix(multMatrix)

a = [[-1, 1, 1]
    ,[0, 2, 1]
    ,[0, 0, 3]]
b = [[1, -1]
    ,[0, 2]
    ,[1, 0]]
multiplyMatrixes(a, b)