def nested_sum(numbers):
    sum = 0
    for list in numbers:
        for n in list:
            sum += n
    return sum

t = [[1, 2], [3], [4, 5, 6]]
print(nested_sum(t))