count = int(input())
kids = dict()
list = []
Flag = True
for i in range(count):
    kid = input()
    if kid not in kids:
        kids[kid] = 1
    else:
        kids[kid] += 1
for key, value in kids.items():
    if value != 1:
        list.append(f'{key} - {value}')
        Flag = False
if Flag:
    print('Однофамильцев нет')
else:
    list.sort()
    for i in list:
        print(i)

# 15 mins