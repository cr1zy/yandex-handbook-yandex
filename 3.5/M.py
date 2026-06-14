import json
from sys import stdin
from pathlib import Path

file_name = input()
# для работы на компьютере
# file_name = Path(r"D:\code\yandex-handbook-python\txts\3.5") / file_name


with open(file_name, encoding="UTF-8") as file_in:
    records = json.load(file_in)

lines = [line.rstrip('\n') for line in stdin.readlines()]

for line in lines:
    if line:
        key, value = line.split('==')
        records[key.strip()] = value.strip()


with open(file_name, 'w', encoding="UTF-8") as file_out:
    json.dump(records, file_out, ensure_ascii=False, indent=2)