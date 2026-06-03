menu = set()
for i in range(int(input())):
    menu.add(input())
bludas = set()
for i in range(int(input())):
    for i in range(int(input())):
        bludas.add(input())
actual = menu - bludas
list = []
for i in actual:
    list.append(i)
list.sort()
if list:
    for i in list:
        print(i)
else:
    print('Готовить нечего')

# 15 mins

