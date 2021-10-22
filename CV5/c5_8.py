# book page 61 - ex 6.3
def is_palidrome(word):
    word = "".join(word.split())
    l = len(word)
    if (l > 1):
        return is_palidrome(word[1: -1]) if word[0] == word[-1] else False
    elif (l == 1):
        return True
    elif (l == 0):
        return True

print(is_palidrome("jelenovi pivo nelej"))