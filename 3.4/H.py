from itertools import cycle
lst = [input() for i in range(int(input()))]
for _, letter in zip(range(int(input())), cycle(lst)):
    print(letter)

# 15 mins