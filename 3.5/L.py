with open (r"D:\code\yandex-handbook-python\txts\3.5\L numbers.txt", encoding="UTF-8") as file_in:
    strings = [string for string in file_in.read().split("\n") if string]

    evens_strings = []
    odds_strings = []
    equals_strings = []

    for line in strings:
        evens, odds, equals = [], [], []
        for number in line.split():
            count_even = 0
            count_odd = 0
            for digit in number:
                if (int(digit) % 2) == 0:
                    count_even += 1
                else:
                    count_odd += 1
            if count_even > count_odd:
                evens.append(number)
            elif count_even < count_odd:
                odds.append(number)
            else:
                equals.append(number)
        evens_strings.append(' '.join(evens) + '\n')
        odds_strings.append(' '.join(odds) + '\n')
        equals_strings.append(' '.join(equals) + '\n')
    with open (r"D:\code\yandex-handbook-python\txts\3.5\L evens", "w", encoding="UTF-8") as file_out:
        file_out.writelines(evens_strings)
    with open (r"D:\code\yandex-handbook-python\txts\3.5\L odds", "w", encoding="UTF-8") as file_out:
        file_out.writelines(odds_strings)
    with open (r"D:\code\yandex-handbook-python\txts\3.5\L equals", "w", encoding="UTF-8") as file_out:
        file_out.writelines(equals_strings)
            