def isSwapedAge(age1, age2):
    age1 = str(age1).zfill(2)
    age2 = str(age2).zfill(2)
    return (age1[0] == age2[1] and age1[1] == age2[0])

def checkAge():
    momAge = 36
    childAge = 0
    countSwapedAges = 0

    while momAge < 99:
        if (isSwapedAge(momAge, childAge)):
            countSwapedAges += 1
        if (countSwapedAges == 6):
            print("Child's current age: " + str(childAge))
            break
        momAge += 1
        childAge += 1

checkAge()