import json
from sys import stdin
from pathlib import Path

request = ' '.join(input().lower().split())
Flag = True

for answer in stdin:
    file_name = answer.rstrip("\n")
    # для работы на компьютере
    file_name = Path(r"D:\code\yandex-handbook-python\txts\3.5") / file_name
    with open(file_name, encoding="UTF-8") as file_in:
        lst = []
        for line in file_in:
            line = ' '.join(line.lower().split())
            if line:
                lst.append(line)
        text = ' '.join(lst)
        if request in text:
            Flag = False
            print(file_name)
if Flag:
    print('404. Not Found')