from pathlib import Path

file_name = input()
# для работы на компьютере
file_name = Path(r"D:\code\yandex-handbook-python\txts\3.5") / file_name


with open(file_name, encoding='UTF-8') as file_in:
    for line in file_in:
        text = line.rstrip('\n')
        text_new = ''
        for i in text:
            text_new += chr(ord(i) % 256)
        print(text_new)


