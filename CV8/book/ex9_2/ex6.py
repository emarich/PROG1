def is_abecedarian(word):
    word = word.lower()
    for i in range(len(word) - 1):
        if (ord(word[i]) > ord(word[i+1])):
            return False
    return True

print(is_abecedarian("bene"))