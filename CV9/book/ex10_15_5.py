def is_sorted(list):
    for i in range(len(list)-1):
        if (list[i] > list[i+1]):
            return False
    return True

t = [1,2,3,2]
print(is_sorted(t))