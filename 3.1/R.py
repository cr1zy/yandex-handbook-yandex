number = input()
digit = []
count = []
counter = 0
while number:
    if number[1] == number[0]:
        counter += 1
    else:
        digit.append(number[0])
        count.append(counter)
        counter = 1  
    number = number[1:]
for i in range(len(digit)):
    print(digit[i], count[i])