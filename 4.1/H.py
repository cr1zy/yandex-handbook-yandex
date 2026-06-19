def fragments(numbers):
    lst = []
    start = 0
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i+1]:
            lst.append(numbers[start:i+1])
            start = i + 1
    lst.append(numbers[start:])
    return lst
print(fragments([0, 4, 5, -9, -6, 3, 2, 3, 4, 9]))