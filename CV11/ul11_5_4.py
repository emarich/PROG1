def someIntervalNotIntersecting(t: list(list())) -> bool:
    for i in range(len(t)):
        for j in range(i+1, len(t)):
            if (not (max(t[j][0], t[i][0]) < min(t[j][1], t[i][1]))):
                return True
            else:
                break
    return False

t = [[1,4],[3,5],[4,6]]
print(someIntervalNotIntersecting(t))