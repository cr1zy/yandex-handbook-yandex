from pathlib import Path

file_name = input()
# для работы на компьютере
file_name = Path(r"D:\code\yandex-handbook-python\txts\3.5") / file_name

counter = 0
with open(file_name, 'rb') as f:
    f.seek(0, 2)
    size = f.tell()
scale = ['Б', 'КБ', 'МБ', 'ГБ', 'ТБ']
weight = 0

while size > 1024 and weight < len(scale):
    weight += 1
    size, overload = divmod(size, 1024)
    size += int(overload > 0)

print(f'{size}{scale[weight]}')