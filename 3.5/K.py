import json
from pprint import pprint

with open (r"D:\code\yandex-handbook-python\txts\3.5\K numbers.txt", encoding="UTF-8") as file_in:
    lst = [int(number) for line in file_in for number in line.split()]

count = len(lst)
positive_count = sum(1 for x in lst if x > 0)
minimum = min(lst)
maximum = max(lst)
total = sum(lst)
average = round(total / count, 2)

json_dict = {
    "Количество всех чисел": count,
    "Количество положительных чисел": positive_count,
    "Минимальное число": minimum,
    "Максимальное число": maximum,
    "Сумма всех чисел": total,
    "Среднее арифметическое": average
}

with open (r"D:\code\yandex-handbook-python\txts\3.5\K statistics.json", "w", encoding="UTF-8") as file_out:
    json.dump(json_dict, file_out, ensure_ascii=False, indent=2)

with open(r"D:\code\yandex-handbook-python\txts\3.5\K statistics.json", encoding="UTF-8") as file_in:
    records = json.load(file_in)
pprint(records)