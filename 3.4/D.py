from itertools import accumulate
for string in accumulate([word + ' ' for word in input().split()]):
    print(string)

# 20 mins