from itertools import permutations

values = list(permutations(sorted(input() for i in range(int(input())))))
for i in values:
    print(', '.join(i))
    
# 10 mins