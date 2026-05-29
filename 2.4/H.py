best_summ = 0
best_name = ''
for i in range(int(input())):
    name = input()
    number = int(input())
    sum_number = 0
    while number:
        sum_number += number % 10 
        number //= 10
    if sum_number >= best_summ:
        best_summ = sum_number
        best_name = name
print(best_name)