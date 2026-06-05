from itertools import accumulate
x = input().split()
for value in x:
    value += ' '
for value in accumulate(x):
    print(f'{value}')

# Вывод:
# 1, 3, 6, 10, 15
# from itertools import accumulate
# for string in accumulate([word + ' ' for word in input().split()]):
#     print(string)

# 20 mins