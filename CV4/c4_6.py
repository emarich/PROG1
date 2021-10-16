def pocet_rovnakych(a, b, c):
    arr = [a, b, c]
    same = max(arr, key=arr.count)
    return 0 if same == 1 else same 
 
print(pocet_rovnakych(1, 3, 2))
