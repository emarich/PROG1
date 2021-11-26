from ex10_15_10 import in_bisect

def reverse_pair(word_list, word):
    """Checks whether a reversed word appears in word_list.
    word_list: list of strings
    word: string
    """
    rev_word = word[::-1]
    return in_bisect(word_list, rev_word)
        

l = ["aha", "aligator", "barak", "byk", "cecilia", "gekon", "xylofon", "zase"]
    
for word in l:
    if reverse_pair(l, word):
        print(word, word[::-1])

