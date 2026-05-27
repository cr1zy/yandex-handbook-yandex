last_number = 0
for i in range(int(input())):
    number = int(input())
    while number:
        last_number += number % 10 
        number //= 10
print(last_number)