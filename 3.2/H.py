kids = dict()
list_kids = []
for i in range(int(input())):
    name, *food = input().split()
    kids[name] = food
request = input()
for kid in kids:
    if request in kids[kid]:
        list_kids.append(kid)
list_kids.sort()
if len(list_kids) == 0:
    print('Таких нет')
else:
    for i in list_kids:
        print(i)