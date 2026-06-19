def find_mountains(heights):
    if not heights:
        return []
    lst = []
    for i in range(len(heights) - 2):
        if heights[i] < heights[i + 1] > heights[i + 2]:
            lst.append(i + 2)
    return tuple(lst)
print(find_mountains([1, 2, 1, 4, 1]))