sum_number = ''
for i in range(int(input())):
    number = int(input())
    best_number = 0
    while number:
        last_number = number % 10 
        number //= 10
        if last_number > best_number:
            best_number = last_number
    sum_number += str(best_number)
print(sum_number)