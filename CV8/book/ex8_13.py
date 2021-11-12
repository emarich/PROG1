# 8.1 - read docs of the string methods

# 8.2
# print("banana".count('a'))

# 8.3 - string slice
# print("banana"[5])
# print("banana"[0:5])
# print("banana"[0:5:2])

# 8.4 -  only check code in book

# 8.5
def rotate_word(string, rotate):
    newString = ""
    for c in string:
        c = chr(ord(c) + rotate) # ord() convert char to unicode
        newString += c
    return newString
print(rotate_word("cheer", 7))