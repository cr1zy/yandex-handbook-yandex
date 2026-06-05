from itertools import product
n = int(input())
for a, b in product(range(1, n + 1), repeat=2):
    print(a * b, end=' ')
    if b == n:
        print()

# 30 mins