import random
from ex10_15_7 import has_duplicates

birthdays=[]
count = 0
for i in range(10):
    for j in range(23):
        randDay = 0
        randMonth = random.randint(1, 12)
        if (randMonth == 2):
            randDay = random.randint(1,28)
        elif (randMonth < 8):
            if (randMonth % 2 == 1):
                randDay = random.randint(1, 31)
            else:
                randDay = random.randint(1, 30)
        else:
            if (randMonth % 2 == 0):
                randDay = random.randint(1, 31)
            else:
                randDay = random.randint(1, 30)
        birthdays.append(str(randDay) + "." + str(randMonth))

    if (has_duplicates(birthdays)):
        count += 1
    birthdays = []

print("Probability: " + str(100 * (count/10)))