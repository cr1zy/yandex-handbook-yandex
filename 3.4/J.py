from itertools import product

n = int(input())

values = list(product(range(1, n + 1), repeat=2))
print('А Б В')
for a, b in values:
    if (a + b) < n:
        print(a, b, n - a - b)

# 15 mins