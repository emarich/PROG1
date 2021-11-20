def sumLocalMax(list):
    sum = 0
    for i in range(1, len(list)-1):
        if (list[i-1] < list[i] > list[i+1]):
            sum += list[i]
    return sum

t = [1,2,1,4,3,4,5]
print(sumLocalMax(t))