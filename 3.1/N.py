str_numbers = input().split()
level = int(input())
for i in range(len(str_numbers)):
    str_numbers[i] = str(int(str_numbers[i]) ** level)
print(' '.join(str_numbers))

# 25 mins