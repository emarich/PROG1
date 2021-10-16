def  test_prvociselnosti(a):
    for i in range(2, a):
        if (delitelnost(a, i)):
            return False
    return True

def delitelnost(a, d):
    return True if a % d == 0 else False

def main():
    while(True):
        try:
            a = int(input("Enter number (or random char for end): "))
            if (a < 2 or a > 50):
                print("> " + str(a) + " je mimo rozsahu <2, 50>")
            else:
                if (test_prvociselnosti(a)):
                    print("> " + str(a) + " je prvocislo")
                else:
                    print("> " + str(a) + " nie je prvocislo")
        except:
            break

main()
# same as c4-13? 