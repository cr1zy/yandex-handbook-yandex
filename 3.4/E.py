# lst = sorted(x for i in range(3) for x in input().split(', '))
# print(lst)

for index, value in enumerate(sorted(x for i in range(3) for x in input().split(', ')), 1):
    print(f"{index}. {value}")