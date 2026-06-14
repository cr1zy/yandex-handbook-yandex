lst = []
with open(r"D:\code\yandex-handbook-python\txts\3.5\I first.txt", encoding="UTF-8") as file_in:
    for line in file_in:
        line = ' '.join(line.split())
        if line:
            lst.append(line)

with open(r"D:\code\yandex-handbook-python\txts\3.5\I second.txt", "w", encoding="UTF-8") as file_out:
    file_out.write(
        '\n'.join(lst)
    )