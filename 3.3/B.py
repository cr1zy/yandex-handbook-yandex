a = 5
b = -4
lst = [x ** 2 for x in range(a, b + (1 if a <= b else -1), 1 if a <= b else -1)]
print(lst)

# 15 mins