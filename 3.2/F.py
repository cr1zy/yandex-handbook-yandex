m_count = int(input())
o_count = int(input())
kids = dict()
list_kids = []
for i in range(m_count + o_count):
    kid = input()
    if kid not in kids:
        kids[kid] = 1
    else:
        del kids[kid]
for key in kids.keys():
    list_kids.append(key)
list_kids.sort()
if len(list_kids) == 0:
    print('Таких нет')
else:
    for i in list_kids:
        print(i)

# 10 mins