a = 1
b = 5
d = 2
lst = [x for x in range(a, b + (1 if a <= b else -1), 1 if a <= b else -1) if x % d == 0]
print(lst)

# 3 mins