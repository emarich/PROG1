# ex 7.2 book page 69
def eval_loop():
    while True:
        inpt = input("What should python EVALuates? (To end this, type \'done\')\n\t> ")
        if (inpt == "done"):
            return
        print("", end="\t  ")
        print(eval(inpt), end="\n\n")

eval_loop()