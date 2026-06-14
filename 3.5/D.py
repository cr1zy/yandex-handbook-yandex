from sys import stdin
list = []
for line in stdin:
    list.append(line.rstrip('\n'))
search = list.pop()
for i in list:
    if search.lower() in str(i).lower():
        print(i)
        