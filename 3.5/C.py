from sys import stdin

lines = []
for line in stdin:
    line = line.rstrip('\n')
    index = line.find('#')
    if index == 0:
        continue
    if index > 0:
        print(line[:index])
    else:
        print(line)