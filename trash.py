number = int(input())

col_count = 1
last_number = 1

while last_number <= number:

    for i in range(col_count):

        if last_number > number:
            break

        print(last_number, end=' ')
        last_number += 1

    print()
    col_count += 1