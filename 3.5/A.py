from sys import stdin

summa = 0
for line in stdin.readlines():
    for item in line.split():
        summa += int(item)

print(summa)