count = int(input())
kids = dict()
for i in range(count):
    kid = input()
    if kid not in kids:
        kids[kid] = 1
    else:
        kids[kid] += 1
counter = 0
for value in kids.values():
    if value != 1:
        counter += value
print(counter)

# 5 mins