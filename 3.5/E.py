from sys import stdin
list = sorted({word for line in stdin for word in line.rstrip('\n').split() if word.lower() == word.lower()[::-1]})
for i in list:
    print(i)