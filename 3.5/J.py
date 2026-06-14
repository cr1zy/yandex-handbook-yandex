str_numbers = int(input())
with open(r"D:\code\yandex-handbook-python\txts\3.5\J some_file.txt", encoding="UTF-8") as file_in:
    lst = [line.rstrip("\n") for line in file_in][-str_numbers:]
with open(r"D:\code\yandex-handbook-python\txts\3.5\J some_file_edited.txt", "w", encoding="UTF-8") as file_out:
    file_out.write('\n'.join(lst))
for i in lst:
    print(i)