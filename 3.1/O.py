str_numbers = input().split()
for i in range(len(str_numbers)):
    a = int(str_numbers[0])
    b = int(str_numbers[i])
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    else:
        a += b
    str_numbers[0] = a
print(a)

# 15 mins