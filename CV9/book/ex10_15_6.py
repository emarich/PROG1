def is_anagram(s1, s2):
    s1 = sorted(s1)
    s2 = sorted(s2)
    if (s1 == s2):
        return True
    else:
        return False

print(is_anagram("repa", "pera"))