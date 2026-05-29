quantity = int(input())
count = 0
for i in range(quantity):
    word = input()
    if word[0] in 'абв':
        count += 1
if count == quantity:
    print('YES')
else:
    print('NO')