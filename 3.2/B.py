first = set(input())
second = set(input())
s_intersection = first & second
s = ''
for i in s_intersection:
    s += i
print(s)

# 2 mins 