from itertools import permutations

values = list(permutations(sorted(input() for i in range(int(input()))), 3))
for i in values:
    print(', '.join(i))

# 2 mins