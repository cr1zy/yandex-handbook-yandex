spisok = set()
while (stroka := input().split()) != []:
    for index in range(len(stroka)):
        if stroka[index] == 'зайка':
            if index > 0:
                spisok.add(stroka[index - 1])
            if index < len(stroka) - 1:
                spisok.add(stroka[index + 1])
for word in sorted(spisok):
    print(word)

# 30 mins