from itertools import combinations

values = list(combinations([input() for i in range(int(input()))], 2))
for first, second in values:
    print(f'{first} - {second}')

# 10 mins