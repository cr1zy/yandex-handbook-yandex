count = 0
for i in range(int(input())):
    number = int(input())
    is_prime = True
    if number < 2:
        is_prime = False
    else: 
        for divisor in range(2, int(number ** 0.5) + 1):
            if number % divisor == 0:
                is_prime = False
                break
    if is_prime:
        count += 1
print(count)