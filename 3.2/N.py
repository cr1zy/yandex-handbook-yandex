ingradients = set()
for i in range(int(input())):
    ingradients.add(input())
bludas = set()
can_make = []
for i in range(int(input())):
    name = input()
    for i in range(int(input())):
        bludas.add(input())
    if bludas <= ingradients:
        can_make.append(name)
    bludas.clear()
can_make.sort()
if can_make:
    for i in can_make:
        print(i)
else:
    print('Готовить нечего')

# 5 mins