# first version

counter = 0
for i in range(int(input())):
    env = ''
    while (obj := input()) != 'ВСЁ':
        env += obj
    else:
        if 'зай' in env:
            counter += 1
print(counter)

# flag version
"""
counter = 0
for i in range(int(input())):
    flag = False
    while (obj := input()) != 'ВСЁ':
        if 'зай' in obj:
            flag = True
    if flag:
        counter += 1
print(counter)
"""
