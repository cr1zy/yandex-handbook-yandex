from sys import stdin
first = []
second = []
for line in stdin:
    buffer = line.split()
    first.append(int(buffer[1]))
    second.append(int(buffer[2]))
print(round(sum(second) / len(second) - sum(first) / len(first)))