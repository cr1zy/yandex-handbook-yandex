from itertools import count
a, b, c = map(float, input().split())
for value in count(a, c):
    if value > b:
        break
    print(float(round(value, 2)))

