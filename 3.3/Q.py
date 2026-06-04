n = int(input())
lst = []
for i in range(n):
    lst1 = []
    for j in range(n):
        lst1.append((i + 1) * (j + 1))
    lst.append(lst1)
print(lst)

[[(i + 1) * (j + 1) for j in range(n)] for i in range(n)]

